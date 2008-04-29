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
        
        pkg_name = None
        pkg_locale = None
        pkg_prepend = None
        pkg_replace = None
        pkg_path_maps = []
        for line in f:
            line = line.rstrip()
            
            if len(line) == 0:
                continue

            # -- a chrome directive and what not
            if line[0] == '%':
                # packagetype packagename path flags
                parts = line[1:].split()
                pkg_type = parts[0]
                if pkg_type == 'content':
                    pkg_ignore = False
                    pkg_name = parts[1]
                    pkg_prepend = os.path.join(pkg_name, pkg_type)
                    pkg_replace = parts[2][1:]
                    if pkg_replace.endswith('/'):
                        pkg_prepend += '/'
                    pkg_path_maps.append((pkg_replace, pkg_name, pkg_prepend))
                elif pkg_type in ('locale', 'skin'):
                    pkg_ignore = False
                    pkg_name = parts[1]
                    pkg_locale = parts[2]
                    # we do _not_ want the locale in there, there should only
                    #  be one at this point...
                    pkg_prepend = os.path.join(pkg_name, pkg_type)
                    pkg_replace = parts[3][1:]
                    if pkg_replace.endswith('/'):
                        pkg_prepend += '/'
                    pkg_path_maps.append((pkg_replace, pkg_name, pkg_prepend))
                else:
                    pass
                #elif pkg_type == 'skin':
                #    pass
                #elif pkg_type == 'style':
                #    pass
                #elif pkg_type == 'override':
                #    pass
                #elif pkg_type == 'resource':
                #    pass
                
            # -- a file to be packaged!
            elif line[0] in (' ', '\t', '*', '+'):
                # we don't care about the flags; we always pre-process things
                #  for now anyways.
                if line[0] in ('*', '+'):
                    line = line[line.index(' '):]
                line = line.lstrip()
                
                # uh, some things don't have the "foo (bar)" syntax; assuming
                #  that if omitted, we should use the foo again...
                if '(' in line:
                    jar_path, paren_fs_path = line.split()
                    fs_path = paren_fs_path[1:-1]
                else:
                    jar_path = line.strip()
                    fs_path = os.path.basename(jar_path)
                
                # locale-case
                if fs_path[0] == '%':
                    path = os.path.join(manifest_dir, 'en-US', fs_path[1:])
                # (absolute) relative to mozilla/
                elif fs_path[0] == '/':
                    path = os.path.join(self.caboodle.moz_src_path, fs_path[1:])
                # relative to this manifest...
                else:
                    path = os.path.join(manifest_dir, fs_path)
                # maybe it had an '.in' friend... maybe we should just append
                #  .in instead?  dunno... TODO: consider consuming .in files?
                if not os.path.exists(path):
                    path = path.replace(self.caboodle.moz_src_path,
                                        self.caboodle.moz_build_path)
                if not os.path.exists(path):
                    raise Exception("Tried to map %s to %s." % (fs_path, path))
                
                # if we were provide explicit chrome directives, use those
                chrome_path = None
                if pkg_path_maps:
                    if jar_path.startswith('chrome://'):
                        chrome_path = jar_path[9:]
                    else:
                        for pkg_replace, pkg_name, pkg_prepend in pkg_path_maps:
                            if jar_path.startswith(pkg_replace):
                                chrome_path = jar_path.replace(pkg_replace,pkg_prepend)
                                break
                # without chrome directives, we must infer things from paths...
                if chrome_path is None and jar_path.count('/') >= 2:
                    # like actual chrome directives, the number of path
                    #  segments dedicated to the encoding varies by the type;
                    #  extract it so we can differentiate and further process
                    this_pkg_type, rem_path = jar_path.split('/', 1)
                    if this_pkg_type == 'content':
                        # (content/)pkg_name/...
                        # and we want pkg_name/content/...
                        this_pkg_name, rem_path = rem_path.split('/', 1)
                        chrome_path = os.path.join(this_pkg_name,
                                                   this_pkg_type,
                                                   rem_path)
                        
                    elif this_pkg_type in ('locale', 'skin') and rem_path.count('/') >= 2:
                        # (locale/)AB_CD/pkg_name/...
                        # and we want pkg_name/locale/...
                        # (we don't want the specific locale; only one should
                        #  exist at this point.)
                        this_locale, this_pkg_name, rem_path = rem_path.split('/', 2)
                        chrome_path = os.path.join(this_pkg_name,
                                                   this_pkg_type,
                                                   rem_path)
                    else:
                        chrome_path = None
                
                if chrome_path:
                    self.caboodle.chrome_map[chrome_path] = path
                print '  %s -> %s' % (chrome_path, path)
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
