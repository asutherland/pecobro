# $ANTLR 3.0.1 /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g 2008-05-19 21:53:24

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FORWARD=7
UUIDPayload=44
LONG_LONG=22
UUID=34
InlineCHeader=33
CONST=6
CHAR=28
LineComment=46
PARAM=13
FLOAT=26
EOF=-1
WCHAR=29
Identifier=36
BlockComment=45
MODIFIERS=11
BOOLEAN=18
HexChar=39
UNSIGNED_LONG=24
UNSIGNED_SHORT=23
DOUBLE=27
HexInteger=38
WhiteSpace=43
VOID=17
BODY=5
WSTRING=31
UNSIGNED_LONG_LONG=25
ATTR=4
IdentifierPart=42
PARAMS=14
I_UUID=9
DecimalChar=40
TYPEDEF=16
DecimalInteger=37
IdentifierStart=41
NATIVE=12
SHORT=20
Include=32
PARENTS=15
INTERFACE=8
LONG=21
METHOD=10
Integer=35
OCTET=19
STRING=30

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ATTR", "BODY", "CONST", "FORWARD", "INTERFACE", "I_UUID", "METHOD", 
    "MODIFIERS", "NATIVE", "PARAM", "PARAMS", "PARENTS", "TYPEDEF", "VOID", 
    "BOOLEAN", "OCTET", "SHORT", "LONG", "LONG_LONG", "UNSIGNED_SHORT", 
    "UNSIGNED_LONG", "UNSIGNED_LONG_LONG", "FLOAT", "DOUBLE", "CHAR", "WCHAR", 
    "STRING", "WSTRING", "Include", "InlineCHeader", "UUID", "Integer", 
    "Identifier", "DecimalInteger", "HexInteger", "HexChar", "DecimalChar", 
    "IdentifierStart", "IdentifierPart", "WhiteSpace", "UUIDPayload", "BlockComment", 
    "LineComment", "'interface'", "';'", "'['", "','", "']'", "':'", "'{'", 
    "'}'", "'scriptable'", "'function'", "'object'", "'notxpcom'", "'noscript'", 
    "'('", "')'", "'const'", "'='", "'short'", "'long'", "'attribute'", 
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:43:1: idlFile : ( toplevel )* EOF ;
    def idlFile(self, ):

        retval = self.idlFile_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        toplevel1 = None


        EOF2_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:44:2: ( ( toplevel )* EOF )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:44:4: ( toplevel )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:44:4: ( toplevel )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((Include <= LA1_0 <= InlineCHeader) or LA1_0 == 47 or LA1_0 == 49 or LA1_0 == 82) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:44:4: toplevel
                        self.following.append(self.FOLLOW_toplevel_in_idlFile147)
                        toplevel1 = self.toplevel()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, toplevel1.tree)


                    else:
                        break #loop1


                EOF2 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_idlFile150)
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:47:1: toplevel : ( interface | typedef | nativeTypeDecl | Include | InlineCHeader );
    def toplevel(self, ):

        retval = self.toplevel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Include6 = None
        InlineCHeader7 = None
        interface3 = None

        typedef4 = None

        nativeTypeDecl5 = None


        Include6_tree = None
        InlineCHeader7_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:48:2: ( interface | typedef | nativeTypeDecl | Include | InlineCHeader )
                alt2 = 5
                LA2 = self.input.LA(1)
                if LA2 == 47:
                    alt2 = 1
                elif LA2 == 49:
                    LA2_2 = self.input.LA(2)

                    if ((75 <= LA2_2 <= 81)) :
                        alt2 = 3
                    elif (LA2_2 == UUID or (55 <= LA2_2 <= 59)) :
                        alt2 = 1
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("47:1: toplevel : ( interface | typedef | nativeTypeDecl | Include | InlineCHeader );", 2, 2, self.input)

                        raise nvae

                elif LA2 == 82:
                    alt2 = 2
                elif LA2 == Include:
                    alt2 = 4
                elif LA2 == InlineCHeader:
                    alt2 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("47:1: toplevel : ( interface | typedef | nativeTypeDecl | Include | InlineCHeader );", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:48:4: interface
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_interface_in_toplevel162)
                    interface3 = self.interface()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, interface3.tree)


                elif alt2 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:49:4: typedef
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_typedef_in_toplevel167)
                    typedef4 = self.typedef()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, typedef4.tree)


                elif alt2 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:50:4: nativeTypeDecl
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_nativeTypeDecl_in_toplevel172)
                    nativeTypeDecl5 = self.nativeTypeDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, nativeTypeDecl5.tree)


                elif alt2 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:51:4: Include
                    root_0 = self.adaptor.nil()

                    Include6 = self.input.LT(1)
                    self.match(self.input, Include, self.FOLLOW_Include_in_toplevel177)
                    if self.failed:
                        return retval

                    Include6_tree = self.adaptor.createWithPayload(Include6)
                    self.adaptor.addChild(root_0, Include6_tree)



                elif alt2 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:52:4: InlineCHeader
                    root_0 = self.adaptor.nil()

                    InlineCHeader7 = self.input.LT(1)
                    self.match(self.input, InlineCHeader, self.FOLLOW_InlineCHeader_in_toplevel182)
                    if self.failed:
                        return retval

                    InlineCHeader7_tree = self.adaptor.createWithPayload(InlineCHeader7)
                    self.adaptor.addChild(root_0, InlineCHeader7_tree)



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

    class interface_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start interface
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:55:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );
    def interface(self, ):

        retval = self.interface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal8 = None
        char_literal10 = None
        char_literal11 = None
        char_literal13 = None
        UUID14 = None
        char_literal15 = None
        string_literal16 = None
        char_literal18 = None
        char_literal20 = None
        char_literal22 = None
        char_literal23 = None
        validId9 = None

        interfaceModifier12 = None

        validId17 = None

        validIdList19 = None

        interfaceBody21 = None


        string_literal8_tree = None
        char_literal10_tree = None
        char_literal11_tree = None
        char_literal13_tree = None
        UUID14_tree = None
        char_literal15_tree = None
        string_literal16_tree = None
        char_literal18_tree = None
        char_literal20_tree = None
        char_literal22_tree = None
        char_literal23_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
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
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:57:2: ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 47) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == Identifier) :
                        LA6_3 = self.input.LA(3)

                        if (LA6_3 == 48) :
                            alt6 = 1
                        elif ((52 <= LA6_3 <= 53)) :
                            alt6 = 2
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("55:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 3, self.input)

                            raise nvae

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("55:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 1, self.input)

                        raise nvae

                elif (LA6_0 == 49) :
                    alt6 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("55:1: interface options {backtrack=true; } : ( 'interface' validId ';' -> ^( FORWARD validId ) | ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';' -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) ) );", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:57:4: 'interface' validId ';'
                    string_literal8 = self.input.LT(1)
                    self.match(self.input, 47, self.FOLLOW_47_in_interface200)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_47.add(string_literal8)
                    self.following.append(self.FOLLOW_validId_in_interface202)
                    validId9 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId9.tree)
                    char_literal10 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_interface204)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_48.add(char_literal10)
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
                        # 58:3: -> ^( FORWARD validId )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:58:6: ^( FORWARD validId )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FORWARD, "FORWARD"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt6 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:4: ( '[' ( interfaceModifier ',' )* UUID ']' )? 'interface' validId ( ':' validIdList )? '{' interfaceBody '}' ';'
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:4: ( '[' ( interfaceModifier ',' )* UUID ']' )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 49) :
                        alt4 = 1
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:5: '[' ( interfaceModifier ',' )* UUID ']'
                        char_literal11 = self.input.LT(1)
                        self.match(self.input, 49, self.FOLLOW_49_in_interface220)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_49.add(char_literal11)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:9: ( interfaceModifier ',' )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if ((55 <= LA3_0 <= 59)) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:10: interfaceModifier ','
                                self.following.append(self.FOLLOW_interfaceModifier_in_interface223)
                                interfaceModifier12 = self.interfaceModifier()
                                self.following.pop()
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_interfaceModifier.add(interfaceModifier12.tree)
                                char_literal13 = self.input.LT(1)
                                self.match(self.input, 50, self.FOLLOW_50_in_interface225)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_50.add(char_literal13)


                            else:
                                break #loop3


                        UUID14 = self.input.LT(1)
                        self.match(self.input, UUID, self.FOLLOW_UUID_in_interface229)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_UUID.add(UUID14)
                        char_literal15 = self.input.LT(1)
                        self.match(self.input, 51, self.FOLLOW_51_in_interface231)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_51.add(char_literal15)



                    string_literal16 = self.input.LT(1)
                    self.match(self.input, 47, self.FOLLOW_47_in_interface235)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_47.add(string_literal16)
                    self.following.append(self.FOLLOW_validId_in_interface237)
                    validId17 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_validId.add(validId17.tree)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:65: ( ':' validIdList )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 52) :
                        alt5 = 1
                    if alt5 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:59:66: ':' validIdList
                        char_literal18 = self.input.LT(1)
                        self.match(self.input, 52, self.FOLLOW_52_in_interface240)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_52.add(char_literal18)
                        self.following.append(self.FOLLOW_validIdList_in_interface242)
                        validIdList19 = self.validIdList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_validIdList.add(validIdList19.tree)



                    char_literal20 = self.input.LT(1)
                    self.match(self.input, 53, self.FOLLOW_53_in_interface249)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_53.add(char_literal20)
                    self.following.append(self.FOLLOW_interfaceBody_in_interface251)
                    interfaceBody21 = self.interfaceBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_interfaceBody.add(interfaceBody21.tree)
                    char_literal22 = self.input.LT(1)
                    self.match(self.input, 54, self.FOLLOW_54_in_interface253)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_54.add(char_literal22)
                    char_literal23 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_interface255)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_48.add(char_literal23)
                    # AST Rewrite
                    # elements: interfaceBody, UUID, validIdList, validId, interfaceModifier
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
                        # 61:3: -> ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:61:6: ^( INTERFACE validId ^( I_UUID ( UUID )? ) ^( PARENTS ( validIdList )? ) ^( MODIFIERS ( interfaceModifier )* ) ^( BODY interfaceBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INTERFACE, "INTERFACE"), root_1)

                        self.adaptor.addChild(root_1, stream_validId.next())
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:61:26: ^( I_UUID ( UUID )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(I_UUID, "I_UUID"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:61:35: ( UUID )?
                        if stream_UUID.hasNext():
                            self.adaptor.addChild(root_2, stream_UUID.next())


                        stream_UUID.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:61:42: ^( PARENTS ( validIdList )? )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARENTS, "PARENTS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:61:52: ( validIdList )?
                        if stream_validIdList.hasNext():
                            self.adaptor.addChild(root_2, stream_validIdList.next())


                        stream_validIdList.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:62:12: ^( MODIFIERS ( interfaceModifier )* )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:62:24: ( interfaceModifier )*
                        while stream_interfaceModifier.hasNext():
                            self.adaptor.addChild(root_2, stream_interfaceModifier.next())


                        stream_interfaceModifier.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:63:12: ^( BODY interfaceBody )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:66:1: interfaceModifierList : interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* ;
    def interfaceModifierList(self, ):

        retval = self.interfaceModifierList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal25 = None
        interfaceModifier24 = None

        interfaceModifier26 = None


        char_literal25_tree = None
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_interfaceModifier = RewriteRuleSubtreeStream(self.adaptor, "rule interfaceModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:67:2: ( interfaceModifier ( ',' interfaceModifier )* -> ( interfaceModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:67:4: interfaceModifier ( ',' interfaceModifier )*
                self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList325)
                interfaceModifier24 = self.interfaceModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_interfaceModifier.add(interfaceModifier24.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:67:22: ( ',' interfaceModifier )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 50) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:67:23: ',' interfaceModifier
                        char_literal25 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_interfaceModifierList328)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_50.add(char_literal25)
                        self.following.append(self.FOLLOW_interfaceModifier_in_interfaceModifierList330)
                        interfaceModifier26 = self.interfaceModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_interfaceModifier.add(interfaceModifier26.tree)


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
                    # 68:3: -> ( interfaceModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:68:6: ( interfaceModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:71:1: interfaceModifier : ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' );
    def interfaceModifier(self, ):

        retval = self.interfaceModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set27 = None

        set27_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:72:2: ( 'scriptable' | 'function' | 'object' | 'notxpcom' | 'noscript' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set27 = self.input.LT(1)
                if (55 <= self.input.LA(1) <= 59):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set27))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:79:1: interfaceBody : ( interfaceBodyItem )* ;
    def interfaceBody(self, ):

        retval = self.interfaceBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        interfaceBodyItem28 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:80:2: ( ( interfaceBodyItem )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:80:4: ( interfaceBodyItem )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:80:4: ( interfaceBodyItem )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == Identifier or LA8_0 == 49 or LA8_0 == 62 or (64 <= LA8_0 <= 66) or (83 <= LA8_0 <= 92)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:80:4: interfaceBodyItem
                        self.following.append(self.FOLLOW_interfaceBodyItem_in_interfaceBody381)
                        interfaceBodyItem28 = self.interfaceBodyItem()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, interfaceBodyItem28.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:83:1: interfaceBodyItem : ( attribute | const | method );
    def interfaceBodyItem(self, ):

        retval = self.interfaceBodyItem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        attribute29 = None

        const30 = None

        method31 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:84:2: ( attribute | const | method )
                alt9 = 3
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:84:4: attribute
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_attribute_in_interfaceBodyItem393)
                    attribute29 = self.attribute()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, attribute29.tree)


                elif alt9 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:85:4: const
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_const_in_interfaceBodyItem398)
                    const30 = self.const()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, const30.tree)


                elif alt9 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:86:4: method
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_method_in_interfaceBodyItem403)
                    method31 = self.method()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, method31.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:89:1: method : ( methodModifiers )? type validId '(' paramList ')' ';' -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) ) ;
    def method(self, ):

        retval = self.method_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal35 = None
        char_literal37 = None
        char_literal38 = None
        methodModifiers32 = None

        type33 = None

        validId34 = None

        paramList36 = None


        char_literal35_tree = None
        char_literal37_tree = None
        char_literal38_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self.adaptor, "token 61")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_paramList = RewriteRuleSubtreeStream(self.adaptor, "rule paramList")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:2: ( ( methodModifiers )? type validId '(' paramList ')' ';' -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: ( methodModifiers )? type validId '(' paramList ')' ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: ( methodModifiers )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 49) :
                    alt10 = 1
                if alt10 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:90:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_method414)
                    methodModifiers32 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers32.tree)



                self.following.append(self.FOLLOW_type_in_method417)
                type33 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type33.tree)
                self.following.append(self.FOLLOW_validId_in_method419)
                validId34 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId34.tree)
                char_literal35 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_method421)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_60.add(char_literal35)
                self.following.append(self.FOLLOW_paramList_in_method423)
                paramList36 = self.paramList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramList.add(paramList36.tree)
                char_literal37 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_method425)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_61.add(char_literal37)
                char_literal38 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_method427)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_48.add(char_literal38)
                # AST Rewrite
                # elements: paramList, methodModifiers, validId, type
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
                    # 91:3: -> ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:91:6: ^( METHOD type validId ^( MODIFIERS ( methodModifiers )? ) ^( PARAMS paramList ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(METHOD, "METHOD"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:91:28: ^( MODIFIERS ( methodModifiers )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:91:40: ( methodModifiers )?
                    if stream_methodModifiers.hasNext():
                        self.adaptor.addChild(root_2, stream_methodModifiers.next())


                    stream_methodModifiers.reset();

                    self.adaptor.addChild(root_1, root_2)
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:91:58: ^( PARAMS paramList )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:94:1: const : 'const' constType validId '=' mathExpr ';' -> ^( CONST constType validId mathExpr ) ;
    def const(self, ):

        retval = self.const_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal39 = None
        char_literal42 = None
        char_literal44 = None
        constType40 = None

        validId41 = None

        mathExpr43 = None


        string_literal39_tree = None
        char_literal42_tree = None
        char_literal44_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_62 = RewriteRuleTokenStream(self.adaptor, "token 62")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_constType = RewriteRuleSubtreeStream(self.adaptor, "rule constType")
        stream_mathExpr = RewriteRuleSubtreeStream(self.adaptor, "rule mathExpr")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:95:2: ( 'const' constType validId '=' mathExpr ';' -> ^( CONST constType validId mathExpr ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:95:4: 'const' constType validId '=' mathExpr ';'
                string_literal39 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_const463)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_62.add(string_literal39)
                self.following.append(self.FOLLOW_constType_in_const465)
                constType40 = self.constType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_constType.add(constType40.tree)
                self.following.append(self.FOLLOW_validId_in_const467)
                validId41 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId41.tree)
                char_literal42 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_const469)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal42)
                self.following.append(self.FOLLOW_mathExpr_in_const471)
                mathExpr43 = self.mathExpr()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_mathExpr.add(mathExpr43.tree)
                char_literal44 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_const473)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_48.add(char_literal44)
                # AST Rewrite
                # elements: validId, constType, mathExpr
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
                    # 96:3: -> ^( CONST constType validId mathExpr )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:96:6: ^( CONST constType validId mathExpr )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:99:1: constType : ( 'short' -> SHORT | 'long' -> LONG | validId );
    def constType(self, ):

        retval = self.constType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal45 = None
        string_literal46 = None
        validId47 = None


        string_literal45_tree = None
        string_literal46_tree = None
        stream_64 = RewriteRuleTokenStream(self.adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:100:2: ( 'short' -> SHORT | 'long' -> LONG | validId )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == 64:
                    alt11 = 1
                elif LA11 == 65:
                    alt11 = 2
                elif LA11 == Identifier:
                    alt11 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("99:1: constType : ( 'short' -> SHORT | 'long' -> LONG | validId );", 11, 0, self.input)

                    raise nvae

                if alt11 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:100:4: 'short'
                    string_literal45 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_constType498)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_64.add(string_literal45)
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
                        # 100:12: -> SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(SHORT, "SHORT"))





                elif alt11 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:101:4: 'long'
                    string_literal46 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_constType507)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal46)
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
                        # 101:11: -> LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG, "LONG"))





                elif alt11 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:102:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_constType516)
                    validId47 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId47.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:105:1: attribute : ( methodModifiers )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) ) ;
    def attribute(self, ):

        retval = self.attribute_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal49 = None
        char_literal52 = None
        methodModifiers48 = None

        type50 = None

        validId51 = None


        string_literal49_tree = None
        char_literal52_tree = None
        stream_66 = RewriteRuleTokenStream(self.adaptor, "token 66")
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_methodModifiers = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifiers")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:2: ( ( methodModifiers )? 'attribute' type validId ';' -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:4: ( methodModifiers )? 'attribute' type validId ';'
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:4: ( methodModifiers )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 49) :
                    alt12 = 1
                if alt12 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:106:4: methodModifiers
                    self.following.append(self.FOLLOW_methodModifiers_in_attribute527)
                    methodModifiers48 = self.methodModifiers()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_methodModifiers.add(methodModifiers48.tree)



                string_literal49 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_attribute530)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_66.add(string_literal49)
                self.following.append(self.FOLLOW_type_in_attribute532)
                type50 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type50.tree)
                self.following.append(self.FOLLOW_validId_in_attribute534)
                validId51 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId51.tree)
                char_literal52 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_attribute536)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_48.add(char_literal52)
                # AST Rewrite
                # elements: validId, type, methodModifiers
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
                    # 107:3: -> ^( ATTR type validId ^( MODIFIERS methodModifiers ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:107:6: ^( ATTR type validId ^( MODIFIERS methodModifiers ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ATTR, "ATTR"), root_1)

                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:107:26: ^( MODIFIERS methodModifiers )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:110:1: methodModifiers : '[' methodModifier ( ',' methodModifier )+ ']' -> ( methodModifier )* ;
    def methodModifiers(self, ):

        retval = self.methodModifiers_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal53 = None
        char_literal55 = None
        char_literal57 = None
        methodModifier54 = None

        methodModifier56 = None


        char_literal53_tree = None
        char_literal55_tree = None
        char_literal57_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_methodModifier = RewriteRuleSubtreeStream(self.adaptor, "rule methodModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:2: ( '[' methodModifier ( ',' methodModifier )+ ']' -> ( methodModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:4: '[' methodModifier ( ',' methodModifier )+ ']'
                char_literal53 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_methodModifiers565)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_49.add(char_literal53)
                self.following.append(self.FOLLOW_methodModifier_in_methodModifiers567)
                methodModifier54 = self.methodModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_methodModifier.add(methodModifier54.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:23: ( ',' methodModifier )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 50) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:111:24: ',' methodModifier
                        char_literal55 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_methodModifiers570)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_50.add(char_literal55)
                        self.following.append(self.FOLLOW_methodModifier_in_methodModifiers572)
                        methodModifier56 = self.methodModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_methodModifier.add(methodModifier56.tree)


                    else:
                        if cnt13 >= 1:
                            break #loop13

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                char_literal57 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_methodModifiers576)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal57)
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
                    # 112:3: -> ( methodModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:112:6: ( methodModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:115:1: methodModifier : ( 'noscript' | 'notxpcom' );
    def methodModifier(self, ):

        retval = self.methodModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set58 = None

        set58_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:116:2: ( 'noscript' | 'notxpcom' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set58 = self.input.LT(1)
                if (58 <= self.input.LA(1) <= 59):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set58))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:120:1: paramList : paramDecl ( ',' paramDecl )+ -> ( paramDecl )* ;
    def paramList(self, ):

        retval = self.paramList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal60 = None
        paramDecl59 = None

        paramDecl61 = None


        char_literal60_tree = None
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_paramDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramDecl")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:2: ( paramDecl ( ',' paramDecl )+ -> ( paramDecl )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:4: paramDecl ( ',' paramDecl )+
                self.following.append(self.FOLLOW_paramDecl_in_paramList610)
                paramDecl59 = self.paramDecl()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramDecl.add(paramDecl59.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:14: ( ',' paramDecl )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == 50) :
                        alt14 = 1


                    if alt14 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:121:15: ',' paramDecl
                        char_literal60 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_paramList613)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_50.add(char_literal60)
                        self.following.append(self.FOLLOW_paramDecl_in_paramList615)
                        paramDecl61 = self.paramDecl()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramDecl.add(paramDecl61.tree)


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
                    # 122:3: -> ( paramDecl )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:122:6: ( paramDecl )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:125:1: paramDecl : ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) ;
    def paramDecl(self, ):

        retval = self.paramDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        paramModifiersDecl62 = None

        paramType63 = None

        type64 = None

        validId65 = None


        stream_paramModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        stream_paramType = RewriteRuleSubtreeStream(self.adaptor, "rule paramType")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:2: ( ( paramModifiersDecl )? paramType type validId -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:4: ( paramModifiersDecl )? paramType type validId
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:4: ( paramModifiersDecl )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 49) :
                    alt15 = 1
                if alt15 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:126:4: paramModifiersDecl
                    self.following.append(self.FOLLOW_paramModifiersDecl_in_paramDecl635)
                    paramModifiersDecl62 = self.paramModifiersDecl()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_paramModifiersDecl.add(paramModifiersDecl62.tree)



                self.following.append(self.FOLLOW_paramType_in_paramDecl638)
                paramType63 = self.paramType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramType.add(paramType63.tree)
                self.following.append(self.FOLLOW_type_in_paramDecl640)
                type64 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type64.tree)
                self.following.append(self.FOLLOW_validId_in_paramDecl642)
                validId65 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId65.tree)
                # AST Rewrite
                # elements: validId, paramType, paramModifiersDecl, type
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
                    # 127:3: -> ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:127:6: ^( PARAM paramType type validId ^( MODIFIERS ( paramModifiersDecl )? ) )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PARAM, "PARAM"), root_1)

                    self.adaptor.addChild(root_1, stream_paramType.next())
                    self.adaptor.addChild(root_1, stream_type.next())
                    self.adaptor.addChild(root_1, stream_validId.next())
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:127:37: ^( MODIFIERS ( paramModifiersDecl )? )
                    root_2 = self.adaptor.nil()
                    root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(MODIFIERS, "MODIFIERS"), root_2)

                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:127:49: ( paramModifiersDecl )?
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:130:1: paramType : ( 'in' | 'out' | 'inout' );
    def paramType(self, ):

        retval = self.paramType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set66 = None

        set66_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:131:2: ( 'in' | 'out' | 'inout' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set66 = self.input.LT(1)
                if (67 <= self.input.LA(1) <= 69):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set66))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:136:1: paramModifiersDecl : '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* ;
    def paramModifiersDecl(self, ):

        retval = self.paramModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal67 = None
        char_literal69 = None
        char_literal71 = None
        paramModifier68 = None

        paramModifier70 = None


        char_literal67_tree = None
        char_literal69_tree = None
        char_literal71_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_paramModifier = RewriteRuleSubtreeStream(self.adaptor, "rule paramModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:137:2: ( '[' paramModifier ( ',' paramModifier )* ']' -> ( paramModifier )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:137:4: '[' paramModifier ( ',' paramModifier )* ']'
                char_literal67 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_paramModifiersDecl695)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_49.add(char_literal67)
                self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl697)
                paramModifier68 = self.paramModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_paramModifier.add(paramModifier68.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:137:22: ( ',' paramModifier )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 50) :
                        alt16 = 1


                    if alt16 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:137:23: ',' paramModifier
                        char_literal69 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_paramModifiersDecl700)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_50.add(char_literal69)
                        self.following.append(self.FOLLOW_paramModifier_in_paramModifiersDecl702)
                        paramModifier70 = self.paramModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_paramModifier.add(paramModifier70.tree)


                    else:
                        break #loop16


                char_literal71 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_paramModifiersDecl706)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal71)
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
                    # 138:3: -> ( paramModifier )*
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:138:6: ( paramModifier )*
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:142:1: paramModifier : ( 'array' | sizeIs | 'retval' | 'const' | 'shared' );
    def paramModifier(self, ):

        retval = self.paramModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal72 = None
        string_literal74 = None
        string_literal75 = None
        string_literal76 = None
        sizeIs73 = None


        string_literal72_tree = None
        string_literal74_tree = None
        string_literal75_tree = None
        string_literal76_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:143:2: ( 'array' | sizeIs | 'retval' | 'const' | 'shared' )
                alt17 = 5
                LA17 = self.input.LA(1)
                if LA17 == 70:
                    alt17 = 1
                elif LA17 == 73:
                    alt17 = 2
                elif LA17 == 71:
                    alt17 = 3
                elif LA17 == 62:
                    alt17 = 4
                elif LA17 == 72:
                    alt17 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("142:1: paramModifier : ( 'array' | sizeIs | 'retval' | 'const' | 'shared' );", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:143:4: 'array'
                    root_0 = self.adaptor.nil()

                    string_literal72 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_paramModifier725)
                    if self.failed:
                        return retval

                    string_literal72_tree = self.adaptor.createWithPayload(string_literal72)
                    self.adaptor.addChild(root_0, string_literal72_tree)



                elif alt17 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:144:4: sizeIs
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_sizeIs_in_paramModifier730)
                    sizeIs73 = self.sizeIs()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, sizeIs73.tree)


                elif alt17 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:145:4: 'retval'
                    root_0 = self.adaptor.nil()

                    string_literal74 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_paramModifier735)
                    if self.failed:
                        return retval

                    string_literal74_tree = self.adaptor.createWithPayload(string_literal74)
                    self.adaptor.addChild(root_0, string_literal74_tree)



                elif alt17 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:146:4: 'const'
                    root_0 = self.adaptor.nil()

                    string_literal75 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_paramModifier740)
                    if self.failed:
                        return retval

                    string_literal75_tree = self.adaptor.createWithPayload(string_literal75)
                    self.adaptor.addChild(root_0, string_literal75_tree)



                elif alt17 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:147:4: 'shared'
                    root_0 = self.adaptor.nil()

                    string_literal76 = self.input.LT(1)
                    self.match(self.input, 72, self.FOLLOW_72_in_paramModifier745)
                    if self.failed:
                        return retval

                    string_literal76_tree = self.adaptor.createWithPayload(string_literal76)
                    self.adaptor.addChild(root_0, string_literal76_tree)



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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:150:1: sizeIs : 'size_is' '(' validId ')' ;
    def sizeIs(self, ):

        retval = self.sizeIs_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal77 = None
        char_literal78 = None
        char_literal80 = None
        validId79 = None


        string_literal77_tree = None
        char_literal78_tree = None
        char_literal80_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:151:2: ( 'size_is' '(' validId ')' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:151:4: 'size_is' '(' validId ')'
                root_0 = self.adaptor.nil()

                string_literal77 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_sizeIs757)
                if self.failed:
                    return retval

                string_literal77_tree = self.adaptor.createWithPayload(string_literal77)
                self.adaptor.addChild(root_0, string_literal77_tree)

                char_literal78 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_sizeIs759)
                if self.failed:
                    return retval

                char_literal78_tree = self.adaptor.createWithPayload(char_literal78)
                self.adaptor.addChild(root_0, char_literal78_tree)

                self.following.append(self.FOLLOW_validId_in_sizeIs761)
                validId79 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, validId79.tree)
                char_literal80 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_sizeIs763)
                if self.failed:
                    return retval

                char_literal80_tree = self.adaptor.createWithPayload(char_literal80)
                self.adaptor.addChild(root_0, char_literal80_tree)




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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:154:1: nativeTypeDecl : nativeType ';' ;
    def nativeTypeDecl(self, ):

        retval = self.nativeTypeDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal82 = None
        nativeType81 = None


        char_literal82_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:2: ( nativeType ';' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:155:4: nativeType ';'
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_nativeType_in_nativeTypeDecl775)
                nativeType81 = self.nativeType()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, nativeType81.tree)
                char_literal82 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_nativeTypeDecl777)
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:158:1: nativeType : typeModifiersDecl 'native' validId -> ^( NATIVE validId typeModifiersDecl ) ;
    def nativeType(self, ):

        retval = self.nativeType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal84 = None
        typeModifiersDecl83 = None

        validId85 = None


        string_literal84_tree = None
        stream_74 = RewriteRuleTokenStream(self.adaptor, "token 74")
        stream_typeModifiersDecl = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifiersDecl")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:159:2: ( typeModifiersDecl 'native' validId -> ^( NATIVE validId typeModifiersDecl ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:159:4: typeModifiersDecl 'native' validId
                self.following.append(self.FOLLOW_typeModifiersDecl_in_nativeType789)
                typeModifiersDecl83 = self.typeModifiersDecl()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_typeModifiersDecl.add(typeModifiersDecl83.tree)
                string_literal84 = self.input.LT(1)
                self.match(self.input, 74, self.FOLLOW_74_in_nativeType791)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_74.add(string_literal84)
                self.following.append(self.FOLLOW_validId_in_nativeType793)
                validId85 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId85.tree)
                # AST Rewrite
                # elements: typeModifiersDecl, validId
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
                    # 160:3: -> ^( NATIVE validId typeModifiersDecl )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:160:6: ^( NATIVE validId typeModifiersDecl )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:163:1: typeModifiersDecl : '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ ;
    def typeModifiersDecl(self, ):

        retval = self.typeModifiersDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal86 = None
        char_literal88 = None
        char_literal90 = None
        typeModifier87 = None

        typeModifier89 = None


        char_literal86_tree = None
        char_literal88_tree = None
        char_literal90_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_typeModifier = RewriteRuleSubtreeStream(self.adaptor, "rule typeModifier")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:2: ( '[' typeModifier ( ',' typeModifier )* ']' -> ( typeModifier )+ )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:4: '[' typeModifier ( ',' typeModifier )* ']'
                char_literal86 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_typeModifiersDecl816)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_49.add(char_literal86)
                self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl818)
                typeModifier87 = self.typeModifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_typeModifier.add(typeModifier87.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:21: ( ',' typeModifier )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 50) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:164:22: ',' typeModifier
                        char_literal88 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_typeModifiersDecl821)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_50.add(char_literal88)
                        self.following.append(self.FOLLOW_typeModifier_in_typeModifiersDecl823)
                        typeModifier89 = self.typeModifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_typeModifier.add(typeModifier89.tree)


                    else:
                        break #loop18


                char_literal90 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_typeModifiersDecl827)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal90)
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
                    # 165:3: -> ( typeModifier )+
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:165:6: ( typeModifier )+
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:168:1: typeModifier : ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' );
    def typeModifier(self, ):

        retval = self.typeModifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set91 = None

        set91_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:169:2: ( 'ref' | 'ptr' | 'nsid' | 'domstring' | 'utf8string' | 'cstring' | 'astring' )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:
                root_0 = self.adaptor.nil()

                set91 = self.input.LT(1)
                if (75 <= self.input.LA(1) <= 81):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set91))
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:178:1: typedef : 'typedef' type validId ';' -> ^( TYPEDEF type validId ) ;
    def typedef(self, ):

        retval = self.typedef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal92 = None
        char_literal95 = None
        type93 = None

        validId94 = None


        string_literal92_tree = None
        char_literal95_tree = None
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_82 = RewriteRuleTokenStream(self.adaptor, "token 82")
        stream_validId = RewriteRuleSubtreeStream(self.adaptor, "rule validId")
        stream_type = RewriteRuleSubtreeStream(self.adaptor, "rule type")
        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:179:2: ( 'typedef' type validId ';' -> ^( TYPEDEF type validId ) )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:179:4: 'typedef' type validId ';'
                string_literal92 = self.input.LT(1)
                self.match(self.input, 82, self.FOLLOW_82_in_typedef886)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_82.add(string_literal92)
                self.following.append(self.FOLLOW_type_in_typedef888)
                type93 = self.type()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_type.add(type93.tree)
                self.following.append(self.FOLLOW_validId_in_typedef890)
                validId94 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_validId.add(validId94.tree)
                char_literal95 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_typedef892)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_48.add(char_literal95)
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
                    # 180:3: -> ^( TYPEDEF type validId )
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:180:6: ^( TYPEDEF type validId )
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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:183:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal96 = None
        string_literal97 = None
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
        validId116 = None


        string_literal96_tree = None
        string_literal97_tree = None
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
        stream_92 = RewriteRuleTokenStream(self.adaptor, "token 92")
        stream_91 = RewriteRuleTokenStream(self.adaptor, "token 91")
        stream_90 = RewriteRuleTokenStream(self.adaptor, "token 90")
        stream_64 = RewriteRuleTokenStream(self.adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_83 = RewriteRuleTokenStream(self.adaptor, "token 83")
        stream_86 = RewriteRuleTokenStream(self.adaptor, "token 86")
        stream_87 = RewriteRuleTokenStream(self.adaptor, "token 87")
        stream_88 = RewriteRuleTokenStream(self.adaptor, "token 88")
        stream_84 = RewriteRuleTokenStream(self.adaptor, "token 84")
        stream_89 = RewriteRuleTokenStream(self.adaptor, "token 89")
        stream_85 = RewriteRuleTokenStream(self.adaptor, "token 85")

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:184:2: ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId )
                alt19 = 16
                LA19 = self.input.LA(1)
                if LA19 == 83:
                    alt19 = 1
                elif LA19 == 84:
                    alt19 = 2
                elif LA19 == 85:
                    alt19 = 3
                elif LA19 == 86:
                    alt19 = 4
                elif LA19 == 64:
                    alt19 = 5
                elif LA19 == 65:
                    LA19_6 = self.input.LA(2)

                    if (LA19_6 == 65) :
                        alt19 = 7
                    elif (LA19_6 == Identifier) :
                        alt19 = 6
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("183:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 6, self.input)

                        raise nvae

                elif LA19 == 87:
                    LA19_7 = self.input.LA(2)

                    if (LA19_7 == 65) :
                        LA19_16 = self.input.LA(3)

                        if (LA19_16 == 65) :
                            alt19 = 10
                        elif (LA19_16 == Identifier) :
                            alt19 = 9
                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            nvae = NoViableAltException("183:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 16, self.input)

                            raise nvae

                    elif (LA19_7 == 64) :
                        alt19 = 8
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("183:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 7, self.input)

                        raise nvae

                elif LA19 == 88:
                    alt19 = 11
                elif LA19 == 89:
                    alt19 = 12
                elif LA19 == 90:
                    alt19 = 13
                elif LA19 == 91:
                    alt19 = 14
                elif LA19 == 92:
                    alt19 = 15
                elif LA19 == Identifier:
                    alt19 = 16
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("183:1: type : ( 'boolean' -> BOOLEAN | 'void' -> VOID | 'string' -> STRING | 'octet' -> OCTET | 'short' -> SHORT | 'long' -> LONG | 'long' 'long' -> LONG_LONG | 'unsigned' 'short' -> UNSIGNED_SHORT | 'unsigned' 'long' -> UNSIGNED_LONG | 'unsigned' 'long' 'long' -> UNSIGNED_LONG_LONG | 'float' -> FLOAT | 'double' -> DOUBLE | 'char' -> CHAR | 'wchar' -> WCHAR | 'wstring' -> WSTRING | validId );", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:184:4: 'boolean'
                    string_literal96 = self.input.LT(1)
                    self.match(self.input, 83, self.FOLLOW_83_in_type915)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_83.add(string_literal96)
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
                        # 184:14: -> BOOLEAN
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(BOOLEAN, "BOOLEAN"))





                elif alt19 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:185:4: 'void'
                    string_literal97 = self.input.LT(1)
                    self.match(self.input, 84, self.FOLLOW_84_in_type924)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_84.add(string_literal97)
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
                        # 185:11: -> VOID
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(VOID, "VOID"))





                elif alt19 == 3:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:186:4: 'string'
                    string_literal98 = self.input.LT(1)
                    self.match(self.input, 85, self.FOLLOW_85_in_type933)
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
                        # 186:13: -> STRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(STRING, "STRING"))





                elif alt19 == 4:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:187:4: 'octet'
                    string_literal99 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_type942)
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
                        # 187:12: -> OCTET
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(OCTET, "OCTET"))





                elif alt19 == 5:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:188:4: 'short'
                    string_literal100 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_type951)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_64.add(string_literal100)
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
                        # 188:12: -> SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(SHORT, "SHORT"))





                elif alt19 == 6:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:189:4: 'long'
                    string_literal101 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type960)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal101)
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
                        # 189:11: -> LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG, "LONG"))





                elif alt19 == 7:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:190:4: 'long' 'long'
                    string_literal102 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type969)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal102)
                    string_literal103 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type971)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal103)
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
                        # 190:18: -> LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(LONG_LONG, "LONG_LONG"))





                elif alt19 == 8:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:191:4: 'unsigned' 'short'
                    string_literal104 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_type980)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_87.add(string_literal104)
                    string_literal105 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_type982)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_64.add(string_literal105)
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
                        # 191:23: -> UNSIGNED_SHORT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_SHORT, "UNSIGNED_SHORT"))





                elif alt19 == 9:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:192:4: 'unsigned' 'long'
                    string_literal106 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_type991)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_87.add(string_literal106)
                    string_literal107 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type993)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal107)
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
                        # 192:22: -> UNSIGNED_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG, "UNSIGNED_LONG"))





                elif alt19 == 10:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:193:4: 'unsigned' 'long' 'long'
                    string_literal108 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_type1002)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_87.add(string_literal108)
                    string_literal109 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type1004)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal109)
                    string_literal110 = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_type1006)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(string_literal110)
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
                        # 193:29: -> UNSIGNED_LONG_LONG
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(UNSIGNED_LONG_LONG, "UNSIGNED_LONG_LONG"))





                elif alt19 == 11:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:194:4: 'float'
                    string_literal111 = self.input.LT(1)
                    self.match(self.input, 88, self.FOLLOW_88_in_type1015)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_88.add(string_literal111)
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
                        # 194:12: -> FLOAT
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(FLOAT, "FLOAT"))





                elif alt19 == 12:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:195:4: 'double'
                    string_literal112 = self.input.LT(1)
                    self.match(self.input, 89, self.FOLLOW_89_in_type1024)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_89.add(string_literal112)
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
                        # 195:13: -> DOUBLE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(DOUBLE, "DOUBLE"))





                elif alt19 == 13:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:196:4: 'char'
                    string_literal113 = self.input.LT(1)
                    self.match(self.input, 90, self.FOLLOW_90_in_type1033)
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
                        # 196:11: -> CHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(CHAR, "CHAR"))





                elif alt19 == 14:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:197:4: 'wchar'
                    string_literal114 = self.input.LT(1)
                    self.match(self.input, 91, self.FOLLOW_91_in_type1042)
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
                        # 197:12: -> WCHAR
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WCHAR, "WCHAR"))





                elif alt19 == 15:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:198:4: 'wstring'
                    string_literal115 = self.input.LT(1)
                    self.match(self.input, 92, self.FOLLOW_92_in_type1051)
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
                        # 198:14: -> WSTRING
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(WSTRING, "WSTRING"))





                elif alt19 == 16:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:199:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_type1060)
                    validId116 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId116.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:202:1: mathExpr : mathMultDiv ;
    def mathExpr(self, ):

        retval = self.mathExpr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mathMultDiv117 = None



        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:203:2: ( mathMultDiv )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:203:4: mathMultDiv
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathMultDiv_in_mathExpr1071)
                mathMultDiv117 = self.mathMultDiv()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathMultDiv117.tree)



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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:206:1: mathMultDiv : mathAddSub ( ( '*' | '/' ) mathAddSub )? ;
    def mathMultDiv(self, ):

        retval = self.mathMultDiv_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set119 = None
        mathAddSub118 = None

        mathAddSub120 = None


        set119_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:2: ( mathAddSub ( ( '*' | '/' ) mathAddSub )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:4: mathAddSub ( ( '*' | '/' ) mathAddSub )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathAddSub_in_mathMultDiv1082)
                mathAddSub118 = self.mathAddSub()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathAddSub118.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:15: ( ( '*' | '/' ) mathAddSub )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((93 <= LA20_0 <= 94)) :
                    alt20 = 1
                if alt20 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:207:16: ( '*' | '/' ) mathAddSub
                    set119 = self.input.LT(1)
                    if (93 <= self.input.LA(1) <= 94):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set119))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_mathMultDiv1085
                            )
                        raise mse


                    self.following.append(self.FOLLOW_mathAddSub_in_mathMultDiv1091)
                    mathAddSub120 = self.mathAddSub()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathAddSub120.tree)






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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:210:1: mathAddSub : mathShift ( ( '+' | '-' ) mathShift )? ;
    def mathAddSub(self, ):

        retval = self.mathAddSub_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set122 = None
        mathShift121 = None

        mathShift123 = None


        set122_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:211:2: ( mathShift ( ( '+' | '-' ) mathShift )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:211:4: mathShift ( ( '+' | '-' ) mathShift )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathShift_in_mathAddSub1104)
                mathShift121 = self.mathShift()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathShift121.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:211:14: ( ( '+' | '-' ) mathShift )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((95 <= LA21_0 <= 96)) :
                    alt21 = 1
                if alt21 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:211:15: ( '+' | '-' ) mathShift
                    set122 = self.input.LT(1)
                    if (95 <= self.input.LA(1) <= 96):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set122))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_mathAddSub1107
                            )
                        raise mse


                    self.following.append(self.FOLLOW_mathShift_in_mathAddSub1113)
                    mathShift123 = self.mathShift()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathShift123.tree)






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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:214:1: mathShift : mathVar ( '<<' mathVar )? ;
    def mathShift(self, ):

        retval = self.mathShift_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal125 = None
        mathVar124 = None

        mathVar126 = None


        string_literal125_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:215:2: ( mathVar ( '<<' mathVar )? )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:215:4: mathVar ( '<<' mathVar )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_mathVar_in_mathShift1126)
                mathVar124 = self.mathVar()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, mathVar124.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:215:12: ( '<<' mathVar )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == 97) :
                    alt22 = 1
                if alt22 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:215:13: '<<' mathVar
                    string_literal125 = self.input.LT(1)
                    self.match(self.input, 97, self.FOLLOW_97_in_mathShift1129)
                    if self.failed:
                        return retval

                    string_literal125_tree = self.adaptor.createWithPayload(string_literal125)
                    self.adaptor.addChild(root_0, string_literal125_tree)

                    self.following.append(self.FOLLOW_mathVar_in_mathShift1131)
                    mathVar126 = self.mathVar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, mathVar126.tree)






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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:218:1: mathVar : ( Integer | validId );
    def mathVar(self, ):

        retval = self.mathVar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Integer127 = None
        validId128 = None


        Integer127_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:219:2: ( Integer | validId )
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

                    nvae = NoViableAltException("218:1: mathVar : ( Integer | validId );", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:219:4: Integer
                    root_0 = self.adaptor.nil()

                    Integer127 = self.input.LT(1)
                    self.match(self.input, Integer, self.FOLLOW_Integer_in_mathVar1144)
                    if self.failed:
                        return retval

                    Integer127_tree = self.adaptor.createWithPayload(Integer127)
                    self.adaptor.addChild(root_0, Integer127_tree)



                elif alt23 == 2:
                    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:220:4: validId
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_validId_in_mathVar1149)
                    validId128 = self.validId()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, validId128.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:223:1: validIdList : validId ( ',' validId )* ;
    def validIdList(self, ):

        retval = self.validIdList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal130 = None
        validId129 = None

        validId131 = None


        char_literal130_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:224:2: ( validId ( ',' validId )* )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:224:4: validId ( ',' validId )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_validId_in_validIdList1160)
                validId129 = self.validId()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, validId129.tree)
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:224:12: ( ',' validId )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 50) :
                        alt24 = 1


                    if alt24 == 1:
                        # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:224:13: ',' validId
                        char_literal130 = self.input.LT(1)
                        self.match(self.input, 50, self.FOLLOW_50_in_validIdList1163)
                        if self.failed:
                            return retval

                        char_literal130_tree = self.adaptor.createWithPayload(char_literal130)
                        self.adaptor.addChild(root_0, char_literal130_tree)

                        self.following.append(self.FOLLOW_validId_in_validIdList1165)
                        validId131 = self.validId()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, validId131.tree)


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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:227:1: validId : Identifier ;
    def validId(self, ):

        retval = self.validId_return()
        retval.start = self.input.LT(1)

        root_0 = None

        Identifier132 = None

        Identifier132_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:228:2: ( Identifier )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:228:4: Identifier
                root_0 = self.adaptor.nil()

                Identifier132 = self.input.LT(1)
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_validId1178)
                if self.failed:
                    return retval

                Identifier132_tree = self.adaptor.createWithPayload(Identifier132)
                self.adaptor.addChild(root_0, Identifier132_tree)




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
    # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:231:1: uuid : UUID ;
    def uuid(self, ):

        retval = self.uuid_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UUID133 = None

        UUID133_tree = None

        try:
            try:
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:232:2: ( UUID )
                # /home/visbrero/rev_control/git/pecobro/pecobro/xpidl/XPIDL.g:232:4: UUID
                root_0 = self.adaptor.nil()

                UUID133 = self.input.LT(1)
                self.match(self.input, UUID, self.FOLLOW_UUID_in_uuid1189)
                if self.failed:
                    return retval

                UUID133_tree = self.adaptor.createWithPayload(UUID133)
                self.adaptor.addChild(root_0, UUID133_tree)




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
        u"\1\44\1\72\3\uffff\1\62\1\72\1\62\1\44"
        )

    DFA9_max = DFA.unpack(
        u"\1\134\1\73\3\uffff\1\62\1\73\1\63\1\134"
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
 

    FOLLOW_toplevel_in_idlFile147 = frozenset([32, 33, 47, 49, 82])
    FOLLOW_EOF_in_idlFile150 = frozenset([1])
    FOLLOW_interface_in_toplevel162 = frozenset([1])
    FOLLOW_typedef_in_toplevel167 = frozenset([1])
    FOLLOW_nativeTypeDecl_in_toplevel172 = frozenset([1])
    FOLLOW_Include_in_toplevel177 = frozenset([1])
    FOLLOW_InlineCHeader_in_toplevel182 = frozenset([1])
    FOLLOW_47_in_interface200 = frozenset([36])
    FOLLOW_validId_in_interface202 = frozenset([48])
    FOLLOW_48_in_interface204 = frozenset([1])
    FOLLOW_49_in_interface220 = frozenset([34, 55, 56, 57, 58, 59])
    FOLLOW_interfaceModifier_in_interface223 = frozenset([50])
    FOLLOW_50_in_interface225 = frozenset([34, 55, 56, 57, 58, 59])
    FOLLOW_UUID_in_interface229 = frozenset([51])
    FOLLOW_51_in_interface231 = frozenset([47])
    FOLLOW_47_in_interface235 = frozenset([36])
    FOLLOW_validId_in_interface237 = frozenset([52, 53])
    FOLLOW_52_in_interface240 = frozenset([36])
    FOLLOW_validIdList_in_interface242 = frozenset([53])
    FOLLOW_53_in_interface249 = frozenset([36, 49, 54, 62, 64, 65, 66, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_interfaceBody_in_interface251 = frozenset([54])
    FOLLOW_54_in_interface253 = frozenset([48])
    FOLLOW_48_in_interface255 = frozenset([1])
    FOLLOW_interfaceModifier_in_interfaceModifierList325 = frozenset([1, 50])
    FOLLOW_50_in_interfaceModifierList328 = frozenset([55, 56, 57, 58, 59])
    FOLLOW_interfaceModifier_in_interfaceModifierList330 = frozenset([1, 50])
    FOLLOW_set_in_interfaceModifier0 = frozenset([1])
    FOLLOW_interfaceBodyItem_in_interfaceBody381 = frozenset([1, 36, 49, 62, 64, 65, 66, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_attribute_in_interfaceBodyItem393 = frozenset([1])
    FOLLOW_const_in_interfaceBodyItem398 = frozenset([1])
    FOLLOW_method_in_interfaceBodyItem403 = frozenset([1])
    FOLLOW_methodModifiers_in_method414 = frozenset([36, 64, 65, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_type_in_method417 = frozenset([36])
    FOLLOW_validId_in_method419 = frozenset([60])
    FOLLOW_60_in_method421 = frozenset([49, 67, 68, 69])
    FOLLOW_paramList_in_method423 = frozenset([61])
    FOLLOW_61_in_method425 = frozenset([48])
    FOLLOW_48_in_method427 = frozenset([1])
    FOLLOW_62_in_const463 = frozenset([36, 64, 65])
    FOLLOW_constType_in_const465 = frozenset([36])
    FOLLOW_validId_in_const467 = frozenset([63])
    FOLLOW_63_in_const469 = frozenset([35, 36])
    FOLLOW_mathExpr_in_const471 = frozenset([48])
    FOLLOW_48_in_const473 = frozenset([1])
    FOLLOW_64_in_constType498 = frozenset([1])
    FOLLOW_65_in_constType507 = frozenset([1])
    FOLLOW_validId_in_constType516 = frozenset([1])
    FOLLOW_methodModifiers_in_attribute527 = frozenset([66])
    FOLLOW_66_in_attribute530 = frozenset([36, 64, 65, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_type_in_attribute532 = frozenset([36])
    FOLLOW_validId_in_attribute534 = frozenset([48])
    FOLLOW_48_in_attribute536 = frozenset([1])
    FOLLOW_49_in_methodModifiers565 = frozenset([58, 59])
    FOLLOW_methodModifier_in_methodModifiers567 = frozenset([50])
    FOLLOW_50_in_methodModifiers570 = frozenset([58, 59])
    FOLLOW_methodModifier_in_methodModifiers572 = frozenset([50, 51])
    FOLLOW_51_in_methodModifiers576 = frozenset([1])
    FOLLOW_set_in_methodModifier0 = frozenset([1])
    FOLLOW_paramDecl_in_paramList610 = frozenset([50])
    FOLLOW_50_in_paramList613 = frozenset([49, 67, 68, 69])
    FOLLOW_paramDecl_in_paramList615 = frozenset([1, 50])
    FOLLOW_paramModifiersDecl_in_paramDecl635 = frozenset([67, 68, 69])
    FOLLOW_paramType_in_paramDecl638 = frozenset([36, 64, 65, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_type_in_paramDecl640 = frozenset([36])
    FOLLOW_validId_in_paramDecl642 = frozenset([1])
    FOLLOW_set_in_paramType0 = frozenset([1])
    FOLLOW_49_in_paramModifiersDecl695 = frozenset([62, 70, 71, 72, 73])
    FOLLOW_paramModifier_in_paramModifiersDecl697 = frozenset([50, 51])
    FOLLOW_50_in_paramModifiersDecl700 = frozenset([62, 70, 71, 72, 73])
    FOLLOW_paramModifier_in_paramModifiersDecl702 = frozenset([50, 51])
    FOLLOW_51_in_paramModifiersDecl706 = frozenset([1])
    FOLLOW_70_in_paramModifier725 = frozenset([1])
    FOLLOW_sizeIs_in_paramModifier730 = frozenset([1])
    FOLLOW_71_in_paramModifier735 = frozenset([1])
    FOLLOW_62_in_paramModifier740 = frozenset([1])
    FOLLOW_72_in_paramModifier745 = frozenset([1])
    FOLLOW_73_in_sizeIs757 = frozenset([60])
    FOLLOW_60_in_sizeIs759 = frozenset([36])
    FOLLOW_validId_in_sizeIs761 = frozenset([61])
    FOLLOW_61_in_sizeIs763 = frozenset([1])
    FOLLOW_nativeType_in_nativeTypeDecl775 = frozenset([48])
    FOLLOW_48_in_nativeTypeDecl777 = frozenset([1])
    FOLLOW_typeModifiersDecl_in_nativeType789 = frozenset([74])
    FOLLOW_74_in_nativeType791 = frozenset([36])
    FOLLOW_validId_in_nativeType793 = frozenset([1])
    FOLLOW_49_in_typeModifiersDecl816 = frozenset([75, 76, 77, 78, 79, 80, 81])
    FOLLOW_typeModifier_in_typeModifiersDecl818 = frozenset([50, 51])
    FOLLOW_50_in_typeModifiersDecl821 = frozenset([75, 76, 77, 78, 79, 80, 81])
    FOLLOW_typeModifier_in_typeModifiersDecl823 = frozenset([50, 51])
    FOLLOW_51_in_typeModifiersDecl827 = frozenset([1])
    FOLLOW_set_in_typeModifier0 = frozenset([1])
    FOLLOW_82_in_typedef886 = frozenset([36, 64, 65, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92])
    FOLLOW_type_in_typedef888 = frozenset([36])
    FOLLOW_validId_in_typedef890 = frozenset([48])
    FOLLOW_48_in_typedef892 = frozenset([1])
    FOLLOW_83_in_type915 = frozenset([1])
    FOLLOW_84_in_type924 = frozenset([1])
    FOLLOW_85_in_type933 = frozenset([1])
    FOLLOW_86_in_type942 = frozenset([1])
    FOLLOW_64_in_type951 = frozenset([1])
    FOLLOW_65_in_type960 = frozenset([1])
    FOLLOW_65_in_type969 = frozenset([65])
    FOLLOW_65_in_type971 = frozenset([1])
    FOLLOW_87_in_type980 = frozenset([64])
    FOLLOW_64_in_type982 = frozenset([1])
    FOLLOW_87_in_type991 = frozenset([65])
    FOLLOW_65_in_type993 = frozenset([1])
    FOLLOW_87_in_type1002 = frozenset([65])
    FOLLOW_65_in_type1004 = frozenset([65])
    FOLLOW_65_in_type1006 = frozenset([1])
    FOLLOW_88_in_type1015 = frozenset([1])
    FOLLOW_89_in_type1024 = frozenset([1])
    FOLLOW_90_in_type1033 = frozenset([1])
    FOLLOW_91_in_type1042 = frozenset([1])
    FOLLOW_92_in_type1051 = frozenset([1])
    FOLLOW_validId_in_type1060 = frozenset([1])
    FOLLOW_mathMultDiv_in_mathExpr1071 = frozenset([1])
    FOLLOW_mathAddSub_in_mathMultDiv1082 = frozenset([1, 93, 94])
    FOLLOW_set_in_mathMultDiv1085 = frozenset([35, 36])
    FOLLOW_mathAddSub_in_mathMultDiv1091 = frozenset([1])
    FOLLOW_mathShift_in_mathAddSub1104 = frozenset([1, 95, 96])
    FOLLOW_set_in_mathAddSub1107 = frozenset([35, 36])
    FOLLOW_mathShift_in_mathAddSub1113 = frozenset([1])
    FOLLOW_mathVar_in_mathShift1126 = frozenset([1, 97])
    FOLLOW_97_in_mathShift1129 = frozenset([35, 36])
    FOLLOW_mathVar_in_mathShift1131 = frozenset([1])
    FOLLOW_Integer_in_mathVar1144 = frozenset([1])
    FOLLOW_validId_in_mathVar1149 = frozenset([1])
    FOLLOW_validId_in_validIdList1160 = frozenset([1, 50])
    FOLLOW_50_in_validIdList1163 = frozenset([36])
    FOLLOW_validId_in_validIdList1165 = frozenset([1, 50])
    FOLLOW_Identifier_in_validId1178 = frozenset([1])
    FOLLOW_UUID_in_uuid1189 = frozenset([1])

