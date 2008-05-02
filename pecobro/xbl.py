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

#from xml import etree
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
import pecobro.core as core 
import jsparse.jsparse as jsparse

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
        self.caboodle = kwargs.pop('caboodle')
        
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
        
        if self._parser.StartElementHandler == etree.XMLTreeBuilder._start:
            self._parser.StartElementHandler = self._start
        else:
            self._parser.StartElementHandler = self._start_list
        
        self.system_id_map = {}
    
    def _skip_ent(self, name, is_param):
        print 'SKIP', name, is_param
        
    def _xml_decl(self, version, encoding, standalone):
        print 'XML DECL', version, encoding, standalone
    
    def _map_chrome(self, systemId):
        chrome_path = systemId[9:]
        
        defines_and_path = self.caboodle.chrome_map.get(chrome_path)
        if defines_and_path is None:
            raise Exception('Unknown chrome path: %s' % (chrome_path,))
        # path[0] is the defines for preprocessing
        return defines_and_path
        
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

    def _do_external_parse(self, filepath, context, defines=consts.defines):
        eep = self._parser.ExternalEntityParserCreate(context)
        f_in = open(filepath, 'r') # codecs.open(filepath, 'r', 'utf-8')
        f_out = StringIO.StringIO()
        mozpreproc.preprocess(includes=[f_in], defines=defines,
                              output=f_out,
                              line_endings='lf',
                              # we do not want the "//@line" updates...
                              line_updates=False,
                              )
        f_in.close()
        f_out.seek(0)
        
        try:
            eep.ParseFile(f_out)
        finally:
            f_out.close()
    
    def _external_entity(self, context, base, systemId, publicId):
        #print 'EXTERNAL ENTITY', context, base, systemId, publicId, ':.'

        if systemId and systemId.startswith('chrome://'):
            defines, filepath = self._map_chrome(systemId)
            if filepath:
                self._do_external_parse(filepath, context, defines)
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
    
    def _start(self, tag, attrib_in):
        rval = etree.XMLTreeBuilder._start(self, tag, attrib_in)
        rval.column = self._parser.CurrentColumnNumber
        rval.line = self._parser.CurrentLineNumber
        return rval

    def _start_list(self, tag, attrib_in):
        rval = etree.XMLTreeBuilder._start_list(self, tag, attrib_in)
        rval.column = self._parser.CurrentColumnNumber
        rval.line = self._parser.CurrentLineNumber
        return rval


