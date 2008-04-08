# todo: make absolute
import core

class TraceParser(object):
    def __init__(self, caboodle, *args, **kwargs):
        self.caboodle = caboodle
        self._vfunc_map = {}

    def _get_func(self, filename, obj, funcname):
        # 
        itupe = (filename, funcname)
        vfunc = self._vfunc_map.get(itupe)
        if vfunc is None:
            vfunc = VFunc(filename, funcname)
            self._vfunc_map[itupe] = vfunc
        return vfunc     
    
    def parse(self, filename):
        func_cache = {}
        def get_func(filename, funcname):
            ctupe = (filename, funcname)
            func = func_cache.get(ctupe)
            
            if func is None:
                source_file = self.caboodle.base_name_to_file.get(filename)
                if source_file is None:
                    raise Exception('Unable to locate source file: %s' % filename)
                
                func = source_file.functions.get(funcname)
                if func is None:
                    func = core.Func(source_file, None, funcname)
                    source_file.add_function(func)
                
                func_cache[ctupe] = func
            
            return func
            
        
        f = open(filename, 'r')
        
        # Let's do a quick pass where we find out the earliest time we see...
        start_ts = None
        max_te = 0
        for line in f:
            line = line.strip()
            if not ',' in line:
                continue
            
            depth_str, ts_str, te_str, filename, funcname = line.split(',')
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
            
            depth_str, ts_str, te_str, filename, funcname = line.split(',')
            depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
            
            # gah! so, the probes are double-counting, so for now, let's exclude
            #  all the even guys...
            if depth%2 == 0:
                continue
            depth = depth / 2 + 1
            
            ts -= start_ts
            te -= start_ts

            # find our function and log this invocation of our function
            func = get_func(filename, funcname)
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
            for func in source_file.functions.values():
                source_file.inclusive_weight += func.inclusive_weight
                source_file.exclusive_weight += func.exclusive_weight
