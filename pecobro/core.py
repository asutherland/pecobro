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

import os.path

try:
    import cerealizer
except:
    cerealizer = None

class FuncInvoc(object):
    __slots__ = ['func', 't_start', 't_end', 'depth', 'cflow',
                 'calls', 'parent']
    '''
    Represents the invocation of a function by the timestamp at entry and exit,
    the depth of the stack during the invocation, control flow uniqueness value,
    and a list of all the invocations we made.
    '''
    def __init__(self, func, t_start, t_end, depth, cflow):
        self.func = func
        self.t_start = t_start
        self.t_end   = t_end
        self.depth = depth
        self.cflow = cflow
        
        self.calls = None
        self.parent = None
    
    @property
    def weight(self):
        return self.t_end - self.t_start
    
    def log_call(self, invoc):
        '''
        Process a call made from this invocation by our function (self.func) to
        another function, as defined by the invoc we are passed.
        '''
        invoc.parent = self
        if self.calls is None:
            self.calls = [invoc]
        else:
            self.calls.append(invoc)
        
        invoc_inc_weight = invoc.t_end - invoc.t_start 
        
        func = self.func
        # ever_called
        func_called, func_inc_weight = func.ever_called.get(invoc.func, (0,0))
        func.ever_called[invoc.func] = (func_called + 1,
                                        func_inc_weight + invoc_inc_weight)
        # (reverse) ever_called_by
        called_by_count, called_by_weight = invoc.func.ever_called_by.get(func, (0,0))
        invoc.func.ever_called_by[func] = (called_by_count + 1,
                                           called_by_weight + invoc_inc_weight)
        
        # subtract off the time we spent outside the function
        func.exclusive_weight -= invoc_inc_weight 

        s_file = self.func.file
        c_file = invoc.func.file
        file_called, file_inc_weight = s_file.ever_called.get(c_file, (0,0))
        s_file.ever_called[c_file] = (file_called + 1,
                                      file_inc_weight + invoc_inc_weight)
        
        # TODO: (reverse) file ever_called_by 
        

class Scope(object):
    '''
    Abstracts nested scopes, providing a combination of actual lookups/storage
    as well as dependency tracking.  The lookup/storage part is that we want
    to properly pierce the veil of (limited) trickery in getting functions to
    be methods.  The tracking part is that we want to know who is accessing/
    modifying global variables.
    '''
    __slots__ = ['name', 'parent', 'values', 'readers', 'writers',
                 'is_var_scope']
    
    def __init__(self, name, parent, var_scope=True):
        #: our scope name
        self.name = name
        #: our parent scope, if any
        self.parent = parent
        #: are we are a var scope or just a let scope?
        self.is_var_scope = var_scope
        
        #: Our stored values...
        self.values = {}
        #: Map value name to set of readers...
        self.readers = {}
        #: Map value name to set of writers...
        self.writers = {}
    
    def lookup(self, name, who):
        '''
        Perform a look-up of a name in this scope, tracking responsibility to
        who.  Returns a tuple of the lookup result and the scope it came from
        (for local tracking on 'who'). 
        '''
        if self.parent and not name in self.values:
            return self.parent.lookup(name, who)
        
        readers = self.readers.get(name)
        if readers is None:
            readers = self.readers.setdefault(name, set())
        readers.add(who)

        return self.values.get(name)
    
    def global_store(self, name, value, who):
        if self.parent:
            self.parent.global_store(name, value, who)
        else:
            self.var_store(name, value, who)
    
    def var_store(self, name, value, who):
        '''
        Perform a var store into the nearest var scope.  A var store is one
        that is the explicit result of a 'var a ='.
        '''
        if not self.is_var_scope:
            return self.parent.var_store(name, value, who)
        
        self.values[name] = value
        writers = self.writers.get(name)
        if writers is None:
            writers = self.writers.setdefault(name, set())
        writers.add(who)
    
    def let_store(self, name, value, who):
        '''
        '''
        self.values[name] = value
        writers = self.writers.get(name)
        if writers is None:
            writers = self.writers.setdefault(name, set())
        writers.add(who)
    
    def gen_store(self, store_type, name, value, who):
        if store_type in ('var', 'const'):
            self.var_store(name, value, who)
        else: # let
            self.let_store(name, value, who)
    
    def lex_store(self, name, value, who):
        '''
        Assign a value based on lexical context; which is to say, find the first
        scope with the given variable name.  If we can't find one, then we are
        effectively a global write.
        '''
        if name in self.values:
            # the use of let store is an 'optimization'; we aren't really a let.
            self.let_store(name, value, who)
        elif self.parent:
            self.parent.lex_store(name, value, who)
        # no parent means we have reached the global case.  do it.
        else:
            self.let_store(name, value, who)
    
    def merge(self, oscope):
        for name, o_readers in oscope.readers.items():
            readers = self.readers.get(name)
            if readers is None:
                readers = self.readers.setdefault(name, set())
            readers.update(o_readers)
        
        for name, o_writers in oscope.writers.items():
            writers = self.writers.get(name)
            if writers is None:
                writers = self.writers.setdefault(name, set())
            writers.update(o_writers)
    
    def usage_slice(self, sub_scope):
        writes_and_read_by = []
        for name in sub_scope.writers:
            writes_and_read_by.append((name, sorted(self.readers.get(name, ()))))
        writes_and_read_by.sort()
        
        reads_and_written_by = []
        for name in sub_scope.readers:
            reads_and_written_by.append((name, sorted(self.writers.get(name, ()))))
        reads_and_written_by.sort()
            
        return reads_and_written_by, writes_and_read_by

