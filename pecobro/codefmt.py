import pygments, pygments.lexer
import pygments.lexers
import pygments.token
import pygments.formatters
import pygments.formatters.html

import pecobro.core as core
import pecobro.vis as vis

class XmlJsFusionLexer(pygments.lexer.Lexer):
    name='XML+JS'
    aliases=['xml+js']
    
    def __init__(self, **options):
        super(XmlJsFusionLexer, self).__init__(**options)
        self.xml_lexer = pygments.lexers.XmlLexer()
        self.js_lexer = pygments.lexers.JavascriptLexer()
    
    CDATA_START = '<![CDATA['
    CDATA_END = ']]>'
    
    def get_tokens_unprocessed(self, text):
        in_relevant_attr = False
        attr_str = None
        attr_start = None
        for xi, xt, xv in self.xml_lexer.get_tokens_unprocessed(text):
            if xt == pygments.token.Comment.Preproc and xv.startswith(self.CDATA_START):
                yield xi, xt, self.CDATA_START
                xxi = xi + len(self.CDATA_START)
                for ji, jt, jv in self.js_lexer.get_tokens_unprocessed(
                        xv[len(self.CDATA_START):-len(self.CDATA_END)]):
                    yield xxi + ji, jt, jv
                xi += len(xv) - len(self.CDATA_END)
                yield xi, xt, self.CDATA_END
            elif in_relevant_attr:
                if attr_start is None:
                    attr_start = xi
                if xt == pygments.token.String:
                    in_relevant_attr = False
                    attr_str += xv
                    
                    if attr_str.startswith('"') or attr_str.startswith("'"):
                        yield_str = attr_str[0]
                        attr_str = attr_str[1:-1]
                    else:
                        yield_str = ''

                    # we want to use Comment.Preproc as the type to serve as a
                    #  helper-cheaty marker to tell our AST-synch code where it
                    #  should adjust its offsets from...
                    if yield_str:
                        yield attr_start, pygments.token.Comment.Preproc, yield_str
                    for ji, jt, jv in self.js_lexer.get_tokens_unprocessed(
                            attr_str):
                        yield attr_start + 1 + ji, jt, jv
                    if yield_str:
                        yield attr_start + 1 + len(attr_str), pygments.token.Comment.Preproc, yield_str
                else:
                    attr_str += xv
            elif xt == pygments.token.Name.Attribute and xv in ('onget=', 'onset='):
                attr_str = ''
                in_relevant_attr = True
                yield xi, xt, xv
            else:
                yield xi, xt, xv
        

class ASTHelper(object):
    def __init__(self, ast):
        self.stack = []
        self.parent = ast
        self.index = -1
        self.node = None

        self.line = 0
        self.pos = -1

        self.advance_ast()

    def push_ast(self):
        self.stack.append((self.parent, self.index))
        self.parent = self.node
        self.index = 0
        self.node = self.parent.getChild(0)
    
    def pop_ast(self):
        if self.stack:
            self.parent, self.index = self.stack.pop()
            return True
        else:
            return False

    def _step_ast(self):
        self.index += 1
        while self.index >= self.parent.getChildCount():
            if not self.pop_ast():
                self.node = None
                return False
            self.index += 1

        self.node = self.parent.getChild(self.index)
        return True
    
    def advance_ast(self):
        # advance the index...
        self._step_ast()
        
        if self.node is None: # this happens when we run out of nodes...
            return
        
        # descend for synthetic tree nodes... (we only descend on synthetic
        #  ones...) skip synthetic nodes that have nothing going on.
        while self.node.token.line == 0:
            if self.node.getChildCount() > 0:
                self.push_ast()
            else:
                if not self._step_ast():
                    return False
        
        self.line = self.node.token.line
        self.pos  = self.node.token.charPositionInLine
        
        return True
    

