from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class IDLPygLexer(RegexLexer):
    '''
    Simple XPIDL lexer for colorization purposes only.  Since we actually have
    a real lexer elsewhere, no need to try and get fancy.
    '''
    name = 'XPIDL'
    aliases = ['idl', 'IDL', 'xpidl']
    filenames = ['*.idl']
    mimetypes = ['text/x-idl']
    
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/)+'
    
    tokens = {
        'whitespace': [
        ],
        'statements': [
        ],
        'root': [
            # preproc
            (r'^\s*#[^\n]*\n', Comment.Preproc),
            # whitespace
            (r'\n', Text),
            (r'\s+', Text),
            (r'//(\n|(.|\n)*?[^\\]\n)', Comment),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment),
            # general body stuff
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'\d+', Number.Integer),
            (r'[~!%^&*+=|?:<>/-;]', Operator),
            (r'[{}()\[\],.]', Punctuation),
            (r'(uuid)(\()([^)]+)(\))', bygroups(Keyword, Punctuation,
                                                Number.Hex, Punctuation)),
            (r'nsI\w+\b', Name.Function),
            (r'(array|astring|const|cstring|domstring|function|iid_is|'
             r'noscript|notxpcom|nsid|object|optional|ptr|ref|readonly|retval|'
             r'scriptable|shared|size_is|utf8string)\b', Keyword),
            (r'(boolean|void|string|octet|char|short|long|unsigned|float|'
             r'double|wchar|wstring)\b', Keyword.Type),
            (r'(native|typedef|interface|const)\b', Keyword.Reserved),
            (r'(in|out|inout)\b', Name.Builtin),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
        ],
    }