class Func(object):
    def __init__(self, source_file, jstype, func_name, line=None, col=None):
        #: what file do we come from
        self.file = source_file
        #: the object/javascript type we are a method on
        self.jstype = jstype
        #: function name, preferring explicit over inferred from property 
        self.name = func_name
        #: what is our name identifier, safely used in our html/javascript
        self.norm_name = func_name.replace('$', '_') + (
                            '_%d' % (line or 0,)) 
        
        self.args = None
        
        self.ast = None
        #: indicates whether this is a nested AST and therefore not top-level.
        self.nested_ast = True
        
        #: number of ticks in this function per our simplistic count...
        self.inclusive_weight = 0
        self.exclusive_weight = 0
        
        #: list of all invocations (of us)...
        self.invocations = []

        #: dict of every function we have ever called and a tuple of (how many
        #   times, inclusive call length)
        self.ever_called = {}
        #: dict of every function we have ever been called by and a tuple of
        #   (how many times, inclusive call length)
        self.ever_called_by = {}
        
        ## tokeny stuff
        self.source_line = line
        self.source_col = col
    
    def __cmp__(self, other):
        if isinstance(other, Func):
            if self.file == other.file:
                return cmp(self.name, other.name)
            else:
                return cmp(self.file, other.file)
        elif isinstance(other, SourceFile):
            return -cmp(other, self)
        else:
            return 0
    
    def is_anon(self):
        return self.name.startswith('anon:')
    
    def rename(self, new_name):
        self.file.rename_anon(self, self.name, new_name)

    def __str__(self):
        return 'Func:%s:%s' % (self.file.base_name, self.name,)

    def __repr__(self):
        return self.__str__()
    
    def log_invoke(self, *args):
        invoc = FuncInvoc(self, *args)
        self.invocations.append(invoc)
        
        weight = invoc.t_end - invoc.t_start
        self.inclusive_weight += weight
        self.exclusive_weight += weight
        
        return invoc
    
    @property
    def sorted_ever_called(self):
        ever_called_funcs = self.ever_called.items()
        ever_called_funcs.sort(key=lambda x:
                                (-x[1][0],
                                 x[0].file.base_name,
                                 x[0].name))
        return ever_called_funcs

    @property
    def sorted_ever_called_by(self):
        ever_called_by_funcs = self.ever_called_by.items()
        ever_called_by_funcs.sort(key=lambda x:
                                (-x[1][0],
                                 x[0].file.base_name,
                                 x[0].name))
        return ever_called_by_funcs


class JSType(object):
    def __init__(self, name, constructor=None, parent=None):
        self.name = name
        
        self.constructor = constructor
        self.parent = parent
        
        self.prototype = Scope('prototype')
        self.instance = Scope('instance', self.prototype)

class JSObj(object):
    '''
    Created especially to represent fields... a sorta-dubious name/call in the
    first place, but for now, we have fallen back to actually treating fields
    as functions because they are evaluated and in their evaluation can cause
    calls to occur...
    '''
    def __init__(self, source_file, name):
        #: what file do we come from
        self.file = source_file
        #: function name, preferring explicit over inferred from property 
        self.name = name
        #: what is our name identifier, safely used in our html/javascript
        self.norm_name = name.replace('$', '_')
        
        self.ast = None
        #: indicates whether this is a nested AST and therefore not top-level.
        self.nested_ast = True
        
        ## tokeny stuff
        self.source_line = None
        self.source_col = None        

class XPAttribute(object):
    __slots__ = ['interface', 'name', 'type', 'readonly']
    
    def __init__(self, interface, name, type,
                 readonly=False):
        self.interface = interface
        self.name = name
        self.type = type
        
        self.readonly = readonly

