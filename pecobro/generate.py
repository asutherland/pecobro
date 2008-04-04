import os, os.path, shutil
try:
    #import xml.etree.cElementTree as etree
    import xml.etree.ElementTree as etree
except:
    import xml.etree.ElementTree as etree

import codecs

import genshi.template, genshi.template.loader

import pygments
import pygments.lexers
import pygments.formatters


# the absolute import explodes for unknown reasons I don't care about right now
import xbl
# didn't try these absolute though...
import core
import codefmt

XBL_NS = 'http://www.mozilla.org/xbl'

class Generator(object):
    def __init__(self, code_dirs=()):
        self.code_dirs = list(code_dirs)
        
        self.code_files = []
    
    def _consider_xml(self, base_path, path):
        #print 'CONSIDERING', path_or_file
        doc = etree.parse(path, xbl.ChromeTreeBuilder(base_path=base_path))
        #doc = etree.parse(path_or_file)
        root = doc.getroot()
        
        #print '  root', dir(root)
        
        if root.tag.startswith('{%s}' % XBL_NS):
            print 'Found XBL:', path
            self.code_files.append(core.SourceFile(path, 'xbl'))
        else:
            print '  non-XBL:', path
    
    def find_code(self):
        for code_dir in self.code_dirs:
            for dirpath, dirnames, filenames in os.walk(code_dir):
                for filename in filenames:
                    trash, suffix = os.path.splitext(filename)
                    filepath = os.path.join(dirpath, filename)
            
                    if suffix in ('.js', '.jsm'):
                        print 'Found JS:', filepath
                        self.code_files.append(core.SourceFile(filepath,
                                                               suffix[1:]))
                        pass 
                    elif suffix in ('.xml',):
                        self._consider_xml(code_dir, filepath)

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
        self.code_files.sort(key=lambda x: x.norm_base_name)
        
        formatter = codefmt.CodeFormatter()
        
        index_tmpl = loader.load('index.html')
        index_stream = index_tmpl.generate(code_files=self.code_files,
                                           pygments_style_defs=formatter.get_style_defs())
        # for mime type reasons, be an xml file.
        index_path = os.path.join(out_path, 'index.xml')
        
        f_index = codecs.open(index_path, 'w', 'utf-8')
        f_index.write(index_stream.render())
        f_index.close()
        
        return
        
        for code_file in self.code_files:
            print '*** Generating', code_file
            fcode = open(code_file.path, 'r')
            code = fcode.read()
            fcode.close()
            
            lexer = pygments.lexers.get_lexer_for_filename(code_file.path)
            formatter = codefmt.CodeFormatter()
            
            webbed = pygments.highlight(code, lexer, formatter)
            
            out_wcode_path = os.path.join(out_path,
                                          code_file.norm_base_name + '.xml')
            fweb = codecs.open(out_wcode_path, 'w', 'utf-8')
            fweb.write('''<?xml version="1.0"?><div xmlns="http://www.w3.org/1999/xhtml">''')
            fweb.write(webbed)
            fweb.write('</div>')
            fweb.close()
            

if __name__ == '__main__':
    gen = Generator(['/home/visbrero/vc_mirrors/mozilla-git-mirror/calendar'])
    gen.find_code()
    gen.output_html('/tmp/pecobro')