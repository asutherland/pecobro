# todo: make absolute
import core

class TraceParser(object):
    def __init__(self, caboodle, *args, **kwargs):
        self.caboodle = caboodle

    def parse(self, filename):
        func_cache = {}
        def get_func(filename, funcname, lineno):
            ctupe = (filename, lineno)
            func = func_cache.get(ctupe)
            
            if not ctupe in func_cache:
                source_file = self.caboodle.base_name_to_file.get(filename)
                # try it as an impl
                if source_file is None:
                    source_file = self.caboodle.impl_name_to_file.get(filename)
                if source_file is None:
                    raise Exception('Unable to locate source file: %s' % filename)
                
                # import is a special case!
                if funcname == 'import' and lineno == 1:
                    func = source_file.import_function
                else:
                    func = source_file.get_func_by_line(lineno)
                
                if func is None:
                    raise Exception('Unable to translate '
                                    '%s,%d to a function (hint: %s)' %
                                    (filename, lineno, funcname))
                
                func_cache[ctupe] = func
            else:
                func = func_cache[ctupe]
            
            return func
            
        
        f = open(filename, 'r')
        
        # Let's do a quick pass where we find out the earliest time we see...
        start_ts = None
        max_te = 0
        for line in f:
            line = line.strip()
            if not ',' in line:
                continue
            
            line_type = line[0]
            
            if line_type == 'r':
                (line_type, depth_str, ts_str, te_str, filename, objname, funcname,
                    lineno_str, caller_filename, caller_lineno_str
                    ) = line.split(',')
                depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
                
                if start_ts is not None:
                    start_ts = min(start_ts, ts)
                else:
                    start_ts = ts
                
                max_te = max(te, max_te)
        
        # because trace events are generated only on function returns, we
        #  need to accumulate things until we hit our parents...
        MAX_RECURSE_DEPTH = 256
        deferreds = [list() for i in range(MAX_RECURSE_DEPTH)]
        
        self.caboodle.max_time_value = max_te - start_ts
        
        f.seek(0)
        for line in f:
            line = line.strip()
            if not ',' in line:
                continue

            line_type = line[0]
            
            # since we do store the entire path for 'e' cases, we can use this
            #  to dis-ambiguate duplicate file names (although there are better
            #  possible solutions; we could probably whittle some files out of
            #  concern by knowing no .xul file uses it, or just have our probes
            #  not have to use basename)
            if line_type == 'e':
                (line_type, path, lineno_str) = line.split(',')
                if path.startswith('chrome://'):
                    chrome_path = path[9:]
                    sf = self.caboodle.get_file_from_chrome_path(chrome_path)
                    # er, and we do this by just overwriting the base_name entry
                    #  for this dude.  this results in a MRU cached entry...
                    # (only do this if we find a source file... this won't be
                    #  the case for .xul jerks...)
                    if sf:
                        self.caboodle.base_name_to_file[sf.base_name] = sf
            
            if line_type != 'r':
                continue
            
            (line_type, depth_str, ts_str, te_str, filename, objname, funcname,
                lineno_str, caller_filename, caller_lineno_str
                ) = line.split(',')
            depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
            lineno = int(lineno_str)
            
            ts -= start_ts
            te -= start_ts

            # find our function and log this invocation of our function
            # (brutally mis-attribute .xul files for now using the last func)
            if not filename.endswith('.xul'):
                func = get_func(filename, funcname, lineno)
            this_invoc = func.log_invoke(ts, te, depth, depth)
            
            # queue up this invocation for later consumption by our parent
            deferreds[depth-1].append(this_invoc)
            
            # log any calls we made that are waiting for us...
            if deferreds[depth]:
                for deferred in deferreds[depth]:
                    this_invoc.log_call(deferred)
                deferreds[depth] = list()
        
        # fix-up source file weights...
        for source_file in self.caboodle.source_files:
            for func in source_file.functions_with_line.values():
                source_file.inclusive_weight += func.inclusive_weight
                source_file.exclusive_weight += func.exclusive_weight
