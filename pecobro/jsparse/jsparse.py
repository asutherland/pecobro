
import codecs

try:
    import cStringIO as StringIO
except:
    import StringIO

import antlr3
# relative
from JavaScriptLexer import JavaScriptLexer, ANONYMOUS, PROP
from JavaScriptParser import JavaScriptParser

import pecobro.mozpreproc as mozpreproc
import pecobro.consts as consts

def scan_and_proc(source_file, ast, depth=0, cur_property=None, prop_type=None):
    for iChild in range(ast.getChildCount()):
        child = ast.getChild(iChild)
        
        print '[%s%s]' % ('  ' * depth, child.token.text)
        
        if child.token.text == 'FUNC':
            funcNode = child.getChild(0)
            
            if funcNode.getType() != ANONYMOUS:
                funcName = funcNode.token.text
            elif cur_property:
                print 'assigning name %s to anonymous func' % (cur_property,)
                funcName = cur_property.token.text
                
                if prop_type and prop_type.getType() != PROP:
                    print 'considering prop magic', prop_type
                    funcName = prop_type.token.text + '_' + funcName
                
                # this is probably not the best way to fix our position problem
                funcNode = cur_property
            else:
                print 'skipping anonymous func at depth %d' % (depth,)
                continue
            
            func = source_file.get_or_create_function(funcName)
            
            func.source_line = funcNode.token.line
            func.source_col  = funcNode.token.charPositionInLine
            
            source_file.contents.append(func)
            
            #print '%s(%d, %d): %s' % ('  ' * depth,
            #                          func.source_line, func.source_col,
            #                          funcName)
        elif child.token.text == 'OBJ':
            scan_and_proc(source_file, child, depth+1)
        elif child.token.text == 'PROP':
            scan_and_proc(source_file, child, depth+1,
                          cur_property=child.getChild(0),
                          prop_type=child.getChild(1))

def parse_file(fname):
    f_in = codecs.open(fname, 'r', 'utf-8')
    f_out = StringIO.StringIO()
    mozpreproc.preprocess(includes=[f_in], defines=consts.defines,
                          output=f_out,
                          line_endings='lf')
    f_in.close()
    f_out.seek(0)
    
    #f = open(fname, 'r')
    ss = antlr3.StringStream(f_out.getvalue())
    #f.close()
    #ss = antlr3.ANTLRFileStream(f_out)
    lexer = JavaScriptLexer(ss)
    token_stream = antlr3.CommonTokenStream(lexer)
    parser = JavaScriptParser(token_stream)
    z = parser.program()
    
    return z

def parse_and_proc(fname):
    ast = parse_file(fname)
    import pecobro.core as pcore
    source_file = pcore.SourceFile(fname)
    return scan_and_proc(source_file, ast.tree)

def sf_process(source_file):
    try:
        ptree = parse_file(source_file.path)
        scan_and_proc(source_file, ptree.tree)
    except Exception, e:
        #print '*** EXCEPTION', e
        pass