class CodeFormatter(pygments.formatters.HtmlFormatter):
    '''
    When decorating javascript code, our goal is to know, for each 'raw' token,
    what the corresponding parsed node is.  And from this parsed node we want
    to be able to get to the corresponding semantic object for decoration
    purposes.  The simplest leap is from parsed node to semantic object; we can
    just add an attribute to the parsed node that identifies the semantic
    object.
    
    The harder leap is getting to the parsed node.  We have a few options here,
    some of which may contradict the above:
    - Use the existing Javascript lexer and map to parse nodes (or even
      semantic objects) by having a queue of the relevant semantic objects.
      We could even attempt to be clever by actually using a stack and when we
      hit our given semantic object, pushing its children on.  (We 'hit' things
      by having the token from the pygments lexer's position info match with
      the next thing on the queue.)
    - Create our own lexer/formatter hybrid that actually pushes the info from
      the antlr lexer with additional semantics.  
      
    Additional thoughts:
    - If we want to use antlr as our lexer, we will need to actually keep around
      its token stream (or regenerate it).  Our rewrite rules discard
      information, unless that stuff is secretly still there under the hood.
    - Pygments might not understand the horrible e4x syntax.
    
    Additional questions:
    - What do we do about the XBL files?
      - We have the following info sources:
        - Element Tree... does it maintain location information?
    - What do we do about the stupid preprocessing in the XBL files?
      
    '''
    def __init__(self, **options):
        pygments.formatters.HtmlFormatter.__init__(self, **options)
        
        self.source_file = options.get('source_file')
            
    def wrap(self, source, outfile):
        source = pygments.formatters.HtmlFormatter.wrap(self, source, outfile)
        
        return self._wrap_executed(source)
    
    def _wrap_executed(self, source):
        cur_line = 0
        
        if self.source_file:
            iContents = iter(self.source_file.contents)
        else:
            iContents = iter(())
        
        nextFunc = None
        
        def next_contents():
            try:
                return iContents.next()
            except:
                return None
        nextFunc = next_contents()
        
        for t, line in source:
            if t == 1:
                cur_line += 1
                
                while nextFunc and nextFunc.source_line <= cur_line:
                    if isinstance(nextFunc, core.Func):
                        yield (0,
                               '<span id="func|%s" class="fhdr">%s</span>' %
                                   (nextFunc.norm_name, nextFunc.name))
                        if nextFunc.invocations:
                            yield 0, vis.func_time_slices(nextFunc)
                        yield 0, '\n'
                        if nextFunc.ever_called:
                            display_names = []
                            ever_called_funcs = nextFunc.ever_called.keys()
                            ever_called_funcs.sort(key=lambda x:(x.file.base_name, x.name))
                            for c_func in ever_called_funcs:
                                display_names.append('%s:%s' % (
                                    c_func.file.base_name,
                                    c_func.name))
                            yield (0, '<span class="fc">Called: %s</span>\n' %
                                    (', '.join(display_names),))
                        if nextFunc.ever_called_by:
                            display_names = []
                            ever_called_by_funcs = nextFunc.ever_called_by.keys()
                            ever_called_by_funcs.sort(key=lambda x:(x.file.base_name, x.name))
                            for cb_func in ever_called_by_funcs:
                                display_names.append('%s:%s' % (
                                    cb_func.file.base_name,
                                    cb_func.name))
                            yield (0, '<span class="fcb">Called By: %s</span>\n' %
                                    (', '.join(display_names),))
                    # NOTE: Right now this doesn't actually happen
                    elif isinstance(nextFunc, core.JSObj):
                        yield (0,
                               '<span id="field|%s" class="fhdr">%s</span>' %
                                   (nextFunc.norm_name, nextFunc.name))
                        yield 0, '\n'
                    
                    nextFunc = next_contents()
                
                yield t, line
            else:
                yield t, line
    
    def _format_lines(self, tokensource):
        if self.source_file is None:
            return super(CodeFormatter, self)._format_lines(tokensource)
        else:
            return self._awesome_format_lines(tokensource) 
    
    def _awesome_format_lines(self, tokensource):
        '''
        Replace the HTMLFormatter's core logic... we derive from and
        special-case, which is to say, copy-paste-modify.
        '''

        # holds tuples of (node, cur child index in node)
        ast_line_adjust = 0
        ast_pos_adjust = 0
        sync_ast = False
        if self.source_file.ast:
            multi_ast = False
            ast = ASTHelper(self.source_file.ast)
        else:
            multi_ast = True
            ast = None

        if self.source_file:
            iContents = iter(self.source_file.contents)
        else:
            iContents = iter(())

        nextFunc = None
        
        def next_contents():
            try:
                return iContents.next()
            except:
                return None
        nextFunc = next_contents()

        cur_line = 1
        cur_pos = 0
                
        enc = self.encoding
        lsep = self.lineseparator

        lspan = ''
        line = ''
        for ttype, value in tokensource:
            #print 'TOKEN', cur_line, cur_pos, value
            
            if nextFunc and nextFunc.source_line <= cur_line:
                while nextFunc and nextFunc.source_line <= cur_line:
                    # Because functions may be defined inside of functions, we
                    #  only want to change the AST we are processing if it's
                    #  actually a top-level/authoritative AST (otherwise we
                    #  would need to maintain a stack for when we left a
                    #  function.  This means we ignore nested_ast's (which is
                    #  everyone by default; the XBL parser sets them to False
                    #  when it creates top-level things.)
                    if multi_ast and not nextFunc.nested_ast:
                        # look for our Comment.Preproc marker...
                        sync_ast = True
                        
                        if nextFunc.ast:
                            ast = ASTHelper(nextFunc.ast)
                            #print '************ new AST', ast.line, ast.pos
                        else:
                            ast = None
                            
                    nextFunc = next_contents()
            elif ttype == pygments.token.Comment.Preproc and sync_ast:
                # ast line is one-based, so we need to subtract one off for the
                #  adjustment.  (sort of like point/vector reps from lin. alg.) 
                ast_line_adjust = cur_line - 1
                ast_pos_adjust = cur_pos + len(value)
                #print '>>> synced', ast_line_adjust, ast_pos_adjust
                sync_ast = False

