import pygments
import pygments.lexers
import pygments.formatters

class CodeFormatter(pygments.formatters.HtmlFormatter):
    def __init__(self, **options):
        pygments.formatters.HtmlFormatter.__init__(self, **options)
        
        self.source_file = options.get('source_file')
    
    def wrap(self, source, outfile):
        source = pygments.formatters.HtmlFormatter.wrap(self, source, outfile)
        
        return self._wrap_executed(source)
    
    def _wrap_executed(self, source):
        cur_line = 0
        
        if self.source_file:
            iContents = iter(self.source_file.contents)
        else:
            iContents = iter(())
        
        nextFunc = None
        
        def next_contents():
            try:
                return iContents.next()
            except:
                return None
        nextFunc = next_contents()
        
        for t, line in source:
            if t == 1:
                cur_line += 1
                
                if nextFunc and nextFunc.source_line == cur_line:
                    yield 0, '<h3 id="func|%s">%s</h3>\n' % (nextFunc.norm_name,
                                                             nextFunc.name)
                    nextFunc = next_contents()
                
                yield t, line
            else:
                yield t, line
