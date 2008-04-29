import codecs, os, os.path

try:
    import cStringIO as StringIO
except:
    import StringIO

import pecobro.mozpreproc as mozpreproc
import pecobro.consts as consts

class JarManifestParser(object):
    def __init__(self, caboodle):
        self.caboodle = caboodle
    
    def _parse_file(self, f, fname):
        manifest_dir = os.path.dirname(os.path.abspath(fname))
        
        for line in f:
            line = line.rstrip()
            
            if len(line) == 0:
                continue
            
            # -- a file to be packaged!
            if line[0] in (' ', '\t', '*', '+'):
                # we don't care about the flags; we always pre-process things
                #  for now anyways.
                if line[0] in ('*', '+'):
                    line = line[line.index(' '):]
                line = line.lstrip()
                
                jar_path, paren_fs_path = line.split()
                fs_path = paren_fs_path[1:-1]
                
                # locale-case
                if fs_path[0] == '%':
                    path = os.path.join('en-US', fs_path[1:])
                # (absolute) relative to mozilla/
                elif fs_path == '/':
                    path = os.path.join(self.caboodle.moz_path, fs_path[1:])
                # relative to this manifest...
                else:
                    path = os.path.join(manifest_dir, fs_path)
                
                self.caboodle.chrome_map[jar_path] = path
                print '  %s -> %s' % (jar_path, path)
            # -- a jar file
            elif line.endswith(':'):
                pass
            else:
                raise Exception('Unable to process jar manifest line: %s' %
                                (line,))
            
    
    def parse(self, fname):
        f_in = codecs.open(fname, 'r', 'latin1')
        sio = StringIO.StringIO()
        f_out = codecs.getwriter('utf-8')(sio)
        mozpreproc.preprocess(includes=[f_in], defines=consts.defines,
                              output=f_out,
                              line_endings='lf')
        f_in.close()
        sio.seek(0)
        
        self._parse_file(sio, fname)