XBL_NS = 'http://www.mozilla.org/xbl'
XBL_BINDINGS = etree.QName(XBL_NS, 'bindings')
XBL_BINDING = etree.QName(XBL_NS, 'binding')
XBL_CONTENT = etree.QName(XBL_NS, 'content')
XBL_IMPLEMENTATION = etree.QName(XBL_NS, 'implementation')
XBL_CONSTRUCTOR = etree.QName(XBL_NS, 'constructor')
XBL_DESTRUCTOR = etree.QName(XBL_NS, 'destructor')
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
    def _make_func(self, source_file, func_name, eNode, code):
        func, created = source_file.get_or_create_function(func_name,
                                                           eNode.line)
        
        func.source_line = eNode.line
        func.source_col = eNode.column

        # let's add a synthetic newline to trigger the implicit ';'-effect if
        #  we don't think we've got a fully legal statement otherwise...
        # (we're adding a newline instead of a semicolon because the LT isn't
        #  really a semantic token)parse_and_proc_snippet
        # note: it is possible for code to be None (deprecated function idiom)
        if code:
            if not ';' in code or not '\n' in code:
                code += '\n'
            # although the AST's line numbering is one-based (and columns
            #  zero-based), so is the XML line numbering, so we need to
            #  subtract one off for the adjustment. 
            func.ast = jsparse.sf_process_snippet(source_file, code, 'func',
                                                  adj_line=eNode.line-1,
                                                  adj_column=eNode.column)
            func.nested_ast = False
        
        source_file.add_to_contents(func)
    
    def _make_field(self, source_file, field_name, eNode, code):
        '''
        Fields are somewhat annoying in that while they are not functions, their
        evaluation is effectively a function call (per the system), and may
        in fact result in function calls occurring.  As such, we are rolling
        back the concept of separate field things for now and only creating a
        function...
        '''
        #field, created = source_file.get_or_create_field(field_name)
        func_name = 'field_' + field_name
        field, created = source_file.get_or_create_function(func_name,
                                                            eNode.line)
        
        field.source_line = eNode.line
        field.source_col  = eNode.column
        
        if code:
            # although the AST's line numbering is one-based (and columns
            #  zero-based), so is the XML line numbering, so we need to
            #  subtract one off for the adjustment. 
            field.ast = jsparse.sf_process_snippet(source_file, code, 'field',
                                                   adj_line=eNode.line-1,
                                                   adj_column=eNode.column)
            field.nested_ast = False
        
        source_file.add_to_contents(field)
    
    def parseBinding(self, source_file, eBinding):
        eImpl = eBinding.find(XBL_IMPLEMENTATION.text)
        if eImpl:
            # implementation can specify a name that apparently can be used in
            #  lieu of the filename...
            impl_name = eImpl.get('name')
            source_file.impl_names.append(impl_name)
            if source_file.caboodle:
                source_file.caboodle.impl_name_to_file[impl_name] = source_file
            
            eConstructor = eImpl.find(XBL_CONSTRUCTOR.text)
            if eConstructor is not None:
                self._make_func(source_file, 'constructor',
                                eConstructor, eConstructor.text)

            eDestructor = eImpl.find(XBL_DESTRUCTOR.text)
            if eDestructor is not None:
                self._make_func(source_file, 'destructor',
                                eDestructor, eDestructor.text)
            
            for eField in eImpl.findall(XBL_FIELD.text):
                field_name = eField.get('name')
                self._make_field(source_file, field_name,
                                 eField, eField.text)
            
            for eProperty in eImpl.findall(XBL_PROPERTY.text):
                prop_name = eProperty.get('name')
                
                eGetter = eProperty.find(XBL_GETTER.text)
                on_get = eProperty.get('onget')
                if eGetter is not None or on_get:
                    func_name = 'get_' + prop_name
                    if eGetter is not None:
                        self._make_func(source_file, func_name,
                                        eGetter, eGetter.text)
                    else:
                        self._make_func(source_file, func_name,
                                        eProperty, on_get)
                
                eSetter = eProperty.find(XBL_SETTER.text)
                on_set = eProperty.get('onset')
                if eSetter is not None or on_set:
                    func_name = 'set_' + prop_name
                    if eSetter is not None:
                        self._make_func(source_file, func_name,
                                        eSetter, eSetter.text)
                    else:
                        self._make_func(source_file, func_name,
                                        eProperty, on_set)
            
            for eMethod in eImpl.findall(XBL_METHOD.text):
                func_name = eMethod.get('name')
                for eParameter in eMethod.findall(XBL_PARAMETER.text):
                    pass
                
                eBody = eMethod.find(XBL_BODY.text)
                if eBody is not None:
                    self._make_func(source_file, func_name, eBody, eBody.text)
            
        eHandlers = eBinding.find(XBL_HANDLERS.text)
        if eHandlers is not None:
            for eHandler in eHandlers.findall(XBL_HANDLER.text):
                func_name = 'on' + eHandler.get('event')
                if eHandler.text:
                    self._make_func(source_file, func_name, eHandler,
                                    eHandler.text)
                elif eHandler.get('action'):
                    self._make_func(source_file, func_name, eHandler,
                                    eHandler.get('action'))
        
        source_file.contents.sort(key=lambda x:(x.source_line, x.source_col))
        
    
    def parse(self, source_file):
        eRoot = source_file.eRoot
        # root should be 'bindings'
        if eRoot.tag != XBL_BINDINGS:
            raise Exception('')
        
        # and is full of 'binding' elements
        for eBinding in eRoot.findall(XBL_BINDING.text):
            self.parseBinding(source_file, eBinding)           
