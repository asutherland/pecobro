# $ANTLR 3.0.1 /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g 2008-05-19 22:12:29

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FORWARD=7
UUIDPayload=46
LONG_LONG=24
UUID=36
InlineCHeader=35
CONST=6
CHAR=30
LineComment=48
PARAM=15
FLOAT=28
EOF=-1
WCHAR=31
Identifier=38
BlockComment=47
MODIFIERS=13
BOOLEAN=20
HexChar=41
UNSIGNED_LONG=26
INCLUDE=8
UNSIGNED_SHORT=25
DOUBLE=29
HexInteger=40
WhiteSpace=45
VOID=19
BODY=5
WSTRING=33
UNSIGNED_LONG_LONG=27
IdentifierPart=44
ATTR=4
PARAMS=16
I_UUID=11
DecimalChar=42
TYPEDEF=18
DecimalInteger=39
IdentifierStart=43
NATIVE=14
SHORT=22
Include=34
PARENTS=17
INTERFACE=10
INLINE=9
LONG=23
METHOD=12
Integer=37
OCTET=21
STRING=32

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ATTR", "BODY", "CONST", "FORWARD", "INCLUDE", "INLINE", "INTERFACE", 
    "I_UUID", "METHOD", "MODIFIERS", "NATIVE", "PARAM", "PARAMS", "PARENTS", 
    "TYPEDEF", "VOID", "BOOLEAN", "OCTET", "SHORT", "LONG", "LONG_LONG", 
    "UNSIGNED_SHORT", "UNSIGNED_LONG", "UNSIGNED_LONG_LONG", "FLOAT", "DOUBLE", 
    "CHAR", "WCHAR", "STRING", "WSTRING", "Include", "InlineCHeader", "UUID", 
    "Integer", "Identifier", "DecimalInteger", "HexInteger", "HexChar", 
    "DecimalChar", "IdentifierStart", "IdentifierPart", "WhiteSpace", "UUIDPayload", 
    "BlockComment", "LineComment", "'interface'", "';'", "'['", "','", "']'", 
    "':'", "'{'", "'}'", "'scriptable'", "'function'", "'object'", "'notxpcom'", 
    "'noscript'", "'('", "')'", "'const'", "'='", "'short'", "'long'", "'attribute'", 
    "'in'", "'out'", "'inout'", "'array'", "'retval'", "'shared'", "'size_is'", 
    "'native'", "'ref'", "'ptr'", "'nsid'", "'domstring'", "'utf8string'", 
    "'cstring'", "'astring'", "'typedef'", "'boolean'", "'void'", "'string'", 
    "'octet'", "'unsigned'", "'float'", "'double'", "'char'", "'wchar'", 
    "'wstring'", "'*'", "'/'", "'+'", "'-'", "'<<'"
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:84:1: idlFile : ( toplevel )* EOF ;
    def idlFile(self, ):

        retval = self.idlFile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        toplevel1 = None


        EOF2_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:85:2: ( ( toplevel )* EOF )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:85:4: ( toplevel )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:85:4: ( toplevel )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((Include <= LA1_0 <= InlineCHeader) or LA1_0 == 49 or LA1_0 == 51 or LA1_0 == 84) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:85:4: toplevel
                        self.following.append(self.FOLLOW_toplevel_in_idlFile158)
                        toplevel1 = self.toplevel()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, toplevel1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_idlFile161)
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:88:1: toplevel : ( interface | typedef | nativeTypeDecl | include | inline );
    def toplevel(self, ):

        retval = self.toplevel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        interface3 = None

        typedef4 = None

        nativeTypeDecl5 = None

        include6 = None

        inline7 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:89:2: ( interface | typedef | nativeTypeDecl | include | inline )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 == 49:
                    alt2 = 1
                elif LA2 == 51:
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == UUID or (57 <= LA2_2 <= 61)) :
                        alt2 = 1
                    elif ((77 <= LA2_2 <= 83)) :
                        alt2 = 3
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("88:1: toplevel : ( interface | typedef | nativeTypeDecl | include | inline );", 2, 2, self.input)

                        raise nvae

                elif LA2 == 84:
                    alt2 = 2
                elif LA2 == Include:
                    alt2 = 4
                elif LA2 == InlineCHeader:
                    alt2 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("88:1: toplevel : ( interface | typedef | nativeTypeDecl | include | inline );", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:89:4: interface
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_interface_in_toplevel173)
                    interface3 = self.interface()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, interface3.tree)


                elif alt2 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: typedef
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_typedef_in_toplevel178)
                    typedef4 = self.typedef()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, typedef4.tree)


                elif alt2 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:91:4: nativeTypeDecl
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_nativeTypeDecl_in_toplevel183)
                    nativeTypeDecl5 = self.nativeTypeDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, nativeTypeDecl5.tree)


                elif alt2 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:92:4: include
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_include_in_toplevel188)
                    include6 = self.include()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, include6.tree)


                elif alt2 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:93:4: inline
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_inline_in_toplevel193)
                    inline7 = self.inline()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, inline7.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:96:1: include : Include -> ^( INCLUDE Include ) ;
    def include(self, ):

        retval = self.include_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Include8 = None

        Include8_tree = None
        stream_Include = RewriteRuleTokenStream(self.adaptor, "token Include")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:97:2: ( Include -> ^( INCLUDE Include ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:97:4: Include
                Include8 = self.input.LT(1)
                self.match(self.input, Include, self.FOLLOW_Include_in_include204)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_Include.add(Include8)
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
                    # 97:12: -> ^( INCLUDE Include )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:97:15: ^( INCLUDE Include )
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

    class inline_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start inline
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:100:1: inline : InlineCHeader -> ^( INLINE InlineCHeader ) ;
    def inline(self, ):

        retval = self.inline_return()
        retval.start = self.input.LT(1)

        root_0 = None

        InlineCHeader9 = None

        InlineCHeader9_tree = None
        stream_InlineCHeader = RewriteRuleTokenStream(self.adaptor, "token InlineCHeader")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:101:2: ( InlineCHeader -> ^( INLINE InlineCHeader ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:101:4: InlineCHeader
                InlineCHeader9 = self.input.LT(1)
                self.match(self.input, InlineCHeader, self.FOLLOW_InlineCHeader_in_inline223)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_InlineCHeader.add(InlineCHeader9)
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
                    # 101:18: -> ^( INLINE InlineCHeader )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:101:21: ^( INLINE InlineCHeader )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:104:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );
    def interface(self, ):

        retval = self.interface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal10 = None
        char_literal12 = None
        char_literal13 = None
        char_literal15 = None
        UUID16 = None
        char_literal17 = None
        string_literal18 = None
        char_literal20 = None
        char_literal22 = None
        char_literal24 = None
        char_literal25 = None
        validId11 = None

        interfaceModifier14 = None

        validId19 = None

        validIdList21 = None

        interfaceBody23 = None


        string_literal10_tree = None
        char_literal12_tree = None
        char_literal13_tree = None
        char_literal15_tree = None
        UUID16_tree = None
        char_literal17_tree = None
        string_literal18_tree = None
        char_literal20_tree = None
        char_literal22_tree = None
        char_literal24_tree = None
        char_literal25_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_56 = RewriteRuleTokenStream(self.adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self.adaptor, "token 55")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_UUID = RewriteRuleTokenStream(self.adaptor, "token UUID")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")
        stream_54 = RewriteRuleTokenStream(self.adaptor, "token 54")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_interfaceBody = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceBody")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_interfaceModifier = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceModifier")
        stream_validIdList = RewriteRuleSubtreeStream(self.adaptor, "rule validIdList")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:2: ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 49) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == Identifier) :
                        LA6_3 = self.input.LA(3)

                        if ((54 <= LA6_3 <= 55)) :
                            alt6 = 2
                        elif (LA6_3 == 50) :
                            alt6 = 1
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("104:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 3, self.input)

                            raise nvae

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("104:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 1, self.input)

                        raise nvae

                elif (LA6_0 == 51) :
                    alt6 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("104:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:4: 'interface' validId ';'
                    string_literal10 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_interface249)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_49.add(string_literal10)
                    self.following.append(self.FOLLOW_validId_in_interface251)
                    validId11 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId11.tree)
                    char_literal12 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_interface253)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_50.add(char_literal12)
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
                        # 107:3: -> ^( FORWARD validId )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:107:6: ^( FORWARD validId )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FORWARD, "FORWARD"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt6 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:4: ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';'
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:4: ( '[' ( interfaceModifier ',' )* UUID ']' )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 51) :
                        alt4 = 1
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:5: '[' ( interfaceModifier ',' )* UUID ']'
                        char_literal13 = self.input.LT(1)
                        self.match(self.input, 51, self.FOLLOW_51_in_interface269)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_51.add(char_literal13)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:9: ( interfaceModifier ',' )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if ((57 <= LA3_0 <= 61)) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:10: interfaceModifier ','
                                self.following.append(self.FOLLOW_interfaceModifier_in_interface272)
                                interfaceModifier14 = self.interfaceModifier()
                                self.following.pop()
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_interfaceModifier.add(interfaceModifier14.tree)
                                char_literal15 = self.input.LT(1)
                                self.match(self.input, 52, self.FOLLOW_52_in_interface274)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_52.add(char_literal15)


                            else:
                                break #loop3


                        UUID16 = self.input.LT(1)
                        self.match(self.input, UUID, self.FOLLOW_UUID_in_interface278)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_UUID.add(UUID16)
                        char_literal17 = self.input.LT(1)
                        self.match(self.input, 53, self.FOLLOW_53_in_interface280)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_53.add(char_literal17)



                    string_literal18 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_interface284)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_49.add(string_literal18)
                    self.following.append(self.FOLLOW_validId_in_interface286)
                    validId19 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId19.tree)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:65: ( ':' validIdList )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 54) :
                        alt5 = 1
                    if alt5 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:108:66: ':' validIdList
                        char_literal20 = self.input.LT(1)
                        self.match(self.input, 54, self.FOLLOW_54_in_interface289)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_54.add(char_literal20)
                        self.following.append(self.FOLLOW_validIdList_in_interface291)
                        validIdList21 = self.validIdList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_validIdList.add(validIdList21.tree)



                    char_literal22 = self.input.LT(1)
                    self.match(self.input, 55, self.FOLLOW_55_in_interface298)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_55.add(char_literal22)
                    self.following.append(self.FOLLOW_interfaceBody_in_interface300)
                    interfaceBody23 = self.interfaceBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_interfaceBody.add(interfaceBody23.tree)
                    char_literal24 = self.input.LT(1)
                    self.match(self.input, 56, self.FOLLOW_56_in_interface302)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_56.add(char_literal24)
                    char_literal25 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_interface304)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_50.add(char_literal25)
                    # AST Rewrite
                    # elements: validIdList, validId, UUID, interfaceModifier, interfaceBody
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
                        # 110:3: -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:6: ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INTERFACE, "INTERFACE"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:26: ^( I_UUID ( UUID )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(I_UUID, "I_UUID"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:35: ( UUID )?
                        if stream_UUID.hasNext():
                            self.adaptor.addChild(root_2, stream_UUID.next())


                        stream_UUID.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:42: ^( PARENTS ( validIdList )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARENTS, "PARENTS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:52: ( validIdList )?
                        if stream_validIdList.hasNext():
                            self.adaptor.addChild(root_2, stream_validIdList.next())


                        stream_validIdList.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:12: ^( MODIFIERS ( interfaceModifier )* )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:24: ( interfaceModifier )*
                        while stream_interfaceModifier.hasNext():
                            self.adaptor.addChild(root_2, stream_interfaceModifier.next())


                        stream_interfaceModifier.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:112:12: ^( BODY interfaceBody )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:115:1: interfaceModifierList : interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* ;
    def interfaceModifierList(self, ):

        retval = self.interfaceModifierList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal27 = None
        interfaceModifier26 = None

        interfaceModifier28 = None


        char_literal27_tree = None
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_interfaceModifier = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:2: ( interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:4: interfaceModifier ( ',' interfaceModifier )*
                self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList374)
                interfaceModifier26 = self.interfaceModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_interfaceModifier.add(interfaceModifier26.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:22: ( ',' interfaceModifier )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 52) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:23: ',' interfaceModifier
                        char_literal27 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_interfaceModifierList377)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal27)
                        self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList379)
                        interfaceModifier28 = self.interfaceModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_interfaceModifier.add(interfaceModifier28.tree)


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
                    # 117:3: -> ( interfaceModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:117:6: ( interfaceModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:1: interfaceModifier : ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' );
    def interfaceModifier(self, ):

        retval = self.interfaceModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set29 = None

        set29_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:2: ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set29 = self.input.LT(1)
                if (57 <= self.input.LA(1) <= 61):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set29))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:128:1: interfaceBody : ( interfaceBodyItem )* ;
    def interfaceBody(self, ):

        retval = self.interfaceBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        interfaceBodyItem30 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:129:2: ( ( interfaceBodyItem )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:129:4: ( interfaceBodyItem )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:129:4: ( interfaceBodyItem )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == Identifier or LA8_0 == 51 or LA8_0 == 64 or (66 <= LA8_0 <= 68) or (85 <= LA8_0 <= 94)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:129:4: interfaceBodyItem
                        self.following.append(self.FOLLOW_interfaceBodyItem_in_interfaceBody430)
                        interfaceBodyItem30 = self.interfaceBodyItem()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, interfaceBodyItem30.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:132:1: interfaceBodyItem : ( attribute | const | method );
    def interfaceBodyItem(self, ):

        retval = self.interfaceBodyItem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        attribute31 = None

        const32 = None

        method33 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:133:2: ( attribute | const | method )
                alt9 = 3
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:133:4: attribute
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_attribute_in_interfaceBodyItem442)
                    attribute31 = self.attribute()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, attribute31.tree)


                elif alt9 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:134:4: const
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_const_in_interfaceBodyItem447)
                    const32 = self.const()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, const32.tree)


                elif alt9 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:135:4: method
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_method_in_interfaceBodyItem452)
                    method33 = self.method()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, method33.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:138:1: method : ( methodModifiers )? type validId '(' paramList ')' ';' -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) ) ;
    def method(self, ):

        retval = self.method_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal37 = None
        char_literal39 = None
        char_literal40 = None
        methodModifiers34 = None

        type35 = None

        validId36 = None

        paramList38 = None


        char_literal37_tree = None
        char_literal39_tree = None
        char_literal40_tree = None
        stream_62 = RewriteRuleTokenStream(self.adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_paramList = RewriteRuleSubtreeStream(self.adaptor, "rule paramList")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:2: ( ( methodModifiers )? type validId '(' paramList ')' ';' -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: ( methodModifiers )? type validId '(' paramList ')' ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: ( methodModifiers )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 51) :
                    alt10 = 1
                if alt10 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:139:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_method463)
                    methodModifiers34 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers34.tree)



                self.following.append(self.FOLLOW_type_in_method466)
                type35 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type35.tree)
                self.following.append(self.FOLLOW_validId_in_method468)
                validId36 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId36.tree)
                char_literal37 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_method470)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_62.add(char_literal37)
                self.following.append(self.FOLLOW_paramList_in_method472)
                paramList38 = self.paramList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramList.add(paramList38.tree)
                char_literal39 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_method474)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal39)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_method476)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal40)
                # AST Rewrite
                # elements: methodModifiers, validId, type, paramList
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
                    # 140:3: -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:140:6: ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(METHOD, "METHOD"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:140:28: ^( MODIFIERS ( methodModifiers )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:140:40: ( methodModifiers )?
                    if stream_methodModifiers.hasNext():
                        self.adaptor.addChild(root_2, stream_methodModifiers.next())


                    stream_methodModifiers.reset();

                    self.adaptor.addChild(root_1, root_2)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:140:58: ^( PARAMS paramList )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARAMS, "PARAMS"), root_2)

                    self.adaptor.addChild(root_2, stream_paramList.next())

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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:143:1: const : 'const' constType validId '=' mathExpr ';' -> ^( CONST constType validId mathExpr ) ;
    def const(self, ):

        retval = self.const_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal41 = None
        char_literal44 = None
        char_literal46 = None
        constType42 = None

        validId43 = None

        mathExpr45 = None


        string_literal41_tree = None
        char_literal44_tree = None
        char_literal46_tree = None
        stream_64 = RewriteRuleTokenStream(self.adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_constType = RewriteRuleSubtreeStream(self.adaptor, "rule constType")
        stream_mathExpr = RewriteRuleSubtreeStream(self.adaptor, "rule mathExpr")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:144:2: ( 'const' constType validId '=' mathExpr ';' -> ^( CONST constType validId mathExpr ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:144:4: 'const' constType validId '=' mathExpr ';'
                string_literal41 = self.input.LT(1)
                self.match(self.input, 64, self.FOLLOW_64_in_const512)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_64.add(string_literal41)
                self.following.append(self.FOLLOW_constType_in_const514)
                constType42 = self.constType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_constType.add(constType42.tree)
                self.following.append(self.FOLLOW_validId_in_const516)
                validId43 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId43.tree)
                char_literal44 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_const518)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal44)
                self.following.append(self.FOLLOW_mathExpr_in_const520)
                mathExpr45 = self.mathExpr()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_mathExpr.add(mathExpr45.tree)
                char_literal46 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_const522)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal46)
                # AST Rewrite
                # elements: constType, mathExpr, validId
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
                    # 145:3: -> ^( CONST constType validId mathExpr )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:145:6: ^( CONST constType validId mathExpr )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CONST, "CONST"), root_1)

                    self.adaptor.addChild(root_1, stream_constType.next())
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

    class constType_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start constType
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:148:1: constType : ( 'short' -> SHORT | 'long' -> LONG | validId );
    def constType(self, ):

        retval = self.constType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal47 = None
        string_literal48 = None
        validId49 = None


        string_literal47_tree = None
        string_literal48_tree = None
        stream_67 = RewriteRuleTokenStream(self.adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self.adaptor, "token 66")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:2: ( 'short' -> SHORT | 'long' -> LONG | validId )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == 66:
                    alt11 = 1
                elif LA11 == 67:
                    alt11 = 2
                elif LA11 == Identifier:
                    alt11 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("148:1: constType : ( 'short' -> SHORT | 'long' -> LONG | validId );", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:149:4: 'short'
                    string_literal47 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_constType547)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_66.add(string_literal47)
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
                        # 149:12: -> SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(SHORT, "SHORT"))





                elif alt11 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:4: 'long'
                    string_literal48 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_constType556)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal48)
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
                        # 150:11: -> LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG, "LONG"))





                elif alt11 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:151:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_constType565)
                    validId49 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId49.tree)


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

    # $ANTLR end constType

    class attribute_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start attribute
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:154:1: attribute : ( methodModifiers )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) ) ;
    def attribute(self, ):

        retval = self.attribute_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal51 = None
        char_literal54 = None
        methodModifiers50 = None

        type52 = None

        validId53 = None


        string_literal51_tree = None
        char_literal54_tree = None
        stream_68 = RewriteRuleTokenStream(self.adaptor, "token 68")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:2: ( ( methodModifiers )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:4: ( methodModifiers )? 'attribute' type validId ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:4: ( methodModifiers )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 51) :
                    alt12 = 1
                if alt12 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_attribute576)
                    methodModifiers50 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers50.tree)



                string_literal51 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_attribute579)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_68.add(string_literal51)
                self.following.append(self.FOLLOW_type_in_attribute581)
                type52 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type52.tree)
                self.following.append(self.FOLLOW_validId_in_attribute583)
                validId53 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId53.tree)
                char_literal54 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_attribute585)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal54)
                # AST Rewrite
                # elements: methodModifiers, validId, type
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
                    # 156:3: -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:156:6: ^( ATTR type validId ^( MODIFIERS methodModifiers ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ATTR, "ATTR"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:156:26: ^( MODIFIERS methodModifiers )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    self.adaptor.addChild(root_2, stream_methodModifiers.next())

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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:159:1: methodModifiers : '[' methodModifier ( ',' methodModifier )+ ']' -> ( methodModifier )* ;
    def methodModifiers(self, ):

        retval = self.methodModifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal55 = None
        char_literal57 = None
        char_literal59 = None
        methodModifier56 = None

        methodModifier58 = None


        char_literal55_tree = None
        char_literal57_tree = None
        char_literal59_tree = None
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")
        stream_methodModifier = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:2: ( '[' methodModifier ( ',' methodModifier )+ ']' -> ( methodModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:4: '[' methodModifier ( ',' methodModifier )+ ']'
                char_literal55 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_methodModifiers614)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal55)
                self.following.append(self.FOLLOW_methodModifier_in_methodModifiers616)
                methodModifier56 = self.methodModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_methodModifier.add(methodModifier56.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:23: ( ',' methodModifier )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 52) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:24: ',' methodModifier
                        char_literal57 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_methodModifiers619)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal57)
                        self.following.append(self.FOLLOW_methodModifier_in_methodModifiers621)
                        methodModifier58 = self.methodModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_methodModifier.add(methodModifier58.tree)


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                char_literal59 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_methodModifiers625)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_53.add(char_literal59)
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
                    # 161:3: -> ( methodModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:161:6: ( methodModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:1: methodModifier : ( 'noscript' | 'notxpcom' );
    def methodModifier(self, ):

        retval = self.methodModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set60 = None

        set60_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:2: ( 'noscript' | 'notxpcom' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set60 = self.input.LT(1)
                if (60 <= self.input.LA(1) <= 61):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set60))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_methodModifier0
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

    # $ANTLR end methodModifier

    class paramList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start paramList
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:169:1: paramList : paramDecl ( ',' paramDecl )+ -> ( paramDecl )* ;
    def paramList(self, ):

        retval = self.paramList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal62 = None
        paramDecl61 = None

        paramDecl63 = None


        char_literal62_tree = None
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_paramDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramDecl")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:2: ( paramDecl ( ',' paramDecl )+ -> ( paramDecl )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:4: paramDecl ( ',' paramDecl )+
                self.following.append(self.FOLLOW_paramDecl_in_paramList659)
                paramDecl61 = self.paramDecl()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramDecl.add(paramDecl61.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:14: ( ',' paramDecl )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 52) :
                        alt14 = 1


                    if alt14 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:170:15: ',' paramDecl
                        char_literal62 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_paramList662)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal62)
                        self.following.append(self.FOLLOW_paramDecl_in_paramList664)
                        paramDecl63 = self.paramDecl()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramDecl.add(paramDecl63.tree)


                    else:
                        if cnt14 >= 1:
                            break #loop14

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1


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
                    # 171:3: -> ( paramDecl )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:171:6: ( paramDecl )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:174:1: paramDecl : ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) ;
    def paramDecl(self, ):

        retval = self.paramDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        paramModifiersDecl64 = None

        paramType65 = None

        type66 = None

        validId67 = None


        stream_paramModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        stream_paramType = RewriteRuleSubtreeStream(self.adaptor, "rule paramType")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:175:2: ( ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:175:4: ( paramModifiersDecl )? paramType type validId
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:175:4: ( paramModifiersDecl )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 51) :
                    alt15 = 1
                if alt15 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:175:4: paramModifiersDecl
                    self.following.append(self.FOLLOW_paramModifiersDecl_in_paramDecl684)
                    paramModifiersDecl64 = self.paramModifiersDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_paramModifiersDecl.add(paramModifiersDecl64.tree)



                self.following.append(self.FOLLOW_paramType_in_paramDecl687)
                paramType65 = self.paramType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramType.add(paramType65.tree)
                self.following.append(self.FOLLOW_type_in_paramDecl689)
                type66 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type66.tree)
                self.following.append(self.FOLLOW_validId_in_paramDecl691)
                validId67 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId67.tree)
                # AST Rewrite
                # elements: paramType, validId, paramModifiersDecl, type
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
                    # 176:3: -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:176:6: ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARAM, "PARAM"), root_1)

                    self.adaptor.addChild(root_1, stream_paramType.next())
                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:176:37: ^( MODIFIERS ( paramModifiersDecl )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:176:49: ( paramModifiersDecl )?
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:179:1: paramType : ( 'in' | 'out' | 'inout' );
    def paramType(self, ):

        retval = self.paramType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set68 = None

        set68_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:180:2: ( 'in' | 'out' | 'inout' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set68 = self.input.LT(1)
                if (69 <= self.input.LA(1) <= 71):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set68))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:185:1: paramModifiersDecl : '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* ;
    def paramModifiersDecl(self, ):

        retval = self.paramModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal69 = None
        char_literal71 = None
        char_literal73 = None
        paramModifier70 = None

        paramModifier72 = None


        char_literal69_tree = None
        char_literal71_tree = None
        char_literal73_tree = None
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")
        stream_paramModifier = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:2: ( '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:4: '[' paramModifier ( ',' paramModifier )* ']'
                char_literal69 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_paramModifiersDecl744)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal69)
                self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl746)
                paramModifier70 = self.paramModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramModifier.add(paramModifier70.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:22: ( ',' paramModifier )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 52) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:23: ',' paramModifier
                        char_literal71 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_paramModifiersDecl749)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal71)
                        self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl751)
                        paramModifier72 = self.paramModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramModifier.add(paramModifier72.tree)


                    else:
                        break #loop16


                char_literal73 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_paramModifiersDecl755)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_53.add(char_literal73)
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
                    # 187:3: -> ( paramModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:187:6: ( paramModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:191:1: paramModifier : ( 'array' | sizeIs | 'retval' | 'const' | 'shared' );
    def paramModifier(self, ):

        retval = self.paramModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal74 = None
        string_literal76 = None
        string_literal77 = None
        string_literal78 = None
        sizeIs75 = None


        string_literal74_tree = None
        string_literal76_tree = None
        string_literal77_tree = None
        string_literal78_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:192:2: ( 'array' | sizeIs | 'retval' | 'const' | 'shared' )
                alt17 = 5
                LA17 = self.input.LA(1)
                if LA17 == 72:
                    alt17 = 1
                elif LA17 == 75:
                    alt17 = 2
                elif LA17 == 73:
                    alt17 = 3
                elif LA17 == 64:
                    alt17 = 4
                elif LA17 == 74:
                    alt17 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("191:1: paramModifier : ( 'array' | sizeIs | 'retval' | 'const' | 'shared' );", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:192:4: 'array'
                    root_0 = self.adaptor.nil()

                    string_literal74 = self.input.LT(1)
                    self.match(self.input, 72, self.FOLLOW_72_in_paramModifier774)
                    if self.failed:
                        return retval

                    string_literal74_tree = self.adaptor.createWithPayload(string_literal74)
                    self.adaptor.addChild(root_0, string_literal74_tree)



                elif alt17 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:193:4: sizeIs
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_sizeIs_in_paramModifier779)
                    sizeIs75 = self.sizeIs()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, sizeIs75.tree)


                elif alt17 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:194:4: 'retval'
                    root_0 = self.adaptor.nil()

                    string_literal76 = self.input.LT(1)
                    self.match(self.input, 73, self.FOLLOW_73_in_paramModifier784)
                    if self.failed:
                        return retval

                    string_literal76_tree = self.adaptor.createWithPayload(string_literal76)
                    self.adaptor.addChild(root_0, string_literal76_tree)



                elif alt17 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:195:4: 'const'
                    root_0 = self.adaptor.nil()

                    string_literal77 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_paramModifier789)
                    if self.failed:
                        return retval

                    string_literal77_tree = self.adaptor.createWithPayload(string_literal77)
                    self.adaptor.addChild(root_0, string_literal77_tree)



                elif alt17 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:196:4: 'shared'
                    root_0 = self.adaptor.nil()

                    string_literal78 = self.input.LT(1)
                    self.match(self.input, 74, self.FOLLOW_74_in_paramModifier794)
                    if self.failed:
                        return retval

                    string_literal78_tree = self.adaptor.createWithPayload(string_literal78)
                    self.adaptor.addChild(root_0, string_literal78_tree)



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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:199:1: sizeIs : 'size_is' '(' validId ')' ;
    def sizeIs(self, ):

        retval = self.sizeIs_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal79 = None
        char_literal80 = None
        char_literal82 = None
        validId81 = None


        string_literal79_tree = None
        char_literal80_tree = None
        char_literal82_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:200:2: ( 'size_is' '(' validId ')' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:200:4: 'size_is' '(' validId ')'
                root_0 = self.adaptor.nil()

                string_literal79 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_sizeIs806)
                if self.failed:
                    return retval

                string_literal79_tree = self.adaptor.createWithPayload(string_literal79)
                self.adaptor.addChild(root_0, string_literal79_tree)

                char_literal80 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_sizeIs808)
                if self.failed:
                    return retval

                char_literal80_tree = self.adaptor.createWithPayload(char_literal80)
                self.adaptor.addChild(root_0, char_literal80_tree)

                self.following.append(self.FOLLOW_validId_in_sizeIs810)
                validId81 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, validId81.tree)
                char_literal82 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_sizeIs812)
                if self.failed:
                    return retval

                char_literal82_tree = self.adaptor.createWithPayload(char_literal82)
                self.adaptor.addChild(root_0, char_literal82_tree)




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

    class nativeTypeDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start nativeTypeDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:203:1: nativeTypeDecl : nativeType ';' ;
    def nativeTypeDecl(self, ):

        retval = self.nativeTypeDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal84 = None
        nativeType83 = None


        char_literal84_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:204:2: ( nativeType ';' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:204:4: nativeType ';'
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_nativeType_in_nativeTypeDecl824)
                nativeType83 = self.nativeType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, nativeType83.tree)
                char_literal84 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_nativeTypeDecl826)
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:1: nativeType : typeModifiersDecl 'native' validId -> ^( NATIVE validId typeModifiersDecl ) ;
    def nativeType(self, ):

        retval = self.nativeType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal86 = None
        typeModifiersDecl85 = None

        validId87 = None


        string_literal86_tree = None
        stream_76 = RewriteRuleTokenStream(self.adaptor, "token 76")
        stream_typeModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:208:2: ( typeModifiersDecl 'native' validId -> ^( NATIVE validId typeModifiersDecl ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:208:4: typeModifiersDecl 'native' validId
                self.following.append(self.FOLLOW_typeModifiersDecl_in_nativeType838)
                typeModifiersDecl85 = self.typeModifiersDecl()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_typeModifiersDecl.add(typeModifiersDecl85.tree)
                string_literal86 = self.input.LT(1)
                self.match(self.input, 76, self.FOLLOW_76_in_nativeType840)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_76.add(string_literal86)
                self.following.append(self.FOLLOW_validId_in_nativeType842)
                validId87 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId87.tree)
                # AST Rewrite
                # elements: validId, typeModifiersDecl
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
                    # 209:3: -> ^( NATIVE validId typeModifiersDecl )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:209:6: ^( NATIVE validId typeModifiersDecl )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NATIVE, "NATIVE"), root_1)

                    self.adaptor.addChild(root_1, stream_validId.next())
                    self.adaptor.addChild(root_1, stream_typeModifiersDecl.next())

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

    class typeModifiersDecl_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start typeModifiersDecl
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:212:1: typeModifiersDecl : '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ ;
    def typeModifiersDecl(self, ):

        retval = self.typeModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal88 = None
        char_literal90 = None
        char_literal92 = None
        typeModifier89 = None

        typeModifier91 = None


        char_literal88_tree = None
        char_literal90_tree = None
        char_literal92_tree = None
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")
        stream_typeModifier = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:213:2: ( '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:213:4: '[' typeModifier ( ',' typeModifier )* ']'
                char_literal88 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_typeModifiersDecl865)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal88)
                self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl867)
                typeModifier89 = self.typeModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_typeModifier.add(typeModifier89.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:213:21: ( ',' typeModifier )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 52) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:213:22: ',' typeModifier
                        char_literal90 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_typeModifiersDecl870)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal90)
                        self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl872)
                        typeModifier91 = self.typeModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_typeModifier.add(typeModifier91.tree)


                    else:
                        break #loop18


                char_literal92 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_typeModifiersDecl876)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_53.add(char_literal92)
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
                    # 214:3: -> ( typeModifier )+
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:214:6: ( typeModifier )+
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:217:1: typeModifier : ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' );
    def typeModifier(self, ):

        retval = self.typeModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set93 = None

        set93_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:218:2: ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set93 = self.input.LT(1)
                if (77 <= self.input.LA(1) <= 83):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set93))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:1: typedef : 'typedef' type validId ';' -> ^( TYPEDEF type validId ) ;
    def typedef(self, ):

        retval = self.typedef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal94 = None
        char_literal97 = None
        type95 = None

        validId96 = None


        string_literal94_tree = None
        char_literal97_tree = None
        stream_84 = RewriteRuleTokenStream(self.adaptor, "token 84")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:228:2: ( 'typedef' type validId ';' -> ^( TYPEDEF type validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:228:4: 'typedef' type validId ';'
                string_literal94 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_typedef935)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_84.add(string_literal94)
                self.following.append(self.FOLLOW_type_in_typedef937)
                type95 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type95.tree)
                self.following.append(self.FOLLOW_validId_in_typedef939)
                validId96 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId96.tree)
                char_literal97 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_typedef941)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal97)
                # AST Rewrite
                # elements: type, validId
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
                    # 229:3: -> ^( TYPEDEF type validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:229:6: ^( TYPEDEF type validId )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:232:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal98 = None
        string_literal99 = None
        string_literal100 = None
        string_literal101 = None
        string_literal102 = None
        string_literal103 = None
        string_literal104 = None
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
        string_literal117 = None
        validId118 = None


        string_literal98_tree = None
        string_literal99_tree = None
        string_literal100_tree = None
        string_literal101_tree = None
        string_literal102_tree = None
        string_literal103_tree = None
        string_literal104_tree = None
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
        string_literal117_tree = None
        stream_67 = RewriteRuleTokenStream(self.adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self.adaptor, "token 66")
        stream_94 = RewriteRuleTokenStream(self.adaptor, "token 94")
        stream_93 = RewriteRuleTokenStream(self.adaptor, "token 93")
        stream_92 = RewriteRuleTokenStream(self.adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self.adaptor, "token 91")
        stream_90 = RewriteRuleTokenStream(self.adaptor, "token 90")
        stream_86 = RewriteRuleTokenStream(self.adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self.adaptor, "token 87")
        stream_88 = RewriteRuleTokenStream(self.adaptor, "token 88")
        stream_89 = RewriteRuleTokenStream(self.adaptor, "token 89")
        stream_85 = RewriteRuleTokenStream(self.adaptor, "token 85")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:233:2: ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId )
                alt19 = 16
                LA19 = self.input.LA(1)
                if LA19 == 85:
                    alt19 = 1
                elif LA19 == 86:
                    alt19 = 2
                elif LA19 == 87:
                    alt19 = 3
                elif LA19 == 88:
                    alt19 = 4
                elif LA19 == 66:
                    alt19 = 5
                elif LA19 == 67:
                    LA19_6 = self.input.LA(2)

                    if (LA19_6 == 67) :
                        alt19 = 7
                    elif (LA19_6 == Identifier) :
                        alt19 = 6
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("232:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 6, self.input)

                        raise nvae

                elif LA19 == 89:
                    LA19_7 = self.input.LA(2)

                    if (LA19_7 == 67) :
                        LA19_16 = self.input.LA(3)

                        if (LA19_16 == 67) :
                            alt19 = 10
                        elif (LA19_16 == Identifier) :
                            alt19 = 9
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("232:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 16, self.input)

                            raise nvae

                    elif (LA19_7 == 66) :
                        alt19 = 8
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("232:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 7, self.input)

                        raise nvae

                elif LA19 == 90:
                    alt19 = 11
                elif LA19 == 91:
                    alt19 = 12
                elif LA19 == 92:
                    alt19 = 13
                elif LA19 == 93:
                    alt19 = 14
                elif LA19 == 94:
                    alt19 = 15
                elif LA19 == Identifier:
                    alt19 = 16
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("232:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:233:4: 'boolean'
                    string_literal98 = self.input.LT(1)
                    self.match(self.input, 85, self.FOLLOW_85_in_type964)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_85.add(string_literal98)
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
                        # 233:14: -> BOOLEAN
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(BOOLEAN, "BOOLEAN"))





                elif alt19 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:234:4: 'void'
                    string_literal99 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_type973)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_86.add(string_literal99)
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
                        # 234:11: -> VOID
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(VOID, "VOID"))





                elif alt19 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:235:4: 'string'
                    string_literal100 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_type982)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_87.add(string_literal100)
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
                        # 235:13: -> STRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(STRING, "STRING"))





                elif alt19 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:236:4: 'octet'
                    string_literal101 = self.input.LT(1)
                    self.match(self.input, 88, self.FOLLOW_88_in_type991)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_88.add(string_literal101)
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
                        # 236:12: -> OCTET
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(OCTET, "OCTET"))





                elif alt19 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:237:4: 'short'
                    string_literal102 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_type1000)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_66.add(string_literal102)
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
                        # 237:12: -> SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(SHORT, "SHORT"))





                elif alt19 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:238:4: 'long'
                    string_literal103 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1009)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal103)
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
                        # 238:11: -> LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG, "LONG"))





                elif alt19 == 7:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:239:4: 'long' 'long'
                    string_literal104 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1018)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal104)
                    string_literal105 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1020)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal105)
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
                        # 239:18: -> LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG_LONG, "LONG_LONG"))





                elif alt19 == 8:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:240:4: 'unsigned' 'short'
                    string_literal106 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_type1029)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_89.add(string_literal106)
                    string_literal107 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_type1031)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_66.add(string_literal107)
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
                        # 240:23: -> UNSIGNED_SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_SHORT, "UNSIGNED_SHORT"))





                elif alt19 == 9:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:241:4: 'unsigned' 'long'
                    string_literal108 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_type1040)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_89.add(string_literal108)
                    string_literal109 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1042)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal109)
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
                        # 241:22: -> UNSIGNED_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG, "UNSIGNED_LONG"))





                elif alt19 == 10:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:242:4: 'unsigned' 'long' 'long'
                    string_literal110 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_type1051)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_89.add(string_literal110)
                    string_literal111 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1053)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal111)
                    string_literal112 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_type1055)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_67.add(string_literal112)
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
                        # 242:29: -> UNSIGNED_LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG_LONG, "UNSIGNED_LONG_LONG"))





                elif alt19 == 11:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:243:4: 'float'
                    string_literal113 = self.input.LT(1)
                    self.match(self.input, 90, self.FOLLOW_90_in_type1064)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_90.add(string_literal113)
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
                        # 243:12: -> FLOAT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(FLOAT, "FLOAT"))





                elif alt19 == 12:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:244:4: 'double'
                    string_literal114 = self.input.LT(1)
                    self.match(self.input, 91, self.FOLLOW_91_in_type1073)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_91.add(string_literal114)
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
                        # 244:13: -> DOUBLE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(DOUBLE, "DOUBLE"))





                elif alt19 == 13:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:245:4: 'char'
                    string_literal115 = self.input.LT(1)
                    self.match(self.input, 92, self.FOLLOW_92_in_type1082)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_92.add(string_literal115)
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
                        # 245:11: -> CHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(CHAR, "CHAR"))





                elif alt19 == 14:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:246:4: 'wchar'
                    string_literal116 = self.input.LT(1)
                    self.match(self.input, 93, self.FOLLOW_93_in_type1091)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_93.add(string_literal116)
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
                        # 246:12: -> WCHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WCHAR, "WCHAR"))





                elif alt19 == 15:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:247:4: 'wstring'
                    string_literal117 = self.input.LT(1)
                    self.match(self.input, 94, self.FOLLOW_94_in_type1100)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_94.add(string_literal117)
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
                        # 247:14: -> WSTRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WSTRING, "WSTRING"))





                elif alt19 == 16:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:248:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_type1109)
                    validId118 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId118.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:251:1: mathExpr : mathMultDiv ;
    def mathExpr(self, ):

        retval = self.mathExpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mathMultDiv119 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:252:2: ( mathMultDiv )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:252:4: mathMultDiv
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathMultDiv_in_mathExpr1120)
                mathMultDiv119 = self.mathMultDiv()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathMultDiv119.tree)



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

    class mathMultDiv_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathMultDiv
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:255:1: mathMultDiv : mathAddSub ( ( '*' | '/' ) mathAddSub )? ;
    def mathMultDiv(self, ):

        retval = self.mathMultDiv_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set121 = None
        mathAddSub120 = None

        mathAddSub122 = None


        set121_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:256:2: ( mathAddSub ( ( '*' | '/' ) mathAddSub )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:256:4: mathAddSub ( ( '*' | '/' ) mathAddSub )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathAddSub_in_mathMultDiv1131)
                mathAddSub120 = self.mathAddSub()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathAddSub120.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:256:15: ( ( '*' | '/' ) mathAddSub )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((95 <= LA20_0 <= 96)) :
                    alt20 = 1
                if alt20 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:256:16: ( '*' | '/' ) mathAddSub
                    set121 = self.input.LT(1)
                    if (95 <= self.input.LA(1) <= 96):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set121))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_mathMultDiv1134
                            )
                        raise mse


                    self.following.append(self.FOLLOW_mathAddSub_in_mathMultDiv1140)
                    mathAddSub122 = self.mathAddSub()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathAddSub122.tree)






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

    class mathAddSub_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathAddSub
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:259:1: mathAddSub : mathShift ( ( '+' | '-' ) mathShift )? ;
    def mathAddSub(self, ):

        retval = self.mathAddSub_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set124 = None
        mathShift123 = None

        mathShift125 = None


        set124_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:260:2: ( mathShift ( ( '+' | '-' ) mathShift )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:260:4: mathShift ( ( '+' | '-' ) mathShift )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathShift_in_mathAddSub1153)
                mathShift123 = self.mathShift()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathShift123.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:260:14: ( ( '+' | '-' ) mathShift )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((97 <= LA21_0 <= 98)) :
                    alt21 = 1
                if alt21 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:260:15: ( '+' | '-' ) mathShift
                    set124 = self.input.LT(1)
                    if (97 <= self.input.LA(1) <= 98):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set124))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_mathAddSub1156
                            )
                        raise mse


                    self.following.append(self.FOLLOW_mathShift_in_mathAddSub1162)
                    mathShift125 = self.mathShift()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathShift125.tree)






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

    class mathShift_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathShift
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:263:1: mathShift : mathVar ( '<<' mathVar )? ;
    def mathShift(self, ):

        retval = self.mathShift_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal127 = None
        mathVar126 = None

        mathVar128 = None


        string_literal127_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:264:2: ( mathVar ( '<<' mathVar )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:264:4: mathVar ( '<<' mathVar )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathVar_in_mathShift1175)
                mathVar126 = self.mathVar()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathVar126.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:264:12: ( '<<' mathVar )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 99) :
                    alt22 = 1
                if alt22 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:264:13: '<<' mathVar
                    string_literal127 = self.input.LT(1)
                    self.match(self.input, 99, self.FOLLOW_99_in_mathShift1178)
                    if self.failed:
                        return retval

                    string_literal127_tree = self.adaptor.createWithPayload(string_literal127)
                    self.adaptor.addChild(root_0, string_literal127_tree)

                    self.following.append(self.FOLLOW_mathVar_in_mathShift1180)
                    mathVar128 = self.mathVar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathVar128.tree)






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

    class mathVar_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start mathVar
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:267:1: mathVar : ( Integer | validId );
    def mathVar(self, ):

        retval = self.mathVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Integer129 = None
        validId130 = None


        Integer129_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:268:2: ( Integer | validId )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == Integer) :
                    alt23 = 1
                elif (LA23_0 == Identifier) :
                    alt23 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("267:1: mathVar : ( Integer | validId );", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:268:4: Integer
                    root_0 = self.adaptor.nil()

                    Integer129 = self.input.LT(1)
                    self.match(self.input, Integer, self.FOLLOW_Integer_in_mathVar1193)
                    if self.failed:
                        return retval

                    Integer129_tree = self.adaptor.createWithPayload(Integer129)
                    self.adaptor.addChild(root_0, Integer129_tree)



                elif alt23 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:269:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_mathVar1198)
                    validId130 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId130.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:272:1: validIdList : validId ( ',' validId )* ;
    def validIdList(self, ):

        retval = self.validIdList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal132 = None
        validId131 = None

        validId133 = None


        char_literal132_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:273:2: ( validId ( ',' validId )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:273:4: validId ( ',' validId )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_validId_in_validIdList1209)
                validId131 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, validId131.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:273:12: ( ',' validId )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 52) :
                        alt24 = 1


                    if alt24 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:273:13: ',' validId
                        char_literal132 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_validIdList1212)
                        if self.failed:
                            return retval

                        char_literal132_tree = self.adaptor.createWithPayload(char_literal132)
                        self.adaptor.addChild(root_0, char_literal132_tree)

                        self.following.append(self.FOLLOW_validId_in_validIdList1214)
                        validId133 = self.validId()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, validId133.tree)


                    else:
                        break #loop24





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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:276:1: validId : Identifier ;
    def validId(self, ):

        retval = self.validId_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Identifier134 = None

        Identifier134_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:277:2: ( Identifier )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:277:4: Identifier
                root_0 = self.adaptor.nil()

                Identifier134 = self.input.LT(1)
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_validId1227)
                if self.failed:
                    return retval

                Identifier134_tree = self.adaptor.createWithPayload(Identifier134)
                self.adaptor.addChild(root_0, Identifier134_tree)




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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:280:1: uuid : UUID ;
    def uuid(self, ):

        retval = self.uuid_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UUID135 = None

        UUID135_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:281:2: ( UUID )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:281:4: UUID
                root_0 = self.adaptor.nil()

                UUID135 = self.input.LT(1)
                self.match(self.input, UUID, self.FOLLOW_UUID_in_uuid1238)
                if self.failed:
                    return retval

                UUID135_tree = self.adaptor.createWithPayload(UUID135)
                self.adaptor.addChild(root_0, UUID135_tree)




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
        u"\11\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\46\1\74\3\uffff\1\64\1\74\1\64\1\46"
        )

    DFA9_max = DFA.unpack(
        u"\1\136\1\75\3\uffff\1\64\1\75\1\65\1\136"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\3\4\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\4\14\uffff\1\1\14\uffff\1\3\1\uffff\2\4\1\2\20\uffff"
        u"\12\4"),
        DFA.unpack(u"\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\2\7"),
        DFA.unpack(u"\1\6\1\10"),
        DFA.unpack(u"\1\4\33\uffff\2\4\1\2\20\uffff\12\4")
    ]

    # class definition for DFA #9

    DFA9 = DFA
 

    FOLLOW_toplevel_in_idlFile158 = frozenset([34, 35, 49, 51, 84])
    FOLLOW_EOF_in_idlFile161 = frozenset([1])
    FOLLOW_interface_in_toplevel173 = frozenset([1])
    FOLLOW_typedef_in_toplevel178 = frozenset([1])
    FOLLOW_nativeTypeDecl_in_toplevel183 = frozenset([1])
    FOLLOW_include_in_toplevel188 = frozenset([1])
    FOLLOW_inline_in_toplevel193 = frozenset([1])
    FOLLOW_Include_in_include204 = frozenset([1])
    FOLLOW_InlineCHeader_in_inline223 = frozenset([1])
    FOLLOW_49_in_interface249 = frozenset([38])
    FOLLOW_validId_in_interface251 = frozenset([50])
    FOLLOW_50_in_interface253 = frozenset([1])
    FOLLOW_51_in_interface269 = frozenset([36, 57, 58, 59, 60, 61])
    FOLLOW_interfaceModifier_in_interface272 = frozenset([52])
    FOLLOW_52_in_interface274 = frozenset([36, 57, 58, 59, 60, 61])
    FOLLOW_UUID_in_interface278 = frozenset([53])
    FOLLOW_53_in_interface280 = frozenset([49])
    FOLLOW_49_in_interface284 = frozenset([38])
    FOLLOW_validId_in_interface286 = frozenset([54, 55])
    FOLLOW_54_in_interface289 = frozenset([38])
    FOLLOW_validIdList_in_interface291 = frozenset([55])
    FOLLOW_55_in_interface298 = frozenset([38, 51, 56, 64, 66, 67, 68, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_interfaceBody_in_interface300 = frozenset([56])
    FOLLOW_56_in_interface302 = frozenset([50])
    FOLLOW_50_in_interface304 = frozenset([1])
    FOLLOW_interfaceModifier_in_interfaceModifierList374 = frozenset([1, 52])
    FOLLOW_52_in_interfaceModifierList377 = frozenset([57, 58, 59, 60, 61])
    FOLLOW_interfaceModifier_in_interfaceModifierList379 = frozenset([1, 52])
    FOLLOW_set_in_interfaceModifier0 = frozenset([1])
    FOLLOW_interfaceBodyItem_in_interfaceBody430 = frozenset([1, 38, 51, 64, 66, 67, 68, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_attribute_in_interfaceBodyItem442 = frozenset([1])
    FOLLOW_const_in_interfaceBodyItem447 = frozenset([1])
    FOLLOW_method_in_interfaceBodyItem452 = frozenset([1])
    FOLLOW_methodModifiers_in_method463 = frozenset([38, 66, 67, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_type_in_method466 = frozenset([38])
    FOLLOW_validId_in_method468 = frozenset([62])
    FOLLOW_62_in_method470 = frozenset([51, 69, 70, 71])
    FOLLOW_paramList_in_method472 = frozenset([63])
    FOLLOW_63_in_method474 = frozenset([50])
    FOLLOW_50_in_method476 = frozenset([1])
    FOLLOW_64_in_const512 = frozenset([38, 66, 67])
    FOLLOW_constType_in_const514 = frozenset([38])
    FOLLOW_validId_in_const516 = frozenset([65])
    FOLLOW_65_in_const518 = frozenset([37, 38])
    FOLLOW_mathExpr_in_const520 = frozenset([50])
    FOLLOW_50_in_const522 = frozenset([1])
    FOLLOW_66_in_constType547 = frozenset([1])
    FOLLOW_67_in_constType556 = frozenset([1])
    FOLLOW_validId_in_constType565 = frozenset([1])
    FOLLOW_methodModifiers_in_attribute576 = frozenset([68])
    FOLLOW_68_in_attribute579 = frozenset([38, 66, 67, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_type_in_attribute581 = frozenset([38])
    FOLLOW_validId_in_attribute583 = frozenset([50])
    FOLLOW_50_in_attribute585 = frozenset([1])
    FOLLOW_51_in_methodModifiers614 = frozenset([60, 61])
    FOLLOW_methodModifier_in_methodModifiers616 = frozenset([52])
    FOLLOW_52_in_methodModifiers619 = frozenset([60, 61])
    FOLLOW_methodModifier_in_methodModifiers621 = frozenset([52, 53])
    FOLLOW_53_in_methodModifiers625 = frozenset([1])
    FOLLOW_set_in_methodModifier0 = frozenset([1])
    FOLLOW_paramDecl_in_paramList659 = frozenset([52])
    FOLLOW_52_in_paramList662 = frozenset([51, 69, 70, 71])
    FOLLOW_paramDecl_in_paramList664 = frozenset([1, 52])
    FOLLOW_paramModifiersDecl_in_paramDecl684 = frozenset([69, 70, 71])
    FOLLOW_paramType_in_paramDecl687 = frozenset([38, 66, 67, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_type_in_paramDecl689 = frozenset([38])
    FOLLOW_validId_in_paramDecl691 = frozenset([1])
    FOLLOW_set_in_paramType0 = frozenset([1])
    FOLLOW_51_in_paramModifiersDecl744 = frozenset([64, 72, 73, 74, 75])
    FOLLOW_paramModifier_in_paramModifiersDecl746 = frozenset([52, 53])
    FOLLOW_52_in_paramModifiersDecl749 = frozenset([64, 72, 73, 74, 75])
    FOLLOW_paramModifier_in_paramModifiersDecl751 = frozenset([52, 53])
    FOLLOW_53_in_paramModifiersDecl755 = frozenset([1])
    FOLLOW_72_in_paramModifier774 = frozenset([1])
    FOLLOW_sizeIs_in_paramModifier779 = frozenset([1])
    FOLLOW_73_in_paramModifier784 = frozenset([1])
    FOLLOW_64_in_paramModifier789 = frozenset([1])
    FOLLOW_74_in_paramModifier794 = frozenset([1])
    FOLLOW_75_in_sizeIs806 = frozenset([62])
    FOLLOW_62_in_sizeIs808 = frozenset([38])
    FOLLOW_validId_in_sizeIs810 = frozenset([63])
    FOLLOW_63_in_sizeIs812 = frozenset([1])
    FOLLOW_nativeType_in_nativeTypeDecl824 = frozenset([50])
    FOLLOW_50_in_nativeTypeDecl826 = frozenset([1])
    FOLLOW_typeModifiersDecl_in_nativeType838 = frozenset([76])
    FOLLOW_76_in_nativeType840 = frozenset([38])
    FOLLOW_validId_in_nativeType842 = frozenset([1])
    FOLLOW_51_in_typeModifiersDecl865 = frozenset([77, 78, 79, 80, 81, 82, 83])
    FOLLOW_typeModifier_in_typeModifiersDecl867 = frozenset([52, 53])
    FOLLOW_52_in_typeModifiersDecl870 = frozenset([77, 78, 79, 80, 81, 82, 83])
    FOLLOW_typeModifier_in_typeModifiersDecl872 = frozenset([52, 53])
    FOLLOW_53_in_typeModifiersDecl876 = frozenset([1])
    FOLLOW_set_in_typeModifier0 = frozenset([1])
    FOLLOW_84_in_typedef935 = frozenset([38, 66, 67, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94])
    FOLLOW_type_in_typedef937 = frozenset([38])
    FOLLOW_validId_in_typedef939 = frozenset([50])
    FOLLOW_50_in_typedef941 = frozenset([1])
    FOLLOW_85_in_type964 = frozenset([1])
    FOLLOW_86_in_type973 = frozenset([1])
    FOLLOW_87_in_type982 = frozenset([1])
    FOLLOW_88_in_type991 = frozenset([1])
    FOLLOW_66_in_type1000 = frozenset([1])
    FOLLOW_67_in_type1009 = frozenset([1])
    FOLLOW_67_in_type1018 = frozenset([67])
    FOLLOW_67_in_type1020 = frozenset([1])
    FOLLOW_89_in_type1029 = frozenset([66])
    FOLLOW_66_in_type1031 = frozenset([1])
    FOLLOW_89_in_type1040 = frozenset([67])
    FOLLOW_67_in_type1042 = frozenset([1])
    FOLLOW_89_in_type1051 = frozenset([67])
    FOLLOW_67_in_type1053 = frozenset([67])
    FOLLOW_67_in_type1055 = frozenset([1])
    FOLLOW_90_in_type1064 = frozenset([1])
    FOLLOW_91_in_type1073 = frozenset([1])
    FOLLOW_92_in_type1082 = frozenset([1])
    FOLLOW_93_in_type1091 = frozenset([1])
    FOLLOW_94_in_type1100 = frozenset([1])
    FOLLOW_validId_in_type1109 = frozenset([1])
    FOLLOW_mathMultDiv_in_mathExpr1120 = frozenset([1])
    FOLLOW_mathAddSub_in_mathMultDiv1131 = frozenset([1, 95, 96])
    FOLLOW_set_in_mathMultDiv1134 = frozenset([37, 38])
    FOLLOW_mathAddSub_in_mathMultDiv1140 = frozenset([1])
    FOLLOW_mathShift_in_mathAddSub1153 = frozenset([1, 97, 98])
    FOLLOW_set_in_mathAddSub1156 = frozenset([37, 38])
    FOLLOW_mathShift_in_mathAddSub1162 = frozenset([1])
    FOLLOW_mathVar_in_mathShift1175 = frozenset([1, 99])
    FOLLOW_99_in_mathShift1178 = frozenset([37, 38])
    FOLLOW_mathVar_in_mathShift1180 = frozenset([1])
    FOLLOW_Integer_in_mathVar1193 = frozenset([1])
    FOLLOW_validId_in_mathVar1198 = frozenset([1])
    FOLLOW_validId_in_validIdList1209 = frozenset([1, 52])
    FOLLOW_52_in_validIdList1212 = frozenset([38])
    FOLLOW_validId_in_validIdList1214 = frozenset([1, 52])
    FOLLOW_Identifier_in_validId1227 = frozenset([1])
    FOLLOW_UUID_in_uuid1238 = frozenset([1])

