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

import os, os.path, shutil
try:
    #import xml.etree.cElementTree as etree
    import xml.etree.ElementTree as etree
except:
    import xml.etree.ElementTree as etree

import codecs
try:
    import cStringIO as StringIO
except:
    import StringIO

try:
    import cerealizer
except:
    cerealizer = None

import genshi.template, genshi.template.loader, genshi

import pygments
import pygments.lexers
import pygments.formatters

import pecobro.mozpreproc as mozpreproc
import pecobro.xbl as xbl
import pecobro.core as core
import pecobro.codefmt as codefmt
import pecobro.jarman as jarman
import pecobro.trace as trace
import pecobro.vis as vis
import pecobro.consts as consts
import pecobro.makeparser as makeparser

XBL_NS = 'http://www.mozilla.org/xbl'

try:
    from IPython.Shell import IPShellEmbed
    ipshell = IPShellEmbed(['-pdb'])
except:
    pass

class Generator(object):
    def __init__(self, moz_src_path, project, moz_build_path,
                 cache_dir=None,
                 remote_src_path=None, remote_build_path=None,
                 overlay_dirs=()):
        # okay, we actually want to parameterize our cache a little
        if cache_dir:
            cache_dir = os.path.join(cache_dir, '%x' % (abs(hash(moz_build_path)),))
        if not os.path.isdir(cache_dir):
            try:
                os.makedirs(cache_dir)
            except:
                cache_dir = None
        self.cache_dir = cache_dir
        
        self.path_maps = []
        if remote_build_path:
            self.path_maps.append((remote_build_path, moz_build_path))
        if remote_src_path:
            self.path_maps.append((remote_src_path, moz_src_path))

        client_mk_path = os.path.join(moz_src_path, 'client.mk')
        if not os.path.isfile(client_mk_path):
            raise Exception("There is no client.mk at %s, what am I supposed to do?" %
                            (client_mk_path,))
        
        mf = makeparser.Makefile(force={'TOPSRCDIR': moz_src_path},
                                 path_maps=self.path_maps)
        mf.parse(client_mk_path)
        # the NS stuff is for checkout perhaps?
        module_dirs_str = mf.get('MODULES_%s' % (project,))
        locale_dirs_str = mf.get('LOCALES_%s' % (project,))
        
        module_dirs = [os.path.join(moz_build_path, md.split('/', 1)[1]) for md in
                       module_dirs_str.split()]
        locale_dirs = [os.path.join(moz_build_path, md) for md in
                       locale_dirs_str.split()]
        
        self.caboodle = core.SourceCaboodle(moz_src_path, moz_build_path,
                                            project,
                                            module_dirs=module_dirs,
                                            locale_dirs=locale_dirs,
                                            overlay_dirs=overlay_dirs)
    
    def _consider_xml(self, path, defines=None):
        if defines is None:
            defines = self.defines 
        print 'CONSIDERING', path
        # grrrrr, we need to preprocess things now...
        f_in = open(path, 'r') #codecs.open(path, 'r', 'utf-8')
        f_out = StringIO.StringIO()
        mozpreproc.preprocess(includes=[f_in], defines=defines,
                              output=f_out,
                              line_endings='lf',
                              # we do not want those //@ line things, they
                              #  screw up our consistency with reality. 
                              line_updates=False,
                              )
        f_in.close()
        f_out.seek(0)
        
        doc = etree.parse(f_out, xbl.ChromeTreeBuilder(caboodle=self.caboodle))
        f_out.close()
        
        #doc = etree.parse(path_or_file)
        root = doc.getroot()
        
        #print '  root', dir(root)
        
        if root.tag.startswith('{%s}' % XBL_NS):
            print 'Found XBL:', path
            # we don't need to set used_codec because we didn't use one...
            self.caboodle.append(core.SourceFile(path, 'xbl',
                                                 base_dir=self.caboodle.moz_src_path,
                                                 eRoot=root,
                                                 defines=defines))
        else:
            print '  non-XBL:', path
    
    def _parse_defines(self, *defines_strs):
        defines = {}
        for defines_str in defines_strs:
            for dash_d in defines_str.split():
                if dash_d.startswith('-D'):
                    dash_d = dash_d[2:]
                    if '=' in dash_d:
                        key, value = dash_d.split('=',1)
                        # er, I guess quotes would lose their escaping
                        #  in reality?  or would the quotes bail too?
                        value = value.replace('\\"', '"')
                    else:
                        key = dash_d
                        value = True
                    defines[key] = value
        return defines
        
    def _find_jars(self):
        '''
        Given the module_dirs and locale_dirs extracted from client.mk (but
        make relative to the build dir) for the given project as a set of
        starting directories, parse the Makefiles in those directories,
        recursing if we haven't yet processed them.  For every directory, see
        if there is a jar.mn manifest file, and if so, process it.
        
        The result of this call is that self.caboodle.chrome_map will have
        entries for all the files that could be used by the system in the
        existing configuration.  We use this both for DTD resolution in XBL
        processing and also as our means of finding source files of interest. 
        
        This is very expensive, so we have a cached wrapped helper, find_jars.
        '''
        jmp = jarman.JarManifestParser(self.caboodle)
        seen_dirs = set()
        
        print 'Scanning %d module dirs, %d locale dirs' % (
                len(self.caboodle.module_dirs), len(self.caboodle.locale_dirs))
        
        def check_path(path):
            seen_dirs.add(path)
            print 'visiting dir', path
            
            # okay, the path is going to be in the build hierarchy, let's get
            #  a corresponding source path
            src_path = path.replace(self.caboodle.moz_build_path,
                                    self.caboodle.moz_src_path)
            
            cand_jar_name = os.path.join(src_path, 'jar.mn')
            #print 'checking', cand_jar_name
            
            cand_makefile = os.path.join(path, 'Makefile')
            if os.path.isfile(cand_makefile):
                #print 'parsing', cand_makefile
                mf = makeparser.Makefile(
                             force={'TOPSRCDIR': self.caboodle.moz_src_path},
                             path_maps=self.path_maps)
                mf.parse(cand_makefile)
                
                defines = self._parse_defines(mf.get('DEFINES'),
                                              mf.get('ACDEFINES'),
                                              mf.get('XULPPFLAGS'))
                
                if os.path.isfile(cand_jar_name):
                    print 'PARSING', cand_jar_name
                    # use the Makefile's resulting variables...
                    print '...', defines
                    jmp.parse(cand_jar_name, defines=defines)
            
                
                # things in EXTRA_COMPONENTS or EXTRA_PP_COMPONENTS hop right on
                for rel_component in (mf.get('EXTRA_COMPONENTS').split() +
                                      mf.get('EXTRA_PP_COMPONENTS').split()):
                    abs_component = os.path.join(path, rel_component)
                    # map them from remote to local paths, if relevant
                    for path_from, path_to in self.path_maps:
                        if abs_component.startswith(path_from):
                            abs_component = abs_component.replace(path_from, path_to)
                    # flop from the build dir to the source dir if relevant
                    if not os.path.exists(abs_component):
                        abs_component = abs_component.replace(self.caboodle.moz_build_path,
                                                              self.caboodle.moz_src_path)
                    if not abs_component in self.caboodle.components:
                        print 'COMPONENT', abs_component
                        self.caboodle.components.append((defines, abs_component))

                # EXTRA_(PP_)JS_MODULES
                for rel_module in (mf.get('EXTRA_JS_MODULES').split() +
                                   mf.get('EXTRA_PP_JS_MODULES').split()):
                    abs_module = os.path.join(path, rel_module)
                    # map them from remote to local paths, if relevant
                    for path_from, path_to in self.path_maps:
                        if abs_module.startswith(path_from):
                            abs_module = abs_module.replace(path_from, path_to)
                    # flop from the build dir to the source dir if relevant
                    if not os.path.exists(abs_module):
                        abs_module = abs_module.replace(self.caboodle.moz_build_path,
                                                        self.caboodle.moz_src_path)
                    if not abs_module in self.caboodle.modules:
                        print 'MODULE', abs_module
                        self.caboodle.modules.append((defines, abs_module))

                
                # recurse into DIRS and TOOL_DIRS; also STATIC_DIRS just in case
                for make_dir in (mf.get('DIRS').split()
                                 + mf.get('TOOL_DIRS').split()
                                 + mf.get('STATIC_DIRS').split()
                                 ):
                    make_path = os.path.join(path, make_dir)
                    if not make_path in seen_dirs:
                        check_path(make_path)
                
                # DIRS
                # STATIC_DIRS
                # TOOL_DIRS
                
                # TIERS -> tier_*_dirs
            elif os.path.isfile(cand_jar_name):
                # TODO: use better defaults for defines
                print 'PARSING', cand_jar_name
                print '... (default defines)'
                jmp.parse(cand_jar_name)
                
        # since we are now so clever, let's just walk from the root Makefile...
        # (we used to process caboodle.module_dirs + caboodle.locale_dirs
        check_path(self.caboodle.moz_build_path)
    
    def find_jars(self):
        '''
        Because _find_jars is so expensive, we attempt to cache the results of
        running that here...  See _find_jars for info on the actual logic.
        '''
        cache_file = None
        if self.cache_dir and cerealizer:
            cache_file = os.path.join(self.cache_dir, 'chrome-map.cereal')
            
            if os.path.isfile(cache_file):
                f = open(cache_file, 'rb')
                jar_info = cerealizer.load(f)
                self.caboodle.chrome_map = jar_info['chrome_map']
                self.caboodle.components = jar_info['components']
                self.caboodle.modules    = jar_info['modules']
                f.close()
                return
        
        self._find_jars()
        
        if cache_file:
            f = open(cache_file, 'wb')
            jar_info = {'chrome_map': self.caboodle.chrome_map,
                        'components': self.caboodle.components,
                        'modules': self.caboodle.modules,
                        }
            cerealizer.dump(jar_info, f)
            f.close()
        
    
    def find_code(self):
        '''
        Walk the listing of all the files known to us in the caboodle chrome_map
        and process any that are of interest to us based on their extension.
        
        We used to just walk some user-provided paths with a heuristic that
        stopped us from going into anything that had 'test' in it.  Now we are
        ever so much more fancy.
        '''
        import glob

        # we want to know the preprocessor defines, so grab them out of
        #  autoconf.mk.  we could alternatively have stashed them earlier, but
        #  we know they're in this file, so let's just run with that...
        mf = makeparser.Makefile(
                     force={'TOPSRCDIR': self.caboodle.moz_src_path},
                     path_maps=self.path_maps)
        mf.parse(os.path.join(self.caboodle.moz_build_path, 'config/autoconf.mk'))
        self.defines = self._parse_defines(mf.get('ACDEFINES'))
        
        overlay_files = []
        for overlay_dir in self.caboodle.overlay_dirs:
            for overlay_file in glob.glob(os.path.join(overlay_dir, '*.js')):
                overlay_files.append((self.defines, overlay_file))
        
        for defines, src_abs_filepath in (overlay_files +
                                 self.caboodle.components +
                                 self.caboodle.modules +
                                 self.caboodle.chrome_map.values()):
            filename = os.path.basename(src_abs_filepath)
            trash, suffix = os.path.splitext(filename)

            if suffix in ('.js', '.jsm'):
                print 'Found JS:', src_abs_filepath
                self.caboodle.append(core.SourceFile(src_abs_filepath,
                                                     suffix[1:],
                                                     base_dir=self.caboodle.moz_src_path,
                                                     defines=defines))
                pass 
            elif suffix in ('.xml',):
                self._consider_xml(src_abs_filepath, defines)

    def parse_trace(self, trace_file):
        import jsparse.jsparse as jsparse
        xblp = xbl.XBLParser()

        for source_file in self.caboodle.source_files:
            #if not source_file.base_name in ['calUtils.js', 'calEvent.js']: continue
            #if not source_file.base_name in ['calDavCalendar.js']: continue
            #if not source_file.base_name in ['aboutDialog.js']: continue
            #if not source_file.base_name in ['calendar-view-core.xml']: continue

            ## DEBUG!!
            #if source_file.base_name != 'dialog.xml':
            #    continue
            
            print '   - Parsing', source_file
            if source_file.filetype.startswith('js'):
                jsparse.sf_process(source_file, cache_dir=self.cache_dir,
                                   defines=source_file.defines)
            elif source_file.filetype == 'xbl':
                xblp.parse(source_file)
            
            ## DEBUG!!
            #ipshell()

        parser = trace.TraceParser(self.caboodle)
        parser.parse(trace_file)

    def generate_index(self):
        formatter = codefmt.CodeFormatter(style='manni')
        
        index_tmpl = self.loader.load('index.html')
        index_stream = index_tmpl.generate(caboodle=self.caboodle,
                                           pygments_style_defs=formatter.get_style_defs())
        # for mime type reasons, be an xml file.
        index_path = os.path.join(self.out_path, 'index.xml')
        
        f_index = codecs.open(index_path, 'w', 'utf-8')
        f_index.write(index_stream.render())
        f_index.close()

    def output_html(self, out_path):
        self.out_path = out_path
        
        if not os.path.isdir(out_path):
            os.makedirs(out_path)
        
        # -- Figure out paths...
        our_path = os.path.dirname(core.__file__)
        template_dir = os.path.join(our_path, 'templates')
        static_dir = os.path.join(our_path, 'static')
        
        self.loader = genshi.template.loader.TemplateLoader([template_dir])
        
        # -- Copy Static Files
        for fname in os.listdir(static_dir):
            # er, no need of our __init__.py if it exists
            if not fname.endswith('.py'):
                in_file = os.path.join(static_dir, fname)
                out_file = os.path.join(out_path, fname)
                if os.path.isfile(in_file):
                    shutil.copyfile(in_file, out_file)
                else:
                    # don't recursive copy every time...
                    if not os.path.exists(out_file):
                        shutil.copytree(in_file, out_file, False)

        
        # -- Index File
        print ' -- generating index'
        self.generate_index()
        
        print '  -- generating vis (%d relevant files)' % (len(self.caboodle.relevant_source_files),)
        overview_path = os.path.join(out_path, 'overview.svg')
        vis.file_overview(self.caboodle, overview_path)
        
        #return
        
        func_list_tmpl = self.loader.load('func_list.html')
        file_index_tmpl = self.loader.load('file_index.html')
        syn_file_tmpl = self.loader.load('synth_file.html')
        
        for source_file in self.caboodle.source_files:
            print '   - Generating', source_file

            if source_file.filetype == 'synthetic':
                out_wcode_path = os.path.join(out_path,
                                              source_file.norm_base_name + '.xml')
                fweb = codecs.open(out_wcode_path, 'w', 'utf-8')
                
                syn_file_stream = syn_file_tmpl.generate(
                                        source_file=source_file,
                                        func_time_slices=vis.func_time_slices,
                                        XML=genshi.XML)
                fweb.write(syn_file_stream.render())
                                
                fweb.close()

                continue
            

            # okay, we need to pre-process this.  we actually have all the
            #  ingredients required to reverse the pre-processing to the
            #  original line numbers so we can show what is in source control,
            #  but we don't do that.  Also, there are there is the '.in'
            #  phenomenon to deal with...
            ## er, looks like maybe we don't need to roll with the codec?
            if False: # source_file.used_codec:
                f_in = codecs.open(source_file.path, 'r',
                                   source_file.used_codec)
            else:
                f_in = open(source_file.path, 'r')
            f_out = StringIO.StringIO()
            mozpreproc.preprocess(includes=[f_in], defines=source_file.defines,
                                  output=f_out,
                                  line_endings='lf',
                                  # we do not want those //@ line things for XBL
                                  line_updates=(source_file.filetype != 'xbl'),
                                  )
            f_in.close()
            code = f_out.getvalue()
            f_out.close()
            
            if source_file.filetype == 'xbl':
                lexer = codefmt.XmlJsFusionLexer()
            elif source_file.filetype in ('js', 'jsm'):
                lexer = pygments.lexers.get_lexer_by_name('javascript')
            else:
                lexer = pygments.lexers.get_lexer_for_filename(source_file.path)
            formatter = codefmt.CodeFormatter(linenos='inline',
                                              source_file=source_file)            
            
            out_wcode_path = os.path.join(out_path,
                                          source_file.norm_base_name + '.xml')
            fweb = codecs.open(out_wcode_path, 'w', 'utf-8')
            fweb.write('''<?xml version="1.0"?><div xmlns="http://www.w3.org/1999/xhtml" xmlns:svg="http://www.w3.org/2000/svg">''')

            func_list_stream = func_list_tmpl.generate(source_file=source_file,
                                                       func_time_slices=vis.func_time_slices,
                                                       XML=genshi.XML)
            fweb.write(func_list_stream.render())
            
            file_index_stream = file_index_tmpl.generate(source_file=source_file)
            fweb.write(file_index_stream.render())

            fweb.write('<div>')
            fweb.write('<h1>%s</h1>' % (source_file.norm_path,))
            webbed = pygments.highlight(code, lexer, formatter)                        
            fweb.write(webbed)
            fweb.write('</div>')
            
            fweb.write('</div>')
            fweb.close()
    
    def main(self):
        self.find_jars()
        self.find_code()

