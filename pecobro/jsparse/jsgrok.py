'''
Analysis logic to attempt to piece together useful semantic information from
javascript.  We are not trying to be fancy, but we don't want to rule it out.

We may move our representation stuff into pecobro.core at some point; for now
the idea is to keep this stuff orthogonal.
'''

import pecobro.jsparse.JavaScriptLexer as jslex

import pecobro.core as core

GLOBAL_OBJ_NAMES = (
    'Array', 'Boolean', 'Date', 'Error', 'EvalError', 'Function', 'Math',
    'Number', 'Object', 'RangeError', 'ReferenceError', 'RegExp', 'String',
    'SyntaxError', 'TypeError', 'URIError',
    )

GLOBAL_PROP_NAMES = (
    'Infinity', 'NaN', 'undefined',
    )

GLOBAL_FUNC_NAMES = (
    'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent',
    'eval', 'isFinite', 'isNaN', 'parseFloat', 'parseInt',
    )

UNDEFINED = None

class JSGrok(object):
    def __init__(self, caboodle):
        self.caboodle = caboodle
    
    def _as_varref(self, node):
        '''
        If the node in question is a VEXPR starting with a VARREF, return its
        children and a flag indicating whether there is more than the one
        child.  (We return the flag for readability of the caller).
        
        If the node is not, both return values are None.
        '''
        if (node.getType() != jslex.VEXPR
                or node.getChildCount() < 1
                or node.getChild(0).getType() != jslex.VARREF):
            return None, None
                
        return node.children, (node.getChildCount() > 1)

    def _val_map(self, source_file, node, scope, who, enclosingPropNode=None):
        '''
        Given a token, map it into our value-space...
        '''
        ntype = node.getType()
        # functions get mapped to our function object
        if ntype == jslex.FUNC:
            nName = node.getChild(0)
            if nName.getType() == jslex.ANONYMOUS:
                if enclosingPropNode is not None:
                    func_name = enclosingPropNode.getChild(0).token.text
                    # because we can't assign the property name token to be
                    #  the basis of the synthetic ANONYMOUS token, we need
                    #  to change things up to just use the property name as our
                    #  token for that purpose
                    # (note that the specific glitch and our grammar change
                    #  only happened in the context of having a property; if
                    #  there is no enclosingPropNode, we should actually be okay
                    #  to leave nName as is (when this next line doesn't get
                    #  executed) because we are propagating things still in the
                    #  pure anonymous function case...)
                    nName = enclosingPropNode.getChild(0)
                
                propTypeNode = enclosingPropNode.getChild(1)
                if propTypeNode.getType() != jslex.PROP:
                    func_name = propTypeNode.token.text + '_' + func_name
                

                func_name = 'anon:%d:%d' % (nName.token.line,
                                            nName.token.charPositionInLine)
            else:
                func_name = nName.token.text
                
            func, created = source_file.get_or_create_function(func_name)

            if created or func.source_line is None:
                func.source_line = nName.token.line
                func.source_col  = nName.token.charPositionInLine
                
                nArgs = node.getChild(1)
                func.args = []
                for argNode in nArgs.children:
                    func.args.append(argNode.token.text)
                
                source_file.add_to_contents(func)
            
            return func
        elif ntype == jslex.VEXPR:
            nPrimary = node.getChild(0)
            ptype = nPrimary.getType()
            
            # --- literals ---
            # -- primitives --
            if ptype == jslex.NULL:
                return None
            elif ptype == jslex.TRUE:
                return True
            elif ptype == jslex.FALSE:
                return False
            elif ptype == jslex.STRING:
                # we need to chop off the quotes
                return nPrimary.getChild(0).token.text[1:-1]
            elif ptype == jslex.NUMBER:
                nstr = nPrimary.getChild(0).token.text
                if '.' in nstr:
                    return float(nstr)
                elif nstr.startswith('0x') or nstr.startswith('0X'):
                    return int(nstr, 16)
                elif nstr.startswith('0'):
                    return int(nstr, 8)
                else:
                    return int(nstr)
            elif ptype == jslex.REGEX:
                # we just treat these as strings...
                return nPrimary.toString()
            # -- array --
            elif ptype == jslex.ARRAY:
                arr = []
                for arrNode in nPrimary.children:
                    arr.append(self._val_map(source_file, arrNode, scope, who))
                return arr
            # -- object --
            elif ptype == jslex.OBJ:
                obj = {}
                for propNode in nPrimary.children:
                    # everyone is a PROP node
                    key = propNode.getChild(0).token.text
                    val = self._val_map(source_file, propNode.getChild(2),
                                        scope, who,
                                        enclosingPropNode=propNode)
                    obj[key] = val
                return obj
            # --- lookups ---
            # 
            elif ptype == jslex.VARREF:
                var_name = nPrimary.getChild(0).token.text
                val = scope.lookup(var_name, who)
                return val

    def grok_globals(self, source_file, ast):
        '''
        Walk the AST looking for contributions to the global namespace.
        '''
        for child in ast.children:
            ctype = child.getType()
            # var|const ...
            if ctype == jslex.VARDEFS:
                # first dude is either 'var' or 'const', skip him
                for vardef in child.children[1:]:
                    # get the name
                    var_name = vardef.getChild(0).token.text
                    # get the value mapped into our space...
                    if len(vardef.children) == 3:
                        var_val = self._val_map(source_file, vardef.getChild(1),
                                                source_file.scope, source_file)
                    else:
                        var_val = UNDEFINED
                    source_file.scope.store(var_name, var_val, source_file)
            # function
            elif ctype == jslex.FUNC:
                tName = child.getChild(0)
                if tName.getType() != jslex.ANONYMOUS:
                    func = self._val_map(source_file, child,
                                         source_file.scope, source_file)
                    source_file.scope.store(func.name, func, source_file)
            # foo = bar
            elif ctype == jslex.ASSIGN:
                vexpr, complex = self._as_varref(child.getChild(0))
                if vexpr and not complex:
                    var_name = vexpr[0].token.text
                    var_val = self._val_map(source_file, child.getChild(1),
                                            source_file.scope, source_file)
                    source_file.scope.store(var_name, var_val, source_file)
        
        import pprint
        print 'SOURCE FILE GLOBALS'
        pprint.pprint(source_file.scope.values)
        print 'GLOBAL READERS'
        pprint.pprint(source_file.scope.readers)
        print 'GLOBAL WRITERS'
        pprint.pprint(source_file.scope.writers)
    
    def grok_objects(self, source_file, ast):
        '''
        Walk the AST processing object definitions...
        
        These will tend to look like one of the following:
        CLASS.prototype.FUNCTION = function() {}
        CLASS.prototype = {FUNCTION: function FUNCTION? () {}}
        '''
        for child in ast.children:
            ctype = child.getType()
            
            # functions can define constructors and thereby objects...
            if ctype == jslex.FUNC:
                # so, we're not sure a function is an object constructor until
                #  we actually see it used in a context that suggests it is
                #  an object.  That translates to seeing its prototype member
                #  accessed or seeing it new'ed (not pursuing that for now).   
                pass
            # assignments may manipulate the prototype
            elif ctype == jslex.ASSIGN:
                vexpr, complex = self._as_varref(child.getChild(0))
                # needs to start with a varref and have multiple kids
                if vexpr is None or not complex:
                    continue
                if vexpr[1].token.text != 'prototype':
                    continue
                # (figure out what they're assigning for subsequent processing)
                right_node = child.getChild(2)
                right_val  = self._val_map(source_file, right_node,
                                           source_file.scope, source_file)
                
                # are they assigning an object to the prototype?
                if len(vexpr) == 2:
                    # they need to be assigning an object literal or something
                    #  that is an object.  However, the latter case can get
                    #  hard, so we punt for now.  (TODO: handle indirect object)
                    pass
                # are they modifying something in the prototype...
                elif len(vexpr) == 3:
                    # they need to be assigning a function, either directly or
                    #  from a (global) variable
                    # make sure the variable reference is a function...
                    if not isinstance(right_val, core.Func):
                        continue
                    

    def grok_source_file(self, source_file, ast):
        
        self.grok_globals(source_file, ast)
        self.grok_objects(source_file, ast)

    def grok_function(self, source_file, func, funcNode):
        '''
        Process a function looking for global references as well as local
        references (self method calls or property manipulation.)
        
        Importante:
        - Don't forget about prefix/postfix manipulations.
        
        Special extras:
        - Detect what Component.classes are accessed (someday)
        '''
        for child in funcNode.children:
            pass
            # the left side of a complex assign is a write at its tip, but a
            #  read at the base. 
            # a post-fix expression is a read and a write
            
        