class XPMethodArg(object):
    __slots__ = ['direction', 'type', 'name']
    def __init__(self, direction, type, name):
        self.direction = direction
        self.type = type
        self.name = name
    
    def __str__(self):
        return '%s %s %s' % (self.direction, self.type, self.name)
    
    def __repr__(self):
        return self.__str__()

class XPMethod(object):
    '''
    A method on an XPCOM interface; although semantically different from a
    function, for all rendering purposes it implements the same fundamental
    interface.
    '''
    EMPTY_MAP = {}
    
    __slots__ = ['interface', 'name', 'type', 'scriptable', 'args',
                 'source_line', 'source_col']
    def __init__(self, interface, name, type, args=(),
                 scriptable=True,
                 source_line=None, source_col=None):
        self.interface = interface
        self.name = name
        self.type = type
        
        self.args = args
        
        self.scriptable = scriptable
        
        self.source_line = source_line
        self.source_col = source_col
    
    def __str__(self):
        return '%s:%s(%s)' % (self.interface.name, self.name,
                              ', '.join(map(str, self.args)))
    
    def __repr__(self):
        return self.__str__()

    # the norm_name can be calculated on demand...
    @property
    def norm_name(self):
        return '%s_%s' % (self.interface.name, self.name)
    
    ## NOP all the things that functions have but only make sense for them...
    def is_anon(self):
        return False
    @property
    def ast(self):
        return None
    @property
    def nested_ast(self):
        return False
    @property
    def inclusive_weight(self):
        return 0
    @property
    def exclusive_weight(self):
        return 0
    @property
    def invocations(self):
        return ()
    @property
    def ever_called(self):
        return XPMethod.EMPTY_MAP
    @property
    def sorted_ever_called(self):
        return ()
    @property
    def ever_called_by(self):
        return XPMethod.EMPTY_MAP
    @property
    def sorted_ever_called_by(self):
        return ()

class XPInterface(object):
    __slots__ = ['file', 'name',
                 'scriptable',
                 'attributes', 'consts', 'methods']
    def __init__(self, source_file, name, scriptable=False):
        self.file = source_file
        self.name = name
        
        self.scriptable = scriptable
        
        self.attributes = {}
        self.consts = {}
        self.methods = {}

    def add_attribute(self, attrib):
        self.attributes[attrib.name] = attrib

    def def_const(self, name, value):
        self.consts[name] = value
    
    def add_method(self, method):
        self.methods[method.name] = method
        
        if self.file:
            self.file.add_function(method, method.source_line)
            self.file.add_to_contents(method)
            

FILE_TYPE_INTERPRETED = {
    'idl': False,
    'js': True, 'jsm': True,
    'xbl': False, 'xul': False,
    }

