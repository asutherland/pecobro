# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is the "pecobro" Peformance Code Browser.
#
# The Initial Developer of the Original Code is
# Mozilla Messaging, Inc.
# Portions created by the Initial Developer are Copyright (C) 2008
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Andrew Sutherland <asutherland@asutherland.org>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import codecs, os, os.path

try:
    import cStringIO as StringIO
except:
    import StringIO

try:
    import cerealizer
except:
    cerealizer = None

import antlr3
# relative
from JavaScriptLexer import JavaScriptLexer, ANONYMOUS, CALL, \
    FUNC, \
    PROP
from JavaScriptParser import JavaScriptParser

import pecobro.mozpreproc as mozpreproc
import pecobro.consts as consts

import pecobro.jsparse.jsgrok as jsgrok

def _anon_func_name(funcNode, adj_line, adj_column):
    return 'anon:%d:%d' % (funcNode.token.line + adj_line,
                           funcNode.token.charPositionInLine +
                           ((funcNode.token.line == 1) and 
                           adj_column or 0))

def _make_func(source_file, funcNode, funcName, astNode,
               adj_line, adj_column):
    func_line = funcNode.token.line + adj_line 
    
    func, created = source_file.get_or_create_function(funcName, func_line)
    
    func.source_line = func_line
    func.source_col  = funcNode.token.charPositionInLine
    # only adjust the column if it is the first line...
    if funcNode.token.line == 1:
        func.source_col += adj_column
    
    func.ast = astNode
    
    source_file.add_to_contents(func)

    print '     (%d, %d): %s' % (func.source_line, func.source_col, funcName)
   
    return func

def scan_and_proc(source_file, ast, depth=0,
                  cur_property=None, prop_type=None,
                  report=True, adj_line=0, adj_column=0):
    '''
    Chew the AST and put info in our core representation.  This type of
    analysis is going to migrate into jsgrok; at some point this should become
    moot...
    '''
    if ast is None:
        print '*** WARNING, null AST for %s' % (source_file,)
        return
    for iChild in range(ast.getChildCount()):
        child = ast.getChild(iChild)
        
        if report:
            print '[%.4d %s%s]' % (child.token.line and
                                   (child.token.line+adj_line) or 0,
                                   '  ' * depth, child.token.text)
        
        # explicitly process functions
        if child.getType() == FUNC:
            funcNode = child.getChild(0)
            
            if funcNode.getType() != ANONYMOUS:
                funcName = funcNode.token.text
                # we have to use the cur_property as our funcNode for
                #  positioning because having antlr assign the property name's
                #  token info to ANONYMOUS screws up WHEN WE HAVE A PROPERTY.
                # things are okay in the non-property case (propagation happens
                #  correctly.)
                if cur_property:
                    funcNode = cur_property
            elif cur_property is not None:
                print 'assigning name %s to anonymous func' % (cur_property,)
                funcName = cur_property.token.text
                
                if prop_type and prop_type.getType() != PROP:
                    if report:
                        print 'considering prop magic', prop_type
                    funcName = prop_type.token.text + '_' + funcName
                
                # this is probably not the best way to fix our position problem
                funcNode = cur_property
            else:
                # it's anonymous!
                funcName = _anon_func_name(funcNode, adj_line, adj_column)
            
            func = _make_func(source_file, funcNode, funcName, child,
                              adj_line, adj_column)
                        
            # there might be interesting stuff in here...
            #  but be quiet with the walking so as to avoid being too verbose
            scan_and_proc(source_file, child.getChild(2), depth+1, report=False,
                          adj_line=adj_line, adj_column=adj_column)
        # PROPs provide context for naming
        elif child.getType() == PROP:
            scan_and_proc(source_file, child, depth+1,
                          cur_property=child.getChild(0),
                          prop_type=child.getChild(1),
                          report=report,
                          adj_line=adj_line, adj_column=adj_column)
        # NEW-ing a Function creates a function, but so just CALLing function,
        #  so let's only handle the CALL case and leave it to the NEW case to
        #  recurse into it.
        # (CALL case)
        elif child.getType() == CALL:
            if jsgrok.call_name(child) == 'Function':
                # CALL -> VEXPR -> VARREF -> 'Function'
                funcNode = child.children[0].children[0].children[0]
                # gr, they're creating an anonymous function
                funcName = _anon_func_name(funcNode, adj_line, adj_column)
                funcNode = _make_func(source_file, funcNode, funcName, funcNode,
                                      adj_line, adj_column)

            # recurse no matter what; there could be more functions in there.
            scan_and_proc(source_file, child, depth+1, report=report,
                          adj_line=adj_line, adj_column=adj_column)
        # everything else we simply want to traverse in the hope of finding more
        #  of the above.
        else:
            scan_and_proc(source_file, child, depth+1, report=report,
                          adj_line=adj_line, adj_column=adj_column)
            

