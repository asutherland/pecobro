# $ANTLR 3.0.1 /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g 2008-05-20 01:46:19

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
JerkyPreprocessorLine=40
FORWARD=8
UUIDPayload=51
LONG_LONG=28
UUID=42
InlineCHeader=41
CONST=7
CHAR=34
LineComment=55
PARAM=17
FLOAT=32
EOF=-1
WCHAR=36
Identifier=44
BlockComment=54
MODIFIERS=15
SIZE_IS=21
BOOLEAN=24
HexChar=47
UNSIGNED_LONG=30
INCLUDE=10
UNSIGNED_SHORT=29
HexInteger=46
DOUBLE=33
WhiteSpace=52
BODY=6
VOID=23
WSTRING=38
UNSIGNED_LONG_LONG=31
BINARY_NAME=5
IdentifierPart=50
ATTR=4
RAISES=20
PARAMS=18
I_UUID=13
DecimalChar=48
JerkyPreprocessorDirectives=53
TYPEDEF=22
DecimalInteger=45
IdentifierStart=49
NATIVE=16
IID_IS=9
SHORT=26
Include=39
PARENTS=19
INTERFACE=12
INLINE=11
UNSIGNED_CHAR=35
LONG=27
METHOD=14
Integer=43
OCTET=25
STRING=37

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ATTR", "BINARY_NAME", "BODY", "CONST", "FORWARD", "IID_IS", "INCLUDE", 
    "INLINE", "INTERFACE", "I_UUID", "METHOD", "MODIFIERS", "NATIVE", "PARAM", 
    "PARAMS", "PARENTS", "RAISES", "SIZE_IS", "TYPEDEF", "VOID", "BOOLEAN", 
    "OCTET", "SHORT", "LONG", "LONG_LONG", "UNSIGNED_SHORT", "UNSIGNED_LONG", 
    "UNSIGNED_LONG_LONG", "FLOAT", "DOUBLE", "CHAR", "UNSIGNED_CHAR", "WCHAR", 
    "STRING", "WSTRING", "Include", "JerkyPreprocessorLine", "InlineCHeader", 
    "UUID", "Integer", "Identifier", "DecimalInteger", "HexInteger", "HexChar", 
    "DecimalChar", "IdentifierStart", "IdentifierPart", "UUIDPayload", "WhiteSpace", 
    "JerkyPreprocessorDirectives", "BlockComment", "LineComment", "'interface'", 
    "';'", "'['", "','", "']'", "':'", "'{'", "'}'", "'scriptable'", "'function'", 
    "'object'", "'notxpcom'", "'noscript'", "'('", "')'", "'raises'", "'const'", 
    "'='", "'readonly'", "'attribute'", "'binaryname'", "'in'", "'out'", 
    "'inout'", "'array'", "'retval'", "'shared'", "'optional'", "'size_is'", 
    "'iid_is'", "'native'", "'boolean'", "'void'", "'string'", "'octet'", 
    "'char'", "'short'", "'long'", "'unsigned'", "'float'", "'double'", 
    "'wchar'", "'wstring'", "'*'", "'&'", "'<'", "'>'", "'ref'", "'ptr'", 
    "'nsid'", "'domstring'", "'utf8string'", "'cstring'", "'astring'", "'typedef'", 
    "'|'", "'^'", "'<<'", "'+'", "'-'", "'/'"
]



