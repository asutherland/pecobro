# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-29 06:09:48

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LT=29
HexEscapeSequence=41
NEW=15
LineComment=58
REGEX=22
DecimalDigit=46
EOF=-1
PROP=20
HexDigit=47
RegularExpressionHacks=34
Identifier=33
SingleStringCharacter=39
XMLComment=31
Comment=57
OBJ=19
SingleEscapeCharacter=43
PROPREF=21
UnicodeLetter=53
ExponentPart=50
ARGS=5
EscapeCharacter=45
WhiteSpace=59
VARDEF=25
VARDEFS=26
IdentifierPart=52
INDEXREF=14
ARRAY=6
UnicodeCombiningMark=56
UnicodeDigit=54
NumericLiteral=32
RegularExpressionChars=35
UnicodeEscapeSequence=42
NULL=16
NUMBER=17
IdentifierStart=51
VEXPR=28
DoubleStringCharacter=38
DecimalLiteral=48
FUNCARGS=13
NSREF=18
DESCREF=10
TRUE=24
StringLiteral=30
RegularExpressionFirstChar=37
HexIntegerLiteral=49
FUNC=12
NonEscapeCharacter=44
ASSIGN=7
VARREF=27
CALL=8
DEFAULTNS=9
CharacterEscapeSequence=40
FALSE=11
EscapeSequence=36
UnicodeConnectorPunctuation=55
ANONYMOUS=4
STRING=23

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ANONYMOUS", "ARGS", "ARRAY", "ASSIGN", "CALL", "DEFAULTNS", "DESCREF", 
    "FALSE", "FUNC", "FUNCARGS", "INDEXREF", "NEW", "NULL", "NUMBER", "NSREF", 
    "OBJ", "PROP", "PROPREF", "REGEX", "STRING", "TRUE", "VARDEF", "VARDEFS", 
    "VARREF", "VEXPR", "LT", "StringLiteral", "XMLComment", "NumericLiteral", 
    "Identifier", "RegularExpressionHacks", "RegularExpressionChars", "EscapeSequence", 
    "RegularExpressionFirstChar", "DoubleStringCharacter", "SingleStringCharacter", 
    "CharacterEscapeSequence", "HexEscapeSequence", "UnicodeEscapeSequence", 
    "SingleEscapeCharacter", "NonEscapeCharacter", "EscapeCharacter", "DecimalDigit", 
    "HexDigit", "DecimalLiteral", "HexIntegerLiteral", "ExponentPart", "IdentifierStart", 
    "IdentifierPart", "UnicodeLetter", "UnicodeDigit", "UnicodeConnectorPunctuation", 
    "UnicodeCombiningMark", "Comment", "LineComment", "WhiteSpace", "'<'", 
    "'>'", "'/'", "':'", "'-'", "'='", "'{'", "'}'", "'function'", "'('", 
    "','", "')'", "'default'", "'xml'", "'namespace'", "';'", "'return'", 
    "'var'", "'const'", "'let'", "'['", "']'", "'if'", "'else'", "'do'", 
    "'while'", "'for'", "'each'", "'in'", "'continue'", "'break'", "'with'", 
    "'switch'", "'case'", "'throw'", "'try'", "'catch'", "'finally'", "'new'", 
    "'.'", "'*'", "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", 
    "'>>>='", "'&='", "'^='", "'|='", "'?'", "'||'", "'&&'", "'|'", "'^'", 
    "'&'", "'=='", "'!='", "'==='", "'!=='", "'<='", "'>='", "'instanceof'", 
    "'<<'", "'>>'", "'>>>'", "'+'", "'%'", "'delete'", "'void'", "'typeof'", 
    "'++'", "'--'", "'~'", "'!'", "'this'", "'get'", "'set'", "'null'", 
    "'true'", "'false'", "'#'"
]



class JavaScriptParser(Parser):
    grammarFileName = "/home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)
        self.ruleMemo = {}
        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )
        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )
        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )
        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
            )
        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
            )
        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
            )
        self.dfa40 = self.DFA40(
            self, 40,
            eot = self.DFA40_eot,
            eof = self.DFA40_eof,
            min = self.DFA40_min,
            max = self.DFA40_max,
            accept = self.DFA40_accept,
            special = self.DFA40_special,
            transition = self.DFA40_transition
            )
        self.dfa51 = self.DFA51(
            self, 51,
            eot = self.DFA51_eot,
            eof = self.DFA51_eof,
            min = self.DFA51_min,
            max = self.DFA51_max,
            accept = self.DFA51_accept,
            special = self.DFA51_special,
            transition = self.DFA51_transition
            )
        self.dfa54 = self.DFA54(
            self, 54,
            eot = self.DFA54_eot,
            eof = self.DFA54_eof,
            min = self.DFA54_min,
            max = self.DFA54_max,
            accept = self.DFA54_accept,
            special = self.DFA54_special,
            transition = self.DFA54_transition
            )
        self.dfa56 = self.DFA56(
            self, 56,
            eot = self.DFA56_eot,
            eof = self.DFA56_eof,
            min = self.DFA56_min,
            max = self.DFA56_max,
            accept = self.DFA56_accept,
            special = self.DFA56_special,
            transition = self.DFA56_transition
            )
        self.dfa62 = self.DFA62(
            self, 62,
            eot = self.DFA62_eot,
            eof = self.DFA62_eof,
            min = self.DFA62_min,
            max = self.DFA62_max,
            accept = self.DFA62_accept,
            special = self.DFA62_special,
            transition = self.DFA62_transition
            )
        self.dfa61 = self.DFA61(
            self, 61,
            eot = self.DFA61_eot,
            eof = self.DFA61_eof,
            min = self.DFA61_min,
            max = self.DFA61_max,
            accept = self.DFA61_accept,
            special = self.DFA61_special,
            transition = self.DFA61_transition
            )
        self.dfa67 = self.DFA67(
            self, 67,
            eot = self.DFA67_eot,
            eof = self.DFA67_eof,
            min = self.DFA67_min,
            max = self.DFA67_max,
            accept = self.DFA67_accept,
            special = self.DFA67_special,
            transition = self.DFA67_transition
            )
        self.dfa70 = self.DFA70(
            self, 70,
            eot = self.DFA70_eot,
            eof = self.DFA70_eof,
            min = self.DFA70_min,
            max = self.DFA70_max,
            accept = self.DFA70_accept,
            special = self.DFA70_special,
            transition = self.DFA70_transition
            )
        self.dfa76 = self.DFA76(
            self, 76,
            eot = self.DFA76_eot,
            eof = self.DFA76_eof,
            min = self.DFA76_min,
            max = self.DFA76_max,
            accept = self.DFA76_accept,
            special = self.DFA76_special,
            transition = self.DFA76_transition
            )
        self.dfa75 = self.DFA75(
            self, 75,
            eot = self.DFA75_eot,
            eof = self.DFA75_eof,
            min = self.DFA75_min,
            max = self.DFA75_max,
            accept = self.DFA75_accept,
            special = self.DFA75_special,
            transition = self.DFA75_transition
            )
        self.dfa81 = self.DFA81(
            self, 81,
            eot = self.DFA81_eot,
            eof = self.DFA81_eof,
            min = self.DFA81_min,
            max = self.DFA81_max,
            accept = self.DFA81_accept,
            special = self.DFA81_special,
            transition = self.DFA81_transition
            )
        self.dfa102 = self.DFA102(
            self, 102,
            eot = self.DFA102_eot,
            eof = self.DFA102_eof,
            min = self.DFA102_min,
            max = self.DFA102_max,
            accept = self.DFA102_accept,
            special = self.DFA102_special,
            transition = self.DFA102_transition
            )
        self.dfa105 = self.DFA105(
            self, 105,
            eot = self.DFA105_eot,
            eof = self.DFA105_eof,
            min = self.DFA105_min,
            max = self.DFA105_max,
            accept = self.DFA105_accept,
            special = self.DFA105_special,
            transition = self.DFA105_transition
            )
        self.dfa108 = self.DFA108(
            self, 108,
            eot = self.DFA108_eot,
            eof = self.DFA108_eof,
            min = self.DFA108_min,
            max = self.DFA108_max,
            accept = self.DFA108_accept,
            special = self.DFA108_special,
            transition = self.DFA108_transition
            )
        self.dfa141 = self.DFA141(
            self, 141,
            eot = self.DFA141_eot,
            eof = self.DFA141_eof,
            min = self.DFA141_min,
            max = self.DFA141_max,
            accept = self.DFA141_accept,
            special = self.DFA141_special,
            transition = self.DFA141_transition
            )
        self.dfa145 = self.DFA145(
            self, 145,
            eot = self.DFA145_eot,
            eof = self.DFA145_eof,
            min = self.DFA145_min,
            max = self.DFA145_max,
            accept = self.DFA145_accept,
            special = self.DFA145_special,
            transition = self.DFA145_transition
            )
        self.dfa144 = self.DFA144(
            self, 144,
            eot = self.DFA144_eot,
            eof = self.DFA144_eof,
            min = self.DFA144_min,
            max = self.DFA144_max,
            accept = self.DFA144_accept,
            special = self.DFA144_special,
            transition = self.DFA144_transition
            )
        self.dfa153 = self.DFA153(
            self, 153,
            eot = self.DFA153_eot,
            eof = self.DFA153_eof,
            min = self.DFA153_min,
            max = self.DFA153_max,
            accept = self.DFA153_accept,
            special = self.DFA153_special,
            transition = self.DFA153_transition
            )
        self.dfa157 = self.DFA157(
            self, 157,
            eot = self.DFA157_eot,
            eof = self.DFA157_eof,
            min = self.DFA157_min,
            max = self.DFA157_max,
            accept = self.DFA157_accept,
            special = self.DFA157_special,
            transition = self.DFA157_transition
            )
        self.dfa169 = self.DFA169(
            self, 169,
            eot = self.DFA169_eot,
            eof = self.DFA169_eof,
            min = self.DFA169_min,
            max = self.DFA169_max,
            accept = self.DFA169_accept,
            special = self.DFA169_special,
            transition = self.DFA169_transition
            )
        self.dfa200 = self.DFA200(
            self, 200,
            eot = self.DFA200_eot,
            eof = self.DFA200_eof,
            min = self.DFA200_min,
            max = self.DFA200_max,
            accept = self.DFA200_accept,
            special = self.DFA200_special,
            transition = self.DFA200_transition
            )
        self.dfa218 = self.DFA218(
            self, 218,
            eot = self.DFA218_eot,
            eof = self.DFA218_eof,
            min = self.DFA218_min,
            max = self.DFA218_max,
            accept = self.DFA218_accept,
            special = self.DFA218_special,
            transition = self.DFA218_transition
            )
        self.dfa224 = self.DFA224(
            self, 224,
            eot = self.DFA224_eot,
            eof = self.DFA224_eof,
            min = self.DFA224_min,
            max = self.DFA224_max,
            accept = self.DFA224_accept,
            special = self.DFA224_special,
            transition = self.DFA224_transition
            )
        self.dfa230 = self.DFA230(
            self, 230,
            eot = self.DFA230_eot,
            eof = self.DFA230_eof,
            min = self.DFA230_min,
            max = self.DFA230_max,
            accept = self.DFA230_accept,
            special = self.DFA230_special,
            transition = self.DFA230_transition
            )
        self.dfa236 = self.DFA236(
            self, 236,
            eot = self.DFA236_eot,
            eof = self.DFA236_eof,
            min = self.DFA236_min,
            max = self.DFA236_max,
            accept = self.DFA236_accept,
            special = self.DFA236_special,
            transition = self.DFA236_transition
            )
        self.dfa242 = self.DFA242(
            self, 242,
            eot = self.DFA242_eot,
            eof = self.DFA242_eof,
            min = self.DFA242_min,
            max = self.DFA242_max,
            accept = self.DFA242_accept,
            special = self.DFA242_special,
            transition = self.DFA242_transition
            )
        self.dfa248 = self.DFA248(
            self, 248,
            eot = self.DFA248_eot,
            eof = self.DFA248_eof,
            min = self.DFA248_min,
            max = self.DFA248_max,
            accept = self.DFA248_accept,
            special = self.DFA248_special,
            transition = self.DFA248_transition
            )
        self.dfa254 = self.DFA254(
            self, 254,
            eot = self.DFA254_eot,
            eof = self.DFA254_eof,
            min = self.DFA254_min,
            max = self.DFA254_max,
            accept = self.DFA254_accept,
            special = self.DFA254_special,
            transition = self.DFA254_transition
            )
        self.dfa260 = self.DFA260(
            self, 260,
            eot = self.DFA260_eot,
            eof = self.DFA260_eof,
            min = self.DFA260_min,
            max = self.DFA260_max,
            accept = self.DFA260_accept,
            special = self.DFA260_special,
            transition = self.DFA260_transition
            )
        self.dfa276 = self.DFA276(
            self, 276,
            eot = self.DFA276_eot,
            eof = self.DFA276_eof,
            min = self.DFA276_min,
            max = self.DFA276_max,
            accept = self.DFA276_accept,
            special = self.DFA276_special,
            transition = self.DFA276_transition
            )
        self.dfa280 = self.DFA280(
            self, 280,
            eot = self.DFA280_eot,
            eof = self.DFA280_eof,
            min = self.DFA280_min,
            max = self.DFA280_max,
            accept = self.DFA280_accept,
            special = self.DFA280_special,
            transition = self.DFA280_transition
            )
        self.dfa279 = self.DFA279(
            self, 279,
            eot = self.DFA279_eot,
            eof = self.DFA279_eof,
            min = self.DFA279_min,
            max = self.DFA279_max,
            accept = self.DFA279_accept,
            special = self.DFA279_special,
            transition = self.DFA279_transition
            )
        self.dfa288 = self.DFA288(
            self, 288,
            eot = self.DFA288_eot,
            eof = self.DFA288_eof,
            min = self.DFA288_min,
            max = self.DFA288_max,
            accept = self.DFA288_accept,
            special = self.DFA288_special,
            transition = self.DFA288_transition
            )
        self.dfa302 = self.DFA302(
            self, 302,
            eot = self.DFA302_eot,
            eof = self.DFA302_eof,
            min = self.DFA302_min,
            max = self.DFA302_max,
            accept = self.DFA302_accept,
            special = self.DFA302_special,
            transition = self.DFA302_transition
            )
        self.dfa327 = self.DFA327(
            self, 327,
            eot = self.DFA327_eot,
            eof = self.DFA327_eof,
            min = self.DFA327_min,
            max = self.DFA327_max,
            accept = self.DFA327_accept,
            special = self.DFA327_special,
            transition = self.DFA327_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class program_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start program
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:1: program : ( LT )* sourceElements ( LT )* EOF ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)
        program_StartIndex = self.input.index()
        root_0 = None

        LT1 = None
        LT3 = None
        EOF4 = None
        sourceElements2 = None


        LT1_tree = None
        LT3_tree = None
        EOF4_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 1):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:2: ( ( LT )* sourceElements ( LT )* EOF )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:4: ( LT )* sourceElements ( LT )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:6: ( LT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == LT) :
                        LA1_2 = self.input.LA(2)

                        if (self.synpred1()) :
                            alt1 = 1




                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT1 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program147)
                        if self.failed:
                            return retval


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_sourceElements_in_program151)
                sourceElements2 = self.sourceElements()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElements2.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT3 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program153)
                        if self.failed:
                            return retval


                    else:
                        break #loop2


                EOF4 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_program157)
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
            if self.backtracking > 0:
                self.memoize(self.input, 1, program_StartIndex)

            pass

        return retval

    # $ANTLR end program

    class sourceElements_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sourceElements
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
    def sourceElements(self, ):

        retval = self.sourceElements_return()
        retval.start = self.input.LT(1)
        sourceElements_StartIndex = self.input.index()
        root_0 = None

        LT6 = None
        sourceElement5 = None

        sourceElement7 = None


        LT6_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 2):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:2: ( sourceElement ( ( LT )* sourceElement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:4: sourceElement ( ( LT )* sourceElement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_sourceElement_in_sourceElements170)
                sourceElement5 = self.sourceElement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElement5.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:19: ( LT )* sourceElement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:21: ( LT )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if (LA3_0 == LT) :
                                LA3_2 = self.input.LA(2)

                                if (self.synpred3()) :
                                    alt3 = 1




                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT6 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements173)
                                if self.failed:
                                    return retval


                            else:
                                break #loop3


                        self.following.append(self.FOLLOW_sourceElement_in_sourceElements177)
                        sourceElement7 = self.sourceElement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, sourceElement7.tree)


                    else:
                        break #loop4





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 2, sourceElements_StartIndex)

            pass

        return retval

    # $ANTLR end sourceElements

    class sourceElement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start sourceElement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );
    def sourceElement(self, ):

        retval = self.sourceElement_return()
        retval.start = self.input.LT(1)
        sourceElement_StartIndex = self.input.index()
        root_0 = None

        functionDeclaration8 = None

        statement9 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 3):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:53:2: ( ( functionDeclaration )=> functionDeclaration | statement )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 68) :
                    LA5_1 = self.input.LA(2)

                    if (self.synpred5()) :
                        alt5 = 1
                    elif (True) :
                        alt5 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("52:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 1, self.input)

                        raise nvae

                elif ((LT <= LA5_0 <= RegularExpressionHacks) or LA5_0 == 60 or LA5_0 == 62 or LA5_0 == 64 or LA5_0 == 66 or LA5_0 == 69 or (72 <= LA5_0 <= 80) or LA5_0 == 82 or (84 <= LA5_0 <= 87) or (89 <= LA5_0 <= 92) or (94 <= LA5_0 <= 95) or LA5_0 == 98 or LA5_0 == 128 or (130 <= LA5_0 <= 142)) :
                    alt5 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("52:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:53:4: ( functionDeclaration )=> functionDeclaration
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionDeclaration_in_sourceElement196)
                    functionDeclaration8 = self.functionDeclaration()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:54:4: statement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statement_in_sourceElement201)
                    statement9 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement9.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 3, sourceElement_StartIndex)

            pass

        return retval

    # $ANTLR end sourceElement

    class xmlStartTag_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlStartTag
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:1: xmlStartTag options {backtrack=false; } : '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>' ;
    def xmlStartTag(self, ):

        retval = self.xmlStartTag_return()
        retval.start = self.input.LT(1)
        xmlStartTag_StartIndex = self.input.index()
        root_0 = None

        char_literal10 = None
        LT12 = None
        LT14 = None
        char_literal15 = None
        xmlTagName11 = None

        xmlAttribute13 = None


        char_literal10_tree = None
        LT12_tree = None
        LT14_tree = None
        char_literal15_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:2: ( '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:4: '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>'
                root_0 = self.adaptor.nil()

                char_literal10 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_xmlStartTag219)
                if self.failed:
                    return retval

                char_literal10_tree = self.adaptor.createWithPayload(char_literal10)
                self.adaptor.addChild(root_0, char_literal10_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlStartTag221)
                xmlTagName11 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName11.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:19: ( ( LT )* xmlAttribute )*
                while True: #loop7
                    alt7 = 2
                    alt7 = self.dfa7.predict(self.input)
                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:20: ( LT )* xmlAttribute
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:22: ( LT )*
                        while True: #loop6
                            alt6 = 2
                            LA6_0 = self.input.LA(1)

                            if (LA6_0 == LT) :
                                alt6 = 1


                            if alt6 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT12 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlStartTag224)
                                if self.failed:
                                    return retval


                            else:
                                break #loop6


                        self.following.append(self.FOLLOW_xmlAttribute_in_xmlStartTag228)
                        xmlAttribute13 = self.xmlAttribute()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, xmlAttribute13.tree)


                    else:
                        break #loop7


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:42: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT14 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_xmlStartTag232)
                        if self.failed:
                            return retval


                    else:
                        break #loop8


                char_literal15 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_xmlStartTag236)
                if self.failed:
                    return retval

                char_literal15_tree = self.adaptor.createWithPayload(char_literal15)
                self.adaptor.addChild(root_0, char_literal15_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 4, xmlStartTag_StartIndex)

            pass

        return retval

    # $ANTLR end xmlStartTag

    class xmlEndTag_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlEndTag
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:1: xmlEndTag options {backtrack=false; } : '<' '/' xmlTagName '>' ;
    def xmlEndTag(self, ):

        retval = self.xmlEndTag_return()
        retval.start = self.input.LT(1)
        xmlEndTag_StartIndex = self.input.index()
        root_0 = None

        char_literal16 = None
        char_literal17 = None
        char_literal19 = None
        xmlTagName18 = None


        char_literal16_tree = None
        char_literal17_tree = None
        char_literal19_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:2: ( '<' '/' xmlTagName '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: '<' '/' xmlTagName '>'
                root_0 = self.adaptor.nil()

                char_literal16 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_xmlEndTag254)
                if self.failed:
                    return retval

                char_literal16_tree = self.adaptor.createWithPayload(char_literal16)
                self.adaptor.addChild(root_0, char_literal16_tree)

                char_literal17 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_xmlEndTag256)
                if self.failed:
                    return retval

                char_literal17_tree = self.adaptor.createWithPayload(char_literal17)
                self.adaptor.addChild(root_0, char_literal17_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlEndTag258)
                xmlTagName18 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName18.tree)
                char_literal19 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_xmlEndTag260)
                if self.failed:
                    return retval

                char_literal19_tree = self.adaptor.createWithPayload(char_literal19)
                self.adaptor.addChild(root_0, char_literal19_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 5, xmlEndTag_StartIndex)

            pass

        return retval

    # $ANTLR end xmlEndTag

    class xmlEmptyTag_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlEmptyTag
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:1: xmlEmptyTag options {backtrack=false; } : '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>' ;
    def xmlEmptyTag(self, ):

        retval = self.xmlEmptyTag_return()
        retval.start = self.input.LT(1)
        xmlEmptyTag_StartIndex = self.input.index()
        root_0 = None

        char_literal20 = None
        LT22 = None
        LT24 = None
        char_literal25 = None
        char_literal26 = None
        xmlTagName21 = None

        xmlAttribute23 = None


        char_literal20_tree = None
        LT22_tree = None
        LT24_tree = None
        char_literal25_tree = None
        char_literal26_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:2: ( '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:4: '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>'
                root_0 = self.adaptor.nil()

                char_literal20 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_xmlEmptyTag278)
                if self.failed:
                    return retval

                char_literal20_tree = self.adaptor.createWithPayload(char_literal20)
                self.adaptor.addChild(root_0, char_literal20_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlEmptyTag280)
                xmlTagName21 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName21.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:19: ( ( LT )* xmlAttribute )*
                while True: #loop10
                    alt10 = 2
                    alt10 = self.dfa10.predict(self.input)
                    if alt10 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:20: ( LT )* xmlAttribute
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:22: ( LT )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == LT) :
                                alt9 = 1


                            if alt9 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT22 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlEmptyTag283)
                                if self.failed:
                                    return retval


                            else:
                                break #loop9


                        self.following.append(self.FOLLOW_xmlAttribute_in_xmlEmptyTag287)
                        xmlAttribute23 = self.xmlAttribute()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, xmlAttribute23.tree)


                    else:
                        break #loop10


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:42: ( LT )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == LT) :
                        alt11 = 1


                    if alt11 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT24 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_xmlEmptyTag291)
                        if self.failed:
                            return retval


                    else:
                        break #loop11


                char_literal25 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_xmlEmptyTag295)
                if self.failed:
                    return retval

                char_literal25_tree = self.adaptor.createWithPayload(char_literal25)
                self.adaptor.addChild(root_0, char_literal25_tree)

                char_literal26 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_xmlEmptyTag297)
                if self.failed:
                    return retval

                char_literal26_tree = self.adaptor.createWithPayload(char_literal26)
                self.adaptor.addChild(root_0, char_literal26_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 6, xmlEmptyTag_StartIndex)

            pass

        return retval

    # $ANTLR end xmlEmptyTag

    class xmlTagName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlTagName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:72:1: xmlTagName options {backtrack=false; } : identifier ( ( ':' | '-' ) identifier )* ;
    def xmlTagName(self, ):

        retval = self.xmlTagName_return()
        retval.start = self.input.LT(1)
        xmlTagName_StartIndex = self.input.index()
        root_0 = None

        set28 = None
        identifier27 = None

        identifier29 = None


        set28_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:2: ( identifier ( ( ':' | '-' ) identifier )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:4: identifier ( ( ':' | '-' ) identifier )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_xmlTagName315)
                identifier27 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier27.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:15: ( ( ':' | '-' ) identifier )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((63 <= LA12_0 <= 64)) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:17: ( ':' | '-' ) identifier
                        set28 = self.input.LT(1)
                        if (63 <= self.input.LA(1) <= 64):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set28))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_xmlTagName319
                                )
                            raise mse


                        self.following.append(self.FOLLOW_identifier_in_xmlTagName325)
                        identifier29 = self.identifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, identifier29.tree)


                    else:
                        break #loop12





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 7, xmlTagName_StartIndex)

            pass

        return retval

    # $ANTLR end xmlTagName

    class xmlAttribute_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlAttribute
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:1: xmlAttribute options {backtrack=false; } : xmlAttributeName '=' xmlAttributeValue ;
    def xmlAttribute(self, ):

        retval = self.xmlAttribute_return()
        retval.start = self.input.LT(1)
        xmlAttribute_StartIndex = self.input.index()
        root_0 = None

        char_literal31 = None
        xmlAttributeName30 = None

        xmlAttributeValue32 = None


        char_literal31_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:79:2: ( xmlAttributeName '=' xmlAttributeValue )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:79:4: xmlAttributeName '=' xmlAttributeValue
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_xmlAttributeName_in_xmlAttribute345)
                xmlAttributeName30 = self.xmlAttributeName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlAttributeName30.tree)
                char_literal31 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_xmlAttribute347)
                if self.failed:
                    return retval

                char_literal31_tree = self.adaptor.createWithPayload(char_literal31)
                self.adaptor.addChild(root_0, char_literal31_tree)

                self.following.append(self.FOLLOW_xmlAttributeValue_in_xmlAttribute349)
                xmlAttributeValue32 = self.xmlAttributeValue()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlAttributeValue32.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 8, xmlAttribute_StartIndex)

            pass

        return retval

    # $ANTLR end xmlAttribute

    class xmlAttributeName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlAttributeName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:83:1: xmlAttributeName options {backtrack=false; } : identifier ( ( ':' | '-' ) identifier )* ;
    def xmlAttributeName(self, ):

        retval = self.xmlAttributeName_return()
        retval.start = self.input.LT(1)
        xmlAttributeName_StartIndex = self.input.index()
        root_0 = None

        set34 = None
        identifier33 = None

        identifier35 = None


        set34_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:2: ( identifier ( ( ':' | '-' ) identifier )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:4: identifier ( ( ':' | '-' ) identifier )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_xmlAttributeName368)
                identifier33 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier33.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:15: ( ( ':' | '-' ) identifier )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((63 <= LA13_0 <= 64)) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:17: ( ':' | '-' ) identifier
                        set34 = self.input.LT(1)
                        if (63 <= self.input.LA(1) <= 64):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set34))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_xmlAttributeName372
                                )
                            raise mse


                        self.following.append(self.FOLLOW_identifier_in_xmlAttributeName378)
                        identifier35 = self.identifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, identifier35.tree)


                    else:
                        break #loop13





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 9, xmlAttributeName_StartIndex)

            pass

        return retval

    # $ANTLR end xmlAttributeName

    class xmlAttributeValue_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlAttributeValue
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:88:1: xmlAttributeValue options {backtrack=false; } : ( ( '{' )=> e4xSplice | StringLiteral );
    def xmlAttributeValue(self, ):

        retval = self.xmlAttributeValue_return()
        retval.start = self.input.LT(1)
        xmlAttributeValue_StartIndex = self.input.index()
        root_0 = None

        StringLiteral37 = None
        e4xSplice36 = None


        StringLiteral37_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:2: ( ( '{' )=> e4xSplice | StringLiteral )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 66) and (self.synpred16()):
                    alt14 = 1
                elif (LA14_0 == StringLiteral) :
                    alt14 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("88:1: xmlAttributeValue options {backtrack=false; } : ( ( '{' )=> e4xSplice | StringLiteral );", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:4: ( '{' )=> e4xSplice
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_e4xSplice_in_xmlAttributeValue403)
                    e4xSplice36 = self.e4xSplice()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, e4xSplice36.tree)


                elif alt14 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral37 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_xmlAttributeValue408)
                    if self.failed:
                        return retval

                    StringLiteral37_tree = self.adaptor.createWithPayload(StringLiteral37)
                    self.adaptor.addChild(root_0, StringLiteral37_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 10, xmlAttributeValue_StartIndex)

            pass

        return retval

    # $ANTLR end xmlAttributeValue

    class e4xSplice_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start e4xSplice
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:1: e4xSplice options {backtrack=false; } : '{' expression '}' ;
    def e4xSplice(self, ):

        retval = self.e4xSplice_return()
        retval.start = self.input.LT(1)
        e4xSplice_StartIndex = self.input.index()
        root_0 = None

        char_literal38 = None
        char_literal40 = None
        expression39 = None


        char_literal38_tree = None
        char_literal40_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:96:2: ( '{' expression '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:96:4: '{' expression '}'
                root_0 = self.adaptor.nil()

                char_literal38 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_e4xSplice426)
                if self.failed:
                    return retval

                char_literal38_tree = self.adaptor.createWithPayload(char_literal38)
                self.adaptor.addChild(root_0, char_literal38_tree)

                self.following.append(self.FOLLOW_expression_in_e4xSplice428)
                expression39 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression39.tree)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_e4xSplice430)
                if self.failed:
                    return retval

                char_literal40_tree = self.adaptor.createWithPayload(char_literal40)
                self.adaptor.addChild(root_0, char_literal40_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 11, e4xSplice_StartIndex)

            pass

        return retval

    # $ANTLR end e4xSplice

    class xmlPayload_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlPayload
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:1: xmlPayload : ( xmlEndTag | xmlEmptyTag | xmlStartTag | e4xSplice | XMLComment );
    def xmlPayload(self, ):

        retval = self.xmlPayload_return()
        retval.start = self.input.LT(1)
        xmlPayload_StartIndex = self.input.index()
        root_0 = None

        XMLComment45 = None
        xmlEndTag41 = None

        xmlEmptyTag42 = None

        xmlStartTag43 = None

        e4xSplice44 = None


        XMLComment45_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:108:2: ( xmlEndTag | xmlEmptyTag | xmlStartTag | e4xSplice | XMLComment )
                alt15 = 5
                alt15 = self.dfa15.predict(self.input)
                if alt15 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:108:4: xmlEndTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlEndTag_in_xmlPayload444)
                    xmlEndTag41 = self.xmlEndTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlEndTag41.tree)


                elif alt15 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:4: xmlEmptyTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlEmptyTag_in_xmlPayload449)
                    xmlEmptyTag42 = self.xmlEmptyTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlEmptyTag42.tree)


                elif alt15 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:4: xmlStartTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlStartTag_in_xmlPayload454)
                    xmlStartTag43 = self.xmlStartTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlStartTag43.tree)


                elif alt15 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:4: e4xSplice
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_e4xSplice_in_xmlPayload459)
                    e4xSplice44 = self.e4xSplice()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, e4xSplice44.tree)


                elif alt15 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:112:4: XMLComment
                    root_0 = self.adaptor.nil()

                    XMLComment45 = self.input.LT(1)
                    self.match(self.input, XMLComment, self.FOLLOW_XMLComment_in_xmlPayload464)
                    if self.failed:
                        return retval

                    XMLComment45_tree = self.adaptor.createWithPayload(XMLComment45)
                    self.adaptor.addChild(root_0, XMLComment45_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 12, xmlPayload_StartIndex)

            pass

        return retval

    # $ANTLR end xmlPayload

    class xmlLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start xmlLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:115:1: xmlLiteral : ( ( LT )* xmlPayload )+ ;
    def xmlLiteral(self, ):

        retval = self.xmlLiteral_return()
        retval.start = self.input.LT(1)
        xmlLiteral_StartIndex = self.input.index()
        root_0 = None

        LT46 = None
        xmlPayload47 = None


        LT46_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:2: ( ( ( LT )* xmlPayload )+ )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:4: ( ( LT )* xmlPayload )+
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:4: ( ( LT )* xmlPayload )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17 = self.input.LA(1)
                    if LA17 == LT:
                        LA17_1 = self.input.LA(2)

                        if (self.synpred22()) :
                            alt17 = 1


                    elif LA17 == 60:
                        LA17_11 = self.input.LA(2)

                        if (self.synpred22()) :
                            alt17 = 1


                    elif LA17 == XMLComment or LA17 == 66:
                        alt17 = 1

                    if alt17 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:5: ( LT )* xmlPayload
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:5: ( LT )*
                        while True: #loop16
                            alt16 = 2
                            LA16_0 = self.input.LA(1)

                            if (LA16_0 == LT) :
                                alt16 = 1


                            if alt16 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT46 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlLiteral477)
                                if self.failed:
                                    return retval

                                LT46_tree = self.adaptor.createWithPayload(LT46)
                                self.adaptor.addChild(root_0, LT46_tree)



                            else:
                                break #loop16


                        self.following.append(self.FOLLOW_xmlPayload_in_xmlLiteral480)
                        xmlPayload47 = self.xmlPayload()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, xmlPayload47.tree)


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 13, xmlLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end xmlLiteral

    class functionDeclaration_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start functionDeclaration
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:122:1: functionDeclaration : 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) ;
    def functionDeclaration(self, ):

        retval = self.functionDeclaration_return()
        retval.start = self.input.LT(1)
        functionDeclaration_StartIndex = self.input.index()
        root_0 = None

        string_literal48 = None
        LT49 = None
        LT51 = None
        LT53 = None
        identifier50 = None

        formalParameterList52 = None

        statementBlock54 = None


        string_literal48_tree = None
        LT49_tree = None
        LT51_tree = None
        LT53_tree = None
        stream_68 = RewriteRuleTokenStream(self.adaptor, "token 68")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                string_literal48 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_functionDeclaration495)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_68.add(string_literal48)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:15: ( LT )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == LT) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT49 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration497)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT49)


                    else:
                        break #loop18


                self.following.append(self.FOLLOW_identifier_in_functionDeclaration500)
                identifier50 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier50.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:30: ( LT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == LT) :
                        alt19 = 1


                    if alt19 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT51 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration502)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT51)


                    else:
                        break #loop19


                self.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration505)
                formalParameterList52 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList52.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:54: ( LT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == LT) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT53 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration507)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT53)


                    else:
                        break #loop20


                self.following.append(self.FOLLOW_statementBlock_in_functionDeclaration510)
                statementBlock54 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_statementBlock.add(statementBlock54.tree)
                # AST Rewrite
                # elements: statementBlock, formalParameterList, identifier
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
                    # 124:3: -> ^( FUNC identifier formalParameterList statementBlock )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:124:6: ^( FUNC identifier formalParameterList statementBlock )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    self.adaptor.addChild(root_1, stream_formalParameterList.next())
                    self.adaptor.addChild(root_1, stream_statementBlock.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 14, functionDeclaration_StartIndex)

            pass

        return retval

    # $ANTLR end functionDeclaration

    class functionExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start functionExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* expression -> ^( FUNC ANONYMOUS[$func] formalParameterList expression ) );
    def functionExpression(self, ):

        retval = self.functionExpression_return()
        retval.start = self.input.LT(1)
        functionExpression_StartIndex = self.input.index()
        root_0 = None

        func = None
        string_literal55 = None
        LT56 = None
        LT58 = None
        LT60 = None
        LT62 = None
        LT64 = None
        LT66 = None
        LT68 = None
        identifier57 = None

        formalParameterList59 = None

        statementBlock61 = None

        formalParameterList63 = None

        statementBlock65 = None

        formalParameterList67 = None

        expression69 = None


        func_tree = None
        string_literal55_tree = None
        LT56_tree = None
        LT58_tree = None
        LT60_tree = None
        LT62_tree = None
        LT64_tree = None
        LT66_tree = None
        LT68_tree = None
        stream_68 = RewriteRuleTokenStream(self.adaptor, "token 68")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_expression = RewriteRuleSubtreeStream(self.adaptor, "rule expression")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* expression -> ^( FUNC ANONYMOUS[$func] formalParameterList expression ) )
                alt28 = 3
                LA28_0 = self.input.LA(1)

                if (LA28_0 == 68) :
                    LA28_1 = self.input.LA(2)

                    if (self.synpred29()) :
                        alt28 = 1
                    elif (self.synpred32()) :
                        alt28 = 2
                    elif (True) :
                        alt28 = 3
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("127:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* expression -> ^( FUNC ANONYMOUS[$func] formalParameterList expression ) );", 28, 1, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("127:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* expression -> ^( FUNC ANONYMOUS[$func] formalParameterList expression ) );", 28, 0, self.input)

                    raise nvae

                if alt28 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                    string_literal55 = self.input.LT(1)
                    self.match(self.input, 68, self.FOLLOW_68_in_functionExpression536)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_68.add(string_literal55)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:15: ( LT )*
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == LT) :
                            alt21 = 1


                        if alt21 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT56 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression538)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT56)


                        else:
                            break #loop21


                    self.following.append(self.FOLLOW_identifier_in_functionExpression541)
                    identifier57 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier57.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:30: ( LT )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == LT) :
                            alt22 = 1


                        if alt22 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT58 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression543)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT58)


                        else:
                            break #loop22


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression546)
                    formalParameterList59 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList59.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:54: ( LT )*
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == LT) :
                            alt23 = 1


                        if alt23 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT60 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression548)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT60)


                        else:
                            break #loop23


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression551)
                    statementBlock61 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock61.tree)
                    # AST Rewrite
                    # elements: statementBlock, formalParameterList, identifier
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
                        # 129:3: -> ^( FUNC identifier formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:6: ^( FUNC identifier formalParameterList statementBlock )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_statementBlock.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt28 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:4: func= 'function' ( LT )* formalParameterList ( LT )* statementBlock
                    func = self.input.LT(1)
                    self.match(self.input, 68, self.FOLLOW_68_in_functionExpression572)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_68.add(func)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:20: ( LT )*
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == LT) :
                            alt24 = 1


                        if alt24 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT62 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression574)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT62)


                        else:
                            break #loop24


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression577)
                    formalParameterList63 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList63.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:44: ( LT )*
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == LT) :
                            alt25 = 1


                        if alt25 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT64 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression579)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT64)


                        else:
                            break #loop25


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression582)
                    statementBlock65 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock65.tree)
                    # AST Rewrite
                    # elements: formalParameterList, statementBlock
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
                        # 131:3: -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:6: ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, self.adaptor.createFromToken(ANONYMOUS, func))
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_statementBlock.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt28 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:4: func= 'function' ( LT )* formalParameterList ( LT )* expression
                    func = self.input.LT(1)
                    self.match(self.input, 68, self.FOLLOW_68_in_functionExpression604)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_68.add(func)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:20: ( LT )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == LT) :
                            alt26 = 1


                        if alt26 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT66 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression606)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT66)


                        else:
                            break #loop26


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression609)
                    formalParameterList67 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList67.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:44: ( LT )*
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == LT) :
                            LA27_2 = self.input.LA(2)

                            if (self.synpred34()) :
                                alt27 = 1




                        if alt27 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT68 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression611)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT68)


                        else:
                            break #loop27


                    self.following.append(self.FOLLOW_expression_in_functionExpression614)
                    expression69 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_expression.add(expression69.tree)
                    # AST Rewrite
                    # elements: formalParameterList, expression
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
                        # 133:3: -> ^( FUNC ANONYMOUS[$func] formalParameterList expression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:6: ^( FUNC ANONYMOUS[$func] formalParameterList expression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, self.adaptor.createFromToken(ANONYMOUS, func))
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_expression.next())

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 15, functionExpression_StartIndex)

            pass

        return retval

    # $ANTLR end functionExpression

    class formalParameterList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start formalParameterList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' -> ^( FUNCARGS ( identifier )* ) ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal70 = None
        LT71 = None
        LT73 = None
        char_literal74 = None
        LT75 = None
        LT77 = None
        char_literal78 = None
        identifier72 = None

        identifier76 = None


        char_literal70_tree = None
        LT71_tree = None
        LT73_tree = None
        char_literal74_tree = None
        LT75_tree = None
        LT77_tree = None
        char_literal78_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self.adaptor, "token 71")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' -> ^( FUNCARGS ( identifier )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                char_literal70 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_formalParameterList641)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal70)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt33 = 2
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:9: ( LT )*
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == LT) :
                            alt29 = 1


                        if alt29 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT71 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList644)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT71)


                        else:
                            break #loop29


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList647)
                    identifier72 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier72.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:24: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop32
                        alt32 = 2
                        alt32 = self.dfa32.predict(self.input)
                        if alt32 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:25: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:25: ( LT )*
                            while True: #loop30
                                alt30 = 2
                                LA30_0 = self.input.LA(1)

                                if (LA30_0 == LT) :
                                    alt30 = 1


                                if alt30 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT73 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList650)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT73)


                                else:
                                    break #loop30


                            char_literal74 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_formalParameterList653)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal74)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:33: ( LT )*
                            while True: #loop31
                                alt31 = 2
                                LA31_0 = self.input.LA(1)

                                if (LA31_0 == LT) :
                                    alt31 = 1


                                if alt31 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT75 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList655)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT75)


                                else:
                                    break #loop31


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList658)
                            identifier76 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_identifier.add(identifier76.tree)


                        else:
                            break #loop32





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:52: ( LT )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == LT) :
                        alt34 = 1


                    if alt34 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT77 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList664)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT77)


                    else:
                        break #loop34


                char_literal78 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_formalParameterList667)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_71.add(char_literal78)
                # AST Rewrite
                # elements: identifier
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
                    # 138:3: -> ^( FUNCARGS ( identifier )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:6: ^( FUNCARGS ( identifier )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNCARGS, "FUNCARGS"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:17: ( identifier )*
                    while stream_identifier.hasNext():
                        self.adaptor.addChild(root_1, stream_identifier.next())


                    stream_identifier.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 16, formalParameterList_StartIndex)

            pass

        return retval

    # $ANTLR end formalParameterList

    class statement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        statementBlock79 = None

        variableStatement80 = None

        emptyStatement81 = None

        expressionStatement82 = None

        ifStatement83 = None

        iterationStatement84 = None

        continueStatement85 = None

        breakStatement86 = None

        returnStatement87 = None

        withStatement88 = None

        letStatement89 = None

        labelledStatement90 = None

        switchStatement91 = None

        throwStatement92 = None

        tryStatement93 = None

        defaultXmlNamespaceStatement94 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement )
                alt35 = 16
                LA35 = self.input.LA(1)
                if LA35 == 66:
                    LA35_1 = self.input.LA(2)

                    if (self.synpred41()) :
                        alt35 = 1
                    elif (self.synpred44()) :
                        alt35 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 35, 1, self.input)

                        raise nvae

                elif LA35 == 77 or LA35 == 78:
                    alt35 = 2
                elif LA35 == 79:
                    LA35_4 = self.input.LA(2)

                    if (self.synpred42()) :
                        alt35 = 2
                    elif (self.synpred51()) :
                        alt35 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 35, 4, self.input)

                        raise nvae

                elif LA35 == 75:
                    alt35 = 3
                elif LA35 == LT or LA35 == StringLiteral or LA35 == XMLComment or LA35 == NumericLiteral or LA35 == RegularExpressionHacks or LA35 == 60 or LA35 == 62 or LA35 == 64 or LA35 == 68 or LA35 == 69 or LA35 == 80 or LA35 == 98 or LA35 == 128 or LA35 == 130 or LA35 == 131 or LA35 == 132 or LA35 == 133 or LA35 == 134 or LA35 == 135 or LA35 == 136 or LA35 == 137 or LA35 == 140 or LA35 == 141 or LA35 == 142:
                    alt35 = 4
                elif LA35 == 72:
                    LA35_10 = self.input.LA(2)

                    if (self.synpred44()) :
                        alt35 = 4
                    elif (self.synpred52()) :
                        alt35 = 12
                    elif (True) :
                        alt35 = 16
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 35, 10, self.input)

                        raise nvae

                elif LA35 == 82:
                    alt35 = 5
                elif LA35 == 84 or LA35 == 85 or LA35 == 86:
                    alt35 = 6
                elif LA35 == 89:
                    alt35 = 7
                elif LA35 == 90:
                    alt35 = 8
                elif LA35 == 76:
                    alt35 = 9
                elif LA35 == 91:
                    alt35 = 10
                elif LA35 == 92:
                    alt35 = 13
                elif LA35 == 94:
                    alt35 = 14
                elif LA35 == 95:
                    alt35 = 15
                elif LA35 == Identifier or LA35 == 73 or LA35 == 74 or LA35 == 87 or LA35 == 138 or LA35 == 139:
                    LA35_34 = self.input.LA(2)

                    if (self.synpred44()) :
                        alt35 = 4
                    elif (self.synpred52()) :
                        alt35 = 12
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 35, 34, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("142:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | letStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 35, 0, self.input)

                    raise nvae

                if alt35 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement690)
                    statementBlock79 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock79.tree)


                elif alt35 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement695)
                    variableStatement80 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement80.tree)


                elif alt35 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement700)
                    emptyStatement81 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement81.tree)


                elif alt35 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement705)
                    expressionStatement82 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement82.tree)


                elif alt35 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:147:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement710)
                    ifStatement83 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement83.tree)


                elif alt35 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:148:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement715)
                    iterationStatement84 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement84.tree)


                elif alt35 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement720)
                    continueStatement85 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement85.tree)


                elif alt35 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement725)
                    breakStatement86 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement86.tree)


                elif alt35 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement730)
                    returnStatement87 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement87.tree)


                elif alt35 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:152:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement735)
                    withStatement88 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement88.tree)


                elif alt35 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:4: letStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_letStatement_in_statement740)
                    letStatement89 = self.letStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, letStatement89.tree)


                elif alt35 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement745)
                    labelledStatement90 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement90.tree)


                elif alt35 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement750)
                    switchStatement91 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement91.tree)


                elif alt35 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement755)
                    throwStatement92 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement92.tree)


                elif alt35 == 15:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:157:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement760)
                    tryStatement93 = self.tryStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, tryStatement93.tree)


                elif alt35 == 16:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:4: defaultXmlNamespaceStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_defaultXmlNamespaceStatement_in_statement765)
                    defaultXmlNamespaceStatement94 = self.defaultXmlNamespaceStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultXmlNamespaceStatement94.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 17, statement_StartIndex)

            pass

        return retval

    # $ANTLR end statement

    class defaultXmlNamespaceStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start defaultXmlNamespaceStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:161:1: defaultXmlNamespaceStatement : 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) ;
    def defaultXmlNamespaceStatement(self, ):

        retval = self.defaultXmlNamespaceStatement_return()
        retval.start = self.input.LT(1)
        defaultXmlNamespaceStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal95 = None
        string_literal96 = None
        string_literal97 = None
        LT98 = None
        char_literal99 = None
        LT100 = None
        LT102 = None
        char_literal103 = None
        identifier101 = None


        string_literal95_tree = None
        string_literal96_tree = None
        string_literal97_tree = None
        LT98_tree = None
        char_literal99_tree = None
        LT100_tree = None
        LT102_tree = None
        char_literal103_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_72 = RewriteRuleTokenStream(self.adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self.adaptor, "token 73")
        stream_74 = RewriteRuleTokenStream(self.adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self.adaptor, "token 75")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:2: ( 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:4: 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' )
                string_literal95 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_defaultXmlNamespaceStatement776)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_72.add(string_literal95)
                string_literal96 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_defaultXmlNamespaceStatement778)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_73.add(string_literal96)
                string_literal97 = self.input.LT(1)
                self.match(self.input, 74, self.FOLLOW_74_in_defaultXmlNamespaceStatement780)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_74.add(string_literal97)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:32: ( LT )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == LT) :
                        alt36 = 1


                    if alt36 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT98 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement782)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT98)


                    else:
                        break #loop36


                char_literal99 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_defaultXmlNamespaceStatement785)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal99)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:40: ( LT )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == LT) :
                        alt37 = 1


                    if alt37 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT100 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement787)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT100)


                    else:
                        break #loop37


                self.following.append(self.FOLLOW_identifier_in_defaultXmlNamespaceStatement790)
                identifier101 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier101.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:55: ( LT | ';' )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == LT) :
                    alt38 = 1
                elif (LA38_0 == 75) :
                    alt38 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("162:55: ( LT | ';' )", 38, 0, self.input)

                    raise nvae

                if alt38 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:56: LT
                    LT102 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement793)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT102)


                elif alt38 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:61: ';'
                    char_literal103 = self.input.LT(1)
                    self.match(self.input, 75, self.FOLLOW_75_in_defaultXmlNamespaceStatement797)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_75.add(char_literal103)



                # AST Rewrite
                # elements: identifier
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
                    # 163:3: -> ^( DEFAULTNS identifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:6: ^( DEFAULTNS identifier )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(DEFAULTNS, "DEFAULTNS"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 18, defaultXmlNamespaceStatement_StartIndex)

            pass

        return retval

    # $ANTLR end defaultXmlNamespaceStatement

    class statementBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:166:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal104 = None
        LT105 = None
        LT107 = None
        char_literal108 = None
        char_literal109 = None
        string_literal110 = None
        char_literal112 = None
        statementList106 = None

        expression111 = None


        char_literal104_tree = None
        LT105_tree = None
        LT107_tree = None
        char_literal108_tree = None
        char_literal109_tree = None
        string_literal110_tree = None
        char_literal112_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' )
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == 66) :
                    LA43_1 = self.input.LA(2)

                    if (self.synpred62()) :
                        alt43 = 1
                    elif (True) :
                        alt43 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("166:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 43, 1, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("166:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                    root_0 = self.adaptor.nil()

                    char_literal104 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_statementBlock819)
                    if self.failed:
                        return retval

                    char_literal104_tree = self.adaptor.createWithPayload(char_literal104)
                    self.adaptor.addChild(root_0, char_literal104_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:10: ( LT )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == LT) :
                            LA39_2 = self.input.LA(2)

                            if (self.synpred59()) :
                                alt39 = 1




                        if alt39 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT105 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock821)
                            if self.failed:
                                return retval


                        else:
                            break #loop39


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:13: ( statementList )?
                    alt40 = 2
                    alt40 = self.dfa40.predict(self.input)
                    if alt40 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                        self.following.append(self.FOLLOW_statementList_in_statementBlock825)
                        statementList106 = self.statementList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statementList106.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:30: ( LT )*
                    while True: #loop41
                        alt41 = 2
                        LA41_0 = self.input.LA(1)

                        if (LA41_0 == LT) :
                            alt41 = 1


                        if alt41 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT107 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock828)
                            if self.failed:
                                return retval


                        else:
                            break #loop41


                    char_literal108 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_statementBlock832)
                    if self.failed:
                        return retval

                    char_literal108_tree = self.adaptor.createWithPayload(char_literal108)
                    self.adaptor.addChild(root_0, char_literal108_tree)



                elif alt43 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:4: '{' ( 'return' )? expression '}'
                    root_0 = self.adaptor.nil()

                    char_literal109 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_statementBlock837)
                    if self.failed:
                        return retval

                    char_literal109_tree = self.adaptor.createWithPayload(char_literal109)
                    self.adaptor.addChild(root_0, char_literal109_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:8: ( 'return' )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == 76) :
                        alt42 = 1
                    if alt42 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'return'
                        string_literal110 = self.input.LT(1)
                        self.match(self.input, 76, self.FOLLOW_76_in_statementBlock839)
                        if self.failed:
                            return retval

                        string_literal110_tree = self.adaptor.createWithPayload(string_literal110)
                        self.adaptor.addChild(root_0, string_literal110_tree)




                    self.following.append(self.FOLLOW_expression_in_statementBlock842)
                    expression111 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression111.tree)
                    char_literal112 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_statementBlock844)
                    if self.failed:
                        return retval

                    char_literal112_tree = self.adaptor.createWithPayload(char_literal112)
                    self.adaptor.addChild(root_0, char_literal112_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 19, statementBlock_StartIndex)

            pass

        return retval

    # $ANTLR end statementBlock

    class statementList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT114 = None
        statement113 = None

        statement115 = None


        LT114_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList857)
                statement113 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement113.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:14: ( ( LT )* statement )*
                while True: #loop45
                    alt45 = 2
                    LA45 = self.input.LA(1)
                    if LA45 == LT:
                        LA45_1 = self.input.LA(2)

                        if (self.synpred65()) :
                            alt45 = 1


                    elif LA45 == 72:
                        LA45_3 = self.input.LA(2)

                        if (self.synpred65()) :
                            alt45 = 1


                    elif LA45 == StringLiteral or LA45 == XMLComment or LA45 == NumericLiteral or LA45 == Identifier or LA45 == RegularExpressionHacks or LA45 == 60 or LA45 == 62 or LA45 == 64 or LA45 == 66 or LA45 == 68 or LA45 == 69 or LA45 == 73 or LA45 == 74 or LA45 == 75 or LA45 == 76 or LA45 == 77 or LA45 == 78 or LA45 == 79 or LA45 == 80 or LA45 == 82 or LA45 == 84 or LA45 == 85 or LA45 == 86 or LA45 == 87 or LA45 == 89 or LA45 == 90 or LA45 == 91 or LA45 == 92 or LA45 == 94 or LA45 == 95 or LA45 == 98 or LA45 == 128 or LA45 == 130 or LA45 == 131 or LA45 == 132 or LA45 == 133 or LA45 == 134 or LA45 == 135 or LA45 == 136 or LA45 == 137 or LA45 == 138 or LA45 == 139 or LA45 == 140 or LA45 == 141 or LA45 == 142:
                        alt45 = 1

                    if alt45 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:17: ( LT )*
                        while True: #loop44
                            alt44 = 2
                            LA44_0 = self.input.LA(1)

                            if (LA44_0 == LT) :
                                LA44_2 = self.input.LA(2)

                                if (self.synpred64()) :
                                    alt44 = 1




                            if alt44 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT114 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList860)
                                if self.failed:
                                    return retval


                            else:
                                break #loop44


                        self.following.append(self.FOLLOW_statement_in_statementList864)
                        statement115 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement115.tree)


                    else:
                        break #loop45





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 20, statementList_StartIndex)

            pass

        return retval

    # $ANTLR end statementList

    class variableStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:1: variableStatement : (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        mod = None
        LT116 = None
        LT118 = None
        char_literal119 = None
        variableDeclarationList117 = None


        mod_tree = None
        LT116_tree = None
        LT118_tree = None
        char_literal119_tree = None
        stream_79 = RewriteRuleTokenStream(self.adaptor, "token 79")
        stream_78 = RewriteRuleTokenStream(self.adaptor, "token 78")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_77 = RewriteRuleTokenStream(self.adaptor, "token 77")
        stream_75 = RewriteRuleTokenStream(self.adaptor, "token 75")
        stream_variableDeclarationList = RewriteRuleSubtreeStream(self.adaptor, "rule variableDeclarationList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:2: ( (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:4: (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:4: (mod= 'var' | mod= 'const' | mod= 'let' )
                alt46 = 3
                LA46 = self.input.LA(1)
                if LA46 == 77:
                    alt46 = 1
                elif LA46 == 78:
                    alt46 = 2
                elif LA46 == 79:
                    alt46 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("176:4: (mod= 'var' | mod= 'const' | mod= 'let' )", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:5: mod= 'var'
                    mod = self.input.LT(1)
                    self.match(self.input, 77, self.FOLLOW_77_in_variableStatement880)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_77.add(mod)


                elif alt46 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:15: mod= 'const'
                    mod = self.input.LT(1)
                    self.match(self.input, 78, self.FOLLOW_78_in_variableStatement884)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_78.add(mod)


                elif alt46 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:27: mod= 'let'
                    mod = self.input.LT(1)
                    self.match(self.input, 79, self.FOLLOW_79_in_variableStatement888)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_79.add(mod)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:38: ( LT )*
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == LT) :
                        alt47 = 1


                    if alt47 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT116 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement891)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT116)


                    else:
                        break #loop47


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement894)
                variableDeclarationList117 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_variableDeclarationList.add(variableDeclarationList117.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:66: ( LT | ';' )
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == LT) :
                    alt48 = 1
                elif (LA48_0 == 75) :
                    alt48 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("176:66: ( LT | ';' )", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:67: LT
                    LT118 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement897)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT118)


                elif alt48 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:72: ';'
                    char_literal119 = self.input.LT(1)
                    self.match(self.input, 75, self.FOLLOW_75_in_variableStatement901)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_75.add(char_literal119)



                # AST Rewrite
                # elements: variableDeclarationList, mod
                # token labels: mod
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                if self.backtracking == 0:

                    retval.tree = root_0
                    stream_mod = RewriteRuleTokenStream(self.adaptor, "token mod", mod)

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                    root_0 = self.adaptor.nil()
                    # 177:3: -> ^( VARDEFS $mod variableDeclarationList )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:177:6: ^( VARDEFS $mod variableDeclarationList )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEFS, "VARDEFS"), root_1)

                    self.adaptor.addChild(root_1, stream_mod.next())
                    self.adaptor.addChild(root_1, stream_variableDeclarationList.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 21, variableStatement_StartIndex)

            pass

        return retval

    # $ANTLR end variableStatement

    class variableDeclarationList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:180:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT121 = None
        char_literal122 = None
        LT123 = None
        variableDeclaration120 = None

        variableDeclaration124 = None


        LT121_tree = None
        char_literal122_tree = None
        LT123_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList926)
                variableDeclaration120 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration120.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop51
                    alt51 = 2
                    alt51 = self.dfa51.predict(self.input)
                    if alt51 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:27: ( LT )*
                        while True: #loop49
                            alt49 = 2
                            LA49_0 = self.input.LA(1)

                            if (LA49_0 == LT) :
                                alt49 = 1


                            if alt49 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT121 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList929)
                                if self.failed:
                                    return retval


                            else:
                                break #loop49


                        char_literal122 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationList933)
                        if self.failed:
                            return retval

                        char_literal122_tree = self.adaptor.createWithPayload(char_literal122)
                        self.adaptor.addChild(root_0, char_literal122_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:36: ( LT )*
                        while True: #loop50
                            alt50 = 2
                            LA50_0 = self.input.LA(1)

                            if (LA50_0 == LT) :
                                alt50 = 1


                            if alt50 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT123 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList935)
                                if self.failed:
                                    return retval


                            else:
                                break #loop50


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList939)
                        variableDeclaration124 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration124.tree)


                    else:
                        break #loop51





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 22, variableDeclarationList_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationList

    class variableDeclarationListNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationListNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT126 = None
        char_literal127 = None
        LT128 = None
        variableDeclarationNoIn125 = None

        variableDeclarationNoIn129 = None


        LT126_tree = None
        char_literal127_tree = None
        LT128_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn953)
                variableDeclarationNoIn125 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn125.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop54
                    alt54 = 2
                    alt54 = self.dfa54.predict(self.input)
                    if alt54 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:31: ( LT )*
                        while True: #loop52
                            alt52 = 2
                            LA52_0 = self.input.LA(1)

                            if (LA52_0 == LT) :
                                alt52 = 1


                            if alt52 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT126 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn956)
                                if self.failed:
                                    return retval


                            else:
                                break #loop52


                        char_literal127 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationListNoIn960)
                        if self.failed:
                            return retval

                        char_literal127_tree = self.adaptor.createWithPayload(char_literal127)
                        self.adaptor.addChild(root_0, char_literal127_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:40: ( LT )*
                        while True: #loop53
                            alt53 = 2
                            LA53_0 = self.input.LA(1)

                            if (LA53_0 == LT) :
                                alt53 = 1


                            if alt53 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT128 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn962)
                                if self.failed:
                                    return retval


                            else:
                                break #loop53


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn966)
                        variableDeclarationNoIn129 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn129.tree)


                    else:
                        break #loop54





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 23, variableDeclarationListNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationListNoIn

    class variableDeclaration_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclaration
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:1: variableDeclaration : ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiser )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiser )? ) );
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT131 = None
        char_literal133 = None
        LT134 = None
        LT136 = None
        char_literal137 = None
        LT138 = None
        LT140 = None
        char_literal141 = None
        LT142 = None
        char_literal143 = None
        LT144 = None
        identifier130 = None

        initialiser132 = None

        identifier135 = None

        identifier139 = None

        initialiser145 = None


        LT131_tree = None
        char_literal133_tree = None
        LT134_tree = None
        LT136_tree = None
        char_literal137_tree = None
        LT138_tree = None
        LT140_tree = None
        char_literal141_tree = None
        LT142_tree = None
        char_literal143_tree = None
        LT144_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_80 = RewriteRuleTokenStream(self.adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self.adaptor, "token 81")
        stream_initialiser = RewriteRuleSubtreeStream(self.adaptor, "rule initialiser")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:2: ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiser )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiser )? ) )
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == Identifier or (72 <= LA68_0 <= 74) or LA68_0 == 87 or (138 <= LA68_0 <= 139)) :
                    alt68 = 1
                elif (LA68_0 == 80) :
                    alt68 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("188:1: variableDeclaration : ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiser )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiser )? ) );", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:4: identifier ( ( LT )* initialiser )?
                    self.following.append(self.FOLLOW_identifier_in_variableDeclaration980)
                    identifier130 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier130.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:15: ( ( LT )* initialiser )?
                    alt56 = 2
                    alt56 = self.dfa56.predict(self.input)
                    if alt56 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:16: ( LT )* initialiser
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:16: ( LT )*
                        while True: #loop55
                            alt55 = 2
                            LA55_0 = self.input.LA(1)

                            if (LA55_0 == LT) :
                                alt55 = 1


                            if alt55 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT131 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration983)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT131)


                            else:
                                break #loop55


                        self.following.append(self.FOLLOW_initialiser_in_variableDeclaration986)
                        initialiser132 = self.initialiser()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_initialiser.add(initialiser132.tree)



                    # AST Rewrite
                    # elements: identifier, initialiser
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
                        # 190:3: -> ^( VARDEF identifier ( initialiser )? )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:6: ^( VARDEF identifier ( initialiser )? )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:26: ( initialiser )?
                        if stream_initialiser.hasNext():
                            self.adaptor.addChild(root_1, stream_initialiser.next())


                        stream_initialiser.reset();

                        self.adaptor.addChild(root_0, root_1)





                elif alt68 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:4: '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiser )?
                    char_literal133 = self.input.LT(1)
                    self.match(self.input, 80, self.FOLLOW_80_in_variableDeclaration1006)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_80.add(char_literal133)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:8: ( LT )*
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == LT) :
                            LA57_2 = self.input.LA(2)

                            if (self.synpred79()) :
                                alt57 = 1




                        if alt57 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT134 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1008)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT134)


                        else:
                            break #loop57


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:12: ( identifier )?
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == Identifier or (72 <= LA58_0 <= 74) or LA58_0 == 87 or (138 <= LA58_0 <= 139)) :
                        alt58 = 1
                    if alt58 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                        self.following.append(self.FOLLOW_identifier_in_variableDeclaration1011)
                        identifier135 = self.identifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_identifier.add(identifier135.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:24: ( ( LT )* ',' ( ( LT )* identifier )? )*
                    while True: #loop62
                        alt62 = 2
                        alt62 = self.dfa62.predict(self.input)
                        if alt62 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:25: ( LT )* ',' ( ( LT )* identifier )?
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:25: ( LT )*
                            while True: #loop59
                                alt59 = 2
                                LA59_0 = self.input.LA(1)

                                if (LA59_0 == LT) :
                                    alt59 = 1


                                if alt59 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT136 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1015)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT136)


                                else:
                                    break #loop59


                            char_literal137 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_variableDeclaration1018)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal137)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:33: ( ( LT )* identifier )?
                            alt61 = 2
                            alt61 = self.dfa61.predict(self.input)
                            if alt61 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:34: ( LT )* identifier
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:34: ( LT )*
                                while True: #loop60
                                    alt60 = 2
                                    LA60_0 = self.input.LA(1)

                                    if (LA60_0 == LT) :
                                        alt60 = 1


                                    if alt60 == 1:
                                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                        LT138 = self.input.LT(1)
                                        self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1021)
                                        if self.failed:
                                            return retval
                                        if self.backtracking == 0:
                                            stream_LT.add(LT138)


                                    else:
                                        break #loop60


                                self.following.append(self.FOLLOW_identifier_in_variableDeclaration1024)
                                identifier139 = self.identifier()
                                self.following.pop()
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_identifier.add(identifier139.tree)





                        else:
                            break #loop62


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:53: ( LT )*
                    while True: #loop63
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if (LA63_0 == LT) :
                            alt63 = 1


                        if alt63 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT140 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1030)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT140)


                        else:
                            break #loop63


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:57: ( ',' ( LT )* )?
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == 70) :
                        alt65 = 1
                    if alt65 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:58: ',' ( LT )*
                        char_literal141 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclaration1034)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal141)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:62: ( LT )*
                        while True: #loop64
                            alt64 = 2
                            LA64_0 = self.input.LA(1)

                            if (LA64_0 == LT) :
                                alt64 = 1


                            if alt64 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT142 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1036)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT142)


                            else:
                                break #loop64





                    char_literal143 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_variableDeclaration1041)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_81.add(char_literal143)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:72: ( ( LT )* initialiser )?
                    alt67 = 2
                    alt67 = self.dfa67.predict(self.input)
                    if alt67 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:73: ( LT )* initialiser
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:73: ( LT )*
                        while True: #loop66
                            alt66 = 2
                            LA66_0 = self.input.LA(1)

                            if (LA66_0 == LT) :
                                alt66 = 1


                            if alt66 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT144 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration1044)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT144)


                            else:
                                break #loop66


                        self.following.append(self.FOLLOW_initialiser_in_variableDeclaration1047)
                        initialiser145 = self.initialiser()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_initialiser.add(initialiser145.tree)



                    # AST Rewrite
                    # elements: initialiser, identifier
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
                        # 192:3: -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiser )? )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:6: ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiser )? )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:15: ^( ARRAY ( identifier )* )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARRAY, "ARRAY"), root_2)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:23: ( identifier )*
                        while stream_identifier.hasNext():
                            self.adaptor.addChild(root_2, stream_identifier.next())


                        stream_identifier.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:36: ( initialiser )?
                        if stream_initialiser.hasNext():
                            self.adaptor.addChild(root_1, stream_initialiser.next())


                        stream_initialiser.reset();

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 24, variableDeclaration_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclaration

    class variableDeclarationNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:1: variableDeclarationNoIn : ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiserNoIn )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiserNoIn )? ) );
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT147 = None
        char_literal149 = None
        LT150 = None
        LT152 = None
        char_literal153 = None
        LT154 = None
        LT156 = None
        char_literal157 = None
        LT158 = None
        char_literal159 = None
        LT160 = None
        identifier146 = None

        initialiserNoIn148 = None

        identifier151 = None

        identifier155 = None

        initialiserNoIn161 = None


        LT147_tree = None
        char_literal149_tree = None
        LT150_tree = None
        LT152_tree = None
        char_literal153_tree = None
        LT154_tree = None
        LT156_tree = None
        char_literal157_tree = None
        LT158_tree = None
        char_literal159_tree = None
        LT160_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_80 = RewriteRuleTokenStream(self.adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self.adaptor, "token 81")
        stream_initialiserNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule initialiserNoIn")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:2: ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiserNoIn )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiserNoIn )? ) )
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == Identifier or (72 <= LA82_0 <= 74) or LA82_0 == 87 or (138 <= LA82_0 <= 139)) :
                    alt82 = 1
                elif (LA82_0 == 80) :
                    alt82 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("195:1: variableDeclarationNoIn : ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) | '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiserNoIn )? -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiserNoIn )? ) );", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:4: identifier ( ( LT )* initialiserNoIn )?
                    self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn1079)
                    identifier146 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier146.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:15: ( ( LT )* initialiserNoIn )?
                    alt70 = 2
                    alt70 = self.dfa70.predict(self.input)
                    if alt70 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:16: ( LT )* initialiserNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:16: ( LT )*
                        while True: #loop69
                            alt69 = 2
                            LA69_0 = self.input.LA(1)

                            if (LA69_0 == LT) :
                                alt69 = 1


                            if alt69 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT147 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1082)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT147)


                            else:
                                break #loop69


                        self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn1085)
                        initialiserNoIn148 = self.initialiserNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_initialiserNoIn.add(initialiserNoIn148.tree)



                    # AST Rewrite
                    # elements: initialiserNoIn, identifier
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
                        # 197:3: -> ^( VARDEF identifier ( initialiserNoIn )? )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:197:6: ^( VARDEF identifier ( initialiserNoIn )? )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:197:26: ( initialiserNoIn )?
                        if stream_initialiserNoIn.hasNext():
                            self.adaptor.addChild(root_1, stream_initialiserNoIn.next())


                        stream_initialiserNoIn.reset();

                        self.adaptor.addChild(root_0, root_1)





                elif alt82 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:4: '[' ( LT )* ( identifier )? ( ( LT )* ',' ( ( LT )* identifier )? )* ( LT )* ( ',' ( LT )* )? ']' ( ( LT )* initialiserNoIn )?
                    char_literal149 = self.input.LT(1)
                    self.match(self.input, 80, self.FOLLOW_80_in_variableDeclarationNoIn1105)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_80.add(char_literal149)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:8: ( LT )*
                    while True: #loop71
                        alt71 = 2
                        LA71_0 = self.input.LA(1)

                        if (LA71_0 == LT) :
                            LA71_2 = self.input.LA(2)

                            if (self.synpred93()) :
                                alt71 = 1




                        if alt71 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT150 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1107)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT150)


                        else:
                            break #loop71


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:12: ( identifier )?
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == Identifier or (72 <= LA72_0 <= 74) or LA72_0 == 87 or (138 <= LA72_0 <= 139)) :
                        alt72 = 1
                    if alt72 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                        self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn1110)
                        identifier151 = self.identifier()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_identifier.add(identifier151.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:24: ( ( LT )* ',' ( ( LT )* identifier )? )*
                    while True: #loop76
                        alt76 = 2
                        alt76 = self.dfa76.predict(self.input)
                        if alt76 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:25: ( LT )* ',' ( ( LT )* identifier )?
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:25: ( LT )*
                            while True: #loop73
                                alt73 = 2
                                LA73_0 = self.input.LA(1)

                                if (LA73_0 == LT) :
                                    alt73 = 1


                                if alt73 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT152 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1114)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT152)


                                else:
                                    break #loop73


                            char_literal153 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationNoIn1117)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal153)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:33: ( ( LT )* identifier )?
                            alt75 = 2
                            alt75 = self.dfa75.predict(self.input)
                            if alt75 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:34: ( LT )* identifier
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:34: ( LT )*
                                while True: #loop74
                                    alt74 = 2
                                    LA74_0 = self.input.LA(1)

                                    if (LA74_0 == LT) :
                                        alt74 = 1


                                    if alt74 == 1:
                                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                        LT154 = self.input.LT(1)
                                        self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1120)
                                        if self.failed:
                                            return retval
                                        if self.backtracking == 0:
                                            stream_LT.add(LT154)


                                    else:
                                        break #loop74


                                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn1123)
                                identifier155 = self.identifier()
                                self.following.pop()
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_identifier.add(identifier155.tree)





                        else:
                            break #loop76


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:53: ( LT )*
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == LT) :
                            alt77 = 1


                        if alt77 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT156 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1129)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT156)


                        else:
                            break #loop77


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:57: ( ',' ( LT )* )?
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if (LA79_0 == 70) :
                        alt79 = 1
                    if alt79 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:58: ',' ( LT )*
                        char_literal157 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationNoIn1133)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal157)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:62: ( LT )*
                        while True: #loop78
                            alt78 = 2
                            LA78_0 = self.input.LA(1)

                            if (LA78_0 == LT) :
                                alt78 = 1


                            if alt78 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT158 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1135)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT158)


                            else:
                                break #loop78





                    char_literal159 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_variableDeclarationNoIn1140)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_81.add(char_literal159)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:72: ( ( LT )* initialiserNoIn )?
                    alt81 = 2
                    alt81 = self.dfa81.predict(self.input)
                    if alt81 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:73: ( LT )* initialiserNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:73: ( LT )*
                        while True: #loop80
                            alt80 = 2
                            LA80_0 = self.input.LA(1)

                            if (LA80_0 == LT) :
                                alt80 = 1


                            if alt80 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT160 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn1143)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT160)


                            else:
                                break #loop80


                        self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn1146)
                        initialiserNoIn161 = self.initialiserNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_initialiserNoIn.add(initialiserNoIn161.tree)



                    # AST Rewrite
                    # elements: initialiserNoIn, identifier
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
                        # 199:3: -> ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiserNoIn )? )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:6: ^( VARDEF ^( ARRAY ( identifier )* ) ( initialiserNoIn )? )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:15: ^( ARRAY ( identifier )* )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARRAY, "ARRAY"), root_2)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:23: ( identifier )*
                        while stream_identifier.hasNext():
                            self.adaptor.addChild(root_2, stream_identifier.next())


                        stream_identifier.reset();

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:36: ( initialiserNoIn )?
                        if stream_initialiserNoIn.hasNext():
                            self.adaptor.addChild(root_1, stream_initialiserNoIn.next())


                        stream_initialiserNoIn.reset();

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 25, variableDeclarationNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationNoIn

    class initialiser_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiser
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:1: initialiser : '=' ( LT )* assignmentExpression -> assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal162 = None
        LT163 = None
        assignmentExpression164 = None


        char_literal162_tree = None
        LT163_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:2: ( '=' ( LT )* assignmentExpression -> assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:4: '=' ( LT )* assignmentExpression
                char_literal162 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_initialiser1178)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal162)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:8: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        LA83_2 = self.input.LA(2)

                        if (self.synpred104()) :
                            alt83 = 1




                    if alt83 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT163 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser1180)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT163)


                    else:
                        break #loop83


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser1183)
                assignmentExpression164 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression164.tree)
                # AST Rewrite
                # elements: assignmentExpression
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
                    # 204:3: -> assignmentExpression
                    self.adaptor.addChild(root_0, stream_assignmentExpression.next())






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 26, initialiser_StartIndex)

            pass

        return retval

    # $ANTLR end initialiser

    class initialiserNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiserNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal165 = None
        LT166 = None
        assignmentExpressionNoIn167 = None


        char_literal165_tree = None
        LT166_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:2: ( '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:4: '=' ( LT )* assignmentExpressionNoIn
                char_literal165 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_initialiserNoIn1201)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal165)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:8: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        LA84_2 = self.input.LA(2)

                        if (self.synpred105()) :
                            alt84 = 1




                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT166 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn1203)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT166)


                    else:
                        break #loop84


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn1206)
                assignmentExpressionNoIn167 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn167.tree)
                # AST Rewrite
                # elements: assignmentExpressionNoIn
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
                    # 209:3: -> assignmentExpressionNoIn
                    self.adaptor.addChild(root_0, stream_assignmentExpressionNoIn.next())






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 27, initialiserNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end initialiserNoIn

    class emptyStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start emptyStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal168 = None

        char_literal168_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:213:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:213:4: ';'
                root_0 = self.adaptor.nil()

                char_literal168 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_emptyStatement1224)
                if self.failed:
                    return retval

                char_literal168_tree = self.adaptor.createWithPayload(char_literal168)
                self.adaptor.addChild(root_0, char_literal168_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 28, emptyStatement_StartIndex)

            pass

        return retval

    # $ANTLR end emptyStatement

    class expressionStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:1: expressionStatement : expression ( LT | ';' ) ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        set170 = None
        expression169 = None


        set170_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement1236)
                expression169 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression169.tree)
                set170 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_expressionStatement1238
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
            if self.backtracking > 0:
                self.memoize(self.input, 29, expressionStatement_StartIndex)

            pass

        return retval

    # $ANTLR end expressionStatement

    class ifStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start ifStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal171 = None
        LT172 = None
        char_literal173 = None
        LT174 = None
        LT176 = None
        char_literal177 = None
        LT178 = None
        LT180 = None
        string_literal181 = None
        LT182 = None
        expression175 = None

        statement179 = None

        statement183 = None


        string_literal171_tree = None
        LT172_tree = None
        char_literal173_tree = None
        LT174_tree = None
        LT176_tree = None
        char_literal177_tree = None
        LT178_tree = None
        LT180_tree = None
        string_literal181_tree = None
        LT182_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal171 = self.input.LT(1)
                self.match(self.input, 82, self.FOLLOW_82_in_ifStatement1257)
                if self.failed:
                    return retval

                string_literal171_tree = self.adaptor.createWithPayload(string_literal171)
                self.adaptor.addChild(root_0, string_literal171_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:11: ( LT )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == LT) :
                        alt85 = 1


                    if alt85 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT172 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1259)
                        if self.failed:
                            return retval


                    else:
                        break #loop85


                char_literal173 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_ifStatement1263)
                if self.failed:
                    return retval

                char_literal173_tree = self.adaptor.createWithPayload(char_literal173)
                self.adaptor.addChild(root_0, char_literal173_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:20: ( LT )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == LT) :
                        LA86_2 = self.input.LA(2)

                        if (self.synpred108()) :
                            alt86 = 1




                    if alt86 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT174 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1265)
                        if self.failed:
                            return retval


                    else:
                        break #loop86


                self.following.append(self.FOLLOW_expression_in_ifStatement1269)
                expression175 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression175.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:36: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        alt87 = 1


                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT176 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1271)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                char_literal177 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_ifStatement1275)
                if self.failed:
                    return retval

                char_literal177_tree = self.adaptor.createWithPayload(char_literal177)
                self.adaptor.addChild(root_0, char_literal177_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:45: ( LT )*
                while True: #loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == LT) :
                        LA88_2 = self.input.LA(2)

                        if (self.synpred110()) :
                            alt88 = 1




                    if alt88 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT178 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1277)
                        if self.failed:
                            return retval


                    else:
                        break #loop88


                self.following.append(self.FOLLOW_statement_in_ifStatement1281)
                statement179 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement179.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:58: ( ( LT )* 'else' ( LT )* statement )?
                alt91 = 2
                LA91_0 = self.input.LA(1)

                if (LA91_0 == LT) :
                    LA91_1 = self.input.LA(2)

                    if (self.synpred113()) :
                        alt91 = 1
                elif (LA91_0 == 83) :
                    LA91_2 = self.input.LA(2)

                    if (self.synpred113()) :
                        alt91 = 1
                if alt91 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:61: ( LT )*
                    while True: #loop89
                        alt89 = 2
                        LA89_0 = self.input.LA(1)

                        if (LA89_0 == LT) :
                            alt89 = 1


                        if alt89 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT180 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1284)
                            if self.failed:
                                return retval


                        else:
                            break #loop89


                    string_literal181 = self.input.LT(1)
                    self.match(self.input, 83, self.FOLLOW_83_in_ifStatement1288)
                    if self.failed:
                        return retval

                    string_literal181_tree = self.adaptor.createWithPayload(string_literal181)
                    self.adaptor.addChild(root_0, string_literal181_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:73: ( LT )*
                    while True: #loop90
                        alt90 = 2
                        LA90_0 = self.input.LA(1)

                        if (LA90_0 == LT) :
                            LA90_2 = self.input.LA(2)

                            if (self.synpred112()) :
                                alt90 = 1




                        if alt90 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT182 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1290)
                            if self.failed:
                                return retval


                        else:
                            break #loop90


                    self.following.append(self.FOLLOW_statement_in_ifStatement1294)
                    statement183 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement183.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 30, ifStatement_StartIndex)

            pass

        return retval

    # $ANTLR end ifStatement

    class iterationStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start iterationStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement184 = None

        whileStatement185 = None

        forStatement186 = None

        forInStatement187 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt92 = 4
                LA92 = self.input.LA(1)
                if LA92 == 84:
                    alt92 = 1
                elif LA92 == 85:
                    alt92 = 2
                elif LA92 == 86:
                    LA92_3 = self.input.LA(2)

                    if (self.synpred116()) :
                        alt92 = 3
                    elif (True) :
                        alt92 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 92, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("224:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 92, 0, self.input)

                    raise nvae

                if alt92 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement1308)
                    doWhileStatement184 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement184.tree)


                elif alt92 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement1313)
                    whileStatement185 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement185.tree)


                elif alt92 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:227:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement1318)
                    forStatement186 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement186.tree)


                elif alt92 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:228:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement1323)
                    forInStatement187 = self.forInStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forInStatement187.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 31, iterationStatement_StartIndex)

            pass

        return retval

    # $ANTLR end iterationStatement

    class doWhileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start doWhileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal188 = None
        LT189 = None
        LT191 = None
        string_literal192 = None
        LT193 = None
        char_literal194 = None
        char_literal196 = None
        set197 = None
        statement190 = None

        expression195 = None


        string_literal188_tree = None
        LT189_tree = None
        LT191_tree = None
        string_literal192_tree = None
        LT193_tree = None
        char_literal194_tree = None
        char_literal196_tree = None
        set197_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal188 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_doWhileStatement1335)
                if self.failed:
                    return retval

                string_literal188_tree = self.adaptor.createWithPayload(string_literal188)
                self.adaptor.addChild(root_0, string_literal188_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:11: ( LT )*
                while True: #loop93
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == LT) :
                        LA93_2 = self.input.LA(2)

                        if (self.synpred117()) :
                            alt93 = 1




                    if alt93 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT189 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1337)
                        if self.failed:
                            return retval


                    else:
                        break #loop93


                self.following.append(self.FOLLOW_statement_in_doWhileStatement1341)
                statement190 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement190.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:26: ( LT )*
                while True: #loop94
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == LT) :
                        alt94 = 1


                    if alt94 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT191 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1343)
                        if self.failed:
                            return retval


                    else:
                        break #loop94


                string_literal192 = self.input.LT(1)
                self.match(self.input, 85, self.FOLLOW_85_in_doWhileStatement1347)
                if self.failed:
                    return retval

                string_literal192_tree = self.adaptor.createWithPayload(string_literal192)
                self.adaptor.addChild(root_0, string_literal192_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:39: ( LT )*
                while True: #loop95
                    alt95 = 2
                    LA95_0 = self.input.LA(1)

                    if (LA95_0 == LT) :
                        alt95 = 1


                    if alt95 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT193 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1349)
                        if self.failed:
                            return retval


                    else:
                        break #loop95


                char_literal194 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_doWhileStatement1353)
                if self.failed:
                    return retval

                char_literal194_tree = self.adaptor.createWithPayload(char_literal194)
                self.adaptor.addChild(root_0, char_literal194_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement1355)
                expression195 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression195.tree)
                char_literal196 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_doWhileStatement1357)
                if self.failed:
                    return retval

                char_literal196_tree = self.adaptor.createWithPayload(char_literal196)
                self.adaptor.addChild(root_0, char_literal196_tree)

                set197 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement1359
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
            if self.backtracking > 0:
                self.memoize(self.input, 32, doWhileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end doWhileStatement

    class whileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start whileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal198 = None
        LT199 = None
        char_literal200 = None
        LT201 = None
        LT203 = None
        char_literal204 = None
        LT205 = None
        expression202 = None

        statement206 = None


        string_literal198_tree = None
        LT199_tree = None
        char_literal200_tree = None
        LT201_tree = None
        LT203_tree = None
        char_literal204_tree = None
        LT205_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal198 = self.input.LT(1)
                self.match(self.input, 85, self.FOLLOW_85_in_whileStatement1378)
                if self.failed:
                    return retval

                string_literal198_tree = self.adaptor.createWithPayload(string_literal198)
                self.adaptor.addChild(root_0, string_literal198_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:14: ( LT )*
                while True: #loop96
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == LT) :
                        alt96 = 1


                    if alt96 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT199 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1380)
                        if self.failed:
                            return retval


                    else:
                        break #loop96


                char_literal200 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_whileStatement1384)
                if self.failed:
                    return retval

                char_literal200_tree = self.adaptor.createWithPayload(char_literal200)
                self.adaptor.addChild(root_0, char_literal200_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:23: ( LT )*
                while True: #loop97
                    alt97 = 2
                    LA97_0 = self.input.LA(1)

                    if (LA97_0 == LT) :
                        LA97_2 = self.input.LA(2)

                        if (self.synpred122()) :
                            alt97 = 1




                    if alt97 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT201 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1386)
                        if self.failed:
                            return retval


                    else:
                        break #loop97


                self.following.append(self.FOLLOW_expression_in_whileStatement1390)
                expression202 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression202.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:39: ( LT )*
                while True: #loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == LT) :
                        alt98 = 1


                    if alt98 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT203 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1392)
                        if self.failed:
                            return retval


                    else:
                        break #loop98


                char_literal204 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_whileStatement1396)
                if self.failed:
                    return retval

                char_literal204_tree = self.adaptor.createWithPayload(char_literal204)
                self.adaptor.addChild(root_0, char_literal204_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:48: ( LT )*
                while True: #loop99
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if (LA99_0 == LT) :
                        LA99_2 = self.input.LA(2)

                        if (self.synpred124()) :
                            alt99 = 1




                    if alt99 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT205 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1398)
                        if self.failed:
                            return retval


                    else:
                        break #loop99


                self.following.append(self.FOLLOW_statement_in_whileStatement1402)
                statement206 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement206.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 33, whileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end whileStatement

    class forStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal207 = None
        LT208 = None
        char_literal209 = None
        LT210 = None
        LT212 = None
        char_literal213 = None
        LT214 = None
        LT216 = None
        char_literal217 = None
        LT218 = None
        LT220 = None
        char_literal221 = None
        LT222 = None
        forStatementInitialiserPart211 = None

        expression215 = None

        expression219 = None

        statement223 = None


        string_literal207_tree = None
        LT208_tree = None
        char_literal209_tree = None
        LT210_tree = None
        LT212_tree = None
        char_literal213_tree = None
        LT214_tree = None
        LT216_tree = None
        char_literal217_tree = None
        LT218_tree = None
        LT220_tree = None
        char_literal221_tree = None
        LT222_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal207 = self.input.LT(1)
                self.match(self.input, 86, self.FOLLOW_86_in_forStatement1414)
                if self.failed:
                    return retval

                string_literal207_tree = self.adaptor.createWithPayload(string_literal207)
                self.adaptor.addChild(root_0, string_literal207_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:12: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT208 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1416)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                char_literal209 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_forStatement1420)
                if self.failed:
                    return retval

                char_literal209_tree = self.adaptor.createWithPayload(char_literal209)
                self.adaptor.addChild(root_0, char_literal209_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:19: ( ( LT )* forStatementInitialiserPart )?
                alt102 = 2
                alt102 = self.dfa102.predict(self.input)
                if alt102 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:22: ( LT )*
                    while True: #loop101
                        alt101 = 2
                        LA101_0 = self.input.LA(1)

                        if (LA101_0 == LT) :
                            LA101_2 = self.input.LA(2)

                            if (self.synpred126()) :
                                alt101 = 1




                        if alt101 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT210 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1423)
                            if self.failed:
                                return retval


                        else:
                            break #loop101


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement1427)
                    forStatementInitialiserPart211 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart211.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:57: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        alt103 = 1


                    if alt103 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT212 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1431)
                        if self.failed:
                            return retval


                    else:
                        break #loop103


                char_literal213 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_forStatement1435)
                if self.failed:
                    return retval

                char_literal213_tree = self.adaptor.createWithPayload(char_literal213)
                self.adaptor.addChild(root_0, char_literal213_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:64: ( ( LT )* expression )?
                alt105 = 2
                alt105 = self.dfa105.predict(self.input)
                if alt105 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:67: ( LT )*
                    while True: #loop104
                        alt104 = 2
                        LA104_0 = self.input.LA(1)

                        if (LA104_0 == LT) :
                            LA104_2 = self.input.LA(2)

                            if (self.synpred129()) :
                                alt104 = 1




                        if alt104 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT214 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1438)
                            if self.failed:
                                return retval


                        else:
                            break #loop104


                    self.following.append(self.FOLLOW_expression_in_forStatement1442)
                    expression215 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression215.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:85: ( LT )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == LT) :
                        alt106 = 1


                    if alt106 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT216 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1446)
                        if self.failed:
                            return retval


                    else:
                        break #loop106


                char_literal217 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_forStatement1450)
                if self.failed:
                    return retval

                char_literal217_tree = self.adaptor.createWithPayload(char_literal217)
                self.adaptor.addChild(root_0, char_literal217_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:92: ( ( LT )* expression )?
                alt108 = 2
                alt108 = self.dfa108.predict(self.input)
                if alt108 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:95: ( LT )*
                    while True: #loop107
                        alt107 = 2
                        LA107_0 = self.input.LA(1)

                        if (LA107_0 == LT) :
                            LA107_2 = self.input.LA(2)

                            if (self.synpred132()) :
                                alt107 = 1




                        if alt107 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT218 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1453)
                            if self.failed:
                                return retval


                        else:
                            break #loop107


                    self.following.append(self.FOLLOW_expression_in_forStatement1457)
                    expression219 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression219.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:113: ( LT )*
                while True: #loop109
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == LT) :
                        alt109 = 1


                    if alt109 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT220 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1461)
                        if self.failed:
                            return retval


                    else:
                        break #loop109


                char_literal221 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_forStatement1465)
                if self.failed:
                    return retval

                char_literal221_tree = self.adaptor.createWithPayload(char_literal221)
                self.adaptor.addChild(root_0, char_literal221_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:122: ( LT )*
                while True: #loop110
                    alt110 = 2
                    LA110_0 = self.input.LA(1)

                    if (LA110_0 == LT) :
                        LA110_2 = self.input.LA(2)

                        if (self.synpred135()) :
                            alt110 = 1




                    if alt110 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT222 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1467)
                        if self.failed:
                            return retval


                    else:
                        break #loop110


                self.following.append(self.FOLLOW_statement_in_forStatement1471)
                statement223 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement223.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 34, forStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forStatement

    class forStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:243:1: forStatementInitialiserPart : ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        set225 = None
        LT226 = None
        expressionNoIn224 = None

        variableDeclarationListNoIn227 = None


        set225_tree = None
        LT226_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:244:2: ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn )
                alt112 = 2
                LA112_0 = self.input.LA(1)

                if ((LT <= LA112_0 <= RegularExpressionHacks) or LA112_0 == 60 or LA112_0 == 62 or LA112_0 == 64 or LA112_0 == 66 or (68 <= LA112_0 <= 69) or (72 <= LA112_0 <= 74) or LA112_0 == 80 or LA112_0 == 87 or LA112_0 == 98 or LA112_0 == 128 or (130 <= LA112_0 <= 142)) :
                    alt112 = 1
                elif (LA112_0 == 77 or LA112_0 == 79) :
                    alt112 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("243:1: forStatementInitialiserPart : ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn );", 112, 0, self.input)

                    raise nvae

                if alt112 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:244:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart1483)
                    expressionNoIn224 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn224.tree)


                elif alt112 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:4: ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    set225 = self.input.LT(1)
                    if self.input.LA(1) == 77 or self.input.LA(1) == 79:
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set225))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_forStatementInitialiserPart1488
                            )
                        raise mse


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:20: ( LT )*
                    while True: #loop111
                        alt111 = 2
                        LA111_0 = self.input.LA(1)

                        if (LA111_0 == LT) :
                            alt111 = 1


                        if alt111 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT226 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart1494)
                            if self.failed:
                                return retval


                        else:
                            break #loop111


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1498)
                    variableDeclarationListNoIn227 = self.variableDeclarationListNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationListNoIn227.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 35, forStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forStatementInitialiserPart

    class forInStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal228 = None
        LT229 = None
        string_literal230 = None
        LT231 = None
        char_literal232 = None
        LT233 = None
        LT235 = None
        string_literal236 = None
        LT237 = None
        LT239 = None
        char_literal240 = None
        LT241 = None
        forInStatementInitialiserPart234 = None

        expression238 = None

        statement242 = None


        string_literal228_tree = None
        LT229_tree = None
        string_literal230_tree = None
        LT231_tree = None
        char_literal232_tree = None
        LT233_tree = None
        LT235_tree = None
        string_literal236_tree = None
        LT237_tree = None
        LT239_tree = None
        char_literal240_tree = None
        LT241_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal228 = self.input.LT(1)
                self.match(self.input, 86, self.FOLLOW_86_in_forInStatement1510)
                if self.failed:
                    return retval

                string_literal228_tree = self.adaptor.createWithPayload(string_literal228)
                self.adaptor.addChild(root_0, string_literal228_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:12: ( LT )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == LT) :
                        LA113_2 = self.input.LA(2)

                        if (self.synpred139()) :
                            alt113 = 1




                    if alt113 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT229 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1512)
                        if self.failed:
                            return retval


                    else:
                        break #loop113


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:15: ( 'each' )?
                alt114 = 2
                LA114_0 = self.input.LA(1)

                if (LA114_0 == 87) :
                    alt114 = 1
                if alt114 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal230 = self.input.LT(1)
                    self.match(self.input, 87, self.FOLLOW_87_in_forInStatement1516)
                    if self.failed:
                        return retval

                    string_literal230_tree = self.adaptor.createWithPayload(string_literal230)
                    self.adaptor.addChild(root_0, string_literal230_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:25: ( LT )*
                while True: #loop115
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == LT) :
                        alt115 = 1


                    if alt115 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT231 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1519)
                        if self.failed:
                            return retval


                    else:
                        break #loop115


                char_literal232 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_forInStatement1523)
                if self.failed:
                    return retval

                char_literal232_tree = self.adaptor.createWithPayload(char_literal232)
                self.adaptor.addChild(root_0, char_literal232_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:34: ( LT )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == LT) :
                        LA116_2 = self.input.LA(2)

                        if (self.synpred142()) :
                            alt116 = 1




                    if alt116 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT233 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1525)
                        if self.failed:
                            return retval


                    else:
                        break #loop116


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement1529)
                forInStatementInitialiserPart234 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart234.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:69: ( LT )*
                while True: #loop117
                    alt117 = 2
                    LA117_0 = self.input.LA(1)

                    if (LA117_0 == LT) :
                        alt117 = 1


                    if alt117 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT235 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1531)
                        if self.failed:
                            return retval


                    else:
                        break #loop117


                string_literal236 = self.input.LT(1)
                self.match(self.input, 88, self.FOLLOW_88_in_forInStatement1535)
                if self.failed:
                    return retval

                string_literal236_tree = self.adaptor.createWithPayload(string_literal236)
                self.adaptor.addChild(root_0, string_literal236_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:79: ( LT )*
                while True: #loop118
                    alt118 = 2
                    LA118_0 = self.input.LA(1)

                    if (LA118_0 == LT) :
                        LA118_2 = self.input.LA(2)

                        if (self.synpred144()) :
                            alt118 = 1




                    if alt118 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT237 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1537)
                        if self.failed:
                            return retval


                    else:
                        break #loop118


                self.following.append(self.FOLLOW_expression_in_forInStatement1541)
                expression238 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression238.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:95: ( LT )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if (LA119_0 == LT) :
                        alt119 = 1


                    if alt119 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT239 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1543)
                        if self.failed:
                            return retval


                    else:
                        break #loop119


                char_literal240 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_forInStatement1547)
                if self.failed:
                    return retval

                char_literal240_tree = self.adaptor.createWithPayload(char_literal240)
                self.adaptor.addChild(root_0, char_literal240_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:104: ( LT )*
                while True: #loop120
                    alt120 = 2
                    LA120_0 = self.input.LA(1)

                    if (LA120_0 == LT) :
                        LA120_2 = self.input.LA(2)

                        if (self.synpred146()) :
                            alt120 = 1




                    if alt120 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT241 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1549)
                        if self.failed:
                            return retval


                    else:
                        break #loop120


                self.following.append(self.FOLLOW_statement_in_forInStatement1553)
                statement242 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement242.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 36, forInStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatement

    class forInStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:252:1: forInStatementInitialiserPart : ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        set244 = None
        LT245 = None
        leftHandSideExpression243 = None

        variableDeclarationNoIn246 = None


        set244_tree = None
        LT245_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:253:2: ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn )
                alt122 = 2
                LA122_0 = self.input.LA(1)

                if ((LT <= LA122_0 <= RegularExpressionHacks) or LA122_0 == 60 or LA122_0 == 62 or LA122_0 == 66 or (68 <= LA122_0 <= 69) or (72 <= LA122_0 <= 74) or LA122_0 == 80 or LA122_0 == 87 or LA122_0 == 98 or (137 <= LA122_0 <= 142)) :
                    alt122 = 1
                elif (LA122_0 == 77 or LA122_0 == 79) :
                    alt122 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("252:1: forInStatementInitialiserPart : ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn );", 122, 0, self.input)

                    raise nvae

                if alt122 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:253:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1565)
                    leftHandSideExpression243 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression243.tree)


                elif alt122 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:4: ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    set244 = self.input.LT(1)
                    if self.input.LA(1) == 77 or self.input.LA(1) == 79:
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set244))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_forInStatementInitialiserPart1570
                            )
                        raise mse


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:20: ( LT )*
                    while True: #loop121
                        alt121 = 2
                        LA121_0 = self.input.LA(1)

                        if (LA121_0 == LT) :
                            alt121 = 1


                        if alt121 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT245 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart1576)
                            if self.failed:
                                return retval


                        else:
                            break #loop121


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1580)
                    variableDeclarationNoIn246 = self.variableDeclarationNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationNoIn246.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 37, forInStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatementInitialiserPart

    class continueStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start continueStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:257:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal247 = None
        set249 = None
        identifier248 = None


        string_literal247_tree = None
        set249_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal247 = self.input.LT(1)
                self.match(self.input, 89, self.FOLLOW_89_in_continueStatement1591)
                if self.failed:
                    return retval

                string_literal247_tree = self.adaptor.createWithPayload(string_literal247)
                self.adaptor.addChild(root_0, string_literal247_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:15: ( identifier )?
                alt123 = 2
                LA123_0 = self.input.LA(1)

                if (LA123_0 == Identifier or (72 <= LA123_0 <= 74) or LA123_0 == 87 or (138 <= LA123_0 <= 139)) :
                    alt123 = 1
                if alt123 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement1593)
                    identifier248 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier248.tree)



                set249 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_continueStatement1596
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
            if self.backtracking > 0:
                self.memoize(self.input, 38, continueStatement_StartIndex)

            pass

        return retval

    # $ANTLR end continueStatement

    class breakStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start breakStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:261:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal250 = None
        set252 = None
        identifier251 = None


        string_literal250_tree = None
        set252_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal250 = self.input.LT(1)
                self.match(self.input, 90, self.FOLLOW_90_in_breakStatement1614)
                if self.failed:
                    return retval

                string_literal250_tree = self.adaptor.createWithPayload(string_literal250)
                self.adaptor.addChild(root_0, string_literal250_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:12: ( identifier )?
                alt124 = 2
                LA124_0 = self.input.LA(1)

                if (LA124_0 == Identifier or (72 <= LA124_0 <= 74) or LA124_0 == 87 or (138 <= LA124_0 <= 139)) :
                    alt124 = 1
                if alt124 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement1616)
                    identifier251 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier251.tree)



                set252 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_breakStatement1619
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
            if self.backtracking > 0:
                self.memoize(self.input, 39, breakStatement_StartIndex)

            pass

        return retval

    # $ANTLR end breakStatement

    class returnStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start returnStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal253 = None
        set255 = None
        expression254 = None


        string_literal253_tree = None
        set255_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal253 = self.input.LT(1)
                self.match(self.input, 76, self.FOLLOW_76_in_returnStatement1637)
                if self.failed:
                    return retval

                string_literal253_tree = self.adaptor.createWithPayload(string_literal253)
                self.adaptor.addChild(root_0, string_literal253_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:13: ( expression )?
                alt125 = 2
                LA125_0 = self.input.LA(1)

                if ((StringLiteral <= LA125_0 <= RegularExpressionHacks) or LA125_0 == 60 or LA125_0 == 62 or LA125_0 == 64 or LA125_0 == 66 or (68 <= LA125_0 <= 69) or (72 <= LA125_0 <= 74) or LA125_0 == 80 or LA125_0 == 87 or LA125_0 == 98 or LA125_0 == 128 or (130 <= LA125_0 <= 142)) :
                    alt125 = 1
                elif (LA125_0 == LT) :
                    LA125_2 = self.input.LA(2)

                    if (self.synpred154()) :
                        alt125 = 1
                if alt125 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement1639)
                    expression254 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression254.tree)



                set255 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_returnStatement1642
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
            if self.backtracking > 0:
                self.memoize(self.input, 40, returnStatement_StartIndex)

            pass

        return retval

    # $ANTLR end returnStatement

    class withStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start withStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal256 = None
        LT257 = None
        char_literal258 = None
        LT259 = None
        LT261 = None
        char_literal262 = None
        LT263 = None
        expression260 = None

        statement264 = None


        string_literal256_tree = None
        LT257_tree = None
        char_literal258_tree = None
        LT259_tree = None
        LT261_tree = None
        char_literal262_tree = None
        LT263_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal256 = self.input.LT(1)
                self.match(self.input, 91, self.FOLLOW_91_in_withStatement1661)
                if self.failed:
                    return retval

                string_literal256_tree = self.adaptor.createWithPayload(string_literal256)
                self.adaptor.addChild(root_0, string_literal256_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:13: ( LT )*
                while True: #loop126
                    alt126 = 2
                    LA126_0 = self.input.LA(1)

                    if (LA126_0 == LT) :
                        alt126 = 1


                    if alt126 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT257 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1663)
                        if self.failed:
                            return retval


                    else:
                        break #loop126


                char_literal258 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_withStatement1667)
                if self.failed:
                    return retval

                char_literal258_tree = self.adaptor.createWithPayload(char_literal258)
                self.adaptor.addChild(root_0, char_literal258_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:22: ( LT )*
                while True: #loop127
                    alt127 = 2
                    LA127_0 = self.input.LA(1)

                    if (LA127_0 == LT) :
                        LA127_2 = self.input.LA(2)

                        if (self.synpred157()) :
                            alt127 = 1




                    if alt127 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT259 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1669)
                        if self.failed:
                            return retval


                    else:
                        break #loop127


                self.following.append(self.FOLLOW_expression_in_withStatement1673)
                expression260 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression260.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:38: ( LT )*
                while True: #loop128
                    alt128 = 2
                    LA128_0 = self.input.LA(1)

                    if (LA128_0 == LT) :
                        alt128 = 1


                    if alt128 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT261 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1675)
                        if self.failed:
                            return retval


                    else:
                        break #loop128


                char_literal262 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_withStatement1679)
                if self.failed:
                    return retval

                char_literal262_tree = self.adaptor.createWithPayload(char_literal262)
                self.adaptor.addChild(root_0, char_literal262_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:47: ( LT )*
                while True: #loop129
                    alt129 = 2
                    LA129_0 = self.input.LA(1)

                    if (LA129_0 == LT) :
                        LA129_2 = self.input.LA(2)

                        if (self.synpred159()) :
                            alt129 = 1




                    if alt129 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT263 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1681)
                        if self.failed:
                            return retval


                    else:
                        break #loop129


                self.following.append(self.FOLLOW_statement_in_withStatement1685)
                statement264 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement264.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 41, withStatement_StartIndex)

            pass

        return retval

    # $ANTLR end withStatement

    class letStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start letStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:273:1: letStatement : 'let' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def letStatement(self, ):

        retval = self.letStatement_return()
        retval.start = self.input.LT(1)
        letStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal265 = None
        LT266 = None
        char_literal267 = None
        LT268 = None
        LT270 = None
        char_literal271 = None
        LT272 = None
        expression269 = None

        statement273 = None


        string_literal265_tree = None
        LT266_tree = None
        char_literal267_tree = None
        LT268_tree = None
        LT270_tree = None
        char_literal271_tree = None
        LT272_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:2: ( 'let' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:4: 'let' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal265 = self.input.LT(1)
                self.match(self.input, 79, self.FOLLOW_79_in_letStatement1696)
                if self.failed:
                    return retval

                string_literal265_tree = self.adaptor.createWithPayload(string_literal265)
                self.adaptor.addChild(root_0, string_literal265_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:12: ( LT )*
                while True: #loop130
                    alt130 = 2
                    LA130_0 = self.input.LA(1)

                    if (LA130_0 == LT) :
                        alt130 = 1


                    if alt130 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT266 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_letStatement1698)
                        if self.failed:
                            return retval


                    else:
                        break #loop130


                char_literal267 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_letStatement1702)
                if self.failed:
                    return retval

                char_literal267_tree = self.adaptor.createWithPayload(char_literal267)
                self.adaptor.addChild(root_0, char_literal267_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:21: ( LT )*
                while True: #loop131
                    alt131 = 2
                    LA131_0 = self.input.LA(1)

                    if (LA131_0 == LT) :
                        LA131_2 = self.input.LA(2)

                        if (self.synpred161()) :
                            alt131 = 1




                    if alt131 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT268 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_letStatement1704)
                        if self.failed:
                            return retval


                    else:
                        break #loop131


                self.following.append(self.FOLLOW_expression_in_letStatement1708)
                expression269 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression269.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:37: ( LT )*
                while True: #loop132
                    alt132 = 2
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == LT) :
                        alt132 = 1


                    if alt132 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT270 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_letStatement1710)
                        if self.failed:
                            return retval


                    else:
                        break #loop132


                char_literal271 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_letStatement1714)
                if self.failed:
                    return retval

                char_literal271_tree = self.adaptor.createWithPayload(char_literal271)
                self.adaptor.addChild(root_0, char_literal271_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:46: ( LT )*
                while True: #loop133
                    alt133 = 2
                    LA133_0 = self.input.LA(1)

                    if (LA133_0 == LT) :
                        LA133_2 = self.input.LA(2)

                        if (self.synpred163()) :
                            alt133 = 1




                    if alt133 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT272 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_letStatement1716)
                        if self.failed:
                            return retval


                    else:
                        break #loop133


                self.following.append(self.FOLLOW_statement_in_letStatement1720)
                statement273 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement273.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 42, letStatement_StartIndex)

            pass

        return retval

    # $ANTLR end letStatement

    class labelledStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start labelledStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:277:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        LT275 = None
        char_literal276 = None
        LT277 = None
        identifier274 = None

        statement278 = None


        LT275_tree = None
        char_literal276_tree = None
        LT277_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1731)
                identifier274 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier274.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:17: ( LT )*
                while True: #loop134
                    alt134 = 2
                    LA134_0 = self.input.LA(1)

                    if (LA134_0 == LT) :
                        alt134 = 1


                    if alt134 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT275 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1733)
                        if self.failed:
                            return retval


                    else:
                        break #loop134


                char_literal276 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_labelledStatement1737)
                if self.failed:
                    return retval

                char_literal276_tree = self.adaptor.createWithPayload(char_literal276)
                self.adaptor.addChild(root_0, char_literal276_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:26: ( LT )*
                while True: #loop135
                    alt135 = 2
                    LA135_0 = self.input.LA(1)

                    if (LA135_0 == LT) :
                        LA135_2 = self.input.LA(2)

                        if (self.synpred165()) :
                            alt135 = 1




                    if alt135 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT277 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1739)
                        if self.failed:
                            return retval


                    else:
                        break #loop135


                self.following.append(self.FOLLOW_statement_in_labelledStatement1743)
                statement278 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement278.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 43, labelledStatement_StartIndex)

            pass

        return retval

    # $ANTLR end labelledStatement

    class switchStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start switchStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:281:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal279 = None
        LT280 = None
        char_literal281 = None
        LT282 = None
        LT284 = None
        char_literal285 = None
        LT286 = None
        expression283 = None

        caseBlock287 = None


        string_literal279_tree = None
        LT280_tree = None
        char_literal281_tree = None
        LT282_tree = None
        LT284_tree = None
        char_literal285_tree = None
        LT286_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal279 = self.input.LT(1)
                self.match(self.input, 92, self.FOLLOW_92_in_switchStatement1755)
                if self.failed:
                    return retval

                string_literal279_tree = self.adaptor.createWithPayload(string_literal279)
                self.adaptor.addChild(root_0, string_literal279_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:15: ( LT )*
                while True: #loop136
                    alt136 = 2
                    LA136_0 = self.input.LA(1)

                    if (LA136_0 == LT) :
                        alt136 = 1


                    if alt136 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT280 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1757)
                        if self.failed:
                            return retval


                    else:
                        break #loop136


                char_literal281 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_switchStatement1761)
                if self.failed:
                    return retval

                char_literal281_tree = self.adaptor.createWithPayload(char_literal281)
                self.adaptor.addChild(root_0, char_literal281_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:24: ( LT )*
                while True: #loop137
                    alt137 = 2
                    LA137_0 = self.input.LA(1)

                    if (LA137_0 == LT) :
                        LA137_2 = self.input.LA(2)

                        if (self.synpred167()) :
                            alt137 = 1




                    if alt137 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT282 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1763)
                        if self.failed:
                            return retval


                    else:
                        break #loop137


                self.following.append(self.FOLLOW_expression_in_switchStatement1767)
                expression283 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression283.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:40: ( LT )*
                while True: #loop138
                    alt138 = 2
                    LA138_0 = self.input.LA(1)

                    if (LA138_0 == LT) :
                        alt138 = 1


                    if alt138 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT284 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1769)
                        if self.failed:
                            return retval


                    else:
                        break #loop138


                char_literal285 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_switchStatement1773)
                if self.failed:
                    return retval

                char_literal285_tree = self.adaptor.createWithPayload(char_literal285)
                self.adaptor.addChild(root_0, char_literal285_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:49: ( LT )*
                while True: #loop139
                    alt139 = 2
                    LA139_0 = self.input.LA(1)

                    if (LA139_0 == LT) :
                        alt139 = 1


                    if alt139 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT286 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1775)
                        if self.failed:
                            return retval


                    else:
                        break #loop139


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1779)
                caseBlock287 = self.caseBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, caseBlock287.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 44, switchStatement_StartIndex)

            pass

        return retval

    # $ANTLR end switchStatement

    class caseBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:285:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal288 = None
        LT289 = None
        LT291 = None
        LT293 = None
        LT295 = None
        char_literal296 = None
        caseClause290 = None

        defaultClause292 = None

        caseClause294 = None


        char_literal288_tree = None
        LT289_tree = None
        LT291_tree = None
        LT293_tree = None
        LT295_tree = None
        char_literal296_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal288 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_caseBlock1791)
                if self.failed:
                    return retval

                char_literal288_tree = self.adaptor.createWithPayload(char_literal288)
                self.adaptor.addChild(root_0, char_literal288_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:8: ( ( LT )* caseClause )*
                while True: #loop141
                    alt141 = 2
                    alt141 = self.dfa141.predict(self.input)
                    if alt141 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:11: ( LT )*
                        while True: #loop140
                            alt140 = 2
                            LA140_0 = self.input.LA(1)

                            if (LA140_0 == LT) :
                                alt140 = 1


                            if alt140 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT289 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1794)
                                if self.failed:
                                    return retval


                            else:
                                break #loop140


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1798)
                        caseClause290 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause290.tree)


                    else:
                        break #loop141


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt145 = 2
                alt145 = self.dfa145.predict(self.input)
                if alt145 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:30: ( LT )*
                    while True: #loop142
                        alt142 = 2
                        LA142_0 = self.input.LA(1)

                        if (LA142_0 == LT) :
                            alt142 = 1


                        if alt142 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT291 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1803)
                            if self.failed:
                                return retval


                        else:
                            break #loop142


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1807)
                    defaultClause292 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause292.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:47: ( ( LT )* caseClause )*
                    while True: #loop144
                        alt144 = 2
                        alt144 = self.dfa144.predict(self.input)
                        if alt144 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:50: ( LT )*
                            while True: #loop143
                                alt143 = 2
                                LA143_0 = self.input.LA(1)

                                if (LA143_0 == LT) :
                                    alt143 = 1


                                if alt143 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT293 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1810)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop143


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1814)
                            caseClause294 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause294.tree)


                        else:
                            break #loop144





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:70: ( LT )*
                while True: #loop146
                    alt146 = 2
                    LA146_0 = self.input.LA(1)

                    if (LA146_0 == LT) :
                        alt146 = 1


                    if alt146 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT295 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1820)
                        if self.failed:
                            return retval


                    else:
                        break #loop146


                char_literal296 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_caseBlock1824)
                if self.failed:
                    return retval

                char_literal296_tree = self.adaptor.createWithPayload(char_literal296)
                self.adaptor.addChild(root_0, char_literal296_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 45, caseBlock_StartIndex)

            pass

        return retval

    # $ANTLR end caseBlock

    class caseClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:289:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal297 = None
        LT298 = None
        LT300 = None
        char_literal301 = None
        LT302 = None
        expression299 = None

        statementList303 = None


        string_literal297_tree = None
        LT298_tree = None
        LT300_tree = None
        char_literal301_tree = None
        LT302_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal297 = self.input.LT(1)
                self.match(self.input, 93, self.FOLLOW_93_in_caseClause1835)
                if self.failed:
                    return retval

                string_literal297_tree = self.adaptor.createWithPayload(string_literal297)
                self.adaptor.addChild(root_0, string_literal297_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:13: ( LT )*
                while True: #loop147
                    alt147 = 2
                    LA147_0 = self.input.LA(1)

                    if (LA147_0 == LT) :
                        LA147_2 = self.input.LA(2)

                        if (self.synpred177()) :
                            alt147 = 1




                    if alt147 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT298 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1837)
                        if self.failed:
                            return retval


                    else:
                        break #loop147


                self.following.append(self.FOLLOW_expression_in_caseClause1841)
                expression299 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression299.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:29: ( LT )*
                while True: #loop148
                    alt148 = 2
                    LA148_0 = self.input.LA(1)

                    if (LA148_0 == LT) :
                        alt148 = 1


                    if alt148 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT300 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1843)
                        if self.failed:
                            return retval


                    else:
                        break #loop148


                char_literal301 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_caseClause1847)
                if self.failed:
                    return retval

                char_literal301_tree = self.adaptor.createWithPayload(char_literal301)
                self.adaptor.addChild(root_0, char_literal301_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:38: ( LT )*
                while True: #loop149
                    alt149 = 2
                    LA149_0 = self.input.LA(1)

                    if (LA149_0 == LT) :
                        LA149_2 = self.input.LA(2)

                        if (self.synpred179()) :
                            alt149 = 1




                    if alt149 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT302 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1849)
                        if self.failed:
                            return retval


                    else:
                        break #loop149


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:41: ( statementList )?
                alt150 = 2
                LA150 = self.input.LA(1)
                if LA150 == StringLiteral or LA150 == XMLComment or LA150 == NumericLiteral or LA150 == Identifier or LA150 == RegularExpressionHacks or LA150 == 60 or LA150 == 62 or LA150 == 64 or LA150 == 66 or LA150 == 68 or LA150 == 69 or LA150 == 73 or LA150 == 74 or LA150 == 75 or LA150 == 76 or LA150 == 77 or LA150 == 78 or LA150 == 79 or LA150 == 80 or LA150 == 82 or LA150 == 84 or LA150 == 85 or LA150 == 86 or LA150 == 87 or LA150 == 89 or LA150 == 90 or LA150 == 91 or LA150 == 92 or LA150 == 94 or LA150 == 95 or LA150 == 98 or LA150 == 128 or LA150 == 130 or LA150 == 131 or LA150 == 132 or LA150 == 133 or LA150 == 134 or LA150 == 135 or LA150 == 136 or LA150 == 137 or LA150 == 138 or LA150 == 139 or LA150 == 140 or LA150 == 141 or LA150 == 142:
                    alt150 = 1
                elif LA150 == LT:
                    LA150_7 = self.input.LA(2)

                    if (self.synpred180()) :
                        alt150 = 1
                elif LA150 == 72:
                    LA150_10 = self.input.LA(2)

                    if (self.synpred180()) :
                        alt150 = 1
                if alt150 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1853)
                    statementList303 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList303.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 46, caseClause_StartIndex)

            pass

        return retval

    # $ANTLR end caseClause

    class defaultClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start defaultClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:293:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal304 = None
        LT305 = None
        char_literal306 = None
        LT307 = None
        statementList308 = None


        string_literal304_tree = None
        LT305_tree = None
        char_literal306_tree = None
        LT307_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal304 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_defaultClause1866)
                if self.failed:
                    return retval

                string_literal304_tree = self.adaptor.createWithPayload(string_literal304)
                self.adaptor.addChild(root_0, string_literal304_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:16: ( LT )*
                while True: #loop151
                    alt151 = 2
                    LA151_0 = self.input.LA(1)

                    if (LA151_0 == LT) :
                        alt151 = 1


                    if alt151 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT305 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1868)
                        if self.failed:
                            return retval


                    else:
                        break #loop151


                char_literal306 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_defaultClause1872)
                if self.failed:
                    return retval

                char_literal306_tree = self.adaptor.createWithPayload(char_literal306)
                self.adaptor.addChild(root_0, char_literal306_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:25: ( LT )*
                while True: #loop152
                    alt152 = 2
                    LA152_0 = self.input.LA(1)

                    if (LA152_0 == LT) :
                        LA152_2 = self.input.LA(2)

                        if (self.synpred182()) :
                            alt152 = 1




                    if alt152 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT307 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1874)
                        if self.failed:
                            return retval


                    else:
                        break #loop152


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:28: ( statementList )?
                alt153 = 2
                alt153 = self.dfa153.predict(self.input)
                if alt153 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1878)
                    statementList308 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList308.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 47, defaultClause_StartIndex)

            pass

        return retval

    # $ANTLR end defaultClause

    class throwStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start throwStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:297:1: throwStatement : 'throw' expression ( LT | ';' ) ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal309 = None
        set311 = None
        expression310 = None


        string_literal309_tree = None
        set311_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal309 = self.input.LT(1)
                self.match(self.input, 94, self.FOLLOW_94_in_throwStatement1891)
                if self.failed:
                    return retval

                string_literal309_tree = self.adaptor.createWithPayload(string_literal309)
                self.adaptor.addChild(root_0, string_literal309_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1893)
                expression310 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression310.tree)
                set311 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 75:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_throwStatement1895
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
            if self.backtracking > 0:
                self.memoize(self.input, 48, throwStatement_StartIndex)

            pass

        return retval

    # $ANTLR end throwStatement

    class tryStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start tryStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:301:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal312 = None
        LT313 = None
        LT315 = None
        LT318 = None
        statementBlock314 = None

        finallyClause316 = None

        catchClause317 = None

        finallyClause319 = None


        string_literal312_tree = None
        LT313_tree = None
        LT315_tree = None
        LT318_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal312 = self.input.LT(1)
                self.match(self.input, 95, self.FOLLOW_95_in_tryStatement1913)
                if self.failed:
                    return retval

                string_literal312_tree = self.adaptor.createWithPayload(string_literal312)
                self.adaptor.addChild(root_0, string_literal312_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:12: ( LT )*
                while True: #loop154
                    alt154 = 2
                    LA154_0 = self.input.LA(1)

                    if (LA154_0 == LT) :
                        alt154 = 1


                    if alt154 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT313 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1915)
                        if self.failed:
                            return retval


                    else:
                        break #loop154


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1919)
                statementBlock314 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock314.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:32: ( LT )*
                while True: #loop155
                    alt155 = 2
                    LA155_0 = self.input.LA(1)

                    if (LA155_0 == LT) :
                        alt155 = 1


                    if alt155 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT315 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1921)
                        if self.failed:
                            return retval


                    else:
                        break #loop155


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt158 = 2
                LA158_0 = self.input.LA(1)

                if (LA158_0 == 97) :
                    alt158 = 1
                elif (LA158_0 == 96) :
                    alt158 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("302:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 158, 0, self.input)

                    raise nvae

                if alt158 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1926)
                    finallyClause316 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause316.tree)


                elif alt158 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1930)
                    catchClause317 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause317.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:64: ( ( LT )* finallyClause )?
                    alt157 = 2
                    alt157 = self.dfa157.predict(self.input)
                    if alt157 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:67: ( LT )*
                        while True: #loop156
                            alt156 = 2
                            LA156_0 = self.input.LA(1)

                            if (LA156_0 == LT) :
                                alt156 = 1


                            if alt156 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT318 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1933)
                                if self.failed:
                                    return retval


                            else:
                                break #loop156


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1937)
                        finallyClause319 = self.finallyClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, finallyClause319.tree)









                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 49, tryStatement_StartIndex)

            pass

        return retval

    # $ANTLR end tryStatement

    class catchClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start catchClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:305:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal320 = None
        LT321 = None
        char_literal322 = None
        LT323 = None
        LT325 = None
        char_literal326 = None
        LT327 = None
        identifier324 = None

        statementBlock328 = None


        string_literal320_tree = None
        LT321_tree = None
        char_literal322_tree = None
        LT323_tree = None
        LT325_tree = None
        char_literal326_tree = None
        LT327_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal320 = self.input.LT(1)
                self.match(self.input, 96, self.FOLLOW_96_in_catchClause1958)
                if self.failed:
                    return retval

                string_literal320_tree = self.adaptor.createWithPayload(string_literal320)
                self.adaptor.addChild(root_0, string_literal320_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:14: ( LT )*
                while True: #loop159
                    alt159 = 2
                    LA159_0 = self.input.LA(1)

                    if (LA159_0 == LT) :
                        alt159 = 1


                    if alt159 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT321 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1960)
                        if self.failed:
                            return retval


                    else:
                        break #loop159


                char_literal322 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_catchClause1964)
                if self.failed:
                    return retval

                char_literal322_tree = self.adaptor.createWithPayload(char_literal322)
                self.adaptor.addChild(root_0, char_literal322_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:23: ( LT )*
                while True: #loop160
                    alt160 = 2
                    LA160_0 = self.input.LA(1)

                    if (LA160_0 == LT) :
                        alt160 = 1


                    if alt160 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT323 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1966)
                        if self.failed:
                            return retval


                    else:
                        break #loop160


                self.following.append(self.FOLLOW_identifier_in_catchClause1970)
                identifier324 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier324.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:39: ( LT )*
                while True: #loop161
                    alt161 = 2
                    LA161_0 = self.input.LA(1)

                    if (LA161_0 == LT) :
                        alt161 = 1


                    if alt161 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT325 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1972)
                        if self.failed:
                            return retval


                    else:
                        break #loop161


                char_literal326 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_catchClause1976)
                if self.failed:
                    return retval

                char_literal326_tree = self.adaptor.createWithPayload(char_literal326)
                self.adaptor.addChild(root_0, char_literal326_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:48: ( LT )*
                while True: #loop162
                    alt162 = 2
                    LA162_0 = self.input.LA(1)

                    if (LA162_0 == LT) :
                        alt162 = 1


                    if alt162 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT327 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1978)
                        if self.failed:
                            return retval


                    else:
                        break #loop162


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1982)
                statementBlock328 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock328.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 50, catchClause_StartIndex)

            pass

        return retval

    # $ANTLR end catchClause

    class finallyClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start finallyClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal329 = None
        LT330 = None
        statementBlock331 = None


        string_literal329_tree = None
        LT330_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal329 = self.input.LT(1)
                self.match(self.input, 97, self.FOLLOW_97_in_finallyClause1994)
                if self.failed:
                    return retval

                string_literal329_tree = self.adaptor.createWithPayload(string_literal329)
                self.adaptor.addChild(root_0, string_literal329_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:16: ( LT )*
                while True: #loop163
                    alt163 = 2
                    LA163_0 = self.input.LA(1)

                    if (LA163_0 == LT) :
                        alt163 = 1


                    if alt163 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT330 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1996)
                        if self.failed:
                            return retval


                    else:
                        break #loop163


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause2000)
                statementBlock331 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock331.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 51, finallyClause_StartIndex)

            pass

        return retval

    # $ANTLR end finallyClause

    class expression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT333 = None
        char_literal334 = None
        LT335 = None
        assignmentExpression332 = None

        assignmentExpression336 = None


        LT333_tree = None
        char_literal334_tree = None
        LT335_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression2012)
                assignmentExpression332 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression332.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop166
                    alt166 = 2
                    LA166_0 = self.input.LA(1)

                    if (LA166_0 == LT) :
                        LA166_2 = self.input.LA(2)

                        if (self.synpred197()) :
                            alt166 = 1


                    elif (LA166_0 == 70) :
                        LA166_3 = self.input.LA(2)

                        if (self.synpred197()) :
                            alt166 = 1




                    if alt166 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:28: ( LT )*
                        while True: #loop164
                            alt164 = 2
                            LA164_0 = self.input.LA(1)

                            if (LA164_0 == LT) :
                                alt164 = 1


                            if alt164 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT333 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression2015)
                                if self.failed:
                                    return retval


                            else:
                                break #loop164


                        char_literal334 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_expression2019)
                        if self.failed:
                            return retval

                        char_literal334_tree = self.adaptor.createWithPayload(char_literal334)
                        self.adaptor.addChild(root_0, char_literal334_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:37: ( LT )*
                        while True: #loop165
                            alt165 = 2
                            LA165_0 = self.input.LA(1)

                            if (LA165_0 == LT) :
                                LA165_2 = self.input.LA(2)

                                if (self.synpred196()) :
                                    alt165 = 1




                            if alt165 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT335 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression2021)
                                if self.failed:
                                    return retval


                            else:
                                break #loop165


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression2025)
                        assignmentExpression336 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression336.tree)


                    else:
                        break #loop166





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 52, expression_StartIndex)

            pass

        return retval

    # $ANTLR end expression

    class expressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT338 = None
        char_literal339 = None
        LT340 = None
        assignmentExpressionNoIn337 = None

        assignmentExpressionNoIn341 = None


        LT338_tree = None
        char_literal339_tree = None
        LT340_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn2039)
                assignmentExpressionNoIn337 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn337.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop169
                    alt169 = 2
                    alt169 = self.dfa169.predict(self.input)
                    if alt169 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:32: ( LT )*
                        while True: #loop167
                            alt167 = 2
                            LA167_0 = self.input.LA(1)

                            if (LA167_0 == LT) :
                                alt167 = 1


                            if alt167 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT338 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn2042)
                                if self.failed:
                                    return retval


                            else:
                                break #loop167


                        char_literal339 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_expressionNoIn2046)
                        if self.failed:
                            return retval

                        char_literal339_tree = self.adaptor.createWithPayload(char_literal339)
                        self.adaptor.addChild(root_0, char_literal339_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:41: ( LT )*
                        while True: #loop168
                            alt168 = 2
                            LA168_0 = self.input.LA(1)

                            if (LA168_0 == LT) :
                                LA168_2 = self.input.LA(2)

                                if (self.synpred199()) :
                                    alt168 = 1




                            if alt168 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT340 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn2048)
                                if self.failed:
                                    return retval


                            else:
                                break #loop168


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn2052)
                        assignmentExpressionNoIn341 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn341.tree)


                    else:
                        break #loop169





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 53, expressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end expressionNoIn

    class assignmentExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT343 = None
        LT345 = None
        leftHandSideExpression342 = None

        assignmentOperator344 = None

        assignmentExpression346 = None

        conditionalExpression347 = None


        LT343_tree = None
        LT345_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_assignmentOperator = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentOperator")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self.adaptor, "rule leftHandSideExpression")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression )
                alt172 = 2
                LA172 = self.input.LA(1)
                if LA172 == 137:
                    LA172_1 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 1, self.input)

                        raise nvae

                elif LA172 == LT:
                    LA172_2 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 2, self.input)

                        raise nvae

                elif LA172 == 60:
                    LA172_3 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 3, self.input)

                        raise nvae

                elif LA172 == 66:
                    LA172_4 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 4, self.input)

                        raise nvae

                elif LA172 == XMLComment:
                    LA172_5 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 5, self.input)

                        raise nvae

                elif LA172 == Identifier or LA172 == 72 or LA172 == 73 or LA172 == 74 or LA172 == 87 or LA172 == 138 or LA172 == 139:
                    LA172_6 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 6, self.input)

                        raise nvae

                elif LA172 == 140:
                    LA172_7 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 7, self.input)

                        raise nvae

                elif LA172 == 141:
                    LA172_8 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 8, self.input)

                        raise nvae

                elif LA172 == 142:
                    LA172_9 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 9, self.input)

                        raise nvae

                elif LA172 == StringLiteral:
                    LA172_10 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 10, self.input)

                        raise nvae

                elif LA172 == NumericLiteral:
                    LA172_11 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 11, self.input)

                        raise nvae

                elif LA172 == 62:
                    LA172_12 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 12, self.input)

                        raise nvae

                elif LA172 == RegularExpressionHacks:
                    LA172_13 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 13, self.input)

                        raise nvae

                elif LA172 == 80:
                    LA172_14 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 14, self.input)

                        raise nvae

                elif LA172 == 69:
                    LA172_15 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 15, self.input)

                        raise nvae

                elif LA172 == 68:
                    LA172_16 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 16, self.input)

                        raise nvae

                elif LA172 == 98:
                    LA172_17 = self.input.LA(2)

                    if (self.synpred203()) :
                        alt172 = 1
                    elif (True) :
                        alt172 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 17, self.input)

                        raise nvae

                elif LA172 == 64 or LA172 == 128 or LA172 == 130 or LA172 == 131 or LA172 == 132 or LA172 == 133 or LA172 == 134 or LA172 == 135 or LA172 == 136:
                    alt172 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("322:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 172, 0, self.input)

                    raise nvae

                if alt172 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression2066)
                    leftHandSideExpression342 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression342.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:27: ( LT )*
                    while True: #loop170
                        alt170 = 2
                        LA170_0 = self.input.LA(1)

                        if (LA170_0 == LT) :
                            alt170 = 1


                        if alt170 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT343 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression2068)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT343)


                        else:
                            break #loop170


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression2071)
                    assignmentOperator344 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentOperator.add(assignmentOperator344.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:50: ( LT )*
                    while True: #loop171
                        alt171 = 2
                        LA171_0 = self.input.LA(1)

                        if (LA171_0 == LT) :
                            LA171_2 = self.input.LA(2)

                            if (self.synpred202()) :
                                alt171 = 1




                        if alt171 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT345 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression2073)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT345)


                        else:
                            break #loop171


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression2076)
                    assignmentExpression346 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression346.tree)
                    # AST Rewrite
                    # elements: leftHandSideExpression, assignmentExpression, assignmentOperator
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
                        # 324:3: -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:6: ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ASSIGN, "ASSIGN"), root_1)

                        self.adaptor.addChild(root_1, stream_leftHandSideExpression.next())
                        self.adaptor.addChild(root_1, stream_assignmentOperator.next())
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt172 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:325:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression2095)
                    conditionalExpression347 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression347.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 54, assignmentExpression_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpression

    class assignmentExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT349 = None
        LT351 = None
        leftHandSideExpression348 = None

        assignmentOperator350 = None

        assignmentExpressionNoIn352 = None

        conditionalExpressionNoIn353 = None


        LT349_tree = None
        LT351_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_assignmentOperator = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentOperator")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self.adaptor, "rule leftHandSideExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn )
                alt175 = 2
                LA175 = self.input.LA(1)
                if LA175 == 137:
                    LA175_1 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 1, self.input)

                        raise nvae

                elif LA175 == LT:
                    LA175_2 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 2, self.input)

                        raise nvae

                elif LA175 == 60:
                    LA175_3 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 3, self.input)

                        raise nvae

                elif LA175 == 66:
                    LA175_4 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 4, self.input)

                        raise nvae

                elif LA175 == XMLComment:
                    LA175_5 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 5, self.input)

                        raise nvae

                elif LA175 == Identifier or LA175 == 72 or LA175 == 73 or LA175 == 74 or LA175 == 87 or LA175 == 138 or LA175 == 139:
                    LA175_6 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 6, self.input)

                        raise nvae

                elif LA175 == 140:
                    LA175_7 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 7, self.input)

                        raise nvae

                elif LA175 == 141:
                    LA175_8 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 8, self.input)

                        raise nvae

                elif LA175 == 142:
                    LA175_9 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 9, self.input)

                        raise nvae

                elif LA175 == StringLiteral:
                    LA175_10 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 10, self.input)

                        raise nvae

                elif LA175 == NumericLiteral:
                    LA175_11 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 11, self.input)

                        raise nvae

                elif LA175 == 62:
                    LA175_12 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 12, self.input)

                        raise nvae

                elif LA175 == RegularExpressionHacks:
                    LA175_13 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 13, self.input)

                        raise nvae

                elif LA175 == 80:
                    LA175_14 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 14, self.input)

                        raise nvae

                elif LA175 == 69:
                    LA175_15 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 15, self.input)

                        raise nvae

                elif LA175 == 68:
                    LA175_16 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 16, self.input)

                        raise nvae

                elif LA175 == 98:
                    LA175_17 = self.input.LA(2)

                    if (self.synpred206()) :
                        alt175 = 1
                    elif (True) :
                        alt175 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 17, self.input)

                        raise nvae

                elif LA175 == 64 or LA175 == 128 or LA175 == 130 or LA175 == 131 or LA175 == 132 or LA175 == 133 or LA175 == 134 or LA175 == 135 or LA175 == 136:
                    alt175 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("328:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 175, 0, self.input)

                    raise nvae

                if alt175 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn2107)
                    leftHandSideExpression348 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression348.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:27: ( LT )*
                    while True: #loop173
                        alt173 = 2
                        LA173_0 = self.input.LA(1)

                        if (LA173_0 == LT) :
                            alt173 = 1


                        if alt173 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT349 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn2109)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT349)


                        else:
                            break #loop173


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn2112)
                    assignmentOperator350 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentOperator.add(assignmentOperator350.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:50: ( LT )*
                    while True: #loop174
                        alt174 = 2
                        LA174_0 = self.input.LA(1)

                        if (LA174_0 == LT) :
                            LA174_2 = self.input.LA(2)

                            if (self.synpred205()) :
                                alt174 = 1




                        if alt174 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT351 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn2114)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT351)


                        else:
                            break #loop174


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn2117)
                    assignmentExpressionNoIn352 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn352.tree)
                    # AST Rewrite
                    # elements: assignmentOperator, leftHandSideExpression, assignmentExpressionNoIn
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
                        # 330:3: -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:6: ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ASSIGN, "ASSIGN"), root_1)

                        self.adaptor.addChild(root_1, stream_leftHandSideExpression.next())
                        self.adaptor.addChild(root_1, stream_assignmentOperator.next())
                        self.adaptor.addChild(root_1, stream_assignmentExpressionNoIn.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt175 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn2136)
                    conditionalExpressionNoIn353 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn353.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 55, assignmentExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpressionNoIn

    class leftHandSideExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start leftHandSideExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression354 = None

        newExpression355 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:2: ( callExpression | newExpression )
                alt176 = 2
                LA176 = self.input.LA(1)
                if LA176 == 137:
                    LA176_1 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 1, self.input)

                        raise nvae

                elif LA176 == LT:
                    LA176_2 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 2, self.input)

                        raise nvae

                elif LA176 == 60:
                    LA176_3 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 3, self.input)

                        raise nvae

                elif LA176 == 66:
                    LA176_4 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 4, self.input)

                        raise nvae

                elif LA176 == XMLComment:
                    LA176_5 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 5, self.input)

                        raise nvae

                elif LA176 == Identifier or LA176 == 72 or LA176 == 73 or LA176 == 74 or LA176 == 87 or LA176 == 138 or LA176 == 139:
                    LA176_6 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 6, self.input)

                        raise nvae

                elif LA176 == 140:
                    LA176_7 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 7, self.input)

                        raise nvae

                elif LA176 == 141:
                    LA176_8 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 8, self.input)

                        raise nvae

                elif LA176 == 142:
                    LA176_9 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 9, self.input)

                        raise nvae

                elif LA176 == StringLiteral:
                    LA176_10 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 10, self.input)

                        raise nvae

                elif LA176 == NumericLiteral:
                    LA176_11 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 11, self.input)

                        raise nvae

                elif LA176 == 62:
                    LA176_12 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 12, self.input)

                        raise nvae

                elif LA176 == RegularExpressionHacks:
                    LA176_13 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 13, self.input)

                        raise nvae

                elif LA176 == 80:
                    LA176_14 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 14, self.input)

                        raise nvae

                elif LA176 == 69:
                    LA176_15 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 15, self.input)

                        raise nvae

                elif LA176 == 68:
                    LA176_16 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 16, self.input)

                        raise nvae

                elif LA176 == 98:
                    LA176_17 = self.input.LA(2)

                    if (self.synpred207()) :
                        alt176 = 1
                    elif (True) :
                        alt176 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("334:1: leftHandSideExpression : ( callExpression | newExpression );", 176, 0, self.input)

                    raise nvae

                if alt176 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression2148)
                    callExpression354 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression354.tree)


                elif alt176 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:336:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression2153)
                    newExpression355 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression355.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 56, leftHandSideExpression_StartIndex)

            pass

        return retval

    # $ANTLR end leftHandSideExpression

    class newExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start newExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal357 = None
        LT358 = None
        memberExpression356 = None

        newExpression359 = None


        string_literal357_tree = None
        LT358_tree = None
        stream_98 = RewriteRuleTokenStream(self.adaptor, "token 98")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_newExpression = RewriteRuleSubtreeStream(self.adaptor, "rule newExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:340:2: ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) )
                alt178 = 2
                LA178_0 = self.input.LA(1)

                if ((LT <= LA178_0 <= RegularExpressionHacks) or LA178_0 == 60 or LA178_0 == 62 or LA178_0 == 66 or (68 <= LA178_0 <= 69) or (72 <= LA178_0 <= 74) or LA178_0 == 80 or LA178_0 == 87 or (137 <= LA178_0 <= 142)) :
                    alt178 = 1
                elif (LA178_0 == 98) :
                    LA178_17 = self.input.LA(2)

                    if (self.synpred208()) :
                        alt178 = 1
                    elif (True) :
                        alt178 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("339:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );", 178, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("339:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );", 178, 0, self.input)

                    raise nvae

                if alt178 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:340:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression2165)
                    memberExpression356 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression356.tree)


                elif alt178 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:4: 'new' ( LT )* newExpression
                    string_literal357 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_newExpression2170)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_98.add(string_literal357)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:10: ( LT )*
                    while True: #loop177
                        alt177 = 2
                        LA177_0 = self.input.LA(1)

                        if (LA177_0 == LT) :
                            LA177_2 = self.input.LA(2)

                            if (self.synpred209()) :
                                alt177 = 1




                        if alt177 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT358 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression2172)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT358)


                        else:
                            break #loop177


                    self.following.append(self.FOLLOW_newExpression_in_newExpression2175)
                    newExpression359 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_newExpression.add(newExpression359.tree)
                    # AST Rewrite
                    # elements: newExpression
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
                        # 342:3: -> ^( NEW newExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:6: ^( NEW newExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NEW, "NEW"), root_1)

                        self.adaptor.addChild(root_1, stream_newExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 57, newExpression_StartIndex)

            pass

        return retval

    # $ANTLR end newExpression

    class memberExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:345:1: memberExpression : ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) );
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        LT361 = None
        LT364 = None
        string_literal366 = None
        LT367 = None
        LT369 = None
        LT371 = None
        primaryExpression360 = None

        memberExpressionSuffix362 = None

        functionExpression363 = None

        memberExpressionSuffix365 = None

        memberExpression368 = None

        arguments370 = None

        memberExpressionSuffix372 = None


        LT361_tree = None
        LT364_tree = None
        string_literal366_tree = None
        LT367_tree = None
        LT369_tree = None
        LT371_tree = None
        stream_98 = RewriteRuleTokenStream(self.adaptor, "token 98")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_primaryExpression = RewriteRuleSubtreeStream(self.adaptor, "rule primaryExpression")
        stream_memberExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:2: ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) )
                alt187 = 3
                LA187 = self.input.LA(1)
                if LA187 == LT or LA187 == StringLiteral or LA187 == XMLComment or LA187 == NumericLiteral or LA187 == Identifier or LA187 == RegularExpressionHacks or LA187 == 60 or LA187 == 62 or LA187 == 66 or LA187 == 69 or LA187 == 72 or LA187 == 73 or LA187 == 74 or LA187 == 80 or LA187 == 87 or LA187 == 137 or LA187 == 138 or LA187 == 139 or LA187 == 140 or LA187 == 141 or LA187 == 142:
                    alt187 = 1
                elif LA187 == 68:
                    alt187 = 2
                elif LA187 == 98:
                    alt187 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("345:1: memberExpression : ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) );", 187, 0, self.input)

                    raise nvae

                if alt187 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:4: primaryExpression ( ( LT )* memberExpressionSuffix )*
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression2197)
                    primaryExpression360 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_primaryExpression.add(primaryExpression360.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:22: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop180
                        alt180 = 2
                        LA180 = self.input.LA(1)
                        if LA180 == LT:
                            LA180_1 = self.input.LA(2)

                            if (self.synpred211()) :
                                alt180 = 1


                        elif LA180 == 80:
                            LA180_20 = self.input.LA(2)

                            if (self.synpred211()) :
                                alt180 = 1


                        elif LA180 == 99:
                            LA180_21 = self.input.LA(2)

                            if (self.synpred211()) :
                                alt180 = 1


                        elif LA180 == 63:
                            LA180_22 = self.input.LA(2)

                            if (self.synpred211()) :
                                alt180 = 1



                        if alt180 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( LT )*
                            while True: #loop179
                                alt179 = 2
                                LA179_0 = self.input.LA(1)

                                if (LA179_0 == LT) :
                                    alt179 = 1


                                if alt179 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT361 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2200)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT361)


                                else:
                                    break #loop179


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression2203)
                            memberExpressionSuffix362 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_memberExpressionSuffix.add(memberExpressionSuffix362.tree)


                        else:
                            break #loop180


                    # AST Rewrite
                    # elements: primaryExpression, memberExpressionSuffix
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
                        # 347:3: -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:6: ^( VEXPR primaryExpression ( memberExpressionSuffix )* )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VEXPR, "VEXPR"), root_1)

                        self.adaptor.addChild(root_1, stream_primaryExpression.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:32: ( memberExpressionSuffix )*
                        while stream_memberExpressionSuffix.hasNext():
                            self.adaptor.addChild(root_1, stream_memberExpressionSuffix.next())


                        stream_memberExpressionSuffix.reset();

                        self.adaptor.addChild(root_0, root_1)





                elif alt187 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:4: functionExpression ( ( LT )* memberExpressionSuffix )*
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression2223)
                    functionExpression363 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression363.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:23: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop182
                        alt182 = 2
                        LA182 = self.input.LA(1)
                        if LA182 == LT:
                            LA182_1 = self.input.LA(2)

                            if (self.synpred214()) :
                                alt182 = 1


                        elif LA182 == 80:
                            LA182_3 = self.input.LA(2)

                            if (self.synpred214()) :
                                alt182 = 1


                        elif LA182 == 99:
                            LA182_4 = self.input.LA(2)

                            if (self.synpred214()) :
                                alt182 = 1


                        elif LA182 == 63:
                            LA182_5 = self.input.LA(2)

                            if (self.synpred214()) :
                                alt182 = 1



                        if alt182 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:24: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:26: ( LT )*
                            while True: #loop181
                                alt181 = 2
                                LA181_0 = self.input.LA(1)

                                if (LA181_0 == LT) :
                                    alt181 = 1


                                if alt181 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT364 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2226)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop181


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression2230)
                            memberExpressionSuffix365 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, memberExpressionSuffix365.tree)


                        else:
                            break #loop182




                elif alt187 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:4: 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )*
                    string_literal366 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_memberExpression2237)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_98.add(string_literal366)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:10: ( LT )*
                    while True: #loop183
                        alt183 = 2
                        LA183_0 = self.input.LA(1)

                        if (LA183_0 == LT) :
                            LA183_2 = self.input.LA(2)

                            if (self.synpred216()) :
                                alt183 = 1




                        if alt183 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT367 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2239)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT367)


                        else:
                            break #loop183


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression2242)
                    memberExpression368 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_memberExpression.add(memberExpression368.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:31: ( LT )*
                    while True: #loop184
                        alt184 = 2
                        LA184_0 = self.input.LA(1)

                        if (LA184_0 == LT) :
                            alt184 = 1


                        if alt184 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT369 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2244)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT369)


                        else:
                            break #loop184


                    self.following.append(self.FOLLOW_arguments_in_memberExpression2247)
                    arguments370 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_arguments.add(arguments370.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:45: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop186
                        alt186 = 2
                        LA186 = self.input.LA(1)
                        if LA186 == LT:
                            LA186_1 = self.input.LA(2)

                            if (self.synpred219()) :
                                alt186 = 1


                        elif LA186 == 80:
                            LA186_20 = self.input.LA(2)

                            if (self.synpred219()) :
                                alt186 = 1


                        elif LA186 == 99:
                            LA186_21 = self.input.LA(2)

                            if (self.synpred219()) :
                                alt186 = 1


                        elif LA186 == 63:
                            LA186_22 = self.input.LA(2)

                            if (self.synpred219()) :
                                alt186 = 1



                        if alt186 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:46: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:46: ( LT )*
                            while True: #loop185
                                alt185 = 2
                                LA185_0 = self.input.LA(1)

                                if (LA185_0 == LT) :
                                    alt185 = 1


                                if alt185 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT371 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2250)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT371)


                                else:
                                    break #loop185


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression2253)
                            memberExpressionSuffix372 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_memberExpressionSuffix.add(memberExpressionSuffix372.tree)


                        else:
                            break #loop186


                    # AST Rewrite
                    # elements: memberExpressionSuffix, memberExpression, arguments
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
                        # 350:3: -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:6: ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VEXPR, "VEXPR"), root_1)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:14: ^( NEW ^( CALL memberExpression arguments ) )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(NEW, "NEW"), root_2)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:20: ^( CALL memberExpression arguments )
                        root_3 = self.adaptor.nil()
                        root_3 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_3)

                        self.adaptor.addChild(root_3, stream_memberExpression.next())
                        self.adaptor.addChild(root_3, stream_arguments.next())

                        self.adaptor.addChild(root_2, root_3)

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:56: ( memberExpressionSuffix )*
                        while stream_memberExpressionSuffix.hasNext():
                            self.adaptor.addChild(root_1, stream_memberExpressionSuffix.next())


                        stream_memberExpressionSuffix.reset();

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 58, memberExpression_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpression

    class memberExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix373 = None

        propertyReferenceSuffix374 = None

        descendentSuffix375 = None

        namespaceSuffix376 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:2: ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt188 = 4
                LA188 = self.input.LA(1)
                if LA188 == 80:
                    alt188 = 1
                elif LA188 == 99:
                    LA188_2 = self.input.LA(2)

                    if (LA188_2 == 99) :
                        alt188 = 3
                    elif (LA188_2 == LT or LA188_2 == Identifier or (72 <= LA188_2 <= 74) or LA188_2 == 87 or LA188_2 == 100 or (138 <= LA188_2 <= 139)) :
                        alt188 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("353:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 188, 2, self.input)

                        raise nvae

                elif LA188 == 63:
                    alt188 = 4
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("353:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 188, 0, self.input)

                    raise nvae

                if alt188 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix2290)
                    indexSuffix373 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix373.tree)


                elif alt188 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix2295)
                    propertyReferenceSuffix374 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix374.tree)


                elif alt188 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:356:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_memberExpressionSuffix2300)
                    descendentSuffix375 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix375.tree)


                elif alt188 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:357:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_memberExpressionSuffix2306)
                    namespaceSuffix376 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix376.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 59, memberExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpressionSuffix

    class callExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:1: callExpression : memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT378 = None
        char_literal379 = None
        LT380 = None
        LT382 = None
        memberExpression377 = None

        arguments381 = None

        callExpressionSuffix383 = None


        LT378_tree = None
        char_literal379_tree = None
        LT380_tree = None
        LT382_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_99 = RewriteRuleTokenStream(self.adaptor, "token 99")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_callExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule callExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:2: ( memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:4: memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                self.following.append(self.FOLLOW_memberExpression_in_callExpression2321)
                memberExpression377 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_memberExpression.add(memberExpression377.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:21: ( LT )*
                while True: #loop189
                    alt189 = 2
                    LA189_0 = self.input.LA(1)

                    if (LA189_0 == LT) :
                        LA189_2 = self.input.LA(2)

                        if (self.synpred223()) :
                            alt189 = 1




                    if alt189 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT378 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2323)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT378)


                    else:
                        break #loop189


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:25: ( '.' )?
                alt190 = 2
                LA190_0 = self.input.LA(1)

                if (LA190_0 == 99) :
                    alt190 = 1
                if alt190 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: '.'
                    char_literal379 = self.input.LT(1)
                    self.match(self.input, 99, self.FOLLOW_99_in_callExpression2326)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_99.add(char_literal379)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:30: ( LT )*
                while True: #loop191
                    alt191 = 2
                    LA191_0 = self.input.LA(1)

                    if (LA191_0 == LT) :
                        alt191 = 1


                    if alt191 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT380 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2329)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT380)


                    else:
                        break #loop191


                self.following.append(self.FOLLOW_arguments_in_callExpression2332)
                arguments381 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_arguments.add(arguments381.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:44: ( ( LT )* callExpressionSuffix )*
                while True: #loop193
                    alt193 = 2
                    LA193 = self.input.LA(1)
                    if LA193 == LT:
                        LA193_1 = self.input.LA(2)

                        if (self.synpred227()) :
                            alt193 = 1


                    elif LA193 == 80:
                        LA193_20 = self.input.LA(2)

                        if (self.synpred227()) :
                            alt193 = 1


                    elif LA193 == 99:
                        LA193_21 = self.input.LA(2)

                        if (self.synpred227()) :
                            alt193 = 1


                    elif LA193 == 63:
                        LA193_22 = self.input.LA(2)

                        if (self.synpred227()) :
                            alt193 = 1


                    elif LA193 == 69:
                        LA193_23 = self.input.LA(2)

                        if (self.synpred227()) :
                            alt193 = 1



                    if alt193 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:45: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:45: ( LT )*
                        while True: #loop192
                            alt192 = 2
                            LA192_0 = self.input.LA(1)

                            if (LA192_0 == LT) :
                                alt192 = 1


                            if alt192 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT382 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2335)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT382)


                            else:
                                break #loop192


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression2338)
                        callExpressionSuffix383 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_callExpressionSuffix.add(callExpressionSuffix383.tree)


                    else:
                        break #loop193


                # AST Rewrite
                # elements: memberExpression, callExpressionSuffix, arguments
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
                    # 365:3: -> ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:365:6: ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_1)

                    self.adaptor.addChild(root_1, stream_memberExpression.next())
                    self.adaptor.addChild(root_1, stream_arguments.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:365:40: ( callExpressionSuffix )*
                    while stream_callExpressionSuffix.hasNext():
                        self.adaptor.addChild(root_1, stream_callExpressionSuffix.next())


                    stream_callExpressionSuffix.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 60, callExpression_StartIndex)

            pass

        return retval

    # $ANTLR end callExpression

    class callExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments384 = None

        indexSuffix385 = None

        propertyReferenceSuffix386 = None

        descendentSuffix387 = None

        namespaceSuffix388 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:2: ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt194 = 5
                LA194 = self.input.LA(1)
                if LA194 == 69:
                    alt194 = 1
                elif LA194 == 80:
                    alt194 = 2
                elif LA194 == 99:
                    LA194_3 = self.input.LA(2)

                    if (LA194_3 == 99) :
                        alt194 = 4
                    elif (LA194_3 == LT or LA194_3 == Identifier or (72 <= LA194_3 <= 74) or LA194_3 == 87 or LA194_3 == 100 or (138 <= LA194_3 <= 139)) :
                        alt194 = 3
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("368:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 194, 3, self.input)

                        raise nvae

                elif LA194 == 63:
                    alt194 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("368:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 194, 0, self.input)

                    raise nvae

                if alt194 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix2367)
                    arguments384 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments384.tree)


                elif alt194 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:370:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix2372)
                    indexSuffix385 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix385.tree)


                elif alt194 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2377)
                    propertyReferenceSuffix386 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix386.tree)


                elif alt194 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:372:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_callExpressionSuffix2382)
                    descendentSuffix387 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix387.tree)


                elif alt194 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_callExpressionSuffix2388)
                    namespaceSuffix388 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix388.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 61, callExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end callExpressionSuffix

    class arguments_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arguments
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:1: arguments : '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' -> ^( ARGS ( assignmentExpression )* ) ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal389 = None
        LT390 = None
        LT392 = None
        char_literal393 = None
        LT394 = None
        LT396 = None
        LT397 = None
        char_literal398 = None
        assignmentExpression391 = None

        assignmentExpression395 = None


        char_literal389_tree = None
        LT390_tree = None
        LT392_tree = None
        char_literal393_tree = None
        LT394_tree = None
        LT396_tree = None
        LT397_tree = None
        char_literal398_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self.adaptor, "token 71")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:2: ( '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' -> ^( ARGS ( assignmentExpression )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:4: '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')'
                char_literal389 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_arguments2403)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal389)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:8: ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )?
                alt200 = 2
                alt200 = self.dfa200.predict(self.input)
                if alt200 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:9: ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:9: ( LT )*
                    while True: #loop195
                        alt195 = 2
                        LA195_0 = self.input.LA(1)

                        if (LA195_0 == LT) :
                            LA195_2 = self.input.LA(2)

                            if (self.synpred232()) :
                                alt195 = 1




                        if alt195 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT390 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2406)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT390)


                        else:
                            break #loop195


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments2409)
                    assignmentExpression391 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression391.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:34: ( LT )*
                    while True: #loop196
                        alt196 = 2
                        LA196_0 = self.input.LA(1)

                        if (LA196_0 == LT) :
                            LA196_2 = self.input.LA(2)

                            if (self.synpred233()) :
                                alt196 = 1




                        if alt196 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT392 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2411)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT392)


                        else:
                            break #loop196


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:38: ( ',' ( LT )* assignmentExpression ( LT )* )*
                    while True: #loop199
                        alt199 = 2
                        LA199_0 = self.input.LA(1)

                        if (LA199_0 == 70) :
                            alt199 = 1


                        if alt199 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:39: ',' ( LT )* assignmentExpression ( LT )*
                            char_literal393 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_arguments2415)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal393)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:43: ( LT )*
                            while True: #loop197
                                alt197 = 2
                                LA197_0 = self.input.LA(1)

                                if (LA197_0 == LT) :
                                    LA197_2 = self.input.LA(2)

                                    if (self.synpred234()) :
                                        alt197 = 1




                                if alt197 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT394 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2417)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT394)


                                else:
                                    break #loop197


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments2420)
                            assignmentExpression395 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression395.tree)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:68: ( LT )*
                            while True: #loop198
                                alt198 = 2
                                LA198_0 = self.input.LA(1)

                                if (LA198_0 == LT) :
                                    LA198_1 = self.input.LA(2)

                                    if (self.synpred235()) :
                                        alt198 = 1




                                if alt198 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT396 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2422)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT396)


                                else:
                                    break #loop198




                        else:
                            break #loop199





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:76: ( LT )*
                while True: #loop201
                    alt201 = 2
                    LA201_0 = self.input.LA(1)

                    if (LA201_0 == LT) :
                        alt201 = 1


                    if alt201 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT397 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments2429)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT397)


                    else:
                        break #loop201


                char_literal398 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_arguments2432)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_71.add(char_literal398)
                # AST Rewrite
                # elements: assignmentExpression
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
                    # 381:3: -> ^( ARGS ( assignmentExpression )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:6: ^( ARGS ( assignmentExpression )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARGS, "ARGS"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:13: ( assignmentExpression )*
                    while stream_assignmentExpression.hasNext():
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())


                    stream_assignmentExpression.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 62, arguments_StartIndex)

            pass

        return retval

    # $ANTLR end arguments

    class indexSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start indexSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal399 = None
        LT400 = None
        LT402 = None
        char_literal403 = None
        expression401 = None


        char_literal399_tree = None
        LT400_tree = None
        LT402_tree = None
        char_literal403_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_80 = RewriteRuleTokenStream(self.adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self.adaptor, "token 81")
        stream_expression = RewriteRuleSubtreeStream(self.adaptor, "rule expression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:2: ( '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:4: '[' ( LT )* expression ( LT )* ']'
                char_literal399 = self.input.LT(1)
                self.match(self.input, 80, self.FOLLOW_80_in_indexSuffix2455)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_80.add(char_literal399)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:8: ( LT )*
                while True: #loop202
                    alt202 = 2
                    LA202_0 = self.input.LA(1)

                    if (LA202_0 == LT) :
                        LA202_2 = self.input.LA(2)

                        if (self.synpred239()) :
                            alt202 = 1




                    if alt202 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT400 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2457)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT400)


                    else:
                        break #loop202


                self.following.append(self.FOLLOW_expression_in_indexSuffix2460)
                expression401 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_expression.add(expression401.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:23: ( LT )*
                while True: #loop203
                    alt203 = 2
                    LA203_0 = self.input.LA(1)

                    if (LA203_0 == LT) :
                        alt203 = 1


                    if alt203 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT402 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2462)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT402)


                    else:
                        break #loop203


                char_literal403 = self.input.LT(1)
                self.match(self.input, 81, self.FOLLOW_81_in_indexSuffix2465)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_81.add(char_literal403)
                # AST Rewrite
                # elements: expression
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
                    # 386:3: -> ^( INDEXREF expression )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:6: ^( INDEXREF expression )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(INDEXREF, "INDEXREF"), root_1)

                    self.adaptor.addChild(root_1, stream_expression.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 63, indexSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end indexSuffix

    class propertyReferenceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyReferenceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:1: propertyReferenceSuffix : '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal404 = None
        LT405 = None
        e4xIdentifier406 = None


        char_literal404_tree = None
        LT405_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_99 = RewriteRuleTokenStream(self.adaptor, "token 99")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:2: ( '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:4: '.' ( LT )* e4xIdentifier
                char_literal404 = self.input.LT(1)
                self.match(self.input, 99, self.FOLLOW_99_in_propertyReferenceSuffix2488)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_99.add(char_literal404)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:8: ( LT )*
                while True: #loop204
                    alt204 = 2
                    LA204_0 = self.input.LA(1)

                    if (LA204_0 == LT) :
                        alt204 = 1


                    if alt204 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT405 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix2490)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT405)


                    else:
                        break #loop204


                self.following.append(self.FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2493)
                e4xIdentifier406 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier406.tree)
                # AST Rewrite
                # elements: e4xIdentifier
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
                    # 391:3: -> ^( PROPREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:391:6: ^( PROPREF e4xIdentifier )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROPREF, "PROPREF"), root_1)

                    self.adaptor.addChild(root_1, stream_e4xIdentifier.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 64, propertyReferenceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end propertyReferenceSuffix

    class descendentSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start descendentSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:1: descendentSuffix : '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) ;
    def descendentSuffix(self, ):

        retval = self.descendentSuffix_return()
        retval.start = self.input.LT(1)
        descendentSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal407 = None
        char_literal408 = None
        LT409 = None
        e4xIdentifier410 = None


        char_literal407_tree = None
        char_literal408_tree = None
        LT409_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_99 = RewriteRuleTokenStream(self.adaptor, "token 99")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:395:2: ( '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:395:4: '.' '.' ( LT )* e4xIdentifier
                char_literal407 = self.input.LT(1)
                self.match(self.input, 99, self.FOLLOW_99_in_descendentSuffix2514)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_99.add(char_literal407)
                char_literal408 = self.input.LT(1)
                self.match(self.input, 99, self.FOLLOW_99_in_descendentSuffix2516)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_99.add(char_literal408)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:395:12: ( LT )*
                while True: #loop205
                    alt205 = 2
                    LA205_0 = self.input.LA(1)

                    if (LA205_0 == LT) :
                        alt205 = 1


                    if alt205 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT409 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_descendentSuffix2518)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT409)


                    else:
                        break #loop205


                self.following.append(self.FOLLOW_e4xIdentifier_in_descendentSuffix2521)
                e4xIdentifier410 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier410.tree)
                # AST Rewrite
                # elements: e4xIdentifier
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
                    # 396:3: -> ^( DESCREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:396:6: ^( DESCREF e4xIdentifier )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(DESCREF, "DESCREF"), root_1)

                    self.adaptor.addChild(root_1, stream_e4xIdentifier.next())

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 65, descendentSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end descendentSuffix

    class namespaceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start namespaceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:399:1: namespaceSuffix : ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) ;
    def namespaceSuffix(self, ):

        retval = self.namespaceSuffix_return()
        retval.start = self.input.LT(1)
        namespaceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal411 = None
        char_literal412 = None
        LT413 = None
        e4xIdentifier414 = None


        char_literal411_tree = None
        char_literal412_tree = None
        LT413_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:2: ( ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:4: ':' ':' ( LT )* ( e4xIdentifier )?
                char_literal411 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_namespaceSuffix2542)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal411)
                char_literal412 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_namespaceSuffix2544)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal412)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:12: ( LT )*
                while True: #loop206
                    alt206 = 2
                    LA206_0 = self.input.LA(1)

                    if (LA206_0 == LT) :
                        LA206_2 = self.input.LA(2)

                        if (self.synpred243()) :
                            alt206 = 1




                    if alt206 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT413 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_namespaceSuffix2546)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT413)


                    else:
                        break #loop206


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:16: ( e4xIdentifier )?
                alt207 = 2
                LA207_0 = self.input.LA(1)

                if (LA207_0 == Identifier or (72 <= LA207_0 <= 74) or LA207_0 == 87 or (138 <= LA207_0 <= 139)) :
                    alt207 = 1
                elif (LA207_0 == 100) :
                    LA207_2 = self.input.LA(2)

                    if (self.synpred244()) :
                        alt207 = 1
                if alt207 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: e4xIdentifier
                    self.following.append(self.FOLLOW_e4xIdentifier_in_namespaceSuffix2549)
                    e4xIdentifier414 = self.e4xIdentifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_e4xIdentifier.add(e4xIdentifier414.tree)



                # AST Rewrite
                # elements: e4xIdentifier
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
                    # 401:3: -> ^( NSREF ( e4xIdentifier )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:401:6: ^( NSREF ( e4xIdentifier )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NSREF, "NSREF"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:401:14: ( e4xIdentifier )?
                    if stream_e4xIdentifier.hasNext():
                        self.adaptor.addChild(root_1, stream_e4xIdentifier.next())


                    stream_e4xIdentifier.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 66, namespaceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end namespaceSuffix

    class e4xIdentifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start e4xIdentifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:1: e4xIdentifier : ( identifier | '*' );
    def e4xIdentifier(self, ):

        retval = self.e4xIdentifier_return()
        retval.start = self.input.LT(1)
        e4xIdentifier_StartIndex = self.input.index()
        root_0 = None

        char_literal416 = None
        identifier415 = None


        char_literal416_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:405:2: ( identifier | '*' )
                alt208 = 2
                LA208_0 = self.input.LA(1)

                if (LA208_0 == Identifier or (72 <= LA208_0 <= 74) or LA208_0 == 87 or (138 <= LA208_0 <= 139)) :
                    alt208 = 1
                elif (LA208_0 == 100) :
                    alt208 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("404:1: e4xIdentifier : ( identifier | '*' );", 208, 0, self.input)

                    raise nvae

                if alt208 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:405:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_e4xIdentifier2572)
                    identifier415 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier415.tree)


                elif alt208 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal416 = self.input.LT(1)
                    self.match(self.input, 100, self.FOLLOW_100_in_e4xIdentifier2577)
                    if self.failed:
                        return retval

                    char_literal416_tree = self.adaptor.createWithPayload(char_literal416)
                    self.adaptor.addChild(root_0, char_literal416_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 67, e4xIdentifier_StartIndex)

            pass

        return retval

    # $ANTLR end e4xIdentifier

    class assignmentOperator_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentOperator
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:409:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set417 = None

        set417_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set417 = self.input.LT(1)
                if self.input.LA(1) == 65 or (101 <= self.input.LA(1) <= 111):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set417))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_assignmentOperator0
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
            if self.backtracking > 0:
                self.memoize(self.input, 68, assignmentOperator_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentOperator

    class conditionalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:413:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT419 = None
        char_literal420 = None
        LT421 = None
        LT423 = None
        char_literal424 = None
        LT425 = None
        logicalORExpression418 = None

        assignmentExpression422 = None

        assignmentExpression426 = None


        LT419_tree = None
        char_literal420_tree = None
        LT421_tree = None
        LT423_tree = None
        char_literal424_tree = None
        LT425_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression2644)
                logicalORExpression418 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression418.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt213 = 2
                LA213_0 = self.input.LA(1)

                if (LA213_0 == LT) :
                    LA213_1 = self.input.LA(2)

                    if (self.synpred261()) :
                        alt213 = 1
                elif (LA213_0 == 112) :
                    LA213_2 = self.input.LA(2)

                    if (self.synpred261()) :
                        alt213 = 1
                if alt213 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:27: ( LT )*
                    while True: #loop209
                        alt209 = 2
                        LA209_0 = self.input.LA(1)

                        if (LA209_0 == LT) :
                            alt209 = 1


                        if alt209 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT419 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2647)
                            if self.failed:
                                return retval


                        else:
                            break #loop209


                    char_literal420 = self.input.LT(1)
                    self.match(self.input, 112, self.FOLLOW_112_in_conditionalExpression2651)
                    if self.failed:
                        return retval

                    char_literal420_tree = self.adaptor.createWithPayload(char_literal420)
                    self.adaptor.addChild(root_0, char_literal420_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:36: ( LT )*
                    while True: #loop210
                        alt210 = 2
                        LA210_0 = self.input.LA(1)

                        if (LA210_0 == LT) :
                            LA210_2 = self.input.LA(2)

                            if (self.synpred258()) :
                                alt210 = 1




                        if alt210 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT421 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2653)
                            if self.failed:
                                return retval


                        else:
                            break #loop210


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2657)
                    assignmentExpression422 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression422.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:62: ( LT )*
                    while True: #loop211
                        alt211 = 2
                        LA211_0 = self.input.LA(1)

                        if (LA211_0 == LT) :
                            alt211 = 1


                        if alt211 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT423 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2659)
                            if self.failed:
                                return retval


                        else:
                            break #loop211


                    char_literal424 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpression2663)
                    if self.failed:
                        return retval

                    char_literal424_tree = self.adaptor.createWithPayload(char_literal424)
                    self.adaptor.addChild(root_0, char_literal424_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:71: ( LT )*
                    while True: #loop212
                        alt212 = 2
                        LA212_0 = self.input.LA(1)

                        if (LA212_0 == LT) :
                            LA212_2 = self.input.LA(2)

                            if (self.synpred260()) :
                                alt212 = 1




                        if alt212 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT425 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2665)
                            if self.failed:
                                return retval


                        else:
                            break #loop212


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2669)
                    assignmentExpression426 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression426.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 69, conditionalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpression

    class conditionalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:417:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
    def conditionalExpressionNoIn(self, ):

        retval = self.conditionalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        conditionalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT428 = None
        char_literal429 = None
        LT430 = None
        LT432 = None
        char_literal433 = None
        LT434 = None
        logicalORExpressionNoIn427 = None

        assignmentExpressionNoIn431 = None

        assignmentExpressionNoIn435 = None


        LT428_tree = None
        char_literal429_tree = None
        LT430_tree = None
        LT432_tree = None
        char_literal433_tree = None
        LT434_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2682)
                logicalORExpressionNoIn427 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn427.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt218 = 2
                alt218 = self.dfa218.predict(self.input)
                if alt218 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:31: ( LT )*
                    while True: #loop214
                        alt214 = 2
                        LA214_0 = self.input.LA(1)

                        if (LA214_0 == LT) :
                            alt214 = 1


                        if alt214 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT428 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2685)
                            if self.failed:
                                return retval


                        else:
                            break #loop214


                    char_literal429 = self.input.LT(1)
                    self.match(self.input, 112, self.FOLLOW_112_in_conditionalExpressionNoIn2689)
                    if self.failed:
                        return retval

                    char_literal429_tree = self.adaptor.createWithPayload(char_literal429)
                    self.adaptor.addChild(root_0, char_literal429_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:40: ( LT )*
                    while True: #loop215
                        alt215 = 2
                        LA215_0 = self.input.LA(1)

                        if (LA215_0 == LT) :
                            LA215_2 = self.input.LA(2)

                            if (self.synpred263()) :
                                alt215 = 1




                        if alt215 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT430 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2691)
                            if self.failed:
                                return retval


                        else:
                            break #loop215


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2695)
                    assignmentExpressionNoIn431 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn431.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:70: ( LT )*
                    while True: #loop216
                        alt216 = 2
                        LA216_0 = self.input.LA(1)

                        if (LA216_0 == LT) :
                            alt216 = 1


                        if alt216 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT432 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2697)
                            if self.failed:
                                return retval


                        else:
                            break #loop216


                    char_literal433 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpressionNoIn2701)
                    if self.failed:
                        return retval

                    char_literal433_tree = self.adaptor.createWithPayload(char_literal433)
                    self.adaptor.addChild(root_0, char_literal433_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:79: ( LT )*
                    while True: #loop217
                        alt217 = 2
                        LA217_0 = self.input.LA(1)

                        if (LA217_0 == LT) :
                            LA217_2 = self.input.LA(2)

                            if (self.synpred265()) :
                                alt217 = 1




                        if alt217 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT434 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2703)
                            if self.failed:
                                return retval


                        else:
                            break #loop217


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2707)
                    assignmentExpressionNoIn435 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn435.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 70, conditionalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpressionNoIn

    class logicalORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:421:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
    def logicalORExpression(self, ):

        retval = self.logicalORExpression_return()
        retval.start = self.input.LT(1)
        logicalORExpression_StartIndex = self.input.index()
        root_0 = None

        LT437 = None
        string_literal438 = None
        LT439 = None
        logicalANDExpression436 = None

        logicalANDExpression440 = None


        LT437_tree = None
        string_literal438_tree = None
        LT439_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2720)
                logicalANDExpression436 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression436.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop221
                    alt221 = 2
                    LA221_0 = self.input.LA(1)

                    if (LA221_0 == LT) :
                        LA221_1 = self.input.LA(2)

                        if (self.synpred269()) :
                            alt221 = 1


                    elif (LA221_0 == 113) :
                        LA221_3 = self.input.LA(2)

                        if (self.synpred269()) :
                            alt221 = 1




                    if alt221 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:28: ( LT )*
                        while True: #loop219
                            alt219 = 2
                            LA219_0 = self.input.LA(1)

                            if (LA219_0 == LT) :
                                alt219 = 1


                            if alt219 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT437 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2723)
                                if self.failed:
                                    return retval


                            else:
                                break #loop219


                        string_literal438 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_logicalORExpression2727)
                        if self.failed:
                            return retval

                        string_literal438_tree = self.adaptor.createWithPayload(string_literal438)
                        self.adaptor.addChild(root_0, string_literal438_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:38: ( LT )*
                        while True: #loop220
                            alt220 = 2
                            LA220_0 = self.input.LA(1)

                            if (LA220_0 == LT) :
                                LA220_2 = self.input.LA(2)

                                if (self.synpred268()) :
                                    alt220 = 1




                            if alt220 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT439 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2729)
                                if self.failed:
                                    return retval


                            else:
                                break #loop220


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2733)
                        logicalANDExpression440 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression440.tree)


                    else:
                        break #loop221





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 71, logicalORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpression

    class logicalORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:425:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
    def logicalORExpressionNoIn(self, ):

        retval = self.logicalORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT442 = None
        string_literal443 = None
        LT444 = None
        logicalANDExpressionNoIn441 = None

        logicalANDExpressionNoIn445 = None


        LT442_tree = None
        string_literal443_tree = None
        LT444_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2747)
                logicalANDExpressionNoIn441 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn441.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop224
                    alt224 = 2
                    alt224 = self.dfa224.predict(self.input)
                    if alt224 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:32: ( LT )*
                        while True: #loop222
                            alt222 = 2
                            LA222_0 = self.input.LA(1)

                            if (LA222_0 == LT) :
                                alt222 = 1


                            if alt222 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT442 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2750)
                                if self.failed:
                                    return retval


                            else:
                                break #loop222


                        string_literal443 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_logicalORExpressionNoIn2754)
                        if self.failed:
                            return retval

                        string_literal443_tree = self.adaptor.createWithPayload(string_literal443)
                        self.adaptor.addChild(root_0, string_literal443_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:42: ( LT )*
                        while True: #loop223
                            alt223 = 2
                            LA223_0 = self.input.LA(1)

                            if (LA223_0 == LT) :
                                LA223_2 = self.input.LA(2)

                                if (self.synpred271()) :
                                    alt223 = 1




                            if alt223 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT444 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2756)
                                if self.failed:
                                    return retval


                            else:
                                break #loop223


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2760)
                        logicalANDExpressionNoIn445 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn445.tree)


                    else:
                        break #loop224





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 72, logicalORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpressionNoIn

    class logicalANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:429:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
    def logicalANDExpression(self, ):

        retval = self.logicalANDExpression_return()
        retval.start = self.input.LT(1)
        logicalANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT447 = None
        string_literal448 = None
        LT449 = None
        bitwiseORExpression446 = None

        bitwiseORExpression450 = None


        LT447_tree = None
        string_literal448_tree = None
        LT449_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2774)
                bitwiseORExpression446 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression446.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop227
                    alt227 = 2
                    LA227_0 = self.input.LA(1)

                    if (LA227_0 == LT) :
                        LA227_1 = self.input.LA(2)

                        if (self.synpred275()) :
                            alt227 = 1


                    elif (LA227_0 == 114) :
                        LA227_3 = self.input.LA(2)

                        if (self.synpred275()) :
                            alt227 = 1




                    if alt227 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:27: ( LT )*
                        while True: #loop225
                            alt225 = 2
                            LA225_0 = self.input.LA(1)

                            if (LA225_0 == LT) :
                                alt225 = 1


                            if alt225 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT447 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2777)
                                if self.failed:
                                    return retval


                            else:
                                break #loop225


                        string_literal448 = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_logicalANDExpression2781)
                        if self.failed:
                            return retval

                        string_literal448_tree = self.adaptor.createWithPayload(string_literal448)
                        self.adaptor.addChild(root_0, string_literal448_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:37: ( LT )*
                        while True: #loop226
                            alt226 = 2
                            LA226_0 = self.input.LA(1)

                            if (LA226_0 == LT) :
                                LA226_2 = self.input.LA(2)

                                if (self.synpred274()) :
                                    alt226 = 1




                            if alt226 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT449 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2783)
                                if self.failed:
                                    return retval


                            else:
                                break #loop226


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2787)
                        bitwiseORExpression450 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression450.tree)


                    else:
                        break #loop227





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 73, logicalANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpression

    class logicalANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:433:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
    def logicalANDExpressionNoIn(self, ):

        retval = self.logicalANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT452 = None
        string_literal453 = None
        LT454 = None
        bitwiseORExpressionNoIn451 = None

        bitwiseORExpressionNoIn455 = None


        LT452_tree = None
        string_literal453_tree = None
        LT454_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2801)
                bitwiseORExpressionNoIn451 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn451.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop230
                    alt230 = 2
                    alt230 = self.dfa230.predict(self.input)
                    if alt230 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:31: ( LT )*
                        while True: #loop228
                            alt228 = 2
                            LA228_0 = self.input.LA(1)

                            if (LA228_0 == LT) :
                                alt228 = 1


                            if alt228 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT452 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2804)
                                if self.failed:
                                    return retval


                            else:
                                break #loop228


                        string_literal453 = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_logicalANDExpressionNoIn2808)
                        if self.failed:
                            return retval

                        string_literal453_tree = self.adaptor.createWithPayload(string_literal453)
                        self.adaptor.addChild(root_0, string_literal453_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:41: ( LT )*
                        while True: #loop229
                            alt229 = 2
                            LA229_0 = self.input.LA(1)

                            if (LA229_0 == LT) :
                                LA229_2 = self.input.LA(2)

                                if (self.synpred277()) :
                                    alt229 = 1




                            if alt229 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT454 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2810)
                                if self.failed:
                                    return retval


                            else:
                                break #loop229


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2814)
                        bitwiseORExpressionNoIn455 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn455.tree)


                    else:
                        break #loop230





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 74, logicalANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpressionNoIn

    class bitwiseORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:437:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
    def bitwiseORExpression(self, ):

        retval = self.bitwiseORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseORExpression_StartIndex = self.input.index()
        root_0 = None

        LT457 = None
        char_literal458 = None
        LT459 = None
        bitwiseXORExpression456 = None

        bitwiseXORExpression460 = None


        LT457_tree = None
        char_literal458_tree = None
        LT459_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2828)
                bitwiseXORExpression456 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression456.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop233
                    alt233 = 2
                    LA233_0 = self.input.LA(1)

                    if (LA233_0 == LT) :
                        LA233_1 = self.input.LA(2)

                        if (self.synpred281()) :
                            alt233 = 1


                    elif (LA233_0 == 115) :
                        LA233_3 = self.input.LA(2)

                        if (self.synpred281()) :
                            alt233 = 1




                    if alt233 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:28: ( LT )*
                        while True: #loop231
                            alt231 = 2
                            LA231_0 = self.input.LA(1)

                            if (LA231_0 == LT) :
                                alt231 = 1


                            if alt231 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT457 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2831)
                                if self.failed:
                                    return retval


                            else:
                                break #loop231


                        char_literal458 = self.input.LT(1)
                        self.match(self.input, 115, self.FOLLOW_115_in_bitwiseORExpression2835)
                        if self.failed:
                            return retval

                        char_literal458_tree = self.adaptor.createWithPayload(char_literal458)
                        self.adaptor.addChild(root_0, char_literal458_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:37: ( LT )*
                        while True: #loop232
                            alt232 = 2
                            LA232_0 = self.input.LA(1)

                            if (LA232_0 == LT) :
                                LA232_2 = self.input.LA(2)

                                if (self.synpred280()) :
                                    alt232 = 1




                            if alt232 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT459 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2837)
                                if self.failed:
                                    return retval


                            else:
                                break #loop232


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2841)
                        bitwiseXORExpression460 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression460.tree)


                    else:
                        break #loop233





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 75, bitwiseORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpression

    class bitwiseORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:441:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
    def bitwiseORExpressionNoIn(self, ):

        retval = self.bitwiseORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT462 = None
        char_literal463 = None
        LT464 = None
        bitwiseXORExpressionNoIn461 = None

        bitwiseXORExpressionNoIn465 = None


        LT462_tree = None
        char_literal463_tree = None
        LT464_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2855)
                bitwiseXORExpressionNoIn461 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn461.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop236
                    alt236 = 2
                    alt236 = self.dfa236.predict(self.input)
                    if alt236 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:32: ( LT )*
                        while True: #loop234
                            alt234 = 2
                            LA234_0 = self.input.LA(1)

                            if (LA234_0 == LT) :
                                alt234 = 1


                            if alt234 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT462 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2858)
                                if self.failed:
                                    return retval


                            else:
                                break #loop234


                        char_literal463 = self.input.LT(1)
                        self.match(self.input, 115, self.FOLLOW_115_in_bitwiseORExpressionNoIn2862)
                        if self.failed:
                            return retval

                        char_literal463_tree = self.adaptor.createWithPayload(char_literal463)
                        self.adaptor.addChild(root_0, char_literal463_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:41: ( LT )*
                        while True: #loop235
                            alt235 = 2
                            LA235_0 = self.input.LA(1)

                            if (LA235_0 == LT) :
                                LA235_2 = self.input.LA(2)

                                if (self.synpred283()) :
                                    alt235 = 1




                            if alt235 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT464 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2864)
                                if self.failed:
                                    return retval


                            else:
                                break #loop235


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2868)
                        bitwiseXORExpressionNoIn465 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn465.tree)


                    else:
                        break #loop236





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 76, bitwiseORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpressionNoIn

    class bitwiseXORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:445:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
    def bitwiseXORExpression(self, ):

        retval = self.bitwiseXORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpression_StartIndex = self.input.index()
        root_0 = None

        LT467 = None
        char_literal468 = None
        LT469 = None
        bitwiseANDExpression466 = None

        bitwiseANDExpression470 = None


        LT467_tree = None
        char_literal468_tree = None
        LT469_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2882)
                bitwiseANDExpression466 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression466.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop239
                    alt239 = 2
                    LA239_0 = self.input.LA(1)

                    if (LA239_0 == LT) :
                        LA239_1 = self.input.LA(2)

                        if (self.synpred287()) :
                            alt239 = 1


                    elif (LA239_0 == 116) :
                        LA239_3 = self.input.LA(2)

                        if (self.synpred287()) :
                            alt239 = 1




                    if alt239 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:28: ( LT )*
                        while True: #loop237
                            alt237 = 2
                            LA237_0 = self.input.LA(1)

                            if (LA237_0 == LT) :
                                alt237 = 1


                            if alt237 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT467 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2885)
                                if self.failed:
                                    return retval


                            else:
                                break #loop237


                        char_literal468 = self.input.LT(1)
                        self.match(self.input, 116, self.FOLLOW_116_in_bitwiseXORExpression2889)
                        if self.failed:
                            return retval

                        char_literal468_tree = self.adaptor.createWithPayload(char_literal468)
                        self.adaptor.addChild(root_0, char_literal468_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:37: ( LT )*
                        while True: #loop238
                            alt238 = 2
                            LA238_0 = self.input.LA(1)

                            if (LA238_0 == LT) :
                                LA238_2 = self.input.LA(2)

                                if (self.synpred286()) :
                                    alt238 = 1




                            if alt238 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT469 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2891)
                                if self.failed:
                                    return retval


                            else:
                                break #loop238


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2895)
                        bitwiseANDExpression470 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression470.tree)


                    else:
                        break #loop239





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 77, bitwiseXORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpression

    class bitwiseXORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:449:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
    def bitwiseXORExpressionNoIn(self, ):

        retval = self.bitwiseXORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT472 = None
        char_literal473 = None
        LT474 = None
        bitwiseANDExpressionNoIn471 = None

        bitwiseANDExpressionNoIn475 = None


        LT472_tree = None
        char_literal473_tree = None
        LT474_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2909)
                bitwiseANDExpressionNoIn471 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn471.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop242
                    alt242 = 2
                    alt242 = self.dfa242.predict(self.input)
                    if alt242 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:32: ( LT )*
                        while True: #loop240
                            alt240 = 2
                            LA240_0 = self.input.LA(1)

                            if (LA240_0 == LT) :
                                alt240 = 1


                            if alt240 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT472 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2912)
                                if self.failed:
                                    return retval


                            else:
                                break #loop240


                        char_literal473 = self.input.LT(1)
                        self.match(self.input, 116, self.FOLLOW_116_in_bitwiseXORExpressionNoIn2916)
                        if self.failed:
                            return retval

                        char_literal473_tree = self.adaptor.createWithPayload(char_literal473)
                        self.adaptor.addChild(root_0, char_literal473_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:41: ( LT )*
                        while True: #loop241
                            alt241 = 2
                            LA241_0 = self.input.LA(1)

                            if (LA241_0 == LT) :
                                LA241_2 = self.input.LA(2)

                                if (self.synpred289()) :
                                    alt241 = 1




                            if alt241 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT474 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2918)
                                if self.failed:
                                    return retval


                            else:
                                break #loop241


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2922)
                        bitwiseANDExpressionNoIn475 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn475.tree)


                    else:
                        break #loop242





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 78, bitwiseXORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpressionNoIn

    class bitwiseANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:453:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
    def bitwiseANDExpression(self, ):

        retval = self.bitwiseANDExpression_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT477 = None
        char_literal478 = None
        LT479 = None
        equalityExpression476 = None

        equalityExpression480 = None


        LT477_tree = None
        char_literal478_tree = None
        LT479_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2936)
                equalityExpression476 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression476.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop245
                    alt245 = 2
                    LA245_0 = self.input.LA(1)

                    if (LA245_0 == LT) :
                        LA245_1 = self.input.LA(2)

                        if (self.synpred293()) :
                            alt245 = 1


                    elif (LA245_0 == 117) :
                        LA245_3 = self.input.LA(2)

                        if (self.synpred293()) :
                            alt245 = 1




                    if alt245 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:26: ( LT )*
                        while True: #loop243
                            alt243 = 2
                            LA243_0 = self.input.LA(1)

                            if (LA243_0 == LT) :
                                alt243 = 1


                            if alt243 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT477 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2939)
                                if self.failed:
                                    return retval


                            else:
                                break #loop243


                        char_literal478 = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_bitwiseANDExpression2943)
                        if self.failed:
                            return retval

                        char_literal478_tree = self.adaptor.createWithPayload(char_literal478)
                        self.adaptor.addChild(root_0, char_literal478_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:35: ( LT )*
                        while True: #loop244
                            alt244 = 2
                            LA244_0 = self.input.LA(1)

                            if (LA244_0 == LT) :
                                LA244_2 = self.input.LA(2)

                                if (self.synpred292()) :
                                    alt244 = 1




                            if alt244 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT479 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2945)
                                if self.failed:
                                    return retval


                            else:
                                break #loop244


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2949)
                        equalityExpression480 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression480.tree)


                    else:
                        break #loop245





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 79, bitwiseANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpression

    class bitwiseANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:457:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
    def bitwiseANDExpressionNoIn(self, ):

        retval = self.bitwiseANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT482 = None
        char_literal483 = None
        LT484 = None
        equalityExpressionNoIn481 = None

        equalityExpressionNoIn485 = None


        LT482_tree = None
        char_literal483_tree = None
        LT484_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2963)
                equalityExpressionNoIn481 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn481.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop248
                    alt248 = 2
                    alt248 = self.dfa248.predict(self.input)
                    if alt248 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:30: ( LT )*
                        while True: #loop246
                            alt246 = 2
                            LA246_0 = self.input.LA(1)

                            if (LA246_0 == LT) :
                                alt246 = 1


                            if alt246 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT482 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2966)
                                if self.failed:
                                    return retval


                            else:
                                break #loop246


                        char_literal483 = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_bitwiseANDExpressionNoIn2970)
                        if self.failed:
                            return retval

                        char_literal483_tree = self.adaptor.createWithPayload(char_literal483)
                        self.adaptor.addChild(root_0, char_literal483_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:39: ( LT )*
                        while True: #loop247
                            alt247 = 2
                            LA247_0 = self.input.LA(1)

                            if (LA247_0 == LT) :
                                LA247_2 = self.input.LA(2)

                                if (self.synpred295()) :
                                    alt247 = 1




                            if alt247 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT484 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2972)
                                if self.failed:
                                    return retval


                            else:
                                break #loop247


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2976)
                        equalityExpressionNoIn485 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn485.tree)


                    else:
                        break #loop248





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 80, bitwiseANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpressionNoIn

    class equalityExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:461:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        LT487 = None
        set488 = None
        LT489 = None
        relationalExpression486 = None

        relationalExpression490 = None


        LT487_tree = None
        set488_tree = None
        LT489_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2990)
                relationalExpression486 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression486.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop251
                    alt251 = 2
                    LA251_0 = self.input.LA(1)

                    if (LA251_0 == LT) :
                        LA251_1 = self.input.LA(2)

                        if (self.synpred302()) :
                            alt251 = 1


                    elif ((118 <= LA251_0 <= 121)) :
                        LA251_3 = self.input.LA(2)

                        if (self.synpred302()) :
                            alt251 = 1




                    if alt251 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:28: ( LT )*
                        while True: #loop249
                            alt249 = 2
                            LA249_0 = self.input.LA(1)

                            if (LA249_0 == LT) :
                                alt249 = 1


                            if alt249 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT487 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2993)
                                if self.failed:
                                    return retval


                            else:
                                break #loop249


                        set488 = self.input.LT(1)
                        if (118 <= self.input.LA(1) <= 121):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set488))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2997
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:63: ( LT )*
                        while True: #loop250
                            alt250 = 2
                            LA250_0 = self.input.LA(1)

                            if (LA250_0 == LT) :
                                LA250_2 = self.input.LA(2)

                                if (self.synpred301()) :
                                    alt250 = 1




                            if alt250 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT489 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression3013)
                                if self.failed:
                                    return retval


                            else:
                                break #loop250


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression3017)
                        relationalExpression490 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression490.tree)


                    else:
                        break #loop251





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 81, equalityExpression_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpression

    class equalityExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:465:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
    def equalityExpressionNoIn(self, ):

        retval = self.equalityExpressionNoIn_return()
        retval.start = self.input.LT(1)
        equalityExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT492 = None
        set493 = None
        LT494 = None
        relationalExpressionNoIn491 = None

        relationalExpressionNoIn495 = None


        LT492_tree = None
        set493_tree = None
        LT494_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn3030)
                relationalExpressionNoIn491 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn491.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop254
                    alt254 = 2
                    alt254 = self.dfa254.predict(self.input)
                    if alt254 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:32: ( LT )*
                        while True: #loop252
                            alt252 = 2
                            LA252_0 = self.input.LA(1)

                            if (LA252_0 == LT) :
                                alt252 = 1


                            if alt252 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT492 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn3033)
                                if self.failed:
                                    return retval


                            else:
                                break #loop252


                        set493 = self.input.LT(1)
                        if (118 <= self.input.LA(1) <= 121):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set493))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn3037
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:67: ( LT )*
                        while True: #loop253
                            alt253 = 2
                            LA253_0 = self.input.LA(1)

                            if (LA253_0 == LT) :
                                LA253_2 = self.input.LA(2)

                                if (self.synpred307()) :
                                    alt253 = 1




                            if alt253 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT494 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn3053)
                                if self.failed:
                                    return retval


                            else:
                                break #loop253


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn3057)
                        relationalExpressionNoIn495 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn495.tree)


                    else:
                        break #loop254





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 82, equalityExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpressionNoIn

    class relationalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:469:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LT497 = None
        set498 = None
        LT499 = None
        shiftExpression496 = None

        shiftExpression500 = None


        LT497_tree = None
        set498_tree = None
        LT499_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression3071)
                shiftExpression496 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression496.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop257
                    alt257 = 2
                    LA257 = self.input.LA(1)
                    if LA257 == LT:
                        LA257_1 = self.input.LA(2)

                        if (self.synpred316()) :
                            alt257 = 1


                    elif LA257 == 88:
                        LA257_3 = self.input.LA(2)

                        if (self.synpred316()) :
                            alt257 = 1


                    elif LA257 == 60 or LA257 == 61 or LA257 == 122 or LA257 == 123 or LA257 == 124:
                        LA257_4 = self.input.LA(2)

                        if (self.synpred316()) :
                            alt257 = 1



                    if alt257 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:23: ( LT )*
                        while True: #loop255
                            alt255 = 2
                            LA255_0 = self.input.LA(1)

                            if (LA255_0 == LT) :
                                alt255 = 1


                            if alt255 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT497 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression3074)
                                if self.failed:
                                    return retval


                            else:
                                break #loop255


                        set498 = self.input.LT(1)
                        if (60 <= self.input.LA(1) <= 61) or self.input.LA(1) == 88 or (122 <= self.input.LA(1) <= 124):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set498))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpression3078
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:76: ( LT )*
                        while True: #loop256
                            alt256 = 2
                            LA256_0 = self.input.LA(1)

                            if (LA256_0 == LT) :
                                LA256_2 = self.input.LA(2)

                                if (self.synpred315()) :
                                    alt256 = 1




                            if alt256 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT499 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression3102)
                                if self.failed:
                                    return retval


                            else:
                                break #loop256


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression3106)
                        shiftExpression500 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression500.tree)


                    else:
                        break #loop257





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 83, relationalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpression

    class relationalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
    def relationalExpressionNoIn(self, ):

        retval = self.relationalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        relationalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT502 = None
        set503 = None
        LT504 = None
        shiftExpression501 = None

        shiftExpression505 = None


        LT502_tree = None
        set503_tree = None
        LT504_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn3119)
                shiftExpression501 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression501.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop260
                    alt260 = 2
                    alt260 = self.dfa260.predict(self.input)
                    if alt260 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:23: ( LT )*
                        while True: #loop258
                            alt258 = 2
                            LA258_0 = self.input.LA(1)

                            if (LA258_0 == LT) :
                                alt258 = 1


                            if alt258 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT502 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn3122)
                                if self.failed:
                                    return retval


                            else:
                                break #loop258


                        set503 = self.input.LT(1)
                        if (60 <= self.input.LA(1) <= 61) or (122 <= self.input.LA(1) <= 124):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set503))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn3126
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:69: ( LT )*
                        while True: #loop259
                            alt259 = 2
                            LA259_0 = self.input.LA(1)

                            if (LA259_0 == LT) :
                                LA259_2 = self.input.LA(2)

                                if (self.synpred322()) :
                                    alt259 = 1




                            if alt259 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT504 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn3146)
                                if self.failed:
                                    return retval


                            else:
                                break #loop259


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn3150)
                        shiftExpression505 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression505.tree)


                    else:
                        break #loop260





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 84, relationalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpressionNoIn

    class shiftExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start shiftExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:477:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        LT507 = None
        set508 = None
        LT509 = None
        additiveExpression506 = None

        additiveExpression510 = None


        LT507_tree = None
        set508_tree = None
        LT509_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 85):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression3163)
                additiveExpression506 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression506.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop263
                    alt263 = 2
                    LA263_0 = self.input.LA(1)

                    if (LA263_0 == LT) :
                        LA263_1 = self.input.LA(2)

                        if (self.synpred328()) :
                            alt263 = 1


                    elif ((125 <= LA263_0 <= 127)) :
                        LA263_3 = self.input.LA(2)

                        if (self.synpred328()) :
                            alt263 = 1




                    if alt263 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:26: ( LT )*
                        while True: #loop261
                            alt261 = 2
                            LA261_0 = self.input.LA(1)

                            if (LA261_0 == LT) :
                                alt261 = 1


                            if alt261 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT507 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression3166)
                                if self.failed:
                                    return retval


                            else:
                                break #loop261


                        set508 = self.input.LT(1)
                        if (125 <= self.input.LA(1) <= 127):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set508))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_shiftExpression3170
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:53: ( LT )*
                        while True: #loop262
                            alt262 = 2
                            LA262_0 = self.input.LA(1)

                            if (LA262_0 == LT) :
                                LA262_2 = self.input.LA(2)

                                if (self.synpred327()) :
                                    alt262 = 1




                            if alt262 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT509 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression3182)
                                if self.failed:
                                    return retval


                            else:
                                break #loop262


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression3186)
                        additiveExpression510 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression510.tree)


                    else:
                        break #loop263





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 85, shiftExpression_StartIndex)

            pass

        return retval

    # $ANTLR end shiftExpression

    class additiveExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start additiveExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:481:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        LT512 = None
        set513 = None
        LT514 = None
        multiplicativeExpression511 = None

        multiplicativeExpression515 = None


        LT512_tree = None
        set513_tree = None
        LT514_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 86):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression3199)
                multiplicativeExpression511 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression511.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop266
                    alt266 = 2
                    LA266_0 = self.input.LA(1)

                    if (LA266_0 == LT) :
                        LA266_1 = self.input.LA(2)

                        if (self.synpred332()) :
                            alt266 = 1


                    elif (LA266_0 == 64 or LA266_0 == 128) :
                        LA266_3 = self.input.LA(2)

                        if (self.synpred332()) :
                            alt266 = 1




                    if alt266 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:32: ( LT )*
                        while True: #loop264
                            alt264 = 2
                            LA264_0 = self.input.LA(1)

                            if (LA264_0 == LT) :
                                alt264 = 1


                            if alt264 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT512 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression3202)
                                if self.failed:
                                    return retval


                            else:
                                break #loop264


                        set513 = self.input.LT(1)
                        if self.input.LA(1) == 64 or self.input.LA(1) == 128:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set513))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_additiveExpression3206
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:49: ( LT )*
                        while True: #loop265
                            alt265 = 2
                            LA265_0 = self.input.LA(1)

                            if (LA265_0 == LT) :
                                LA265_2 = self.input.LA(2)

                                if (self.synpred331()) :
                                    alt265 = 1




                            if alt265 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT514 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression3214)
                                if self.failed:
                                    return retval


                            else:
                                break #loop265


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression3218)
                        multiplicativeExpression515 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression515.tree)


                    else:
                        break #loop266





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 86, additiveExpression_StartIndex)

            pass

        return retval

    # $ANTLR end additiveExpression

    class multiplicativeExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start multiplicativeExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:485:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        LT517 = None
        set518 = None
        LT519 = None
        unaryExpression516 = None

        unaryExpression520 = None


        LT517_tree = None
        set518_tree = None
        LT519_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 87):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression3231)
                unaryExpression516 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression516.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop269
                    alt269 = 2
                    LA269_0 = self.input.LA(1)

                    if (LA269_0 == LT) :
                        LA269_1 = self.input.LA(2)

                        if (self.synpred337()) :
                            alt269 = 1


                    elif (LA269_0 == 62 or LA269_0 == 100 or LA269_0 == 129) :
                        LA269_3 = self.input.LA(2)

                        if (self.synpred337()) :
                            alt269 = 1




                    if alt269 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:23: ( LT )*
                        while True: #loop267
                            alt267 = 2
                            LA267_0 = self.input.LA(1)

                            if (LA267_0 == LT) :
                                alt267 = 1


                            if alt267 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT517 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression3234)
                                if self.failed:
                                    return retval


                            else:
                                break #loop267


                        set518 = self.input.LT(1)
                        if self.input.LA(1) == 62 or self.input.LA(1) == 100 or self.input.LA(1) == 129:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set518))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression3238
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:46: ( LT )*
                        while True: #loop268
                            alt268 = 2
                            LA268_0 = self.input.LA(1)

                            if (LA268_0 == LT) :
                                LA268_2 = self.input.LA(2)

                                if (self.synpred336()) :
                                    alt268 = 1




                            if alt268 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT519 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression3250)
                                if self.failed:
                                    return retval


                            else:
                                break #loop268


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression3254)
                        unaryExpression520 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression520.tree)


                    else:
                        break #loop269





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 87, multiplicativeExpression_StartIndex)

            pass

        return retval

    # $ANTLR end multiplicativeExpression

    class unaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start unaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set522 = None
        postfixExpression521 = None

        unaryExpression523 = None


        set522_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 88):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt270 = 2
                LA270_0 = self.input.LA(1)

                if ((LT <= LA270_0 <= RegularExpressionHacks) or LA270_0 == 60 or LA270_0 == 62 or LA270_0 == 66 or (68 <= LA270_0 <= 69) or (72 <= LA270_0 <= 74) or LA270_0 == 80 or LA270_0 == 87 or LA270_0 == 98 or (137 <= LA270_0 <= 142)) :
                    alt270 = 1
                elif (LA270_0 == 64 or LA270_0 == 128 or (130 <= LA270_0 <= 136)) :
                    alt270 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("489:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 270, 0, self.input)

                    raise nvae

                if alt270 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression3267)
                    postfixExpression521 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression521.tree)


                elif alt270 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:491:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set522 = self.input.LT(1)
                    if self.input.LA(1) == 64 or self.input.LA(1) == 128 or (130 <= self.input.LA(1) <= 136):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set522))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_unaryExpression3272
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression3308)
                    unaryExpression523 = self.unaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unaryExpression523.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 88, unaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end unaryExpression

    class postfixExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start postfixExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:494:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set525 = None
        leftHandSideExpression524 = None


        set525_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 89):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression3320)
                leftHandSideExpression524 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression524.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:27: ( '++' | '--' )?
                alt271 = 2
                LA271_0 = self.input.LA(1)

                if ((133 <= LA271_0 <= 134)) :
                    alt271 = 1
                if alt271 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set525 = self.input.LT(1)
                    if (133 <= self.input.LA(1) <= 134):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set525))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_postfixExpression3322
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
            if self.backtracking > 0:
                self.memoize(self.input, 89, postfixExpression_StartIndex)

            pass

        return retval

    # $ANTLR end postfixExpression

    class primaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start primaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:498:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal526 = None
        char_literal532 = None
        LT533 = None
        LT535 = None
        char_literal536 = None
        xmlLiteral527 = None

        identifier528 = None

        literal529 = None

        arrayLiteral530 = None

        objectLiteral531 = None

        expression534 = None


        string_literal526_tree = None
        char_literal532_tree = None
        LT533_tree = None
        LT535_tree = None
        char_literal536_tree = None
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 90):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:499:2: ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt274 = 7
                LA274_0 = self.input.LA(1)

                if (LA274_0 == 137) :
                    alt274 = 1
                elif (LA274_0 == LT) and (self.synpred352()):
                    alt274 = 2
                elif (LA274_0 == 60) and (self.synpred352()):
                    alt274 = 2
                elif (LA274_0 == 66) :
                    LA274_4 = self.input.LA(2)

                    if (self.synpred352()) :
                        alt274 = 2
                    elif (self.synpred356()) :
                        alt274 = 6
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("498:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 274, 4, self.input)

                        raise nvae

                elif (LA274_0 == XMLComment) and (self.synpred352()):
                    alt274 = 2
                elif (LA274_0 == Identifier or (72 <= LA274_0 <= 74) or LA274_0 == 87 or (138 <= LA274_0 <= 139)) :
                    alt274 = 3
                elif (LA274_0 == StringLiteral or LA274_0 == NumericLiteral or LA274_0 == RegularExpressionHacks or LA274_0 == 62 or (140 <= LA274_0 <= 142)) :
                    alt274 = 4
                elif (LA274_0 == 80) :
                    alt274 = 5
                elif (LA274_0 == 69) :
                    alt274 = 7
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("498:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 274, 0, self.input)

                    raise nvae

                if alt274 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:499:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal526 = self.input.LT(1)
                    self.match(self.input, 137, self.FOLLOW_137_in_primaryExpression3340)
                    if self.failed:
                        return retval

                    string_literal526_tree = self.adaptor.createWithPayload(string_literal526)
                    self.adaptor.addChild(root_0, string_literal526_tree)



                elif alt274 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:4: ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlLiteral_in_primaryExpression3357)
                    xmlLiteral527 = self.xmlLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlLiteral527.tree)


                elif alt274 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:501:4: identifier
                    self.following.append(self.FOLLOW_identifier_in_primaryExpression3362)
                    identifier528 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier528.tree)
                    # AST Rewrite
                    # elements: identifier
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
                        # 502:3: -> ^( VARREF identifier )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:502:6: ^( VARREF identifier )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARREF, "VARREF"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt274 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:503:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression3377)
                    literal529 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal529.tree)


                elif alt274 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:504:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression3382)
                    arrayLiteral530 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral530.tree)


                elif alt274 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:505:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression3387)
                    objectLiteral531 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral531.tree)


                elif alt274 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal532 = self.input.LT(1)
                    self.match(self.input, 69, self.FOLLOW_69_in_primaryExpression3392)
                    if self.failed:
                        return retval

                    char_literal532_tree = self.adaptor.createWithPayload(char_literal532)
                    self.adaptor.addChild(root_0, char_literal532_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:10: ( LT )*
                    while True: #loop272
                        alt272 = 2
                        LA272_0 = self.input.LA(1)

                        if (LA272_0 == LT) :
                            LA272_2 = self.input.LA(2)

                            if (self.synpred357()) :
                                alt272 = 1




                        if alt272 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT533 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3394)
                            if self.failed:
                                return retval


                        else:
                            break #loop272


                    self.following.append(self.FOLLOW_expression_in_primaryExpression3398)
                    expression534 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression534.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:26: ( LT )*
                    while True: #loop273
                        alt273 = 2
                        LA273_0 = self.input.LA(1)

                        if (LA273_0 == LT) :
                            alt273 = 1


                        if alt273 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT535 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3400)
                            if self.failed:
                                return retval


                        else:
                            break #loop273


                    char_literal536 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_primaryExpression3404)
                    if self.failed:
                        return retval

                    char_literal536_tree = self.adaptor.createWithPayload(char_literal536)
                    self.adaptor.addChild(root_0, char_literal536_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 90, primaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end primaryExpression

    class arrayLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arrayLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:510:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' -> ^( ARRAY ( assignmentExpression )* ) ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal537 = None
        LT538 = None
        LT540 = None
        char_literal541 = None
        LT542 = None
        LT544 = None
        char_literal545 = None
        LT546 = None
        char_literal547 = None
        assignmentExpression539 = None

        assignmentExpression543 = None


        char_literal537_tree = None
        LT538_tree = None
        LT540_tree = None
        char_literal541_tree = None
        LT542_tree = None
        LT544_tree = None
        char_literal545_tree = None
        LT546_tree = None
        char_literal547_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_80 = RewriteRuleTokenStream(self.adaptor, "token 80")
        stream_81 = RewriteRuleTokenStream(self.adaptor, "token 81")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 91):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' -> ^( ARRAY ( assignmentExpression )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']'
                char_literal537 = self.input.LT(1)
                self.match(self.input, 80, self.FOLLOW_80_in_arrayLiteral3417)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_80.add(char_literal537)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:8: ( LT )*
                while True: #loop275
                    alt275 = 2
                    LA275_0 = self.input.LA(1)

                    if (LA275_0 == LT) :
                        LA275_2 = self.input.LA(2)

                        if (self.synpred359()) :
                            alt275 = 1




                    if alt275 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT538 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3419)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT538)


                    else:
                        break #loop275


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:12: ( assignmentExpression )?
                alt276 = 2
                alt276 = self.dfa276.predict(self.input)
                if alt276 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3422)
                    assignmentExpression539 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression539.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:34: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop280
                    alt280 = 2
                    alt280 = self.dfa280.predict(self.input)
                    if alt280 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:35: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:35: ( LT )*
                        while True: #loop277
                            alt277 = 2
                            LA277_0 = self.input.LA(1)

                            if (LA277_0 == LT) :
                                alt277 = 1


                            if alt277 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT540 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3426)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT540)


                            else:
                                break #loop277


                        char_literal541 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_arrayLiteral3429)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal541)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:43: ( ( LT )* assignmentExpression )?
                        alt279 = 2
                        alt279 = self.dfa279.predict(self.input)
                        if alt279 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: ( LT )*
                            while True: #loop278
                                alt278 = 2
                                LA278_0 = self.input.LA(1)

                                if (LA278_0 == LT) :
                                    LA278_2 = self.input.LA(2)

                                    if (self.synpred362()) :
                                        alt278 = 1




                                if alt278 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT542 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3432)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT542)


                                else:
                                    break #loop278


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3435)
                            assignmentExpression543 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression543.tree)





                    else:
                        break #loop280


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:73: ( LT )*
                while True: #loop281
                    alt281 = 2
                    LA281_0 = self.input.LA(1)

                    if (LA281_0 == LT) :
                        alt281 = 1


                    if alt281 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT544 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3441)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT544)


                    else:
                        break #loop281


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:77: ( ',' ( LT )* )?
                alt283 = 2
                LA283_0 = self.input.LA(1)

                if (LA283_0 == 70) :
                    alt283 = 1
                if alt283 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:78: ',' ( LT )*
                    char_literal545 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_arrayLiteral3445)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_70.add(char_literal545)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:82: ( LT )*
                    while True: #loop282
                        alt282 = 2
                        LA282_0 = self.input.LA(1)

                        if (LA282_0 == LT) :
                            alt282 = 1


                        if alt282 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT546 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3447)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT546)


                        else:
                            break #loop282





                char_literal547 = self.input.LT(1)
                self.match(self.input, 81, self.FOLLOW_81_in_arrayLiteral3452)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_81.add(char_literal547)
                # AST Rewrite
                # elements: assignmentExpression
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
                    # 512:3: -> ^( ARRAY ( assignmentExpression )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:512:6: ^( ARRAY ( assignmentExpression )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARRAY, "ARRAY"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:512:14: ( assignmentExpression )*
                    while stream_assignmentExpression.hasNext():
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())


                    stream_assignmentExpression.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 91, arrayLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end arrayLiteral

    class objectLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start objectLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:516:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal548 = None
        LT549 = None
        LT551 = None
        char_literal552 = None
        LT553 = None
        LT555 = None
        char_literal556 = None
        LT557 = None
        char_literal558 = None
        propertyNameAndValue550 = None

        propertyNameAndValue554 = None


        char_literal548_tree = None
        LT549_tree = None
        LT551_tree = None
        char_literal552_tree = None
        LT553_tree = None
        LT555_tree = None
        char_literal556_tree = None
        LT557_tree = None
        char_literal558_tree = None
        stream_67 = RewriteRuleTokenStream(self.adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self.adaptor, "token 66")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 92):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}'
                char_literal548 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_objectLiteral3482)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_66.add(char_literal548)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:8: ( LT )*
                while True: #loop284
                    alt284 = 2
                    LA284_0 = self.input.LA(1)

                    if (LA284_0 == LT) :
                        LA284_2 = self.input.LA(2)

                        if (self.synpred368()) :
                            alt284 = 1




                    if alt284 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT549 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3484)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT549)


                    else:
                        break #loop284


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:12: ( propertyNameAndValue )?
                alt285 = 2
                LA285_0 = self.input.LA(1)

                if (LA285_0 == StringLiteral or (NumericLiteral <= LA285_0 <= Identifier) or (72 <= LA285_0 <= 74) or LA285_0 == 87 or (138 <= LA285_0 <= 139)) :
                    alt285 = 1
                if alt285 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3487)
                    propertyNameAndValue550 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue550.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop288
                    alt288 = 2
                    alt288 = self.dfa288.predict(self.input)
                    if alt288 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:35: ( LT )*
                        while True: #loop286
                            alt286 = 2
                            LA286_0 = self.input.LA(1)

                            if (LA286_0 == LT) :
                                alt286 = 1


                            if alt286 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT551 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3491)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT551)


                            else:
                                break #loop286


                        char_literal552 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_objectLiteral3494)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal552)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:43: ( LT )*
                        while True: #loop287
                            alt287 = 2
                            LA287_0 = self.input.LA(1)

                            if (LA287_0 == LT) :
                                alt287 = 1


                            if alt287 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT553 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3496)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT553)


                            else:
                                break #loop287


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3499)
                        propertyNameAndValue554 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue554.tree)


                    else:
                        break #loop288


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:70: ( LT )*
                while True: #loop289
                    alt289 = 2
                    LA289_0 = self.input.LA(1)

                    if (LA289_0 == LT) :
                        alt289 = 1


                    if alt289 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT555 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3503)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT555)


                    else:
                        break #loop289


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:74: ( ',' ( LT )* )?
                alt291 = 2
                LA291_0 = self.input.LA(1)

                if (LA291_0 == 70) :
                    alt291 = 1
                if alt291 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:75: ',' ( LT )*
                    char_literal556 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_objectLiteral3507)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_70.add(char_literal556)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:79: ( LT )*
                    while True: #loop290
                        alt290 = 2
                        LA290_0 = self.input.LA(1)

                        if (LA290_0 == LT) :
                            alt290 = 1


                        if alt290 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT557 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3509)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT557)


                        else:
                            break #loop290





                char_literal558 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_objectLiteral3514)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_67.add(char_literal558)
                # AST Rewrite
                # elements: propertyNameAndValue
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
                    # 518:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:518:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:518:12: ( propertyNameAndValue )*
                    while stream_propertyNameAndValue.hasNext():
                        self.adaptor.addChild(root_1, stream_propertyNameAndValue.next())


                    stream_propertyNameAndValue.reset();

                    self.adaptor.addChild(root_0, root_1)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 92, objectLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end objectLiteral

    class propertyNameAndValue_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyNameAndValue
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:521:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        action = None
        LT560 = None
        char_literal561 = None
        LT562 = None
        LT564 = None
        LT565 = None
        LT567 = None
        LT569 = None
        LT570 = None
        LT572 = None
        propname = None

        funcname = None

        propertyName559 = None

        assignmentExpression563 = None

        formalParameterList566 = None

        statementBlock568 = None

        formalParameterList571 = None

        statementBlock573 = None


        action_tree = None
        LT560_tree = None
        char_literal561_tree = None
        LT562_tree = None
        LT564_tree = None
        LT565_tree = None
        LT567_tree = None
        LT569_tree = None
        LT570_tree = None
        LT572_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_138 = RewriteRuleTokenStream(self.adaptor, "token 138")
        stream_139 = RewriteRuleTokenStream(self.adaptor, "token 139")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_propertyName = RewriteRuleSubtreeStream(self.adaptor, "rule propertyName")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 93):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) )
                alt302 = 3
                alt302 = self.dfa302.predict(self.input)
                if alt302 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue3538)
                    propertyName559 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName559.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:17: ( LT )*
                    while True: #loop292
                        alt292 = 2
                        LA292_0 = self.input.LA(1)

                        if (LA292_0 == LT) :
                            alt292 = 1


                        if alt292 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT560 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3540)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT560)


                        else:
                            break #loop292


                    char_literal561 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_propertyNameAndValue3543)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_63.add(char_literal561)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:25: ( LT )*
                    while True: #loop293
                        alt293 = 2
                        LA293_0 = self.input.LA(1)

                        if (LA293_0 == LT) :
                            LA293_2 = self.input.LA(2)

                            if (self.synpred377()) :
                                alt293 = 1




                        if alt293 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT562 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3545)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT562)


                        else:
                            break #loop293


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue3548)
                    assignmentExpression563 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression563.tree)
                    # AST Rewrite
                    # elements: propertyName, assignmentExpression
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
                        # 523:3: -> ^( PROP propertyName PROP assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:523:6: ^( PROP propertyName PROP assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, self.adaptor.createFromType(PROP, "PROP"))
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt302 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:4: (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:4: (action= 'get' | action= 'set' )
                    alt294 = 2
                    LA294_0 = self.input.LA(1)

                    if (LA294_0 == 138) :
                        alt294 = 1
                    elif (LA294_0 == 139) :
                        alt294 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("524:4: (action= 'get' | action= 'set' )", 294, 0, self.input)

                        raise nvae

                    if alt294 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 138, self.FOLLOW_138_in_propertyNameAndValue3570)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_138.add(action)


                    elif alt294 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 139, self.FOLLOW_139_in_propertyNameAndValue3574)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_139.add(action)



                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3579)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:52: ( LT )*
                    while True: #loop295
                        alt295 = 2
                        LA295_0 = self.input.LA(1)

                        if (LA295_0 == LT) :
                            alt295 = 1


                        if alt295 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT564 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3581)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT564)


                        else:
                            break #loop295


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3586)
                    funcname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(funcname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:76: ( LT )*
                    while True: #loop296
                        alt296 = 2
                        LA296_0 = self.input.LA(1)

                        if (LA296_0 == LT) :
                            alt296 = 1


                        if alt296 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT565 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3588)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT565)


                        else:
                            break #loop296


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3591)
                    formalParameterList566 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList566.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:524:100: ( LT )*
                    while True: #loop297
                        alt297 = 2
                        LA297_0 = self.input.LA(1)

                        if (LA297_0 == LT) :
                            alt297 = 1


                        if alt297 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT567 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3593)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT567)


                        else:
                            break #loop297


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3596)
                    statementBlock568 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock568.tree)
                    # AST Rewrite
                    # elements: propname, funcname, statementBlock, formalParameterList, action
                    # token labels: action
                    # rule labels: propname, retval, funcname
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0
                        stream_action = RewriteRuleTokenStream(self.adaptor, "token action", action)

                        if propname is not None:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", propname.tree)
                        else:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", None)


                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        if funcname is not None:
                            stream_funcname = RewriteRuleSubtreeStream(self.adaptor, "token funcname", funcname.tree)
                        else:
                            stream_funcname = RewriteRuleSubtreeStream(self.adaptor, "token funcname", None)


                        root_0 = self.adaptor.nil()
                        # 525:3: -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:525:6: ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:525:31: ^( FUNC $funcname formalParameterList statementBlock )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_funcname.next())
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_statementBlock.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                elif alt302 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:4: (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:4: (action= 'get' | action= 'set' )
                    alt298 = 2
                    LA298_0 = self.input.LA(1)

                    if (LA298_0 == 138) :
                        alt298 = 1
                    elif (LA298_0 == 139) :
                        alt298 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("526:4: (action= 'get' | action= 'set' )", 298, 0, self.input)

                        raise nvae

                    if alt298 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 138, self.FOLLOW_138_in_propertyNameAndValue3629)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_138.add(action)


                    elif alt298 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 139, self.FOLLOW_139_in_propertyNameAndValue3633)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_139.add(action)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:32: ( LT )*
                    while True: #loop299
                        alt299 = 2
                        LA299_0 = self.input.LA(1)

                        if (LA299_0 == LT) :
                            alt299 = 1


                        if alt299 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT569 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3636)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT569)


                        else:
                            break #loop299


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3641)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:56: ( LT )*
                    while True: #loop300
                        alt300 = 2
                        LA300_0 = self.input.LA(1)

                        if (LA300_0 == LT) :
                            alt300 = 1


                        if alt300 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT570 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3643)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT570)


                        else:
                            break #loop300


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3646)
                    formalParameterList571 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList571.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:80: ( LT )*
                    while True: #loop301
                        alt301 = 2
                        LA301_0 = self.input.LA(1)

                        if (LA301_0 == LT) :
                            alt301 = 1


                        if alt301 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT572 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3648)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT572)


                        else:
                            break #loop301


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3651)
                    statementBlock573 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock573.tree)
                    # AST Rewrite
                    # elements: statementBlock, action, formalParameterList, propname
                    # token labels: action
                    # rule labels: propname, retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0
                        stream_action = RewriteRuleTokenStream(self.adaptor, "token action", action)

                        if propname is not None:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", propname.tree)
                        else:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", None)


                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 527:3: -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:527:6: ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:527:31: ^( FUNC ANONYMOUS formalParameterList statementBlock )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, self.adaptor.createFromType(ANONYMOUS, "ANONYMOUS"))
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_statementBlock.next())

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
            if self.backtracking > 0:
                self.memoize(self.input, 93, propertyNameAndValue_StartIndex)

            pass

        return retval

    # $ANTLR end propertyNameAndValue

    class propertyName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:530:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral575 = None
        NumericLiteral576 = None
        identifier574 = None


        StringLiteral575_tree = None
        NumericLiteral576_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 94):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:531:2: ( identifier | StringLiteral | NumericLiteral )
                alt303 = 3
                LA303 = self.input.LA(1)
                if LA303 == Identifier or LA303 == 72 or LA303 == 73 or LA303 == 74 or LA303 == 87 or LA303 == 138 or LA303 == 139:
                    alt303 = 1
                elif LA303 == StringLiteral:
                    alt303 = 2
                elif LA303 == NumericLiteral:
                    alt303 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("530:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 303, 0, self.input)

                    raise nvae

                if alt303 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:531:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName3686)
                    identifier574 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier574.tree)


                elif alt303 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:532:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral575 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName3691)
                    if self.failed:
                        return retval

                    StringLiteral575_tree = self.adaptor.createWithPayload(StringLiteral575)
                    self.adaptor.addChild(root_0, StringLiteral575_tree)



                elif alt303 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:533:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral576 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName3696)
                    if self.failed:
                        return retval

                    NumericLiteral576_tree = self.adaptor.createWithPayload(NumericLiteral576)
                    self.adaptor.addChild(root_0, NumericLiteral576_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 94, propertyName_StartIndex)

            pass

        return retval

    # $ANTLR end propertyName

    class literal_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start literal
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:537:1: literal : ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        string_literal577 = None
        string_literal578 = None
        string_literal579 = None
        StringLiteral580 = None
        NumericLiteral581 = None
        regularExpressionLiteral582 = None


        string_literal577_tree = None
        string_literal578_tree = None
        string_literal579_tree = None
        StringLiteral580_tree = None
        NumericLiteral581_tree = None
        stream_StringLiteral = RewriteRuleTokenStream(self.adaptor, "token StringLiteral")
        stream_NumericLiteral = RewriteRuleTokenStream(self.adaptor, "token NumericLiteral")
        stream_140 = RewriteRuleTokenStream(self.adaptor, "token 140")
        stream_142 = RewriteRuleTokenStream(self.adaptor, "token 142")
        stream_141 = RewriteRuleTokenStream(self.adaptor, "token 141")
        stream_regularExpressionLiteral = RewriteRuleSubtreeStream(self.adaptor, "rule regularExpressionLiteral")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 95):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:538:2: ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) )
                alt304 = 6
                LA304 = self.input.LA(1)
                if LA304 == 140:
                    alt304 = 1
                elif LA304 == 141:
                    alt304 = 2
                elif LA304 == 142:
                    alt304 = 3
                elif LA304 == StringLiteral:
                    alt304 = 4
                elif LA304 == NumericLiteral:
                    alt304 = 5
                elif LA304 == RegularExpressionHacks or LA304 == 62:
                    alt304 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("537:1: literal : ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) );", 304, 0, self.input)

                    raise nvae

                if alt304 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:538:4: 'null'
                    string_literal577 = self.input.LT(1)
                    self.match(self.input, 140, self.FOLLOW_140_in_literal3708)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_140.add(string_literal577)
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
                        # 538:11: -> NULL
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(NULL, "NULL"))





                elif alt304 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:539:4: 'true'
                    string_literal578 = self.input.LT(1)
                    self.match(self.input, 141, self.FOLLOW_141_in_literal3717)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_141.add(string_literal578)
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
                        # 539:11: -> TRUE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(TRUE, "TRUE"))





                elif alt304 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:540:4: 'false'
                    string_literal579 = self.input.LT(1)
                    self.match(self.input, 142, self.FOLLOW_142_in_literal3726)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_142.add(string_literal579)
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
                        # 540:12: -> FALSE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(FALSE, "FALSE"))





                elif alt304 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:541:4: StringLiteral
                    StringLiteral580 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_literal3735)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_StringLiteral.add(StringLiteral580)
                    # AST Rewrite
                    # elements: StringLiteral
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
                        # 541:18: -> ^( STRING StringLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:541:21: ^( STRING StringLiteral )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(STRING, "STRING"), root_1)

                        self.adaptor.addChild(root_1, stream_StringLiteral.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt304 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:542:4: NumericLiteral
                    NumericLiteral581 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_literal3748)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_NumericLiteral.add(NumericLiteral581)
                    # AST Rewrite
                    # elements: NumericLiteral
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
                        # 542:19: -> ^( NUMBER NumericLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:542:22: ^( NUMBER NumericLiteral )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NUMBER, "NUMBER"), root_1)

                        self.adaptor.addChild(root_1, stream_NumericLiteral.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt304 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:543:4: regularExpressionLiteral
                    self.following.append(self.FOLLOW_regularExpressionLiteral_in_literal3761)
                    regularExpressionLiteral582 = self.regularExpressionLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_regularExpressionLiteral.add(regularExpressionLiteral582.tree)
                    # AST Rewrite
                    # elements: regularExpressionLiteral
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
                        # 543:29: -> ^( REGEX regularExpressionLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:543:32: ^( REGEX regularExpressionLiteral )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(REGEX, "REGEX"), root_1)

                        self.adaptor.addChild(root_1, stream_regularExpressionLiteral.next())

                        self.adaptor.addChild(root_0, root_1)





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 95, literal_StartIndex)

            pass

        return retval

    # $ANTLR end literal

    class reFirstChar_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reFirstChar
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:553:1: reFirstChar : ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'let' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier );
    def reFirstChar(self, ):

        retval = self.reFirstChar_return()
        retval.start = self.input.LT(1)
        reFirstChar_StartIndex = self.input.index()
        root_0 = None

        set583 = None

        set583_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 96):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:554:2: ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'let' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set583 = self.input.LT(1)
                if self.input.LA(1) == StringLiteral or (NumericLiteral <= self.input.LA(1) <= Identifier) or (60 <= self.input.LA(1) <= 61) or (63 <= self.input.LA(1) <= 99) or (101 <= self.input.LA(1) <= 117) or (122 <= self.input.LA(1) <= 143):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set583))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_reFirstChar0
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
            if self.backtracking > 0:
                self.memoize(self.input, 96, reFirstChar_StartIndex)

            pass

        return retval

    # $ANTLR end reFirstChar

    class reChars_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reChars
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:572:1: reChars : ( reFirstChar | '*' );
    def reChars(self, ):

        retval = self.reChars_return()
        retval.start = self.input.LT(1)
        reChars_StartIndex = self.input.index()
        root_0 = None

        char_literal585 = None
        reFirstChar584 = None


        char_literal585_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 97):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:573:2: ( reFirstChar | '*' )
                alt305 = 2
                LA305_0 = self.input.LA(1)

                if (LA305_0 == StringLiteral or (NumericLiteral <= LA305_0 <= Identifier) or (60 <= LA305_0 <= 61) or (63 <= LA305_0 <= 99) or (101 <= LA305_0 <= 117) or (122 <= LA305_0 <= 143)) :
                    alt305 = 1
                elif (LA305_0 == 100) :
                    alt305 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("572:1: reChars : ( reFirstChar | '*' );", 305, 0, self.input)

                    raise nvae

                if alt305 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:573:4: reFirstChar
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_reFirstChar_in_reChars4162)
                    reFirstChar584 = self.reFirstChar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, reFirstChar584.tree)


                elif alt305 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:574:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal585 = self.input.LT(1)
                    self.match(self.input, 100, self.FOLLOW_100_in_reChars4167)
                    if self.failed:
                        return retval

                    char_literal585_tree = self.adaptor.createWithPayload(char_literal585)
                    self.adaptor.addChild(root_0, char_literal585_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 97, reChars_StartIndex)

            pass

        return retval

    # $ANTLR end reChars

    class regularExpressionLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start regularExpressionLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:580:1: regularExpressionLiteral : ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal586 = None
        char_literal589 = None
        Identifier590 = None
        RegularExpressionHacks591 = None
        Identifier592 = None
        reFirstChar587 = None

        reChars588 = None


        char_literal586_tree = None
        char_literal589_tree = None
        Identifier590_tree = None
        RegularExpressionHacks591_tree = None
        Identifier592_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 98):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:2: ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? )
                alt310 = 2
                LA310_0 = self.input.LA(1)

                if (LA310_0 == 62) :
                    alt310 = 1
                elif (LA310_0 == RegularExpressionHacks) :
                    alt310 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("580:1: regularExpressionLiteral : ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );", 310, 0, self.input)

                    raise nvae

                if alt310 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:4: '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )?
                    root_0 = self.adaptor.nil()

                    char_literal586 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_regularExpressionLiteral4181)
                    if self.failed:
                        return retval

                    char_literal586_tree = self.adaptor.createWithPayload(char_literal586)
                    self.adaptor.addChild(root_0, char_literal586_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:8: ( reFirstChar )?
                    alt306 = 2
                    LA306_0 = self.input.LA(1)

                    if (LA306_0 == StringLiteral or (NumericLiteral <= LA306_0 <= Identifier) or (60 <= LA306_0 <= 61) or (63 <= LA306_0 <= 99) or (101 <= LA306_0 <= 117) or (122 <= LA306_0 <= 143)) :
                        LA306_1 = self.input.LA(2)

                        if (self.synpred476()) :
                            alt306 = 1
                    if alt306 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reFirstChar
                        self.following.append(self.FOLLOW_reFirstChar_in_regularExpressionLiteral4183)
                        reFirstChar587 = self.reFirstChar()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, reFirstChar587.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:21: ( reChars )*
                    while True: #loop307
                        alt307 = 2
                        LA307_0 = self.input.LA(1)

                        if (LA307_0 == StringLiteral or (NumericLiteral <= LA307_0 <= Identifier) or (60 <= LA307_0 <= 61) or (63 <= LA307_0 <= 117) or (122 <= LA307_0 <= 143)) :
                            alt307 = 1


                        if alt307 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reChars
                            self.following.append(self.FOLLOW_reChars_in_regularExpressionLiteral4186)
                            reChars588 = self.reChars()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, reChars588.tree)


                        else:
                            break #loop307


                    char_literal589 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_regularExpressionLiteral4189)
                    if self.failed:
                        return retval

                    char_literal589_tree = self.adaptor.createWithPayload(char_literal589)
                    self.adaptor.addChild(root_0, char_literal589_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:34: ( Identifier )?
                    alt308 = 2
                    LA308_0 = self.input.LA(1)

                    if (LA308_0 == Identifier) :
                        alt308 = 1
                    if alt308 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier590 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral4191)
                        if self.failed:
                            return retval

                        Identifier590_tree = self.adaptor.createWithPayload(Identifier590)
                        self.adaptor.addChild(root_0, Identifier590_tree)






                elif alt310 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:582:4: RegularExpressionHacks ( Identifier )?
                    root_0 = self.adaptor.nil()

                    RegularExpressionHacks591 = self.input.LT(1)
                    self.match(self.input, RegularExpressionHacks, self.FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral4197)
                    if self.failed:
                        return retval

                    RegularExpressionHacks591_tree = self.adaptor.createWithPayload(RegularExpressionHacks591)
                    self.adaptor.addChild(root_0, RegularExpressionHacks591_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:582:27: ( Identifier )?
                    alt309 = 2
                    LA309_0 = self.input.LA(1)

                    if (LA309_0 == Identifier) :
                        alt309 = 1
                    if alt309 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier592 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral4199)
                        if self.failed:
                            return retval

                        Identifier592_tree = self.adaptor.createWithPayload(Identifier592)
                        self.adaptor.addChild(root_0, Identifier592_tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 98, regularExpressionLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end regularExpressionLiteral

    class identifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start identifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:587:1: identifier : ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set593 = None

        set593_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 99):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:588:2: ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set593 = self.input.LT(1)
                if self.input.LA(1) == Identifier or (72 <= self.input.LA(1) <= 74) or self.input.LA(1) == 87 or (138 <= self.input.LA(1) <= 139):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set593))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_identifier0
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
            if self.backtracking > 0:
                self.memoize(self.input, 99, identifier_StartIndex)

            pass

        return retval

    # $ANTLR end identifier

    # $ANTLR start synpred1
    def synpred1_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:4: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:4: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1147)
        if self.failed:
            return 


    # $ANTLR end synpred1



    # $ANTLR start synpred3
    def synpred3_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:19: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:19: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3173)
        if self.failed:
            return 


    # $ANTLR end synpred3



    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:53:4: ( functionDeclaration )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:53:5: functionDeclaration
        self.following.append(self.FOLLOW_functionDeclaration_in_synpred5192)
        self.functionDeclaration()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred16
    def synpred16_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:4: ( '{' )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:5: '{'
        self.match(self.input, 66, self.FOLLOW_66_in_synpred16399)
        if self.failed:
            return 


    # $ANTLR end synpred16



    # $ANTLR start synpred18
    def synpred18_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:4: ( xmlEmptyTag )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:4: xmlEmptyTag
        self.following.append(self.FOLLOW_xmlEmptyTag_in_synpred18449)
        self.xmlEmptyTag()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred18



    # $ANTLR start synpred19
    def synpred19_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:4: ( xmlStartTag )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:4: xmlStartTag
        self.following.append(self.FOLLOW_xmlStartTag_in_synpred19454)
        self.xmlStartTag()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred19



    # $ANTLR start synpred22
    def synpred22_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:5: ( ( LT )* xmlPayload )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:5: ( LT )* xmlPayload
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:5: ( LT )*
        while True: #loop314
            alt314 = 2
            LA314_0 = self.input.LA(1)

            if (LA314_0 == LT) :
                alt314 = 1


            if alt314 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred22477)
                if self.failed:
                    return 


            else:
                break #loop314


        self.following.append(self.FOLLOW_xmlPayload_in_synpred22480)
        self.xmlPayload()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred22



    # $ANTLR start synpred29
    def synpred29_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
        self.match(self.input, 68, self.FOLLOW_68_in_synpred29536)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:15: ( LT )*
        while True: #loop315
            alt315 = 2
            LA315_0 = self.input.LA(1)

            if (LA315_0 == LT) :
                alt315 = 1


            if alt315 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred29538)
                if self.failed:
                    return 


            else:
                break #loop315


        self.following.append(self.FOLLOW_identifier_in_synpred29541)
        self.identifier()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:30: ( LT )*
        while True: #loop316
            alt316 = 2
            LA316_0 = self.input.LA(1)

            if (LA316_0 == LT) :
                alt316 = 1


            if alt316 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred29543)
                if self.failed:
                    return 


            else:
                break #loop316


        self.following.append(self.FOLLOW_formalParameterList_in_synpred29546)
        self.formalParameterList()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:54: ( LT )*
        while True: #loop317
            alt317 = 2
            LA317_0 = self.input.LA(1)

            if (LA317_0 == LT) :
                alt317 = 1


            if alt317 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred29548)
                if self.failed:
                    return 


            else:
                break #loop317


        self.following.append(self.FOLLOW_statementBlock_in_synpred29551)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred29



    # $ANTLR start synpred32
    def synpred32_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:4: ( 'function' ( LT )* formalParameterList ( LT )* statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:4: 'function' ( LT )* formalParameterList ( LT )* statementBlock
        self.match(self.input, 68, self.FOLLOW_68_in_synpred32572)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:20: ( LT )*
        while True: #loop318
            alt318 = 2
            LA318_0 = self.input.LA(1)

            if (LA318_0 == LT) :
                alt318 = 1


            if alt318 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred32574)
                if self.failed:
                    return 


            else:
                break #loop318


        self.following.append(self.FOLLOW_formalParameterList_in_synpred32577)
        self.formalParameterList()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:44: ( LT )*
        while True: #loop319
            alt319 = 2
            LA319_0 = self.input.LA(1)

            if (LA319_0 == LT) :
                alt319 = 1


            if alt319 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred32579)
                if self.failed:
                    return 


            else:
                break #loop319


        self.following.append(self.FOLLOW_statementBlock_in_synpred32582)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred32



    # $ANTLR start synpred34
    def synpred34_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred34611)
        if self.failed:
            return 


    # $ANTLR end synpred34



    # $ANTLR start synpred41
    def synpred41_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred41690)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred41



    # $ANTLR start synpred42
    def synpred42_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: ( variableStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: variableStatement
        self.following.append(self.FOLLOW_variableStatement_in_synpred42695)
        self.variableStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred42



    # $ANTLR start synpred44
    def synpred44_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred44705)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred44



    # $ANTLR start synpred51
    def synpred51_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:4: ( letStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:4: letStatement
        self.following.append(self.FOLLOW_letStatement_in_synpred51740)
        self.letStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred51



    # $ANTLR start synpred52
    def synpred52_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred52745)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred52



    # $ANTLR start synpred59
    def synpred59_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred59821)
        if self.failed:
            return 


    # $ANTLR end synpred59



    # $ANTLR start synpred62
    def synpred62_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:4: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:4: '{' ( LT )* ( statementList )? ( LT )* '}'
        self.match(self.input, 66, self.FOLLOW_66_in_synpred62819)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:10: ( LT )*
        while True: #loop326
            alt326 = 2
            LA326_0 = self.input.LA(1)

            if (LA326_0 == LT) :
                LA326_2 = self.input.LA(2)

                if (self.synpred59()) :
                    alt326 = 1




            if alt326 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred62821)
                if self.failed:
                    return 


            else:
                break #loop326


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:13: ( statementList )?
        alt327 = 2
        alt327 = self.dfa327.predict(self.input)
        if alt327 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
            self.following.append(self.FOLLOW_statementList_in_synpred62825)
            self.statementList()
            self.following.pop()
            if self.failed:
                return 



        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:30: ( LT )*
        while True: #loop328
            alt328 = 2
            LA328_0 = self.input.LA(1)

            if (LA328_0 == LT) :
                alt328 = 1


            if alt328 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred62828)
                if self.failed:
                    return 


            else:
                break #loop328


        self.match(self.input, 67, self.FOLLOW_67_in_synpred62832)
        if self.failed:
            return 


    # $ANTLR end synpred62



    # $ANTLR start synpred64
    def synpred64_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:15: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:15: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred64860)
        if self.failed:
            return 


    # $ANTLR end synpred64



    # $ANTLR start synpred65
    def synpred65_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:15: ( ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:15: ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:17: ( LT )*
        while True: #loop329
            alt329 = 2
            LA329_0 = self.input.LA(1)

            if (LA329_0 == LT) :
                LA329_2 = self.input.LA(2)

                if (self.synpred64()) :
                    alt329 = 1




            if alt329 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred65860)
                if self.failed:
                    return 


            else:
                break #loop329


        self.following.append(self.FOLLOW_statement_in_synpred65864)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred65



    # $ANTLR start synpred79
    def synpred79_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred791008)
        if self.failed:
            return 


    # $ANTLR end synpred79



    # $ANTLR start synpred84
    def synpred84_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:25: ( ( LT )* ',' ( ( LT )* identifier )? )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:25: ( LT )* ',' ( ( LT )* identifier )?
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:25: ( LT )*
        while True: #loop338
            alt338 = 2
            LA338_0 = self.input.LA(1)

            if (LA338_0 == LT) :
                alt338 = 1


            if alt338 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred841015)
                if self.failed:
                    return 


            else:
                break #loop338


        self.match(self.input, 70, self.FOLLOW_70_in_synpred841018)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:33: ( ( LT )* identifier )?
        alt340 = 2
        LA340_0 = self.input.LA(1)

        if (LA340_0 == LT or LA340_0 == Identifier or (72 <= LA340_0 <= 74) or LA340_0 == 87 or (138 <= LA340_0 <= 139)) :
            alt340 = 1
        if alt340 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:34: ( LT )* identifier
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:34: ( LT )*
            while True: #loop339
                alt339 = 2
                LA339_0 = self.input.LA(1)

                if (LA339_0 == LT) :
                    alt339 = 1


                if alt339 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_synpred841021)
                    if self.failed:
                        return 


                else:
                    break #loop339


            self.following.append(self.FOLLOW_identifier_in_synpred841024)
            self.identifier()
            self.following.pop()
            if self.failed:
                return 





    # $ANTLR end synpred84



    # $ANTLR start synpred93
    def synpred93_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred931107)
        if self.failed:
            return 


    # $ANTLR end synpred93



    # $ANTLR start synpred98
    def synpred98_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:25: ( ( LT )* ',' ( ( LT )* identifier )? )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:25: ( LT )* ',' ( ( LT )* identifier )?
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:25: ( LT )*
        while True: #loop347
            alt347 = 2
            LA347_0 = self.input.LA(1)

            if (LA347_0 == LT) :
                alt347 = 1


            if alt347 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred981114)
                if self.failed:
                    return 


            else:
                break #loop347


        self.match(self.input, 70, self.FOLLOW_70_in_synpred981117)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:33: ( ( LT )* identifier )?
        alt349 = 2
        LA349_0 = self.input.LA(1)

        if (LA349_0 == LT or LA349_0 == Identifier or (72 <= LA349_0 <= 74) or LA349_0 == 87 or (138 <= LA349_0 <= 139)) :
            alt349 = 1
        if alt349 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:34: ( LT )* identifier
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:34: ( LT )*
            while True: #loop348
                alt348 = 2
                LA348_0 = self.input.LA(1)

                if (LA348_0 == LT) :
                    alt348 = 1


                if alt348 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_synpred981120)
                    if self.failed:
                        return 


                else:
                    break #loop348


            self.following.append(self.FOLLOW_identifier_in_synpred981123)
            self.identifier()
            self.following.pop()
            if self.failed:
                return 





    # $ANTLR end synpred98



    # $ANTLR start synpred104
    def synpred104_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1041180)
        if self.failed:
            return 


    # $ANTLR end synpred104



    # $ANTLR start synpred105
    def synpred105_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1051203)
        if self.failed:
            return 


    # $ANTLR end synpred105



    # $ANTLR start synpred108
    def synpred108_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:18: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:18: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1081265)
        if self.failed:
            return 


    # $ANTLR end synpred108



    # $ANTLR start synpred110
    def synpred110_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:43: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:43: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1101277)
        if self.failed:
            return 


    # $ANTLR end synpred110



    # $ANTLR start synpred112
    def synpred112_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:71: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:71: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1121290)
        if self.failed:
            return 


    # $ANTLR end synpred112



    # $ANTLR start synpred113
    def synpred113_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:61: ( LT )*
        while True: #loop352
            alt352 = 2
            LA352_0 = self.input.LA(1)

            if (LA352_0 == LT) :
                alt352 = 1


            if alt352 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1131284)
                if self.failed:
                    return 


            else:
                break #loop352


        self.match(self.input, 83, self.FOLLOW_83_in_synpred1131288)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:73: ( LT )*
        while True: #loop353
            alt353 = 2
            LA353_0 = self.input.LA(1)

            if (LA353_0 == LT) :
                LA353_2 = self.input.LA(2)

                if (self.synpred112()) :
                    alt353 = 1




            if alt353 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1131290)
                if self.failed:
                    return 


            else:
                break #loop353


        self.following.append(self.FOLLOW_statement_in_synpred1131294)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred113



    # $ANTLR start synpred116
    def synpred116_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:227:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:227:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred1161318)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred116



    # $ANTLR start synpred117
    def synpred117_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1171337)
        if self.failed:
            return 


    # $ANTLR end synpred117



    # $ANTLR start synpred122
    def synpred122_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1221386)
        if self.failed:
            return 


    # $ANTLR end synpred122



    # $ANTLR start synpred124
    def synpred124_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:46: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:46: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1241398)
        if self.failed:
            return 


    # $ANTLR end synpred124



    # $ANTLR start synpred126
    def synpred126_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1261423)
        if self.failed:
            return 


    # $ANTLR end synpred126



    # $ANTLR start synpred129
    def synpred129_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1291438)
        if self.failed:
            return 


    # $ANTLR end synpred129



    # $ANTLR start synpred132
    def synpred132_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:93: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:93: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1321453)
        if self.failed:
            return 


    # $ANTLR end synpred132



    # $ANTLR start synpred135
    def synpred135_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:120: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:120: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1351467)
        if self.failed:
            return 


    # $ANTLR end synpred135



    # $ANTLR start synpred139
    def synpred139_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1391512)
        if self.failed:
            return 


    # $ANTLR end synpred139



    # $ANTLR start synpred142
    def synpred142_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:32: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:32: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1421525)
        if self.failed:
            return 


    # $ANTLR end synpred142



    # $ANTLR start synpred144
    def synpred144_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1441537)
        if self.failed:
            return 


    # $ANTLR end synpred144



    # $ANTLR start synpred146
    def synpred146_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:102: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:102: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1461549)
        if self.failed:
            return 


    # $ANTLR end synpred146



    # $ANTLR start synpred154
    def synpred154_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:13: ( expression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:13: expression
        self.following.append(self.FOLLOW_expression_in_synpred1541639)
        self.expression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred154



    # $ANTLR start synpred157
    def synpred157_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1571669)
        if self.failed:
            return 


    # $ANTLR end synpred157



    # $ANTLR start synpred159
    def synpred159_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:45: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:45: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1591681)
        if self.failed:
            return 


    # $ANTLR end synpred159



    # $ANTLR start synpred161
    def synpred161_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:19: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:19: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1611704)
        if self.failed:
            return 


    # $ANTLR end synpred161



    # $ANTLR start synpred163
    def synpred163_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1631716)
        if self.failed:
            return 


    # $ANTLR end synpred163



    # $ANTLR start synpred165
    def synpred165_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:24: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:24: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1651739)
        if self.failed:
            return 


    # $ANTLR end synpred165



    # $ANTLR start synpred167
    def synpred167_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:22: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:22: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1671763)
        if self.failed:
            return 


    # $ANTLR end synpred167



    # $ANTLR start synpred177
    def synpred177_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:11: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:11: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1771837)
        if self.failed:
            return 


    # $ANTLR end synpred177



    # $ANTLR start synpred179
    def synpred179_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1791849)
        if self.failed:
            return 


    # $ANTLR end synpred179



    # $ANTLR start synpred180
    def synpred180_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:41: ( statementList )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:41: statementList
        self.following.append(self.FOLLOW_statementList_in_synpred1801853)
        self.statementList()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred180



    # $ANTLR start synpred182
    def synpred182_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1821874)
        if self.failed:
            return 


    # $ANTLR end synpred182



    # $ANTLR start synpred196
    def synpred196_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1962021)
        if self.failed:
            return 


    # $ANTLR end synpred196



    # $ANTLR start synpred197
    def synpred197_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:26: ( ( LT )* ',' ( LT )* assignmentExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:26: ( LT )* ',' ( LT )* assignmentExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:28: ( LT )*
        while True: #loop363
            alt363 = 2
            LA363_0 = self.input.LA(1)

            if (LA363_0 == LT) :
                alt363 = 1


            if alt363 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1972015)
                if self.failed:
                    return 


            else:
                break #loop363


        self.match(self.input, 70, self.FOLLOW_70_in_synpred1972019)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:37: ( LT )*
        while True: #loop364
            alt364 = 2
            LA364_0 = self.input.LA(1)

            if (LA364_0 == LT) :
                LA364_2 = self.input.LA(2)

                if (self.synpred196()) :
                    alt364 = 1




            if alt364 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1972021)
                if self.failed:
                    return 


            else:
                break #loop364


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred1972025)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred197



    # $ANTLR start synpred199
    def synpred199_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1992048)
        if self.failed:
            return 


    # $ANTLR end synpred199



    # $ANTLR start synpred202
    def synpred202_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:50: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:50: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2022073)
        if self.failed:
            return 


    # $ANTLR end synpred202



    # $ANTLR start synpred203
    def synpred203_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred2032066)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:27: ( LT )*
        while True: #loop367
            alt367 = 2
            LA367_0 = self.input.LA(1)

            if (LA367_0 == LT) :
                alt367 = 1


            if alt367 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2032068)
                if self.failed:
                    return 


            else:
                break #loop367


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred2032071)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:50: ( LT )*
        while True: #loop368
            alt368 = 2
            LA368_0 = self.input.LA(1)

            if (LA368_0 == LT) :
                LA368_2 = self.input.LA(2)

                if (self.synpred202()) :
                    alt368 = 1




            if alt368 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2032073)
                if self.failed:
                    return 


            else:
                break #loop368


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred2032076)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred203



    # $ANTLR start synpred205
    def synpred205_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:50: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:50: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2052114)
        if self.failed:
            return 


    # $ANTLR end synpred205



    # $ANTLR start synpred206
    def synpred206_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred2062107)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:27: ( LT )*
        while True: #loop369
            alt369 = 2
            LA369_0 = self.input.LA(1)

            if (LA369_0 == LT) :
                alt369 = 1


            if alt369 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2062109)
                if self.failed:
                    return 


            else:
                break #loop369


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred2062112)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:50: ( LT )*
        while True: #loop370
            alt370 = 2
            LA370_0 = self.input.LA(1)

            if (LA370_0 == LT) :
                LA370_2 = self.input.LA(2)

                if (self.synpred205()) :
                    alt370 = 1




            if alt370 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2062114)
                if self.failed:
                    return 


            else:
                break #loop370


        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_synpred2062117)
        self.assignmentExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred206



    # $ANTLR start synpred207
    def synpred207_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred2072148)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred207



    # $ANTLR start synpred208
    def synpred208_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:340:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:340:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred2082165)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred208



    # $ANTLR start synpred209
    def synpred209_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2092172)
        if self.failed:
            return 


    # $ANTLR end synpred209



    # $ANTLR start synpred211
    def synpred211_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( LT )*
        while True: #loop371
            alt371 = 2
            LA371_0 = self.input.LA(1)

            if (LA371_0 == LT) :
                alt371 = 1


            if alt371 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2112200)
                if self.failed:
                    return 


            else:
                break #loop371


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred2112203)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred211



    # $ANTLR start synpred214
    def synpred214_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:24: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:24: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:26: ( LT )*
        while True: #loop374
            alt374 = 2
            LA374_0 = self.input.LA(1)

            if (LA374_0 == LT) :
                alt374 = 1


            if alt374 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2142226)
                if self.failed:
                    return 


            else:
                break #loop374


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred2142230)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred214



    # $ANTLR start synpred216
    def synpred216_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2162239)
        if self.failed:
            return 


    # $ANTLR end synpred216



    # $ANTLR start synpred219
    def synpred219_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:46: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:46: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:46: ( LT )*
        while True: #loop377
            alt377 = 2
            LA377_0 = self.input.LA(1)

            if (LA377_0 == LT) :
                alt377 = 1


            if alt377 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2192250)
                if self.failed:
                    return 


            else:
                break #loop377


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred2192253)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred219



    # $ANTLR start synpred223
    def synpred223_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2232323)
        if self.failed:
            return 


    # $ANTLR end synpred223



    # $ANTLR start synpred227
    def synpred227_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:45: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:45: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:45: ( LT )*
        while True: #loop378
            alt378 = 2
            LA378_0 = self.input.LA(1)

            if (LA378_0 == LT) :
                alt378 = 1


            if alt378 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2272335)
                if self.failed:
                    return 


            else:
                break #loop378


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred2272338)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred227



    # $ANTLR start synpred232
    def synpred232_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2322406)
        if self.failed:
            return 


    # $ANTLR end synpred232



    # $ANTLR start synpred233
    def synpred233_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:34: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:34: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2332411)
        if self.failed:
            return 


    # $ANTLR end synpred233



    # $ANTLR start synpred234
    def synpred234_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:43: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:43: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2342417)
        if self.failed:
            return 


    # $ANTLR end synpred234



    # $ANTLR start synpred235
    def synpred235_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:68: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:68: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2352422)
        if self.failed:
            return 


    # $ANTLR end synpred235



    # $ANTLR start synpred239
    def synpred239_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2392457)
        if self.failed:
            return 


    # $ANTLR end synpred239



    # $ANTLR start synpred243
    def synpred243_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:12: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:12: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2432546)
        if self.failed:
            return 


    # $ANTLR end synpred243



    # $ANTLR start synpred244
    def synpred244_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:16: ( e4xIdentifier )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:400:16: e4xIdentifier
        self.following.append(self.FOLLOW_e4xIdentifier_in_synpred2442549)
        self.e4xIdentifier()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred244



    # $ANTLR start synpred258
    def synpred258_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:34: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:34: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2582653)
        if self.failed:
            return 


    # $ANTLR end synpred258



    # $ANTLR start synpred260
    def synpred260_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:69: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:69: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2602665)
        if self.failed:
            return 


    # $ANTLR end synpred260



    # $ANTLR start synpred261
    def synpred261_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:25: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:27: ( LT )*
        while True: #loop386
            alt386 = 2
            LA386_0 = self.input.LA(1)

            if (LA386_0 == LT) :
                alt386 = 1


            if alt386 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2612647)
                if self.failed:
                    return 


            else:
                break #loop386


        self.match(self.input, 112, self.FOLLOW_112_in_synpred2612651)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:36: ( LT )*
        while True: #loop387
            alt387 = 2
            LA387_0 = self.input.LA(1)

            if (LA387_0 == LT) :
                LA387_2 = self.input.LA(2)

                if (self.synpred258()) :
                    alt387 = 1




            if alt387 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2612653)
                if self.failed:
                    return 


            else:
                break #loop387


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred2612657)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:62: ( LT )*
        while True: #loop388
            alt388 = 2
            LA388_0 = self.input.LA(1)

            if (LA388_0 == LT) :
                alt388 = 1


            if alt388 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2612659)
                if self.failed:
                    return 


            else:
                break #loop388


        self.match(self.input, 63, self.FOLLOW_63_in_synpred2612663)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:71: ( LT )*
        while True: #loop389
            alt389 = 2
            LA389_0 = self.input.LA(1)

            if (LA389_0 == LT) :
                LA389_2 = self.input.LA(2)

                if (self.synpred260()) :
                    alt389 = 1




            if alt389 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2612665)
                if self.failed:
                    return 


            else:
                break #loop389


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred2612669)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred261



    # $ANTLR start synpred263
    def synpred263_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:38: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:38: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2632691)
        if self.failed:
            return 


    # $ANTLR end synpred263



    # $ANTLR start synpred265
    def synpred265_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2652703)
        if self.failed:
            return 


    # $ANTLR end synpred265



    # $ANTLR start synpred268
    def synpred268_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2682729)
        if self.failed:
            return 


    # $ANTLR end synpred268



    # $ANTLR start synpred269
    def synpred269_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:26: ( ( LT )* '||' ( LT )* logicalANDExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:26: ( LT )* '||' ( LT )* logicalANDExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:28: ( LT )*
        while True: #loop394
            alt394 = 2
            LA394_0 = self.input.LA(1)

            if (LA394_0 == LT) :
                alt394 = 1


            if alt394 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2692723)
                if self.failed:
                    return 


            else:
                break #loop394


        self.match(self.input, 113, self.FOLLOW_113_in_synpred2692727)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:38: ( LT )*
        while True: #loop395
            alt395 = 2
            LA395_0 = self.input.LA(1)

            if (LA395_0 == LT) :
                LA395_2 = self.input.LA(2)

                if (self.synpred268()) :
                    alt395 = 1




            if alt395 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2692729)
                if self.failed:
                    return 


            else:
                break #loop395


        self.following.append(self.FOLLOW_logicalANDExpression_in_synpred2692733)
        self.logicalANDExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred269



    # $ANTLR start synpred271
    def synpred271_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:40: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:40: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2712756)
        if self.failed:
            return 


    # $ANTLR end synpred271



    # $ANTLR start synpred274
    def synpred274_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2742783)
        if self.failed:
            return 


    # $ANTLR end synpred274



    # $ANTLR start synpred275
    def synpred275_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:25: ( ( LT )* '&&' ( LT )* bitwiseORExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:25: ( LT )* '&&' ( LT )* bitwiseORExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:27: ( LT )*
        while True: #loop398
            alt398 = 2
            LA398_0 = self.input.LA(1)

            if (LA398_0 == LT) :
                alt398 = 1


            if alt398 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2752777)
                if self.failed:
                    return 


            else:
                break #loop398


        self.match(self.input, 114, self.FOLLOW_114_in_synpred2752781)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:37: ( LT )*
        while True: #loop399
            alt399 = 2
            LA399_0 = self.input.LA(1)

            if (LA399_0 == LT) :
                LA399_2 = self.input.LA(2)

                if (self.synpred274()) :
                    alt399 = 1




            if alt399 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2752783)
                if self.failed:
                    return 


            else:
                break #loop399


        self.following.append(self.FOLLOW_bitwiseORExpression_in_synpred2752787)
        self.bitwiseORExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred275



    # $ANTLR start synpred277
    def synpred277_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2772810)
        if self.failed:
            return 


    # $ANTLR end synpred277



    # $ANTLR start synpred280
    def synpred280_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2802837)
        if self.failed:
            return 


    # $ANTLR end synpred280



    # $ANTLR start synpred281
    def synpred281_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:26: ( ( LT )* '|' ( LT )* bitwiseXORExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:26: ( LT )* '|' ( LT )* bitwiseXORExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:28: ( LT )*
        while True: #loop402
            alt402 = 2
            LA402_0 = self.input.LA(1)

            if (LA402_0 == LT) :
                alt402 = 1


            if alt402 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2812831)
                if self.failed:
                    return 


            else:
                break #loop402


        self.match(self.input, 115, self.FOLLOW_115_in_synpred2812835)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:37: ( LT )*
        while True: #loop403
            alt403 = 2
            LA403_0 = self.input.LA(1)

            if (LA403_0 == LT) :
                LA403_2 = self.input.LA(2)

                if (self.synpred280()) :
                    alt403 = 1




            if alt403 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2812837)
                if self.failed:
                    return 


            else:
                break #loop403


        self.following.append(self.FOLLOW_bitwiseXORExpression_in_synpred2812841)
        self.bitwiseXORExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred281



    # $ANTLR start synpred283
    def synpred283_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2832864)
        if self.failed:
            return 


    # $ANTLR end synpred283



    # $ANTLR start synpred286
    def synpred286_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2862891)
        if self.failed:
            return 


    # $ANTLR end synpred286



    # $ANTLR start synpred287
    def synpred287_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:26: ( ( LT )* '^' ( LT )* bitwiseANDExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:26: ( LT )* '^' ( LT )* bitwiseANDExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:28: ( LT )*
        while True: #loop406
            alt406 = 2
            LA406_0 = self.input.LA(1)

            if (LA406_0 == LT) :
                alt406 = 1


            if alt406 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2872885)
                if self.failed:
                    return 


            else:
                break #loop406


        self.match(self.input, 116, self.FOLLOW_116_in_synpred2872889)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:37: ( LT )*
        while True: #loop407
            alt407 = 2
            LA407_0 = self.input.LA(1)

            if (LA407_0 == LT) :
                LA407_2 = self.input.LA(2)

                if (self.synpred286()) :
                    alt407 = 1




            if alt407 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2872891)
                if self.failed:
                    return 


            else:
                break #loop407


        self.following.append(self.FOLLOW_bitwiseANDExpression_in_synpred2872895)
        self.bitwiseANDExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred287



    # $ANTLR start synpred289
    def synpred289_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2892918)
        if self.failed:
            return 


    # $ANTLR end synpred289



    # $ANTLR start synpred292
    def synpred292_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:33: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:33: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2922945)
        if self.failed:
            return 


    # $ANTLR end synpred292



    # $ANTLR start synpred293
    def synpred293_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:24: ( ( LT )* '&' ( LT )* equalityExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:24: ( LT )* '&' ( LT )* equalityExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:26: ( LT )*
        while True: #loop410
            alt410 = 2
            LA410_0 = self.input.LA(1)

            if (LA410_0 == LT) :
                alt410 = 1


            if alt410 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2932939)
                if self.failed:
                    return 


            else:
                break #loop410


        self.match(self.input, 117, self.FOLLOW_117_in_synpred2932943)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:35: ( LT )*
        while True: #loop411
            alt411 = 2
            LA411_0 = self.input.LA(1)

            if (LA411_0 == LT) :
                LA411_2 = self.input.LA(2)

                if (self.synpred292()) :
                    alt411 = 1




            if alt411 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2932945)
                if self.failed:
                    return 


            else:
                break #loop411


        self.following.append(self.FOLLOW_equalityExpression_in_synpred2932949)
        self.equalityExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred293



    # $ANTLR start synpred295
    def synpred295_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:37: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:37: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2952972)
        if self.failed:
            return 


    # $ANTLR end synpred295



    # $ANTLR start synpred301
    def synpred301_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:61: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:61: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3013013)
        if self.failed:
            return 


    # $ANTLR end synpred301



    # $ANTLR start synpred302
    def synpred302_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:26: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:28: ( LT )*
        while True: #loop414
            alt414 = 2
            LA414_0 = self.input.LA(1)

            if (LA414_0 == LT) :
                alt414 = 1


            if alt414 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3022993)
                if self.failed:
                    return 


            else:
                break #loop414


        if (118 <= self.input.LA(1) <= 121):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3022997
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:63: ( LT )*
        while True: #loop415
            alt415 = 2
            LA415_0 = self.input.LA(1)

            if (LA415_0 == LT) :
                LA415_2 = self.input.LA(2)

                if (self.synpred301()) :
                    alt415 = 1




            if alt415 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3023013)
                if self.failed:
                    return 


            else:
                break #loop415


        self.following.append(self.FOLLOW_relationalExpression_in_synpred3023017)
        self.relationalExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred302



    # $ANTLR start synpred307
    def synpred307_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3073053)
        if self.failed:
            return 


    # $ANTLR end synpred307



    # $ANTLR start synpred315
    def synpred315_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:74: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:74: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3153102)
        if self.failed:
            return 


    # $ANTLR end synpred315



    # $ANTLR start synpred316
    def synpred316_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:21: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:23: ( LT )*
        while True: #loop418
            alt418 = 2
            LA418_0 = self.input.LA(1)

            if (LA418_0 == LT) :
                alt418 = 1


            if alt418 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3163074)
                if self.failed:
                    return 


            else:
                break #loop418


        if (60 <= self.input.LA(1) <= 61) or self.input.LA(1) == 88 or (122 <= self.input.LA(1) <= 124):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3163078
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:76: ( LT )*
        while True: #loop419
            alt419 = 2
            LA419_0 = self.input.LA(1)

            if (LA419_0 == LT) :
                LA419_2 = self.input.LA(2)

                if (self.synpred315()) :
                    alt419 = 1




            if alt419 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3163102)
                if self.failed:
                    return 


            else:
                break #loop419


        self.following.append(self.FOLLOW_shiftExpression_in_synpred3163106)
        self.shiftExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred316



    # $ANTLR start synpred322
    def synpred322_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:67: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:67: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3223146)
        if self.failed:
            return 


    # $ANTLR end synpred322



    # $ANTLR start synpred327
    def synpred327_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:51: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:51: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3273182)
        if self.failed:
            return 


    # $ANTLR end synpred327



    # $ANTLR start synpred328
    def synpred328_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:24: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:26: ( LT )*
        while True: #loop422
            alt422 = 2
            LA422_0 = self.input.LA(1)

            if (LA422_0 == LT) :
                alt422 = 1


            if alt422 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3283166)
                if self.failed:
                    return 


            else:
                break #loop422


        if (125 <= self.input.LA(1) <= 127):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3283170
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:53: ( LT )*
        while True: #loop423
            alt423 = 2
            LA423_0 = self.input.LA(1)

            if (LA423_0 == LT) :
                LA423_2 = self.input.LA(2)

                if (self.synpred327()) :
                    alt423 = 1




            if alt423 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3283182)
                if self.failed:
                    return 


            else:
                break #loop423


        self.following.append(self.FOLLOW_additiveExpression_in_synpred3283186)
        self.additiveExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred328



    # $ANTLR start synpred331
    def synpred331_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:47: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:47: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3313214)
        if self.failed:
            return 


    # $ANTLR end synpred331



    # $ANTLR start synpred332
    def synpred332_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:32: ( LT )*
        while True: #loop424
            alt424 = 2
            LA424_0 = self.input.LA(1)

            if (LA424_0 == LT) :
                alt424 = 1


            if alt424 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3323202)
                if self.failed:
                    return 


            else:
                break #loop424


        if self.input.LA(1) == 64 or self.input.LA(1) == 128:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3323206
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:49: ( LT )*
        while True: #loop425
            alt425 = 2
            LA425_0 = self.input.LA(1)

            if (LA425_0 == LT) :
                LA425_2 = self.input.LA(2)

                if (self.synpred331()) :
                    alt425 = 1




            if alt425 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3323214)
                if self.failed:
                    return 


            else:
                break #loop425


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred3323218)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred332



    # $ANTLR start synpred336
    def synpred336_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3363250)
        if self.failed:
            return 


    # $ANTLR end synpred336



    # $ANTLR start synpred337
    def synpred337_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:21: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:23: ( LT )*
        while True: #loop426
            alt426 = 2
            LA426_0 = self.input.LA(1)

            if (LA426_0 == LT) :
                alt426 = 1


            if alt426 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3373234)
                if self.failed:
                    return 


            else:
                break #loop426


        if self.input.LA(1) == 62 or self.input.LA(1) == 100 or self.input.LA(1) == 129:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3373238
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:486:46: ( LT )*
        while True: #loop427
            alt427 = 2
            LA427_0 = self.input.LA(1)

            if (LA427_0 == LT) :
                LA427_2 = self.input.LA(2)

                if (self.synpred336()) :
                    alt427 = 1




            if alt427 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3373250)
                if self.failed:
                    return 


            else:
                break #loop427


        self.following.append(self.FOLLOW_unaryExpression_in_synpred3373254)
        self.unaryExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred337



    # $ANTLR start synpred352
    def synpred352_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:4: ( ( LT )* ( '<' | XMLComment ) )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:5: ( LT )* ( '<' | XMLComment )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:5: ( LT )*
        while True: #loop428
            alt428 = 2
            LA428_0 = self.input.LA(1)

            if (LA428_0 == LT) :
                alt428 = 1


            if alt428 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3523346)
                if self.failed:
                    return 


            else:
                break #loop428


        if self.input.LA(1) == XMLComment or self.input.LA(1) == 60:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3523349
                )
            raise mse




    # $ANTLR end synpred352



    # $ANTLR start synpred356
    def synpred356_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:505:4: ( objectLiteral )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:505:4: objectLiteral
        self.following.append(self.FOLLOW_objectLiteral_in_synpred3563387)
        self.objectLiteral()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred356



    # $ANTLR start synpred357
    def synpred357_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3573394)
        if self.failed:
            return 


    # $ANTLR end synpred357



    # $ANTLR start synpred359
    def synpred359_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3593419)
        if self.failed:
            return 


    # $ANTLR end synpred359



    # $ANTLR start synpred362
    def synpred362_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3623432)
        if self.failed:
            return 


    # $ANTLR end synpred362



    # $ANTLR start synpred364
    def synpred364_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:35: ( LT )* ',' ( ( LT )* assignmentExpression )?
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:35: ( LT )*
        while True: #loop430
            alt430 = 2
            LA430_0 = self.input.LA(1)

            if (LA430_0 == LT) :
                alt430 = 1


            if alt430 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3643426)
                if self.failed:
                    return 


            else:
                break #loop430


        self.match(self.input, 70, self.FOLLOW_70_in_synpred3643429)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:43: ( ( LT )* assignmentExpression )?
        alt432 = 2
        LA432_0 = self.input.LA(1)

        if ((LT <= LA432_0 <= RegularExpressionHacks) or LA432_0 == 60 or LA432_0 == 62 or LA432_0 == 64 or LA432_0 == 66 or (68 <= LA432_0 <= 69) or (72 <= LA432_0 <= 74) or LA432_0 == 80 or LA432_0 == 87 or LA432_0 == 98 or LA432_0 == 128 or (130 <= LA432_0 <= 142)) :
            alt432 = 1
        if alt432 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: ( LT )* assignmentExpression
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:44: ( LT )*
            while True: #loop431
                alt431 = 2
                LA431_0 = self.input.LA(1)

                if (LA431_0 == LT) :
                    LA431_2 = self.input.LA(2)

                    if (self.synpred362()) :
                        alt431 = 1




                if alt431 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_synpred3643432)
                    if self.failed:
                        return 


                else:
                    break #loop431


            self.following.append(self.FOLLOW_assignmentExpression_in_synpred3643435)
            self.assignmentExpression()
            self.following.pop()
            if self.failed:
                return 





    # $ANTLR end synpred364



    # $ANTLR start synpred368
    def synpred368_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:517:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3683484)
        if self.failed:
            return 


    # $ANTLR end synpred368



    # $ANTLR start synpred377
    def synpred377_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:25: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:25: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3773545)
        if self.failed:
            return 


    # $ANTLR end synpred377



    # $ANTLR start synpred476
    def synpred476_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:8: ( reFirstChar )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:581:8: reFirstChar
        self.following.append(self.FOLLOW_reFirstChar_in_synpred4764183)
        self.reFirstChar()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred476



    def synpred44(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred44_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred302(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred302_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred301(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred301_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred42(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred42_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred41(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred41_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred165(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred165_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred359(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred359_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred163(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred163_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred357(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred357_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred356(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred356_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred161(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred161_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred307(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred307_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred352(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred352_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred167(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred167_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred258(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred258_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred34(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred34_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred32(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred32_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred368(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred368_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred154(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred154_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred260(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred260_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred364(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred364_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred261(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred261_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred263(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred263_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred159(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred159_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred265(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred265_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred268(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred268_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred362(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred362_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred269(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred269_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred157(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred157_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred65(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred65_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred62(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred62_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred64(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred64_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred105(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred105_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred104(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred104_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred108(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred108_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred377(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred377_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred182(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred182_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred180(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred180_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred239(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred239_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred235(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred235_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred234(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred234_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred233(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred233_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred232(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred232_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred59(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred59_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred5(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred5_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred52(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred52_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred51(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred51_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred1(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred1_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred3(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred3_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred177(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred177_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred179(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred179_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred244(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred244_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred243(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred243_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred126(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred126_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred129(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred129_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred122(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred122_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred84(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred84_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred124(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred124_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred219(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred219_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred292(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred292_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred293(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred293_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred295(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred295_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred211(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred211_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred216(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred216_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred214(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred214_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred315(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred315_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred316(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred316_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred117(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred117_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred116(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred116_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred113(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred113_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred328(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred328_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred112(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred112_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred110(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred110_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred79(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred79_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred223(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred223_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred199(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred199_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred227(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred227_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred196(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred196_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred197(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred197_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred327(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred327_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred322(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred322_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred144(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred144_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred146(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred146_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred277(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred277_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred29(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred29_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred274(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred274_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred275(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred275_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred476(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred476_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred142(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred142_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred271(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred271_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred331(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred331_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred332(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred332_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred337(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred337_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred336(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred336_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred22(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred22_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred135(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred135_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred139(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred139_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred19(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred19_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred289(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred289_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred18(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred18_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred93(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred93_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred287(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred287_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred286(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred286_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred283(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred283_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred208(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred208_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred281(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred281_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred132(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred132_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred207(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred207_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred98(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred98_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred209(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred209_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred280(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred280_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred203(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred203_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred205(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred205_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred206(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred206_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred202(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred202_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred16(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred16_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success



    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\2\2\2\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA4_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\1\3\1\uffff\2\3\2\uffff\11\3\1\uffff\1\3\1\uffff\4\3\1\uffff\4"
        u"\3\1\uffff\2\3\2\uffff\1\3\35\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\1\3\1\uffff\2\3\2\uffff\11\3\1\uffff\1\3\1\uffff\4\3\1\uffff\4"
        u"\3\1\uffff\2\3\2\uffff\1\3\35\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    DFA4 = DFA
    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA7_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\14\uffff"
        u"\1\3\62\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\14\uffff"
        u"\1\3\62\uffff\2\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    DFA7 = DFA
    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA10_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\14\uffff"
        u"\1\3\62\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\14\uffff"
        u"\1\3\62\uffff\2\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    DFA10 = DFA
    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\37\1\41\3\uffff\1\35\1\41\1\35\1\77\2\uffff\1\35\1\41\1\36\1"
        u"\77\1\0\1\35"
        )

    DFA15_max = DFA.unpack(
        u"\1\102\1\u008b\3\uffff\3\u008b\1\101\2\uffff\2\u008b\1\102\1\101"
        u"\1\0\1\u008b"
        )

    DFA15_accept = DFA.unpack(
        u"\2\uffff\1\4\1\5\1\1\4\uffff\1\3\1\2\6\uffff"
        )

    DFA15_special = DFA.unpack(
        u"\17\uffff\1\0\1\uffff"
        )

            
    DFA15_transition = [
        DFA.unpack(u"\1\3\34\uffff\1\1\5\uffff\1\2"),
        DFA.unpack(u"\1\5\34\uffff\1\4\11\uffff\3\5\14\uffff\1\5\62\uffff"
        u"\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\2\6\7\uffff\3\10"
        u"\14\uffff\1\10\62\uffff\2\10"),
        DFA.unpack(u"\1\13\46\uffff\3\13\14\uffff\1\13\62\uffff\2\13"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\11\uffff\3\10\14"
        u"\uffff\1\10\62\uffff\2\10"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\2\6\7\uffff\3\10"
        u"\14\uffff\1\10\62\uffff\2\10"),
        DFA.unpack(u"\1\16\46\uffff\3\16\14\uffff\1\16\62\uffff\2\16"),
        DFA.unpack(u"\1\20\43\uffff\1\17"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\11\uffff\3\10\14"
        u"\uffff\1\10\62\uffff\2\10")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA15_15 = input.LA(1)

                 
                index15_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred18()):
                    s = 10

                elif (self.synpred19()):
                    s = 9

                 
                input.seek(index15_15)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 15, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA33_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA33_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA33_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\14\uffff\1\2\62\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\14\uffff\1\2\62\uffff"
        u"\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #33

    DFA33 = DFA
    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA32_max = DFA.unpack(
        u"\2\107\2\uffff"
        )

    DFA32_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA32_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #32

    DFA32 = DFA
    # lookup tables for DFA #40

    DFA40_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA40_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA40_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA40_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\103\1\uffff"
        )

    DFA40_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA40_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA40_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\1\1\1\uffff\4\1\1\uffff\4\1\1"
        u"\uffff\2\1\2\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #40

    DFA40 = DFA
    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\2"
        )

    DFA51_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA51_max = DFA.unpack(
        u"\1\113\1\u008e\2\uffff\1\u008e"
        )

    DFA51_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA51_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\4\2\1\3\1\uffff\11\2\1\uffff\6\2\1\uffff\7\2\2\uffff\1\2\35\uffff"
        u"\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\4\2\1\3\1\uffff\11\2\1\uffff\6\2\1\uffff\7\2\2\uffff\1\2\35\uffff"
        u"\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #51

    DFA51 = DFA
    # lookup tables for DFA #54

    DFA54_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA54_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA54_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA54_max = DFA.unpack(
        u"\2\113\2\uffff"
        )

    DFA54_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA54_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA54_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #54

    DFA54 = DFA
    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA56_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA56_max = DFA.unpack(
        u"\1\113\1\u008e\2\uffff\1\u008e"
        )

    DFA56_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA56_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA56_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3"),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\11\3\1\uffff\6\3\1\uffff\7\3\2\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\11\3\1\uffff\6\3\1\uffff\7\3\2\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3")
    ]

    # class definition for DFA #56

    DFA56 = DFA
    # lookup tables for DFA #62

    DFA62_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA62_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA62_min = DFA.unpack(
        u"\2\35\1\0\2\uffff"
        )

    DFA62_max = DFA.unpack(
        u"\2\121\1\0\2\uffff"
        )

    DFA62_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA62_special = DFA.unpack(
        u"\2\uffff\1\0\2\uffff"
        )

            
    DFA62_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #62

    class DFA62(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA62_2 = input.LA(1)

                 
                index62_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred84()):
                    s = 4

                elif (True):
                    s = 3

                 
                input.seek(index62_2)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 62, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #61

    DFA61_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA61_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA61_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA61_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA61_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA61_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA61_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\44\uffff\1\3\1\uffff\3\2\6\uffff\1"
        u"\3\5\uffff\1\2\62\uffff\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\44\uffff\1\3\1\uffff\3\2\6\uffff\1"
        u"\3\5\uffff\1\2\62\uffff\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #61

    DFA61 = DFA
    # lookup tables for DFA #67

    DFA67_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA67_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA67_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA67_max = DFA.unpack(
        u"\1\113\1\u008e\2\uffff\1\u008e"
        )

    DFA67_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA67_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA67_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3"),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\11\3\1\uffff\6\3\1\uffff\7\3\2\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\11\3\1\uffff\6\3\1\uffff\7\3\2\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3")
    ]

    # class definition for DFA #67

    DFA67 = DFA
    # lookup tables for DFA #70

    DFA70_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA70_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA70_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA70_max = DFA.unpack(
        u"\2\130\2\uffff"
        )

    DFA70_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA70_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA70_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #70

    DFA70 = DFA
    # lookup tables for DFA #76

    DFA76_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA76_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA76_min = DFA.unpack(
        u"\2\35\1\0\2\uffff"
        )

    DFA76_max = DFA.unpack(
        u"\2\121\1\0\2\uffff"
        )

    DFA76_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA76_special = DFA.unpack(
        u"\2\uffff\1\0\2\uffff"
        )

            
    DFA76_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #76

    class DFA76(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA76_2 = input.LA(1)

                 
                index76_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred98()):
                    s = 4

                elif (True):
                    s = 3

                 
                input.seek(index76_2)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 76, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #75

    DFA75_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA75_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA75_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA75_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA75_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA75_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA75_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\44\uffff\1\3\1\uffff\3\2\6\uffff\1"
        u"\3\5\uffff\1\2\62\uffff\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\44\uffff\1\3\1\uffff\3\2\6\uffff\1"
        u"\3\5\uffff\1\2\62\uffff\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #75

    DFA75 = DFA
    # lookup tables for DFA #81

    DFA81_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA81_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA81_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA81_max = DFA.unpack(
        u"\2\130\2\uffff"
        )

    DFA81_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA81_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA81_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #81

    DFA81 = DFA
    # lookup tables for DFA #102

    DFA102_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA102_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA102_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA102_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA102_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA102_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA102_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\1\uffff\2\2\6\uffff"
        u"\1\2\12\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\1\uffff\2\2\6\uffff"
        u"\1\2\12\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #102

    DFA102 = DFA
    # lookup tables for DFA #105

    DFA105_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA105_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA105_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA105_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA105_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA105_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA105_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\4\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\4\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #105

    DFA105 = DFA
    # lookup tables for DFA #108

    DFA108_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA108_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA108_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA108_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA108_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA108_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA108_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\5\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\5\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #108

    DFA108 = DFA
    # lookup tables for DFA #141

    DFA141_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA141_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA141_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA141_max = DFA.unpack(
        u"\2\135\2\uffff"
        )

    DFA141_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA141_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA141_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\24\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\24\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #141

    DFA141 = DFA
    # lookup tables for DFA #145

    DFA145_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA145_max = DFA.unpack(
        u"\2\110\2\uffff"
        )

    DFA145_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA145_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA145_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\45\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #145

    DFA145 = DFA
    # lookup tables for DFA #144

    DFA144_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA144_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA144_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA144_max = DFA.unpack(
        u"\2\135\2\uffff"
        )

    DFA144_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA144_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA144_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\31\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\31\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #144

    DFA144 = DFA
    # lookup tables for DFA #153

    DFA153_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA153_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA153_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA153_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\135\1\uffff"
        )

    DFA153_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA153_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA153_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\1\1\1\uffff\4\1\1\uffff\4\1\1"
        u"\3\2\1\2\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3\31\uffff"
        u"\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #153

    DFA153 = DFA
    # lookup tables for DFA #157

    DFA157_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA157_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA157_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA157_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA157_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA157_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA157_transition = [
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\11\3\1\uffff\6\3\1\uffff\7\3\1\uffff\1\2\1\3\35\uffff"
        u"\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\11\3\1\uffff\6\3\1\uffff\7\3\1\uffff\1\2\1\3\35\uffff"
        u"\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #157

    DFA157 = DFA
    # lookup tables for DFA #169

    DFA169_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA169_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA169_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA169_max = DFA.unpack(
        u"\2\113\2\uffff"
        )

    DFA169_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA169_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA169_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #169

    DFA169 = DFA
    # lookup tables for DFA #200

    DFA200_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA200_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA200_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA200_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA200_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA200_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA200_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\5\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\5\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #200

    DFA200 = DFA
    # lookup tables for DFA #218

    DFA218_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA218_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA218_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA218_max = DFA.unpack(
        u"\2\160\2\uffff"
        )

    DFA218_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA218_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA218_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3\27\uffff\1\2"),
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\14\uffff\1"
        u"\3\27\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #218

    DFA218 = DFA
    # lookup tables for DFA #224

    DFA224_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA224_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA224_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA224_max = DFA.unpack(
        u"\2\161\2\uffff"
        )

    DFA224_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA224_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA224_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #224

    DFA224 = DFA
    # lookup tables for DFA #230

    DFA230_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA230_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA230_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA230_max = DFA.unpack(
        u"\2\162\2\uffff"
        )

    DFA230_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA230_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA230_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #230

    DFA230 = DFA
    # lookup tables for DFA #236

    DFA236_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA236_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA236_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA236_max = DFA.unpack(
        u"\2\163\2\uffff"
        )

    DFA236_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA236_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA236_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #236

    DFA236 = DFA
    # lookup tables for DFA #242

    DFA242_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA242_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA242_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA242_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA242_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA242_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA242_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\4\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #242

    DFA242 = DFA
    # lookup tables for DFA #248

    DFA248_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA248_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA248_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA248_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA248_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA248_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA248_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\5\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #248

    DFA248 = DFA
    # lookup tables for DFA #254

    DFA254_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA254_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA254_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA254_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA254_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA254_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA254_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\14\uffff\1"
        u"\2\27\uffff\6\2\4\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #254

    DFA254 = DFA
    # lookup tables for DFA #260

    DFA260_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA260_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA260_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA260_max = DFA.unpack(
        u"\2\174\2\uffff"
        )

    DFA260_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA260_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA260_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\14\uffff\1\2\27\uffff\12\2\3\3"),
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\14\uffff\1\2\27\uffff\12\2\3\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #260

    DFA260 = DFA
    # lookup tables for DFA #276

    DFA276_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA276_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA276_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA276_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\121\1\uffff"
        )

    DFA276_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA276_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA276_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\uffff\2\1\1\3\1\uffff\3\1\5\uffff\1\1\1\3\5\uffff\1\1\12"
        u"\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\3\uffff\1"
        u"\3\12\uffff\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #276

    DFA276 = DFA
    # lookup tables for DFA #280

    DFA280_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA280_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA280_min = DFA.unpack(
        u"\2\35\1\0\2\uffff"
        )

    DFA280_max = DFA.unpack(
        u"\2\121\1\0\2\uffff"
        )

    DFA280_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA280_special = DFA.unpack(
        u"\2\uffff\1\0\2\uffff"
        )

            
    DFA280_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\1\50\uffff\1\2\12\uffff\1\3"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #280

    class DFA280(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA280_2 = input.LA(1)

                 
                index280_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred364()):
                    s = 4

                elif (True):
                    s = 3

                 
                input.seek(index280_2)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 280, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #279

    DFA279_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA279_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA279_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA279_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA279_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA279_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA279_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\5\uffff\1\2\1\3\5\uffff\1\2\12"
        u"\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\5\uffff\1\2\1\3\5\uffff\1\2\12"
        u"\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #279

    DFA279 = DFA
    # lookup tables for DFA #288

    DFA288_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA288_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA288_min = DFA.unpack(
        u"\3\35\1\uffff\1\35\1\uffff"
        )

    DFA288_max = DFA.unpack(
        u"\2\106\1\u008b\1\uffff\1\u008b\1\uffff"
        )

    DFA288_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1"
        )

    DFA288_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA288_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\14\uffff"
        u"\1\5\62\uffff\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\14\uffff"
        u"\1\5\62\uffff\2\5"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #288

    DFA288 = DFA
    # lookup tables for DFA #302

    DFA302_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA302_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA302_min = DFA.unpack(
        u"\1\36\1\35\1\uffff\3\35\1\uffff\1\35\1\uffff"
        )

    DFA302_max = DFA.unpack(
        u"\2\u008b\1\uffff\3\u008b\1\uffff\1\u008b\1\uffff"
        )

    DFA302_accept = DFA.unpack(
        u"\2\uffff\1\1\3\uffff\1\3\1\uffff\1\2"
        )

    DFA302_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA302_transition = [
        DFA.unpack(u"\1\2\1\uffff\2\2\46\uffff\3\2\14\uffff\1\2\62\uffff"
        u"\1\1\1\3"),
        DFA.unpack(u"\1\4\3\uffff\1\5\35\uffff\1\2\10\uffff\3\5\14\uffff"
        u"\1\5\62\uffff\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\uffff\1\5\35\uffff\1\2\10\uffff\3\5\14\uffff"
        u"\1\5\62\uffff\2\5"),
        DFA.unpack(u"\1\4\3\uffff\1\6\35\uffff\1\2\10\uffff\3\6\14\uffff"
        u"\1\6\62\uffff\2\6"),
        DFA.unpack(u"\1\7\3\uffff\1\10\43\uffff\1\6\2\uffff\3\10\14\uffff"
        u"\1\10\62\uffff\2\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\43\uffff\1\6\2\uffff\3\10\14\uffff"
        u"\1\10\62\uffff\2\10"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #302

    DFA302 = DFA
    # lookup tables for DFA #327

    DFA327_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA327_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA327_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA327_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\103\1\uffff"
        )

    DFA327_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA327_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA327_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\1\1\1\uffff\4\1\1\uffff\4\1\1"
        u"\uffff\2\1\2\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #327

    DFA327 = DFA
 

    FOLLOW_LT_in_program147 = frozenset([1])
    FOLLOW_sourceElements_in_program151 = frozenset([29])
    FOLLOW_LT_in_program153 = frozenset([1])
    FOLLOW_EOF_in_program157 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements170 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_sourceElements173 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_sourceElement_in_sourceElements177 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_functionDeclaration_in_sourceElement196 = frozenset([1])
    FOLLOW_statement_in_sourceElement201 = frozenset([1])
    FOLLOW_60_in_xmlStartTag219 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_xmlTagName_in_xmlStartTag221 = frozenset([29, 33, 61, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_xmlStartTag224 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_xmlAttribute_in_xmlStartTag228 = frozenset([29, 33, 61, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_xmlStartTag232 = frozenset([1])
    FOLLOW_61_in_xmlStartTag236 = frozenset([1])
    FOLLOW_60_in_xmlEndTag254 = frozenset([62])
    FOLLOW_62_in_xmlEndTag256 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_xmlTagName_in_xmlEndTag258 = frozenset([61])
    FOLLOW_61_in_xmlEndTag260 = frozenset([1])
    FOLLOW_60_in_xmlEmptyTag278 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_xmlTagName_in_xmlEmptyTag280 = frozenset([29, 33, 62, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_xmlEmptyTag283 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_xmlAttribute_in_xmlEmptyTag287 = frozenset([29, 33, 62, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_xmlEmptyTag291 = frozenset([1])
    FOLLOW_62_in_xmlEmptyTag295 = frozenset([61])
    FOLLOW_61_in_xmlEmptyTag297 = frozenset([1])
    FOLLOW_identifier_in_xmlTagName315 = frozenset([1, 63, 64])
    FOLLOW_set_in_xmlTagName319 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_xmlTagName325 = frozenset([1, 63, 64])
    FOLLOW_xmlAttributeName_in_xmlAttribute345 = frozenset([65])
    FOLLOW_65_in_xmlAttribute347 = frozenset([30, 66])
    FOLLOW_xmlAttributeValue_in_xmlAttribute349 = frozenset([1])
    FOLLOW_identifier_in_xmlAttributeName368 = frozenset([1, 63, 64])
    FOLLOW_set_in_xmlAttributeName372 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_xmlAttributeName378 = frozenset([1, 63, 64])
    FOLLOW_e4xSplice_in_xmlAttributeValue403 = frozenset([1])
    FOLLOW_StringLiteral_in_xmlAttributeValue408 = frozenset([1])
    FOLLOW_66_in_e4xSplice426 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_e4xSplice428 = frozenset([67])
    FOLLOW_67_in_e4xSplice430 = frozenset([1])
    FOLLOW_xmlEndTag_in_xmlPayload444 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_xmlPayload449 = frozenset([1])
    FOLLOW_xmlStartTag_in_xmlPayload454 = frozenset([1])
    FOLLOW_e4xSplice_in_xmlPayload459 = frozenset([1])
    FOLLOW_XMLComment_in_xmlPayload464 = frozenset([1])
    FOLLOW_LT_in_xmlLiteral477 = frozenset([29, 31, 60, 66])
    FOLLOW_xmlPayload_in_xmlLiteral480 = frozenset([1, 29, 31, 60, 66])
    FOLLOW_68_in_functionDeclaration495 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_functionDeclaration497 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_functionDeclaration500 = frozenset([29, 69])
    FOLLOW_LT_in_functionDeclaration502 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_functionDeclaration505 = frozenset([29, 66])
    FOLLOW_LT_in_functionDeclaration507 = frozenset([29, 66])
    FOLLOW_statementBlock_in_functionDeclaration510 = frozenset([1])
    FOLLOW_68_in_functionExpression536 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_functionExpression538 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_functionExpression541 = frozenset([29, 69])
    FOLLOW_LT_in_functionExpression543 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_functionExpression546 = frozenset([29, 66])
    FOLLOW_LT_in_functionExpression548 = frozenset([29, 66])
    FOLLOW_statementBlock_in_functionExpression551 = frozenset([1])
    FOLLOW_68_in_functionExpression572 = frozenset([29, 69])
    FOLLOW_LT_in_functionExpression574 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_functionExpression577 = frozenset([29, 66])
    FOLLOW_LT_in_functionExpression579 = frozenset([29, 66])
    FOLLOW_statementBlock_in_functionExpression582 = frozenset([1])
    FOLLOW_68_in_functionExpression604 = frozenset([29, 69])
    FOLLOW_LT_in_functionExpression606 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_functionExpression609 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_functionExpression611 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_functionExpression614 = frozenset([1])
    FOLLOW_69_in_formalParameterList641 = frozenset([29, 33, 71, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_formalParameterList644 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_formalParameterList647 = frozenset([29, 70, 71])
    FOLLOW_LT_in_formalParameterList650 = frozenset([29, 70])
    FOLLOW_70_in_formalParameterList653 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_formalParameterList655 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_formalParameterList658 = frozenset([29, 70, 71])
    FOLLOW_LT_in_formalParameterList664 = frozenset([29, 71])
    FOLLOW_71_in_formalParameterList667 = frozenset([1])
    FOLLOW_statementBlock_in_statement690 = frozenset([1])
    FOLLOW_variableStatement_in_statement695 = frozenset([1])
    FOLLOW_emptyStatement_in_statement700 = frozenset([1])
    FOLLOW_expressionStatement_in_statement705 = frozenset([1])
    FOLLOW_ifStatement_in_statement710 = frozenset([1])
    FOLLOW_iterationStatement_in_statement715 = frozenset([1])
    FOLLOW_continueStatement_in_statement720 = frozenset([1])
    FOLLOW_breakStatement_in_statement725 = frozenset([1])
    FOLLOW_returnStatement_in_statement730 = frozenset([1])
    FOLLOW_withStatement_in_statement735 = frozenset([1])
    FOLLOW_letStatement_in_statement740 = frozenset([1])
    FOLLOW_labelledStatement_in_statement745 = frozenset([1])
    FOLLOW_switchStatement_in_statement750 = frozenset([1])
    FOLLOW_throwStatement_in_statement755 = frozenset([1])
    FOLLOW_tryStatement_in_statement760 = frozenset([1])
    FOLLOW_defaultXmlNamespaceStatement_in_statement765 = frozenset([1])
    FOLLOW_72_in_defaultXmlNamespaceStatement776 = frozenset([73])
    FOLLOW_73_in_defaultXmlNamespaceStatement778 = frozenset([74])
    FOLLOW_74_in_defaultXmlNamespaceStatement780 = frozenset([29, 65])
    FOLLOW_LT_in_defaultXmlNamespaceStatement782 = frozenset([29, 65])
    FOLLOW_65_in_defaultXmlNamespaceStatement785 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_defaultXmlNamespaceStatement787 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_defaultXmlNamespaceStatement790 = frozenset([29, 75])
    FOLLOW_LT_in_defaultXmlNamespaceStatement793 = frozenset([1])
    FOLLOW_75_in_defaultXmlNamespaceStatement797 = frozenset([1])
    FOLLOW_66_in_statementBlock819 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_statementBlock821 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statementList_in_statementBlock825 = frozenset([29, 67])
    FOLLOW_LT_in_statementBlock828 = frozenset([29, 67])
    FOLLOW_67_in_statementBlock832 = frozenset([1])
    FOLLOW_66_in_statementBlock837 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 76, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_76_in_statementBlock839 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_statementBlock842 = frozenset([67])
    FOLLOW_67_in_statementBlock844 = frozenset([1])
    FOLLOW_statement_in_statementList857 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_statementList860 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_statementList864 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_77_in_variableStatement880 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_78_in_variableStatement884 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_79_in_variableStatement888 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_LT_in_variableStatement891 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_variableDeclarationList_in_variableStatement894 = frozenset([29, 75])
    FOLLOW_LT_in_variableStatement897 = frozenset([1])
    FOLLOW_75_in_variableStatement901 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList926 = frozenset([1, 29, 70])
    FOLLOW_LT_in_variableDeclarationList929 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclarationList933 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_LT_in_variableDeclarationList935 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_variableDeclaration_in_variableDeclarationList939 = frozenset([1, 29, 70])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn953 = frozenset([1, 29, 70])
    FOLLOW_LT_in_variableDeclarationListNoIn956 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclarationListNoIn960 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_LT_in_variableDeclarationListNoIn962 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn966 = frozenset([1, 29, 70])
    FOLLOW_identifier_in_variableDeclaration980 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclaration983 = frozenset([29, 65])
    FOLLOW_initialiser_in_variableDeclaration986 = frozenset([1])
    FOLLOW_80_in_variableDeclaration1006 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_LT_in_variableDeclaration1008 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_identifier_in_variableDeclaration1011 = frozenset([29, 70, 81])
    FOLLOW_LT_in_variableDeclaration1015 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclaration1018 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_LT_in_variableDeclaration1021 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_variableDeclaration1024 = frozenset([29, 70, 81])
    FOLLOW_LT_in_variableDeclaration1030 = frozenset([29, 70, 81])
    FOLLOW_70_in_variableDeclaration1034 = frozenset([29, 81])
    FOLLOW_LT_in_variableDeclaration1036 = frozenset([29, 81])
    FOLLOW_81_in_variableDeclaration1041 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclaration1044 = frozenset([29, 65])
    FOLLOW_initialiser_in_variableDeclaration1047 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn1079 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclarationNoIn1082 = frozenset([29, 65])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn1085 = frozenset([1])
    FOLLOW_80_in_variableDeclarationNoIn1105 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_LT_in_variableDeclarationNoIn1107 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_identifier_in_variableDeclarationNoIn1110 = frozenset([29, 70, 81])
    FOLLOW_LT_in_variableDeclarationNoIn1114 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclarationNoIn1117 = frozenset([29, 33, 70, 72, 73, 74, 81, 87, 138, 139])
    FOLLOW_LT_in_variableDeclarationNoIn1120 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_variableDeclarationNoIn1123 = frozenset([29, 70, 81])
    FOLLOW_LT_in_variableDeclarationNoIn1129 = frozenset([29, 70, 81])
    FOLLOW_70_in_variableDeclarationNoIn1133 = frozenset([29, 81])
    FOLLOW_LT_in_variableDeclarationNoIn1135 = frozenset([29, 81])
    FOLLOW_81_in_variableDeclarationNoIn1140 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclarationNoIn1143 = frozenset([29, 65])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn1146 = frozenset([1])
    FOLLOW_65_in_initialiser1178 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_initialiser1180 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_initialiser1183 = frozenset([1])
    FOLLOW_65_in_initialiserNoIn1201 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_initialiserNoIn1203 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn1206 = frozenset([1])
    FOLLOW_75_in_emptyStatement1224 = frozenset([1])
    FOLLOW_expression_in_expressionStatement1236 = frozenset([29, 75])
    FOLLOW_set_in_expressionStatement1238 = frozenset([1])
    FOLLOW_82_in_ifStatement1257 = frozenset([29, 69])
    FOLLOW_LT_in_ifStatement1259 = frozenset([1])
    FOLLOW_69_in_ifStatement1263 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1265 = frozenset([1])
    FOLLOW_expression_in_ifStatement1269 = frozenset([29, 71])
    FOLLOW_LT_in_ifStatement1271 = frozenset([1])
    FOLLOW_71_in_ifStatement1275 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1277 = frozenset([1])
    FOLLOW_statement_in_ifStatement1281 = frozenset([1, 29, 83])
    FOLLOW_LT_in_ifStatement1284 = frozenset([29, 83])
    FOLLOW_83_in_ifStatement1288 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1290 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_ifStatement1294 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement1308 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement1313 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement1318 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement1323 = frozenset([1])
    FOLLOW_84_in_doWhileStatement1335 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_doWhileStatement1337 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement1341 = frozenset([29, 85])
    FOLLOW_LT_in_doWhileStatement1343 = frozenset([1])
    FOLLOW_85_in_doWhileStatement1347 = frozenset([29, 69])
    FOLLOW_LT_in_doWhileStatement1349 = frozenset([1])
    FOLLOW_69_in_doWhileStatement1353 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_doWhileStatement1355 = frozenset([71])
    FOLLOW_71_in_doWhileStatement1357 = frozenset([29, 75])
    FOLLOW_set_in_doWhileStatement1359 = frozenset([1])
    FOLLOW_85_in_whileStatement1378 = frozenset([29, 69])
    FOLLOW_LT_in_whileStatement1380 = frozenset([1])
    FOLLOW_69_in_whileStatement1384 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_whileStatement1386 = frozenset([1])
    FOLLOW_expression_in_whileStatement1390 = frozenset([29, 71])
    FOLLOW_LT_in_whileStatement1392 = frozenset([1])
    FOLLOW_71_in_whileStatement1396 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_whileStatement1398 = frozenset([1])
    FOLLOW_statement_in_whileStatement1402 = frozenset([1])
    FOLLOW_86_in_forStatement1414 = frozenset([29, 69])
    FOLLOW_LT_in_forStatement1416 = frozenset([1])
    FOLLOW_69_in_forStatement1420 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 77, 79, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1423 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 77, 79, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_forStatementInitialiserPart_in_forStatement1427 = frozenset([29, 75])
    FOLLOW_LT_in_forStatement1431 = frozenset([1])
    FOLLOW_75_in_forStatement1435 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1438 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_forStatement1442 = frozenset([29, 75])
    FOLLOW_LT_in_forStatement1446 = frozenset([1])
    FOLLOW_75_in_forStatement1450 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 71, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1453 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_forStatement1457 = frozenset([29, 71])
    FOLLOW_LT_in_forStatement1461 = frozenset([1])
    FOLLOW_71_in_forStatement1465 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1467 = frozenset([1])
    FOLLOW_statement_in_forStatement1471 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart1483 = frozenset([1])
    FOLLOW_set_in_forStatementInitialiserPart1488 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_LT_in_forStatementInitialiserPart1494 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1498 = frozenset([1])
    FOLLOW_86_in_forInStatement1510 = frozenset([29, 69, 87])
    FOLLOW_LT_in_forInStatement1512 = frozenset([1])
    FOLLOW_87_in_forInStatement1516 = frozenset([29, 69])
    FOLLOW_LT_in_forInStatement1519 = frozenset([1])
    FOLLOW_69_in_forInStatement1523 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 77, 79, 80, 87, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1525 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement1529 = frozenset([29, 88])
    FOLLOW_LT_in_forInStatement1531 = frozenset([1])
    FOLLOW_88_in_forInStatement1535 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1537 = frozenset([1])
    FOLLOW_expression_in_forInStatement1541 = frozenset([29, 71])
    FOLLOW_LT_in_forInStatement1543 = frozenset([1])
    FOLLOW_71_in_forInStatement1547 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1549 = frozenset([1])
    FOLLOW_statement_in_forInStatement1553 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1565 = frozenset([1])
    FOLLOW_set_in_forInStatementInitialiserPart1570 = frozenset([29, 33, 72, 73, 74, 80, 87, 138, 139])
    FOLLOW_LT_in_forInStatementInitialiserPart1576 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1580 = frozenset([1])
    FOLLOW_89_in_continueStatement1591 = frozenset([29, 33, 72, 73, 74, 75, 87, 138, 139])
    FOLLOW_identifier_in_continueStatement1593 = frozenset([29, 75])
    FOLLOW_set_in_continueStatement1596 = frozenset([1])
    FOLLOW_90_in_breakStatement1614 = frozenset([29, 33, 72, 73, 74, 75, 87, 138, 139])
    FOLLOW_identifier_in_breakStatement1616 = frozenset([29, 75])
    FOLLOW_set_in_breakStatement1619 = frozenset([1])
    FOLLOW_76_in_returnStatement1637 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_returnStatement1639 = frozenset([29, 75])
    FOLLOW_set_in_returnStatement1642 = frozenset([1])
    FOLLOW_91_in_withStatement1661 = frozenset([29, 69])
    FOLLOW_LT_in_withStatement1663 = frozenset([1])
    FOLLOW_69_in_withStatement1667 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_withStatement1669 = frozenset([1])
    FOLLOW_expression_in_withStatement1673 = frozenset([29, 71])
    FOLLOW_LT_in_withStatement1675 = frozenset([1])
    FOLLOW_71_in_withStatement1679 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_withStatement1681 = frozenset([1])
    FOLLOW_statement_in_withStatement1685 = frozenset([1])
    FOLLOW_79_in_letStatement1696 = frozenset([29, 69])
    FOLLOW_LT_in_letStatement1698 = frozenset([1])
    FOLLOW_69_in_letStatement1702 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_letStatement1704 = frozenset([1])
    FOLLOW_expression_in_letStatement1708 = frozenset([29, 71])
    FOLLOW_LT_in_letStatement1710 = frozenset([1])
    FOLLOW_71_in_letStatement1714 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_letStatement1716 = frozenset([1])
    FOLLOW_statement_in_letStatement1720 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1731 = frozenset([29, 63])
    FOLLOW_LT_in_labelledStatement1733 = frozenset([1])
    FOLLOW_63_in_labelledStatement1737 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_labelledStatement1739 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1743 = frozenset([1])
    FOLLOW_92_in_switchStatement1755 = frozenset([29, 69])
    FOLLOW_LT_in_switchStatement1757 = frozenset([1])
    FOLLOW_69_in_switchStatement1761 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_switchStatement1763 = frozenset([1])
    FOLLOW_expression_in_switchStatement1767 = frozenset([29, 71])
    FOLLOW_LT_in_switchStatement1769 = frozenset([1])
    FOLLOW_71_in_switchStatement1773 = frozenset([29, 66])
    FOLLOW_LT_in_switchStatement1775 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1779 = frozenset([1])
    FOLLOW_66_in_caseBlock1791 = frozenset([29, 67, 72, 93])
    FOLLOW_LT_in_caseBlock1794 = frozenset([29, 93])
    FOLLOW_caseClause_in_caseBlock1798 = frozenset([29, 67, 72, 93])
    FOLLOW_LT_in_caseBlock1803 = frozenset([29, 72])
    FOLLOW_defaultClause_in_caseBlock1807 = frozenset([29, 67, 93])
    FOLLOW_LT_in_caseBlock1810 = frozenset([29, 93])
    FOLLOW_caseClause_in_caseBlock1814 = frozenset([29, 67, 93])
    FOLLOW_LT_in_caseBlock1820 = frozenset([1])
    FOLLOW_67_in_caseBlock1824 = frozenset([1])
    FOLLOW_93_in_caseClause1835 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_caseClause1837 = frozenset([1])
    FOLLOW_expression_in_caseClause1841 = frozenset([29, 63])
    FOLLOW_LT_in_caseClause1843 = frozenset([1])
    FOLLOW_63_in_caseClause1847 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_caseClause1849 = frozenset([1])
    FOLLOW_statementList_in_caseClause1853 = frozenset([1])
    FOLLOW_72_in_defaultClause1866 = frozenset([29, 63])
    FOLLOW_LT_in_defaultClause1868 = frozenset([1])
    FOLLOW_63_in_defaultClause1872 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_defaultClause1874 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1878 = frozenset([1])
    FOLLOW_94_in_throwStatement1891 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_throwStatement1893 = frozenset([29, 75])
    FOLLOW_set_in_throwStatement1895 = frozenset([1])
    FOLLOW_95_in_tryStatement1913 = frozenset([29, 66])
    FOLLOW_LT_in_tryStatement1915 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1919 = frozenset([29, 96, 97])
    FOLLOW_LT_in_tryStatement1921 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1926 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1930 = frozenset([1, 29, 97])
    FOLLOW_LT_in_tryStatement1933 = frozenset([29, 97])
    FOLLOW_finallyClause_in_tryStatement1937 = frozenset([1])
    FOLLOW_96_in_catchClause1958 = frozenset([29, 69])
    FOLLOW_LT_in_catchClause1960 = frozenset([1])
    FOLLOW_69_in_catchClause1964 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_catchClause1966 = frozenset([1])
    FOLLOW_identifier_in_catchClause1970 = frozenset([29, 71])
    FOLLOW_LT_in_catchClause1972 = frozenset([1])
    FOLLOW_71_in_catchClause1976 = frozenset([29, 66])
    FOLLOW_LT_in_catchClause1978 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1982 = frozenset([1])
    FOLLOW_97_in_finallyClause1994 = frozenset([29, 66])
    FOLLOW_LT_in_finallyClause1996 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause2000 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression2012 = frozenset([1, 29, 70])
    FOLLOW_LT_in_expression2015 = frozenset([29, 70])
    FOLLOW_70_in_expression2019 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_expression2021 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_expression2025 = frozenset([1, 29, 70])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn2039 = frozenset([1, 29, 70])
    FOLLOW_LT_in_expressionNoIn2042 = frozenset([29, 70])
    FOLLOW_70_in_expressionNoIn2046 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_expressionNoIn2048 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn2052 = frozenset([1, 29, 70])
    FOLLOW_leftHandSideExpression_in_assignmentExpression2066 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_assignmentExpression2068 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_assignmentExpression2071 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_assignmentExpression2073 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_assignmentExpression2076 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpression2095 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn2107 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_assignmentExpressionNoIn2109 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn2112 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_assignmentExpressionNoIn2114 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn2117 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn2136 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression2148 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression2153 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression2165 = frozenset([1])
    FOLLOW_98_in_newExpression2170 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 80, 87, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_newExpression2172 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 80, 87, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_newExpression_in_newExpression2175 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression2197 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_LT_in_memberExpression2200 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_memberExpression2203 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_functionExpression_in_memberExpression2223 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_LT_in_memberExpression2226 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_memberExpression2230 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_98_in_memberExpression2237 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 80, 87, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_memberExpression2239 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 80, 87, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_memberExpression_in_memberExpression2242 = frozenset([29, 69])
    FOLLOW_LT_in_memberExpression2244 = frozenset([29, 69])
    FOLLOW_arguments_in_memberExpression2247 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_LT_in_memberExpression2250 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_memberExpression2253 = frozenset([1, 29, 63, 80, 99])
    FOLLOW_indexSuffix_in_memberExpressionSuffix2290 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix2295 = frozenset([1])
    FOLLOW_descendentSuffix_in_memberExpressionSuffix2300 = frozenset([1])
    FOLLOW_namespaceSuffix_in_memberExpressionSuffix2306 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression2321 = frozenset([29, 69, 99])
    FOLLOW_LT_in_callExpression2323 = frozenset([29, 69, 99])
    FOLLOW_99_in_callExpression2326 = frozenset([29, 69])
    FOLLOW_LT_in_callExpression2329 = frozenset([29, 69])
    FOLLOW_arguments_in_callExpression2332 = frozenset([1, 29, 63, 69, 80, 99])
    FOLLOW_LT_in_callExpression2335 = frozenset([29, 63, 69, 80, 99])
    FOLLOW_callExpressionSuffix_in_callExpression2338 = frozenset([1, 29, 63, 69, 80, 99])
    FOLLOW_arguments_in_callExpressionSuffix2367 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix2372 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2377 = frozenset([1])
    FOLLOW_descendentSuffix_in_callExpressionSuffix2382 = frozenset([1])
    FOLLOW_namespaceSuffix_in_callExpressionSuffix2388 = frozenset([1])
    FOLLOW_69_in_arguments2403 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 71, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arguments2406 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arguments2409 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2411 = frozenset([29, 70, 71])
    FOLLOW_70_in_arguments2415 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arguments2417 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arguments2420 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2422 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2429 = frozenset([29, 71])
    FOLLOW_71_in_arguments2432 = frozenset([1])
    FOLLOW_80_in_indexSuffix2455 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_indexSuffix2457 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_indexSuffix2460 = frozenset([29, 81])
    FOLLOW_LT_in_indexSuffix2462 = frozenset([29, 81])
    FOLLOW_81_in_indexSuffix2465 = frozenset([1])
    FOLLOW_99_in_propertyReferenceSuffix2488 = frozenset([29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_LT_in_propertyReferenceSuffix2490 = frozenset([29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2493 = frozenset([1])
    FOLLOW_99_in_descendentSuffix2514 = frozenset([99])
    FOLLOW_99_in_descendentSuffix2516 = frozenset([29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_LT_in_descendentSuffix2518 = frozenset([29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_descendentSuffix2521 = frozenset([1])
    FOLLOW_63_in_namespaceSuffix2542 = frozenset([63])
    FOLLOW_63_in_namespaceSuffix2544 = frozenset([1, 29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_LT_in_namespaceSuffix2546 = frozenset([1, 29, 33, 72, 73, 74, 87, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_namespaceSuffix2549 = frozenset([1])
    FOLLOW_identifier_in_e4xIdentifier2572 = frozenset([1])
    FOLLOW_100_in_e4xIdentifier2577 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression2644 = frozenset([1, 29, 112])
    FOLLOW_LT_in_conditionalExpression2647 = frozenset([29, 112])
    FOLLOW_112_in_conditionalExpression2651 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpression2653 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_conditionalExpression2657 = frozenset([29, 63])
    FOLLOW_LT_in_conditionalExpression2659 = frozenset([29, 63])
    FOLLOW_63_in_conditionalExpression2663 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpression2665 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_conditionalExpression2669 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2682 = frozenset([1, 29, 112])
    FOLLOW_LT_in_conditionalExpressionNoIn2685 = frozenset([29, 112])
    FOLLOW_112_in_conditionalExpressionNoIn2689 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpressionNoIn2691 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2695 = frozenset([29, 63])
    FOLLOW_LT_in_conditionalExpressionNoIn2697 = frozenset([29, 63])
    FOLLOW_63_in_conditionalExpressionNoIn2701 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpressionNoIn2703 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2707 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression2720 = frozenset([1, 29, 113])
    FOLLOW_LT_in_logicalORExpression2723 = frozenset([29, 113])
    FOLLOW_113_in_logicalORExpression2727 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalORExpression2729 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_logicalANDExpression_in_logicalORExpression2733 = frozenset([1, 29, 113])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2747 = frozenset([1, 29, 113])
    FOLLOW_LT_in_logicalORExpressionNoIn2750 = frozenset([29, 113])
    FOLLOW_113_in_logicalORExpressionNoIn2754 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalORExpressionNoIn2756 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2760 = frozenset([1, 29, 113])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2774 = frozenset([1, 29, 114])
    FOLLOW_LT_in_logicalANDExpression2777 = frozenset([29, 114])
    FOLLOW_114_in_logicalANDExpression2781 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalANDExpression2783 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2787 = frozenset([1, 29, 114])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2801 = frozenset([1, 29, 114])
    FOLLOW_LT_in_logicalANDExpressionNoIn2804 = frozenset([29, 114])
    FOLLOW_114_in_logicalANDExpressionNoIn2808 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalANDExpressionNoIn2810 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2814 = frozenset([1, 29, 114])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2828 = frozenset([1, 29, 115])
    FOLLOW_LT_in_bitwiseORExpression2831 = frozenset([29, 115])
    FOLLOW_115_in_bitwiseORExpression2835 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseORExpression2837 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2841 = frozenset([1, 29, 115])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2855 = frozenset([1, 29, 115])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2858 = frozenset([29, 115])
    FOLLOW_115_in_bitwiseORExpressionNoIn2862 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2864 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2868 = frozenset([1, 29, 115])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2882 = frozenset([1, 29, 116])
    FOLLOW_LT_in_bitwiseXORExpression2885 = frozenset([29, 116])
    FOLLOW_116_in_bitwiseXORExpression2889 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseXORExpression2891 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2895 = frozenset([1, 29, 116])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2909 = frozenset([1, 29, 116])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2912 = frozenset([29, 116])
    FOLLOW_116_in_bitwiseXORExpressionNoIn2916 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2918 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2922 = frozenset([1, 29, 116])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2936 = frozenset([1, 29, 117])
    FOLLOW_LT_in_bitwiseANDExpression2939 = frozenset([29, 117])
    FOLLOW_117_in_bitwiseANDExpression2943 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseANDExpression2945 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2949 = frozenset([1, 29, 117])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2963 = frozenset([1, 29, 117])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2966 = frozenset([29, 117])
    FOLLOW_117_in_bitwiseANDExpressionNoIn2970 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2972 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2976 = frozenset([1, 29, 117])
    FOLLOW_relationalExpression_in_equalityExpression2990 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpression2993 = frozenset([29, 118, 119, 120, 121])
    FOLLOW_set_in_equalityExpression2997 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_equalityExpression3013 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_relationalExpression_in_equalityExpression3017 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn3030 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpressionNoIn3033 = frozenset([29, 118, 119, 120, 121])
    FOLLOW_set_in_equalityExpressionNoIn3037 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_equalityExpressionNoIn3053 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn3057 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_shiftExpression_in_relationalExpression3071 = frozenset([1, 29, 60, 61, 88, 122, 123, 124])
    FOLLOW_LT_in_relationalExpression3074 = frozenset([29, 60, 61, 88, 122, 123, 124])
    FOLLOW_set_in_relationalExpression3078 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_relationalExpression3102 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_relationalExpression3106 = frozenset([1, 29, 60, 61, 88, 122, 123, 124])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn3119 = frozenset([1, 29, 60, 61, 122, 123, 124])
    FOLLOW_LT_in_relationalExpressionNoIn3122 = frozenset([29, 60, 61, 122, 123, 124])
    FOLLOW_set_in_relationalExpressionNoIn3126 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_relationalExpressionNoIn3146 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn3150 = frozenset([1, 29, 60, 61, 122, 123, 124])
    FOLLOW_additiveExpression_in_shiftExpression3163 = frozenset([1, 29, 125, 126, 127])
    FOLLOW_LT_in_shiftExpression3166 = frozenset([29, 125, 126, 127])
    FOLLOW_set_in_shiftExpression3170 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_shiftExpression3182 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_additiveExpression_in_shiftExpression3186 = frozenset([1, 29, 125, 126, 127])
    FOLLOW_multiplicativeExpression_in_additiveExpression3199 = frozenset([1, 29, 64, 128])
    FOLLOW_LT_in_additiveExpression3202 = frozenset([29, 64, 128])
    FOLLOW_set_in_additiveExpression3206 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_additiveExpression3214 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_multiplicativeExpression_in_additiveExpression3218 = frozenset([1, 29, 64, 128])
    FOLLOW_unaryExpression_in_multiplicativeExpression3231 = frozenset([1, 29, 62, 100, 129])
    FOLLOW_LT_in_multiplicativeExpression3234 = frozenset([29, 62, 100, 129])
    FOLLOW_set_in_multiplicativeExpression3238 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_multiplicativeExpression3250 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_multiplicativeExpression3254 = frozenset([1, 29, 62, 100, 129])
    FOLLOW_postfixExpression_in_unaryExpression3267 = frozenset([1])
    FOLLOW_set_in_unaryExpression3272 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_unaryExpression3308 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression3320 = frozenset([1, 133, 134])
    FOLLOW_set_in_postfixExpression3322 = frozenset([1])
    FOLLOW_137_in_primaryExpression3340 = frozenset([1])
    FOLLOW_xmlLiteral_in_primaryExpression3357 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression3362 = frozenset([1])
    FOLLOW_literal_in_primaryExpression3377 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression3382 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression3387 = frozenset([1])
    FOLLOW_69_in_primaryExpression3392 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_primaryExpression3394 = frozenset([1])
    FOLLOW_expression_in_primaryExpression3398 = frozenset([29, 71])
    FOLLOW_LT_in_primaryExpression3400 = frozenset([1])
    FOLLOW_71_in_primaryExpression3404 = frozenset([1])
    FOLLOW_80_in_arrayLiteral3417 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 80, 81, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arrayLiteral3419 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 80, 81, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arrayLiteral3422 = frozenset([29, 70, 81])
    FOLLOW_LT_in_arrayLiteral3426 = frozenset([29, 70])
    FOLLOW_70_in_arrayLiteral3429 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 80, 81, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arrayLiteral3432 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arrayLiteral3435 = frozenset([29, 70, 81])
    FOLLOW_LT_in_arrayLiteral3441 = frozenset([29, 70, 81])
    FOLLOW_70_in_arrayLiteral3445 = frozenset([29, 81])
    FOLLOW_LT_in_arrayLiteral3447 = frozenset([29, 81])
    FOLLOW_81_in_arrayLiteral3452 = frozenset([1])
    FOLLOW_66_in_objectLiteral3482 = frozenset([29, 30, 32, 33, 67, 70, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_objectLiteral3484 = frozenset([29, 30, 32, 33, 67, 70, 72, 73, 74, 87, 138, 139])
    FOLLOW_propertyNameAndValue_in_objectLiteral3487 = frozenset([29, 67, 70])
    FOLLOW_LT_in_objectLiteral3491 = frozenset([29, 70])
    FOLLOW_70_in_objectLiteral3494 = frozenset([29, 30, 32, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_objectLiteral3496 = frozenset([29, 30, 32, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_propertyNameAndValue_in_objectLiteral3499 = frozenset([29, 67, 70])
    FOLLOW_LT_in_objectLiteral3503 = frozenset([29, 67, 70])
    FOLLOW_70_in_objectLiteral3507 = frozenset([29, 67])
    FOLLOW_LT_in_objectLiteral3509 = frozenset([29, 67])
    FOLLOW_67_in_objectLiteral3514 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue3538 = frozenset([29, 63])
    FOLLOW_LT_in_propertyNameAndValue3540 = frozenset([29, 63])
    FOLLOW_63_in_propertyNameAndValue3543 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_propertyNameAndValue3545 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_propertyNameAndValue3548 = frozenset([1])
    FOLLOW_138_in_propertyNameAndValue3570 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_139_in_propertyNameAndValue3574 = frozenset([33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3579 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_propertyNameAndValue3581 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3586 = frozenset([29, 69])
    FOLLOW_LT_in_propertyNameAndValue3588 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_propertyNameAndValue3591 = frozenset([29, 66])
    FOLLOW_LT_in_propertyNameAndValue3593 = frozenset([29, 66])
    FOLLOW_statementBlock_in_propertyNameAndValue3596 = frozenset([1])
    FOLLOW_138_in_propertyNameAndValue3629 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_139_in_propertyNameAndValue3633 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_propertyNameAndValue3636 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3641 = frozenset([29, 69])
    FOLLOW_LT_in_propertyNameAndValue3643 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_propertyNameAndValue3646 = frozenset([29, 66])
    FOLLOW_LT_in_propertyNameAndValue3648 = frozenset([29, 66])
    FOLLOW_statementBlock_in_propertyNameAndValue3651 = frozenset([1])
    FOLLOW_identifier_in_propertyName3686 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName3691 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName3696 = frozenset([1])
    FOLLOW_140_in_literal3708 = frozenset([1])
    FOLLOW_141_in_literal3717 = frozenset([1])
    FOLLOW_142_in_literal3726 = frozenset([1])
    FOLLOW_StringLiteral_in_literal3735 = frozenset([1])
    FOLLOW_NumericLiteral_in_literal3748 = frozenset([1])
    FOLLOW_regularExpressionLiteral_in_literal3761 = frozenset([1])
    FOLLOW_set_in_reFirstChar0 = frozenset([1])
    FOLLOW_reFirstChar_in_reChars4162 = frozenset([1])
    FOLLOW_100_in_reChars4167 = frozenset([1])
    FOLLOW_62_in_regularExpressionLiteral4181 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_reFirstChar_in_regularExpressionLiteral4183 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_reChars_in_regularExpressionLiteral4186 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_62_in_regularExpressionLiteral4189 = frozenset([1, 33])
    FOLLOW_Identifier_in_regularExpressionLiteral4191 = frozenset([1])
    FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral4197 = frozenset([1, 33])
    FOLLOW_Identifier_in_regularExpressionLiteral4199 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_LT_in_synpred1147 = frozenset([1])
    FOLLOW_LT_in_synpred3173 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_functionDeclaration_in_synpred5192 = frozenset([1])
    FOLLOW_66_in_synpred16399 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_synpred18449 = frozenset([1])
    FOLLOW_xmlStartTag_in_synpred19454 = frozenset([1])
    FOLLOW_LT_in_synpred22477 = frozenset([29, 31, 60, 66])
    FOLLOW_xmlPayload_in_synpred22480 = frozenset([1])
    FOLLOW_68_in_synpred29536 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_synpred29538 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_synpred29541 = frozenset([29, 69])
    FOLLOW_LT_in_synpred29543 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_synpred29546 = frozenset([29, 66])
    FOLLOW_LT_in_synpred29548 = frozenset([29, 66])
    FOLLOW_statementBlock_in_synpred29551 = frozenset([1])
    FOLLOW_68_in_synpred32572 = frozenset([29, 69])
    FOLLOW_LT_in_synpred32574 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_synpred32577 = frozenset([29, 66])
    FOLLOW_LT_in_synpred32579 = frozenset([29, 66])
    FOLLOW_statementBlock_in_synpred32582 = frozenset([1])
    FOLLOW_LT_in_synpred34611 = frozenset([1])
    FOLLOW_statementBlock_in_synpred41690 = frozenset([1])
    FOLLOW_variableStatement_in_synpred42695 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred44705 = frozenset([1])
    FOLLOW_letStatement_in_synpred51740 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred52745 = frozenset([1])
    FOLLOW_LT_in_synpred59821 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_66_in_synpred62819 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred62821 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statementList_in_synpred62825 = frozenset([29, 67])
    FOLLOW_LT_in_synpred62828 = frozenset([29, 67])
    FOLLOW_67_in_synpred62832 = frozenset([1])
    FOLLOW_LT_in_synpred64860 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred65860 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_synpred65864 = frozenset([1])
    FOLLOW_LT_in_synpred791008 = frozenset([1])
    FOLLOW_LT_in_synpred841015 = frozenset([29, 70])
    FOLLOW_70_in_synpred841018 = frozenset([1, 29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_synpred841021 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_synpred841024 = frozenset([1])
    FOLLOW_LT_in_synpred931107 = frozenset([1])
    FOLLOW_LT_in_synpred981114 = frozenset([29, 70])
    FOLLOW_70_in_synpred981117 = frozenset([1, 29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_LT_in_synpred981120 = frozenset([29, 33, 72, 73, 74, 87, 138, 139])
    FOLLOW_identifier_in_synpred981123 = frozenset([1])
    FOLLOW_LT_in_synpred1041180 = frozenset([1])
    FOLLOW_LT_in_synpred1051203 = frozenset([1])
    FOLLOW_LT_in_synpred1081265 = frozenset([1])
    FOLLOW_LT_in_synpred1101277 = frozenset([1])
    FOLLOW_LT_in_synpred1121290 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1131284 = frozenset([29, 83])
    FOLLOW_83_in_synpred1131288 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1131290 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 89, 90, 91, 92, 94, 95, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_synpred1131294 = frozenset([1])
    FOLLOW_forStatement_in_synpred1161318 = frozenset([1])
    FOLLOW_LT_in_synpred1171337 = frozenset([1])
    FOLLOW_LT_in_synpred1221386 = frozenset([1])
    FOLLOW_LT_in_synpred1241398 = frozenset([1])
    FOLLOW_LT_in_synpred1261423 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 77, 79, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1291438 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1321453 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1351467 = frozenset([1])
    FOLLOW_LT_in_synpred1391512 = frozenset([1])
    FOLLOW_LT_in_synpred1421525 = frozenset([1])
    FOLLOW_LT_in_synpred1441537 = frozenset([1])
    FOLLOW_LT_in_synpred1461549 = frozenset([1])
    FOLLOW_expression_in_synpred1541639 = frozenset([1])
    FOLLOW_LT_in_synpred1571669 = frozenset([1])
    FOLLOW_LT_in_synpred1591681 = frozenset([1])
    FOLLOW_LT_in_synpred1611704 = frozenset([1])
    FOLLOW_LT_in_synpred1631716 = frozenset([1])
    FOLLOW_LT_in_synpred1651739 = frozenset([1])
    FOLLOW_LT_in_synpred1671763 = frozenset([1])
    FOLLOW_LT_in_synpred1771837 = frozenset([1])
    FOLLOW_LT_in_synpred1791849 = frozenset([1])
    FOLLOW_statementList_in_synpred1801853 = frozenset([1])
    FOLLOW_LT_in_synpred1821874 = frozenset([1])
    FOLLOW_LT_in_synpred1962021 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1972015 = frozenset([29, 70])
    FOLLOW_70_in_synpred1972019 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1972021 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred1972025 = frozenset([1])
    FOLLOW_LT_in_synpred1992048 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2022073 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred2032066 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_synpred2032068 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_synpred2032071 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2032073 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred2032076 = frozenset([1])
    FOLLOW_LT_in_synpred2052114 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred2062107 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_synpred2062109 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_synpred2062112 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2062114 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_synpred2062117 = frozenset([1])
    FOLLOW_callExpression_in_synpred2072148 = frozenset([1])
    FOLLOW_memberExpression_in_synpred2082165 = frozenset([1])
    FOLLOW_LT_in_synpred2092172 = frozenset([1])
    FOLLOW_LT_in_synpred2112200 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_synpred2112203 = frozenset([1])
    FOLLOW_LT_in_synpred2142226 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_synpred2142230 = frozenset([1])
    FOLLOW_LT_in_synpred2162239 = frozenset([1])
    FOLLOW_LT_in_synpred2192250 = frozenset([29, 63, 80, 99])
    FOLLOW_memberExpressionSuffix_in_synpred2192253 = frozenset([1])
    FOLLOW_LT_in_synpred2232323 = frozenset([1])
    FOLLOW_LT_in_synpred2272335 = frozenset([29, 63, 69, 80, 99])
    FOLLOW_callExpressionSuffix_in_synpred2272338 = frozenset([1])
    FOLLOW_LT_in_synpred2322406 = frozenset([1])
    FOLLOW_LT_in_synpred2332411 = frozenset([1])
    FOLLOW_LT_in_synpred2342417 = frozenset([1])
    FOLLOW_LT_in_synpred2352422 = frozenset([1])
    FOLLOW_LT_in_synpred2392457 = frozenset([1])
    FOLLOW_LT_in_synpred2432546 = frozenset([1])
    FOLLOW_e4xIdentifier_in_synpred2442549 = frozenset([1])
    FOLLOW_LT_in_synpred2582653 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2602665 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2612647 = frozenset([29, 112])
    FOLLOW_112_in_synpred2612651 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2612653 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred2612657 = frozenset([29, 63])
    FOLLOW_LT_in_synpred2612659 = frozenset([29, 63])
    FOLLOW_63_in_synpred2612663 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2612665 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred2612669 = frozenset([1])
    FOLLOW_LT_in_synpred2632691 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2652703 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2682729 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2692723 = frozenset([29, 113])
    FOLLOW_113_in_synpred2692727 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2692729 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_logicalANDExpression_in_synpred2692733 = frozenset([1])
    FOLLOW_LT_in_synpred2712756 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2742783 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2752777 = frozenset([29, 114])
    FOLLOW_114_in_synpred2752781 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2752783 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseORExpression_in_synpred2752787 = frozenset([1])
    FOLLOW_LT_in_synpred2772810 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2802837 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2812831 = frozenset([29, 115])
    FOLLOW_115_in_synpred2812835 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2812837 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseXORExpression_in_synpred2812841 = frozenset([1])
    FOLLOW_LT_in_synpred2832864 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2862891 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2872885 = frozenset([29, 116])
    FOLLOW_116_in_synpred2872889 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2872891 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseANDExpression_in_synpred2872895 = frozenset([1])
    FOLLOW_LT_in_synpred2892918 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2922945 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2932939 = frozenset([29, 117])
    FOLLOW_117_in_synpred2932943 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2932945 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_equalityExpression_in_synpred2932949 = frozenset([1])
    FOLLOW_LT_in_synpred2952972 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3013013 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3022993 = frozenset([29, 118, 119, 120, 121])
    FOLLOW_set_in_synpred3022997 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3023013 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_relationalExpression_in_synpred3023017 = frozenset([1])
    FOLLOW_LT_in_synpred3073053 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3153102 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3163074 = frozenset([29, 60, 61, 88, 122, 123, 124])
    FOLLOW_set_in_synpred3163078 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3163102 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_synpred3163106 = frozenset([1])
    FOLLOW_LT_in_synpred3223146 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3273182 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3283166 = frozenset([29, 125, 126, 127])
    FOLLOW_set_in_synpred3283170 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3283182 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_additiveExpression_in_synpred3283186 = frozenset([1])
    FOLLOW_LT_in_synpred3313214 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3323202 = frozenset([29, 64, 128])
    FOLLOW_set_in_synpred3323206 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3323214 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_multiplicativeExpression_in_synpred3323218 = frozenset([1])
    FOLLOW_LT_in_synpred3363250 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3373234 = frozenset([29, 62, 100, 129])
    FOLLOW_set_in_synpred3373238 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3373250 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_synpred3373254 = frozenset([1])
    FOLLOW_LT_in_synpred3523346 = frozenset([29, 31, 60])
    FOLLOW_set_in_synpred3523349 = frozenset([1])
    FOLLOW_objectLiteral_in_synpred3563387 = frozenset([1])
    FOLLOW_LT_in_synpred3573394 = frozenset([1])
    FOLLOW_LT_in_synpred3593419 = frozenset([1])
    FOLLOW_LT_in_synpred3623432 = frozenset([1])
    FOLLOW_LT_in_synpred3643426 = frozenset([29, 70])
    FOLLOW_70_in_synpred3643429 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3643432 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 80, 87, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred3643435 = frozenset([1])
    FOLLOW_LT_in_synpred3683484 = frozenset([1])
    FOLLOW_LT_in_synpred3773545 = frozenset([1])
    FOLLOW_reFirstChar_in_synpred4764183 = frozenset([1])

