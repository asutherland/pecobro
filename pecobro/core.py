import os.path

class SourceFunc(object):
    def __init__(self, source_file, clazz, func_name):
        self.file = source_file
        self.clazz = clazz
        self.func_name

class SourceFile(object):
    def __init__(self, path, file_type):
        self.path     = path
        self.filetype = file_type
        
        self.base_name = os.path.basename(path)
        self.norm_base_name = os.path.basename(path).replace('.', '_')
    
    def __str__(self):
        return 'SourceFile: %s' % (self.path,)