if __name__ == '__main__':
#    gen = Generator([('/home/visbrero/vc_mirrors/mozilla-git-mirror/calendar',
#                      '/home/visbrero/vc_mirrors/mozilla-git-mirror'),
#                     ('/home/visbrero/vc_mirrors/mozilla-git-mirror/toolkit/content/widgets',
#                      '/home/visbrero/vc_mirrors/mozilla-git-mirror')])
    mac = True
    if mac:
        tb_build_dir = '/home/visbrero/mnt/roisin/rev_control/hg/mozilla/obj-thunderbird-generic/'
        tb_src_dir = '/home/visbrero/mnt/roisin/rev_control/hg/mozilla/'
        remote_build_dir = '/Users/sombrero/rev_control/hg/mozilla/obj-thunderbird-generic/'
        remote_src_dir = '/Users/sombrero/rev_control/hg/mozilla/'
        chrome_dir = '/home/visbrero/mnt/roisin/rev_control/hg/mozilla/obj-thunderbird-generic/dist/Thunderbird.app/Contents/MacOS/chrome/'
        overlay_dirs=[chrome_dir]
    else:
        tb_build_dir = '/home/visbrero/rev_control/hg/moz-mac/mozilla/obj-thunderbird-generic/'
        tb_src_dir = '/home/visbrero/rev_control/hg/moz-mac/mozilla/'
        remote_build_dir = remote_src_dir = None
        overlay_dirs = []
    #trace_file = '/home/visbrero/projects/perf/bloat-context-script.log'
    #out_dir = '/tmp/pecobro'
    trace_file = '/home/visbrero/projects/perf/del-trimmed.log'
    out_dir = '/tmp/pecobro2'
    
    gen = Generator(tb_src_dir, 'mail', tb_build_dir,
                    cache_dir='/tmp/pecobro_cache',
                    remote_src_path=remote_src_dir,
                    remote_build_path=remote_build_dir,
                    overlay_dirs=overlay_dirs)
    print '--- finding code ---'
    gen.main()
    print '--- parsing trace ---'
    gen.parse_trace(trace_file)
    print '--- generating output ---'
    gen.output_html(out_dir)
