'''
Parse Makefiles to the extent we need to parse them.  We use simple manual rules
for the obvious, easy stuff, but fall back to some pyparsing help to try and
avoid screwing up things that could be screwed up (and provide a potential
future basis for expansion).  The only thing we actually claim to probably get
right is simple variable assignment with simple variable expansion.  No
function calls, etc.
'''

from pyparsing import *

dollar = Suppress('$')
lbrace = Suppress('(')
rbrace = Suppress(')')
lparen = Suppress('{')
rparen = Suppress('}')

colon = Literal(':')
double_colon = Literal('::')
comma = Literal(',')
semicolon = Literal(';')

assign = Literal('=')
cond_assign = Literal('?=')
immed_assign = Literal(':=')
add_assign = Literal('+=')

override = Literal('override')

body = Forward()

var_name = Word(alphas + '_', alphanums + '-_')
gen_word = (Word(alphanums + '/-_*.%@:') |
            quotedString | dblQuotedString |
            comma | Literal('|') | Literal('>') | semicolon)

var_ref = Forward()
var_expr = (var_name + Optional(body)) | var_ref('ref') 
var_ref << Group(dollar + ((lbrace + var_expr + rbrace) |
                    (lparen + var_expr + rparen)))

body_word = gen_word | var_ref('ref')
body << OneOrMore(body_word)

var_def = Optional(override) + Group(OneOrMore(var_name('name') +
                (assign | cond_assign | immed_assign | add_assign)('operator')) +
                Group(ZeroOrMore(body_word))('values'))

var_statement = Group(var_ref('ref'))('statement')

filename = Word(alphanums + './_', alphanums + './_-')
target = (var_ref + Optional(filename)) | filename

rule = (OneOrMore(target) + (double_colon | colon) + ZeroOrMore(target) +
        Optional(semicolon + OneOrMore(target))) 

wotsit = (var_def('def') | var_statement | rule('rule')) + stringEnd 

class Makefile(object):
    def __init__(self):
        self.vars = {}
    
    CONDITIONALS = set(['ifdef', 'ifeq', 'ifndef', 'ifneq', 'else', 'endif'])
    
    # technically we could just assume these, but hey...
    FUNCTIONS = set(
                ['abspath', 'addprefix', 'addsuffix', 'and', 'basename', 'call',
                 'dir', 'error', 'eval', 'filter', 'filter-out', 'findstring',
                 'flavor', 'foreach', 'if', 'info', 'join', 'lastword',
                 'notdir', 'or', 'origin', 'patsubst', 'realpath', 'shell',
                 'strip', 'sort', 'subst', 'suffix', 'value', 'warning',
                 'wildcard', 'word', 'wordlist', 'words'])
    
    def parse(self, path):
        f = open(path, 'rU')
        
        continuing = False
        prev_lines = None
        in_rule = False
        for line in f:
            line = line[:-1]
            
            # for line continuation junk, don't actually process things until
            #  we have the whole effective line
            if continuing:
                line = prev_lines + ' ' + line
            if line.endswith('\\'):
                continuing = True
                prev_lines = line[:-1]
                continue
            else:
                continuing = False
                prev_lines = None

            # ignore comments
            if line.startswith('#'):
                continue

            if ' ' in line:
                first_word = line[:line.find(' ')]
            else:
                first_word = line
            
            # ignore control-flow
            if first_word in self.CONDITIONALS:
                continue
            # uh, I guess ignore 'include' for now too...
            if first_word == 'include':
                continue
            # we don't care about exporting yet either
            if first_word == 'export':
                continue
            # bail on gibberish statements
            if first_word in ('$(warning', '$(error', '$(info'):
                continue
            
            if in_rule and not line.startswith('\t'):
                in_rule = False
            # ignore rules
            if in_rule:
                continue
            
            if len(line) == 0:
                continue
            
            print 'trying:', line
            p = wotsit.parseString(line)
            if p.getName() == 'rule':
                in_rule = True
            print ' name:', p.getName()
            print '  parsed as', p.asXML()
            
if __name__ == '__main__':
    m = Makefile()
    m.parse('/home/visbrero/rev_control/mozilla-cvs/client.mk')
