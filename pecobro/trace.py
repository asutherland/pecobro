
class TraceParser(object):
    def __init__(self, *args, **kwargs):
        self._vfunc_map = {}

    def _get_vfunc(self, filename, funcname):
        itupe = (filename, funcname)
        vfunc = self._vfunc_map.get(itupe)
        if vfunc is None:
            vfunc = VFunc(filename, funcname)
            self._vfunc_map[itupe] = vfunc
        return vfunc     
    
    def parse(self, filename):
        f = open(filename, 'r')
        
        # Let's do a quick pass where we find out the earliest time we see...
        # This will end up being the first depth 1 we see, assuming there is
        #  one.  We'll assume so, otherwise we'd want to just do minimization
        #  logic for fallback or canon.
        start_ts = 0
        for line in f:
            line = line.strip()
            if not ',' in line:
                continue
            
            depth_str, ts_str, te_str, filename, funcname = line.split(',')
            depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
            
            if depth == 1:
                start_ts = ts
                break
        
        # because trace events are generated only on function returns, we
        #  need to accumulate things until we hit our parents...
        MAX_RECURSE_DEPTH = 256
        deferreds = [list() for i in range(MAX_RECURSE_DEPTH)]
        
        for line in f:
            line = line.strip()
            if not ',' in line:
                continue
            
            depth_str, ts_str, te_str, filename, funcname = line.split(',')
            depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
            
            ts -= start_ts
            te -= start_ts
            
            vfunc = self._get_vfunc(filename, funcname)
            this_invoc = vfunc.invoke(ts, te, depth, depth)
            deferreds[depth-1].append(this_invoc)
            
            if deferreds[depth]:
                for deferred in deferreds[depth]:
                    vfunc.invoc_called(this_invoc, deferred)
                deferreds[depth] = list()
