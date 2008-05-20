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
import pecobro.xpidl.XPIDLLexer as idllex 

import pecobro.core as core

def as_type(node, typedefs):
    if node.token and node.token.text:
        name = node.token.text
        if name in typedefs:
            name = typedefs[name]
        return name
    else:
        return str(node)

class IDLGrok(object):
    
    def _grok_attribute(self, interface, ast, typedefs={}):
        # children: type, name, MODIFIERS
        c_type, c_name, c_modifiers = ast.children
        
        modifiers = [c.token.text for c in c_modifiers.children]
        
        attrib = core.XPAttribute(interface, c_name.token.text,
                                  as_type(c_type, typedefs),
                                  readonly='readonly' in modifiers)
    
    def _grok_const(self, interface, ast, typedefs={}):
        # children: type, name, expr+
        c_type, c_name = ast.children[:2]
        c_exprs = [n.token.text for n in ast.children[2:]]
        
        if len(c_exprs) == 1 and c_exprs[0][0].isdigit():
            if c_exprs[0].startswith('0x') or c_exprs[0].startswith('0X'):
                val = int(c_exprs[0], 16)
            else:
                val = int(c_exprs[0])
        else:
            # TODO: process fancy expressions
            print 'Ignoring fancy const expression %s for %s:' % (c_exprs,
                                                                  c_name)
            val = 0
        
        # the type is some form of integer, but we don't really care. 
        #  so, ignore it.
        interface.def_const(c_name, val)
    
    def _grok_method(self, interface, ast, typedefs={}):
        # children: type, name, MODIFIERS, PARAMS, RAISES
        c_type, c_name, c_modifiers, c_params, c_raises = ast.children
        
        modifiers = [c.token.text for c in c_modifiers.children]
        
        args = []
        
        for c_param in c_params.children:
            # direction (in/out/inout), type, name, MODIFIERS
            p_dir, p_type, p_name, p_modifiers = c_param.children
            arg = core.XPMethodArg(p_dir.token.text, as_type(p_type, typedefs),
                                   p_name.token.text)
            args.append(arg)
        
        method = core.XPMethod(interface, c_name.token.text,
                               as_type(c_type, typedefs),
                               args=args,
                               scriptable=not 'noscript' in modifiers,
                               source_line = c_name.token.line,
                               source_col = c_name.token.charPositionInLine,
                               )
        interface.add_method(method)
    
    def grok_interface(self, source_file, ast, typedefs={}):
        # children: name, I_UUID, PARENTS, MODIFIERS, BODY
        c_name, c_uuid, c_parents, c_modifiers, c_body = ast.children
        
        interface_name = c_name.token.text
        
        modifiers = [c.token.text for c in c_modifiers.children]
        
        interface = core.XPInterface(source_file, interface_name,
                                     scriptable='scriptable' in modifiers,
                                     )
        
        for child in c_body.children:
            ctype = child.getType()
            
            if ctype == idllex.ATTR:
                self._grok_attribute(interface, child, typedefs)
            elif ctype == idllex.CONST:
                self._grok_const(interface, child, typedefs)
            elif ctype == idllex.METHOD:
                self._grok_method(interface, child, typedefs)
         
        source_file.add_xpcom_interface(interface)

    def grok_top_level(self, source_file, ast):
        typedefs = {}
        
        for child in ast.children:
            ctype = child.getType()
            
            # we ignore include's...
            if ctype == idllex.INCLUDE:
                pass
            # we ignore C++ inline's
            elif ctype == idllex.INLINE:
                pass
            # meh, forwarded types are for suckers
            elif ctype == idllex.FORWARD:
                pass
            elif ctype == idllex.TYPEDEF:
                ttype, tname = child.children 
                typedefs[tname] = ttype
            # native types are also for suckers
            elif ctype == idllex.NATIVE:
                pass
            elif ctype == idllex.INTERFACE:
                self.grok_interface(source_file, child, typedefs)

grokker = IDLGrok()

if __name__ == '__main__':
    try:
        from IPython.Shell import IPShellEmbed
        ipshell = IPShellEmbed(['-pdb'])
    except:
        ipshell = None
    
    import pecobro.xpidl.idlparse as idlparse
    import sys
    fname = sys.argv[1]
    z, used_codec = idlparse.parse_file(fname)
    grokker = IDLGrok()
    sf = core.SourceFile(fname, 'idl')
    a = grokker.grok_top_level(sf, z.tree)
    if ipshell:
        print 'z: AST'
        print 'sf: source file'
        ipshell()
