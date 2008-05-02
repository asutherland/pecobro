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

def as_varref(node):
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

def propref_name(node):
    if node.getType() == jslex.PROPREF:
        return node.children[0].token.text
    else:
        return None

def as_string(node):
    if node.getType() == jslex.VEXPR:
        if len(node.children) != 1:
            return None
        else:
            return as_string(node.children[0])
    elif node.getType() == jslex.STRING:
        # we need to chop off the quotes
        return node.children[0].token.text[1:-1]
    else:
        return None

def call_name(node):
    '''
    If node is a CALL node with a single VARREF VEXPR, returns the name of the
    VARREF, otherwise None.
    '''
    if node.getType() == jslex.CALL:
        calledNode = node.children[0]
        if (calledNode.getType() == jslex.VEXPR and
                len(calledNode.children) == 1):
            vexprKid = calledNode.children[0]
            if vexprKid.getType() == jslex.VARREF:
                return vexprKid.children[0].token.text
    return None

class JSGrok(object):
    def __init__(self, caboodle):
        self.caboodle = caboodle
    
    def _val_map(self, source_file, node, scope, who, enclosingPropNode=None,
                 adj_line=0, adj_column=0):
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
                else:
                    func_name = 'anon:%d:%d' % (nName.token.line + self.adj_line,
                                                nName.token.charPositionInLine +
                                                ((nName.token.line == 1) and 
                                                 self.adj_column or 0))
            else:
                func_name = nName.token.text
            
            func_line = nName.token.line + self.adj_line
            
            func, created = source_file.get_or_create_function(func_name,
                                                               func_line)

            if created or func.source_line is None:
                func.source_line = func_line
                func.source_col  = nName.token.charPositionInLine
                if nName.token.line == 1:
                    func.source_col += self.adj_column
                
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

    def grok_globals(self, source_file, ast, nested=False):
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
                vexpr, complex = as_varref(child.getChild(0))
                if vexpr and not complex:
                    var_name = vexpr[0].token.text
                    var_val = self._val_map(source_file, child.getChild(1),
                                            source_file.scope, source_file)
                    source_file.scope.store(var_name, var_val, source_file)
            # handle top-level logic...
            elif ctype in (jslex.COND, jslex.CODE):
                self.grok_globals(source_file, child, nested=True)
        
        if not nested:
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
                # children: left, operator (=/+=/etc.), right)
                vexpr, complex = as_varref(child.getChild(0))
                # needs to start with a varref and have multiple kids
                if vexpr is None or not complex:
                    continue
                if propref_name(vexpr[1]) != 'prototype':
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
                    func = right_val
                    
                    prop_name = propref_name(vexpr[2])
                    if func.is_anon():
                        print 'renaming anoymous %s to %s' % (func.name, prop_name)
                        func.rename(prop_name)
            # possibility of __defineGetter__ or __defineSetter__... 
            elif ctype == jslex.CALL:
                # children: thing being called, arguments
                vexpr, complex = as_varref(child.children[0])
                # can't be FOO.prototype.__defineGetter__  if not like so...
                if vexpr is None or not complex or len(vexpr) != 3:
                    continue
                if propref_name(vexpr[1]) != 'prototype':
                    continue
                if propref_name(vexpr[2]) not in ('__defineGetter__',
                                                  '__defineSetter__'):
                    continue
                
                args = child.children[1].children
                # arguments: property name, function

                prop_name = as_string(args[0])
                if prop_name is None:
                    continue
                
                should_be_func = self._val_map(source_file, args[1],
                                               source_file.scope, source_file)
                if not isinstance(should_be_func, core.Func):
                    continue

                if should_be_func.is_anon():
                    if propref_name(vexpr[2]) == '__defineGetter__':
                        func_name = 'get_' + prop_name
                    else:
                        func_name = 'set_' + prop_name
                    print 'renaming anonymous %s to %s' % (should_be_func.name,
                                                           func_name)
                    should_be_func.rename(func_name)
                    

    def grok_field(self, source_file, ast,
                         adj_line=0, adj_column=0):
        # we can't be used concurrently...
        self.adj_line = adj_line
        self.adj_column = adj_column
        
        # nothing is currently suitable...
        
        ##self.grok_globals(source_file, ast)
        ##self.grok_objects(source_file, ast)

    def grok_func(self, source_file, ast,
                         adj_line=0, adj_column=0):
        # we can't be used concurrently...
        self.adj_line = adj_line
        self.adj_column = adj_column
        
        # nothing is currently suitable...
        
        ##self.grok_globals(source_file, ast)
        ##self.grok_objects(source_file, ast)

    def grok_source_file(self, source_file, ast,
                         adj_line=0, adj_column=0):
        # we can't be used concurrently...
        self.adj_line = adj_line
        self.adj_column = adj_column
        
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
            
        
