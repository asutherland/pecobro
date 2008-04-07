from xml import etree
try:
    #import xml.etree.cElementTree as etree
    import xml.etree.ElementTree as etree
except:
    #import xml.etree.ElementTree as etree
    pass
try:
    import cStringIO as StringIO
except:
    import StringIO

import xml.parsers.expat as expat
import codecs, os.path

import pecobro.mozpreproc as mozpreproc
import pecobro.consts as consts 

BASE_PATH = None
# okay, this is a hack, we really should just parse whatever the
#  underlying rdf file is or what not, but this works for now...
CHROME_MAP = {'calendar' : {'locale': ('calendar/locales/en-US/chrome/calendar',
                                       'calendar/locales/en-US/chrome/prototypes')},
              'global' : {'locale': ('dom/locales/en-US/chrome',
                                     'toolkit/locales/en-US/chrome/global')},
              }
# and this is even worse
LOCAL_DTD_PATHS = ['/usr/share/4Suite/Schemata']

class ChromeTreeBuilder(etree.XMLTreeBuilder):
    '''
    Provide entity resolution; most of our logic is to find files, and much of
    that is currently a hack.
    '''
    def __init__(self, *args, **kwargs):
        self.base_path = kwargs.pop('base_path')
        
        etree.XMLTreeBuilder.__init__(self, *args, **kwargs)
        
        self._parser.EntityDeclHandler = self._entity_decl
        
        # basically, the XBL files use entities as a mechanism for inlining.
        # they immediately reference their entities are defining them, and
        #  if we don't set the following, it will bail on entity defining
        #  once it sees an entity invocation.
        self._parser.SetParamEntityParsing(expat.XML_PARAM_ENTITY_PARSING_ALWAYS)
        self._parser.ExternalEntityRefHandler = self._external_entity
        
        #self._parser.XmlDeclHandler = self._xml_decl
        #self._parser.SkippedEntityHandler = self._skip_ent
        
        self.system_id_map = {}
    
    def _skip_ent(self, name, is_param):
        print 'SKIP', name, is_param
        
    def _xml_decl(self, version, encoding, standalone):
        print 'XML DECL', version, encoding, standalone
    
    def _map_chrome(self, systemId):
        chrome_path = systemId[9:]
        
        cur_map = CHROME_MAP
        rest_path = chrome_path
        while isinstance(cur_map, dict):
            cur_part, rest_path = rest_path.split('/', 1)
            if cur_part in cur_map:
                cur_map = cur_map[cur_part]
            else:
                raise Exception('Unknown chrome path part %s in %s' % 
                                (cur_part, chrome_path))
        
        good_path = None
        for map_part in cur_map:
            filepath = os.path.join(self.base_path, map_part, rest_path)
            if os.path.exists(filepath):
                good_path = filepath
                break
        
        return good_path
    
    def _entity_decl(self, entityName, is_parameter, value,
                     base, systemId, publicId, notationName):
        #print 'ENTITY DECL', entityName, is_parameter, value, base, systemId, publicId, notationName
        
        if is_parameter and systemId and systemId.startswith('chrome://'):
            # we will handle this in our external entity dude
            pass
        elif value:
            self.entity[entityName] = value
            #print '  added', entityName, value
        else:
            #print 'ENTITY DECL', entityName, is_parameter, value, base, systemId, publicId, notationName
            pass
    
    def _map_dtd_path(self, systemId):
        dtd_filename = os.path.basename(systemId)
        
        for local_dtd_path in LOCAL_DTD_PATHS:
            dtd_path = os.path.join(local_dtd_path, dtd_filename)
            if os.path.exists(dtd_path):
                return dtd_path
        
        return None

    def _do_external_parse(self, filepath, context):
        eep = self._parser.ExternalEntityParserCreate(context)
        f_in = open(filepath, 'r') # codecs.open(filepath, 'r', 'utf-8')
        f_out = StringIO.StringIO()
        mozpreproc.preprocess(includes=[f_in], defines=consts.defines,
                              output=f_out,
                              line_endings='lf')
        f_in.close()
        f_out.seek(0)
        
        try:
            eep.ParseFile(f_out)
        finally:
            f_out.close()
    
    def _external_entity(self, context, base, systemId, publicId):
        #print 'EXTERNAL ENTITY', context, base, systemId, publicId, ':.'

        if systemId and systemId.startswith('chrome://'):
            filepath = self._map_chrome(systemId)
            if filepath:
                self._do_external_parse(filepath, context)
            else:
                raise Exception("Don't know how to map %s" % (systemId,))
            return 1
        else:
            dtd_path = self._map_dtd_path(systemId)
            if dtd_path:
                self._do_external_parse(dtd_path, context)
            else:
                print 'Ignoring DTD from:', systemId
            return 1

XBL_NS = 'http://www.mozilla.org/xbl'
XBL_BINDINGS = etree.QName(XBL_NS, 'bindings')
XBL_BINDING = etree.QName(XBL_NS, 'binding')
XBL_CONTENT = etree.QName(XBL_NS, 'content')
XBL_IMPLEMENTATION = etree.QName(XBL_NS, 'implementation')
XBL_CONSTRUCTOR = etree.QName(XBL_NS, 'constructor')
XBL_FIELD = etree.QName(XBL_NS, 'field')
XBL_PROPERTY = etree.QName(XBL_NS, 'property')
XBL_GETTER = etree.QName(XBL_NS, 'getter')
XBL_SETTER = etree.QName(XBL_NS, 'setter')
XBL_METHOD = etree.QName(XBL_NS, 'method')
XBL_PARAMETER = etree.QName(XBL_NS, 'parameter')
XBL_BODY = etree.QName(XBL_NS, 'body')
XBL_HANDLERS = etree.QName(XBL_NS, 'handlers')
XBL_HANDLER = etree.QName(XBL_NS, 'handler')

class XBLParser(object):
    def parseBinding(self, eBinding):
        eImpl = eBinding.find(XBL_IMPLEMENTATION)
        if eImpl:
            eConstructor = eImpl.find(XBL_CONSTRUCTOR)
            if eConstructor:
                pass
            
            for eField in eImpl.findall(XBL_FIELD):
                pass
            
            for eProperty in eImpl.findall(XBL_PROPERTY):
                eGetter = eProperty.find(XBL_GETTER)
                if eGetter:
                    pass
                
                eSetter = eProperty.find(XBL_SETTER)
                if eSetter:
                    pass
            
            for eMethod in eImpl.findall(XBL_METHOD):
                for eParameter in eMethod.findall(XBL_PARAMETER):
                    pass
                
                eBody = eMethod.find(XBL_BODY)
                assert(eBody is not None)
                
            
            for eHandler in eImpl.findall(XBL_HANDLERS + '/' + XBL_HANDLER):
                pass
        
        
    
    def parse(self, eRoot):
        # root should be 'bindings'
        if eRoot.tag != XBL_BINDINGS:
            raise Exception('')
        
        # and is full of 'binding' elements
        for eBinding in eRoot.findall(XBL_BINDING):
            self.parseBinding(eBinding)           

    