class XPIDLParser(Parser):
    grammarFileName = "/home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)
        self.ruleMemo = {}
        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class idlFile_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start idlFile
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:89:1: idlFile : ( toplevel )* EOF ;
    def idlFile(self, ):

        retval = self.idlFile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        toplevel1 = None


        EOF2_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:2: ( ( toplevel )* EOF )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: ( toplevel )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: ( toplevel )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((Include <= LA1_0 <= InlineCHeader) or LA1_0 == 56 or LA1_0 == 58 or LA1_0 == 86 or LA1_0 == 110) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: toplevel
                        self.following.append(self.FOLLOW_toplevel_in_idlFile178)
                        toplevel1 = self.toplevel()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, toplevel1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_idlFile181)
                if self.failed:
                    return retval



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end idlFile

    class toplevel_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start toplevel
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:93:1: toplevel : ( interface | typedef | nativeTypeDecl | include | jerkyPreprocessorDirectives | inline );
    def toplevel(self, ):

        retval = self.toplevel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        interface3 = None

        typedef4 = None

        nativeTypeDecl5 = None

        include6 = None

        jerkyPreprocessorDirectives7 = None

        inline8 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:94:2: ( interface | typedef | nativeTypeDecl | include | jerkyPreprocessorDirectives | inline )
                alt2 = 6
                LA2 = self.input.LA(1)
                if LA2 == 56:
                    alt2 = 1
                elif LA2 == 58:
                    LA2_2 = self.input.LA(2)

                    if ((103 <= LA2_2 <= 109)) :
                        alt2 = 3
                    elif (LA2_2 == UUID or (64 <= LA2_2 <= 68)) :
                        alt2 = 1
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("93:1: toplevel : ( interface | typedef | nativeTypeDecl | include | jerkyPreprocessorDirectives | inline );", 2, 2, self.input)

                        raise nvae

                elif LA2 == 110:
                    alt2 = 2
                elif LA2 == 86:
                    alt2 = 3
                elif LA2 == Include:
                    alt2 = 4
                elif LA2 == JerkyPreprocessorLine:
                    alt2 = 5
                elif LA2 == InlineCHeader:
                    alt2 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("93:1: toplevel : ( interface | typedef | nativeTypeDecl | include | jerkyPreprocessorDirectives | inline );", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:94:4: interface
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_interface_in_toplevel193)
                    interface3 = self.interface()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, interface3.tree)


                elif alt2 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:95:4: typedef
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_typedef_in_toplevel198)
                    typedef4 = self.typedef()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, typedef4.tree)


                elif alt2 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:96:4: nativeTypeDecl
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_nativeTypeDecl_in_toplevel203)
                    nativeTypeDecl5 = self.nativeTypeDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, nativeTypeDecl5.tree)


                elif alt2 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:97:4: include
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_include_in_toplevel208)
                    include6 = self.include()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, include6.tree)


                elif alt2 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:98:4: jerkyPreprocessorDirectives
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_jerkyPreprocessorDirectives_in_toplevel213)
                    jerkyPreprocessorDirectives7 = self.jerkyPreprocessorDirectives()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, jerkyPreprocessorDirectives7.tree)


                elif alt2 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:99:4: inline
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_inline_in_toplevel218)
                    inline8 = self.inline()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, inline8.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end toplevel

    class include_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start include
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:102:1: include : Include -> ^( INCLUDE Include ) ;
    def include(self, ):

        retval = self.include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Include9 = None

        Include9_tree = None
        stream_Include = RewriteRuleTokenStream(self.adaptor, "token Include")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:103:2: ( Include -> ^( INCLUDE Include ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:103:4: Include
                Include9 = self.input.LT(1)
                self.match(self.input, Include, self.FOLLOW_Include_in_include229)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_Include.add(Include9)
                # AST Rewrite
                # elements: Include
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 103:12: -> ^( INCLUDE Include )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:103:15: ^( INCLUDE Include )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INCLUDE, "INCLUDE"), root_1)

                    self.adaptor.addChild(root_1, stream_Include.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end include

    class jerkyPreprocessorDirectives_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start jerkyPreprocessorDirectives
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:1: jerkyPreprocessorDirectives : JerkyPreprocessorLine ;
    def jerkyPreprocessorDirectives(self, ):

        retval = self.jerkyPreprocessorDirectives_return()
        retval.start = self.input.LT(1)

        root_0 = None

        JerkyPreprocessorLine10 = None

        JerkyPreprocessorLine10_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:107:2: ( JerkyPreprocessorLine )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:107:4: JerkyPreprocessorLine
                root_0 = self.adaptor.nil()

                JerkyPreprocessorLine10 = self.input.LT(1)
                self.match(self.input, JerkyPreprocessorLine, self.FOLLOW_JerkyPreprocessorLine_in_jerkyPreprocessorDirectives248)
                if self.failed:
                    return retval

                JerkyPreprocessorLine10_tree = self.adaptor.createWithPayload(JerkyPreprocessorLine10)
                self.adaptor.addChild(root_0, JerkyPreprocessorLine10_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end jerkyPreprocessorDirectives

    class inline_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start inline
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:1: inline : InlineCHeader -> ^( INLINE InlineCHeader ) ;
    def inline(self, ):

        retval = self.inline_return()
        retval.start = self.input.LT(1)

        root_0 = None

        InlineCHeader11 = None

        InlineCHeader11_tree = None
        stream_InlineCHeader = RewriteRuleTokenStream(self.adaptor, "token InlineCHeader")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:2: ( InlineCHeader -> ^( INLINE InlineCHeader ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:4: InlineCHeader
                InlineCHeader11 = self.input.LT(1)
                self.match(self.input, InlineCHeader, self.FOLLOW_InlineCHeader_in_inline259)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_InlineCHeader.add(InlineCHeader11)
                # AST Rewrite
                # elements: InlineCHeader
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 111:18: -> ^( INLINE InlineCHeader )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:21: ^( INLINE InlineCHeader )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INLINE, "INLINE"), root_1)

                    self.adaptor.addChild(root_1, stream_InlineCHeader.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end inline

    class interface_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interface
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:114:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );
    def interface(self, ):

        retval = self.interface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal12 = None
        char_literal14 = None
        char_literal15 = None
        char_literal17 = None
        UUID18 = None
        char_literal19 = None
        string_literal20 = None
        char_literal22 = None
        char_literal24 = None
        char_literal26 = None
        char_literal27 = None
        validId13 = None

        interfaceModifier16 = None

        validId21 = None

        validIdList23 = None

        interfaceBody25 = None


        string_literal12_tree = None
        char_literal14_tree = None
        char_literal15_tree = None
        char_literal17_tree = None
        UUID18_tree = None
        char_literal19_tree = None
        string_literal20_tree = None
        char_literal22_tree = None
        char_literal24_tree = None
        char_literal26_tree = None
        char_literal27_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self.adaptor, "token 56")
        stream_UUID = RewriteRuleTokenStream(self.adaptor, "token UUID")
        stream_62 = RewriteRuleTokenStream(self.adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self.adaptor, "token 61")
        stream_interfaceBody = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceBody")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_interfaceModifier = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceModifier")
        stream_validIdList = RewriteRuleSubtreeStream(self.adaptor, "rule validIdList")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:2: ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 56) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == Identifier or LA6_1 == 56 or (64 <= LA6_1 <= 68) or LA6_1 == 72 or (80 <= LA6_1 <= 83) or LA6_1 == 85 or (103 <= LA6_1 <= 109)) :
                        LA6_3 = self.input.LA(3)

                        if ((61 <= LA6_3 <= 62)) :
                            alt6 = 2
                        elif (LA6_3 == 57) :
                            alt6 = 1
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("114:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 3, self.input)

                            raise nvae

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("114:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 1, self.input)

                        raise nvae

                elif (LA6_0 == 58) :
                    alt6 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("114:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:4: 'interface' validId ';'
                    string_literal12 = self.input.LT(1)
                    self.match(self.input, 56, self.FOLLOW_56_in_interface285)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_56.add(string_literal12)
                    self.following.append(self.FOLLOW_validId_in_interface287)
                    validId13 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId13.tree)
                    char_literal14 = self.input.LT(1)
                    self.match(self.input, 57, self.FOLLOW_57_in_interface289)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_57.add(char_literal14)
                    # AST Rewrite
                    # elements: validId
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 117:3: -> ^( FORWARD validId )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:117:6: ^( FORWARD validId )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FORWARD, "FORWARD"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt6 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:4: ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';'
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:4: ( '[' ( interfaceModifier ',' )* UUID ']' )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 58) :
                        alt4 = 1
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:5: '[' ( interfaceModifier ',' )* UUID ']'
                        char_literal15 = self.input.LT(1)
                        self.match(self.input, 58, self.FOLLOW_58_in_interface305)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_58.add(char_literal15)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:9: ( interfaceModifier ',' )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if ((64 <= LA3_0 <= 68)) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:10: interfaceModifier ','
                                self.following.append(self.FOLLOW_interfaceModifier_in_interface308)
                                interfaceModifier16 = self.interfaceModifier()
                                self.following.pop()
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_interfaceModifier.add(interfaceModifier16.tree)
                                char_literal17 = self.input.LT(1)
                                self.match(self.input, 59, self.FOLLOW_59_in_interface310)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_59.add(char_literal17)


                            else:
                                break #loop3


                        UUID18 = self.input.LT(1)
                        self.match(self.input, UUID, self.FOLLOW_UUID_in_interface314)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_UUID.add(UUID18)
                        char_literal19 = self.input.LT(1)
                        self.match(self.input, 60, self.FOLLOW_60_in_interface316)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_60.add(char_literal19)



                    string_literal20 = self.input.LT(1)
                    self.match(self.input, 56, self.FOLLOW_56_in_interface320)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_56.add(string_literal20)
                    self.following.append(self.FOLLOW_validId_in_interface322)
                    validId21 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId21.tree)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:65: ( ':' validIdList )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 61) :
                        alt5 = 1
                    if alt5 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:118:66: ':' validIdList
                        char_literal22 = self.input.LT(1)
                        self.match(self.input, 61, self.FOLLOW_61_in_interface325)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_61.add(char_literal22)
                        self.following.append(self.FOLLOW_validIdList_in_interface327)
                        validIdList23 = self.validIdList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_validIdList.add(validIdList23.tree)



                    char_literal24 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_interface334)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_62.add(char_literal24)
                    self.following.append(self.FOLLOW_interfaceBody_in_interface336)
                    interfaceBody25 = self.interfaceBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_interfaceBody.add(interfaceBody25.tree)
                    char_literal26 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_interface338)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_63.add(char_literal26)
                    char_literal27 = self.input.LT(1)
                    self.match(self.input, 57, self.FOLLOW_57_in_interface340)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_57.add(char_literal27)
                    # AST Rewrite
                    # elements: interfaceBody, UUID, validIdList, interfaceModifier, validId
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 120:3: -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:6: ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INTERFACE, "INTERFACE"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:26: ^( I_UUID ( UUID )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(I_UUID, "I_UUID"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:35: ( UUID )?
                        if stream_UUID.hasNext():
                            self.adaptor.addChild(root_2, stream_UUID.next())


                        stream_UUID.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:42: ^( PARENTS ( validIdList )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARENTS, "PARENTS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:52: ( validIdList )?
                        if stream_validIdList.hasNext():
                            self.adaptor.addChild(root_2, stream_validIdList.next())


                        stream_validIdList.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:12: ^( MODIFIERS ( interfaceModifier )* )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:24: ( interfaceModifier )*
                        while stream_interfaceModifier.hasNext():
                            self.adaptor.addChild(root_2, stream_interfaceModifier.next())


                        stream_interfaceModifier.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:122:12: ^( BODY interfaceBody )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(BODY, "BODY"), root_2)

                        self.adaptor.addChild(root_2, stream_interfaceBody.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end interface

    class interfaceModifierList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interfaceModifierList
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:125:1: interfaceModifierList : interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* ;
    def interfaceModifierList(self, ):

        retval = self.interfaceModifierList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal29 = None
        interfaceModifier28 = None

        interfaceModifier30 = None


        char_literal29_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_interfaceModifier = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:2: ( interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:4: interfaceModifier ( ',' interfaceModifier )*
                self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList410)
                interfaceModifier28 = self.interfaceModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_interfaceModifier.add(interfaceModifier28.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:22: ( ',' interfaceModifier )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 59) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:23: ',' interfaceModifier
                        char_literal29 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_interfaceModifierList413)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_59.add(char_literal29)
                        self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList415)
                        interfaceModifier30 = self.interfaceModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_interfaceModifier.add(interfaceModifier30.tree)


                    else:
                        break #loop7


                # AST Rewrite
                # elements: interfaceModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 127:3: -> ( interfaceModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:127:6: ( interfaceModifier )*
                    while stream_interfaceModifier.hasNext():
                        self.adaptor.addChild(root_0, stream_interfaceModifier.next())


                    stream_interfaceModifier.reset();






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end interfaceModifierList

    class interfaceModifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interfaceModifier
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:130:1: interfaceModifier : ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' );
    def interfaceModifier(self, ):

        retval = self.interfaceModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set31 = None

        set31_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:131:2: ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set31 = self.input.LT(1)
                if (64 <= self.input.LA(1) <= 68):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set31))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_interfaceModifier0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end interfaceModifier

    class interfaceBody_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interfaceBody
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:138:1: interfaceBody : ( interfaceBodyItem )* ;
    def interfaceBody(self, ):

        retval = self.interfaceBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        interfaceBodyItem32 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:2: ( ( interfaceBodyItem )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: ( interfaceBodyItem )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: ( interfaceBodyItem )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == Identifier or LA8_0 == 56 or LA8_0 == 58 or (64 <= LA8_0 <= 68) or LA8_0 == 72 or (74 <= LA8_0 <= 75) or (80 <= LA8_0 <= 83) or LA8_0 == 85 or (87 <= LA8_0 <= 98) or (103 <= LA8_0 <= 109)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: interfaceBodyItem
                        self.following.append(self.FOLLOW_interfaceBodyItem_in_interfaceBody466)
                        interfaceBodyItem32 = self.interfaceBodyItem()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, interfaceBodyItem32.tree)


                    else:
                        break #loop8





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end interfaceBody

    class interfaceBodyItem_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interfaceBodyItem
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:142:1: interfaceBodyItem : ( attribute | const | method );
    def interfaceBodyItem(self, ):

        retval = self.interfaceBodyItem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        attribute33 = None

        const34 = None

        method35 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:143:2: ( attribute | const | method )
                alt9 = 3
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:143:4: attribute
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_attribute_in_interfaceBodyItem478)
                    attribute33 = self.attribute()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, attribute33.tree)


                elif alt9 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:144:4: const
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_const_in_interfaceBodyItem483)
                    const34 = self.const()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, const34.tree)


                elif alt9 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:145:4: method
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_method_in_interfaceBodyItem488)
                    method35 = self.method()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, method35.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end interfaceBodyItem

    class method_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start method
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:148:1: method : ( methodModifiers )? type name= validId '(' ( paramList )? ')' ( 'raises' '(' raises= validId ( ',' raises= validId )* ')' )? ';' -> ^( METHOD type $name ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS ( paramList )? ) ^( RAISES ( $raises)* ) ) ;
    def method(self, ):

        retval = self.method_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal38 = None
        char_literal40 = None
        string_literal41 = None
        char_literal42 = None
        char_literal43 = None
        char_literal44 = None
        char_literal45 = None
        name = None

        raises = None

        methodModifiers36 = None

        type37 = None

        paramList39 = None


        char_literal38_tree = None
        char_literal40_tree = None
        string_literal41_tree = None
        char_literal42_tree = None
        char_literal43_tree = None
        char_literal44_tree = None
        char_literal45_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self.adaptor, "token 71")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_paramList = RewriteRuleSubtreeStream(self.adaptor, "rule paramList")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:2: ( ( methodModifiers )? type name= validId '(' ( paramList )? ')' ( 'raises' '(' raises= validId ( ',' raises= validId )* ')' )? ';' -> ^( METHOD type $name ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS ( paramList )? ) ^( RAISES ( $raises)* ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:4: ( methodModifiers )? type name= validId '(' ( paramList )? ')' ( 'raises' '(' raises= validId ( ',' raises= validId )* ')' )? ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:4: ( methodModifiers )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 58) :
                    alt10 = 1
                if alt10 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_method499)
                    methodModifiers36 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers36.tree)



                self.following.append(self.FOLLOW_type_in_method502)
                type37 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type37.tree)
                self.following.append(self.FOLLOW_validId_in_method506)
                name = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(name.tree)
                char_literal38 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_method508)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal38)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:43: ( paramList )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == 58 or (77 <= LA11_0 <= 79)) :
                    alt11 = 1
                if alt11 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:43: paramList
                    self.following.append(self.FOLLOW_paramList_in_method510)
                    paramList39 = self.paramList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_paramList.add(paramList39.tree)



                char_literal40 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_method513)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_70.add(char_literal40)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:58: ( 'raises' '(' raises= validId ( ',' raises= validId )* ')' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 71) :
                    alt13 = 1
                if alt13 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:59: 'raises' '(' raises= validId ( ',' raises= validId )* ')'
                    string_literal41 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_method516)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_71.add(string_literal41)
                    char_literal42 = self.input.LT(1)
                    self.match(self.input, 69, self.FOLLOW_69_in_method518)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_69.add(char_literal42)
                    self.following.append(self.FOLLOW_validId_in_method522)
                    raises = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(raises.tree)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:87: ( ',' raises= validId )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == 59) :
                            alt12 = 1


                        if alt12 == 1:
                            # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:88: ',' raises= validId
                            char_literal43 = self.input.LT(1)
                            self.match(self.input, 59, self.FOLLOW_59_in_method525)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_59.add(char_literal43)
                            self.following.append(self.FOLLOW_validId_in_method529)
                            raises = self.validId()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_validId.add(raises.tree)


                        else:
                            break #loop12


                    char_literal44 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_method533)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_70.add(char_literal44)



                char_literal45 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_method537)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_57.add(char_literal45)
                # AST Rewrite
                # elements: name, methodModifiers, paramList, type, raises
                # token labels: 
                # rule labels: retval, raises, name
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    if raises is not None:
                        stream_raises = RewriteRuleSubtreeStream(self.adaptor, "token raises", raises.tree)
                    else:
                        stream_raises = RewriteRuleSubtreeStream(self.adaptor, "token raises", None)


                    if name is not None:
                        stream_name = RewriteRuleSubtreeStream(self.adaptor, "token name", name.tree)
                    else:
                        stream_name = RewriteRuleSubtreeStream(self.adaptor, "token name", None)


                    root_0 = self.adaptor.nil()
                    # 150:3: -> ^( METHOD type $name ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS ( paramList )? ) ^( RAISES ( $raises)* ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:6: ^( METHOD type $name ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS ( paramList )? ) ^( RAISES ( $raises)* ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(METHOD, "METHOD"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_name.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:26: ^( MODIFIERS ( methodModifiers )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:38: ( methodModifiers )?
                    if stream_methodModifiers.hasNext():
                        self.adaptor.addChild(root_2, stream_methodModifiers.next())


                    stream_methodModifiers.reset();

                    self.adaptor.addChild(root_1, root_2)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:56: ^( PARAMS ( paramList )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARAMS, "PARAMS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:65: ( paramList )?
                    if stream_paramList.hasNext():
                        self.adaptor.addChild(root_2, stream_paramList.next())


                    stream_paramList.reset();

                    self.adaptor.addChild(root_1, root_2)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:77: ^( RAISES ( $raises)* )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(RAISES, "RAISES"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:86: ( $raises)*
                    while stream_raises.hasNext():
                        self.adaptor.addChild(root_2, stream_raises.next())


                    stream_raises.reset();

                    self.adaptor.addChild(root_1, root_2)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end method

    class const_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start const
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:154:1: const : 'const' type validId '=' mathExpr ';' -> ^( CONST type validId mathExpr ) ;
    def const(self, ):

        retval = self.const_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal46 = None
        char_literal49 = None
        char_literal51 = None
        type47 = None

        validId48 = None

        mathExpr50 = None


        string_literal46_tree = None
        char_literal49_tree = None
        char_literal51_tree = None
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_72 = RewriteRuleTokenStream(self.adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self.adaptor, "token 73")
        stream_mathExpr = RewriteRuleSubtreeStream(self.adaptor, "rule mathExpr")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:2: ( 'const' type validId '=' mathExpr ';' -> ^( CONST type validId mathExpr ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:4: 'const' type validId '=' mathExpr ';'
                string_literal46 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_const584)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_72.add(string_literal46)
                self.following.append(self.FOLLOW_type_in_const586)
                type47 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type47.tree)
                self.following.append(self.FOLLOW_validId_in_const588)
                validId48 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId48.tree)
                char_literal49 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_const590)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_73.add(char_literal49)
                self.following.append(self.FOLLOW_mathExpr_in_const592)
                mathExpr50 = self.mathExpr()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_mathExpr.add(mathExpr50.tree)
                char_literal51 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_const594)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_57.add(char_literal51)
                # AST Rewrite
                # elements: validId, mathExpr, type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 156:3: -> ^( CONST type validId mathExpr )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:156:6: ^( CONST type validId mathExpr )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CONST, "CONST"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    self.adaptor.addChild(root_1, stream_mathExpr.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end const

    class attribute_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start attribute
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:159:1: attribute : ( methodModifiers )? ( 'readonly' )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS ( methodModifiers )? ( 'readonly' )? ) ) ;
    def attribute(self, ):

        retval = self.attribute_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal53 = None
        string_literal54 = None
        char_literal57 = None
        methodModifiers52 = None

        type55 = None

        validId56 = None


        string_literal53_tree = None
        string_literal54_tree = None
        char_literal57_tree = None
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_74 = RewriteRuleTokenStream(self.adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self.adaptor, "token 75")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:2: ( ( methodModifiers )? ( 'readonly' )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS ( methodModifiers )? ( 'readonly' )? ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:4: ( methodModifiers )? ( 'readonly' )? 'attribute' type validId ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:4: ( methodModifiers )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 58) :
                    alt14 = 1
                if alt14 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_attribute619)
                    methodModifiers52 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers52.tree)



                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:21: ( 'readonly' )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 74) :
                    alt15 = 1
                if alt15 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:21: 'readonly'
                    string_literal53 = self.input.LT(1)
                    self.match(self.input, 74, self.FOLLOW_74_in_attribute622)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_74.add(string_literal53)



                string_literal54 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_attribute625)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_75.add(string_literal54)
                self.following.append(self.FOLLOW_type_in_attribute627)
                type55 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type55.tree)
                self.following.append(self.FOLLOW_validId_in_attribute629)
                validId56 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId56.tree)
                char_literal57 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_attribute631)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_57.add(char_literal57)
                # AST Rewrite
                # elements: validId, methodModifiers, 74, type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 161:3: -> ^( ATTR type validId ^( MODIFIERS ( methodModifiers )? ( 'readonly' )? ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:161:6: ^( ATTR type validId ^( MODIFIERS ( methodModifiers )? ( 'readonly' )? ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ATTR, "ATTR"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:161:26: ^( MODIFIERS ( methodModifiers )? ( 'readonly' )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:161:38: ( methodModifiers )?
                    if stream_methodModifiers.hasNext():
                        self.adaptor.addChild(root_2, stream_methodModifiers.next())


                    stream_methodModifiers.reset();
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:161:55: ( 'readonly' )?
                    if stream_74.hasNext():
                        self.adaptor.addChild(root_2, stream_74.next())


                    stream_74.reset();

                    self.adaptor.addChild(root_1, root_2)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end attribute

    class methodModifiers_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start methodModifiers
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:1: methodModifiers : '[' methodModifier ( ',' methodModifier )* ']' -> ( methodModifier )* ;
    def methodModifiers(self, ):

        retval = self.methodModifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal58 = None
        char_literal60 = None
        char_literal62 = None
        methodModifier59 = None

        methodModifier61 = None


        char_literal58_tree = None
        char_literal60_tree = None
        char_literal62_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_methodModifier = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:2: ( '[' methodModifier ( ',' methodModifier )* ']' -> ( methodModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:4: '[' methodModifier ( ',' methodModifier )* ']'
                char_literal58 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_methodModifiers664)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_58.add(char_literal58)
                self.following.append(self.FOLLOW_methodModifier_in_methodModifiers666)
                methodModifier59 = self.methodModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_methodModifier.add(methodModifier59.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:23: ( ',' methodModifier )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 59) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:24: ',' methodModifier
                        char_literal60 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_methodModifiers669)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_59.add(char_literal60)
                        self.following.append(self.FOLLOW_methodModifier_in_methodModifiers671)
                        methodModifier61 = self.methodModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_methodModifier.add(methodModifier61.tree)


                    else:
                        break #loop16


                char_literal62 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_methodModifiers675)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_60.add(char_literal62)
                # AST Rewrite
                # elements: methodModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 166:3: -> ( methodModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:166:6: ( methodModifier )*
                    while stream_methodModifier.hasNext():
                        self.adaptor.addChild(root_0, stream_methodModifier.next())


                    stream_methodModifier.reset();






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end methodModifiers

    class methodModifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start methodModifier
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:169:1: methodModifier : ( 'noscript' | 'notxpcom' | binaryName );
    def methodModifier(self, ):

        retval = self.methodModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal63 = None
        string_literal64 = None
        binaryName65 = None


        string_literal63_tree = None
        string_literal64_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:2: ( 'noscript' | 'notxpcom' | binaryName )
                alt17 = 3
                LA17 = self.input.LA(1)
                if LA17 == 68:
                    alt17 = 1
                elif LA17 == 67:
                    alt17 = 2
                elif LA17 == 76:
                    alt17 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("169:1: methodModifier : ( 'noscript' | 'notxpcom' | binaryName );", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:4: 'noscript'
                    root_0 = self.adaptor.nil()

                    string_literal63 = self.input.LT(1)
                    self.match(self.input, 68, self.FOLLOW_68_in_methodModifier693)
                    if self.failed:
                        return retval

                    string_literal63_tree = self.adaptor.createWithPayload(string_literal63)
                    self.adaptor.addChild(root_0, string_literal63_tree)



                elif alt17 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:171:4: 'notxpcom'
                    root_0 = self.adaptor.nil()

                    string_literal64 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_methodModifier698)
                    if self.failed:
                        return retval

                    string_literal64_tree = self.adaptor.createWithPayload(string_literal64)
                    self.adaptor.addChild(root_0, string_literal64_tree)



                elif alt17 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:172:4: binaryName
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_binaryName_in_methodModifier703)
                    binaryName65 = self.binaryName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, binaryName65.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end methodModifier

    class binaryName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start binaryName
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:175:1: binaryName : 'binaryname' '(' validId ')' -> ^( BINARY_NAME validId ) ;
    def binaryName(self, ):

        retval = self.binaryName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal66 = None
        char_literal67 = None
        char_literal69 = None
        validId68 = None


        string_literal66_tree = None
        char_literal67_tree = None
        char_literal69_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_76 = RewriteRuleTokenStream(self.adaptor, "token 76")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:176:2: ( 'binaryname' '(' validId ')' -> ^( BINARY_NAME validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:176:4: 'binaryname' '(' validId ')'
                string_literal66 = self.input.LT(1)
                self.match(self.input, 76, self.FOLLOW_76_in_binaryName714)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_76.add(string_literal66)
                char_literal67 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_binaryName716)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal67)
                self.following.append(self.FOLLOW_validId_in_binaryName718)
                validId68 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId68.tree)
                char_literal69 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_binaryName720)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_70.add(char_literal69)
                # AST Rewrite
                # elements: validId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 177:3: -> ^( BINARY_NAME validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:177:6: ^( BINARY_NAME validId )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(BINARY_NAME, "BINARY_NAME"), root_1)

                    self.adaptor.addChild(root_1, stream_validId.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end binaryName

    class paramList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramList
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:180:1: paramList : paramDecl ( ',' paramDecl )* -> ( paramDecl )* ;
    def paramList(self, ):

        retval = self.paramList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal71 = None
        paramDecl70 = None

        paramDecl72 = None


        char_literal71_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_paramDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramDecl")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:181:2: ( paramDecl ( ',' paramDecl )* -> ( paramDecl )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:181:4: paramDecl ( ',' paramDecl )*
                self.following.append(self.FOLLOW_paramDecl_in_paramList741)
                paramDecl70 = self.paramDecl()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramDecl.add(paramDecl70.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:181:14: ( ',' paramDecl )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 59) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:181:15: ',' paramDecl
                        char_literal71 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_paramList744)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_59.add(char_literal71)
                        self.following.append(self.FOLLOW_paramDecl_in_paramList746)
                        paramDecl72 = self.paramDecl()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramDecl.add(paramDecl72.tree)


                    else:
                        break #loop18


                # AST Rewrite
                # elements: paramDecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 182:3: -> ( paramDecl )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:182:6: ( paramDecl )*
                    while stream_paramDecl.hasNext():
                        self.adaptor.addChild(root_0, stream_paramDecl.next())


                    stream_paramDecl.reset();






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end paramList

    class paramDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:185:1: paramDecl : ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) ;
    def paramDecl(self, ):

        retval = self.paramDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        paramModifiersDecl73 = None

        paramType74 = None

        type75 = None

        validId76 = None


        stream_paramModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        stream_paramType = RewriteRuleSubtreeStream(self.adaptor, "rule paramType")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:2: ( ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:4: ( paramModifiersDecl )? paramType type validId
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:4: ( paramModifiersDecl )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == 58) :
                    alt19 = 1
                if alt19 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:4: paramModifiersDecl
                    self.following.append(self.FOLLOW_paramModifiersDecl_in_paramDecl766)
                    paramModifiersDecl73 = self.paramModifiersDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_paramModifiersDecl.add(paramModifiersDecl73.tree)



                self.following.append(self.FOLLOW_paramType_in_paramDecl769)
                paramType74 = self.paramType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramType.add(paramType74.tree)
                self.following.append(self.FOLLOW_type_in_paramDecl771)
                type75 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type75.tree)
                self.following.append(self.FOLLOW_validId_in_paramDecl773)
                validId76 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId76.tree)
                # AST Rewrite
                # elements: type, paramModifiersDecl, paramType, validId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 187:3: -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:187:6: ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARAM, "PARAM"), root_1)

                    self.adaptor.addChild(root_1, stream_paramType.next())
                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:187:37: ^( MODIFIERS ( paramModifiersDecl )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:187:49: ( paramModifiersDecl )?
                    if stream_paramModifiersDecl.hasNext():
                        self.adaptor.addChild(root_2, stream_paramModifiersDecl.next())


                    stream_paramModifiersDecl.reset();

                    self.adaptor.addChild(root_1, root_2)

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end paramDecl

    class paramType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramType
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:190:1: paramType : ( 'in' | 'out' | 'inout' );
    def paramType(self, ):

        retval = self.paramType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set77 = None

        set77_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:191:2: ( 'in' | 'out' | 'inout' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set77 = self.input.LT(1)
                if (77 <= self.input.LA(1) <= 79):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set77))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_paramType0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end paramType

    class paramModifiersDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramModifiersDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:196:1: paramModifiersDecl : '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* ;
    def paramModifiersDecl(self, ):

        retval = self.paramModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal78 = None
        char_literal80 = None
        char_literal82 = None
        paramModifier79 = None

        paramModifier81 = None


        char_literal78_tree = None
        char_literal80_tree = None
        char_literal82_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_paramModifier = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:197:2: ( '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:197:4: '[' paramModifier ( ',' paramModifier )* ']'
                char_literal78 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_paramModifiersDecl826)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_58.add(char_literal78)
                self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl828)
                paramModifier79 = self.paramModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramModifier.add(paramModifier79.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:197:22: ( ',' paramModifier )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == 59) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:197:23: ',' paramModifier
                        char_literal80 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_paramModifiersDecl831)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_59.add(char_literal80)
                        self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl833)
                        paramModifier81 = self.paramModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramModifier.add(paramModifier81.tree)


                    else:
                        break #loop20


                char_literal82 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_paramModifiersDecl837)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_60.add(char_literal82)
                # AST Rewrite
                # elements: paramModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 198:3: -> ( paramModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:198:6: ( paramModifier )*
                    while stream_paramModifier.hasNext():
                        self.adaptor.addChild(root_0, stream_paramModifier.next())


                    stream_paramModifier.reset();






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end paramModifiersDecl

    class paramModifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramModifier
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:201:1: paramModifier : ( 'array' | sizeIs | iidIs | 'retval' | 'const' | 'shared' | 'optional' );
    def paramModifier(self, ):

        retval = self.paramModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal83 = None
        string_literal86 = None
        string_literal87 = None
        string_literal88 = None
        string_literal89 = None
        sizeIs84 = None

        iidIs85 = None


        string_literal83_tree = None
        string_literal86_tree = None
        string_literal87_tree = None
        string_literal88_tree = None
        string_literal89_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:202:2: ( 'array' | sizeIs | iidIs | 'retval' | 'const' | 'shared' | 'optional' )
                alt21 = 7
                LA21 = self.input.LA(1)
                if LA21 == 80:
                    alt21 = 1
                elif LA21 == 84:
                    alt21 = 2
                elif LA21 == 85:
                    alt21 = 3
                elif LA21 == 81:
                    alt21 = 4
                elif LA21 == 72:
                    alt21 = 5
                elif LA21 == 82:
                    alt21 = 6
                elif LA21 == 83:
                    alt21 = 7
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("201:1: paramModifier : ( 'array' | sizeIs | iidIs | 'retval' | 'const' | 'shared' | 'optional' );", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:202:4: 'array'
                    root_0 = self.adaptor.nil()

                    string_literal83 = self.input.LT(1)
                    self.match(self.input, 80, self.FOLLOW_80_in_paramModifier855)
                    if self.failed:
                        return retval

                    string_literal83_tree = self.adaptor.createWithPayload(string_literal83)
                    self.adaptor.addChild(root_0, string_literal83_tree)



                elif alt21 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:203:4: sizeIs
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_sizeIs_in_paramModifier860)
                    sizeIs84 = self.sizeIs()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, sizeIs84.tree)


                elif alt21 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:204:4: iidIs
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iidIs_in_paramModifier865)
                    iidIs85 = self.iidIs()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iidIs85.tree)


                elif alt21 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:205:4: 'retval'
                    root_0 = self.adaptor.nil()

                    string_literal86 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_paramModifier870)
                    if self.failed:
                        return retval

                    string_literal86_tree = self.adaptor.createWithPayload(string_literal86)
                    self.adaptor.addChild(root_0, string_literal86_tree)



                elif alt21 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:206:4: 'const'
                    root_0 = self.adaptor.nil()

                    string_literal87 = self.input.LT(1)
                    self.match(self.input, 72, self.FOLLOW_72_in_paramModifier875)
                    if self.failed:
                        return retval

                    string_literal87_tree = self.adaptor.createWithPayload(string_literal87)
                    self.adaptor.addChild(root_0, string_literal87_tree)



                elif alt21 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:4: 'shared'
                    root_0 = self.adaptor.nil()

                    string_literal88 = self.input.LT(1)
                    self.match(self.input, 82, self.FOLLOW_82_in_paramModifier880)
                    if self.failed:
                        return retval

                    string_literal88_tree = self.adaptor.createWithPayload(string_literal88)
                    self.adaptor.addChild(root_0, string_literal88_tree)



                elif alt21 == 7:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:208:4: 'optional'
                    root_0 = self.adaptor.nil()

                    string_literal89 = self.input.LT(1)
                    self.match(self.input, 83, self.FOLLOW_83_in_paramModifier885)
                    if self.failed:
                        return retval

                    string_literal89_tree = self.adaptor.createWithPayload(string_literal89)
                    self.adaptor.addChild(root_0, string_literal89_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end paramModifier

    class sizeIs_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sizeIs
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:211:1: sizeIs : 'size_is' '(' validId ')' -> ^( SIZE_IS validId ) ;
    def sizeIs(self, ):

        retval = self.sizeIs_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal90 = None
        char_literal91 = None
        char_literal93 = None
        validId92 = None


        string_literal90_tree = None
        char_literal91_tree = None
        char_literal93_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_84 = RewriteRuleTokenStream(self.adaptor, "token 84")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:212:2: ( 'size_is' '(' validId ')' -> ^( SIZE_IS validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:212:4: 'size_is' '(' validId ')'
                string_literal90 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_sizeIs897)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_84.add(string_literal90)
                char_literal91 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_sizeIs899)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal91)
                self.following.append(self.FOLLOW_validId_in_sizeIs901)
                validId92 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId92.tree)
                char_literal93 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_sizeIs903)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_70.add(char_literal93)
                # AST Rewrite
                # elements: validId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 213:3: -> ^( SIZE_IS validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:213:6: ^( SIZE_IS validId )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(SIZE_IS, "SIZE_IS"), root_1)

                    self.adaptor.addChild(root_1, stream_validId.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end sizeIs

    class iidIs_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start iidIs
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:216:1: iidIs : 'iid_is' '(' validId ')' -> ^( IID_IS validId ) ;
    def iidIs(self, ):

        retval = self.iidIs_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal94 = None
        char_literal95 = None
        char_literal97 = None
        validId96 = None


        string_literal94_tree = None
        char_literal95_tree = None
        char_literal97_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_85 = RewriteRuleTokenStream(self.adaptor, "token 85")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:217:2: ( 'iid_is' '(' validId ')' -> ^( IID_IS validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:217:4: 'iid_is' '(' validId ')'
                string_literal94 = self.input.LT(1)
                self.match(self.input, 85, self.FOLLOW_85_in_iidIs925)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_85.add(string_literal94)
                char_literal95 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_iidIs927)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal95)
                self.following.append(self.FOLLOW_validId_in_iidIs929)
                validId96 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId96.tree)
                char_literal97 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_iidIs931)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_70.add(char_literal97)
                # AST Rewrite
                # elements: validId
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 218:3: -> ^( IID_IS validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:218:6: ^( IID_IS validId )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(IID_IS, "IID_IS"), root_1)

                    self.adaptor.addChild(root_1, stream_validId.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end iidIs

    class nativeTypeDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start nativeTypeDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:221:1: nativeTypeDecl : nativeType ';' ;
    def nativeTypeDecl(self, ):

        retval = self.nativeTypeDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal99 = None
        nativeType98 = None


        char_literal99_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:222:2: ( nativeType ';' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:222:4: nativeType ';'
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_nativeType_in_nativeTypeDecl952)
                nativeType98 = self.nativeType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, nativeType98.tree)
                char_literal99 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_nativeTypeDecl954)
                if self.failed:
                    return retval



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end nativeTypeDecl

    class nativeType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start nativeType
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:225:1: nativeType : ( typeModifiersDecl )? 'native' name= validId '(' ( nativeTypePayload )+ ')' -> ^( NATIVE $name ^( MODIFIERS ( typeModifiersDecl )? ) ( nativeTypePayload )+ ) ;
    def nativeType(self, ):

        retval = self.nativeType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal101 = None
        char_literal102 = None
        char_literal104 = None
        name = None

        typeModifiersDecl100 = None

        nativeTypePayload103 = None


        string_literal101_tree = None
        char_literal102_tree = None
        char_literal104_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_86 = RewriteRuleTokenStream(self.adaptor, "token 86")
        stream_typeModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_nativeTypePayload = RewriteRuleSubtreeStream(self.adaptor, "rule nativeTypePayload")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:2: ( ( typeModifiersDecl )? 'native' name= validId '(' ( nativeTypePayload )+ ')' -> ^( NATIVE $name ^( MODIFIERS ( typeModifiersDecl )? ) ( nativeTypePayload )+ ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:4: ( typeModifiersDecl )? 'native' name= validId '(' ( nativeTypePayload )+ ')'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:4: ( typeModifiersDecl )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 58) :
                    alt22 = 1
                if alt22 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:4: typeModifiersDecl
                    self.following.append(self.FOLLOW_typeModifiersDecl_in_nativeType966)
                    typeModifiersDecl100 = self.typeModifiersDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_typeModifiersDecl.add(typeModifiersDecl100.tree)



                string_literal101 = self.input.LT(1)
                self.match(self.input, 86, self.FOLLOW_86_in_nativeType969)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_86.add(string_literal101)
                self.following.append(self.FOLLOW_validId_in_nativeType973)
                name = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(name.tree)
                char_literal102 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_nativeType975)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal102)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:49: ( nativeTypePayload )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == Identifier or LA23_0 == 56 or (64 <= LA23_0 <= 68) or LA23_0 == 72 or (80 <= LA23_0 <= 83) or LA23_0 == 85 or (87 <= LA23_0 <= 109)) :
                        alt23 = 1


                    if alt23 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:226:49: nativeTypePayload
                        self.following.append(self.FOLLOW_nativeTypePayload_in_nativeType977)
                        nativeTypePayload103 = self.nativeTypePayload()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_nativeTypePayload.add(nativeTypePayload103.tree)


                    else:
                        if cnt23 >= 1:
                            break #loop23

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1


                char_literal104 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_nativeType980)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_70.add(char_literal104)
                # AST Rewrite
                # elements: name, nativeTypePayload, typeModifiersDecl
                # token labels: 
                # rule labels: retval, name
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    if name is not None:
                        stream_name = RewriteRuleSubtreeStream(self.adaptor, "token name", name.tree)
                    else:
                        stream_name = RewriteRuleSubtreeStream(self.adaptor, "token name", None)


                    root_0 = self.adaptor.nil()
                    # 227:3: -> ^( NATIVE $name ^( MODIFIERS ( typeModifiersDecl )? ) ( nativeTypePayload )+ )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:6: ^( NATIVE $name ^( MODIFIERS ( typeModifiersDecl )? ) ( nativeTypePayload )+ )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NATIVE, "NATIVE"), root_1)

                    self.adaptor.addChild(root_1, stream_name.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:21: ^( MODIFIERS ( typeModifiersDecl )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:33: ( typeModifiersDecl )?
                    if stream_typeModifiersDecl.hasNext():
                        self.adaptor.addChild(root_2, stream_typeModifiersDecl.next())


                    stream_typeModifiersDecl.reset();

                    self.adaptor.addChild(root_1, root_2)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:53: ( nativeTypePayload )+
                    if not (stream_nativeTypePayload.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_nativeTypePayload.hasNext():
                        self.adaptor.addChild(root_1, stream_nativeTypePayload.next())


                    stream_nativeTypePayload.reset()

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end nativeType

    class nativeTypePayload_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start nativeTypePayload
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:230:1: nativeTypePayload : ( 'boolean' | 'void' | 'string' | 'octet' | 'char' | 'short' | 'long' | 'unsigned' | 'float' | 'double' | 'wchar' | 'wstring' | '*' | '&' | '<' | '>' | validId );
    def nativeTypePayload(self, ):

        retval = self.nativeTypePayload_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal105 = None
        string_literal106 = None
        string_literal107 = None
        string_literal108 = None
        string_literal109 = None
        string_literal110 = None
        string_literal111 = None
        string_literal112 = None
        string_literal113 = None
        string_literal114 = None
        string_literal115 = None
        string_literal116 = None
        char_literal117 = None
        char_literal118 = None
        char_literal119 = None
        char_literal120 = None
        validId121 = None


        string_literal105_tree = None
        string_literal106_tree = None
        string_literal107_tree = None
        string_literal108_tree = None
        string_literal109_tree = None
        string_literal110_tree = None
        string_literal111_tree = None
        string_literal112_tree = None
        string_literal113_tree = None
        string_literal114_tree = None
        string_literal115_tree = None
        string_literal116_tree = None
        char_literal117_tree = None
        char_literal118_tree = None
        char_literal119_tree = None
        char_literal120_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:231:2: ( 'boolean' | 'void' | 'string' | 'octet' | 'char' | 'short' | 'long' | 'unsigned' | 'float' | 'double' | 'wchar' | 'wstring' | '*' | '&' | '<' | '>' | validId )
                alt24 = 17
                LA24 = self.input.LA(1)
                if LA24 == 87:
                    alt24 = 1
                elif LA24 == 88:
                    alt24 = 2
                elif LA24 == 89:
                    alt24 = 3
                elif LA24 == 90:
                    alt24 = 4
                elif LA24 == 91:
                    alt24 = 5
                elif LA24 == 92:
                    alt24 = 6
                elif LA24 == 93:
                    alt24 = 7
                elif LA24 == 94:
                    alt24 = 8
                elif LA24 == 95:
                    alt24 = 9
                elif LA24 == 96:
                    alt24 = 10
                elif LA24 == 97:
                    alt24 = 11
                elif LA24 == 98:
                    alt24 = 12
                elif LA24 == 99:
                    alt24 = 13
                elif LA24 == 100:
                    alt24 = 14
                elif LA24 == 101:
                    alt24 = 15
                elif LA24 == 102:
                    alt24 = 16
                elif LA24 == Identifier or LA24 == 56 or LA24 == 64 or LA24 == 65 or LA24 == 66 or LA24 == 67 or LA24 == 68 or LA24 == 72 or LA24 == 80 or LA24 == 81 or LA24 == 82 or LA24 == 83 or LA24 == 85 or LA24 == 103 or LA24 == 104 or LA24 == 105 or LA24 == 106 or LA24 == 107 or LA24 == 108 or LA24 == 109:
                    alt24 = 17
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("230:1: nativeTypePayload : ( 'boolean' | 'void' | 'string' | 'octet' | 'char' | 'short' | 'long' | 'unsigned' | 'float' | 'double' | 'wchar' | 'wstring' | '*' | '&' | '<' | '>' | validId );", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:231:4: 'boolean'
                    root_0 = self.adaptor.nil()

                    string_literal105 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_nativeTypePayload1012)
                    if self.failed:
                        return retval

                    string_literal105_tree = self.adaptor.createWithPayload(string_literal105)
                    self.adaptor.addChild(root_0, string_literal105_tree)



                elif alt24 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:232:4: 'void'
                    root_0 = self.adaptor.nil()

                    string_literal106 = self.input.LT(1)
                    self.match(self.input, 88, self.FOLLOW_88_in_nativeTypePayload1017)
                    if self.failed:
                        return retval

                    string_literal106_tree = self.adaptor.createWithPayload(string_literal106)
                    self.adaptor.addChild(root_0, string_literal106_tree)



                elif alt24 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:233:4: 'string'
                    root_0 = self.adaptor.nil()

                    string_literal107 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_nativeTypePayload1022)
                    if self.failed:
                        return retval

                    string_literal107_tree = self.adaptor.createWithPayload(string_literal107)
                    self.adaptor.addChild(root_0, string_literal107_tree)



                elif alt24 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:234:4: 'octet'
                    root_0 = self.adaptor.nil()

                    string_literal108 = self.input.LT(1)
                    self.match(self.input, 90, self.FOLLOW_90_in_nativeTypePayload1027)
                    if self.failed:
                        return retval

                    string_literal108_tree = self.adaptor.createWithPayload(string_literal108)
                    self.adaptor.addChild(root_0, string_literal108_tree)



                elif alt24 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:235:4: 'char'
                    root_0 = self.adaptor.nil()

                    string_literal109 = self.input.LT(1)
                    self.match(self.input, 91, self.FOLLOW_91_in_nativeTypePayload1032)
                    if self.failed:
                        return retval

                    string_literal109_tree = self.adaptor.createWithPayload(string_literal109)
                    self.adaptor.addChild(root_0, string_literal109_tree)



                elif alt24 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:236:4: 'short'
                    root_0 = self.adaptor.nil()

                    string_literal110 = self.input.LT(1)
                    self.match(self.input, 92, self.FOLLOW_92_in_nativeTypePayload1037)
                    if self.failed:
                        return retval

                    string_literal110_tree = self.adaptor.createWithPayload(string_literal110)
                    self.adaptor.addChild(root_0, string_literal110_tree)



                elif alt24 == 7:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:237:4: 'long'
                    root_0 = self.adaptor.nil()

                    string_literal111 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_nativeTypePayload1042)
                    if self.failed:
                        return retval

                    string_literal111_tree = self.adaptor.createWithPayload(string_literal111)
                    self.adaptor.addChild(root_0, string_literal111_tree)



                elif alt24 == 8:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:238:4: 'unsigned'
                    root_0 = self.adaptor.nil()

                    string_literal112 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_nativeTypePayload1047)
                    if self.failed:
                        return retval

                    string_literal112_tree = self.adaptor.createWithPayload(string_literal112)
                    self.adaptor.addChild(root_0, string_literal112_tree)



                elif alt24 == 9:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:239:4: 'float'
                    root_0 = self.adaptor.nil()

                    string_literal113 = self.input.LT(1)
                    self.match(self.input, 95, self.FOLLOW_95_in_nativeTypePayload1052)
                    if self.failed:
                        return retval

                    string_literal113_tree = self.adaptor.createWithPayload(string_literal113)
                    self.adaptor.addChild(root_0, string_literal113_tree)



                elif alt24 == 10:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:240:4: 'double'
                    root_0 = self.adaptor.nil()

                    string_literal114 = self.input.LT(1)
                    self.match(self.input, 96, self.FOLLOW_96_in_nativeTypePayload1057)
                    if self.failed:
                        return retval

                    string_literal114_tree = self.adaptor.createWithPayload(string_literal114)
                    self.adaptor.addChild(root_0, string_literal114_tree)



                elif alt24 == 11:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:241:4: 'wchar'
                    root_0 = self.adaptor.nil()

                    string_literal115 = self.input.LT(1)
                    self.match(self.input, 97, self.FOLLOW_97_in_nativeTypePayload1062)
                    if self.failed:
                        return retval

                    string_literal115_tree = self.adaptor.createWithPayload(string_literal115)
                    self.adaptor.addChild(root_0, string_literal115_tree)



                elif alt24 == 12:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:242:4: 'wstring'
                    root_0 = self.adaptor.nil()

                    string_literal116 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_nativeTypePayload1067)
                    if self.failed:
                        return retval

                    string_literal116_tree = self.adaptor.createWithPayload(string_literal116)
                    self.adaptor.addChild(root_0, string_literal116_tree)



                elif alt24 == 13:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:243:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal117 = self.input.LT(1)
                    self.match(self.input, 99, self.FOLLOW_99_in_nativeTypePayload1072)
                    if self.failed:
                        return retval

                    char_literal117_tree = self.adaptor.createWithPayload(char_literal117)
                    self.adaptor.addChild(root_0, char_literal117_tree)



                elif alt24 == 14:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:244:4: '&'
                    root_0 = self.adaptor.nil()

                    char_literal118 = self.input.LT(1)
                    self.match(self.input, 100, self.FOLLOW_100_in_nativeTypePayload1077)
                    if self.failed:
                        return retval

                    char_literal118_tree = self.adaptor.createWithPayload(char_literal118)
                    self.adaptor.addChild(root_0, char_literal118_tree)



                elif alt24 == 15:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:245:4: '<'
                    root_0 = self.adaptor.nil()

                    char_literal119 = self.input.LT(1)
                    self.match(self.input, 101, self.FOLLOW_101_in_nativeTypePayload1082)
                    if self.failed:
                        return retval

                    char_literal119_tree = self.adaptor.createWithPayload(char_literal119)
                    self.adaptor.addChild(root_0, char_literal119_tree)



                elif alt24 == 16:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:246:4: '>'
                    root_0 = self.adaptor.nil()

                    char_literal120 = self.input.LT(1)
                    self.match(self.input, 102, self.FOLLOW_102_in_nativeTypePayload1087)
                    if self.failed:
                        return retval

                    char_literal120_tree = self.adaptor.createWithPayload(char_literal120)
                    self.adaptor.addChild(root_0, char_literal120_tree)



                elif alt24 == 17:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:247:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_nativeTypePayload1092)
                    validId121 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId121.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end nativeTypePayload

    class typeModifiersDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start typeModifiersDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:250:1: typeModifiersDecl : '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ ;
    def typeModifiersDecl(self, ):

        retval = self.typeModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal122 = None
        char_literal124 = None
        char_literal126 = None
        typeModifier123 = None

        typeModifier125 = None


        char_literal122_tree = None
        char_literal124_tree = None
        char_literal126_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_typeModifier = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:251:2: ( '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:251:4: '[' typeModifier ( ',' typeModifier )* ']'
                char_literal122 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_typeModifiersDecl1103)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_58.add(char_literal122)
                self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl1105)
                typeModifier123 = self.typeModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_typeModifier.add(typeModifier123.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:251:21: ( ',' typeModifier )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == 59) :
                        alt25 = 1


                    if alt25 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:251:22: ',' typeModifier
                        char_literal124 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_typeModifiersDecl1108)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_59.add(char_literal124)
                        self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl1110)
                        typeModifier125 = self.typeModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_typeModifier.add(typeModifier125.tree)


                    else:
                        break #loop25


                char_literal126 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_typeModifiersDecl1114)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_60.add(char_literal126)
                # AST Rewrite
                # elements: typeModifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 252:3: -> ( typeModifier )+
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:252:6: ( typeModifier )+
                    if not (stream_typeModifier.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_typeModifier.hasNext():
                        self.adaptor.addChild(root_0, stream_typeModifier.next())


                    stream_typeModifier.reset()






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end typeModifiersDecl

    class typeModifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start typeModifier
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:255:1: typeModifier : ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' );
    def typeModifier(self, ):

        retval = self.typeModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set127 = None

        set127_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:256:2: ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set127 = self.input.LT(1)
                if (103 <= self.input.LA(1) <= 109):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set127))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_typeModifier0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end typeModifier

    class typedef_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start typedef
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:265:1: typedef : 'typedef' type validId ';' -> ^( TYPEDEF type validId ) ;
    def typedef(self, ):

        retval = self.typedef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal128 = None
        char_literal131 = None
        type129 = None

        validId130 = None


        string_literal128_tree = None
        char_literal131_tree = None
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_110 = RewriteRuleTokenStream(self.adaptor, "token 110")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:266:2: ( 'typedef' type validId ';' -> ^( TYPEDEF type validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:266:4: 'typedef' type validId ';'
                string_literal128 = self.input.LT(1)
                self.match(self.input, 110, self.FOLLOW_110_in_typedef1173)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_110.add(string_literal128)
                self.following.append(self.FOLLOW_type_in_typedef1175)
                type129 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type129.tree)
                self.following.append(self.FOLLOW_validId_in_typedef1177)
                validId130 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId130.tree)
                char_literal131 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_typedef1179)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_57.add(char_literal131)
                # AST Rewrite
                # elements: validId, type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 267:3: -> ^( TYPEDEF type validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:267:6: ^( TYPEDEF type validId )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(TYPEDEF, "TYPEDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end typedef

    class type_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start type
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:270:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal132 = None
        string_literal133 = None
        string_literal134 = None
        string_literal135 = None
        string_literal136 = None
        string_literal137 = None
        string_literal138 = None
        string_literal139 = None
        string_literal140 = None
        string_literal141 = None
        string_literal142 = None
        string_literal143 = None
        string_literal144 = None
        string_literal145 = None
        string_literal146 = None
        string_literal147 = None
        string_literal148 = None
        string_literal149 = None
        string_literal150 = None
        string_literal151 = None
        string_literal152 = None
        string_literal153 = None
        validId154 = None


        string_literal132_tree = None
        string_literal133_tree = None
        string_literal134_tree = None
        string_literal135_tree = None
        string_literal136_tree = None
        string_literal137_tree = None
        string_literal138_tree = None
        string_literal139_tree = None
        string_literal140_tree = None
        string_literal141_tree = None
        string_literal142_tree = None
        string_literal143_tree = None
        string_literal144_tree = None
        string_literal145_tree = None
        string_literal146_tree = None
        string_literal147_tree = None
        string_literal148_tree = None
        string_literal149_tree = None
        string_literal150_tree = None
        string_literal151_tree = None
        string_literal152_tree = None
        string_literal153_tree = None
        stream_98 = RewriteRuleTokenStream(self.adaptor, "token 98")
        stream_97 = RewriteRuleTokenStream(self.adaptor, "token 97")
        stream_96 = RewriteRuleTokenStream(self.adaptor, "token 96")
        stream_95 = RewriteRuleTokenStream(self.adaptor, "token 95")
        stream_94 = RewriteRuleTokenStream(self.adaptor, "token 94")
        stream_93 = RewriteRuleTokenStream(self.adaptor, "token 93")
        stream_92 = RewriteRuleTokenStream(self.adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self.adaptor, "token 91")
        stream_90 = RewriteRuleTokenStream(self.adaptor, "token 90")
        stream_87 = RewriteRuleTokenStream(self.adaptor, "token 87")
        stream_88 = RewriteRuleTokenStream(self.adaptor, "token 88")
        stream_89 = RewriteRuleTokenStream(self.adaptor, "token 89")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:271:2: ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId )
                alt26 = 17
                LA26 = self.input.LA(1)
                if LA26 == 87:
                    alt26 = 1
                elif LA26 == 88:
                    alt26 = 2
                elif LA26 == 89:
                    alt26 = 3
                elif LA26 == 90:
                    alt26 = 4
                elif LA26 == 91:
                    alt26 = 5
                elif LA26 == 92:
                    alt26 = 6
                elif LA26 == 93:
                    LA26_7 = self.input.LA(2)

                    if (LA26_7 == 93) :
                        alt26 = 8
                    elif (LA26_7 == Identifier or LA26_7 == 56 or (64 <= LA26_7 <= 68) or LA26_7 == 72 or (80 <= LA26_7 <= 83) or LA26_7 == 85 or (103 <= LA26_7 <= 109)) :
                        alt26 = 7
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("270:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 26, 7, self.input)

                        raise nvae

                elif LA26 == 94:
                    LA26 = self.input.LA(2)
                    if LA26 == 92:
                        alt26 = 10
                    elif LA26 == 91:
                        alt26 = 9
                    elif LA26 == 93:
                        LA26_18 = self.input.LA(3)

                        if (LA26_18 == 93) :
                            alt26 = 12
                        elif (LA26_18 == Identifier or LA26_18 == 56 or (64 <= LA26_18 <= 68) or LA26_18 == 72 or (80 <= LA26_18 <= 83) or LA26_18 == 85 or (103 <= LA26_18 <= 109)) :
                            alt26 = 11
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("270:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 26, 18, self.input)

                            raise nvae

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("270:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 26, 8, self.input)

                        raise nvae

                elif LA26 == 95:
                    alt26 = 13
                elif LA26 == 96:
                    alt26 = 14
                elif LA26 == 97:
                    alt26 = 15
                elif LA26 == 98:
                    alt26 = 16
                elif LA26 == Identifier or LA26 == 56 or LA26 == 64 or LA26 == 65 or LA26 == 66 or LA26 == 67 or LA26 == 68 or LA26 == 72 or LA26 == 80 or LA26 == 81 or LA26 == 82 or LA26 == 83 or LA26 == 85 or LA26 == 103 or LA26 == 104 or LA26 == 105 or LA26 == 106 or LA26 == 107 or LA26 == 108 or LA26 == 109:
                    alt26 = 17
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("270:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'char' -> CHAR | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'char' -> UNSIGNED_CHAR | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 26, 0, self.input)

                    raise nvae

                if alt26 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:271:4: 'boolean'
                    string_literal132 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_type1202)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_87.add(string_literal132)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 271:14: -> BOOLEAN
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(BOOLEAN, "BOOLEAN"))





                elif alt26 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:272:4: 'void'
                    string_literal133 = self.input.LT(1)
                    self.match(self.input, 88, self.FOLLOW_88_in_type1211)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_88.add(string_literal133)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 272:11: -> VOID
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(VOID, "VOID"))





                elif alt26 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:273:4: 'string'
                    string_literal134 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_type1220)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_89.add(string_literal134)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 273:13: -> STRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(STRING, "STRING"))





                elif alt26 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:274:4: 'octet'
                    string_literal135 = self.input.LT(1)
                    self.match(self.input, 90, self.FOLLOW_90_in_type1229)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_90.add(string_literal135)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 274:12: -> OCTET
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(OCTET, "OCTET"))





                elif alt26 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:275:4: 'char'
                    string_literal136 = self.input.LT(1)
                    self.match(self.input, 91, self.FOLLOW_91_in_type1238)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_91.add(string_literal136)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 275:11: -> CHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(CHAR, "CHAR"))





                elif alt26 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:276:4: 'short'
                    string_literal137 = self.input.LT(1)
                    self.match(self.input, 92, self.FOLLOW_92_in_type1247)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_92.add(string_literal137)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 276:12: -> SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(SHORT, "SHORT"))





                elif alt26 == 7:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:277:4: 'long'
                    string_literal138 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1256)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal138)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 277:11: -> LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG, "LONG"))





                elif alt26 == 8:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:278:4: 'long' 'long'
                    string_literal139 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1265)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal139)
                    string_literal140 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1267)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal140)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 278:18: -> LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG_LONG, "LONG_LONG"))





                elif alt26 == 9:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:279:4: 'unsigned' 'char'
                    string_literal141 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_type1276)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_94.add(string_literal141)
                    string_literal142 = self.input.LT(1)
                    self.match(self.input, 91, self.FOLLOW_91_in_type1278)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_91.add(string_literal142)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 279:22: -> UNSIGNED_CHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_CHAR, "UNSIGNED_CHAR"))





                elif alt26 == 10:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:280:4: 'unsigned' 'short'
                    string_literal143 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_type1287)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_94.add(string_literal143)
                    string_literal144 = self.input.LT(1)
                    self.match(self.input, 92, self.FOLLOW_92_in_type1289)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_92.add(string_literal144)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 280:23: -> UNSIGNED_SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_SHORT, "UNSIGNED_SHORT"))





                elif alt26 == 11:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:281:4: 'unsigned' 'long'
                    string_literal145 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_type1298)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_94.add(string_literal145)
                    string_literal146 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1300)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal146)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 281:22: -> UNSIGNED_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG, "UNSIGNED_LONG"))





                elif alt26 == 12:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:282:4: 'unsigned' 'long' 'long'
                    string_literal147 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_type1309)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_94.add(string_literal147)
                    string_literal148 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1311)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal148)
                    string_literal149 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1313)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal149)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 282:29: -> UNSIGNED_LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG_LONG, "UNSIGNED_LONG_LONG"))





                elif alt26 == 13:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:283:4: 'float'
                    string_literal150 = self.input.LT(1)
                    self.match(self.input, 95, self.FOLLOW_95_in_type1322)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_95.add(string_literal150)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 283:12: -> FLOAT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(FLOAT, "FLOAT"))





                elif alt26 == 14:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:284:4: 'double'
                    string_literal151 = self.input.LT(1)
                    self.match(self.input, 96, self.FOLLOW_96_in_type1331)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_96.add(string_literal151)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 284:13: -> DOUBLE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(DOUBLE, "DOUBLE"))





                elif alt26 == 15:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:285:4: 'wchar'
                    string_literal152 = self.input.LT(1)
                    self.match(self.input, 97, self.FOLLOW_97_in_type1340)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_97.add(string_literal152)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 285:12: -> WCHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WCHAR, "WCHAR"))





                elif alt26 == 16:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:286:4: 'wstring'
                    string_literal153 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_type1349)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_98.add(string_literal153)
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 286:14: -> WSTRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WSTRING, "WSTRING"))





                elif alt26 == 17:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:287:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_type1358)
                    validId154 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId154.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end type

    class mathExpr_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathExpr
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:290:1: mathExpr : mathBitOr ;
    def mathExpr(self, ):

        retval = self.mathExpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mathBitOr155 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:291:2: ( mathBitOr )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:291:4: mathBitOr
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathBitOr_in_mathExpr1369)
                mathBitOr155 = self.mathBitOr()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathBitOr155.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathExpr

    class mathBitOr_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathBitOr
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:294:1: mathBitOr : mathBitXor ( '|' mathBitXor )* ;
    def mathBitOr(self, ):

        retval = self.mathBitOr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal157 = None
        mathBitXor156 = None

        mathBitXor158 = None


        char_literal157_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:295:2: ( mathBitXor ( '|' mathBitXor )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:295:4: mathBitXor ( '|' mathBitXor )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathBitXor_in_mathBitOr1381)
                mathBitXor156 = self.mathBitXor()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathBitXor156.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:295:15: ( '|' mathBitXor )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == 111) :
                        alt27 = 1


                    if alt27 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:295:16: '|' mathBitXor
                        char_literal157 = self.input.LT(1)
                        self.match(self.input, 111, self.FOLLOW_111_in_mathBitOr1384)
                        if self.failed:
                            return retval

                        char_literal157_tree = self.adaptor.createWithPayload(char_literal157)
                        self.adaptor.addChild(root_0, char_literal157_tree)

                        self.following.append(self.FOLLOW_mathBitXor_in_mathBitOr1386)
                        mathBitXor158 = self.mathBitXor()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathBitXor158.tree)


                    else:
                        break #loop27





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathBitOr

    class mathBitXor_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathBitXor
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:298:1: mathBitXor : mathBitAnd ( '^' mathBitAnd )* ;
    def mathBitXor(self, ):

        retval = self.mathBitXor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal160 = None
        mathBitAnd159 = None

        mathBitAnd161 = None


        char_literal160_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:299:2: ( mathBitAnd ( '^' mathBitAnd )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:299:4: mathBitAnd ( '^' mathBitAnd )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathBitAnd_in_mathBitXor1400)
                mathBitAnd159 = self.mathBitAnd()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathBitAnd159.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:299:15: ( '^' mathBitAnd )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == 112) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:299:16: '^' mathBitAnd
                        char_literal160 = self.input.LT(1)
                        self.match(self.input, 112, self.FOLLOW_112_in_mathBitXor1403)
                        if self.failed:
                            return retval

                        char_literal160_tree = self.adaptor.createWithPayload(char_literal160)
                        self.adaptor.addChild(root_0, char_literal160_tree)

                        self.following.append(self.FOLLOW_mathBitAnd_in_mathBitXor1405)
                        mathBitAnd161 = self.mathBitAnd()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathBitAnd161.tree)


                    else:
                        break #loop28





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathBitXor

    class mathBitAnd_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathBitAnd
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:302:1: mathBitAnd : mathShift ( '&' mathShift )* ;
    def mathBitAnd(self, ):

        retval = self.mathBitAnd_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal163 = None
        mathShift162 = None

        mathShift164 = None


        char_literal163_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:303:2: ( mathShift ( '&' mathShift )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:303:4: mathShift ( '&' mathShift )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathShift_in_mathBitAnd1418)
                mathShift162 = self.mathShift()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathShift162.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:303:14: ( '&' mathShift )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == 100) :
                        alt29 = 1


                    if alt29 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:303:15: '&' mathShift
                        char_literal163 = self.input.LT(1)
                        self.match(self.input, 100, self.FOLLOW_100_in_mathBitAnd1421)
                        if self.failed:
                            return retval

                        char_literal163_tree = self.adaptor.createWithPayload(char_literal163)
                        self.adaptor.addChild(root_0, char_literal163_tree)

                        self.following.append(self.FOLLOW_mathShift_in_mathBitAnd1423)
                        mathShift164 = self.mathShift()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathShift164.tree)


                    else:
                        break #loop29





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathBitAnd

    class mathShift_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathShift
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:306:1: mathShift : mathAddSub ( '<<' mathAddSub )* ;
    def mathShift(self, ):

        retval = self.mathShift_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal166 = None
        mathAddSub165 = None

        mathAddSub167 = None


        string_literal166_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:307:2: ( mathAddSub ( '<<' mathAddSub )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:307:4: mathAddSub ( '<<' mathAddSub )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathAddSub_in_mathShift1436)
                mathAddSub165 = self.mathAddSub()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathAddSub165.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:307:15: ( '<<' mathAddSub )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 113) :
                        alt30 = 1


                    if alt30 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:307:16: '<<' mathAddSub
                        string_literal166 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_mathShift1439)
                        if self.failed:
                            return retval

                        string_literal166_tree = self.adaptor.createWithPayload(string_literal166)
                        self.adaptor.addChild(root_0, string_literal166_tree)

                        self.following.append(self.FOLLOW_mathAddSub_in_mathShift1441)
                        mathAddSub167 = self.mathAddSub()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathAddSub167.tree)


                    else:
                        break #loop30





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathShift

    class mathAddSub_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathAddSub
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:310:1: mathAddSub : mathMultDiv ( ( '+' | '-' ) mathMultDiv )* ;
    def mathAddSub(self, ):

        retval = self.mathAddSub_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set169 = None
        mathMultDiv168 = None

        mathMultDiv170 = None


        set169_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:311:2: ( mathMultDiv ( ( '+' | '-' ) mathMultDiv )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:311:4: mathMultDiv ( ( '+' | '-' ) mathMultDiv )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathMultDiv_in_mathAddSub1454)
                mathMultDiv168 = self.mathMultDiv()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathMultDiv168.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:311:16: ( ( '+' | '-' ) mathMultDiv )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if ((114 <= LA31_0 <= 115)) :
                        alt31 = 1


                    if alt31 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:311:17: ( '+' | '-' ) mathMultDiv
                        set169 = self.input.LT(1)
                        if (114 <= self.input.LA(1) <= 115):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set169))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_mathAddSub1457
                                )
                            raise mse


                        self.following.append(self.FOLLOW_mathMultDiv_in_mathAddSub1463)
                        mathMultDiv170 = self.mathMultDiv()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathMultDiv170.tree)


                    else:
                        break #loop31





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathAddSub

    class mathMultDiv_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathMultDiv
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:314:1: mathMultDiv : mathUnary ( ( '*' | '/' ) mathUnary )* ;
    def mathMultDiv(self, ):

        retval = self.mathMultDiv_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set172 = None
        mathUnary171 = None

        mathUnary173 = None


        set172_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:315:2: ( mathUnary ( ( '*' | '/' ) mathUnary )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:315:4: mathUnary ( ( '*' | '/' ) mathUnary )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathUnary_in_mathMultDiv1476)
                mathUnary171 = self.mathUnary()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathUnary171.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:315:14: ( ( '*' | '/' ) mathUnary )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == 99 or LA32_0 == 116) :
                        alt32 = 1


                    if alt32 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:315:15: ( '*' | '/' ) mathUnary
                        set172 = self.input.LT(1)
                        if self.input.LA(1) == 99 or self.input.LA(1) == 116:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set172))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_mathMultDiv1479
                                )
                            raise mse


                        self.following.append(self.FOLLOW_mathUnary_in_mathMultDiv1485)
                        mathUnary173 = self.mathUnary()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, mathUnary173.tree)


                    else:
                        break #loop32





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathMultDiv

    class mathUnary_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathUnary
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:318:1: mathUnary : ( '-' )? mathBottom ;
    def mathUnary(self, ):

        retval = self.mathUnary_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal174 = None
        mathBottom175 = None


        char_literal174_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:319:2: ( ( '-' )? mathBottom )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:319:4: ( '-' )? mathBottom
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:319:4: ( '-' )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == 115) :
                    alt33 = 1
                if alt33 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:319:4: '-'
                    char_literal174 = self.input.LT(1)
                    self.match(self.input, 115, self.FOLLOW_115_in_mathUnary1498)
                    if self.failed:
                        return retval

                    char_literal174_tree = self.adaptor.createWithPayload(char_literal174)
                    self.adaptor.addChild(root_0, char_literal174_tree)




                self.following.append(self.FOLLOW_mathBottom_in_mathUnary1501)
                mathBottom175 = self.mathBottom()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathBottom175.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathUnary

    class mathBottom_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathBottom
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:322:1: mathBottom : ( '(' mathExpr ')' | mathVar );
    def mathBottom(self, ):

        retval = self.mathBottom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal176 = None
        char_literal178 = None
        mathExpr177 = None

        mathVar179 = None


        char_literal176_tree = None
        char_literal178_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:323:2: ( '(' mathExpr ')' | mathVar )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 69) :
                    alt34 = 1
                elif ((Integer <= LA34_0 <= Identifier) or LA34_0 == 56 or (64 <= LA34_0 <= 68) or LA34_0 == 72 or (80 <= LA34_0 <= 83) or LA34_0 == 85 or (103 <= LA34_0 <= 109)) :
                    alt34 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("322:1: mathBottom : ( '(' mathExpr ')' | mathVar );", 34, 0, self.input)

                    raise nvae

                if alt34 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:323:4: '(' mathExpr ')'
                    root_0 = self.adaptor.nil()

                    char_literal176 = self.input.LT(1)
                    self.match(self.input, 69, self.FOLLOW_69_in_mathBottom1512)
                    if self.failed:
                        return retval

                    char_literal176_tree = self.adaptor.createWithPayload(char_literal176)
                    self.adaptor.addChild(root_0, char_literal176_tree)

                    self.following.append(self.FOLLOW_mathExpr_in_mathBottom1514)
                    mathExpr177 = self.mathExpr()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathExpr177.tree)
                    char_literal178 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_mathBottom1516)
                    if self.failed:
                        return retval

                    char_literal178_tree = self.adaptor.createWithPayload(char_literal178)
                    self.adaptor.addChild(root_0, char_literal178_tree)



                elif alt34 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:324:4: mathVar
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_mathVar_in_mathBottom1521)
                    mathVar179 = self.mathVar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathVar179.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathBottom

    class mathVar_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathVar
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:327:1: mathVar : ( Integer | validId );
    def mathVar(self, ):

        retval = self.mathVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Integer180 = None
        validId181 = None


        Integer180_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:328:2: ( Integer | validId )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == Integer) :
                    alt35 = 1
                elif (LA35_0 == Identifier or LA35_0 == 56 or (64 <= LA35_0 <= 68) or LA35_0 == 72 or (80 <= LA35_0 <= 83) or LA35_0 == 85 or (103 <= LA35_0 <= 109)) :
                    alt35 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("327:1: mathVar : ( Integer | validId );", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:328:4: Integer
                    root_0 = self.adaptor.nil()

                    Integer180 = self.input.LT(1)
                    self.match(self.input, Integer, self.FOLLOW_Integer_in_mathVar1532)
                    if self.failed:
                        return retval

                    Integer180_tree = self.adaptor.createWithPayload(Integer180)
                    self.adaptor.addChild(root_0, Integer180_tree)



                elif alt35 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:329:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_mathVar1537)
                    validId181 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId181.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end mathVar

    class validIdList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start validIdList
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:332:1: validIdList : validId ( ',' validId )* ;
    def validIdList(self, ):

        retval = self.validIdList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal183 = None
        validId182 = None

        validId184 = None


        char_literal183_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:333:2: ( validId ( ',' validId )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:333:4: validId ( ',' validId )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_validId_in_validIdList1548)
                validId182 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, validId182.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:333:12: ( ',' validId )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 59) :
                        alt36 = 1


                    if alt36 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:333:13: ',' validId
                        char_literal183 = self.input.LT(1)
                        self.match(self.input, 59, self.FOLLOW_59_in_validIdList1551)
                        if self.failed:
                            return retval

                        char_literal183_tree = self.adaptor.createWithPayload(char_literal183)
                        self.adaptor.addChild(root_0, char_literal183_tree)

                        self.following.append(self.FOLLOW_validId_in_validIdList1553)
                        validId184 = self.validId()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, validId184.tree)


                    else:
                        break #loop36





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end validIdList

    class validId_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start validId
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:339:1: validId : ( Identifier | 'array' | 'astring' | 'const' | 'cstring' | 'domstring' | 'function' | 'iid_is' | 'interface' | 'noscript' | 'notxpcom' | 'nsid' | 'object' | 'optional' | 'ptr' | 'ref' | 'retval' | 'scriptable' | 'shared' | 'utf8string' );
    def validId(self, ):

        retval = self.validId_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set185 = None

        set185_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:340:2: ( Identifier | 'array' | 'astring' | 'const' | 'cstring' | 'domstring' | 'function' | 'iid_is' | 'interface' | 'noscript' | 'notxpcom' | 'nsid' | 'object' | 'optional' | 'ptr' | 'ref' | 'retval' | 'scriptable' | 'shared' | 'utf8string' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set185 = self.input.LT(1)
                if self.input.LA(1) == Identifier or self.input.LA(1) == 56 or (64 <= self.input.LA(1) <= 68) or self.input.LA(1) == 72 or (80 <= self.input.LA(1) <= 83) or self.input.LA(1) == 85 or (103 <= self.input.LA(1) <= 109):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set185))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_validId0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end validId

    class uuid_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start uuid
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:362:1: uuid : UUID ;
    def uuid(self, ):

        retval = self.uuid_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UUID186 = None

        UUID186_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:363:2: ( UUID )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:363:4: UUID
                root_0 = self.adaptor.nil()

                UUID186 = self.input.LT(1)
                self.match(self.input, UUID, self.FOLLOW_UUID_in_uuid1675)
                if self.failed:
                    return retval

                UUID186_tree = self.adaptor.createWithPayload(UUID186)
                self.adaptor.addChild(root_0, UUID186_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end uuid


    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\25\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\25\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\54\1\103\1\uffff\1\54\1\uffff\2\73\1\105\1\54\1\uffff\1\103"
        u"\2\54\2\73\1\105\1\106\1\54\1\73\1\106\1\73"
        )

    DFA9_max = DFA.unpack(
        u"\1\155\1\114\1\uffff\1\155\1\uffff\2\74\1\105\1\155\1\uffff\1\114"
        u"\2\155\2\74\1\105\1\106\1\155\1\74\1\106\1\74"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\1\1\uffff\1\3\4\uffff\1\2\13\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\25\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\4\13\uffff\1\4\1\uffff\1\1\5\uffff\5\4\3\uffff\1"
        u"\3\1\uffff\2\2\4\uffff\4\4\1\uffff\1\4\1\uffff\14\4\4\uffff\7\4"),
        DFA.unpack(u"\1\6\1\5\7\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10\13\uffff\1\10\7\uffff\5\10\3\uffff\1\10\7\uffff"
        u"\4\10\1\uffff\1\10\1\uffff\14\11\4\uffff\7\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\1\13"),
        DFA.unpack(u"\1\12\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u"\1\11\13\uffff\1\11\7\uffff\5\11\1\4\2\uffff\1\11\7"
        u"\uffff\4\11\1\uffff\1\11\21\uffff\7\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\1\15\7\uffff\1\17"),
        DFA.unpack(u"\1\4\13\uffff\1\4\7\uffff\5\4\3\uffff\1\4\1\uffff\2"
        u"\2\4\uffff\4\4\1\uffff\1\4\1\uffff\14\4\4\uffff\7\4"),
        DFA.unpack(u"\1\20\13\uffff\1\20\7\uffff\5\20\3\uffff\1\20\7\uffff"
        u"\4\20\1\uffff\1\20\21\uffff\7\20"),
        DFA.unpack(u"\1\12\1\13"),
        DFA.unpack(u"\1\12\1\13"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u"\1\23\13\uffff\1\23\7\uffff\5\23\3\uffff\1\23\7\uffff"
        u"\4\23\1\uffff\1\23\21\uffff\7\23"),
        DFA.unpack(u"\1\12\1\13"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\12\1\13")
    ]

    # class definition for DFA #9

    DFA9 = DFA
 

    FOLLOW_toplevel_in_idlFile178 = frozenset([39, 40, 41, 56, 58, 86, 110])
    FOLLOW_EOF_in_idlFile181 = frozenset([1])
    FOLLOW_interface_in_toplevel193 = frozenset([1])
    FOLLOW_typedef_in_toplevel198 = frozenset([1])
    FOLLOW_nativeTypeDecl_in_toplevel203 = frozenset([1])
    FOLLOW_include_in_toplevel208 = frozenset([1])
    FOLLOW_jerkyPreprocessorDirectives_in_toplevel213 = frozenset([1])
    FOLLOW_inline_in_toplevel218 = frozenset([1])
    FOLLOW_Include_in_include229 = frozenset([1])
    FOLLOW_JerkyPreprocessorLine_in_jerkyPreprocessorDirectives248 = frozenset([1])
    FOLLOW_InlineCHeader_in_inline259 = frozenset([1])
    FOLLOW_56_in_interface285 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_interface287 = frozenset([57])
    FOLLOW_57_in_interface289 = frozenset([1])
    FOLLOW_58_in_interface305 = frozenset([42, 64, 65, 66, 67, 68])
    FOLLOW_interfaceModifier_in_interface308 = frozenset([59])
    FOLLOW_59_in_interface310 = frozenset([42, 64, 65, 66, 67, 68])
    FOLLOW_UUID_in_interface314 = frozenset([60])
    FOLLOW_60_in_interface316 = frozenset([56])
    FOLLOW_56_in_interface320 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_interface322 = frozenset([61, 62])
    FOLLOW_61_in_interface325 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validIdList_in_interface327 = frozenset([62])
    FOLLOW_62_in_interface334 = frozenset([44, 56, 58, 63, 64, 65, 66, 67, 68, 72, 74, 75, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_interfaceBody_in_interface336 = frozenset([63])
    FOLLOW_63_in_interface338 = frozenset([57])
    FOLLOW_57_in_interface340 = frozenset([1])
    FOLLOW_interfaceModifier_in_interfaceModifierList410 = frozenset([1, 59])
    FOLLOW_59_in_interfaceModifierList413 = frozenset([64, 65, 66, 67, 68])
    FOLLOW_interfaceModifier_in_interfaceModifierList415 = frozenset([1, 59])
    FOLLOW_set_in_interfaceModifier0 = frozenset([1])
    FOLLOW_interfaceBodyItem_in_interfaceBody466 = frozenset([1, 44, 56, 58, 64, 65, 66, 67, 68, 72, 74, 75, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_attribute_in_interfaceBodyItem478 = frozenset([1])
    FOLLOW_const_in_interfaceBodyItem483 = frozenset([1])
    FOLLOW_method_in_interfaceBodyItem488 = frozenset([1])
    FOLLOW_methodModifiers_in_method499 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_type_in_method502 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_method506 = frozenset([69])
    FOLLOW_69_in_method508 = frozenset([58, 70, 77, 78, 79])
    FOLLOW_paramList_in_method510 = frozenset([70])
    FOLLOW_70_in_method513 = frozenset([57, 71])
    FOLLOW_71_in_method516 = frozenset([69])
    FOLLOW_69_in_method518 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_method522 = frozenset([59, 70])
    FOLLOW_59_in_method525 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_method529 = frozenset([59, 70])
    FOLLOW_70_in_method533 = frozenset([57])
    FOLLOW_57_in_method537 = frozenset([1])
    FOLLOW_72_in_const584 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_type_in_const586 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_const588 = frozenset([73])
    FOLLOW_73_in_const590 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathExpr_in_const592 = frozenset([57])
    FOLLOW_57_in_const594 = frozenset([1])
    FOLLOW_methodModifiers_in_attribute619 = frozenset([74, 75])
    FOLLOW_74_in_attribute622 = frozenset([75])
    FOLLOW_75_in_attribute625 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_type_in_attribute627 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_attribute629 = frozenset([57])
    FOLLOW_57_in_attribute631 = frozenset([1])
    FOLLOW_58_in_methodModifiers664 = frozenset([67, 68, 76])
    FOLLOW_methodModifier_in_methodModifiers666 = frozenset([59, 60])
    FOLLOW_59_in_methodModifiers669 = frozenset([67, 68, 76])
    FOLLOW_methodModifier_in_methodModifiers671 = frozenset([59, 60])
    FOLLOW_60_in_methodModifiers675 = frozenset([1])
    FOLLOW_68_in_methodModifier693 = frozenset([1])
    FOLLOW_67_in_methodModifier698 = frozenset([1])
    FOLLOW_binaryName_in_methodModifier703 = frozenset([1])
    FOLLOW_76_in_binaryName714 = frozenset([69])
    FOLLOW_69_in_binaryName716 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_binaryName718 = frozenset([70])
    FOLLOW_70_in_binaryName720 = frozenset([1])
    FOLLOW_paramDecl_in_paramList741 = frozenset([1, 59])
    FOLLOW_59_in_paramList744 = frozenset([58, 77, 78, 79])
    FOLLOW_paramDecl_in_paramList746 = frozenset([1, 59])
    FOLLOW_paramModifiersDecl_in_paramDecl766 = frozenset([77, 78, 79])
    FOLLOW_paramType_in_paramDecl769 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_type_in_paramDecl771 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_paramDecl773 = frozenset([1])
    FOLLOW_set_in_paramType0 = frozenset([1])
    FOLLOW_58_in_paramModifiersDecl826 = frozenset([72, 80, 81, 82, 83, 84, 85])
    FOLLOW_paramModifier_in_paramModifiersDecl828 = frozenset([59, 60])
    FOLLOW_59_in_paramModifiersDecl831 = frozenset([72, 80, 81, 82, 83, 84, 85])
    FOLLOW_paramModifier_in_paramModifiersDecl833 = frozenset([59, 60])
    FOLLOW_60_in_paramModifiersDecl837 = frozenset([1])
    FOLLOW_80_in_paramModifier855 = frozenset([1])
    FOLLOW_sizeIs_in_paramModifier860 = frozenset([1])
    FOLLOW_iidIs_in_paramModifier865 = frozenset([1])
    FOLLOW_81_in_paramModifier870 = frozenset([1])
    FOLLOW_72_in_paramModifier875 = frozenset([1])
    FOLLOW_82_in_paramModifier880 = frozenset([1])
    FOLLOW_83_in_paramModifier885 = frozenset([1])
    FOLLOW_84_in_sizeIs897 = frozenset([69])
    FOLLOW_69_in_sizeIs899 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_sizeIs901 = frozenset([70])
    FOLLOW_70_in_sizeIs903 = frozenset([1])
    FOLLOW_85_in_iidIs925 = frozenset([69])
    FOLLOW_69_in_iidIs927 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_iidIs929 = frozenset([70])
    FOLLOW_70_in_iidIs931 = frozenset([1])
    FOLLOW_nativeType_in_nativeTypeDecl952 = frozenset([57])
    FOLLOW_57_in_nativeTypeDecl954 = frozenset([1])
    FOLLOW_typeModifiersDecl_in_nativeType966 = frozenset([86])
    FOLLOW_86_in_nativeType969 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_nativeType973 = frozenset([69])
    FOLLOW_69_in_nativeType975 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_nativeTypePayload_in_nativeType977 = frozenset([44, 56, 64, 65, 66, 67, 68, 70, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_70_in_nativeType980 = frozenset([1])
    FOLLOW_87_in_nativeTypePayload1012 = frozenset([1])
    FOLLOW_88_in_nativeTypePayload1017 = frozenset([1])
    FOLLOW_89_in_nativeTypePayload1022 = frozenset([1])
    FOLLOW_90_in_nativeTypePayload1027 = frozenset([1])
    FOLLOW_91_in_nativeTypePayload1032 = frozenset([1])
    FOLLOW_92_in_nativeTypePayload1037 = frozenset([1])
    FOLLOW_93_in_nativeTypePayload1042 = frozenset([1])
    FOLLOW_94_in_nativeTypePayload1047 = frozenset([1])
    FOLLOW_95_in_nativeTypePayload1052 = frozenset([1])
    FOLLOW_96_in_nativeTypePayload1057 = frozenset([1])
    FOLLOW_97_in_nativeTypePayload1062 = frozenset([1])
    FOLLOW_98_in_nativeTypePayload1067 = frozenset([1])
    FOLLOW_99_in_nativeTypePayload1072 = frozenset([1])
    FOLLOW_100_in_nativeTypePayload1077 = frozenset([1])
    FOLLOW_101_in_nativeTypePayload1082 = frozenset([1])
    FOLLOW_102_in_nativeTypePayload1087 = frozenset([1])
    FOLLOW_validId_in_nativeTypePayload1092 = frozenset([1])
    FOLLOW_58_in_typeModifiersDecl1103 = frozenset([103, 104, 105, 106, 107, 108, 109])
    FOLLOW_typeModifier_in_typeModifiersDecl1105 = frozenset([59, 60])
    FOLLOW_59_in_typeModifiersDecl1108 = frozenset([103, 104, 105, 106, 107, 108, 109])
    FOLLOW_typeModifier_in_typeModifiersDecl1110 = frozenset([59, 60])
    FOLLOW_60_in_typeModifiersDecl1114 = frozenset([1])
    FOLLOW_set_in_typeModifier0 = frozenset([1])
    FOLLOW_110_in_typedef1173 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_type_in_typedef1175 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_typedef1177 = frozenset([57])
    FOLLOW_57_in_typedef1179 = frozenset([1])
    FOLLOW_87_in_type1202 = frozenset([1])
    FOLLOW_88_in_type1211 = frozenset([1])
    FOLLOW_89_in_type1220 = frozenset([1])
    FOLLOW_90_in_type1229 = frozenset([1])
    FOLLOW_91_in_type1238 = frozenset([1])
    FOLLOW_92_in_type1247 = frozenset([1])
    FOLLOW_93_in_type1256 = frozenset([1])
    FOLLOW_93_in_type1265 = frozenset([93])
    FOLLOW_93_in_type1267 = frozenset([1])
    FOLLOW_94_in_type1276 = frozenset([91])
    FOLLOW_91_in_type1278 = frozenset([1])
    FOLLOW_94_in_type1287 = frozenset([92])
    FOLLOW_92_in_type1289 = frozenset([1])
    FOLLOW_94_in_type1298 = frozenset([93])
    FOLLOW_93_in_type1300 = frozenset([1])
    FOLLOW_94_in_type1309 = frozenset([93])
    FOLLOW_93_in_type1311 = frozenset([93])
    FOLLOW_93_in_type1313 = frozenset([1])
    FOLLOW_95_in_type1322 = frozenset([1])
    FOLLOW_96_in_type1331 = frozenset([1])
    FOLLOW_97_in_type1340 = frozenset([1])
    FOLLOW_98_in_type1349 = frozenset([1])
    FOLLOW_validId_in_type1358 = frozenset([1])
    FOLLOW_mathBitOr_in_mathExpr1369 = frozenset([1])
    FOLLOW_mathBitXor_in_mathBitOr1381 = frozenset([1, 111])
    FOLLOW_111_in_mathBitOr1384 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathBitXor_in_mathBitOr1386 = frozenset([1, 111])
    FOLLOW_mathBitAnd_in_mathBitXor1400 = frozenset([1, 112])
    FOLLOW_112_in_mathBitXor1403 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathBitAnd_in_mathBitXor1405 = frozenset([1, 112])
    FOLLOW_mathShift_in_mathBitAnd1418 = frozenset([1, 100])
    FOLLOW_100_in_mathBitAnd1421 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathShift_in_mathBitAnd1423 = frozenset([1, 100])
    FOLLOW_mathAddSub_in_mathShift1436 = frozenset([1, 113])
    FOLLOW_113_in_mathShift1439 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathAddSub_in_mathShift1441 = frozenset([1, 113])
    FOLLOW_mathMultDiv_in_mathAddSub1454 = frozenset([1, 114, 115])
    FOLLOW_set_in_mathAddSub1457 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathMultDiv_in_mathAddSub1463 = frozenset([1, 114, 115])
    FOLLOW_mathUnary_in_mathMultDiv1476 = frozenset([1, 99, 116])
    FOLLOW_set_in_mathMultDiv1479 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathUnary_in_mathMultDiv1485 = frozenset([1, 99, 116])
    FOLLOW_115_in_mathUnary1498 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_mathBottom_in_mathUnary1501 = frozenset([1])
    FOLLOW_69_in_mathBottom1512 = frozenset([43, 44, 56, 64, 65, 66, 67, 68, 69, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109, 115])
    FOLLOW_mathExpr_in_mathBottom1514 = frozenset([70])
    FOLLOW_70_in_mathBottom1516 = frozenset([1])
    FOLLOW_mathVar_in_mathBottom1521 = frozenset([1])
    FOLLOW_Integer_in_mathVar1532 = frozenset([1])
    FOLLOW_validId_in_mathVar1537 = frozenset([1])
    FOLLOW_validId_in_validIdList1548 = frozenset([1, 59])
    FOLLOW_59_in_validIdList1551 = frozenset([44, 56, 64, 65, 66, 67, 68, 72, 80, 81, 82, 83, 85, 103, 104, 105, 106, 107, 108, 109])
    FOLLOW_validId_in_validIdList1553 = frozenset([1, 59])
    FOLLOW_set_in_validId0 = frozenset([1])
    FOLLOW_UUID_in_uuid1675 = frozenset([1])

