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
        

class Func(object):
    def __init__(self, source_file, clazz, func_name):
        self.file = source_file
        self.clazz = clazz
        self.name = func_name
        self.norm_name = func_name.replace('$', '_')
        
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

    
    def log_invoke(self, *args):
        invoc = FuncInvoc(self, *args)
        self.invocations.append(invoc)
        
        weight = invoc.t_end - invoc.t_start
        self.inclusive_weight += weight
        self.exclusive_weight += weight
        
        return invoc


class SourceFile(object):
    def __init__(self, path, file_type):
        self.caboodle = None
        
        self.path     = path
        self.filetype = file_type
        
        self.base_name = os.path.basename(path)
        self.norm_base_name = os.path.basename(path).replace('.', '_')
        
        self.functions = {}
        
        self.ever_called = {}
        
        # the contents of the file, as they ocurr in the file sequentially.
        self.contents = []

        # multiple-counting in this case is probably extra-non-intuitive.
        self.inclusive_weight = 0
        self.exclusive_weight = 0

    def get_or_create_function(self, funcname):
        func = self.functions.get(funcname)
        if func is None:
            func = Func(self, None, funcname)
            self.add_function(func)
        return func

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

    