def parse_string(s, dude='program'):
    '''
    Intended for debug use.
    '''
    ss = antlr3.StringStream(s)
    lexer = JavaScriptLexer(ss)
    token_stream = antlr3.CommonTokenStream(lexer)
    parser = JavaScriptParser(token_stream)
    duder = getattr(parser, dude)
    z = duder()
    
    return z

TRY_CODECS = ['utf-8', 'cp1252']

def parse_snippet(snippet, kind='program'):
    ss = antlr3.StringStream(snippet)
    lexer = JavaScriptLexer(ss)
    token_stream = antlr3.CommonTokenStream(lexer)
    parser = JavaScriptParser(token_stream)
    if kind in ('program', 'func'):
        z = parser.program()
    elif kind in ('field',):
        z = parser.standaloneExpression()
    
    if z is not None:
        return z.tree
    else:
        return None    

def _parse_file(fname, defines=consts.defines):
    sio = None
    used_codec = None
    for try_codec in TRY_CODECS:
        try:
            f_in = codecs.open(fname, 'r', try_codec)
            sio = StringIO.StringIO()
            f_out = codecs.getwriter('utf-8')(sio)
            mozpreproc.preprocess(includes=[f_in], defines=defines,
                                  output=f_out,
                                  line_endings='lf')
            f_in.close()
            sio.seek(0)
            # if we got here, we are victorious
            used_codec = try_codec
            break
        except Exception, e:
            print '(codec %s failed us, trying next)' % (try_codec,)
            print '  exception was:', e
            f_out = None
    
    if sio is None:
        raise Exception('All our mighty codecs failed us on %s' % (fname,))
    
    #f = open(fname, 'r')
    #ss = antlr3.StringStream(sio.getvalue())
    ss = antlr3.ANTLRInputStream(sio, 'utf-8')
    #f.close()
    #ss = antlr3.ANTLRFileStream(f_out)
    lexer = JavaScriptLexer(ss)
    token_stream = antlr3.CommonTokenStream(lexer)
    parser = JavaScriptParser(token_stream)
    z = parser.program()
    
    return z, used_codec

_CACHE_INITED = False

def _init_cache():
    global _CACHE_INITED
    try:
        registered = set()
        
        def register_class_and_kids(c):
            if c in registered:
                return
            
            cerealizer.register(c)
            
            for key, val in c.__dict__.items():
                if type(val) == type and val not in registered:
                    cerealizer.register(val)
                    registered.add(val)
        
        def register_module(m):
            for key, val in m.__dict__.items():
                if type(val) == type and val not in registered:
                    cerealizer.register(val)
                    registered.add(val)            
        
        import antlr3.tokens, antlr3.streams, antlr3.tree
        register_module(antlr3.tokens)
        register_module(antlr3.streams)
        register_module(antlr3.tree)
        
        # we need to register all the classes...
        register_class_and_kids(JavaScriptLexer)
        register_class_and_kids(JavaScriptParser)
    except Exception, e:
        # this is a debugging thing here mainly... it gets mad about
        #  multiple registrations when I reload things...
        print 'Warning: cache initialization problem:', e
    
    _CACHE_INITED = True

