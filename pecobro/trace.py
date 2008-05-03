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

# todo: make absolute
import core

class TraceParser(object):
    def __init__(self, caboodle, *args, **kwargs):
        self.caboodle = caboodle

    def parse(self, filename):
        func_cache = {}
        def get_synthetic_func(objname, funcname):
            '''
            For native functions, create a synthetic file if it does not exist
            and a synthetic function in that file if it does not exist.
            '''
            synth_file = self.caboodle.base_name_to_file.get(objname)
            if synth_file is None:
                synth_file = core.SourceFile(objname, 'synthetic')
                self.caboodle.append(synth_file)
            
            func, created = synth_file.get_or_create_function(funcname)
            return func
        
        def get_func(filename, funcname, lineno):
            '''
            Given a filename and lineno (and ignoring the funcname), look-up the
            function in the given file.
            '''
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
                (line_type, context_str, depth_str, ts_str, te_str,
                    filename, objname, funcname,
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
        MAX_RECURSE_DEPTH = 128
        context_to_deferreds = {}
        
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
            
            (line_type, context_str_, depth_str, ts_str, te_str,
                filename, objname, funcname,
                lineno_str, caller_filename, caller_lineno_str
                ) = line.split(',')
            depth, ts, te = int(depth_str, 16), int(ts_str, 16), int(te_str, 16)
            lineno = int(lineno_str)
            
            ts -= start_ts
            te -= start_ts

            # -- find our function and log this invocation of our function
            # brutally mis-attribute .xul files for now using the last func
            if filename.endswith('.xul'):
                pass
            # the native function case; use a synthetic function
            elif filename == '<null>':
                # okay, so in this case objname is a real thing, and funcname
                #  is a real function name, but our source_file stuff will know
                #  nothing about them...
                func = get_synthetic_func(objname, funcname)
            # an interpreted function; use our awesome parsing results
            else:
                func = get_func(filename, funcname, lineno)
            this_invoc = func.log_invoke(ts, te, depth, depth)
            
            if context_str in context_to_deferreds:
                deferreds = context_to_deferreds[context_str]
            else:
                deferreds = [list() for i in range(MAX_RECURSE_DEPTH)]
                context_to_deferreds[context_str] = deferreds
            
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
