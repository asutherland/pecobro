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

import genshi.template, genshi.template.loader, genshi

import pygments
import pygments.lexers
import pygments.formatters

import pecobro.mozpreproc as mozpreproc
import pecobro.xbl as xbl
import pecobro.core as core
import pecobro.codefmt as codefmt
import pecobro.trace as trace
import pecobro.vis as vis
import pecobro.consts as consts

XBL_NS = 'http://www.mozilla.org/xbl'

#from IPython.Shell import IPShellEmbed
#ipshell = IPShellEmbed()

class Generator(object):
    def __init__(self, code_dirs=()):
        self.code_dirs = list(code_dirs)
        
        self.caboodle = core.SourceCaboodle()
    
    def _consider_xml(self, code_path, base_path, path):
        print 'CONSIDERING', path
        # grrrrr, we need to preprocess things now...
        f_in = open(path, 'r') #codecs.open(path, 'r', 'utf-8')
        f_out = StringIO.StringIO()
        mozpreproc.preprocess(includes=[f_in], defines=consts.defines,
                              output=f_out,
                              line_endings='lf')
        f_in.close()
        f_out.seek(0)
        
        doc = etree.parse(f_out, xbl.ChromeTreeBuilder(base_path=base_path))
        f_out.close()
        
        #doc = etree.parse(path_or_file)
        root = doc.getroot()
        
        #print '  root', dir(root)
        
        if root.tag.startswith('{%s}' % XBL_NS):
            print 'Found XBL:', path
            self.caboodle.append(core.SourceFile(path, 'xbl',
                                                 base_dir=base_path,
                                                 eRoot=root))
        else:
            print '  non-XBL:', path
    
    def find_code(self):
        for code_dir, base_dir in self.code_dirs:
            for dirpath, dirnames, filenames in os.walk(code_dir):
                # don't walk into test subdirs for now...
                if 'test' in dirnames:
                    del dirnames[dirnames.index('test')]
                
                for filename in filenames:
                    trash, suffix = os.path.splitext(filename)
                    filepath = os.path.join(dirpath, filename)
            
                    if suffix in ('.js', '.jsm'):
                        print 'Found JS:', filepath
                        self.caboodle.append(core.SourceFile(filepath,
                                                             suffix[1:],
                                                             base_dir=base_dir))
                        pass 
                    elif suffix in ('.xml',):
                        self._consider_xml(code_dir, base_dir, filepath)

    def parse_trace(self, trace_file):
        parser = trace.TraceParser(self.caboodle)
        parser.parse(trace_file)

    def output_html(self, out_path):
        if not os.path.isdir(out_path):
            os.makedirs(out_path)
        
        # -- Figure out paths...
        our_path = os.path.dirname(core.__file__)
        template_dir = os.path.join(our_path, 'templates')
        static_dir = os.path.join(our_path, 'static')
        
        loader = genshi.template.loader.TemplateLoader([template_dir])
        
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
        formatter = codefmt.CodeFormatter(style='manni')
        
        index_tmpl = loader.load('index.html')
        index_stream = index_tmpl.generate(caboodle=self.caboodle,
                                           pygments_style_defs=formatter.get_style_defs())
        # for mime type reasons, be an xml file.
        index_path = os.path.join(out_path, 'index.xml')
        
        f_index = codecs.open(index_path, 'w', 'utf-8')
        f_index.write(index_stream.render())
        f_index.close()
        
        print '  -- generating vis (%d relevant files)' % (len(self.caboodle.relevant_source_files),)
        overview_path = os.path.join(out_path, 'overview.svg')
        vis.file_overview(self.caboodle, overview_path)
        
        #return
        
        import jsparse.jsparse as jsparse
        
        func_list_tmpl = loader.load('func_list.html')
        file_index_tmpl = loader.load('file_index.html')
        
        xblp = xbl.XBLParser()
        
        for source_file in self.caboodle.source_files:
            #if not source_file.base_name in ['calUtils.js', 'calEvent.js']: continue
            #if not source_file.base_name in ['calDavCalendar.js']: continue
            #if not source_file.base_name in ['aboutDialog.js']: continue
            #if not source_file.base_name in ['calendar-view-core.xml']: continue
            
            print '   - Parsing', source_file
            if source_file.filetype.startswith('js'):
                jsparse.sf_process(source_file, cache_dir='/tmp/pecobro_cache')
            elif source_file.filetype == 'xbl':
                xblp.parse(source_file)
            # er, XBL in theory should already be processed, what with us
            #  having to parse the XML to figure out if it is XML.  (well, I
            #  guess we didn't have to full parse it)
            
            print '   - Generating', source_file
            fcode = open(source_file.path, 'r')
            code = fcode.read()
            fcode.close()
            
            if source_file.filetype == 'xbl':
                lexer = codefmt.XmlJsFusionLexer()
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
            

if __name__ == '__main__':
    gen = Generator([('/home/visbrero/vc_mirrors/mozilla-git-mirror/calendar',
                      '/home/visbrero/vc_mirrors/mozilla-git-mirror'),
                     ('/home/visbrero/vc_mirrors/mozilla-git-mirror/toolkit/content/widgets',
                      '/home/visbrero/vc_mirrors/mozilla-git-mirror')])
    print '--- finding code ---'
    gen.find_code()
    print '--- parsing trace ---'
    gen.parse_trace('/home/visbrero/projects/perf/bob.log')
    print '--- generating output ---'
    gen.output_html('/tmp/pecobro')
