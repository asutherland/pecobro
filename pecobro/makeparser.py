'''
Parse Makefiles to the extent we need to parse them.  We use simple manual rules
for the obvious, easy stuff, but fall back to some pyparsing help to try and
avoid screwing up things that could be screwed up (and provide a potential
future basis for expansion).  The only thing we actually claim to probably get
right is simple variable assignment with simple variable expansion.  No
function calls, etc.
'''

class Context(object):
    '''
    Exists so that we can change between error-on-nonexistent and silent-empty.
    Arbitrarily chosen in
    '''
    def __init__(self):
        self.values = {}
    
    def __setitem__(self, name, value):
        self.values[name] = value
    
    def __getitem__(self, name):
        return self.values.get(name, EMPTY_STRING)

class Literal(object):
    def __init__(self, value):
        self.value = value
    
    def evalInContext(self, context):
        return self.value
    
    def __add__(self, other):
        if isinstance(other, Literal):
            return Literal(self.value + other.value)
        else:
            return ComplexString([self, other])
    
    def __cmp__(self, other):
        if isinstance(other, basestring):
            return cmp(self.value, other)
        return False
    
    def __str__(self):
        return self.value
    
EMPTY_STRING = Literal('')

class VarRef(object):
    def __init__(self, node):
        self.node = node
    
    def evalInContext(self, context):
        var_name = self.node.evalInContext(context)
        return context[var_name].evalInContext(context)
    
    def __add__(self, other):
        return ComplexString([self, other])
    
    def __str__(self):
        return '$(%s)' % (self.node,)

class ComplexString(object):
    def __init__(self, nodes):
        self.nodes = nodes
    
    def evalInContext(self, context):
        return ''.join(map(lambda x: x.evalInContext(context), self.nodes))
    
    def __add__(self, other):
        if isinstance(other, ComplexString):
            self.nodes.extend(other.nodes)
        else:
            self.nodes.append(other)
        return self
    
    def __str__(self):
        return '+'.join(map(str, self.nodes))

class Makefile(object):
    def __init__(self, values={}):
        self.context = Context()
        
        for key, value in values.items():
            self.context[key] = Literal(value)
    
    CONDITIONALS = set(['ifdef', 'ifeq', 'ifndef', 'ifneq', 'else', 'endif'])
    
    # technically we could just assume these, but hey...
    FUNCTIONS = set(
                ['abspath', 'addprefix', 'addsuffix', 'and', 'basename', 'call',
                 'dir', 'error', 'eval', 'filter', 'filter-out', 'findstring',
                 'flavor', 'foreach', 'if', 'info', 'join', 'lastword',
                 'notdir', 'or', 'origin', 'patsubst', 'realpath', 'shell',
                 'strip', 'sort', 'subst', 'suffix', 'value', 'warning',
                 'wildcard', 'word', 'wordlist', 'words'])
    
    def _parseOneFileThing(self, s, stopAtWhitespace=True):
        acc = ''
        just_saw_dollar = False
        var_stack = []
        cur_nodes = []
        i = -1
        for i, c in enumerate(s):
            if just_saw_dollar:
                if c == '$':
                    acc += '$'
                elif c in ('(', '{'):
                    if c == '(':
                        term_c = ')'
                    else:
                        term_c = '}'
                    if acc:
                        cur_nodes.append(Literal(acc))
                        acc = ''
                    var_stack.append((term_c, cur_nodes))
                    cur_nodes = []
                else:
                    # single-letter value
                    cur_nodes.append(VarRef(c))
                just_saw_dollar = False
            else:
                if c == '$':
                    just_saw_dollar = True
                elif var_stack and c == var_stack[-1][0]:
                    if acc:
                        cur_nodes.append(Literal(acc))
                        acc = ''
                    if len(cur_nodes) > 1:
                        var_node = VarRef(ComplexString(cur_nodes))
                    else:
                        var_node = VarRef(cur_nodes[0])
                    cur_nodes = var_stack.pop()[1]
                    cur_nodes.append(var_node)
                elif var_stack:
                    acc += c
                elif c == ' ' and stopAtWhitespace:
                    break
                else:
                    acc += c

        if acc:
            cur_nodes.append(Literal(acc))
        
        if len(cur_nodes) > 1:
            return ComplexString(cur_nodes), s[i+1:].lstrip()
        elif cur_nodes:
            return cur_nodes[0], s[i+1:].lstrip()
        else:
            return EMPTY_STRING, s[i+1:].lstrip()
    
    def parse(self, path):
        f = open(path, 'rU')
        context = self.context
        
        SPACE_LITERAL = Literal(' ')
        
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
            
            line = line.lstrip()
            
            file_things = []
            pre_gobble_line = line
            while line and line[0] not in ':?+=':
                file_thing, line = self._parseOneFileThing(line)
                file_things.append(file_thing)
            
            if (line.startswith('=') or line.startswith(':=') or
                    line.startswith('+=') or line.startswith('?=')):
                if line[0] == '=':
                    line = line[1:].lstrip()
                    action = '='
                else:
                    action = line[0]
                    line = line[2:].lstrip()
                value, trash = self._parseOneFileThing(line, False)
                #print 'found a variable statement...', pre_gobble_line
                #print '  ', file_things[0], '=', value
                
                if file_things[0] == 'override':
                    del file_things[0]
                if file_things[0] == 'export':
                    del file_things[0]
                if len(file_things) > 1:
                    print '***', pre_gobble_line
                    print '===', map(str,file_things)
                    raise Exception('Multiple file things for an assignment...')
                
                name = file_things[0].evalInContext(context)
                if action == '=':
                    context[name] = value
                elif action == '+':
                    context[name] = context[name] + SPACE_LITERAL + value
                elif action == ':':
                    value = Literal(value.evalInContext(context))
                    context[name] = value
                elif action == '?':
                    if name not in self.context.values:
                        context[name] = value
                
                #print '   now equals...', context[name].evalInContext(context)
                
            elif line.startswith(':'):
                in_rule = True
                #print 'found a rule...', pre_gobble_line
    
    def get(self, name):
        return self.context[name].evalInContext(self.context)
    
    def dump(self):
        for key in self.context.values:
            print '%s: %s' % (key, self.context[key].evalInContext(self.context))
            
if __name__ == '__main__':
    m = Makefile()
    m.parse('/home/visbrero/rev_control/mozilla-cvs/client.mk')
    #m.dump()
    print m.get('MODULES_mail').split()
