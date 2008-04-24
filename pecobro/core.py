import os.path

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
        func_called, func_inc_weight = func.ever_called.get(invoc.func, (0,0))
        func.ever_called[invoc.func] = (func_called + 1,
                                        func_inc_weight + invoc_inc_weight)
        # subtract off the time we spent outside the function
        func.exclusive_weight -= invoc_inc_weight 

        s_file = self.func.file
        c_file = invoc.func.file
        file_called, file_inc_weight = s_file.ever_called.get(c_file, (0,0))
        s_file.ever_called[c_file] = (file_called + 1,
                                      file_inc_weight + invoc_inc_weight)
        

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
    def __init__(self, source_file, jstype, func_name):
        #: what file do we come from
        self.file = source_file
        #: the object/javascript type we are a method on
        self.jstype = jstype
        #: function name, preferring explicit over inferred from property 
        self.name = func_name
        #: what is our name identifier, safely used in our html/javascript
        self.norm_name = func_name.replace('$', '_')
        
        self.args = None
        
        self.ast = None
        
        #: number of ticks in this function per our simplistic count...
        self.inclusive_weight = 0
        self.exclusive_weight = 0
        
        #: list of all invocations (of us)...
        self.invocations = []

        #: dict of every function we have ever called and a tuple of (how many
        #   times, inclusive call length)
        self.ever_called = {}
        
        ## tokeny stuff
        self.source_line = None
        self.source_col = None        

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

class SourceFile(object):
    def __init__(self, path, file_type, base_dir=None, eRoot=None):
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
        
        self.functions = {}
        
        self.ever_called = {}
        
        self.eRoot = eRoot
        
        self.ast = None
        
        # the contents of the file, as they ocurr in the file sequentially.
        self.contents = []

        # multiple-counting in this case is probably extra-non-intuitive.
        self.inclusive_weight = 0
        self.exclusive_weight = 0
        
        #: Global variables exposed by this file.
        self.scope = Scope('global', None)

    def get_or_create_function(self, funcname):
        func = self.functions.get(funcname)
        if func is None:
            func = Func(self, None, funcname)
            self.add_function(func)
            created = True
        else:
            created = False
        return func, created
    
    def def_global(self, var_name, var_value, token):
        self.globals[var_name] = var_value
        self.global_tokens[var_name] = token

    def add_function(self, func):
        self.functions[func.name] = func
    
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
    def __init__(self):
        self.source_files = []
        self.base_name_to_file = {}
        
        self.globals = {}
        self.global_def_locations = {}
    
    def append(self, source_file):
        source_file.caboodle = self
        self.source_files.append(source_file)
        self.base_name_to_file[source_file.base_name] = source_file
    
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

    