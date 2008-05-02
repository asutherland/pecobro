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
    def __init__(self, name, parent):
        #: our scope name
        self.name = name
        #: our parent scope, if any
        self.parent = parent
        
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
        readers = self.readers.get(name)
        if readers is None:
            readers = self.readers.setdefault(name, set())
        readers.add(who)

        return self.values.get(name)
    
    def store(self, name, value, who):
        '''
        Stores the value into name, tracking the request from who  Returns
        '''
        self.values[name] = value
        writers = self.writers.get(name)
        if writers is None:
            writers = self.writers.setdefault(name, set())
        writers.add(who)

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
        self.import_function, trash = self.get_or_create_function('!import', 0)
        self.import_function.source_line = 0
        self.import_function.source_col = 0
        self.add_to_contents(self.import_function)

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
    
    def def_global(self, var_name, var_value, token):
        self.globals[var_name] = var_value
        self.global_tokens[var_name] = token

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
        
        self.globals = {}
        self.global_def_locations = {}
        
    
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

    