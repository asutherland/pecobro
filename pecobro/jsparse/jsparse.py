
import antlr3
# relative
from JavaScriptLexer import JavaScriptLexer
from JavaScriptParser import JavaScriptParser

def parse_file(fname):
    f = open(fname, 'r')
    ss = antlr3.StringStream(f.read())
    f.close()
    lexer = JavaScriptLexer(ss)
    token_stream = antlr3.CommonTokenStream(lexer)
    parser = JavaScriptParser(token_stream)
    z = parser.program()
    
    return z