#            if ast and ast.node and not sync_ast:
#                print '  (next:', ast.node.token.text, ast.line, ast.pos, ast_line_adjust, ast_pos_adjust, ')'

            # -- translate to semantic meaning...
            if (ast and ast.node and not sync_ast and
                    cur_line >= (ast.line + ast_line_adjust) and
                    cur_pos >= (ast.pos + ast_pos_adjust)):
#                print '  (pyg %d,%d ast %d,%d (adjusted %d,%d))' % (cur_line, cur_pos,
#                                                   ast.line+ast_line_adjust,
#                                                   ast.pos+ast_pos_adjust,
#                                                   ast_line_adjust,
#                                                   ast_pos_adjust)
#                print '  ast:', ast.node
                
                nodes = []
                
                while (cur_line >= (ast.line + ast_line_adjust) and
                        cur_pos >= (ast.pos + ast_pos_adjust)):
                    nodes.append(ast.node)
                    if not ast.advance_ast():
                        break
                
                #print '  traversed:', len(nodes)
            
            # -- semantic cleanup --     
            cls = self._get_css_class(ttype)
            cspan = cls and '<span class="%s">' % cls or ''
            
            if enc:
                value = value.encode(enc)
            fake_parts = value.split('\n')
            if len(fake_parts) > 1:
                cur_line += len(fake_parts) - 1
                ast_pos_adjust = 0
                # zero-based!
                cur_pos = len(fake_parts[-1])
            else:
                cur_pos += len(fake_parts[-1]) 
            parts = pygments.formatters.html.escape_html(value).split('\n')
            
            # these are all full lines
            for part in parts[:-1]:
                if line:
                    if lspan != cspan:
                        line += (lspan and '</span>') + cspan + part + \
                                (cspan and '</span>') + lsep
                    else: # both are the same
                        line += part + (lspan and '</span>') + lsep
                    yield 1, line
                    line = ''
                elif part:
                    yield 1, cspan + part + (cspan and '</span>') + lsep
                else:
                    yield 1, lsep
            # this is not a full line (and may be empty)
            if line and parts[-1]:
                if lspan != cspan:
                    line += (lspan and '</span>') + cspan + parts[-1]
                    lspan = cspan
                else:
                    line += parts[-1]
            elif parts[-1]:
                line = cspan + parts[-1]
                lspan = cspan
            # else we neither have to open a new span nor set lspan

        if line:
            yield 1, line + (lspan and '</span>') + lsep
                    