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
	| Include
	| InlineCHeader
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
	: methodModifiers? 'attribute' type validId ';'
		-> ^(ATTR type validId ^(MODIFIERS methodModifiers))
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
	| 'retval'
	| 'const'
	| 'shared'
	;
	
sizeIs
	: 'size_is' '(' validId ')'
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
