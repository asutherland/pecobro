'''
Parse Makefiles to the extent we need to parse them.  We use simple manual rules
for the obvious, easy stuff, but fall back to some pyparsing help to try and
avoid screwing up things that could be screwed up (and provide a potential
future basis for expansion).  The only thing we actually claim to probably get
right is simple variable assignment with simple variable expansion.  No
function calls, etc.
'''

import os.path

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
    
    def eval(self, name):
        return self[name].evalInContext(self)

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
        return '"%s"' % (self.value,)
    
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
        return '[' + '+'.join(map(str, self.nodes)) + ']'

class Makefile(object):
    def __init__(self, values={}):
        self.context = Context()
        
        self.makefile_stack = []
        
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
    
    def _parseOneFileThing(self, s, stopAtWhitespace=True, whitespace=' \t'):
        acc = ''
        just_saw_dollar = False
        var_stack = []
        cur_nodes = []
        i = -1
        term_char = None
        for i, c in enumerate(s):
            if just_saw_dollar:
                if c == '$':
                    acc += '$'
                elif c in ('(', '{'):
                    if c == '(':
                        term_c = ')'
                    else:
                        term_c = '}'
                    # save any existing literal string at this stack depth
                    if acc:
                        cur_nodes.append(Literal(acc))
                        acc = ''
                    # push a new node list...
                    var_stack.append((term_c, cur_nodes))
                    cur_nodes = []
                else:
                    if acc:
                        cur_nodes.append(Literal(acc))
                        acc = ''                    
                    # single-letter value
                    cur_nodes.append(VarRef(Literal(c)))
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
                elif c in whitespace and stopAtWhitespace:
                    term_char = c
                    break
                else:
                    acc += c

        if acc:
            cur_nodes.append(Literal(acc))
        
        if len(cur_nodes) > 1:
            return ComplexString(cur_nodes), s[i+1:].lstrip(), term_char
        elif cur_nodes:
            return cur_nodes[0], s[i+1:].lstrip(), term_char
        else:
            return EMPTY_STRING, s[i+1:].lstrip(), term_char
    
    def parse(self, path):
        self.makefile_stack.append(path)
        
        f = open(path, 'rU')
        context = self.context
        
        SPACE_LITERAL = Literal(' ')
        
        continuing = False
        prev_lines = None
        in_rule = False
        in_define = False
        define_text = None
        cond_stack = []
        active = True
        for line in f:
            line = line[:-1]
            ls_line = line.lstrip()
            s_line = line.strip()
            
            # ignore comments
            if ls_line.startswith('#'):
                #print 'ignoring comment', line
                continue
            
            # for line continuation junk, don't actually process things until
            #  we have the whole effective line
            if continuing:
                line = prev_lines + ' ' + line
                ls_line = line.lstrip()
                s_line = line.strip()
            if line.endswith('\\'):
                continuing = True
                prev_lines = line[:-1]
                continue
            else:
                continuing = False
                prev_lines = None
                
            # we can strip leading whitespace if we aren't in a rule or the
            #  whitespace isn't a tab...
            if not in_rule or line.startswith(' '):
                line = ls_line

            if in_define:
                if line == 'endef':
                    self.context[in_define] = self._parseOneFileThing(define_text,
                                                                      False)[0]
                    in_define = False
                    define_text = None
                    continue
                else:
                    define_text += line
                    continue

            if ' ' in s_line or '\t' in s_line:
                first_word, rest = line.split(None, 1)
            else:
                first_word = s_line
            
            if first_word == 'define':
                in_define = rest.strip()
                define_text = ''
                continue
            # control-flow now gets some love
            elif first_word in self.CONDITIONALS:
                # we do not affect in_rule status
                if first_word == 'endif':
                    active = cond_stack.pop()
                elif first_word == 'else':
                    active = not active
                else: # it's a conditional!
                    cond_stack.append(active)
                    if first_word in ('ifdef', 'ifndef'):
                        active = bool(self.context.eval(rest))
                        if first_word == 'ifndef':
                            active = not active
                        #print 'COND', active, 'from', line
                    else: # ifeq, ifneq
                        if not rest:
                            raise Exception("Weird ifeq/ifneq: %s" % (line,))
                        if rest[0] == '(':
                            # eat parens
                            rest = rest[1:-1]
                            # get first guy through the comma...
                            first_part, rest,t = self._parseOneFileThing(rest,
                                                                         True,
                                                                         ',')
                            second_part, rest,t = self._parseOneFileThing(rest,
                                                                          False)
                        else: # quoted
                            quote_char = rest[0]
                            first_part, rest,t = self._parseOneFileThing(
                                                     rest[1:], True, quote_char)
                            quote_char = rest[0]
                            second_part, rest,t = self._parseOneFileThing(
                                                     rest[1:], True, quote_char)
                            
                        first_val  = first_part.evalInContext(self.context)
                        second_val = second_part.evalInContext(self.context)
                        
                        active = (first_val == second_val)
                        
                        if first_word == 'ifneq':
                            active = not active

                        #print 'COND', active, 'from', line
                continue

            # uh, I guess ignore 'include' for now too...
            if first_word == 'include' or first_word == '-include':
                in_rule = False
                if not active:
                    #print 'skipping include because inactive'
                    continue
                include_files_node = self._parseOneFileThing(rest, False)[0]
                print 'INCLUDE NODE', include_files_node
                include_files_s = include_files_node.evalInContext(self.context)
                include_files = include_files_s.split()
                
                for include_file in include_files:
                    include_path = os.path.join(os.path.dirname(path),
                                                include_file)
                    if include_path in self.makefile_stack:
                        raise Exception("Attempted makefile recursion! "
                                        "stack: %s" % (self.makefile_stack,))
                    # if we are -included and the file doesn't exist, just skip
                    # (otherwise we'll let our parse command fail...)
                    if not os.path.isfile(include_path) and first_word == '-include':
                        continue
                    
                    #print 'INCLUDING', include_path
                    self.parse(include_path)
                
                continue
            
            # uh, we're no longer in a rule if we see a line with content that
            #  doesn't start with a tab.  but blank lines apparently don't
            #  terminate rules.
            if in_rule and not line.startswith('\t') and line.strip():
                in_rule = False
            # ignore rules
            if in_rule:
                #print 'in rule, skipping', line
                continue
            
            if len(line) == 0:
                #print 'skipping blank line'
                continue
            
            line = line.lstrip()
            
            file_things = []
            pre_gobble_line = line
            while line and line[0] not in ':?+=':
                file_thing, line, term_char = self._parseOneFileThing(line,
                                                                      True,
                                                                      ' \t:=')
                file_things.append(file_thing)
                if term_char and term_char in ':=':
                    line = term_char + line
                    break
            
            if (line.startswith('=') or line.startswith(':=') or
                    line.startswith('+=') or line.startswith('?=')):
                if line[0] == '=':
                    line = line[1:].lstrip()
                    action = '='
                else:
                    action = line[0]
                    line = line[2:].lstrip()
                value = self._parseOneFileThing(line, False)[0]
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
                
                if active:
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
                #else:
                    #print 'ignoring variable assignment because inactive'
                
            elif line.startswith(':'):
                in_rule = True
                print 'found a rule...', pre_gobble_line
            elif file_things and file_things[0] == 'export':
                # export without assignment doesn't matter to us
                continue
            elif file_things and file_things[0] == 'override':
                # override without assignment doesn't matter to us
                continue
            elif file_things and file_things[0] == 'unexport':
                # unexport without assignment doesn't matter to us
                continue
            # be okay with (void) variable expansion for side-effects
            elif len(file_things) == 1 and isinstance(file_things[0], VarRef):
                continue 
            else:
                raise Exception("Weird parse: %s, %s: %s" % (map(str, file_things),
                                                     line, pre_gobble_line))
        
        self.makefile_stack.pop()
    
    def get(self, name):
        return self.context[name].evalInContext(self.context)
    
    def dump(self):
        for key in self.context.values:
            print '%s: %s' % (key, self.context[key].evalInContext(self.context))
            
if __name__ == '__main__':
    m = Makefile()
    #m.parse('/home/visbrero/rev_control/mozilla-cvs/client.mk')
    #m.parse('/home/visbrero/rev_control/mozilla-cvs/xpcom/Makefile.in')
    m.parse('/home/visbrero/rev_control/hg/moz-mac/mozilla/obj-thunderbird-generic/xpcom/Makefile')
    m.dump()
    #print m.get('MODULES_mail').split()
