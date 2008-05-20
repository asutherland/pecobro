/*
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
*/

grammar XPIDL;

options
{
	output=AST;
	language=Python;
}

tokens
{
// semantic tokens
	ATTR;
	BODY;
	CONST;
	FORWARD;
	INCLUDE;
	INLINE;
	INTERFACE;
	I_UUID;
	METHOD;
	MODIFIERS;
	NATIVE;
	PARAM;
	PARAMS;
	PARENTS;
	TYPEDEF;
// type normalization tokens
	VOID;
	BOOLEAN;
	OCTET;
	SHORT;
	LONG;
	LONG_LONG;
	UNSIGNED_SHORT;
	UNSIGNED_LONG;
	UNSIGNED_LONG_LONG;
	FLOAT;
	DOUBLE;
	CHAR;
	WCHAR;
	STRING;
	WSTRING;
}

idlFile
	: toplevel* EOF!
	;

toplevel
	: interface
	| typedef
	| nativeTypeDecl
	| include
	| inline
	;

include
	: Include -> ^(INCLUDE Include)
	;

inline
	: InlineCHeader -> ^(INLINE InlineCHeader)
	;

interface
options {backtrack=true;}
	: 'interface' validId ';'
		-> ^(FORWARD validId)
	| ('[' (interfaceModifier ',')* UUID ']')? 'interface' validId (':' validIdList)?
	  '{' interfaceBody '}' ';'
		-> ^(INTERFACE validId ^(I_UUID UUID?) ^(PARENTS validIdList?)
		         ^(MODIFIERS interfaceModifier*)
		         ^(BODY interfaceBody))
	;

interfaceModifierList
	: interfaceModifier (',' interfaceModifier)*
		-> interfaceModifier*
	;

interfaceModifier
	: 'scriptable'
	| 'function'
	| 'object'
	| 'notxpcom'
	| 'noscript'
	;

interfaceBody
	: interfaceBodyItem*
	;

interfaceBodyItem
	: attribute
	| const
	| method
	;

method
	: methodModifiers? type validId '(' paramList ')' ';'
		-> ^(METHOD type validId ^(MODIFIERS methodModifiers?) ^(PARAMS paramList))
	;

const
	: 'const' constType validId '=' mathExpr ';'
		-> ^(CONST constType validId mathExpr)
	;

constType
	: 'short' -> SHORT
	| 'long' -> LONG
	| validId
	;

attribute
	: attributeModifiers? 'attribute' type validId ';'
		-> ^(ATTR type validId ^(MODIFIERS methodModifiers))
	;

attributeModifiers
	: '[' attributeModifier (',' attributeModifier)+ ']'
		-> attributeModifier*
	;

attributeModifier
	: 'readonly'
	| methodModifier
	;

methodModifiers
	: '[' methodModifier (',' methodModifier)+ ']'
		-> methodModifier*
	;

methodModifier
	: 'noscript'
	| 'notxpcom'
	;

paramList
	: paramDecl (',' paramDecl)+
		-> paramDecl*
	;

paramDecl
	: paramModifiersDecl? paramType type validId
		-> ^(PARAM paramType type validId ^(MODIFIERS paramModifiersDecl?))
	;

paramType
	: 'in'
	| 'out'
	| 'inout'
	;

paramModifiersDecl
	: '[' paramModifier (',' paramModifier)* ']'
		-> paramModifier*
	;

paramModifier
	: 'array'
	| sizeIs
	| iidIs
	| 'retval'
	| 'const'
	| 'shared'
	;
	
sizeIs
	: 'size_is' '(' validId ')'
	; 

iidIs
	: IID_IS
	;

nativeTypeDecl
	: nativeType ';'!
	;

nativeType
	: typeModifiersDecl 'native' validId
		-> ^(NATIVE validId typeModifiersDecl)
	;

typeModifiersDecl
	: '[' typeModifier (',' typeModifier)* ']'
		-> typeModifier+
	;

typeModifier
	: 'ref'
	| 'ptr'
	| 'nsid'
	| 'domstring'
	| 'utf8string'
	| 'cstring'
	| 'astring'
	;

typedef
	: 'typedef' type validId ';'
		-> ^(TYPEDEF type validId)
	;

type
	: 'boolean' -> BOOLEAN
	| 'void' -> VOID
	| 'string' -> STRING
	| 'octet' -> OCTET
	| 'short' -> SHORT
	| 'long' -> LONG
	| 'long' 'long' -> LONG_LONG
	| 'unsigned' 'short' -> UNSIGNED_SHORT
	| 'unsigned' 'long' -> UNSIGNED_LONG
	| 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG
	| 'float' -> FLOAT
	| 'double' -> DOUBLE
	| 'char' -> CHAR
	| 'wchar' -> WCHAR
	| 'wstring' -> WSTRING
	| validId
	;

mathExpr
	: mathMultDiv
	;

mathMultDiv
	: mathAddSub (('*'|'/') mathAddSub)?
	;

mathAddSub
	: mathShift (('+'|'-') mathShift)?
	;

mathShift
	: mathVar ('<<' mathVar)?
	;

mathVar
	: Integer
	| validId
	;

validIdList
	: validId (',' validId)*
	;

validId
	: Identifier
	;

uuid
	: UUID
	;

// We only need integers...
Integer
	: DecimalInteger
	| HexInteger
	;

fragment HexInteger
	: '0' ('x' | 'X') HexChar+
	;

fragment DecimalInteger
	: DecimalChar+
	;

fragment DecimalChar
	: ('0'..'9')
	;

Identifier
	: IdentifierStart IdentifierPart*
	;
	
fragment IdentifierStart
	: ('a'..'z')|('A'..'Z')
	;

fragment IdentifierPart
	: IdentifierStart
	| '_'
	| ('0'..'9')
	;

UUID
	: 'uuid' WhiteSpace* '(' UUIDPayload ')'
	;

IID_IS
	: 'iid_is' WhiteSpace* '(' UUIDPayload ')'
	;

// really 8-4-4-4-12
fragment UUIDPayload
	: HexChar+ '-' HexChar+ '-' HexChar+ '-' HexChar+ '-' HexChar+
	;

fragment HexChar
	: ('0'..'9')
	| ('a'..'f')|('A'..'F')
	;	

InlineCHeader
	: '%{C++' (options {greedy=false;} : .)* '%}' 'C++'?
	;

// since Includes have a specific lexer definition and are basically
//  preprocessor gunk, handle it at the lexer level.
// note: we are allowing a little extra whitespace...
Include
	: '#include' WhiteSpace* '"' ~('\n' | '"')* '"' WhiteSpace* '\n'
	;


BlockComment
	: '/*' (options {greedy=false;} : .)* '*/' {$channel=HIDDEN;}
	;

LineComment
	: '//' ~('\n')* '\n' {$channel=HIDDEN;}
	;

// newlines, tabs (horiz and vert), form feed, and honest to goodness spaces.
WhiteSpace
	: ('\n' | '\r' | '\t' | '\v' | '\f' | ' ') {$channel=HIDDEN;}
	;