def parse_file(fname, cache_dir=None, force=False, defines=consts.defines):
    '''
    Parse the file, caching if cache_dir is supplied (and valid).
    
    @param cache_dir: Cache directory to use, or None (default) if no cache
        is desired.
    @param force: Force a parse to occur, potentially ignoring an otherwise
        usable cache entry.
    '''
    global _CACHE_INITED
    
    if cerealizer and cache_dir and os.path.exists(cache_dir):
        if not _CACHE_INITED:
            _init_cache()
            
        cache_fname = os.path.join(cache_dir, os.path.basename(fname)+'.cache')
        
        file_ts = os.path.getmtime(fname)
        
        if (os.path.exists(cache_fname) and not force
                and os.path.getmtime(cache_fname) >= file_ts
                and os.path.getsize(cache_fname)):
            # use the cache if we can, but fail-over to a fresh parse if we
            #  somehow fail.
            try:
                f = open(cache_fname, 'rb')
                ast = cerealizer.load(f)
                f.close()
                
                if ast is not None:
                    # okay, returning None as used_codec is not good...
                    # luckily most things are meta-cached, but this could turn
                    #  out very badly...
                    return ast, None
            except:
                pass
        
        ast, used_codec = _parse_file(fname, defines=defines)
        # (no need to try and back-date the mtime to the file's mtime)            
        f = open(cache_fname, 'wb')
        cerealizer.dump(ast, f, protocol=-1) # use highest version
        f.close()
        
        return ast, used_codec
    else:
        return _parse_file(fname)

grokker = jsgrok.JSGrok(None)

def parse_and_proc(fname, cache_dir=None, force=False, defines=consts.defines):
    ast, used_codec = parse_file(fname, cache_dir=cache_dir, force=force,
                                 defines=defines)
    import pecobro.core as pcore
    source_file = pcore.SourceFile(fname, 'js')
    source_file.used_codec = used_codec
    scan_and_proc(source_file, ast.tree)
    grokker.grok_source_file(source_file, ast.tree)
    return source_file

def sf_process_snippet(source_file, code, kind='program',
                       adj_line=0, adj_column=0):
    tree = parse_snippet(code, kind)
    if tree:
        scan_and_proc(source_file, tree, report=False,
                      adj_line=adj_line, adj_column=adj_column)
        if kind == 'func':
            grokker.grok_func(source_file, tree,
                                     adj_line=adj_line, adj_column=adj_column)        
        elif kind == 'field':
            grokker.grok_field(source_file, tree,
                                     adj_line=adj_line, adj_column=adj_column)
    return tree

def sf_process(source_file, cache_dir=None, force=False, defines=consts.defines):
    # Called by generate...
    #try:
        # if the file managed to get fully cached before, load it!
        if cache_dir:
            if not _CACHE_INITED:
                _init_cache()
            meta_cache_fname = os.path.join(cache_dir,
                                            os.path.basename(source_file.path)+
                                                '.mcache')
            if os.path.exists(meta_cache_fname) and not force:
                f = open(meta_cache_fname, 'rb')
                cached_source_file = cerealizer.load(f)
                f.close()
                
                # restore the links we nuked before in order to de-couple the
                #  source_file from any global/caboodle context...
                cached_source_file.caboodle = source_file.caboodle
                
                # evil? perhaps.  easy? you betcha!
                source_file.__dict__ = cached_source_file.__dict__
                
                print 'Restored %s from meta-cache.' % (source_file.path,)
                
                return
    
        ptree, used_codec = parse_file(source_file.path, cache_dir=cache_dir,
                                       force=force, defines=defines)
        source_file.ast = ptree.tree
        source_file.used_codec = used_codec
        scan_and_proc(source_file, ptree.tree, report=False)
        grokker.grok_source_file(source_file, ptree.tree)
        
        if cache_dir:
            # break any global/caboodle links to avoid persisting everything
            saved_caboodle = source_file.caboodle
            source_file.caboodle = None
            
            f = open(meta_cache_fname, 'wb')
            cerealizer.dump(source_file, f, protocol=-1)
            f.close()
            
            # TODO: consider nuking the AST cache...
            
            # restore the global link
            source_file.caboodle = saved_caboodle
        
    #except Exception, e:
    #    print '*** EXCEPTION', e
    #    pass

def dbg_load_cached(filename, cache_dir):
    import pecobro.core as pcore
    source_file = pcore.SourceFile(filename, '')
    sf_process(source_file, cache_dir)
    return source_file

def dbg_reparse(source_file):
    new_sf = parse_and_proc(source_file.path, defines=source_file.defines)
    return new_sf

if __name__ == '__main__':
    from IPython.Shell import IPShellEmbed
    ipshell = IPShellEmbed(['-pdb'])
    import sys
    CACHE_DIR = '/tmp/pecobro_cache/debug'
    sf = dbg_load_cached(sys.argv[1], CACHE_DIR)
    ipshell()