class SourceFile(object):
    def __init__(self, path, file_type, base_dir=None, eRoot=None, defines=None):
        self.caboodle = None
        
        self.path     = path
        if base_dir:
            abspath = os.path.abspath(path)
            absbase = os.path.abspath(base_dir)
            self.norm_path = abspath[len(absbase)+1:]
        else:
            self.norm_path = path
            
        self.filetype = file_type
        
        self.base_name = os.path.basename(path)
        self.norm_base_name = os.path.basename(path).replace('.', '_')
        
        #: implementation names in this file; dtrace may use instead of filename
        self.impl_names = []
        
        #: function name to Func.  collisions may occur!
        self.functions = {}
        #: (function name, function line) tuple.  collisions are rather unlikely 
        self.functions_with_line = {}
        #: function line to Func.  collisions could happen.
        self.functions_by_line = {}
        #: in case we cleverly rename an anonymous function, help unclever code
        self.anon_function_tombstones = {}
        
        self.xpcom_interfaces = {}
        
        #: currently unused because we no longer break-out fields specially...
        self.fields = {}
        
        self.ever_called = {}
        
        self.eRoot = eRoot
        
        #: defines passed to the preprocessor, although we may not be preproced
        self.defines = defines
        
        #: if a pure javascript file, the AST associated with it; not for XBL.
        self.ast = None
        #: the codec we used, if any, to parse this file.  we may lie if our
        #:  ast was cached but we were not (meta-)cached...
        self.used_codec = None
        
        # the contents of the file, as they ocurr in the file sequentially.
        self.contents = []

        # multiple-counting in this case is probably extra-non-intuitive.
        self.inclusive_weight = 0
        self.exclusive_weight = 0
        
        #: Global variables exposed by this file.
        self.scope = Scope('global', None)
        
        # create our synthetic import function
        if FILE_TYPE_INTERPRETED.get(self.filetype):
            self.import_function, trash = self.get_or_create_function('!import',
                                                                      0)
            self.import_function.source_line = 0
            self.import_function.source_col = 0
            self.add_to_contents(self.import_function)

    def __cmp__(self, other):
        if isinstance(other, SourceFile):
            return cmp(self.path, other.path)
        elif isinstance(other, Func):
            return cmp(self.path, other.file.path)
        else:
            return 0

    def rename_anon(self, func, anon_name, new_name):
        del self.functions[anon_name]
        del self.functions_with_line[(anon_name, func.source_line)]
        self.anon_function_tombstones[anon_name] = func
        self.functions[new_name] = func
        self.functions_with_line[(new_name, func.source_line)] = func 
        
        func.name = new_name

    def get_or_create_function(self, funcname, lineno=None):
        func = self.functions_with_line.get((funcname, lineno))
        # try an anonymous tombstone (even if not anonymous; no risk)
        if func is None:
            func = self.anon_function_tombstones.get(funcname)
        if func is None:
            func = Func(self, None, funcname, line=lineno)
            self.add_function(func, lineno)
            created = True
        else:
            created = False
        return func, created
    
    def get_or_create_field(self, field_name):
        field = self.fields.get(field_name)
        if field is None:
            field = JSObj(self, field_name)
            self.add_field(field)
            created = True
        else:
            created = False
        return field, created
    
    def get_func_by_line(self, lineno):
        '''
        Return the function that exists at the given line.  We will fudge by
        a line because it appears that the javascript engine may actually
        register the function as starting on the line with the brace...
        '''
        return (self.functions_by_line.get(lineno) or
                self.functions_by_line.get(lineno-1))

    def add_function(self, func, lineno):
        self.functions[func.name] = func
        self.functions_with_line[(func.name, lineno)] = func
        
    def add_field(self, field):
        self.fields[field.name] = field
    
    def add_to_contents(self, thing):
        self.contents.append(thing)
        if isinstance(thing, Func):
            func = thing
            if func.source_line is not None:
                self.functions_by_line[func.source_line] = func
    
    def add_xpcom_interface(self, interface):
        self.xpcom_interfaces[interface.name] = interface
    
    def __str__(self):
        return 'SourceFile: %s' % (self.path,)
    
    @property
    def sorted_functions(self):
        sfuncs = list(self.functions.values())
        sfuncs.sort(key=lambda x:x.name)
        return sfuncs
    
    @property
    def weighted_functions(self):
        sfuncs = list(self.functions.values())
        sfuncs.sort(key=lambda x:(x.inclusive_weight, x.name), reverse=True)
        return sfuncs
    

class SourceCaboodle(object):
    '''
    In theory we might consume an install.rdf or something or otherwise be
    clever about providing search paths, predicating on configurations, etc.
    Right now we are just a fancy (and poorly, if awesomely, named) dictionary.
    '''
    def __init__(self, moz_src_path, moz_build_path,
                 project,
                 module_dirs=(), locale_dirs=(), overlay_dirs=()):
        self.moz_src_path = moz_src_path
        self.moz_build_path = moz_build_path
        self.project = project
        
        self.module_dirs = module_dirs
        self.locale_dirs = locale_dirs
        self.overlay_dirs = overlay_dirs
        
        self.source_files = []
        self.base_name_to_file = {}
        self.impl_name_to_file = {}
        
        self.path_to_file = {}

        #: map chrome paths to file-system paths
        self.chrome_map = {}
        #: components
        self.components = []
        #: modules (from EXTRA_(PP_)JS_MODULES)
        self.modules = []
        #: XPCOM interface definition files
        self.xpcom_idl_files = []
        
        #: temporary global scope
        self.scope = Scope('catch-all-global', None)
        # (there isn't just one global scope, but until we understand XUL, this
        #  will have to do...)
        
    
    def append(self, source_file):
        source_file.caboodle = self
        self.source_files.append(source_file)
        self.base_name_to_file[source_file.base_name] = source_file
        self.path_to_file[source_file.path] = source_file
    
    def get_file_from_chrome_path(self, chrome_path):
        if not chrome_path in self.chrome_map:
            return None
        defines, file_path = self.chrome_map[chrome_path]
        return self.path_to_file.get(file_path) 
    
    def update_global_info_from(self, source_file):
        self.scope.merge(source_file.scope)
    
    @property
    def sorted_source_files(self):
        # eh, let's favor 'manual' quicksort over the cool iterator
        sortee = self.source_files[:]
        sortee.sort(key=lambda x:x.base_name)
        return sortee

    @property
    def relevant_source_files(self):
        sortee = filter(lambda x: x.inclusive_weight, self.source_files)
        sortee.sort(key=lambda x:x.base_name)
        return sortee

if cerealizer:
    cerealizer.register(FuncInvoc)
    cerealizer.register(Scope)
    cerealizer.register(Func)
    cerealizer.register(JSType)
    cerealizer.register(JSObj)
    cerealizer.register(SourceFile)

    