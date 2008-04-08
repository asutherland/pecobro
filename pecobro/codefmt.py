import pygments
import pygments.lexers
import pygments.formatters

import pecobro.vis as vis

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
                    yield 0, '<span id="func|%s" class="fhdr">%s</span>' % (nextFunc.norm_name,
                                                             nextFunc.name)
                    if nextFunc.invocations:
                        yield 0, vis.func_time_slices(nextFunc)
                    
                    yield 0, '\n'
                    nextFunc = next_contents()
                
                yield t, line
            else:
                yield t, line
