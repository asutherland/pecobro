
import codecs

try:
    import cStringIO as StringIO
except:
    import StringIO

import antlr3
# relative
from JavaScriptLexer import JavaScriptLexer
from JavaScriptParser import JavaScriptParser

import pecobro.mozpreproc as mozpreproc
import pecobro.consts as consts

def scan_and_proc(source_file, ast, depth=0):
    for iChild in range(ast.getChildCount()):
        child = ast.getChild(iChild)
        
        #print '[%s%s]' % ('  ' * depth, child.token.text)
        
        if child.token.text == 'FUNC':
            funcNode = child.getChild(0)
            
            funcName = funcNode.token.text
            
            if funcName is None:
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
            scan_and_proc(source_file, child, depth+1)

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
    except:
        pass
