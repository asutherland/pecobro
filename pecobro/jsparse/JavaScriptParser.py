# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-29 05:37:45

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
    "'var'", "'const'", "'let'", "'if'", "'else'", "'do'", "'while'", "'for'", 
    "'each'", "'in'", "'continue'", "'break'", "'with'", "'switch'", "'case'", 
    "'throw'", "'try'", "'catch'", "'finally'", "'new'", "'.'", "'['", "']'", 
    "'*'", "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", 
    "'&='", "'^='", "'|='", "'?'", "'||'", "'&&'", "'|'", "'^'", "'&'", 
    "'=='", "'!='", "'==='", "'!=='", "'<='", "'>='", "'instanceof'", "'<<'", 
    "'>>'", "'>>>'", "'+'", "'%'", "'delete'", "'void'", "'typeof'", "'++'", 
    "'--'", "'~'", "'!'", "'this'", "'get'", "'set'", "'null'", "'true'", 
    "'false'", "'#'"
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
        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
            )
        self.dfa31 = self.DFA31(
            self, 31,
            eot = self.DFA31_eot,
            eof = self.DFA31_eof,
            min = self.DFA31_min,
            max = self.DFA31_max,
            accept = self.DFA31_accept,
            special = self.DFA31_special,
            transition = self.DFA31_transition
            )
        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
            )
        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )
        self.dfa49 = self.DFA49(
            self, 49,
            eot = self.DFA49_eot,
            eof = self.DFA49_eof,
            min = self.DFA49_min,
            max = self.DFA49_max,
            accept = self.DFA49_accept,
            special = self.DFA49_special,
            transition = self.DFA49_transition
            )
        self.dfa52 = self.DFA52(
            self, 52,
            eot = self.DFA52_eot,
            eof = self.DFA52_eof,
            min = self.DFA52_min,
            max = self.DFA52_max,
            accept = self.DFA52_accept,
            special = self.DFA52_special,
            transition = self.DFA52_transition
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
        self.dfa79 = self.DFA79(
            self, 79,
            eot = self.DFA79_eot,
            eof = self.DFA79_eof,
            min = self.DFA79_min,
            max = self.DFA79_max,
            accept = self.DFA79_accept,
            special = self.DFA79_special,
            transition = self.DFA79_transition
            )
        self.dfa82 = self.DFA82(
            self, 82,
            eot = self.DFA82_eot,
            eof = self.DFA82_eof,
            min = self.DFA82_min,
            max = self.DFA82_max,
            accept = self.DFA82_accept,
            special = self.DFA82_special,
            transition = self.DFA82_transition
            )
        self.dfa111 = self.DFA111(
            self, 111,
            eot = self.DFA111_eot,
            eof = self.DFA111_eof,
            min = self.DFA111_min,
            max = self.DFA111_max,
            accept = self.DFA111_accept,
            special = self.DFA111_special,
            transition = self.DFA111_transition
            )
        self.dfa115 = self.DFA115(
            self, 115,
            eot = self.DFA115_eot,
            eof = self.DFA115_eof,
            min = self.DFA115_min,
            max = self.DFA115_max,
            accept = self.DFA115_accept,
            special = self.DFA115_special,
            transition = self.DFA115_transition
            )
        self.dfa114 = self.DFA114(
            self, 114,
            eot = self.DFA114_eot,
            eof = self.DFA114_eof,
            min = self.DFA114_min,
            max = self.DFA114_max,
            accept = self.DFA114_accept,
            special = self.DFA114_special,
            transition = self.DFA114_transition
            )
        self.dfa123 = self.DFA123(
            self, 123,
            eot = self.DFA123_eot,
            eof = self.DFA123_eof,
            min = self.DFA123_min,
            max = self.DFA123_max,
            accept = self.DFA123_accept,
            special = self.DFA123_special,
            transition = self.DFA123_transition
            )
        self.dfa127 = self.DFA127(
            self, 127,
            eot = self.DFA127_eot,
            eof = self.DFA127_eof,
            min = self.DFA127_min,
            max = self.DFA127_max,
            accept = self.DFA127_accept,
            special = self.DFA127_special,
            transition = self.DFA127_transition
            )
        self.dfa136 = self.DFA136(
            self, 136,
            eot = self.DFA136_eot,
            eof = self.DFA136_eof,
            min = self.DFA136_min,
            max = self.DFA136_max,
            accept = self.DFA136_accept,
            special = self.DFA136_special,
            transition = self.DFA136_transition
            )
        self.dfa139 = self.DFA139(
            self, 139,
            eot = self.DFA139_eot,
            eof = self.DFA139_eof,
            min = self.DFA139_min,
            max = self.DFA139_max,
            accept = self.DFA139_accept,
            special = self.DFA139_special,
            transition = self.DFA139_transition
            )
        self.dfa170 = self.DFA170(
            self, 170,
            eot = self.DFA170_eot,
            eof = self.DFA170_eof,
            min = self.DFA170_min,
            max = self.DFA170_max,
            accept = self.DFA170_accept,
            special = self.DFA170_special,
            transition = self.DFA170_transition
            )
        self.dfa183 = self.DFA183(
            self, 183,
            eot = self.DFA183_eot,
            eof = self.DFA183_eof,
            min = self.DFA183_min,
            max = self.DFA183_max,
            accept = self.DFA183_accept,
            special = self.DFA183_special,
            transition = self.DFA183_transition
            )
        self.dfa188 = self.DFA188(
            self, 188,
            eot = self.DFA188_eot,
            eof = self.DFA188_eof,
            min = self.DFA188_min,
            max = self.DFA188_max,
            accept = self.DFA188_accept,
            special = self.DFA188_special,
            transition = self.DFA188_transition
            )
        self.dfa191 = self.DFA191(
            self, 191,
            eot = self.DFA191_eot,
            eof = self.DFA191_eof,
            min = self.DFA191_min,
            max = self.DFA191_max,
            accept = self.DFA191_accept,
            special = self.DFA191_special,
            transition = self.DFA191_transition
            )
        self.dfa194 = self.DFA194(
            self, 194,
            eot = self.DFA194_eot,
            eof = self.DFA194_eof,
            min = self.DFA194_min,
            max = self.DFA194_max,
            accept = self.DFA194_accept,
            special = self.DFA194_special,
            transition = self.DFA194_transition
            )
        self.dfa197 = self.DFA197(
            self, 197,
            eot = self.DFA197_eot,
            eof = self.DFA197_eof,
            min = self.DFA197_min,
            max = self.DFA197_max,
            accept = self.DFA197_accept,
            special = self.DFA197_special,
            transition = self.DFA197_transition
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
        self.dfa203 = self.DFA203(
            self, 203,
            eot = self.DFA203_eot,
            eof = self.DFA203_eof,
            min = self.DFA203_min,
            max = self.DFA203_max,
            accept = self.DFA203_accept,
            special = self.DFA203_special,
            transition = self.DFA203_transition
            )
        self.dfa206 = self.DFA206(
            self, 206,
            eot = self.DFA206_eot,
            eof = self.DFA206_eof,
            min = self.DFA206_min,
            max = self.DFA206_max,
            accept = self.DFA206_accept,
            special = self.DFA206_special,
            transition = self.DFA206_transition
            )
        self.dfa209 = self.DFA209(
            self, 209,
            eot = self.DFA209_eot,
            eof = self.DFA209_eof,
            min = self.DFA209_min,
            max = self.DFA209_max,
            accept = self.DFA209_accept,
            special = self.DFA209_special,
            transition = self.DFA209_transition
            )
        self.dfa212 = self.DFA212(
            self, 212,
            eot = self.DFA212_eot,
            eof = self.DFA212_eof,
            min = self.DFA212_min,
            max = self.DFA212_max,
            accept = self.DFA212_accept,
            special = self.DFA212_special,
            transition = self.DFA212_transition
            )
        self.dfa215 = self.DFA215(
            self, 215,
            eot = self.DFA215_eot,
            eof = self.DFA215_eof,
            min = self.DFA215_min,
            max = self.DFA215_max,
            accept = self.DFA215_accept,
            special = self.DFA215_special,
            transition = self.DFA215_transition
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
        self.dfa221 = self.DFA221(
            self, 221,
            eot = self.DFA221_eot,
            eof = self.DFA221_eof,
            min = self.DFA221_min,
            max = self.DFA221_max,
            accept = self.DFA221_accept,
            special = self.DFA221_special,
            transition = self.DFA221_transition
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
        self.dfa233 = self.DFA233(
            self, 233,
            eot = self.DFA233_eot,
            eof = self.DFA233_eof,
            min = self.DFA233_min,
            max = self.DFA233_max,
            accept = self.DFA233_accept,
            special = self.DFA233_special,
            transition = self.DFA233_transition
            )
        self.dfa246 = self.DFA246(
            self, 246,
            eot = self.DFA246_eot,
            eof = self.DFA246_eof,
            min = self.DFA246_min,
            max = self.DFA246_max,
            accept = self.DFA246_accept,
            special = self.DFA246_special,
            transition = self.DFA246_transition
            )
        self.dfa250 = self.DFA250(
            self, 250,
            eot = self.DFA250_eot,
            eof = self.DFA250_eof,
            min = self.DFA250_min,
            max = self.DFA250_max,
            accept = self.DFA250_accept,
            special = self.DFA250_special,
            transition = self.DFA250_transition
            )
        self.dfa249 = self.DFA249(
            self, 249,
            eot = self.DFA249_eot,
            eof = self.DFA249_eof,
            min = self.DFA249_min,
            max = self.DFA249_max,
            accept = self.DFA249_accept,
            special = self.DFA249_special,
            transition = self.DFA249_transition
            )
        self.dfa258 = self.DFA258(
            self, 258,
            eot = self.DFA258_eot,
            eof = self.DFA258_eof,
            min = self.DFA258_min,
            max = self.DFA258_max,
            accept = self.DFA258_accept,
            special = self.DFA258_special,
            transition = self.DFA258_transition
            )
        self.dfa272 = self.DFA272(
            self, 272,
            eot = self.DFA272_eot,
            eof = self.DFA272_eof,
            min = self.DFA272_min,
            max = self.DFA272_max,
            accept = self.DFA272_accept,
            special = self.DFA272_special,
            transition = self.DFA272_transition
            )
        self.dfa295 = self.DFA295(
            self, 295,
            eot = self.DFA295_eot,
            eof = self.DFA295_eof,
            min = self.DFA295_min,
            max = self.DFA295_max,
            accept = self.DFA295_accept,
            special = self.DFA295_special,
            transition = self.DFA295_transition
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

                elif ((LT <= LA5_0 <= RegularExpressionHacks) or LA5_0 == 60 or LA5_0 == 62 or LA5_0 == 64 or LA5_0 == 66 or LA5_0 == 69 or (72 <= LA5_0 <= 80) or (82 <= LA5_0 <= 85) or (87 <= LA5_0 <= 90) or (92 <= LA5_0 <= 93) or LA5_0 == 96 or LA5_0 == 98 or LA5_0 == 128 or (130 <= LA5_0 <= 142)) :
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
                # elements: formalParameterList, identifier, statementBlock
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) );
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
        identifier57 = None

        formalParameterList59 = None

        statementBlock61 = None

        formalParameterList63 = None

        statementBlock65 = None


        func_tree = None
        string_literal55_tree = None
        LT56_tree = None
        LT58_tree = None
        LT60_tree = None
        LT62_tree = None
        LT64_tree = None
        stream_68 = RewriteRuleTokenStream(self.adaptor, "token 68")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | func= 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS[$func] formalParameterList statementBlock ) )
                alt26 = 2
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
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
                    # elements: identifier, statementBlock, formalParameterList
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





                elif alt26 == 2:
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
                    # elements: statementBlock, formalParameterList
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:134:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' -> ^( FUNCARGS ( identifier )* ) ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal66 = None
        LT67 = None
        LT69 = None
        char_literal70 = None
        LT71 = None
        LT73 = None
        char_literal74 = None
        identifier68 = None

        identifier72 = None


        char_literal66_tree = None
        LT67_tree = None
        LT69_tree = None
        char_literal70_tree = None
        LT71_tree = None
        LT73_tree = None
        char_literal74_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self.adaptor, "token 71")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' -> ^( FUNCARGS ( identifier )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                char_literal66 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_formalParameterList609)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal66)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt31 = 2
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:9: ( LT )*
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == LT) :
                            alt27 = 1


                        if alt27 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT67 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList612)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT67)


                        else:
                            break #loop27


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList615)
                    identifier68 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier68.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:24: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop30
                        alt30 = 2
                        alt30 = self.dfa30.predict(self.input)
                        if alt30 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:25: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:25: ( LT )*
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == LT) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT69 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList618)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT69)


                                else:
                                    break #loop28


                            char_literal70 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_formalParameterList621)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal70)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:33: ( LT )*
                            while True: #loop29
                                alt29 = 2
                                LA29_0 = self.input.LA(1)

                                if (LA29_0 == LT) :
                                    alt29 = 1


                                if alt29 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT71 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList623)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT71)


                                else:
                                    break #loop29


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList626)
                            identifier72 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_identifier.add(identifier72.tree)


                        else:
                            break #loop30





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:52: ( LT )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == LT) :
                        alt32 = 1


                    if alt32 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT73 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList632)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT73)


                    else:
                        break #loop32


                char_literal74 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_formalParameterList635)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_71.add(char_literal74)
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
                    # 136:3: -> ^( FUNCARGS ( identifier )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:6: ^( FUNCARGS ( identifier )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNCARGS, "FUNCARGS"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:17: ( identifier )*
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        statementBlock75 = None

        variableStatement76 = None

        emptyStatement77 = None

        expressionStatement78 = None

        ifStatement79 = None

        iterationStatement80 = None

        continueStatement81 = None

        breakStatement82 = None

        returnStatement83 = None

        withStatement84 = None

        labelledStatement85 = None

        switchStatement86 = None

        throwStatement87 = None

        tryStatement88 = None

        defaultXmlNamespaceStatement89 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement )
                alt33 = 15
                LA33 = self.input.LA(1)
                if LA33 == 66:
                    LA33_1 = self.input.LA(2)

                    if (self.synpred38()) :
                        alt33 = 1
                    elif (self.synpred41()) :
                        alt33 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("140:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 1, self.input)

                        raise nvae

                elif LA33 == 77 or LA33 == 78 or LA33 == 79:
                    alt33 = 2
                elif LA33 == 75:
                    alt33 = 3
                elif LA33 == LT or LA33 == StringLiteral or LA33 == XMLComment or LA33 == NumericLiteral or LA33 == RegularExpressionHacks or LA33 == 60 or LA33 == 62 or LA33 == 64 or LA33 == 68 or LA33 == 69 or LA33 == 96 or LA33 == 98 or LA33 == 128 or LA33 == 130 or LA33 == 131 or LA33 == 132 or LA33 == 133 or LA33 == 134 or LA33 == 135 or LA33 == 136 or LA33 == 137 or LA33 == 140 or LA33 == 141 or LA33 == 142:
                    alt33 = 4
                elif LA33 == 72:
                    LA33_10 = self.input.LA(2)

                    if (self.synpred41()) :
                        alt33 = 4
                    elif (self.synpred48()) :
                        alt33 = 11
                    elif (True) :
                        alt33 = 15
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("140:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 10, self.input)

                        raise nvae

                elif LA33 == 80:
                    alt33 = 5
                elif LA33 == 82 or LA33 == 83 or LA33 == 84:
                    alt33 = 6
                elif LA33 == 87:
                    alt33 = 7
                elif LA33 == 88:
                    alt33 = 8
                elif LA33 == 76:
                    alt33 = 9
                elif LA33 == 89:
                    alt33 = 10
                elif LA33 == 90:
                    alt33 = 12
                elif LA33 == 92:
                    alt33 = 13
                elif LA33 == 93:
                    alt33 = 14
                elif LA33 == Identifier or LA33 == 73 or LA33 == 74 or LA33 == 85 or LA33 == 138 or LA33 == 139:
                    LA33_34 = self.input.LA(2)

                    if (self.synpred41()) :
                        alt33 = 4
                    elif (self.synpred48()) :
                        alt33 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("140:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 34, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("140:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement658)
                    statementBlock75 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock75.tree)


                elif alt33 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement663)
                    variableStatement76 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement76.tree)


                elif alt33 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement668)
                    emptyStatement77 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement77.tree)


                elif alt33 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement673)
                    expressionStatement78 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement78.tree)


                elif alt33 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement678)
                    ifStatement79 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement79.tree)


                elif alt33 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement683)
                    iterationStatement80 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement80.tree)


                elif alt33 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:147:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement688)
                    continueStatement81 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement81.tree)


                elif alt33 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:148:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement693)
                    breakStatement82 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement82.tree)


                elif alt33 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement698)
                    returnStatement83 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement83.tree)


                elif alt33 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement703)
                    withStatement84 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement84.tree)


                elif alt33 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement708)
                    labelledStatement85 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement85.tree)


                elif alt33 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:152:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement713)
                    switchStatement86 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement86.tree)


                elif alt33 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement718)
                    throwStatement87 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement87.tree)


                elif alt33 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement723)
                    tryStatement88 = self.tryStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, tryStatement88.tree)


                elif alt33 == 15:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:4: defaultXmlNamespaceStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_defaultXmlNamespaceStatement_in_statement728)
                    defaultXmlNamespaceStatement89 = self.defaultXmlNamespaceStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultXmlNamespaceStatement89.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:1: defaultXmlNamespaceStatement : 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) ;
    def defaultXmlNamespaceStatement(self, ):

        retval = self.defaultXmlNamespaceStatement_return()
        retval.start = self.input.LT(1)
        defaultXmlNamespaceStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal90 = None
        string_literal91 = None
        string_literal92 = None
        LT93 = None
        char_literal94 = None
        LT95 = None
        LT97 = None
        char_literal98 = None
        identifier96 = None


        string_literal90_tree = None
        string_literal91_tree = None
        string_literal92_tree = None
        LT93_tree = None
        char_literal94_tree = None
        LT95_tree = None
        LT97_tree = None
        char_literal98_tree = None
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:2: ( 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:4: 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' )
                string_literal90 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_defaultXmlNamespaceStatement739)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_72.add(string_literal90)
                string_literal91 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_defaultXmlNamespaceStatement741)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_73.add(string_literal91)
                string_literal92 = self.input.LT(1)
                self.match(self.input, 74, self.FOLLOW_74_in_defaultXmlNamespaceStatement743)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_74.add(string_literal92)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:32: ( LT )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == LT) :
                        alt34 = 1


                    if alt34 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT93 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement745)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT93)


                    else:
                        break #loop34


                char_literal94 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_defaultXmlNamespaceStatement748)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal94)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:40: ( LT )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == LT) :
                        alt35 = 1


                    if alt35 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT95 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement750)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT95)


                    else:
                        break #loop35


                self.following.append(self.FOLLOW_identifier_in_defaultXmlNamespaceStatement753)
                identifier96 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier96.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:55: ( LT | ';' )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == LT) :
                    alt36 = 1
                elif (LA36_0 == 75) :
                    alt36 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("159:55: ( LT | ';' )", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:56: LT
                    LT97 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement756)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT97)


                elif alt36 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:61: ';'
                    char_literal98 = self.input.LT(1)
                    self.match(self.input, 75, self.FOLLOW_75_in_defaultXmlNamespaceStatement760)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_75.add(char_literal98)



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
                    # 160:3: -> ^( DEFAULTNS identifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:6: ^( DEFAULTNS identifier )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal99 = None
        LT100 = None
        LT102 = None
        char_literal103 = None
        char_literal104 = None
        string_literal105 = None
        char_literal107 = None
        statementList101 = None

        expression106 = None


        char_literal99_tree = None
        LT100_tree = None
        LT102_tree = None
        char_literal103_tree = None
        char_literal104_tree = None
        string_literal105_tree = None
        char_literal107_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == 66) :
                    LA41_1 = self.input.LA(2)

                    if (self.synpred58()) :
                        alt41 = 1
                    elif (True) :
                        alt41 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("163:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 41, 1, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("163:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                    root_0 = self.adaptor.nil()

                    char_literal99 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_statementBlock782)
                    if self.failed:
                        return retval

                    char_literal99_tree = self.adaptor.createWithPayload(char_literal99)
                    self.adaptor.addChild(root_0, char_literal99_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:10: ( LT )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LT) :
                            LA37_2 = self.input.LA(2)

                            if (self.synpred55()) :
                                alt37 = 1




                        if alt37 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT100 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock784)
                            if self.failed:
                                return retval


                        else:
                            break #loop37


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:13: ( statementList )?
                    alt38 = 2
                    alt38 = self.dfa38.predict(self.input)
                    if alt38 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                        self.following.append(self.FOLLOW_statementList_in_statementBlock788)
                        statementList101 = self.statementList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statementList101.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:30: ( LT )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == LT) :
                            alt39 = 1


                        if alt39 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT102 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock791)
                            if self.failed:
                                return retval


                        else:
                            break #loop39


                    char_literal103 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_statementBlock795)
                    if self.failed:
                        return retval

                    char_literal103_tree = self.adaptor.createWithPayload(char_literal103)
                    self.adaptor.addChild(root_0, char_literal103_tree)



                elif alt41 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:4: '{' ( 'return' )? expression '}'
                    root_0 = self.adaptor.nil()

                    char_literal104 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_statementBlock800)
                    if self.failed:
                        return retval

                    char_literal104_tree = self.adaptor.createWithPayload(char_literal104)
                    self.adaptor.addChild(root_0, char_literal104_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:8: ( 'return' )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 76) :
                        alt40 = 1
                    if alt40 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'return'
                        string_literal105 = self.input.LT(1)
                        self.match(self.input, 76, self.FOLLOW_76_in_statementBlock802)
                        if self.failed:
                            return retval

                        string_literal105_tree = self.adaptor.createWithPayload(string_literal105)
                        self.adaptor.addChild(root_0, string_literal105_tree)




                    self.following.append(self.FOLLOW_expression_in_statementBlock805)
                    expression106 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression106.tree)
                    char_literal107 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_statementBlock807)
                    if self.failed:
                        return retval

                    char_literal107_tree = self.adaptor.createWithPayload(char_literal107)
                    self.adaptor.addChild(root_0, char_literal107_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT109 = None
        statement108 = None

        statement110 = None


        LT109_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList820)
                statement108 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement108.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:14: ( ( LT )* statement )*
                while True: #loop43
                    alt43 = 2
                    LA43 = self.input.LA(1)
                    if LA43 == LT:
                        LA43_1 = self.input.LA(2)

                        if (self.synpred61()) :
                            alt43 = 1


                    elif LA43 == 72:
                        LA43_3 = self.input.LA(2)

                        if (self.synpred61()) :
                            alt43 = 1


                    elif LA43 == StringLiteral or LA43 == XMLComment or LA43 == NumericLiteral or LA43 == Identifier or LA43 == RegularExpressionHacks or LA43 == 60 or LA43 == 62 or LA43 == 64 or LA43 == 66 or LA43 == 68 or LA43 == 69 or LA43 == 73 or LA43 == 74 or LA43 == 75 or LA43 == 76 or LA43 == 77 or LA43 == 78 or LA43 == 79 or LA43 == 80 or LA43 == 82 or LA43 == 83 or LA43 == 84 or LA43 == 85 or LA43 == 87 or LA43 == 88 or LA43 == 89 or LA43 == 90 or LA43 == 92 or LA43 == 93 or LA43 == 96 or LA43 == 98 or LA43 == 128 or LA43 == 130 or LA43 == 131 or LA43 == 132 or LA43 == 133 or LA43 == 134 or LA43 == 135 or LA43 == 136 or LA43 == 137 or LA43 == 138 or LA43 == 139 or LA43 == 140 or LA43 == 141 or LA43 == 142:
                        alt43 = 1

                    if alt43 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:17: ( LT )*
                        while True: #loop42
                            alt42 = 2
                            LA42_0 = self.input.LA(1)

                            if (LA42_0 == LT) :
                                LA42_2 = self.input.LA(2)

                                if (self.synpred60()) :
                                    alt42 = 1




                            if alt42 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT109 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList823)
                                if self.failed:
                                    return retval


                            else:
                                break #loop42


                        self.following.append(self.FOLLOW_statement_in_statementList827)
                        statement110 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement110.tree)


                    else:
                        break #loop43





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:1: variableStatement : (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        mod = None
        LT111 = None
        LT113 = None
        char_literal114 = None
        variableDeclarationList112 = None


        mod_tree = None
        LT111_tree = None
        LT113_tree = None
        char_literal114_tree = None
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:2: ( (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:4: (mod= 'var' | mod= 'const' | mod= 'let' ) ( LT )* variableDeclarationList ( LT | ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:4: (mod= 'var' | mod= 'const' | mod= 'let' )
                alt44 = 3
                LA44 = self.input.LA(1)
                if LA44 == 77:
                    alt44 = 1
                elif LA44 == 78:
                    alt44 = 2
                elif LA44 == 79:
                    alt44 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("173:4: (mod= 'var' | mod= 'const' | mod= 'let' )", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:5: mod= 'var'
                    mod = self.input.LT(1)
                    self.match(self.input, 77, self.FOLLOW_77_in_variableStatement843)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_77.add(mod)


                elif alt44 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:15: mod= 'const'
                    mod = self.input.LT(1)
                    self.match(self.input, 78, self.FOLLOW_78_in_variableStatement847)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_78.add(mod)


                elif alt44 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:27: mod= 'let'
                    mod = self.input.LT(1)
                    self.match(self.input, 79, self.FOLLOW_79_in_variableStatement851)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_79.add(mod)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:38: ( LT )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT111 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement854)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT111)


                    else:
                        break #loop45


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement857)
                variableDeclarationList112 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_variableDeclarationList.add(variableDeclarationList112.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:66: ( LT | ';' )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == LT) :
                    alt46 = 1
                elif (LA46_0 == 75) :
                    alt46 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("173:66: ( LT | ';' )", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:67: LT
                    LT113 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement860)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT113)


                elif alt46 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:72: ';'
                    char_literal114 = self.input.LT(1)
                    self.match(self.input, 75, self.FOLLOW_75_in_variableStatement864)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_75.add(char_literal114)



                # AST Rewrite
                # elements: mod, variableDeclarationList
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
                    # 174:3: -> ^( VARDEFS $mod variableDeclarationList )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:6: ^( VARDEFS $mod variableDeclarationList )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:177:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT116 = None
        char_literal117 = None
        LT118 = None
        variableDeclaration115 = None

        variableDeclaration119 = None


        LT116_tree = None
        char_literal117_tree = None
        LT118_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList889)
                variableDeclaration115 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration115.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop49
                    alt49 = 2
                    alt49 = self.dfa49.predict(self.input)
                    if alt49 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:27: ( LT )*
                        while True: #loop47
                            alt47 = 2
                            LA47_0 = self.input.LA(1)

                            if (LA47_0 == LT) :
                                alt47 = 1


                            if alt47 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT116 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList892)
                                if self.failed:
                                    return retval


                            else:
                                break #loop47


                        char_literal117 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationList896)
                        if self.failed:
                            return retval

                        char_literal117_tree = self.adaptor.createWithPayload(char_literal117)
                        self.adaptor.addChild(root_0, char_literal117_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:36: ( LT )*
                        while True: #loop48
                            alt48 = 2
                            LA48_0 = self.input.LA(1)

                            if (LA48_0 == LT) :
                                alt48 = 1


                            if alt48 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT118 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList898)
                                if self.failed:
                                    return retval


                            else:
                                break #loop48


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList902)
                        variableDeclaration119 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration119.tree)


                    else:
                        break #loop49





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT121 = None
        char_literal122 = None
        LT123 = None
        variableDeclarationNoIn120 = None

        variableDeclarationNoIn124 = None


        LT121_tree = None
        char_literal122_tree = None
        LT123_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn916)
                variableDeclarationNoIn120 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn120.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop52
                    alt52 = 2
                    alt52 = self.dfa52.predict(self.input)
                    if alt52 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:31: ( LT )*
                        while True: #loop50
                            alt50 = 2
                            LA50_0 = self.input.LA(1)

                            if (LA50_0 == LT) :
                                alt50 = 1


                            if alt50 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT121 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn919)
                                if self.failed:
                                    return retval


                            else:
                                break #loop50


                        char_literal122 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_variableDeclarationListNoIn923)
                        if self.failed:
                            return retval

                        char_literal122_tree = self.adaptor.createWithPayload(char_literal122)
                        self.adaptor.addChild(root_0, char_literal122_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:40: ( LT )*
                        while True: #loop51
                            alt51 = 2
                            LA51_0 = self.input.LA(1)

                            if (LA51_0 == LT) :
                                alt51 = 1


                            if alt51 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT123 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn925)
                                if self.failed:
                                    return retval


                            else:
                                break #loop51


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn929)
                        variableDeclarationNoIn124 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn124.tree)


                    else:
                        break #loop52





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:1: variableDeclaration : identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT126 = None
        identifier125 = None

        initialiser127 = None


        LT126_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiser = RewriteRuleSubtreeStream(self.adaptor, "rule initialiser")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:2: ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:4: identifier ( ( LT )* initialiser )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclaration943)
                identifier125 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier125.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:15: ( ( LT )* initialiser )?
                alt54 = 2
                alt54 = self.dfa54.predict(self.input)
                if alt54 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:16: ( LT )* initialiser
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:16: ( LT )*
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == LT) :
                            alt53 = 1


                        if alt53 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT126 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration946)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT126)


                        else:
                            break #loop53


                    self.following.append(self.FOLLOW_initialiser_in_variableDeclaration949)
                    initialiser127 = self.initialiser()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiser.add(initialiser127.tree)



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
                    # 187:3: -> ^( VARDEF identifier ( initialiser )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:6: ^( VARDEF identifier ( initialiser )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:26: ( initialiser )?
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:1: variableDeclarationNoIn : identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT129 = None
        identifier128 = None

        initialiserNoIn130 = None


        LT129_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiserNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule initialiserNoIn")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:2: ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:4: identifier ( ( LT )* initialiserNoIn )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn976)
                identifier128 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier128.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:15: ( ( LT )* initialiserNoIn )?
                alt56 = 2
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:16: ( LT )* initialiserNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:16: ( LT )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == LT) :
                            alt55 = 1


                        if alt55 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT129 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn979)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT129)


                        else:
                            break #loop55


                    self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn982)
                    initialiserNoIn130 = self.initialiserNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiserNoIn.add(initialiserNoIn130.tree)



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
                    # 192:3: -> ^( VARDEF identifier ( initialiserNoIn )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:6: ^( VARDEF identifier ( initialiserNoIn )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:26: ( initialiserNoIn )?
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:1: initialiser : '=' ( LT )* assignmentExpression -> assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal131 = None
        LT132 = None
        assignmentExpression133 = None


        char_literal131_tree = None
        LT132_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:2: ( '=' ( LT )* assignmentExpression -> assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:4: '=' ( LT )* assignmentExpression
                char_literal131 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_initialiser1009)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal131)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:8: ( LT )*
                while True: #loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == LT) :
                        LA57_2 = self.input.LA(2)

                        if (self.synpred76()) :
                            alt57 = 1




                    if alt57 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT132 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser1011)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT132)


                    else:
                        break #loop57


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser1014)
                assignmentExpression133 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression133.tree)
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
                    # 197:3: -> assignmentExpression
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:200:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal134 = None
        LT135 = None
        assignmentExpressionNoIn136 = None


        char_literal134_tree = None
        LT135_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:2: ( '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:4: '=' ( LT )* assignmentExpressionNoIn
                char_literal134 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_initialiserNoIn1032)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_65.add(char_literal134)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:8: ( LT )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == LT) :
                        LA58_2 = self.input.LA(2)

                        if (self.synpred77()) :
                            alt58 = 1




                    if alt58 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT135 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn1034)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT135)


                    else:
                        break #loop58


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn1037)
                assignmentExpressionNoIn136 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn136.tree)
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
                    # 202:3: -> assignmentExpressionNoIn
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:205:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal137 = None

        char_literal137_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:4: ';'
                root_0 = self.adaptor.nil()

                char_literal137 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_emptyStatement1055)
                if self.failed:
                    return retval

                char_literal137_tree = self.adaptor.createWithPayload(char_literal137)
                self.adaptor.addChild(root_0, char_literal137_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:209:1: expressionStatement : expression ( LT | ';' ) ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        set139 = None
        expression138 = None


        set139_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:210:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:210:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement1067)
                expression138 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression138.tree)
                set139 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_expressionStatement1069
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:213:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal140 = None
        LT141 = None
        char_literal142 = None
        LT143 = None
        LT145 = None
        char_literal146 = None
        LT147 = None
        LT149 = None
        string_literal150 = None
        LT151 = None
        expression144 = None

        statement148 = None

        statement152 = None


        string_literal140_tree = None
        LT141_tree = None
        char_literal142_tree = None
        LT143_tree = None
        LT145_tree = None
        char_literal146_tree = None
        LT147_tree = None
        LT149_tree = None
        string_literal150_tree = None
        LT151_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal140 = self.input.LT(1)
                self.match(self.input, 80, self.FOLLOW_80_in_ifStatement1088)
                if self.failed:
                    return retval

                string_literal140_tree = self.adaptor.createWithPayload(string_literal140)
                self.adaptor.addChild(root_0, string_literal140_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:11: ( LT )*
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == LT) :
                        alt59 = 1


                    if alt59 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT141 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1090)
                        if self.failed:
                            return retval


                    else:
                        break #loop59


                char_literal142 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_ifStatement1094)
                if self.failed:
                    return retval

                char_literal142_tree = self.adaptor.createWithPayload(char_literal142)
                self.adaptor.addChild(root_0, char_literal142_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:20: ( LT )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == LT) :
                        LA60_2 = self.input.LA(2)

                        if (self.synpred80()) :
                            alt60 = 1




                    if alt60 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT143 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1096)
                        if self.failed:
                            return retval


                    else:
                        break #loop60


                self.following.append(self.FOLLOW_expression_in_ifStatement1100)
                expression144 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression144.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:36: ( LT )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == LT) :
                        alt61 = 1


                    if alt61 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT145 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1102)
                        if self.failed:
                            return retval


                    else:
                        break #loop61


                char_literal146 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_ifStatement1106)
                if self.failed:
                    return retval

                char_literal146_tree = self.adaptor.createWithPayload(char_literal146)
                self.adaptor.addChild(root_0, char_literal146_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:45: ( LT )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == LT) :
                        LA62_2 = self.input.LA(2)

                        if (self.synpred82()) :
                            alt62 = 1




                    if alt62 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT147 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1108)
                        if self.failed:
                            return retval


                    else:
                        break #loop62


                self.following.append(self.FOLLOW_statement_in_ifStatement1112)
                statement148 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement148.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:58: ( ( LT )* 'else' ( LT )* statement )?
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == LT) :
                    LA65_1 = self.input.LA(2)

                    if (self.synpred85()) :
                        alt65 = 1
                elif (LA65_0 == 81) :
                    LA65_2 = self.input.LA(2)

                    if (self.synpred85()) :
                        alt65 = 1
                if alt65 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:61: ( LT )*
                    while True: #loop63
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if (LA63_0 == LT) :
                            alt63 = 1


                        if alt63 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT149 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1115)
                            if self.failed:
                                return retval


                        else:
                            break #loop63


                    string_literal150 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_ifStatement1119)
                    if self.failed:
                        return retval

                    string_literal150_tree = self.adaptor.createWithPayload(string_literal150)
                    self.adaptor.addChild(root_0, string_literal150_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:73: ( LT )*
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == LT) :
                            LA64_2 = self.input.LA(2)

                            if (self.synpred84()) :
                                alt64 = 1




                        if alt64 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT151 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1121)
                            if self.failed:
                                return retval


                        else:
                            break #loop64


                    self.following.append(self.FOLLOW_statement_in_ifStatement1125)
                    statement152 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement152.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement153 = None

        whileStatement154 = None

        forStatement155 = None

        forInStatement156 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:218:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt66 = 4
                LA66 = self.input.LA(1)
                if LA66 == 82:
                    alt66 = 1
                elif LA66 == 83:
                    alt66 = 2
                elif LA66 == 84:
                    LA66_3 = self.input.LA(2)

                    if (self.synpred88()) :
                        alt66 = 3
                    elif (True) :
                        alt66 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("217:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 66, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("217:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 66, 0, self.input)

                    raise nvae

                if alt66 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:218:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement1139)
                    doWhileStatement153 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement153.tree)


                elif alt66 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement1144)
                    whileStatement154 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement154.tree)


                elif alt66 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement1149)
                    forStatement155 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement155.tree)


                elif alt66 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement1154)
                    forInStatement156 = self.forInStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forInStatement156.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal157 = None
        LT158 = None
        LT160 = None
        string_literal161 = None
        LT162 = None
        char_literal163 = None
        char_literal165 = None
        set166 = None
        statement159 = None

        expression164 = None


        string_literal157_tree = None
        LT158_tree = None
        LT160_tree = None
        string_literal161_tree = None
        LT162_tree = None
        char_literal163_tree = None
        char_literal165_tree = None
        set166_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal157 = self.input.LT(1)
                self.match(self.input, 82, self.FOLLOW_82_in_doWhileStatement1166)
                if self.failed:
                    return retval

                string_literal157_tree = self.adaptor.createWithPayload(string_literal157)
                self.adaptor.addChild(root_0, string_literal157_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:11: ( LT )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == LT) :
                        LA67_2 = self.input.LA(2)

                        if (self.synpred89()) :
                            alt67 = 1




                    if alt67 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT158 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1168)
                        if self.failed:
                            return retval


                    else:
                        break #loop67


                self.following.append(self.FOLLOW_statement_in_doWhileStatement1172)
                statement159 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement159.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:26: ( LT )*
                while True: #loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == LT) :
                        alt68 = 1


                    if alt68 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT160 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1174)
                        if self.failed:
                            return retval


                    else:
                        break #loop68


                string_literal161 = self.input.LT(1)
                self.match(self.input, 83, self.FOLLOW_83_in_doWhileStatement1178)
                if self.failed:
                    return retval

                string_literal161_tree = self.adaptor.createWithPayload(string_literal161)
                self.adaptor.addChild(root_0, string_literal161_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:39: ( LT )*
                while True: #loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == LT) :
                        alt69 = 1


                    if alt69 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT162 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1180)
                        if self.failed:
                            return retval


                    else:
                        break #loop69


                char_literal163 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_doWhileStatement1184)
                if self.failed:
                    return retval

                char_literal163_tree = self.adaptor.createWithPayload(char_literal163)
                self.adaptor.addChild(root_0, char_literal163_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement1186)
                expression164 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression164.tree)
                char_literal165 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_doWhileStatement1188)
                if self.failed:
                    return retval

                char_literal165_tree = self.adaptor.createWithPayload(char_literal165)
                self.adaptor.addChild(root_0, char_literal165_tree)

                set166 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement1190
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:228:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal167 = None
        LT168 = None
        char_literal169 = None
        LT170 = None
        LT172 = None
        char_literal173 = None
        LT174 = None
        expression171 = None

        statement175 = None


        string_literal167_tree = None
        LT168_tree = None
        char_literal169_tree = None
        LT170_tree = None
        LT172_tree = None
        char_literal173_tree = None
        LT174_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal167 = self.input.LT(1)
                self.match(self.input, 83, self.FOLLOW_83_in_whileStatement1209)
                if self.failed:
                    return retval

                string_literal167_tree = self.adaptor.createWithPayload(string_literal167)
                self.adaptor.addChild(root_0, string_literal167_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:14: ( LT )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == LT) :
                        alt70 = 1


                    if alt70 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT168 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1211)
                        if self.failed:
                            return retval


                    else:
                        break #loop70


                char_literal169 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_whileStatement1215)
                if self.failed:
                    return retval

                char_literal169_tree = self.adaptor.createWithPayload(char_literal169)
                self.adaptor.addChild(root_0, char_literal169_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:23: ( LT )*
                while True: #loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == LT) :
                        LA71_2 = self.input.LA(2)

                        if (self.synpred94()) :
                            alt71 = 1




                    if alt71 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT170 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1217)
                        if self.failed:
                            return retval


                    else:
                        break #loop71


                self.following.append(self.FOLLOW_expression_in_whileStatement1221)
                expression171 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression171.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:39: ( LT )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == LT) :
                        alt72 = 1


                    if alt72 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT172 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1223)
                        if self.failed:
                            return retval


                    else:
                        break #loop72


                char_literal173 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_whileStatement1227)
                if self.failed:
                    return retval

                char_literal173_tree = self.adaptor.createWithPayload(char_literal173)
                self.adaptor.addChild(root_0, char_literal173_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:48: ( LT )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == LT) :
                        LA73_2 = self.input.LA(2)

                        if (self.synpred96()) :
                            alt73 = 1




                    if alt73 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT174 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1229)
                        if self.failed:
                            return retval


                    else:
                        break #loop73


                self.following.append(self.FOLLOW_statement_in_whileStatement1233)
                statement175 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement175.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal176 = None
        LT177 = None
        char_literal178 = None
        LT179 = None
        LT181 = None
        char_literal182 = None
        LT183 = None
        LT185 = None
        char_literal186 = None
        LT187 = None
        LT189 = None
        char_literal190 = None
        LT191 = None
        forStatementInitialiserPart180 = None

        expression184 = None

        expression188 = None

        statement192 = None


        string_literal176_tree = None
        LT177_tree = None
        char_literal178_tree = None
        LT179_tree = None
        LT181_tree = None
        char_literal182_tree = None
        LT183_tree = None
        LT185_tree = None
        char_literal186_tree = None
        LT187_tree = None
        LT189_tree = None
        char_literal190_tree = None
        LT191_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal176 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_forStatement1245)
                if self.failed:
                    return retval

                string_literal176_tree = self.adaptor.createWithPayload(string_literal176)
                self.adaptor.addChild(root_0, string_literal176_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:12: ( LT )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == LT) :
                        alt74 = 1


                    if alt74 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT177 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1247)
                        if self.failed:
                            return retval


                    else:
                        break #loop74


                char_literal178 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_forStatement1251)
                if self.failed:
                    return retval

                char_literal178_tree = self.adaptor.createWithPayload(char_literal178)
                self.adaptor.addChild(root_0, char_literal178_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:19: ( ( LT )* forStatementInitialiserPart )?
                alt76 = 2
                alt76 = self.dfa76.predict(self.input)
                if alt76 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:22: ( LT )*
                    while True: #loop75
                        alt75 = 2
                        LA75_0 = self.input.LA(1)

                        if (LA75_0 == LT) :
                            LA75_2 = self.input.LA(2)

                            if (self.synpred98()) :
                                alt75 = 1




                        if alt75 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT179 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1254)
                            if self.failed:
                                return retval


                        else:
                            break #loop75


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement1258)
                    forStatementInitialiserPart180 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart180.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:57: ( LT )*
                while True: #loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == LT) :
                        alt77 = 1


                    if alt77 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT181 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1262)
                        if self.failed:
                            return retval


                    else:
                        break #loop77


                char_literal182 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_forStatement1266)
                if self.failed:
                    return retval

                char_literal182_tree = self.adaptor.createWithPayload(char_literal182)
                self.adaptor.addChild(root_0, char_literal182_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:64: ( ( LT )* expression )?
                alt79 = 2
                alt79 = self.dfa79.predict(self.input)
                if alt79 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:67: ( LT )*
                    while True: #loop78
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == LT) :
                            LA78_2 = self.input.LA(2)

                            if (self.synpred101()) :
                                alt78 = 1




                        if alt78 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT183 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1269)
                            if self.failed:
                                return retval


                        else:
                            break #loop78


                    self.following.append(self.FOLLOW_expression_in_forStatement1273)
                    expression184 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression184.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:85: ( LT )*
                while True: #loop80
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if (LA80_0 == LT) :
                        alt80 = 1


                    if alt80 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT185 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1277)
                        if self.failed:
                            return retval


                    else:
                        break #loop80


                char_literal186 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_forStatement1281)
                if self.failed:
                    return retval

                char_literal186_tree = self.adaptor.createWithPayload(char_literal186)
                self.adaptor.addChild(root_0, char_literal186_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:92: ( ( LT )* expression )?
                alt82 = 2
                alt82 = self.dfa82.predict(self.input)
                if alt82 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:95: ( LT )*
                    while True: #loop81
                        alt81 = 2
                        LA81_0 = self.input.LA(1)

                        if (LA81_0 == LT) :
                            LA81_2 = self.input.LA(2)

                            if (self.synpred104()) :
                                alt81 = 1




                        if alt81 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT187 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1284)
                            if self.failed:
                                return retval


                        else:
                            break #loop81


                    self.following.append(self.FOLLOW_expression_in_forStatement1288)
                    expression188 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression188.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:113: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        alt83 = 1


                    if alt83 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT189 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1292)
                        if self.failed:
                            return retval


                    else:
                        break #loop83


                char_literal190 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_forStatement1296)
                if self.failed:
                    return retval

                char_literal190_tree = self.adaptor.createWithPayload(char_literal190)
                self.adaptor.addChild(root_0, char_literal190_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:122: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        LA84_2 = self.input.LA(2)

                        if (self.synpred107()) :
                            alt84 = 1




                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT191 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1298)
                        if self.failed:
                            return retval


                    else:
                        break #loop84


                self.following.append(self.FOLLOW_statement_in_forStatement1302)
                statement192 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement192.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:1: forStatementInitialiserPart : ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        set194 = None
        LT195 = None
        expressionNoIn193 = None

        variableDeclarationListNoIn196 = None


        set194_tree = None
        LT195_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:237:2: ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn )
                alt86 = 2
                LA86_0 = self.input.LA(1)

                if ((LT <= LA86_0 <= RegularExpressionHacks) or LA86_0 == 60 or LA86_0 == 62 or LA86_0 == 64 or LA86_0 == 66 or (68 <= LA86_0 <= 69) or (72 <= LA86_0 <= 74) or LA86_0 == 85 or LA86_0 == 96 or LA86_0 == 98 or LA86_0 == 128 or (130 <= LA86_0 <= 142)) :
                    alt86 = 1
                elif (LA86_0 == 77 or LA86_0 == 79) :
                    alt86 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("236:1: forStatementInitialiserPart : ( expressionNoIn | ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn );", 86, 0, self.input)

                    raise nvae

                if alt86 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:237:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart1314)
                    expressionNoIn193 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn193.tree)


                elif alt86 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:4: ( 'var' | 'let' ) ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    set194 = self.input.LT(1)
                    if self.input.LA(1) == 77 or self.input.LA(1) == 79:
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set194))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_forStatementInitialiserPart1319
                            )
                        raise mse


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:20: ( LT )*
                    while True: #loop85
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == LT) :
                            alt85 = 1


                        if alt85 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT195 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart1325)
                            if self.failed:
                                return retval


                        else:
                            break #loop85


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1329)
                    variableDeclarationListNoIn196 = self.variableDeclarationListNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationListNoIn196.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:241:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal197 = None
        LT198 = None
        string_literal199 = None
        LT200 = None
        char_literal201 = None
        LT202 = None
        LT204 = None
        string_literal205 = None
        LT206 = None
        LT208 = None
        char_literal209 = None
        LT210 = None
        forInStatementInitialiserPart203 = None

        expression207 = None

        statement211 = None


        string_literal197_tree = None
        LT198_tree = None
        string_literal199_tree = None
        LT200_tree = None
        char_literal201_tree = None
        LT202_tree = None
        LT204_tree = None
        string_literal205_tree = None
        LT206_tree = None
        LT208_tree = None
        char_literal209_tree = None
        LT210_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal197 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_forInStatement1341)
                if self.failed:
                    return retval

                string_literal197_tree = self.adaptor.createWithPayload(string_literal197)
                self.adaptor.addChild(root_0, string_literal197_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:12: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        LA87_2 = self.input.LA(2)

                        if (self.synpred111()) :
                            alt87 = 1




                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT198 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1343)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:15: ( 'each' )?
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if (LA88_0 == 85) :
                    alt88 = 1
                if alt88 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal199 = self.input.LT(1)
                    self.match(self.input, 85, self.FOLLOW_85_in_forInStatement1347)
                    if self.failed:
                        return retval

                    string_literal199_tree = self.adaptor.createWithPayload(string_literal199)
                    self.adaptor.addChild(root_0, string_literal199_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:25: ( LT )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LT) :
                        alt89 = 1


                    if alt89 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT200 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1350)
                        if self.failed:
                            return retval


                    else:
                        break #loop89


                char_literal201 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_forInStatement1354)
                if self.failed:
                    return retval

                char_literal201_tree = self.adaptor.createWithPayload(char_literal201)
                self.adaptor.addChild(root_0, char_literal201_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:34: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        LA90_2 = self.input.LA(2)

                        if (self.synpred114()) :
                            alt90 = 1




                    if alt90 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT202 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1356)
                        if self.failed:
                            return retval


                    else:
                        break #loop90


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement1360)
                forInStatementInitialiserPart203 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart203.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:69: ( LT )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == LT) :
                        alt91 = 1


                    if alt91 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT204 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1362)
                        if self.failed:
                            return retval


                    else:
                        break #loop91


                string_literal205 = self.input.LT(1)
                self.match(self.input, 86, self.FOLLOW_86_in_forInStatement1366)
                if self.failed:
                    return retval

                string_literal205_tree = self.adaptor.createWithPayload(string_literal205)
                self.adaptor.addChild(root_0, string_literal205_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:79: ( LT )*
                while True: #loop92
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == LT) :
                        LA92_2 = self.input.LA(2)

                        if (self.synpred116()) :
                            alt92 = 1




                    if alt92 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT206 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1368)
                        if self.failed:
                            return retval


                    else:
                        break #loop92


                self.following.append(self.FOLLOW_expression_in_forInStatement1372)
                expression207 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression207.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:95: ( LT )*
                while True: #loop93
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == LT) :
                        alt93 = 1


                    if alt93 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT208 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1374)
                        if self.failed:
                            return retval


                    else:
                        break #loop93


                char_literal209 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_forInStatement1378)
                if self.failed:
                    return retval

                char_literal209_tree = self.adaptor.createWithPayload(char_literal209)
                self.adaptor.addChild(root_0, char_literal209_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:104: ( LT )*
                while True: #loop94
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == LT) :
                        LA94_2 = self.input.LA(2)

                        if (self.synpred118()) :
                            alt94 = 1




                    if alt94 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT210 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1380)
                        if self.failed:
                            return retval


                    else:
                        break #loop94


                self.following.append(self.FOLLOW_statement_in_forInStatement1384)
                statement211 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement211.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:1: forInStatementInitialiserPart : ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        set213 = None
        LT214 = None
        leftHandSideExpression212 = None

        variableDeclarationNoIn215 = None


        set213_tree = None
        LT214_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:2: ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn )
                alt96 = 2
                LA96_0 = self.input.LA(1)

                if ((LT <= LA96_0 <= RegularExpressionHacks) or LA96_0 == 60 or LA96_0 == 62 or LA96_0 == 66 or (68 <= LA96_0 <= 69) or (72 <= LA96_0 <= 74) or LA96_0 == 85 or LA96_0 == 96 or LA96_0 == 98 or (137 <= LA96_0 <= 142)) :
                    alt96 = 1
                elif (LA96_0 == 77 or LA96_0 == 79) :
                    alt96 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("245:1: forInStatementInitialiserPart : ( leftHandSideExpression | ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn );", 96, 0, self.input)

                    raise nvae

                if alt96 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1396)
                    leftHandSideExpression212 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression212.tree)


                elif alt96 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:247:4: ( 'var' | 'let' ) ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    set213 = self.input.LT(1)
                    if self.input.LA(1) == 77 or self.input.LA(1) == 79:
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set213))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_forInStatementInitialiserPart1401
                            )
                        raise mse


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:247:20: ( LT )*
                    while True: #loop95
                        alt95 = 2
                        LA95_0 = self.input.LA(1)

                        if (LA95_0 == LT) :
                            alt95 = 1


                        if alt95 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT214 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart1407)
                            if self.failed:
                                return retval


                        else:
                            break #loop95


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1411)
                    variableDeclarationNoIn215 = self.variableDeclarationNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationNoIn215.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal216 = None
        set218 = None
        identifier217 = None


        string_literal216_tree = None
        set218_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:251:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:251:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal216 = self.input.LT(1)
                self.match(self.input, 87, self.FOLLOW_87_in_continueStatement1422)
                if self.failed:
                    return retval

                string_literal216_tree = self.adaptor.createWithPayload(string_literal216)
                self.adaptor.addChild(root_0, string_literal216_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:251:15: ( identifier )?
                alt97 = 2
                LA97_0 = self.input.LA(1)

                if (LA97_0 == Identifier or (72 <= LA97_0 <= 74) or LA97_0 == 85 or (138 <= LA97_0 <= 139)) :
                    alt97 = 1
                if alt97 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement1424)
                    identifier217 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier217.tree)



                set218 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_continueStatement1427
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal219 = None
        set221 = None
        identifier220 = None


        string_literal219_tree = None
        set221_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal219 = self.input.LT(1)
                self.match(self.input, 88, self.FOLLOW_88_in_breakStatement1445)
                if self.failed:
                    return retval

                string_literal219_tree = self.adaptor.createWithPayload(string_literal219)
                self.adaptor.addChild(root_0, string_literal219_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:12: ( identifier )?
                alt98 = 2
                LA98_0 = self.input.LA(1)

                if (LA98_0 == Identifier or (72 <= LA98_0 <= 74) or LA98_0 == 85 or (138 <= LA98_0 <= 139)) :
                    alt98 = 1
                if alt98 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement1447)
                    identifier220 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier220.tree)



                set221 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_breakStatement1450
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal222 = None
        set224 = None
        expression223 = None


        string_literal222_tree = None
        set224_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal222 = self.input.LT(1)
                self.match(self.input, 76, self.FOLLOW_76_in_returnStatement1468)
                if self.failed:
                    return retval

                string_literal222_tree = self.adaptor.createWithPayload(string_literal222)
                self.adaptor.addChild(root_0, string_literal222_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:13: ( expression )?
                alt99 = 2
                LA99_0 = self.input.LA(1)

                if ((StringLiteral <= LA99_0 <= RegularExpressionHacks) or LA99_0 == 60 or LA99_0 == 62 or LA99_0 == 64 or LA99_0 == 66 or (68 <= LA99_0 <= 69) or (72 <= LA99_0 <= 74) or LA99_0 == 85 or LA99_0 == 96 or LA99_0 == 98 or LA99_0 == 128 or (130 <= LA99_0 <= 142)) :
                    alt99 = 1
                elif (LA99_0 == LT) :
                    LA99_2 = self.input.LA(2)

                    if (self.synpred126()) :
                        alt99 = 1
                if alt99 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement1470)
                    expression223 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression223.tree)



                set224 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_returnStatement1473
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal225 = None
        LT226 = None
        char_literal227 = None
        LT228 = None
        LT230 = None
        char_literal231 = None
        LT232 = None
        expression229 = None

        statement233 = None


        string_literal225_tree = None
        LT226_tree = None
        char_literal227_tree = None
        LT228_tree = None
        LT230_tree = None
        char_literal231_tree = None
        LT232_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal225 = self.input.LT(1)
                self.match(self.input, 89, self.FOLLOW_89_in_withStatement1492)
                if self.failed:
                    return retval

                string_literal225_tree = self.adaptor.createWithPayload(string_literal225)
                self.adaptor.addChild(root_0, string_literal225_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:13: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT226 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1494)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                char_literal227 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_withStatement1498)
                if self.failed:
                    return retval

                char_literal227_tree = self.adaptor.createWithPayload(char_literal227)
                self.adaptor.addChild(root_0, char_literal227_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:22: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        LA101_2 = self.input.LA(2)

                        if (self.synpred129()) :
                            alt101 = 1




                    if alt101 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT228 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1500)
                        if self.failed:
                            return retval


                    else:
                        break #loop101


                self.following.append(self.FOLLOW_expression_in_withStatement1504)
                expression229 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression229.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:38: ( LT )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == LT) :
                        alt102 = 1


                    if alt102 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT230 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1506)
                        if self.failed:
                            return retval


                    else:
                        break #loop102


                char_literal231 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_withStatement1510)
                if self.failed:
                    return retval

                char_literal231_tree = self.adaptor.createWithPayload(char_literal231)
                self.adaptor.addChild(root_0, char_literal231_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:47: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        LA103_2 = self.input.LA(2)

                        if (self.synpred131()) :
                            alt103 = 1




                    if alt103 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT232 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1512)
                        if self.failed:
                            return retval


                    else:
                        break #loop103


                self.following.append(self.FOLLOW_statement_in_withStatement1516)
                statement233 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement233.tree)



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

    class labelledStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start labelledStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        LT235 = None
        char_literal236 = None
        LT237 = None
        identifier234 = None

        statement238 = None


        LT235_tree = None
        char_literal236_tree = None
        LT237_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1527)
                identifier234 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier234.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:17: ( LT )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == LT) :
                        alt104 = 1


                    if alt104 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT235 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1529)
                        if self.failed:
                            return retval


                    else:
                        break #loop104


                char_literal236 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_labelledStatement1533)
                if self.failed:
                    return retval

                char_literal236_tree = self.adaptor.createWithPayload(char_literal236)
                self.adaptor.addChild(root_0, char_literal236_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:26: ( LT )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == LT) :
                        LA105_2 = self.input.LA(2)

                        if (self.synpred133()) :
                            alt105 = 1




                    if alt105 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT237 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1535)
                        if self.failed:
                            return retval


                    else:
                        break #loop105


                self.following.append(self.FOLLOW_statement_in_labelledStatement1539)
                statement238 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement238.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 42, labelledStatement_StartIndex)

            pass

        return retval

    # $ANTLR end labelledStatement

    class switchStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start switchStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal239 = None
        LT240 = None
        char_literal241 = None
        LT242 = None
        LT244 = None
        char_literal245 = None
        LT246 = None
        expression243 = None

        caseBlock247 = None


        string_literal239_tree = None
        LT240_tree = None
        char_literal241_tree = None
        LT242_tree = None
        LT244_tree = None
        char_literal245_tree = None
        LT246_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal239 = self.input.LT(1)
                self.match(self.input, 90, self.FOLLOW_90_in_switchStatement1551)
                if self.failed:
                    return retval

                string_literal239_tree = self.adaptor.createWithPayload(string_literal239)
                self.adaptor.addChild(root_0, string_literal239_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:15: ( LT )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == LT) :
                        alt106 = 1


                    if alt106 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT240 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1553)
                        if self.failed:
                            return retval


                    else:
                        break #loop106


                char_literal241 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_switchStatement1557)
                if self.failed:
                    return retval

                char_literal241_tree = self.adaptor.createWithPayload(char_literal241)
                self.adaptor.addChild(root_0, char_literal241_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:24: ( LT )*
                while True: #loop107
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if (LA107_0 == LT) :
                        LA107_2 = self.input.LA(2)

                        if (self.synpred135()) :
                            alt107 = 1




                    if alt107 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT242 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1559)
                        if self.failed:
                            return retval


                    else:
                        break #loop107


                self.following.append(self.FOLLOW_expression_in_switchStatement1563)
                expression243 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression243.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:40: ( LT )*
                while True: #loop108
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == LT) :
                        alt108 = 1


                    if alt108 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT244 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1565)
                        if self.failed:
                            return retval


                    else:
                        break #loop108


                char_literal245 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_switchStatement1569)
                if self.failed:
                    return retval

                char_literal245_tree = self.adaptor.createWithPayload(char_literal245)
                self.adaptor.addChild(root_0, char_literal245_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:49: ( LT )*
                while True: #loop109
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == LT) :
                        alt109 = 1


                    if alt109 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT246 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1571)
                        if self.failed:
                            return retval


                    else:
                        break #loop109


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1575)
                caseBlock247 = self.caseBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, caseBlock247.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 43, switchStatement_StartIndex)

            pass

        return retval

    # $ANTLR end switchStatement

    class caseBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal248 = None
        LT249 = None
        LT251 = None
        LT253 = None
        LT255 = None
        char_literal256 = None
        caseClause250 = None

        defaultClause252 = None

        caseClause254 = None


        char_literal248_tree = None
        LT249_tree = None
        LT251_tree = None
        LT253_tree = None
        LT255_tree = None
        char_literal256_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal248 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_caseBlock1587)
                if self.failed:
                    return retval

                char_literal248_tree = self.adaptor.createWithPayload(char_literal248)
                self.adaptor.addChild(root_0, char_literal248_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:8: ( ( LT )* caseClause )*
                while True: #loop111
                    alt111 = 2
                    alt111 = self.dfa111.predict(self.input)
                    if alt111 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:11: ( LT )*
                        while True: #loop110
                            alt110 = 2
                            LA110_0 = self.input.LA(1)

                            if (LA110_0 == LT) :
                                alt110 = 1


                            if alt110 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT249 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1590)
                                if self.failed:
                                    return retval


                            else:
                                break #loop110


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1594)
                        caseClause250 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause250.tree)


                    else:
                        break #loop111


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt115 = 2
                alt115 = self.dfa115.predict(self.input)
                if alt115 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:30: ( LT )*
                    while True: #loop112
                        alt112 = 2
                        LA112_0 = self.input.LA(1)

                        if (LA112_0 == LT) :
                            alt112 = 1


                        if alt112 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT251 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1599)
                            if self.failed:
                                return retval


                        else:
                            break #loop112


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1603)
                    defaultClause252 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause252.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:47: ( ( LT )* caseClause )*
                    while True: #loop114
                        alt114 = 2
                        alt114 = self.dfa114.predict(self.input)
                        if alt114 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:50: ( LT )*
                            while True: #loop113
                                alt113 = 2
                                LA113_0 = self.input.LA(1)

                                if (LA113_0 == LT) :
                                    alt113 = 1


                                if alt113 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT253 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1606)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop113


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1610)
                            caseClause254 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause254.tree)


                        else:
                            break #loop114





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:70: ( LT )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == LT) :
                        alt116 = 1


                    if alt116 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT255 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1616)
                        if self.failed:
                            return retval


                    else:
                        break #loop116


                char_literal256 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_caseBlock1620)
                if self.failed:
                    return retval

                char_literal256_tree = self.adaptor.createWithPayload(char_literal256)
                self.adaptor.addChild(root_0, char_literal256_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 44, caseBlock_StartIndex)

            pass

        return retval

    # $ANTLR end caseBlock

    class caseClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal257 = None
        LT258 = None
        LT260 = None
        char_literal261 = None
        LT262 = None
        expression259 = None

        statementList263 = None


        string_literal257_tree = None
        LT258_tree = None
        LT260_tree = None
        char_literal261_tree = None
        LT262_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal257 = self.input.LT(1)
                self.match(self.input, 91, self.FOLLOW_91_in_caseClause1631)
                if self.failed:
                    return retval

                string_literal257_tree = self.adaptor.createWithPayload(string_literal257)
                self.adaptor.addChild(root_0, string_literal257_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:13: ( LT )*
                while True: #loop117
                    alt117 = 2
                    LA117_0 = self.input.LA(1)

                    if (LA117_0 == LT) :
                        LA117_2 = self.input.LA(2)

                        if (self.synpred145()) :
                            alt117 = 1




                    if alt117 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT258 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1633)
                        if self.failed:
                            return retval


                    else:
                        break #loop117


                self.following.append(self.FOLLOW_expression_in_caseClause1637)
                expression259 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression259.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:29: ( LT )*
                while True: #loop118
                    alt118 = 2
                    LA118_0 = self.input.LA(1)

                    if (LA118_0 == LT) :
                        alt118 = 1


                    if alt118 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT260 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1639)
                        if self.failed:
                            return retval


                    else:
                        break #loop118


                char_literal261 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_caseClause1643)
                if self.failed:
                    return retval

                char_literal261_tree = self.adaptor.createWithPayload(char_literal261)
                self.adaptor.addChild(root_0, char_literal261_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:38: ( LT )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if (LA119_0 == LT) :
                        LA119_2 = self.input.LA(2)

                        if (self.synpred147()) :
                            alt119 = 1




                    if alt119 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT262 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1645)
                        if self.failed:
                            return retval


                    else:
                        break #loop119


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:41: ( statementList )?
                alt120 = 2
                LA120 = self.input.LA(1)
                if LA120 == StringLiteral or LA120 == XMLComment or LA120 == NumericLiteral or LA120 == Identifier or LA120 == RegularExpressionHacks or LA120 == 60 or LA120 == 62 or LA120 == 64 or LA120 == 66 or LA120 == 68 or LA120 == 69 or LA120 == 73 or LA120 == 74 or LA120 == 75 or LA120 == 76 or LA120 == 77 or LA120 == 78 or LA120 == 79 or LA120 == 80 or LA120 == 82 or LA120 == 83 or LA120 == 84 or LA120 == 85 or LA120 == 87 or LA120 == 88 or LA120 == 89 or LA120 == 90 or LA120 == 92 or LA120 == 93 or LA120 == 96 or LA120 == 98 or LA120 == 128 or LA120 == 130 or LA120 == 131 or LA120 == 132 or LA120 == 133 or LA120 == 134 or LA120 == 135 or LA120 == 136 or LA120 == 137 or LA120 == 138 or LA120 == 139 or LA120 == 140 or LA120 == 141 or LA120 == 142:
                    alt120 = 1
                elif LA120 == LT:
                    LA120_7 = self.input.LA(2)

                    if (self.synpred148()) :
                        alt120 = 1
                elif LA120 == 72:
                    LA120_10 = self.input.LA(2)

                    if (self.synpred148()) :
                        alt120 = 1
                if alt120 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1649)
                    statementList263 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList263.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 45, caseClause_StartIndex)

            pass

        return retval

    # $ANTLR end caseClause

    class defaultClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start defaultClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal264 = None
        LT265 = None
        char_literal266 = None
        LT267 = None
        statementList268 = None


        string_literal264_tree = None
        LT265_tree = None
        char_literal266_tree = None
        LT267_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal264 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_defaultClause1662)
                if self.failed:
                    return retval

                string_literal264_tree = self.adaptor.createWithPayload(string_literal264)
                self.adaptor.addChild(root_0, string_literal264_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:16: ( LT )*
                while True: #loop121
                    alt121 = 2
                    LA121_0 = self.input.LA(1)

                    if (LA121_0 == LT) :
                        alt121 = 1


                    if alt121 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT265 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1664)
                        if self.failed:
                            return retval


                    else:
                        break #loop121


                char_literal266 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_defaultClause1668)
                if self.failed:
                    return retval

                char_literal266_tree = self.adaptor.createWithPayload(char_literal266)
                self.adaptor.addChild(root_0, char_literal266_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:25: ( LT )*
                while True: #loop122
                    alt122 = 2
                    LA122_0 = self.input.LA(1)

                    if (LA122_0 == LT) :
                        LA122_2 = self.input.LA(2)

                        if (self.synpred150()) :
                            alt122 = 1




                    if alt122 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT267 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1670)
                        if self.failed:
                            return retval


                    else:
                        break #loop122


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:28: ( statementList )?
                alt123 = 2
                alt123 = self.dfa123.predict(self.input)
                if alt123 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1674)
                    statementList268 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList268.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 46, defaultClause_StartIndex)

            pass

        return retval

    # $ANTLR end defaultClause

    class throwStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start throwStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:1: throwStatement : 'throw' expression ( LT | ';' ) ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal269 = None
        set271 = None
        expression270 = None


        string_literal269_tree = None
        set271_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal269 = self.input.LT(1)
                self.match(self.input, 92, self.FOLLOW_92_in_throwStatement1687)
                if self.failed:
                    return retval

                string_literal269_tree = self.adaptor.createWithPayload(string_literal269)
                self.adaptor.addChild(root_0, string_literal269_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1689)
                expression270 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression270.tree)
                set271 = self.input.LT(1)
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
                        self.input, mse, self.FOLLOW_set_in_throwStatement1691
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
                self.memoize(self.input, 47, throwStatement_StartIndex)

            pass

        return retval

    # $ANTLR end throwStatement

    class tryStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start tryStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal272 = None
        LT273 = None
        LT275 = None
        LT278 = None
        statementBlock274 = None

        finallyClause276 = None

        catchClause277 = None

        finallyClause279 = None


        string_literal272_tree = None
        LT273_tree = None
        LT275_tree = None
        LT278_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal272 = self.input.LT(1)
                self.match(self.input, 93, self.FOLLOW_93_in_tryStatement1709)
                if self.failed:
                    return retval

                string_literal272_tree = self.adaptor.createWithPayload(string_literal272)
                self.adaptor.addChild(root_0, string_literal272_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:12: ( LT )*
                while True: #loop124
                    alt124 = 2
                    LA124_0 = self.input.LA(1)

                    if (LA124_0 == LT) :
                        alt124 = 1


                    if alt124 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT273 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1711)
                        if self.failed:
                            return retval


                    else:
                        break #loop124


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1715)
                statementBlock274 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock274.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:32: ( LT )*
                while True: #loop125
                    alt125 = 2
                    LA125_0 = self.input.LA(1)

                    if (LA125_0 == LT) :
                        alt125 = 1


                    if alt125 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT275 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1717)
                        if self.failed:
                            return retval


                    else:
                        break #loop125


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt128 = 2
                LA128_0 = self.input.LA(1)

                if (LA128_0 == 95) :
                    alt128 = 1
                elif (LA128_0 == 94) :
                    alt128 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("291:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 128, 0, self.input)

                    raise nvae

                if alt128 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1722)
                    finallyClause276 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause276.tree)


                elif alt128 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1726)
                    catchClause277 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause277.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:64: ( ( LT )* finallyClause )?
                    alt127 = 2
                    alt127 = self.dfa127.predict(self.input)
                    if alt127 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:67: ( LT )*
                        while True: #loop126
                            alt126 = 2
                            LA126_0 = self.input.LA(1)

                            if (LA126_0 == LT) :
                                alt126 = 1


                            if alt126 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT278 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1729)
                                if self.failed:
                                    return retval


                            else:
                                break #loop126


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1733)
                        finallyClause279 = self.finallyClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, finallyClause279.tree)









                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 48, tryStatement_StartIndex)

            pass

        return retval

    # $ANTLR end tryStatement

    class catchClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start catchClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal280 = None
        LT281 = None
        char_literal282 = None
        LT283 = None
        LT285 = None
        char_literal286 = None
        LT287 = None
        identifier284 = None

        statementBlock288 = None


        string_literal280_tree = None
        LT281_tree = None
        char_literal282_tree = None
        LT283_tree = None
        LT285_tree = None
        char_literal286_tree = None
        LT287_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal280 = self.input.LT(1)
                self.match(self.input, 94, self.FOLLOW_94_in_catchClause1754)
                if self.failed:
                    return retval

                string_literal280_tree = self.adaptor.createWithPayload(string_literal280)
                self.adaptor.addChild(root_0, string_literal280_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:14: ( LT )*
                while True: #loop129
                    alt129 = 2
                    LA129_0 = self.input.LA(1)

                    if (LA129_0 == LT) :
                        alt129 = 1


                    if alt129 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT281 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1756)
                        if self.failed:
                            return retval


                    else:
                        break #loop129


                char_literal282 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_catchClause1760)
                if self.failed:
                    return retval

                char_literal282_tree = self.adaptor.createWithPayload(char_literal282)
                self.adaptor.addChild(root_0, char_literal282_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:23: ( LT )*
                while True: #loop130
                    alt130 = 2
                    LA130_0 = self.input.LA(1)

                    if (LA130_0 == LT) :
                        alt130 = 1


                    if alt130 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT283 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1762)
                        if self.failed:
                            return retval


                    else:
                        break #loop130


                self.following.append(self.FOLLOW_identifier_in_catchClause1766)
                identifier284 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier284.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:39: ( LT )*
                while True: #loop131
                    alt131 = 2
                    LA131_0 = self.input.LA(1)

                    if (LA131_0 == LT) :
                        alt131 = 1


                    if alt131 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT285 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1768)
                        if self.failed:
                            return retval


                    else:
                        break #loop131


                char_literal286 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_catchClause1772)
                if self.failed:
                    return retval

                char_literal286_tree = self.adaptor.createWithPayload(char_literal286)
                self.adaptor.addChild(root_0, char_literal286_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:48: ( LT )*
                while True: #loop132
                    alt132 = 2
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == LT) :
                        alt132 = 1


                    if alt132 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT287 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1774)
                        if self.failed:
                            return retval


                    else:
                        break #loop132


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1778)
                statementBlock288 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock288.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 49, catchClause_StartIndex)

            pass

        return retval

    # $ANTLR end catchClause

    class finallyClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start finallyClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal289 = None
        LT290 = None
        statementBlock291 = None


        string_literal289_tree = None
        LT290_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal289 = self.input.LT(1)
                self.match(self.input, 95, self.FOLLOW_95_in_finallyClause1790)
                if self.failed:
                    return retval

                string_literal289_tree = self.adaptor.createWithPayload(string_literal289)
                self.adaptor.addChild(root_0, string_literal289_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:16: ( LT )*
                while True: #loop133
                    alt133 = 2
                    LA133_0 = self.input.LA(1)

                    if (LA133_0 == LT) :
                        alt133 = 1


                    if alt133 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT290 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1792)
                        if self.failed:
                            return retval


                    else:
                        break #loop133


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause1796)
                statementBlock291 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock291.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 50, finallyClause_StartIndex)

            pass

        return retval

    # $ANTLR end finallyClause

    class expression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT293 = None
        char_literal294 = None
        LT295 = None
        assignmentExpression292 = None

        assignmentExpression296 = None


        LT293_tree = None
        char_literal294_tree = None
        LT295_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression1808)
                assignmentExpression292 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression292.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop136
                    alt136 = 2
                    alt136 = self.dfa136.predict(self.input)
                    if alt136 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:28: ( LT )*
                        while True: #loop134
                            alt134 = 2
                            LA134_0 = self.input.LA(1)

                            if (LA134_0 == LT) :
                                alt134 = 1


                            if alt134 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT293 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1811)
                                if self.failed:
                                    return retval


                            else:
                                break #loop134


                        char_literal294 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_expression1815)
                        if self.failed:
                            return retval

                        char_literal294_tree = self.adaptor.createWithPayload(char_literal294)
                        self.adaptor.addChild(root_0, char_literal294_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:37: ( LT )*
                        while True: #loop135
                            alt135 = 2
                            LA135_0 = self.input.LA(1)

                            if (LA135_0 == LT) :
                                LA135_2 = self.input.LA(2)

                                if (self.synpred164()) :
                                    alt135 = 1




                            if alt135 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT295 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1817)
                                if self.failed:
                                    return retval


                            else:
                                break #loop135


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression1821)
                        assignmentExpression296 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression296.tree)


                    else:
                        break #loop136





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 51, expression_StartIndex)

            pass

        return retval

    # $ANTLR end expression

    class expressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT298 = None
        char_literal299 = None
        LT300 = None
        assignmentExpressionNoIn297 = None

        assignmentExpressionNoIn301 = None


        LT298_tree = None
        char_literal299_tree = None
        LT300_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1835)
                assignmentExpressionNoIn297 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn297.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop139
                    alt139 = 2
                    alt139 = self.dfa139.predict(self.input)
                    if alt139 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:32: ( LT )*
                        while True: #loop137
                            alt137 = 2
                            LA137_0 = self.input.LA(1)

                            if (LA137_0 == LT) :
                                alt137 = 1


                            if alt137 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT298 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1838)
                                if self.failed:
                                    return retval


                            else:
                                break #loop137


                        char_literal299 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_expressionNoIn1842)
                        if self.failed:
                            return retval

                        char_literal299_tree = self.adaptor.createWithPayload(char_literal299)
                        self.adaptor.addChild(root_0, char_literal299_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:41: ( LT )*
                        while True: #loop138
                            alt138 = 2
                            LA138_0 = self.input.LA(1)

                            if (LA138_0 == LT) :
                                LA138_2 = self.input.LA(2)

                                if (self.synpred167()) :
                                    alt138 = 1




                            if alt138 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT300 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1844)
                                if self.failed:
                                    return retval


                            else:
                                break #loop138


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1848)
                        assignmentExpressionNoIn301 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn301.tree)


                    else:
                        break #loop139





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 52, expressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end expressionNoIn

    class assignmentExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT303 = None
        LT305 = None
        leftHandSideExpression302 = None

        assignmentOperator304 = None

        assignmentExpression306 = None

        conditionalExpression307 = None


        LT303_tree = None
        LT305_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_assignmentOperator = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentOperator")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self.adaptor, "rule leftHandSideExpression")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression )
                alt142 = 2
                LA142 = self.input.LA(1)
                if LA142 == 137:
                    LA142_1 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 1, self.input)

                        raise nvae

                elif LA142 == LT:
                    LA142_2 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 2, self.input)

                        raise nvae

                elif LA142 == 60:
                    LA142_3 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 3, self.input)

                        raise nvae

                elif LA142 == 66:
                    LA142_4 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 4, self.input)

                        raise nvae

                elif LA142 == XMLComment:
                    LA142_5 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 5, self.input)

                        raise nvae

                elif LA142 == Identifier or LA142 == 72 or LA142 == 73 or LA142 == 74 or LA142 == 85 or LA142 == 138 or LA142 == 139:
                    LA142_6 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 6, self.input)

                        raise nvae

                elif LA142 == 140:
                    LA142_7 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 7, self.input)

                        raise nvae

                elif LA142 == 141:
                    LA142_8 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 8, self.input)

                        raise nvae

                elif LA142 == 142:
                    LA142_9 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 9, self.input)

                        raise nvae

                elif LA142 == StringLiteral:
                    LA142_10 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 10, self.input)

                        raise nvae

                elif LA142 == NumericLiteral:
                    LA142_11 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 11, self.input)

                        raise nvae

                elif LA142 == 62:
                    LA142_12 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 12, self.input)

                        raise nvae

                elif LA142 == RegularExpressionHacks:
                    LA142_13 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 13, self.input)

                        raise nvae

                elif LA142 == 98:
                    LA142_14 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 14, self.input)

                        raise nvae

                elif LA142 == 69:
                    LA142_15 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 15, self.input)

                        raise nvae

                elif LA142 == 68:
                    LA142_16 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 16, self.input)

                        raise nvae

                elif LA142 == 96:
                    LA142_17 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 17, self.input)

                        raise nvae

                elif LA142 == 64 or LA142 == 128 or LA142 == 130 or LA142 == 131 or LA142 == 132 or LA142 == 133 or LA142 == 134 or LA142 == 135 or LA142 == 136:
                    alt142 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("311:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression ) | conditionalExpression );", 142, 0, self.input)

                    raise nvae

                if alt142 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1862)
                    leftHandSideExpression302 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression302.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:27: ( LT )*
                    while True: #loop140
                        alt140 = 2
                        LA140_0 = self.input.LA(1)

                        if (LA140_0 == LT) :
                            alt140 = 1


                        if alt140 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT303 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1864)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT303)


                        else:
                            break #loop140


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1867)
                    assignmentOperator304 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentOperator.add(assignmentOperator304.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:50: ( LT )*
                    while True: #loop141
                        alt141 = 2
                        LA141_0 = self.input.LA(1)

                        if (LA141_0 == LT) :
                            LA141_2 = self.input.LA(2)

                            if (self.synpred170()) :
                                alt141 = 1




                        if alt141 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT305 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1869)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT305)


                        else:
                            break #loop141


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1872)
                    assignmentExpression306 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression306.tree)
                    # AST Rewrite
                    # elements: assignmentExpression, leftHandSideExpression, assignmentOperator
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
                        # 313:3: -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:313:6: ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ASSIGN, "ASSIGN"), root_1)

                        self.adaptor.addChild(root_1, stream_leftHandSideExpression.next())
                        self.adaptor.addChild(root_1, stream_assignmentOperator.next())
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt142 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression1891)
                    conditionalExpression307 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression307.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 53, assignmentExpression_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpression

    class assignmentExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT309 = None
        LT311 = None
        leftHandSideExpression308 = None

        assignmentOperator310 = None

        assignmentExpressionNoIn312 = None

        conditionalExpressionNoIn313 = None


        LT309_tree = None
        LT311_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_assignmentOperator = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentOperator")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        stream_leftHandSideExpression = RewriteRuleSubtreeStream(self.adaptor, "rule leftHandSideExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn )
                alt145 = 2
                LA145 = self.input.LA(1)
                if LA145 == 137:
                    LA145_1 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 1, self.input)

                        raise nvae

                elif LA145 == LT:
                    LA145_2 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 2, self.input)

                        raise nvae

                elif LA145 == 60:
                    LA145_3 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 3, self.input)

                        raise nvae

                elif LA145 == 66:
                    LA145_4 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 4, self.input)

                        raise nvae

                elif LA145 == XMLComment:
                    LA145_5 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 5, self.input)

                        raise nvae

                elif LA145 == Identifier or LA145 == 72 or LA145 == 73 or LA145 == 74 or LA145 == 85 or LA145 == 138 or LA145 == 139:
                    LA145_6 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 6, self.input)

                        raise nvae

                elif LA145 == 140:
                    LA145_7 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 7, self.input)

                        raise nvae

                elif LA145 == 141:
                    LA145_8 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 8, self.input)

                        raise nvae

                elif LA145 == 142:
                    LA145_9 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 9, self.input)

                        raise nvae

                elif LA145 == StringLiteral:
                    LA145_10 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 10, self.input)

                        raise nvae

                elif LA145 == NumericLiteral:
                    LA145_11 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 11, self.input)

                        raise nvae

                elif LA145 == 62:
                    LA145_12 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 12, self.input)

                        raise nvae

                elif LA145 == RegularExpressionHacks:
                    LA145_13 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 13, self.input)

                        raise nvae

                elif LA145 == 98:
                    LA145_14 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 14, self.input)

                        raise nvae

                elif LA145 == 69:
                    LA145_15 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 15, self.input)

                        raise nvae

                elif LA145 == 68:
                    LA145_16 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 16, self.input)

                        raise nvae

                elif LA145 == 96:
                    LA145_17 = self.input.LA(2)

                    if (self.synpred174()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 17, self.input)

                        raise nvae

                elif LA145 == 64 or LA145 == 128 or LA145 == 130 or LA145 == 131 or LA145 == 132 or LA145 == 133 or LA145 == 134 or LA145 == 135 or LA145 == 136:
                    alt145 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("317:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn ) | conditionalExpressionNoIn );", 145, 0, self.input)

                    raise nvae

                if alt145 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1903)
                    leftHandSideExpression308 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_leftHandSideExpression.add(leftHandSideExpression308.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:27: ( LT )*
                    while True: #loop143
                        alt143 = 2
                        LA143_0 = self.input.LA(1)

                        if (LA143_0 == LT) :
                            alt143 = 1


                        if alt143 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT309 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1905)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT309)


                        else:
                            break #loop143


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1908)
                    assignmentOperator310 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentOperator.add(assignmentOperator310.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:50: ( LT )*
                    while True: #loop144
                        alt144 = 2
                        LA144_0 = self.input.LA(1)

                        if (LA144_0 == LT) :
                            LA144_2 = self.input.LA(2)

                            if (self.synpred173()) :
                                alt144 = 1




                        if alt144 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT311 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1910)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT311)


                        else:
                            break #loop144


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1913)
                    assignmentExpressionNoIn312 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn312.tree)
                    # AST Rewrite
                    # elements: assignmentExpressionNoIn, leftHandSideExpression, assignmentOperator
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
                        # 319:3: -> ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:6: ^( ASSIGN leftHandSideExpression assignmentOperator assignmentExpressionNoIn )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ASSIGN, "ASSIGN"), root_1)

                        self.adaptor.addChild(root_1, stream_leftHandSideExpression.next())
                        self.adaptor.addChild(root_1, stream_assignmentOperator.next())
                        self.adaptor.addChild(root_1, stream_assignmentExpressionNoIn.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt145 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:320:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1932)
                    conditionalExpressionNoIn313 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn313.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 54, assignmentExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpressionNoIn

    class leftHandSideExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start leftHandSideExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression314 = None

        newExpression315 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:2: ( callExpression | newExpression )
                alt146 = 2
                LA146 = self.input.LA(1)
                if LA146 == 137:
                    LA146_1 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 1, self.input)

                        raise nvae

                elif LA146 == LT:
                    LA146_2 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 2, self.input)

                        raise nvae

                elif LA146 == 60:
                    LA146_3 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 3, self.input)

                        raise nvae

                elif LA146 == 66:
                    LA146_4 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 4, self.input)

                        raise nvae

                elif LA146 == XMLComment:
                    LA146_5 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 5, self.input)

                        raise nvae

                elif LA146 == Identifier or LA146 == 72 or LA146 == 73 or LA146 == 74 or LA146 == 85 or LA146 == 138 or LA146 == 139:
                    LA146_6 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 6, self.input)

                        raise nvae

                elif LA146 == 140:
                    LA146_7 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 7, self.input)

                        raise nvae

                elif LA146 == 141:
                    LA146_8 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 8, self.input)

                        raise nvae

                elif LA146 == 142:
                    LA146_9 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 9, self.input)

                        raise nvae

                elif LA146 == StringLiteral:
                    LA146_10 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 10, self.input)

                        raise nvae

                elif LA146 == NumericLiteral:
                    LA146_11 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 11, self.input)

                        raise nvae

                elif LA146 == 62:
                    LA146_12 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 12, self.input)

                        raise nvae

                elif LA146 == RegularExpressionHacks:
                    LA146_13 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 13, self.input)

                        raise nvae

                elif LA146 == 98:
                    LA146_14 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 14, self.input)

                        raise nvae

                elif LA146 == 69:
                    LA146_15 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 15, self.input)

                        raise nvae

                elif LA146 == 68:
                    LA146_16 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 16, self.input)

                        raise nvae

                elif LA146 == 96:
                    LA146_17 = self.input.LA(2)

                    if (self.synpred175()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("323:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 0, self.input)

                    raise nvae

                if alt146 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression1944)
                    callExpression314 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression314.tree)


                elif alt146 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:325:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression1949)
                    newExpression315 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression315.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 55, leftHandSideExpression_StartIndex)

            pass

        return retval

    # $ANTLR end leftHandSideExpression

    class newExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start newExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:328:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal317 = None
        LT318 = None
        memberExpression316 = None

        newExpression319 = None


        string_literal317_tree = None
        LT318_tree = None
        stream_96 = RewriteRuleTokenStream(self.adaptor, "token 96")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_newExpression = RewriteRuleSubtreeStream(self.adaptor, "rule newExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:2: ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) )
                alt148 = 2
                LA148_0 = self.input.LA(1)

                if ((LT <= LA148_0 <= RegularExpressionHacks) or LA148_0 == 60 or LA148_0 == 62 or LA148_0 == 66 or (68 <= LA148_0 <= 69) or (72 <= LA148_0 <= 74) or LA148_0 == 85 or LA148_0 == 98 or (137 <= LA148_0 <= 142)) :
                    alt148 = 1
                elif (LA148_0 == 96) :
                    LA148_17 = self.input.LA(2)

                    if (self.synpred176()) :
                        alt148 = 1
                    elif (True) :
                        alt148 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("328:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );", 148, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("328:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression -> ^( NEW newExpression ) );", 148, 0, self.input)

                    raise nvae

                if alt148 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression1961)
                    memberExpression316 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression316.tree)


                elif alt148 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:4: 'new' ( LT )* newExpression
                    string_literal317 = self.input.LT(1)
                    self.match(self.input, 96, self.FOLLOW_96_in_newExpression1966)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_96.add(string_literal317)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:10: ( LT )*
                    while True: #loop147
                        alt147 = 2
                        LA147_0 = self.input.LA(1)

                        if (LA147_0 == LT) :
                            LA147_2 = self.input.LA(2)

                            if (self.synpred177()) :
                                alt147 = 1




                        if alt147 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT318 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1968)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT318)


                        else:
                            break #loop147


                    self.following.append(self.FOLLOW_newExpression_in_newExpression1971)
                    newExpression319 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_newExpression.add(newExpression319.tree)
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
                        # 331:3: -> ^( NEW newExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:6: ^( NEW newExpression )
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
                self.memoize(self.input, 56, newExpression_StartIndex)

            pass

        return retval

    # $ANTLR end newExpression

    class memberExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:1: memberExpression : ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) );
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        LT321 = None
        LT324 = None
        string_literal326 = None
        LT327 = None
        LT329 = None
        LT331 = None
        primaryExpression320 = None

        memberExpressionSuffix322 = None

        functionExpression323 = None

        memberExpressionSuffix325 = None

        memberExpression328 = None

        arguments330 = None

        memberExpressionSuffix332 = None


        LT321_tree = None
        LT324_tree = None
        string_literal326_tree = None
        LT327_tree = None
        LT329_tree = None
        LT331_tree = None
        stream_96 = RewriteRuleTokenStream(self.adaptor, "token 96")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_primaryExpression = RewriteRuleSubtreeStream(self.adaptor, "rule primaryExpression")
        stream_memberExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:2: ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) )
                alt157 = 3
                LA157 = self.input.LA(1)
                if LA157 == LT or LA157 == StringLiteral or LA157 == XMLComment or LA157 == NumericLiteral or LA157 == Identifier or LA157 == RegularExpressionHacks or LA157 == 60 or LA157 == 62 or LA157 == 66 or LA157 == 69 or LA157 == 72 or LA157 == 73 or LA157 == 74 or LA157 == 85 or LA157 == 98 or LA157 == 137 or LA157 == 138 or LA157 == 139 or LA157 == 140 or LA157 == 141 or LA157 == 142:
                    alt157 = 1
                elif LA157 == 68:
                    alt157 = 2
                elif LA157 == 96:
                    alt157 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("334:1: memberExpression : ( primaryExpression ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* ) | functionExpression ( ( LT )* memberExpressionSuffix )* | 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )* -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* ) );", 157, 0, self.input)

                    raise nvae

                if alt157 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: primaryExpression ( ( LT )* memberExpressionSuffix )*
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression1993)
                    primaryExpression320 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_primaryExpression.add(primaryExpression320.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:22: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop150
                        alt150 = 2
                        LA150 = self.input.LA(1)
                        if LA150 == LT:
                            LA150_1 = self.input.LA(2)

                            if (self.synpred179()) :
                                alt150 = 1


                        elif LA150 == 63:
                            LA150_21 = self.input.LA(2)

                            if (self.synpred179()) :
                                alt150 = 1


                        elif LA150 == 97:
                            LA150_24 = self.input.LA(2)

                            if (self.synpred179()) :
                                alt150 = 1


                        elif LA150 == 98:
                            alt150 = 1

                        if alt150 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( LT )*
                            while True: #loop149
                                alt149 = 2
                                LA149_0 = self.input.LA(1)

                                if (LA149_0 == LT) :
                                    alt149 = 1


                                if alt149 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT321 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1996)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT321)


                                else:
                                    break #loop149


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1999)
                            memberExpressionSuffix322 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_memberExpressionSuffix.add(memberExpressionSuffix322.tree)


                        else:
                            break #loop150


                    # AST Rewrite
                    # elements: memberExpressionSuffix, primaryExpression
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
                        # 336:3: -> ^( VEXPR primaryExpression ( memberExpressionSuffix )* )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:336:6: ^( VEXPR primaryExpression ( memberExpressionSuffix )* )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VEXPR, "VEXPR"), root_1)

                        self.adaptor.addChild(root_1, stream_primaryExpression.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:336:32: ( memberExpressionSuffix )*
                        while stream_memberExpressionSuffix.hasNext():
                            self.adaptor.addChild(root_1, stream_memberExpressionSuffix.next())


                        stream_memberExpressionSuffix.reset();

                        self.adaptor.addChild(root_0, root_1)





                elif alt157 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:4: functionExpression ( ( LT )* memberExpressionSuffix )*
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression2019)
                    functionExpression323 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression323.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:23: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop152
                        alt152 = 2
                        LA152 = self.input.LA(1)
                        if LA152 == LT:
                            LA152_1 = self.input.LA(2)

                            if (self.synpred182()) :
                                alt152 = 1


                        elif LA152 == 63:
                            LA152_21 = self.input.LA(2)

                            if (self.synpred182()) :
                                alt152 = 1


                        elif LA152 == 97:
                            LA152_24 = self.input.LA(2)

                            if (self.synpred182()) :
                                alt152 = 1


                        elif LA152 == 98:
                            alt152 = 1

                        if alt152 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:24: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:26: ( LT )*
                            while True: #loop151
                                alt151 = 2
                                LA151_0 = self.input.LA(1)

                                if (LA151_0 == LT) :
                                    alt151 = 1


                                if alt151 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT324 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2022)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop151


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression2026)
                            memberExpressionSuffix325 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, memberExpressionSuffix325.tree)


                        else:
                            break #loop152




                elif alt157 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:4: 'new' ( LT )* memberExpression ( LT )* arguments ( ( LT )* memberExpressionSuffix )*
                    string_literal326 = self.input.LT(1)
                    self.match(self.input, 96, self.FOLLOW_96_in_memberExpression2033)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_96.add(string_literal326)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:10: ( LT )*
                    while True: #loop153
                        alt153 = 2
                        LA153_0 = self.input.LA(1)

                        if (LA153_0 == LT) :
                            LA153_2 = self.input.LA(2)

                            if (self.synpred184()) :
                                alt153 = 1




                        if alt153 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT327 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2035)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT327)


                        else:
                            break #loop153


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression2038)
                    memberExpression328 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_memberExpression.add(memberExpression328.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:31: ( LT )*
                    while True: #loop154
                        alt154 = 2
                        LA154_0 = self.input.LA(1)

                        if (LA154_0 == LT) :
                            alt154 = 1


                        if alt154 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT329 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2040)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT329)


                        else:
                            break #loop154


                    self.following.append(self.FOLLOW_arguments_in_memberExpression2043)
                    arguments330 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_arguments.add(arguments330.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:45: ( ( LT )* memberExpressionSuffix )*
                    while True: #loop156
                        alt156 = 2
                        LA156 = self.input.LA(1)
                        if LA156 == LT:
                            LA156_1 = self.input.LA(2)

                            if (self.synpred187()) :
                                alt156 = 1


                        elif LA156 == 63:
                            LA156_21 = self.input.LA(2)

                            if (self.synpred187()) :
                                alt156 = 1


                        elif LA156 == 97:
                            LA156_24 = self.input.LA(2)

                            if (self.synpred187()) :
                                alt156 = 1


                        elif LA156 == 98:
                            alt156 = 1

                        if alt156 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:46: ( LT )* memberExpressionSuffix
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:46: ( LT )*
                            while True: #loop155
                                alt155 = 2
                                LA155_0 = self.input.LA(1)

                                if (LA155_0 == LT) :
                                    alt155 = 1


                                if alt155 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT331 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression2046)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT331)


                                else:
                                    break #loop155


                            self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression2049)
                            memberExpressionSuffix332 = self.memberExpressionSuffix()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_memberExpressionSuffix.add(memberExpressionSuffix332.tree)


                        else:
                            break #loop156


                    # AST Rewrite
                    # elements: memberExpressionSuffix, arguments, memberExpression
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
                        # 339:3: -> ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:6: ^( VEXPR ^( NEW ^( CALL memberExpression arguments ) ) ( memberExpressionSuffix )* )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VEXPR, "VEXPR"), root_1)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:14: ^( NEW ^( CALL memberExpression arguments ) )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(NEW, "NEW"), root_2)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:20: ^( CALL memberExpression arguments )
                        root_3 = self.adaptor.nil()
                        root_3 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_3)

                        self.adaptor.addChild(root_3, stream_memberExpression.next())
                        self.adaptor.addChild(root_3, stream_arguments.next())

                        self.adaptor.addChild(root_2, root_3)

                        self.adaptor.addChild(root_1, root_2)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:56: ( memberExpressionSuffix )*
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
                self.memoize(self.input, 57, memberExpression_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpression

    class memberExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix333 = None

        propertyReferenceSuffix334 = None

        descendentSuffix335 = None

        namespaceSuffix336 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:2: ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt158 = 4
                LA158 = self.input.LA(1)
                if LA158 == 98:
                    alt158 = 1
                elif LA158 == 97:
                    LA158_2 = self.input.LA(2)

                    if (LA158_2 == 97) :
                        alt158 = 3
                    elif (LA158_2 == LT or LA158_2 == Identifier or (72 <= LA158_2 <= 74) or LA158_2 == 85 or LA158_2 == 100 or (138 <= LA158_2 <= 139)) :
                        alt158 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("342:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 158, 2, self.input)

                        raise nvae

                elif LA158 == 63:
                    alt158 = 4
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("342:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 158, 0, self.input)

                    raise nvae

                if alt158 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix2086)
                    indexSuffix333 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix333.tree)


                elif alt158 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:344:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix2091)
                    propertyReferenceSuffix334 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix334.tree)


                elif alt158 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:345:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_memberExpressionSuffix2096)
                    descendentSuffix335 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix335.tree)


                elif alt158 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_memberExpressionSuffix2102)
                    namespaceSuffix336 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix336.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 58, memberExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpressionSuffix

    class callExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:352:1: callExpression : memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT338 = None
        char_literal339 = None
        LT340 = None
        LT342 = None
        memberExpression337 = None

        arguments341 = None

        callExpressionSuffix343 = None


        LT338_tree = None
        char_literal339_tree = None
        LT340_tree = None
        LT342_tree = None
        stream_97 = RewriteRuleTokenStream(self.adaptor, "token 97")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_callExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule callExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:2: ( memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:4: memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                self.following.append(self.FOLLOW_memberExpression_in_callExpression2117)
                memberExpression337 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_memberExpression.add(memberExpression337.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:21: ( LT )*
                while True: #loop159
                    alt159 = 2
                    LA159_0 = self.input.LA(1)

                    if (LA159_0 == LT) :
                        LA159_2 = self.input.LA(2)

                        if (self.synpred191()) :
                            alt159 = 1




                    if alt159 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT338 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2119)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT338)


                    else:
                        break #loop159


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:25: ( '.' )?
                alt160 = 2
                LA160_0 = self.input.LA(1)

                if (LA160_0 == 97) :
                    alt160 = 1
                if alt160 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: '.'
                    char_literal339 = self.input.LT(1)
                    self.match(self.input, 97, self.FOLLOW_97_in_callExpression2122)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_97.add(char_literal339)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:30: ( LT )*
                while True: #loop161
                    alt161 = 2
                    LA161_0 = self.input.LA(1)

                    if (LA161_0 == LT) :
                        alt161 = 1


                    if alt161 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT340 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2125)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT340)


                    else:
                        break #loop161


                self.following.append(self.FOLLOW_arguments_in_callExpression2128)
                arguments341 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_arguments.add(arguments341.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:44: ( ( LT )* callExpressionSuffix )*
                while True: #loop163
                    alt163 = 2
                    LA163 = self.input.LA(1)
                    if LA163 == LT:
                        LA163_1 = self.input.LA(2)

                        if (self.synpred195()) :
                            alt163 = 1


                    elif LA163 == 63:
                        LA163_21 = self.input.LA(2)

                        if (self.synpred195()) :
                            alt163 = 1


                    elif LA163 == 69 or LA163 == 97 or LA163 == 98:
                        alt163 = 1

                    if alt163 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:45: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:45: ( LT )*
                        while True: #loop162
                            alt162 = 2
                            LA162_0 = self.input.LA(1)

                            if (LA162_0 == LT) :
                                alt162 = 1


                            if alt162 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT342 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression2131)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT342)


                            else:
                                break #loop162


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression2134)
                        callExpressionSuffix343 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_callExpressionSuffix.add(callExpressionSuffix343.tree)


                    else:
                        break #loop163


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
                    # 354:3: -> ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:6: ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_1)

                    self.adaptor.addChild(root_1, stream_memberExpression.next())
                    self.adaptor.addChild(root_1, stream_arguments.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:40: ( callExpressionSuffix )*
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
                self.memoize(self.input, 59, callExpression_StartIndex)

            pass

        return retval

    # $ANTLR end callExpression

    class callExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:357:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments344 = None

        indexSuffix345 = None

        propertyReferenceSuffix346 = None

        descendentSuffix347 = None

        namespaceSuffix348 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:2: ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt164 = 5
                LA164 = self.input.LA(1)
                if LA164 == 69:
                    alt164 = 1
                elif LA164 == 98:
                    alt164 = 2
                elif LA164 == 97:
                    LA164_3 = self.input.LA(2)

                    if (LA164_3 == 97) :
                        alt164 = 4
                    elif (LA164_3 == LT or LA164_3 == Identifier or (72 <= LA164_3 <= 74) or LA164_3 == 85 or LA164_3 == 100 or (138 <= LA164_3 <= 139)) :
                        alt164 = 3
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("357:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 164, 3, self.input)

                        raise nvae

                elif LA164 == 63:
                    alt164 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("357:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 164, 0, self.input)

                    raise nvae

                if alt164 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix2163)
                    arguments344 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments344.tree)


                elif alt164 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix2168)
                    indexSuffix345 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix345.tree)


                elif alt164 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:360:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2173)
                    propertyReferenceSuffix346 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix346.tree)


                elif alt164 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:361:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_callExpressionSuffix2178)
                    descendentSuffix347 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix347.tree)


                elif alt164 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:362:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_callExpressionSuffix2184)
                    namespaceSuffix348 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix348.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 60, callExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end callExpressionSuffix

    class arguments_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arguments
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:1: arguments : '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' -> ^( ARGS ( assignmentExpression )* ) ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal349 = None
        LT350 = None
        LT352 = None
        char_literal353 = None
        LT354 = None
        LT356 = None
        LT357 = None
        char_literal358 = None
        assignmentExpression351 = None

        assignmentExpression355 = None


        char_literal349_tree = None
        LT350_tree = None
        LT352_tree = None
        char_literal353_tree = None
        LT354_tree = None
        LT356_tree = None
        LT357_tree = None
        char_literal358_tree = None
        stream_69 = RewriteRuleTokenStream(self.adaptor, "token 69")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_71 = RewriteRuleTokenStream(self.adaptor, "token 71")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:2: ( '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' -> ^( ARGS ( assignmentExpression )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:4: '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')'
                char_literal349 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_arguments2199)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_69.add(char_literal349)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:8: ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )?
                alt170 = 2
                alt170 = self.dfa170.predict(self.input)
                if alt170 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:9: ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:9: ( LT )*
                    while True: #loop165
                        alt165 = 2
                        LA165_0 = self.input.LA(1)

                        if (LA165_0 == LT) :
                            LA165_2 = self.input.LA(2)

                            if (self.synpred200()) :
                                alt165 = 1




                        if alt165 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT350 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2202)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT350)


                        else:
                            break #loop165


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments2205)
                    assignmentExpression351 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression351.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:34: ( LT )*
                    while True: #loop166
                        alt166 = 2
                        LA166_0 = self.input.LA(1)

                        if (LA166_0 == LT) :
                            LA166_2 = self.input.LA(2)

                            if (self.synpred201()) :
                                alt166 = 1




                        if alt166 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT352 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2207)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT352)


                        else:
                            break #loop166


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:38: ( ',' ( LT )* assignmentExpression ( LT )* )*
                    while True: #loop169
                        alt169 = 2
                        LA169_0 = self.input.LA(1)

                        if (LA169_0 == 70) :
                            alt169 = 1


                        if alt169 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:39: ',' ( LT )* assignmentExpression ( LT )*
                            char_literal353 = self.input.LT(1)
                            self.match(self.input, 70, self.FOLLOW_70_in_arguments2211)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_70.add(char_literal353)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:43: ( LT )*
                            while True: #loop167
                                alt167 = 2
                                LA167_0 = self.input.LA(1)

                                if (LA167_0 == LT) :
                                    LA167_2 = self.input.LA(2)

                                    if (self.synpred202()) :
                                        alt167 = 1




                                if alt167 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT354 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2213)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT354)


                                else:
                                    break #loop167


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments2216)
                            assignmentExpression355 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression355.tree)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:68: ( LT )*
                            while True: #loop168
                                alt168 = 2
                                LA168_0 = self.input.LA(1)

                                if (LA168_0 == LT) :
                                    LA168_1 = self.input.LA(2)

                                    if (self.synpred203()) :
                                        alt168 = 1




                                if alt168 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT356 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2218)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT356)


                                else:
                                    break #loop168




                        else:
                            break #loop169





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:76: ( LT )*
                while True: #loop171
                    alt171 = 2
                    LA171_0 = self.input.LA(1)

                    if (LA171_0 == LT) :
                        alt171 = 1


                    if alt171 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT357 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments2225)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT357)


                    else:
                        break #loop171


                char_literal358 = self.input.LT(1)
                self.match(self.input, 71, self.FOLLOW_71_in_arguments2228)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_71.add(char_literal358)
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
                    # 370:3: -> ^( ARGS ( assignmentExpression )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:370:6: ^( ARGS ( assignmentExpression )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARGS, "ARGS"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:370:13: ( assignmentExpression )*
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
                self.memoize(self.input, 61, arguments_StartIndex)

            pass

        return retval

    # $ANTLR end arguments

    class indexSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start indexSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal359 = None
        LT360 = None
        LT362 = None
        char_literal363 = None
        expression361 = None


        char_literal359_tree = None
        LT360_tree = None
        LT362_tree = None
        char_literal363_tree = None
        stream_98 = RewriteRuleTokenStream(self.adaptor, "token 98")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_99 = RewriteRuleTokenStream(self.adaptor, "token 99")
        stream_expression = RewriteRuleSubtreeStream(self.adaptor, "rule expression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:2: ( '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:4: '[' ( LT )* expression ( LT )* ']'
                char_literal359 = self.input.LT(1)
                self.match(self.input, 98, self.FOLLOW_98_in_indexSuffix2251)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_98.add(char_literal359)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: ( LT )*
                while True: #loop172
                    alt172 = 2
                    LA172_0 = self.input.LA(1)

                    if (LA172_0 == LT) :
                        LA172_2 = self.input.LA(2)

                        if (self.synpred207()) :
                            alt172 = 1




                    if alt172 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT360 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2253)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT360)


                    else:
                        break #loop172


                self.following.append(self.FOLLOW_expression_in_indexSuffix2256)
                expression361 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_expression.add(expression361.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:23: ( LT )*
                while True: #loop173
                    alt173 = 2
                    LA173_0 = self.input.LA(1)

                    if (LA173_0 == LT) :
                        alt173 = 1


                    if alt173 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT362 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2258)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT362)


                    else:
                        break #loop173


                char_literal363 = self.input.LT(1)
                self.match(self.input, 99, self.FOLLOW_99_in_indexSuffix2261)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_99.add(char_literal363)
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
                    # 375:3: -> ^( INDEXREF expression )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:375:6: ^( INDEXREF expression )
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
                self.memoize(self.input, 62, indexSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end indexSuffix

    class propertyReferenceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyReferenceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:1: propertyReferenceSuffix : '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal364 = None
        LT365 = None
        e4xIdentifier366 = None


        char_literal364_tree = None
        LT365_tree = None
        stream_97 = RewriteRuleTokenStream(self.adaptor, "token 97")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:2: ( '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:4: '.' ( LT )* e4xIdentifier
                char_literal364 = self.input.LT(1)
                self.match(self.input, 97, self.FOLLOW_97_in_propertyReferenceSuffix2284)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_97.add(char_literal364)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:8: ( LT )*
                while True: #loop174
                    alt174 = 2
                    LA174_0 = self.input.LA(1)

                    if (LA174_0 == LT) :
                        alt174 = 1


                    if alt174 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT365 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix2286)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT365)


                    else:
                        break #loop174


                self.following.append(self.FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2289)
                e4xIdentifier366 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier366.tree)
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
                    # 380:3: -> ^( PROPREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:6: ^( PROPREF e4xIdentifier )
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
                self.memoize(self.input, 63, propertyReferenceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end propertyReferenceSuffix

    class descendentSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start descendentSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:1: descendentSuffix : '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) ;
    def descendentSuffix(self, ):

        retval = self.descendentSuffix_return()
        retval.start = self.input.LT(1)
        descendentSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal367 = None
        char_literal368 = None
        LT369 = None
        e4xIdentifier370 = None


        char_literal367_tree = None
        char_literal368_tree = None
        LT369_tree = None
        stream_97 = RewriteRuleTokenStream(self.adaptor, "token 97")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:2: ( '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:4: '.' '.' ( LT )* e4xIdentifier
                char_literal367 = self.input.LT(1)
                self.match(self.input, 97, self.FOLLOW_97_in_descendentSuffix2310)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_97.add(char_literal367)
                char_literal368 = self.input.LT(1)
                self.match(self.input, 97, self.FOLLOW_97_in_descendentSuffix2312)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_97.add(char_literal368)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:12: ( LT )*
                while True: #loop175
                    alt175 = 2
                    LA175_0 = self.input.LA(1)

                    if (LA175_0 == LT) :
                        alt175 = 1


                    if alt175 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT369 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_descendentSuffix2314)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT369)


                    else:
                        break #loop175


                self.following.append(self.FOLLOW_e4xIdentifier_in_descendentSuffix2317)
                e4xIdentifier370 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier370.tree)
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
                    # 385:3: -> ^( DESCREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:6: ^( DESCREF e4xIdentifier )
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
                self.memoize(self.input, 64, descendentSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end descendentSuffix

    class namespaceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start namespaceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:1: namespaceSuffix : ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) ;
    def namespaceSuffix(self, ):

        retval = self.namespaceSuffix_return()
        retval.start = self.input.LT(1)
        namespaceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal371 = None
        char_literal372 = None
        LT373 = None
        e4xIdentifier374 = None


        char_literal371_tree = None
        char_literal372_tree = None
        LT373_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:2: ( ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:4: ':' ':' ( LT )* ( e4xIdentifier )?
                char_literal371 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_namespaceSuffix2338)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal371)
                char_literal372 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_namespaceSuffix2340)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_63.add(char_literal372)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:12: ( LT )*
                while True: #loop176
                    alt176 = 2
                    LA176_0 = self.input.LA(1)

                    if (LA176_0 == LT) :
                        LA176_2 = self.input.LA(2)

                        if (self.synpred211()) :
                            alt176 = 1




                    if alt176 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT373 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_namespaceSuffix2342)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT373)


                    else:
                        break #loop176


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:16: ( e4xIdentifier )?
                alt177 = 2
                LA177_0 = self.input.LA(1)

                if (LA177_0 == Identifier or (72 <= LA177_0 <= 74) or LA177_0 == 85 or (138 <= LA177_0 <= 139)) :
                    alt177 = 1
                elif (LA177_0 == 100) :
                    LA177_2 = self.input.LA(2)

                    if (self.synpred212()) :
                        alt177 = 1
                if alt177 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: e4xIdentifier
                    self.following.append(self.FOLLOW_e4xIdentifier_in_namespaceSuffix2345)
                    e4xIdentifier374 = self.e4xIdentifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_e4xIdentifier.add(e4xIdentifier374.tree)



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
                    # 390:3: -> ^( NSREF ( e4xIdentifier )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:6: ^( NSREF ( e4xIdentifier )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NSREF, "NSREF"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:14: ( e4xIdentifier )?
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
                self.memoize(self.input, 65, namespaceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end namespaceSuffix

    class e4xIdentifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start e4xIdentifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:393:1: e4xIdentifier : ( identifier | '*' );
    def e4xIdentifier(self, ):

        retval = self.e4xIdentifier_return()
        retval.start = self.input.LT(1)
        e4xIdentifier_StartIndex = self.input.index()
        root_0 = None

        char_literal376 = None
        identifier375 = None


        char_literal376_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:2: ( identifier | '*' )
                alt178 = 2
                LA178_0 = self.input.LA(1)

                if (LA178_0 == Identifier or (72 <= LA178_0 <= 74) or LA178_0 == 85 or (138 <= LA178_0 <= 139)) :
                    alt178 = 1
                elif (LA178_0 == 100) :
                    alt178 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("393:1: e4xIdentifier : ( identifier | '*' );", 178, 0, self.input)

                    raise nvae

                if alt178 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_e4xIdentifier2368)
                    identifier375 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier375.tree)


                elif alt178 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:395:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal376 = self.input.LT(1)
                    self.match(self.input, 100, self.FOLLOW_100_in_e4xIdentifier2373)
                    if self.failed:
                        return retval

                    char_literal376_tree = self.adaptor.createWithPayload(char_literal376)
                    self.adaptor.addChild(root_0, char_literal376_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 66, e4xIdentifier_StartIndex)

            pass

        return retval

    # $ANTLR end e4xIdentifier

    class assignmentOperator_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentOperator
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set377 = None

        set377_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:399:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set377 = self.input.LT(1)
                if self.input.LA(1) == 65 or (101 <= self.input.LA(1) <= 111):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set377))
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
                self.memoize(self.input, 67, assignmentOperator_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentOperator

    class conditionalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT379 = None
        char_literal380 = None
        LT381 = None
        LT383 = None
        char_literal384 = None
        LT385 = None
        logicalORExpression378 = None

        assignmentExpression382 = None

        assignmentExpression386 = None


        LT379_tree = None
        char_literal380_tree = None
        LT381_tree = None
        LT383_tree = None
        char_literal384_tree = None
        LT385_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression2440)
                logicalORExpression378 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression378.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt183 = 2
                alt183 = self.dfa183.predict(self.input)
                if alt183 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:27: ( LT )*
                    while True: #loop179
                        alt179 = 2
                        LA179_0 = self.input.LA(1)

                        if (LA179_0 == LT) :
                            alt179 = 1


                        if alt179 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT379 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2443)
                            if self.failed:
                                return retval


                        else:
                            break #loop179


                    char_literal380 = self.input.LT(1)
                    self.match(self.input, 112, self.FOLLOW_112_in_conditionalExpression2447)
                    if self.failed:
                        return retval

                    char_literal380_tree = self.adaptor.createWithPayload(char_literal380)
                    self.adaptor.addChild(root_0, char_literal380_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:36: ( LT )*
                    while True: #loop180
                        alt180 = 2
                        LA180_0 = self.input.LA(1)

                        if (LA180_0 == LT) :
                            LA180_2 = self.input.LA(2)

                            if (self.synpred226()) :
                                alt180 = 1




                        if alt180 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT381 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2449)
                            if self.failed:
                                return retval


                        else:
                            break #loop180


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2453)
                    assignmentExpression382 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression382.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:62: ( LT )*
                    while True: #loop181
                        alt181 = 2
                        LA181_0 = self.input.LA(1)

                        if (LA181_0 == LT) :
                            alt181 = 1


                        if alt181 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT383 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2455)
                            if self.failed:
                                return retval


                        else:
                            break #loop181


                    char_literal384 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpression2459)
                    if self.failed:
                        return retval

                    char_literal384_tree = self.adaptor.createWithPayload(char_literal384)
                    self.adaptor.addChild(root_0, char_literal384_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:71: ( LT )*
                    while True: #loop182
                        alt182 = 2
                        LA182_0 = self.input.LA(1)

                        if (LA182_0 == LT) :
                            LA182_2 = self.input.LA(2)

                            if (self.synpred228()) :
                                alt182 = 1




                        if alt182 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT385 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2461)
                            if self.failed:
                                return retval


                        else:
                            break #loop182


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2465)
                    assignmentExpression386 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression386.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 68, conditionalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpression

    class conditionalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
    def conditionalExpressionNoIn(self, ):

        retval = self.conditionalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        conditionalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT388 = None
        char_literal389 = None
        LT390 = None
        LT392 = None
        char_literal393 = None
        LT394 = None
        logicalORExpressionNoIn387 = None

        assignmentExpressionNoIn391 = None

        assignmentExpressionNoIn395 = None


        LT388_tree = None
        char_literal389_tree = None
        LT390_tree = None
        LT392_tree = None
        char_literal393_tree = None
        LT394_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2478)
                logicalORExpressionNoIn387 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn387.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt188 = 2
                alt188 = self.dfa188.predict(self.input)
                if alt188 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:31: ( LT )*
                    while True: #loop184
                        alt184 = 2
                        LA184_0 = self.input.LA(1)

                        if (LA184_0 == LT) :
                            alt184 = 1


                        if alt184 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT388 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2481)
                            if self.failed:
                                return retval


                        else:
                            break #loop184


                    char_literal389 = self.input.LT(1)
                    self.match(self.input, 112, self.FOLLOW_112_in_conditionalExpressionNoIn2485)
                    if self.failed:
                        return retval

                    char_literal389_tree = self.adaptor.createWithPayload(char_literal389)
                    self.adaptor.addChild(root_0, char_literal389_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:40: ( LT )*
                    while True: #loop185
                        alt185 = 2
                        LA185_0 = self.input.LA(1)

                        if (LA185_0 == LT) :
                            LA185_2 = self.input.LA(2)

                            if (self.synpred231()) :
                                alt185 = 1




                        if alt185 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT390 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2487)
                            if self.failed:
                                return retval


                        else:
                            break #loop185


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2491)
                    assignmentExpressionNoIn391 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn391.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:70: ( LT )*
                    while True: #loop186
                        alt186 = 2
                        LA186_0 = self.input.LA(1)

                        if (LA186_0 == LT) :
                            alt186 = 1


                        if alt186 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT392 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2493)
                            if self.failed:
                                return retval


                        else:
                            break #loop186


                    char_literal393 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpressionNoIn2497)
                    if self.failed:
                        return retval

                    char_literal393_tree = self.adaptor.createWithPayload(char_literal393)
                    self.adaptor.addChild(root_0, char_literal393_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:79: ( LT )*
                    while True: #loop187
                        alt187 = 2
                        LA187_0 = self.input.LA(1)

                        if (LA187_0 == LT) :
                            LA187_2 = self.input.LA(2)

                            if (self.synpred233()) :
                                alt187 = 1




                        if alt187 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT394 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2499)
                            if self.failed:
                                return retval


                        else:
                            break #loop187


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2503)
                    assignmentExpressionNoIn395 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn395.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 69, conditionalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpressionNoIn

    class logicalORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
    def logicalORExpression(self, ):

        retval = self.logicalORExpression_return()
        retval.start = self.input.LT(1)
        logicalORExpression_StartIndex = self.input.index()
        root_0 = None

        LT397 = None
        string_literal398 = None
        LT399 = None
        logicalANDExpression396 = None

        logicalANDExpression400 = None


        LT397_tree = None
        string_literal398_tree = None
        LT399_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2516)
                logicalANDExpression396 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression396.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop191
                    alt191 = 2
                    alt191 = self.dfa191.predict(self.input)
                    if alt191 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:28: ( LT )*
                        while True: #loop189
                            alt189 = 2
                            LA189_0 = self.input.LA(1)

                            if (LA189_0 == LT) :
                                alt189 = 1


                            if alt189 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT397 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2519)
                                if self.failed:
                                    return retval


                            else:
                                break #loop189


                        string_literal398 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_logicalORExpression2523)
                        if self.failed:
                            return retval

                        string_literal398_tree = self.adaptor.createWithPayload(string_literal398)
                        self.adaptor.addChild(root_0, string_literal398_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:38: ( LT )*
                        while True: #loop190
                            alt190 = 2
                            LA190_0 = self.input.LA(1)

                            if (LA190_0 == LT) :
                                LA190_2 = self.input.LA(2)

                                if (self.synpred236()) :
                                    alt190 = 1




                            if alt190 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT399 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2525)
                                if self.failed:
                                    return retval


                            else:
                                break #loop190


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2529)
                        logicalANDExpression400 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression400.tree)


                    else:
                        break #loop191





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 70, logicalORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpression

    class logicalORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
    def logicalORExpressionNoIn(self, ):

        retval = self.logicalORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT402 = None
        string_literal403 = None
        LT404 = None
        logicalANDExpressionNoIn401 = None

        logicalANDExpressionNoIn405 = None


        LT402_tree = None
        string_literal403_tree = None
        LT404_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2543)
                logicalANDExpressionNoIn401 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn401.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop194
                    alt194 = 2
                    alt194 = self.dfa194.predict(self.input)
                    if alt194 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:32: ( LT )*
                        while True: #loop192
                            alt192 = 2
                            LA192_0 = self.input.LA(1)

                            if (LA192_0 == LT) :
                                alt192 = 1


                            if alt192 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT402 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2546)
                                if self.failed:
                                    return retval


                            else:
                                break #loop192


                        string_literal403 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_logicalORExpressionNoIn2550)
                        if self.failed:
                            return retval

                        string_literal403_tree = self.adaptor.createWithPayload(string_literal403)
                        self.adaptor.addChild(root_0, string_literal403_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:42: ( LT )*
                        while True: #loop193
                            alt193 = 2
                            LA193_0 = self.input.LA(1)

                            if (LA193_0 == LT) :
                                LA193_2 = self.input.LA(2)

                                if (self.synpred239()) :
                                    alt193 = 1




                            if alt193 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT404 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2552)
                                if self.failed:
                                    return retval


                            else:
                                break #loop193


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2556)
                        logicalANDExpressionNoIn405 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn405.tree)


                    else:
                        break #loop194





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 71, logicalORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpressionNoIn

    class logicalANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
    def logicalANDExpression(self, ):

        retval = self.logicalANDExpression_return()
        retval.start = self.input.LT(1)
        logicalANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT407 = None
        string_literal408 = None
        LT409 = None
        bitwiseORExpression406 = None

        bitwiseORExpression410 = None


        LT407_tree = None
        string_literal408_tree = None
        LT409_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2570)
                bitwiseORExpression406 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression406.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop197
                    alt197 = 2
                    alt197 = self.dfa197.predict(self.input)
                    if alt197 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:27: ( LT )*
                        while True: #loop195
                            alt195 = 2
                            LA195_0 = self.input.LA(1)

                            if (LA195_0 == LT) :
                                alt195 = 1


                            if alt195 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT407 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2573)
                                if self.failed:
                                    return retval


                            else:
                                break #loop195


                        string_literal408 = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_logicalANDExpression2577)
                        if self.failed:
                            return retval

                        string_literal408_tree = self.adaptor.createWithPayload(string_literal408)
                        self.adaptor.addChild(root_0, string_literal408_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:37: ( LT )*
                        while True: #loop196
                            alt196 = 2
                            LA196_0 = self.input.LA(1)

                            if (LA196_0 == LT) :
                                LA196_2 = self.input.LA(2)

                                if (self.synpred242()) :
                                    alt196 = 1




                            if alt196 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT409 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2579)
                                if self.failed:
                                    return retval


                            else:
                                break #loop196


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2583)
                        bitwiseORExpression410 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression410.tree)


                    else:
                        break #loop197





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 72, logicalANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpression

    class logicalANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
    def logicalANDExpressionNoIn(self, ):

        retval = self.logicalANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT412 = None
        string_literal413 = None
        LT414 = None
        bitwiseORExpressionNoIn411 = None

        bitwiseORExpressionNoIn415 = None


        LT412_tree = None
        string_literal413_tree = None
        LT414_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2597)
                bitwiseORExpressionNoIn411 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn411.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop200
                    alt200 = 2
                    alt200 = self.dfa200.predict(self.input)
                    if alt200 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:31: ( LT )*
                        while True: #loop198
                            alt198 = 2
                            LA198_0 = self.input.LA(1)

                            if (LA198_0 == LT) :
                                alt198 = 1


                            if alt198 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT412 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2600)
                                if self.failed:
                                    return retval


                            else:
                                break #loop198


                        string_literal413 = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_logicalANDExpressionNoIn2604)
                        if self.failed:
                            return retval

                        string_literal413_tree = self.adaptor.createWithPayload(string_literal413)
                        self.adaptor.addChild(root_0, string_literal413_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:41: ( LT )*
                        while True: #loop199
                            alt199 = 2
                            LA199_0 = self.input.LA(1)

                            if (LA199_0 == LT) :
                                LA199_2 = self.input.LA(2)

                                if (self.synpred245()) :
                                    alt199 = 1




                            if alt199 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT414 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2606)
                                if self.failed:
                                    return retval


                            else:
                                break #loop199


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2610)
                        bitwiseORExpressionNoIn415 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn415.tree)


                    else:
                        break #loop200





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 73, logicalANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpressionNoIn

    class bitwiseORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
    def bitwiseORExpression(self, ):

        retval = self.bitwiseORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseORExpression_StartIndex = self.input.index()
        root_0 = None

        LT417 = None
        char_literal418 = None
        LT419 = None
        bitwiseXORExpression416 = None

        bitwiseXORExpression420 = None


        LT417_tree = None
        char_literal418_tree = None
        LT419_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2624)
                bitwiseXORExpression416 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression416.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop203
                    alt203 = 2
                    alt203 = self.dfa203.predict(self.input)
                    if alt203 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:28: ( LT )*
                        while True: #loop201
                            alt201 = 2
                            LA201_0 = self.input.LA(1)

                            if (LA201_0 == LT) :
                                alt201 = 1


                            if alt201 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT417 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2627)
                                if self.failed:
                                    return retval


                            else:
                                break #loop201


                        char_literal418 = self.input.LT(1)
                        self.match(self.input, 115, self.FOLLOW_115_in_bitwiseORExpression2631)
                        if self.failed:
                            return retval

                        char_literal418_tree = self.adaptor.createWithPayload(char_literal418)
                        self.adaptor.addChild(root_0, char_literal418_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:37: ( LT )*
                        while True: #loop202
                            alt202 = 2
                            LA202_0 = self.input.LA(1)

                            if (LA202_0 == LT) :
                                LA202_2 = self.input.LA(2)

                                if (self.synpred248()) :
                                    alt202 = 1




                            if alt202 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT419 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2633)
                                if self.failed:
                                    return retval


                            else:
                                break #loop202


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2637)
                        bitwiseXORExpression420 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression420.tree)


                    else:
                        break #loop203





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 74, bitwiseORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpression

    class bitwiseORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
    def bitwiseORExpressionNoIn(self, ):

        retval = self.bitwiseORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT422 = None
        char_literal423 = None
        LT424 = None
        bitwiseXORExpressionNoIn421 = None

        bitwiseXORExpressionNoIn425 = None


        LT422_tree = None
        char_literal423_tree = None
        LT424_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2651)
                bitwiseXORExpressionNoIn421 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn421.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop206
                    alt206 = 2
                    alt206 = self.dfa206.predict(self.input)
                    if alt206 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:32: ( LT )*
                        while True: #loop204
                            alt204 = 2
                            LA204_0 = self.input.LA(1)

                            if (LA204_0 == LT) :
                                alt204 = 1


                            if alt204 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT422 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2654)
                                if self.failed:
                                    return retval


                            else:
                                break #loop204


                        char_literal423 = self.input.LT(1)
                        self.match(self.input, 115, self.FOLLOW_115_in_bitwiseORExpressionNoIn2658)
                        if self.failed:
                            return retval

                        char_literal423_tree = self.adaptor.createWithPayload(char_literal423)
                        self.adaptor.addChild(root_0, char_literal423_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:41: ( LT )*
                        while True: #loop205
                            alt205 = 2
                            LA205_0 = self.input.LA(1)

                            if (LA205_0 == LT) :
                                LA205_2 = self.input.LA(2)

                                if (self.synpred251()) :
                                    alt205 = 1




                            if alt205 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT424 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2660)
                                if self.failed:
                                    return retval


                            else:
                                break #loop205


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2664)
                        bitwiseXORExpressionNoIn425 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn425.tree)


                    else:
                        break #loop206





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 75, bitwiseORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpressionNoIn

    class bitwiseXORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
    def bitwiseXORExpression(self, ):

        retval = self.bitwiseXORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpression_StartIndex = self.input.index()
        root_0 = None

        LT427 = None
        char_literal428 = None
        LT429 = None
        bitwiseANDExpression426 = None

        bitwiseANDExpression430 = None


        LT427_tree = None
        char_literal428_tree = None
        LT429_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2678)
                bitwiseANDExpression426 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression426.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop209
                    alt209 = 2
                    alt209 = self.dfa209.predict(self.input)
                    if alt209 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:28: ( LT )*
                        while True: #loop207
                            alt207 = 2
                            LA207_0 = self.input.LA(1)

                            if (LA207_0 == LT) :
                                alt207 = 1


                            if alt207 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT427 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2681)
                                if self.failed:
                                    return retval


                            else:
                                break #loop207


                        char_literal428 = self.input.LT(1)
                        self.match(self.input, 116, self.FOLLOW_116_in_bitwiseXORExpression2685)
                        if self.failed:
                            return retval

                        char_literal428_tree = self.adaptor.createWithPayload(char_literal428)
                        self.adaptor.addChild(root_0, char_literal428_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:37: ( LT )*
                        while True: #loop208
                            alt208 = 2
                            LA208_0 = self.input.LA(1)

                            if (LA208_0 == LT) :
                                LA208_2 = self.input.LA(2)

                                if (self.synpred254()) :
                                    alt208 = 1




                            if alt208 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT429 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2687)
                                if self.failed:
                                    return retval


                            else:
                                break #loop208


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2691)
                        bitwiseANDExpression430 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression430.tree)


                    else:
                        break #loop209





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 76, bitwiseXORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpression

    class bitwiseXORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
    def bitwiseXORExpressionNoIn(self, ):

        retval = self.bitwiseXORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT432 = None
        char_literal433 = None
        LT434 = None
        bitwiseANDExpressionNoIn431 = None

        bitwiseANDExpressionNoIn435 = None


        LT432_tree = None
        char_literal433_tree = None
        LT434_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2705)
                bitwiseANDExpressionNoIn431 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn431.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop212
                    alt212 = 2
                    alt212 = self.dfa212.predict(self.input)
                    if alt212 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:32: ( LT )*
                        while True: #loop210
                            alt210 = 2
                            LA210_0 = self.input.LA(1)

                            if (LA210_0 == LT) :
                                alt210 = 1


                            if alt210 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT432 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2708)
                                if self.failed:
                                    return retval


                            else:
                                break #loop210


                        char_literal433 = self.input.LT(1)
                        self.match(self.input, 116, self.FOLLOW_116_in_bitwiseXORExpressionNoIn2712)
                        if self.failed:
                            return retval

                        char_literal433_tree = self.adaptor.createWithPayload(char_literal433)
                        self.adaptor.addChild(root_0, char_literal433_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:41: ( LT )*
                        while True: #loop211
                            alt211 = 2
                            LA211_0 = self.input.LA(1)

                            if (LA211_0 == LT) :
                                LA211_2 = self.input.LA(2)

                                if (self.synpred257()) :
                                    alt211 = 1




                            if alt211 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT434 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2714)
                                if self.failed:
                                    return retval


                            else:
                                break #loop211


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2718)
                        bitwiseANDExpressionNoIn435 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn435.tree)


                    else:
                        break #loop212





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 77, bitwiseXORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpressionNoIn

    class bitwiseANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
    def bitwiseANDExpression(self, ):

        retval = self.bitwiseANDExpression_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT437 = None
        char_literal438 = None
        LT439 = None
        equalityExpression436 = None

        equalityExpression440 = None


        LT437_tree = None
        char_literal438_tree = None
        LT439_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2732)
                equalityExpression436 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression436.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop215
                    alt215 = 2
                    alt215 = self.dfa215.predict(self.input)
                    if alt215 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:26: ( LT )*
                        while True: #loop213
                            alt213 = 2
                            LA213_0 = self.input.LA(1)

                            if (LA213_0 == LT) :
                                alt213 = 1


                            if alt213 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT437 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2735)
                                if self.failed:
                                    return retval


                            else:
                                break #loop213


                        char_literal438 = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_bitwiseANDExpression2739)
                        if self.failed:
                            return retval

                        char_literal438_tree = self.adaptor.createWithPayload(char_literal438)
                        self.adaptor.addChild(root_0, char_literal438_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:35: ( LT )*
                        while True: #loop214
                            alt214 = 2
                            LA214_0 = self.input.LA(1)

                            if (LA214_0 == LT) :
                                LA214_2 = self.input.LA(2)

                                if (self.synpred260()) :
                                    alt214 = 1




                            if alt214 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT439 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2741)
                                if self.failed:
                                    return retval


                            else:
                                break #loop214


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2745)
                        equalityExpression440 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression440.tree)


                    else:
                        break #loop215





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 78, bitwiseANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpression

    class bitwiseANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
    def bitwiseANDExpressionNoIn(self, ):

        retval = self.bitwiseANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT442 = None
        char_literal443 = None
        LT444 = None
        equalityExpressionNoIn441 = None

        equalityExpressionNoIn445 = None


        LT442_tree = None
        char_literal443_tree = None
        LT444_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2759)
                equalityExpressionNoIn441 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn441.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop218
                    alt218 = 2
                    alt218 = self.dfa218.predict(self.input)
                    if alt218 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:30: ( LT )*
                        while True: #loop216
                            alt216 = 2
                            LA216_0 = self.input.LA(1)

                            if (LA216_0 == LT) :
                                alt216 = 1


                            if alt216 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT442 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2762)
                                if self.failed:
                                    return retval


                            else:
                                break #loop216


                        char_literal443 = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_bitwiseANDExpressionNoIn2766)
                        if self.failed:
                            return retval

                        char_literal443_tree = self.adaptor.createWithPayload(char_literal443)
                        self.adaptor.addChild(root_0, char_literal443_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:39: ( LT )*
                        while True: #loop217
                            alt217 = 2
                            LA217_0 = self.input.LA(1)

                            if (LA217_0 == LT) :
                                LA217_2 = self.input.LA(2)

                                if (self.synpred263()) :
                                    alt217 = 1




                            if alt217 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT444 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2768)
                                if self.failed:
                                    return retval


                            else:
                                break #loop217


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2772)
                        equalityExpressionNoIn445 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn445.tree)


                    else:
                        break #loop218





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 79, bitwiseANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpressionNoIn

    class equalityExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        LT447 = None
        set448 = None
        LT449 = None
        relationalExpression446 = None

        relationalExpression450 = None


        LT447_tree = None
        set448_tree = None
        LT449_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2786)
                relationalExpression446 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression446.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop221
                    alt221 = 2
                    alt221 = self.dfa221.predict(self.input)
                    if alt221 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:28: ( LT )*
                        while True: #loop219
                            alt219 = 2
                            LA219_0 = self.input.LA(1)

                            if (LA219_0 == LT) :
                                alt219 = 1


                            if alt219 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT447 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2789)
                                if self.failed:
                                    return retval


                            else:
                                break #loop219


                        set448 = self.input.LT(1)
                        if (118 <= self.input.LA(1) <= 121):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set448))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2793
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:63: ( LT )*
                        while True: #loop220
                            alt220 = 2
                            LA220_0 = self.input.LA(1)

                            if (LA220_0 == LT) :
                                LA220_2 = self.input.LA(2)

                                if (self.synpred269()) :
                                    alt220 = 1




                            if alt220 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT449 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2809)
                                if self.failed:
                                    return retval


                            else:
                                break #loop220


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2813)
                        relationalExpression450 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression450.tree)


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
                self.memoize(self.input, 80, equalityExpression_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpression

    class equalityExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
    def equalityExpressionNoIn(self, ):

        retval = self.equalityExpressionNoIn_return()
        retval.start = self.input.LT(1)
        equalityExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT452 = None
        set453 = None
        LT454 = None
        relationalExpressionNoIn451 = None

        relationalExpressionNoIn455 = None


        LT452_tree = None
        set453_tree = None
        LT454_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2826)
                relationalExpressionNoIn451 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn451.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop224
                    alt224 = 2
                    alt224 = self.dfa224.predict(self.input)
                    if alt224 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:32: ( LT )*
                        while True: #loop222
                            alt222 = 2
                            LA222_0 = self.input.LA(1)

                            if (LA222_0 == LT) :
                                alt222 = 1


                            if alt222 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT452 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2829)
                                if self.failed:
                                    return retval


                            else:
                                break #loop222


                        set453 = self.input.LT(1)
                        if (118 <= self.input.LA(1) <= 121):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set453))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn2833
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:67: ( LT )*
                        while True: #loop223
                            alt223 = 2
                            LA223_0 = self.input.LA(1)

                            if (LA223_0 == LT) :
                                LA223_2 = self.input.LA(2)

                                if (self.synpred275()) :
                                    alt223 = 1




                            if alt223 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT454 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2849)
                                if self.failed:
                                    return retval


                            else:
                                break #loop223


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2853)
                        relationalExpressionNoIn455 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn455.tree)


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
                self.memoize(self.input, 81, equalityExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpressionNoIn

    class relationalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LT457 = None
        set458 = None
        LT459 = None
        shiftExpression456 = None

        shiftExpression460 = None


        LT457_tree = None
        set458_tree = None
        LT459_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2867)
                shiftExpression456 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression456.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop227
                    alt227 = 2
                    LA227_0 = self.input.LA(1)

                    if (LA227_0 == LT) :
                        LA227_1 = self.input.LA(2)

                        if (self.synpred284()) :
                            alt227 = 1


                    elif ((60 <= LA227_0 <= 61) or LA227_0 == 86 or (122 <= LA227_0 <= 124)) :
                        alt227 = 1


                    if alt227 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:23: ( LT )*
                        while True: #loop225
                            alt225 = 2
                            LA225_0 = self.input.LA(1)

                            if (LA225_0 == LT) :
                                alt225 = 1


                            if alt225 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT457 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2870)
                                if self.failed:
                                    return retval


                            else:
                                break #loop225


                        set458 = self.input.LT(1)
                        if (60 <= self.input.LA(1) <= 61) or self.input.LA(1) == 86 or (122 <= self.input.LA(1) <= 124):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set458))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpression2874
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:76: ( LT )*
                        while True: #loop226
                            alt226 = 2
                            LA226_0 = self.input.LA(1)

                            if (LA226_0 == LT) :
                                LA226_2 = self.input.LA(2)

                                if (self.synpred283()) :
                                    alt226 = 1




                            if alt226 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT459 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2898)
                                if self.failed:
                                    return retval


                            else:
                                break #loop226


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2902)
                        shiftExpression460 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression460.tree)


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
                self.memoize(self.input, 82, relationalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpression

    class relationalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
    def relationalExpressionNoIn(self, ):

        retval = self.relationalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        relationalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT462 = None
        set463 = None
        LT464 = None
        shiftExpression461 = None

        shiftExpression465 = None


        LT462_tree = None
        set463_tree = None
        LT464_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2915)
                shiftExpression461 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression461.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop230
                    alt230 = 2
                    alt230 = self.dfa230.predict(self.input)
                    if alt230 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:23: ( LT )*
                        while True: #loop228
                            alt228 = 2
                            LA228_0 = self.input.LA(1)

                            if (LA228_0 == LT) :
                                alt228 = 1


                            if alt228 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT462 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2918)
                                if self.failed:
                                    return retval


                            else:
                                break #loop228


                        set463 = self.input.LT(1)
                        if (60 <= self.input.LA(1) <= 61) or (122 <= self.input.LA(1) <= 124):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set463))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn2922
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:69: ( LT )*
                        while True: #loop229
                            alt229 = 2
                            LA229_0 = self.input.LA(1)

                            if (LA229_0 == LT) :
                                LA229_2 = self.input.LA(2)

                                if (self.synpred290()) :
                                    alt229 = 1




                            if alt229 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT464 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2942)
                                if self.failed:
                                    return retval


                            else:
                                break #loop229


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2946)
                        shiftExpression465 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression465.tree)


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
                self.memoize(self.input, 83, relationalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpressionNoIn

    class shiftExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start shiftExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        LT467 = None
        set468 = None
        LT469 = None
        additiveExpression466 = None

        additiveExpression470 = None


        LT467_tree = None
        set468_tree = None
        LT469_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2959)
                additiveExpression466 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression466.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop233
                    alt233 = 2
                    alt233 = self.dfa233.predict(self.input)
                    if alt233 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:26: ( LT )*
                        while True: #loop231
                            alt231 = 2
                            LA231_0 = self.input.LA(1)

                            if (LA231_0 == LT) :
                                alt231 = 1


                            if alt231 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT467 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2962)
                                if self.failed:
                                    return retval


                            else:
                                break #loop231


                        set468 = self.input.LT(1)
                        if (125 <= self.input.LA(1) <= 127):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set468))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_shiftExpression2966
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:53: ( LT )*
                        while True: #loop232
                            alt232 = 2
                            LA232_0 = self.input.LA(1)

                            if (LA232_0 == LT) :
                                LA232_2 = self.input.LA(2)

                                if (self.synpred295()) :
                                    alt232 = 1




                            if alt232 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT469 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2978)
                                if self.failed:
                                    return retval


                            else:
                                break #loop232


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2982)
                        additiveExpression470 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression470.tree)


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
                self.memoize(self.input, 84, shiftExpression_StartIndex)

            pass

        return retval

    # $ANTLR end shiftExpression

    class additiveExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start additiveExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        LT472 = None
        set473 = None
        LT474 = None
        multiplicativeExpression471 = None

        multiplicativeExpression475 = None


        LT472_tree = None
        set473_tree = None
        LT474_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 85):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2995)
                multiplicativeExpression471 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression471.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop236
                    alt236 = 2
                    LA236_0 = self.input.LA(1)

                    if (LA236_0 == LT) :
                        LA236_1 = self.input.LA(2)

                        if (self.synpred300()) :
                            alt236 = 1


                    elif (LA236_0 == 64 or LA236_0 == 128) :
                        alt236 = 1


                    if alt236 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:32: ( LT )*
                        while True: #loop234
                            alt234 = 2
                            LA234_0 = self.input.LA(1)

                            if (LA234_0 == LT) :
                                alt234 = 1


                            if alt234 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT472 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2998)
                                if self.failed:
                                    return retval


                            else:
                                break #loop234


                        set473 = self.input.LT(1)
                        if self.input.LA(1) == 64 or self.input.LA(1) == 128:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set473))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_additiveExpression3002
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:49: ( LT )*
                        while True: #loop235
                            alt235 = 2
                            LA235_0 = self.input.LA(1)

                            if (LA235_0 == LT) :
                                LA235_2 = self.input.LA(2)

                                if (self.synpred299()) :
                                    alt235 = 1




                            if alt235 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT474 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression3010)
                                if self.failed:
                                    return retval


                            else:
                                break #loop235


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression3014)
                        multiplicativeExpression475 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression475.tree)


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
                self.memoize(self.input, 85, additiveExpression_StartIndex)

            pass

        return retval

    # $ANTLR end additiveExpression

    class multiplicativeExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start multiplicativeExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:474:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        LT477 = None
        set478 = None
        LT479 = None
        unaryExpression476 = None

        unaryExpression480 = None


        LT477_tree = None
        set478_tree = None
        LT479_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 86):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression3027)
                unaryExpression476 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression476.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop239
                    alt239 = 2
                    LA239_0 = self.input.LA(1)

                    if (LA239_0 == LT) :
                        LA239_1 = self.input.LA(2)

                        if (self.synpred305()) :
                            alt239 = 1


                    elif (LA239_0 == 62 or LA239_0 == 100 or LA239_0 == 129) :
                        alt239 = 1


                    if alt239 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:23: ( LT )*
                        while True: #loop237
                            alt237 = 2
                            LA237_0 = self.input.LA(1)

                            if (LA237_0 == LT) :
                                alt237 = 1


                            if alt237 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT477 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression3030)
                                if self.failed:
                                    return retval


                            else:
                                break #loop237


                        set478 = self.input.LT(1)
                        if self.input.LA(1) == 62 or self.input.LA(1) == 100 or self.input.LA(1) == 129:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set478))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression3034
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:46: ( LT )*
                        while True: #loop238
                            alt238 = 2
                            LA238_0 = self.input.LA(1)

                            if (LA238_0 == LT) :
                                LA238_2 = self.input.LA(2)

                                if (self.synpred304()) :
                                    alt238 = 1




                            if alt238 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT479 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression3046)
                                if self.failed:
                                    return retval


                            else:
                                break #loop238


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression3050)
                        unaryExpression480 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression480.tree)


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
                self.memoize(self.input, 86, multiplicativeExpression_StartIndex)

            pass

        return retval

    # $ANTLR end multiplicativeExpression

    class unaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start unaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set482 = None
        postfixExpression481 = None

        unaryExpression483 = None


        set482_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 87):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:479:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt240 = 2
                LA240_0 = self.input.LA(1)

                if ((LT <= LA240_0 <= RegularExpressionHacks) or LA240_0 == 60 or LA240_0 == 62 or LA240_0 == 66 or (68 <= LA240_0 <= 69) or (72 <= LA240_0 <= 74) or LA240_0 == 85 or LA240_0 == 96 or LA240_0 == 98 or (137 <= LA240_0 <= 142)) :
                    alt240 = 1
                elif (LA240_0 == 64 or LA240_0 == 128 or (130 <= LA240_0 <= 136)) :
                    alt240 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("478:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 240, 0, self.input)

                    raise nvae

                if alt240 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:479:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression3063)
                    postfixExpression481 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression481.tree)


                elif alt240 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:480:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set482 = self.input.LT(1)
                    if self.input.LA(1) == 64 or self.input.LA(1) == 128 or (130 <= self.input.LA(1) <= 136):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set482))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_unaryExpression3068
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression3104)
                    unaryExpression483 = self.unaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unaryExpression483.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 87, unaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end unaryExpression

    class postfixExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start postfixExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set485 = None
        leftHandSideExpression484 = None


        set485_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 88):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:484:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:484:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression3116)
                leftHandSideExpression484 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression484.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:484:27: ( '++' | '--' )?
                alt241 = 2
                LA241_0 = self.input.LA(1)

                if ((133 <= LA241_0 <= 134)) :
                    alt241 = 1
                if alt241 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set485 = self.input.LT(1)
                    if (133 <= self.input.LA(1) <= 134):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set485))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_postfixExpression3118
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
                self.memoize(self.input, 88, postfixExpression_StartIndex)

            pass

        return retval

    # $ANTLR end postfixExpression

    class primaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start primaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:487:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal486 = None
        char_literal492 = None
        LT493 = None
        LT495 = None
        char_literal496 = None
        xmlLiteral487 = None

        identifier488 = None

        literal489 = None

        arrayLiteral490 = None

        objectLiteral491 = None

        expression494 = None


        string_literal486_tree = None
        char_literal492_tree = None
        LT493_tree = None
        LT495_tree = None
        char_literal496_tree = None
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 89):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:2: ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt244 = 7
                LA244_0 = self.input.LA(1)

                if (LA244_0 == 137) :
                    alt244 = 1
                elif (LA244_0 == LT) and (self.synpred320()):
                    alt244 = 2
                elif (LA244_0 == 60) and (self.synpred320()):
                    alt244 = 2
                elif (LA244_0 == 66) :
                    LA244_4 = self.input.LA(2)

                    if (self.synpred320()) :
                        alt244 = 2
                    elif (self.synpred324()) :
                        alt244 = 6
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("487:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 244, 4, self.input)

                        raise nvae

                elif (LA244_0 == XMLComment) and (self.synpred320()):
                    alt244 = 2
                elif (LA244_0 == Identifier or (72 <= LA244_0 <= 74) or LA244_0 == 85 or (138 <= LA244_0 <= 139)) :
                    alt244 = 3
                elif (LA244_0 == StringLiteral or LA244_0 == NumericLiteral or LA244_0 == RegularExpressionHacks or LA244_0 == 62 or (140 <= LA244_0 <= 142)) :
                    alt244 = 4
                elif (LA244_0 == 98) :
                    alt244 = 5
                elif (LA244_0 == 69) :
                    alt244 = 7
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("487:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier -> ^( VARREF identifier ) | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 244, 0, self.input)

                    raise nvae

                if alt244 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal486 = self.input.LT(1)
                    self.match(self.input, 137, self.FOLLOW_137_in_primaryExpression3136)
                    if self.failed:
                        return retval

                    string_literal486_tree = self.adaptor.createWithPayload(string_literal486)
                    self.adaptor.addChild(root_0, string_literal486_tree)



                elif alt244 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:4: ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlLiteral_in_primaryExpression3153)
                    xmlLiteral487 = self.xmlLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlLiteral487.tree)


                elif alt244 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:4: identifier
                    self.following.append(self.FOLLOW_identifier_in_primaryExpression3158)
                    identifier488 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier488.tree)
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
                        # 491:3: -> ^( VARREF identifier )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:491:6: ^( VARREF identifier )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARREF, "VARREF"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt244 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression3173)
                    literal489 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal489.tree)


                elif alt244 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:493:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression3178)
                    arrayLiteral490 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral490.tree)


                elif alt244 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:494:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression3183)
                    objectLiteral491 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral491.tree)


                elif alt244 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal492 = self.input.LT(1)
                    self.match(self.input, 69, self.FOLLOW_69_in_primaryExpression3188)
                    if self.failed:
                        return retval

                    char_literal492_tree = self.adaptor.createWithPayload(char_literal492)
                    self.adaptor.addChild(root_0, char_literal492_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:10: ( LT )*
                    while True: #loop242
                        alt242 = 2
                        LA242_0 = self.input.LA(1)

                        if (LA242_0 == LT) :
                            LA242_2 = self.input.LA(2)

                            if (self.synpred325()) :
                                alt242 = 1




                        if alt242 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT493 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3190)
                            if self.failed:
                                return retval


                        else:
                            break #loop242


                    self.following.append(self.FOLLOW_expression_in_primaryExpression3194)
                    expression494 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression494.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:26: ( LT )*
                    while True: #loop243
                        alt243 = 2
                        LA243_0 = self.input.LA(1)

                        if (LA243_0 == LT) :
                            alt243 = 1


                        if alt243 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT495 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3196)
                            if self.failed:
                                return retval


                        else:
                            break #loop243


                    char_literal496 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_primaryExpression3200)
                    if self.failed:
                        return retval

                    char_literal496_tree = self.adaptor.createWithPayload(char_literal496)
                    self.adaptor.addChild(root_0, char_literal496_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 89, primaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end primaryExpression

    class arrayLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arrayLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:499:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' -> ^( ARRAY ( assignmentExpression )* ) ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal497 = None
        LT498 = None
        LT500 = None
        char_literal501 = None
        LT502 = None
        LT504 = None
        char_literal505 = None
        LT506 = None
        char_literal507 = None
        assignmentExpression499 = None

        assignmentExpression503 = None


        char_literal497_tree = None
        LT498_tree = None
        LT500_tree = None
        char_literal501_tree = None
        LT502_tree = None
        LT504_tree = None
        char_literal505_tree = None
        LT506_tree = None
        char_literal507_tree = None
        stream_98 = RewriteRuleTokenStream(self.adaptor, "token 98")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_99 = RewriteRuleTokenStream(self.adaptor, "token 99")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 90):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' -> ^( ARRAY ( assignmentExpression )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']'
                char_literal497 = self.input.LT(1)
                self.match(self.input, 98, self.FOLLOW_98_in_arrayLiteral3213)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_98.add(char_literal497)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:8: ( LT )*
                while True: #loop245
                    alt245 = 2
                    LA245_0 = self.input.LA(1)

                    if (LA245_0 == LT) :
                        LA245_2 = self.input.LA(2)

                        if (self.synpred327()) :
                            alt245 = 1




                    if alt245 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT498 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3215)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT498)


                    else:
                        break #loop245


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:12: ( assignmentExpression )?
                alt246 = 2
                alt246 = self.dfa246.predict(self.input)
                if alt246 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3218)
                    assignmentExpression499 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression499.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:34: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop250
                    alt250 = 2
                    alt250 = self.dfa250.predict(self.input)
                    if alt250 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:35: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:35: ( LT )*
                        while True: #loop247
                            alt247 = 2
                            LA247_0 = self.input.LA(1)

                            if (LA247_0 == LT) :
                                alt247 = 1


                            if alt247 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT500 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3222)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT500)


                            else:
                                break #loop247


                        char_literal501 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_arrayLiteral3225)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal501)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:43: ( ( LT )* assignmentExpression )?
                        alt249 = 2
                        alt249 = self.dfa249.predict(self.input)
                        if alt249 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: ( LT )*
                            while True: #loop248
                                alt248 = 2
                                LA248_0 = self.input.LA(1)

                                if (LA248_0 == LT) :
                                    LA248_2 = self.input.LA(2)

                                    if (self.synpred330()) :
                                        alt248 = 1




                                if alt248 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT502 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3228)
                                    if self.failed:
                                        return retval
                                    if self.backtracking == 0:
                                        stream_LT.add(LT502)


                                else:
                                    break #loop248


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3231)
                            assignmentExpression503 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_assignmentExpression.add(assignmentExpression503.tree)





                    else:
                        break #loop250


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:73: ( LT )*
                while True: #loop251
                    alt251 = 2
                    LA251_0 = self.input.LA(1)

                    if (LA251_0 == LT) :
                        alt251 = 1


                    if alt251 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT504 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3237)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT504)


                    else:
                        break #loop251


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:77: ( ',' ( LT )* )?
                alt253 = 2
                LA253_0 = self.input.LA(1)

                if (LA253_0 == 70) :
                    alt253 = 1
                if alt253 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:78: ',' ( LT )*
                    char_literal505 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_arrayLiteral3241)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_70.add(char_literal505)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:82: ( LT )*
                    while True: #loop252
                        alt252 = 2
                        LA252_0 = self.input.LA(1)

                        if (LA252_0 == LT) :
                            alt252 = 1


                        if alt252 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT506 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3243)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT506)


                        else:
                            break #loop252





                char_literal507 = self.input.LT(1)
                self.match(self.input, 99, self.FOLLOW_99_in_arrayLiteral3248)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_99.add(char_literal507)
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
                    # 501:3: -> ^( ARRAY ( assignmentExpression )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:501:6: ^( ARRAY ( assignmentExpression )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(ARRAY, "ARRAY"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:501:14: ( assignmentExpression )*
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
                self.memoize(self.input, 90, arrayLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end arrayLiteral

    class objectLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start objectLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:505:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal508 = None
        LT509 = None
        LT511 = None
        char_literal512 = None
        LT513 = None
        LT515 = None
        char_literal516 = None
        LT517 = None
        char_literal518 = None
        propertyNameAndValue510 = None

        propertyNameAndValue514 = None


        char_literal508_tree = None
        LT509_tree = None
        LT511_tree = None
        char_literal512_tree = None
        LT513_tree = None
        LT515_tree = None
        char_literal516_tree = None
        LT517_tree = None
        char_literal518_tree = None
        stream_67 = RewriteRuleTokenStream(self.adaptor, "token 67")
        stream_66 = RewriteRuleTokenStream(self.adaptor, "token 66")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_70 = RewriteRuleTokenStream(self.adaptor, "token 70")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 91):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}'
                char_literal508 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_objectLiteral3278)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_66.add(char_literal508)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:8: ( LT )*
                while True: #loop254
                    alt254 = 2
                    LA254_0 = self.input.LA(1)

                    if (LA254_0 == LT) :
                        LA254_2 = self.input.LA(2)

                        if (self.synpred336()) :
                            alt254 = 1




                    if alt254 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT509 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3280)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT509)


                    else:
                        break #loop254


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:12: ( propertyNameAndValue )?
                alt255 = 2
                LA255_0 = self.input.LA(1)

                if (LA255_0 == StringLiteral or (NumericLiteral <= LA255_0 <= Identifier) or (72 <= LA255_0 <= 74) or LA255_0 == 85 or (138 <= LA255_0 <= 139)) :
                    alt255 = 1
                if alt255 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3283)
                    propertyNameAndValue510 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue510.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop258
                    alt258 = 2
                    alt258 = self.dfa258.predict(self.input)
                    if alt258 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:35: ( LT )*
                        while True: #loop256
                            alt256 = 2
                            LA256_0 = self.input.LA(1)

                            if (LA256_0 == LT) :
                                alt256 = 1


                            if alt256 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT511 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3287)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT511)


                            else:
                                break #loop256


                        char_literal512 = self.input.LT(1)
                        self.match(self.input, 70, self.FOLLOW_70_in_objectLiteral3290)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_70.add(char_literal512)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:43: ( LT )*
                        while True: #loop257
                            alt257 = 2
                            LA257_0 = self.input.LA(1)

                            if (LA257_0 == LT) :
                                alt257 = 1


                            if alt257 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT513 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3292)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT513)


                            else:
                                break #loop257


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3295)
                        propertyNameAndValue514 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue514.tree)


                    else:
                        break #loop258


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:70: ( LT )*
                while True: #loop259
                    alt259 = 2
                    LA259_0 = self.input.LA(1)

                    if (LA259_0 == LT) :
                        alt259 = 1


                    if alt259 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT515 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3299)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT515)


                    else:
                        break #loop259


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:74: ( ',' ( LT )* )?
                alt261 = 2
                LA261_0 = self.input.LA(1)

                if (LA261_0 == 70) :
                    alt261 = 1
                if alt261 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:75: ',' ( LT )*
                    char_literal516 = self.input.LT(1)
                    self.match(self.input, 70, self.FOLLOW_70_in_objectLiteral3303)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_70.add(char_literal516)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:79: ( LT )*
                    while True: #loop260
                        alt260 = 2
                        LA260_0 = self.input.LA(1)

                        if (LA260_0 == LT) :
                            alt260 = 1


                        if alt260 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT517 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3305)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT517)


                        else:
                            break #loop260





                char_literal518 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_objectLiteral3310)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_67.add(char_literal518)
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
                    # 507:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:507:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:507:12: ( propertyNameAndValue )*
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
                self.memoize(self.input, 91, objectLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end objectLiteral

    class propertyNameAndValue_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyNameAndValue
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:510:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        action = None
        LT520 = None
        char_literal521 = None
        LT522 = None
        LT524 = None
        LT525 = None
        LT527 = None
        LT529 = None
        LT530 = None
        LT532 = None
        propname = None

        funcname = None

        propertyName519 = None

        assignmentExpression523 = None

        formalParameterList526 = None

        statementBlock528 = None

        formalParameterList531 = None

        statementBlock533 = None


        action_tree = None
        LT520_tree = None
        char_literal521_tree = None
        LT522_tree = None
        LT524_tree = None
        LT525_tree = None
        LT527_tree = None
        LT529_tree = None
        LT530_tree = None
        LT532_tree = None
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 92):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) )
                alt272 = 3
                alt272 = self.dfa272.predict(self.input)
                if alt272 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue3334)
                    propertyName519 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName519.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:17: ( LT )*
                    while True: #loop262
                        alt262 = 2
                        LA262_0 = self.input.LA(1)

                        if (LA262_0 == LT) :
                            alt262 = 1


                        if alt262 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT520 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3336)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT520)


                        else:
                            break #loop262


                    char_literal521 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_propertyNameAndValue3339)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_63.add(char_literal521)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:25: ( LT )*
                    while True: #loop263
                        alt263 = 2
                        LA263_0 = self.input.LA(1)

                        if (LA263_0 == LT) :
                            LA263_2 = self.input.LA(2)

                            if (self.synpred345()) :
                                alt263 = 1




                        if alt263 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT522 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3341)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT522)


                        else:
                            break #loop263


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue3344)
                    assignmentExpression523 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression523.tree)
                    # AST Rewrite
                    # elements: assignmentExpression, propertyName
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
                        # 512:3: -> ^( PROP propertyName PROP assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:512:6: ^( PROP propertyName PROP assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, self.adaptor.createFromType(PROP, "PROP"))
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt272 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:4: (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:4: (action= 'get' | action= 'set' )
                    alt264 = 2
                    LA264_0 = self.input.LA(1)

                    if (LA264_0 == 138) :
                        alt264 = 1
                    elif (LA264_0 == 139) :
                        alt264 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("513:4: (action= 'get' | action= 'set' )", 264, 0, self.input)

                        raise nvae

                    if alt264 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 138, self.FOLLOW_138_in_propertyNameAndValue3366)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_138.add(action)


                    elif alt264 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 139, self.FOLLOW_139_in_propertyNameAndValue3370)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_139.add(action)



                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3375)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:52: ( LT )*
                    while True: #loop265
                        alt265 = 2
                        LA265_0 = self.input.LA(1)

                        if (LA265_0 == LT) :
                            alt265 = 1


                        if alt265 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT524 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3377)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT524)


                        else:
                            break #loop265


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3382)
                    funcname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(funcname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:76: ( LT )*
                    while True: #loop266
                        alt266 = 2
                        LA266_0 = self.input.LA(1)

                        if (LA266_0 == LT) :
                            alt266 = 1


                        if alt266 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT525 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3384)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT525)


                        else:
                            break #loop266


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3387)
                    formalParameterList526 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList526.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:513:100: ( LT )*
                    while True: #loop267
                        alt267 = 2
                        LA267_0 = self.input.LA(1)

                        if (LA267_0 == LT) :
                            alt267 = 1


                        if alt267 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT527 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3389)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT527)


                        else:
                            break #loop267


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3392)
                    statementBlock528 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock528.tree)
                    # AST Rewrite
                    # elements: statementBlock, propname, formalParameterList, action, funcname
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
                        # 514:3: -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:514:6: ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:514:31: ^( FUNC $funcname formalParameterList statementBlock )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_funcname.next())
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_statementBlock.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                elif alt272 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:4: (action= 'get' | action= 'set' ) ( LT )* propname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:4: (action= 'get' | action= 'set' )
                    alt268 = 2
                    LA268_0 = self.input.LA(1)

                    if (LA268_0 == 138) :
                        alt268 = 1
                    elif (LA268_0 == 139) :
                        alt268 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("515:4: (action= 'get' | action= 'set' )", 268, 0, self.input)

                        raise nvae

                    if alt268 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 138, self.FOLLOW_138_in_propertyNameAndValue3425)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_138.add(action)


                    elif alt268 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 139, self.FOLLOW_139_in_propertyNameAndValue3429)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_139.add(action)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:32: ( LT )*
                    while True: #loop269
                        alt269 = 2
                        LA269_0 = self.input.LA(1)

                        if (LA269_0 == LT) :
                            alt269 = 1


                        if alt269 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT529 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3432)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT529)


                        else:
                            break #loop269


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3437)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:56: ( LT )*
                    while True: #loop270
                        alt270 = 2
                        LA270_0 = self.input.LA(1)

                        if (LA270_0 == LT) :
                            alt270 = 1


                        if alt270 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT530 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3439)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT530)


                        else:
                            break #loop270


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3442)
                    formalParameterList531 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList531.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:515:80: ( LT )*
                    while True: #loop271
                        alt271 = 2
                        LA271_0 = self.input.LA(1)

                        if (LA271_0 == LT) :
                            alt271 = 1


                        if alt271 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT532 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3444)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT532)


                        else:
                            break #loop271


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3447)
                    statementBlock533 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock533.tree)
                    # AST Rewrite
                    # elements: statementBlock, propname, action, formalParameterList
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
                        # 516:3: -> ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:516:6: ^( PROP $propname $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:516:31: ^( FUNC ANONYMOUS formalParameterList statementBlock )
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
                self.memoize(self.input, 92, propertyNameAndValue_StartIndex)

            pass

        return retval

    # $ANTLR end propertyNameAndValue

    class propertyName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:519:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral535 = None
        NumericLiteral536 = None
        identifier534 = None


        StringLiteral535_tree = None
        NumericLiteral536_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 93):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:520:2: ( identifier | StringLiteral | NumericLiteral )
                alt273 = 3
                LA273 = self.input.LA(1)
                if LA273 == Identifier or LA273 == 72 or LA273 == 73 or LA273 == 74 or LA273 == 85 or LA273 == 138 or LA273 == 139:
                    alt273 = 1
                elif LA273 == StringLiteral:
                    alt273 = 2
                elif LA273 == NumericLiteral:
                    alt273 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("519:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 273, 0, self.input)

                    raise nvae

                if alt273 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:520:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName3482)
                    identifier534 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier534.tree)


                elif alt273 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:521:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral535 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName3487)
                    if self.failed:
                        return retval

                    StringLiteral535_tree = self.adaptor.createWithPayload(StringLiteral535)
                    self.adaptor.addChild(root_0, StringLiteral535_tree)



                elif alt273 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:522:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral536 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName3492)
                    if self.failed:
                        return retval

                    NumericLiteral536_tree = self.adaptor.createWithPayload(NumericLiteral536)
                    self.adaptor.addChild(root_0, NumericLiteral536_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 93, propertyName_StartIndex)

            pass

        return retval

    # $ANTLR end propertyName

    class literal_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start literal
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:526:1: literal : ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        string_literal537 = None
        string_literal538 = None
        string_literal539 = None
        StringLiteral540 = None
        NumericLiteral541 = None
        regularExpressionLiteral542 = None


        string_literal537_tree = None
        string_literal538_tree = None
        string_literal539_tree = None
        StringLiteral540_tree = None
        NumericLiteral541_tree = None
        stream_StringLiteral = RewriteRuleTokenStream(self.adaptor, "token StringLiteral")
        stream_NumericLiteral = RewriteRuleTokenStream(self.adaptor, "token NumericLiteral")
        stream_140 = RewriteRuleTokenStream(self.adaptor, "token 140")
        stream_142 = RewriteRuleTokenStream(self.adaptor, "token 142")
        stream_141 = RewriteRuleTokenStream(self.adaptor, "token 141")
        stream_regularExpressionLiteral = RewriteRuleSubtreeStream(self.adaptor, "rule regularExpressionLiteral")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 94):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:527:2: ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) )
                alt274 = 6
                LA274 = self.input.LA(1)
                if LA274 == 140:
                    alt274 = 1
                elif LA274 == 141:
                    alt274 = 2
                elif LA274 == 142:
                    alt274 = 3
                elif LA274 == StringLiteral:
                    alt274 = 4
                elif LA274 == NumericLiteral:
                    alt274 = 5
                elif LA274 == RegularExpressionHacks or LA274 == 62:
                    alt274 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("526:1: literal : ( 'null' -> NULL | 'true' -> TRUE | 'false' -> FALSE | StringLiteral -> ^( STRING StringLiteral ) | NumericLiteral -> ^( NUMBER NumericLiteral ) | regularExpressionLiteral -> ^( REGEX regularExpressionLiteral ) );", 274, 0, self.input)

                    raise nvae

                if alt274 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:527:4: 'null'
                    string_literal537 = self.input.LT(1)
                    self.match(self.input, 140, self.FOLLOW_140_in_literal3504)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_140.add(string_literal537)
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
                        # 527:11: -> NULL
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(NULL, "NULL"))





                elif alt274 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:528:4: 'true'
                    string_literal538 = self.input.LT(1)
                    self.match(self.input, 141, self.FOLLOW_141_in_literal3513)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_141.add(string_literal538)
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
                        # 528:11: -> TRUE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(TRUE, "TRUE"))





                elif alt274 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:529:4: 'false'
                    string_literal539 = self.input.LT(1)
                    self.match(self.input, 142, self.FOLLOW_142_in_literal3522)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_142.add(string_literal539)
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
                        # 529:12: -> FALSE
                        self.adaptor.addChild(root_0, self.adaptor.createFromType(FALSE, "FALSE"))





                elif alt274 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:530:4: StringLiteral
                    StringLiteral540 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_literal3531)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_StringLiteral.add(StringLiteral540)
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
                        # 530:18: -> ^( STRING StringLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:530:21: ^( STRING StringLiteral )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(STRING, "STRING"), root_1)

                        self.adaptor.addChild(root_1, stream_StringLiteral.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt274 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:531:4: NumericLiteral
                    NumericLiteral541 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_literal3544)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_NumericLiteral.add(NumericLiteral541)
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
                        # 531:19: -> ^( NUMBER NumericLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:531:22: ^( NUMBER NumericLiteral )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NUMBER, "NUMBER"), root_1)

                        self.adaptor.addChild(root_1, stream_NumericLiteral.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt274 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:532:4: regularExpressionLiteral
                    self.following.append(self.FOLLOW_regularExpressionLiteral_in_literal3557)
                    regularExpressionLiteral542 = self.regularExpressionLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_regularExpressionLiteral.add(regularExpressionLiteral542.tree)
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
                        # 532:29: -> ^( REGEX regularExpressionLiteral )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:532:32: ^( REGEX regularExpressionLiteral )
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
                self.memoize(self.input, 94, literal_StartIndex)

            pass

        return retval

    # $ANTLR end literal

    class reFirstChar_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reFirstChar
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:542:1: reFirstChar : ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'let' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier );
    def reFirstChar(self, ):

        retval = self.reFirstChar_return()
        retval.start = self.input.LT(1)
        reFirstChar_StartIndex = self.input.index()
        root_0 = None

        set543 = None

        set543_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 95):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:543:2: ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'let' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set543 = self.input.LT(1)
                if self.input.LA(1) == StringLiteral or (NumericLiteral <= self.input.LA(1) <= Identifier) or (60 <= self.input.LA(1) <= 61) or (63 <= self.input.LA(1) <= 99) or (101 <= self.input.LA(1) <= 117) or (122 <= self.input.LA(1) <= 143):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set543))
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
                self.memoize(self.input, 95, reFirstChar_StartIndex)

            pass

        return retval

    # $ANTLR end reFirstChar

    class reChars_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reChars
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:561:1: reChars : ( reFirstChar | '*' );
    def reChars(self, ):

        retval = self.reChars_return()
        retval.start = self.input.LT(1)
        reChars_StartIndex = self.input.index()
        root_0 = None

        char_literal545 = None
        reFirstChar544 = None


        char_literal545_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 96):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:562:2: ( reFirstChar | '*' )
                alt275 = 2
                LA275_0 = self.input.LA(1)

                if (LA275_0 == StringLiteral or (NumericLiteral <= LA275_0 <= Identifier) or (60 <= LA275_0 <= 61) or (63 <= LA275_0 <= 99) or (101 <= LA275_0 <= 117) or (122 <= LA275_0 <= 143)) :
                    alt275 = 1
                elif (LA275_0 == 100) :
                    alt275 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("561:1: reChars : ( reFirstChar | '*' );", 275, 0, self.input)

                    raise nvae

                if alt275 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:562:4: reFirstChar
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_reFirstChar_in_reChars3958)
                    reFirstChar544 = self.reFirstChar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, reFirstChar544.tree)


                elif alt275 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:563:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal545 = self.input.LT(1)
                    self.match(self.input, 100, self.FOLLOW_100_in_reChars3963)
                    if self.failed:
                        return retval

                    char_literal545_tree = self.adaptor.createWithPayload(char_literal545)
                    self.adaptor.addChild(root_0, char_literal545_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 96, reChars_StartIndex)

            pass

        return retval

    # $ANTLR end reChars

    class regularExpressionLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start regularExpressionLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:569:1: regularExpressionLiteral : ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal546 = None
        char_literal549 = None
        Identifier550 = None
        RegularExpressionHacks551 = None
        Identifier552 = None
        reFirstChar547 = None

        reChars548 = None


        char_literal546_tree = None
        char_literal549_tree = None
        Identifier550_tree = None
        RegularExpressionHacks551_tree = None
        Identifier552_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 97):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:2: ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? )
                alt280 = 2
                LA280_0 = self.input.LA(1)

                if (LA280_0 == 62) :
                    alt280 = 1
                elif (LA280_0 == RegularExpressionHacks) :
                    alt280 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("569:1: regularExpressionLiteral : ( '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );", 280, 0, self.input)

                    raise nvae

                if alt280 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:4: '/' ( reFirstChar )? ( reChars )* '/' ( Identifier )?
                    root_0 = self.adaptor.nil()

                    char_literal546 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_regularExpressionLiteral3977)
                    if self.failed:
                        return retval

                    char_literal546_tree = self.adaptor.createWithPayload(char_literal546)
                    self.adaptor.addChild(root_0, char_literal546_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:8: ( reFirstChar )?
                    alt276 = 2
                    LA276_0 = self.input.LA(1)

                    if (LA276_0 == StringLiteral or (NumericLiteral <= LA276_0 <= Identifier) or (60 <= LA276_0 <= 61) or (63 <= LA276_0 <= 99) or (101 <= LA276_0 <= 117) or (122 <= LA276_0 <= 143)) :
                        LA276_1 = self.input.LA(2)

                        if (self.synpred444()) :
                            alt276 = 1
                    if alt276 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reFirstChar
                        self.following.append(self.FOLLOW_reFirstChar_in_regularExpressionLiteral3979)
                        reFirstChar547 = self.reFirstChar()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, reFirstChar547.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:21: ( reChars )*
                    while True: #loop277
                        alt277 = 2
                        LA277_0 = self.input.LA(1)

                        if (LA277_0 == StringLiteral or (NumericLiteral <= LA277_0 <= Identifier) or (60 <= LA277_0 <= 61) or (63 <= LA277_0 <= 117) or (122 <= LA277_0 <= 143)) :
                            alt277 = 1


                        if alt277 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reChars
                            self.following.append(self.FOLLOW_reChars_in_regularExpressionLiteral3982)
                            reChars548 = self.reChars()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, reChars548.tree)


                        else:
                            break #loop277


                    char_literal549 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_regularExpressionLiteral3985)
                    if self.failed:
                        return retval

                    char_literal549_tree = self.adaptor.createWithPayload(char_literal549)
                    self.adaptor.addChild(root_0, char_literal549_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:34: ( Identifier )?
                    alt278 = 2
                    LA278_0 = self.input.LA(1)

                    if (LA278_0 == Identifier) :
                        alt278 = 1
                    if alt278 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier550 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral3987)
                        if self.failed:
                            return retval

                        Identifier550_tree = self.adaptor.createWithPayload(Identifier550)
                        self.adaptor.addChild(root_0, Identifier550_tree)






                elif alt280 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:571:4: RegularExpressionHacks ( Identifier )?
                    root_0 = self.adaptor.nil()

                    RegularExpressionHacks551 = self.input.LT(1)
                    self.match(self.input, RegularExpressionHacks, self.FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral3993)
                    if self.failed:
                        return retval

                    RegularExpressionHacks551_tree = self.adaptor.createWithPayload(RegularExpressionHacks551)
                    self.adaptor.addChild(root_0, RegularExpressionHacks551_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:571:27: ( Identifier )?
                    alt279 = 2
                    LA279_0 = self.input.LA(1)

                    if (LA279_0 == Identifier) :
                        alt279 = 1
                    if alt279 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier552 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral3995)
                        if self.failed:
                            return retval

                        Identifier552_tree = self.adaptor.createWithPayload(Identifier552)
                        self.adaptor.addChild(root_0, Identifier552_tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 97, regularExpressionLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end regularExpressionLiteral

    class identifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start identifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:576:1: identifier : ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set553 = None

        set553_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 98):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:577:2: ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set553 = self.input.LT(1)
                if self.input.LA(1) == Identifier or (72 <= self.input.LA(1) <= 74) or self.input.LA(1) == 85 or (138 <= self.input.LA(1) <= 139):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set553))
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
                self.memoize(self.input, 98, identifier_StartIndex)

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
        while True: #loop284
            alt284 = 2
            LA284_0 = self.input.LA(1)

            if (LA284_0 == LT) :
                alt284 = 1


            if alt284 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred22477)
                if self.failed:
                    return 


            else:
                break #loop284


        self.following.append(self.FOLLOW_xmlPayload_in_synpred22480)
        self.xmlPayload()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred22



    # $ANTLR start synpred38
    def synpred38_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred38658)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred38



    # $ANTLR start synpred41
    def synpred41_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred41673)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred41



    # $ANTLR start synpred48
    def synpred48_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred48708)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred48



    # $ANTLR start synpred55
    def synpred55_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred55784)
        if self.failed:
            return 


    # $ANTLR end synpred55



    # $ANTLR start synpred58
    def synpred58_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:4: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:4: '{' ( LT )* ( statementList )? ( LT )* '}'
        self.match(self.input, 66, self.FOLLOW_66_in_synpred58782)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:10: ( LT )*
        while True: #loop294
            alt294 = 2
            LA294_0 = self.input.LA(1)

            if (LA294_0 == LT) :
                LA294_2 = self.input.LA(2)

                if (self.synpred55()) :
                    alt294 = 1




            if alt294 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred58784)
                if self.failed:
                    return 


            else:
                break #loop294


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:13: ( statementList )?
        alt295 = 2
        alt295 = self.dfa295.predict(self.input)
        if alt295 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
            self.following.append(self.FOLLOW_statementList_in_synpred58788)
            self.statementList()
            self.following.pop()
            if self.failed:
                return 



        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:30: ( LT )*
        while True: #loop296
            alt296 = 2
            LA296_0 = self.input.LA(1)

            if (LA296_0 == LT) :
                alt296 = 1


            if alt296 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred58791)
                if self.failed:
                    return 


            else:
                break #loop296


        self.match(self.input, 67, self.FOLLOW_67_in_synpred58795)
        if self.failed:
            return 


    # $ANTLR end synpred58



    # $ANTLR start synpred60
    def synpred60_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:15: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:15: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred60823)
        if self.failed:
            return 


    # $ANTLR end synpred60



    # $ANTLR start synpred61
    def synpred61_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:15: ( ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:15: ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:17: ( LT )*
        while True: #loop297
            alt297 = 2
            LA297_0 = self.input.LA(1)

            if (LA297_0 == LT) :
                LA297_2 = self.input.LA(2)

                if (self.synpred60()) :
                    alt297 = 1




            if alt297 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred61823)
                if self.failed:
                    return 


            else:
                break #loop297


        self.following.append(self.FOLLOW_statement_in_synpred61827)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred61



    # $ANTLR start synpred76
    def synpred76_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred761011)
        if self.failed:
            return 


    # $ANTLR end synpred76



    # $ANTLR start synpred77
    def synpred77_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred771034)
        if self.failed:
            return 


    # $ANTLR end synpred77



    # $ANTLR start synpred80
    def synpred80_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:18: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:18: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred801096)
        if self.failed:
            return 


    # $ANTLR end synpred80



    # $ANTLR start synpred82
    def synpred82_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:43: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:43: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred821108)
        if self.failed:
            return 


    # $ANTLR end synpred82



    # $ANTLR start synpred84
    def synpred84_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:71: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:71: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred841121)
        if self.failed:
            return 


    # $ANTLR end synpred84



    # $ANTLR start synpred85
    def synpred85_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:61: ( LT )*
        while True: #loop304
            alt304 = 2
            LA304_0 = self.input.LA(1)

            if (LA304_0 == LT) :
                alt304 = 1


            if alt304 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred851115)
                if self.failed:
                    return 


            else:
                break #loop304


        self.match(self.input, 81, self.FOLLOW_81_in_synpred851119)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:73: ( LT )*
        while True: #loop305
            alt305 = 2
            LA305_0 = self.input.LA(1)

            if (LA305_0 == LT) :
                LA305_2 = self.input.LA(2)

                if (self.synpred84()) :
                    alt305 = 1




            if alt305 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred851121)
                if self.failed:
                    return 


            else:
                break #loop305


        self.following.append(self.FOLLOW_statement_in_synpred851125)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred85



    # $ANTLR start synpred88
    def synpred88_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred881149)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred88



    # $ANTLR start synpred89
    def synpred89_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred891168)
        if self.failed:
            return 


    # $ANTLR end synpred89



    # $ANTLR start synpred94
    def synpred94_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred941217)
        if self.failed:
            return 


    # $ANTLR end synpred94



    # $ANTLR start synpred96
    def synpred96_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:46: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:46: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred961229)
        if self.failed:
            return 


    # $ANTLR end synpred96



    # $ANTLR start synpred98
    def synpred98_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred981254)
        if self.failed:
            return 


    # $ANTLR end synpred98



    # $ANTLR start synpred101
    def synpred101_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1011269)
        if self.failed:
            return 


    # $ANTLR end synpred101



    # $ANTLR start synpred104
    def synpred104_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:93: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:93: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1041284)
        if self.failed:
            return 


    # $ANTLR end synpred104



    # $ANTLR start synpred107
    def synpred107_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:120: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:120: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1071298)
        if self.failed:
            return 


    # $ANTLR end synpred107



    # $ANTLR start synpred111
    def synpred111_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1111343)
        if self.failed:
            return 


    # $ANTLR end synpred111



    # $ANTLR start synpred114
    def synpred114_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:32: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:32: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1141356)
        if self.failed:
            return 


    # $ANTLR end synpred114



    # $ANTLR start synpred116
    def synpred116_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1161368)
        if self.failed:
            return 


    # $ANTLR end synpred116



    # $ANTLR start synpred118
    def synpred118_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:102: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:102: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1181380)
        if self.failed:
            return 


    # $ANTLR end synpred118



    # $ANTLR start synpred126
    def synpred126_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:13: ( expression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:13: expression
        self.following.append(self.FOLLOW_expression_in_synpred1261470)
        self.expression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred126



    # $ANTLR start synpred129
    def synpred129_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1291500)
        if self.failed:
            return 


    # $ANTLR end synpred129



    # $ANTLR start synpred131
    def synpred131_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:45: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:45: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1311512)
        if self.failed:
            return 


    # $ANTLR end synpred131



    # $ANTLR start synpred133
    def synpred133_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:24: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:24: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1331535)
        if self.failed:
            return 


    # $ANTLR end synpred133



    # $ANTLR start synpred135
    def synpred135_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:22: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:22: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1351559)
        if self.failed:
            return 


    # $ANTLR end synpred135



    # $ANTLR start synpred145
    def synpred145_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:11: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:11: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1451633)
        if self.failed:
            return 


    # $ANTLR end synpred145



    # $ANTLR start synpred147
    def synpred147_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1471645)
        if self.failed:
            return 


    # $ANTLR end synpred147



    # $ANTLR start synpred148
    def synpred148_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:41: ( statementList )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:41: statementList
        self.following.append(self.FOLLOW_statementList_in_synpred1481649)
        self.statementList()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred148



    # $ANTLR start synpred150
    def synpred150_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1501670)
        if self.failed:
            return 


    # $ANTLR end synpred150



    # $ANTLR start synpred164
    def synpred164_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1641817)
        if self.failed:
            return 


    # $ANTLR end synpred164



    # $ANTLR start synpred167
    def synpred167_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1671844)
        if self.failed:
            return 


    # $ANTLR end synpred167



    # $ANTLR start synpred170
    def synpred170_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:50: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:50: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1701869)
        if self.failed:
            return 


    # $ANTLR end synpred170



    # $ANTLR start synpred171
    def synpred171_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred1711862)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:27: ( LT )*
        while True: #loop319
            alt319 = 2
            LA319_0 = self.input.LA(1)

            if (LA319_0 == LT) :
                alt319 = 1


            if alt319 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1711864)
                if self.failed:
                    return 


            else:
                break #loop319


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred1711867)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:312:50: ( LT )*
        while True: #loop320
            alt320 = 2
            LA320_0 = self.input.LA(1)

            if (LA320_0 == LT) :
                LA320_2 = self.input.LA(2)

                if (self.synpred170()) :
                    alt320 = 1




            if alt320 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1711869)
                if self.failed:
                    return 


            else:
                break #loop320


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred1711872)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred171



    # $ANTLR start synpred173
    def synpred173_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:50: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:50: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1731910)
        if self.failed:
            return 


    # $ANTLR end synpred173



    # $ANTLR start synpred174
    def synpred174_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred1741903)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:27: ( LT )*
        while True: #loop321
            alt321 = 2
            LA321_0 = self.input.LA(1)

            if (LA321_0 == LT) :
                alt321 = 1


            if alt321 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1741905)
                if self.failed:
                    return 


            else:
                break #loop321


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred1741908)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:50: ( LT )*
        while True: #loop322
            alt322 = 2
            LA322_0 = self.input.LA(1)

            if (LA322_0 == LT) :
                LA322_2 = self.input.LA(2)

                if (self.synpred173()) :
                    alt322 = 1




            if alt322 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1741910)
                if self.failed:
                    return 


            else:
                break #loop322


        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_synpred1741913)
        self.assignmentExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred174



    # $ANTLR start synpred175
    def synpred175_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred1751944)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred175



    # $ANTLR start synpred176
    def synpred176_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred1761961)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred176



    # $ANTLR start synpred177
    def synpred177_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1771968)
        if self.failed:
            return 


    # $ANTLR end synpred177



    # $ANTLR start synpred179
    def synpred179_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( LT )*
        while True: #loop323
            alt323 = 2
            LA323_0 = self.input.LA(1)

            if (LA323_0 == LT) :
                alt323 = 1


            if alt323 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1791996)
                if self.failed:
                    return 


            else:
                break #loop323


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1791999)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred179



    # $ANTLR start synpred182
    def synpred182_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:24: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:24: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:26: ( LT )*
        while True: #loop326
            alt326 = 2
            LA326_0 = self.input.LA(1)

            if (LA326_0 == LT) :
                alt326 = 1


            if alt326 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1822022)
                if self.failed:
                    return 


            else:
                break #loop326


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1822026)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred182



    # $ANTLR start synpred184
    def synpred184_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1842035)
        if self.failed:
            return 


    # $ANTLR end synpred184



    # $ANTLR start synpred187
    def synpred187_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:46: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:46: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:46: ( LT )*
        while True: #loop329
            alt329 = 2
            LA329_0 = self.input.LA(1)

            if (LA329_0 == LT) :
                alt329 = 1


            if alt329 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1872046)
                if self.failed:
                    return 


            else:
                break #loop329


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1872049)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred187



    # $ANTLR start synpred191
    def synpred191_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1912119)
        if self.failed:
            return 


    # $ANTLR end synpred191



    # $ANTLR start synpred195
    def synpred195_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:45: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:45: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:45: ( LT )*
        while True: #loop330
            alt330 = 2
            LA330_0 = self.input.LA(1)

            if (LA330_0 == LT) :
                alt330 = 1


            if alt330 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1952131)
                if self.failed:
                    return 


            else:
                break #loop330


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred1952134)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred195



    # $ANTLR start synpred200
    def synpred200_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2002202)
        if self.failed:
            return 


    # $ANTLR end synpred200



    # $ANTLR start synpred201
    def synpred201_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:34: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:34: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2012207)
        if self.failed:
            return 


    # $ANTLR end synpred201



    # $ANTLR start synpred202
    def synpred202_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:43: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:43: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2022213)
        if self.failed:
            return 


    # $ANTLR end synpred202



    # $ANTLR start synpred203
    def synpred203_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:68: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:68: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2032218)
        if self.failed:
            return 


    # $ANTLR end synpred203



    # $ANTLR start synpred207
    def synpred207_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2072253)
        if self.failed:
            return 


    # $ANTLR end synpred207



    # $ANTLR start synpred211
    def synpred211_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:12: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:12: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2112342)
        if self.failed:
            return 


    # $ANTLR end synpred211



    # $ANTLR start synpred212
    def synpred212_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:16: ( e4xIdentifier )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:16: e4xIdentifier
        self.following.append(self.FOLLOW_e4xIdentifier_in_synpred2122345)
        self.e4xIdentifier()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred212



    # $ANTLR start synpred226
    def synpred226_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:34: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:34: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2262449)
        if self.failed:
            return 


    # $ANTLR end synpred226



    # $ANTLR start synpred228
    def synpred228_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:69: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:69: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2282461)
        if self.failed:
            return 


    # $ANTLR end synpred228



    # $ANTLR start synpred231
    def synpred231_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:38: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:38: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2312487)
        if self.failed:
            return 


    # $ANTLR end synpred231



    # $ANTLR start synpred233
    def synpred233_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2332499)
        if self.failed:
            return 


    # $ANTLR end synpred233



    # $ANTLR start synpred236
    def synpred236_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:411:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2362525)
        if self.failed:
            return 


    # $ANTLR end synpred236



    # $ANTLR start synpred239
    def synpred239_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:40: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:415:40: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2392552)
        if self.failed:
            return 


    # $ANTLR end synpred239



    # $ANTLR start synpred242
    def synpred242_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2422579)
        if self.failed:
            return 


    # $ANTLR end synpred242



    # $ANTLR start synpred245
    def synpred245_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:423:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2452606)
        if self.failed:
            return 


    # $ANTLR end synpred245



    # $ANTLR start synpred248
    def synpred248_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:427:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2482633)
        if self.failed:
            return 


    # $ANTLR end synpred248



    # $ANTLR start synpred251
    def synpred251_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:431:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2512660)
        if self.failed:
            return 


    # $ANTLR end synpred251



    # $ANTLR start synpred254
    def synpred254_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:435:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2542687)
        if self.failed:
            return 


    # $ANTLR end synpred254



    # $ANTLR start synpred257
    def synpred257_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2572714)
        if self.failed:
            return 


    # $ANTLR end synpred257



    # $ANTLR start synpred260
    def synpred260_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:33: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:33: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2602741)
        if self.failed:
            return 


    # $ANTLR end synpred260



    # $ANTLR start synpred263
    def synpred263_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:37: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:447:37: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2632768)
        if self.failed:
            return 


    # $ANTLR end synpred263



    # $ANTLR start synpred269
    def synpred269_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:61: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:451:61: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2692809)
        if self.failed:
            return 


    # $ANTLR end synpred269



    # $ANTLR start synpred275
    def synpred275_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:455:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2752849)
        if self.failed:
            return 


    # $ANTLR end synpred275



    # $ANTLR start synpred283
    def synpred283_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:74: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:74: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2832898)
        if self.failed:
            return 


    # $ANTLR end synpred283



    # $ANTLR start synpred284
    def synpred284_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:21: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:23: ( LT )*
        while True: #loop370
            alt370 = 2
            LA370_0 = self.input.LA(1)

            if (LA370_0 == LT) :
                alt370 = 1


            if alt370 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2842870)
                if self.failed:
                    return 


            else:
                break #loop370


        if (60 <= self.input.LA(1) <= 61) or self.input.LA(1) == 86 or (122 <= self.input.LA(1) <= 124):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2842874
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:76: ( LT )*
        while True: #loop371
            alt371 = 2
            LA371_0 = self.input.LA(1)

            if (LA371_0 == LT) :
                LA371_2 = self.input.LA(2)

                if (self.synpred283()) :
                    alt371 = 1




            if alt371 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2842898)
                if self.failed:
                    return 


            else:
                break #loop371


        self.following.append(self.FOLLOW_shiftExpression_in_synpred2842902)
        self.shiftExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred284



    # $ANTLR start synpred290
    def synpred290_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:67: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:67: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2902942)
        if self.failed:
            return 


    # $ANTLR end synpred290



    # $ANTLR start synpred295
    def synpred295_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:51: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:51: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2952978)
        if self.failed:
            return 


    # $ANTLR end synpred295



    # $ANTLR start synpred299
    def synpred299_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:47: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:47: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2993010)
        if self.failed:
            return 


    # $ANTLR end synpred299



    # $ANTLR start synpred300
    def synpred300_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:32: ( LT )*
        while True: #loop376
            alt376 = 2
            LA376_0 = self.input.LA(1)

            if (LA376_0 == LT) :
                alt376 = 1


            if alt376 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3002998)
                if self.failed:
                    return 


            else:
                break #loop376


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
                self.input, mse, self.FOLLOW_set_in_synpred3003002
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:49: ( LT )*
        while True: #loop377
            alt377 = 2
            LA377_0 = self.input.LA(1)

            if (LA377_0 == LT) :
                LA377_2 = self.input.LA(2)

                if (self.synpred299()) :
                    alt377 = 1




            if alt377 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3003010)
                if self.failed:
                    return 


            else:
                break #loop377


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred3003014)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred300



    # $ANTLR start synpred304
    def synpred304_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3043046)
        if self.failed:
            return 


    # $ANTLR end synpred304



    # $ANTLR start synpred305
    def synpred305_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:21: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:23: ( LT )*
        while True: #loop378
            alt378 = 2
            LA378_0 = self.input.LA(1)

            if (LA378_0 == LT) :
                alt378 = 1


            if alt378 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3053030)
                if self.failed:
                    return 


            else:
                break #loop378


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
                self.input, mse, self.FOLLOW_set_in_synpred3053034
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:475:46: ( LT )*
        while True: #loop379
            alt379 = 2
            LA379_0 = self.input.LA(1)

            if (LA379_0 == LT) :
                LA379_2 = self.input.LA(2)

                if (self.synpred304()) :
                    alt379 = 1




            if alt379 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3053046)
                if self.failed:
                    return 


            else:
                break #loop379


        self.following.append(self.FOLLOW_unaryExpression_in_synpred3053050)
        self.unaryExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred305



    # $ANTLR start synpred320
    def synpred320_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:4: ( ( LT )* ( '<' | XMLComment ) )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:5: ( LT )* ( '<' | XMLComment )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:5: ( LT )*
        while True: #loop380
            alt380 = 2
            LA380_0 = self.input.LA(1)

            if (LA380_0 == LT) :
                alt380 = 1


            if alt380 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3203142)
                if self.failed:
                    return 


            else:
                break #loop380


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
                self.input, mse, self.FOLLOW_set_in_synpred3203145
                )
            raise mse




    # $ANTLR end synpred320



    # $ANTLR start synpred324
    def synpred324_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:494:4: ( objectLiteral )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:494:4: objectLiteral
        self.following.append(self.FOLLOW_objectLiteral_in_synpred3243183)
        self.objectLiteral()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred324



    # $ANTLR start synpred325
    def synpred325_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:495:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3253190)
        if self.failed:
            return 


    # $ANTLR end synpred325



    # $ANTLR start synpred327
    def synpred327_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3273215)
        if self.failed:
            return 


    # $ANTLR end synpred327



    # $ANTLR start synpred330
    def synpred330_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3303228)
        if self.failed:
            return 


    # $ANTLR end synpred330



    # $ANTLR start synpred332
    def synpred332_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:35: ( LT )* ',' ( ( LT )* assignmentExpression )?
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:35: ( LT )*
        while True: #loop382
            alt382 = 2
            LA382_0 = self.input.LA(1)

            if (LA382_0 == LT) :
                alt382 = 1


            if alt382 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3323222)
                if self.failed:
                    return 


            else:
                break #loop382


        self.match(self.input, 70, self.FOLLOW_70_in_synpred3323225)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:43: ( ( LT )* assignmentExpression )?
        alt384 = 2
        LA384_0 = self.input.LA(1)

        if ((LT <= LA384_0 <= RegularExpressionHacks) or LA384_0 == 60 or LA384_0 == 62 or LA384_0 == 64 or LA384_0 == 66 or (68 <= LA384_0 <= 69) or (72 <= LA384_0 <= 74) or LA384_0 == 85 or LA384_0 == 96 or LA384_0 == 98 or LA384_0 == 128 or (130 <= LA384_0 <= 142)) :
            alt384 = 1
        if alt384 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: ( LT )* assignmentExpression
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:500:44: ( LT )*
            while True: #loop383
                alt383 = 2
                LA383_0 = self.input.LA(1)

                if (LA383_0 == LT) :
                    LA383_2 = self.input.LA(2)

                    if (self.synpred330()) :
                        alt383 = 1




                if alt383 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_synpred3323228)
                    if self.failed:
                        return 


                else:
                    break #loop383


            self.following.append(self.FOLLOW_assignmentExpression_in_synpred3323231)
            self.assignmentExpression()
            self.following.pop()
            if self.failed:
                return 





    # $ANTLR end synpred332



    # $ANTLR start synpred336
    def synpred336_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3363280)
        if self.failed:
            return 


    # $ANTLR end synpred336



    # $ANTLR start synpred345
    def synpred345_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:25: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:511:25: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3453341)
        if self.failed:
            return 


    # $ANTLR end synpred345



    # $ANTLR start synpred444
    def synpred444_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:8: ( reFirstChar )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:570:8: reFirstChar
        self.following.append(self.FOLLOW_reFirstChar_in_synpred4443979)
        self.reFirstChar()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred444



    def synpred126(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred126_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred299(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred299_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred80(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred80_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred82(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred82_fragment()
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

    def synpred48(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred48_fragment()
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

    def synpred85(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred85_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred305(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred305_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred290(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred290_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred304(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred304_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred88(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred88_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred89(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred89_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred300(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred300_fragment()
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

    def synpred41(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred41_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred212(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred212_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred164(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred164_fragment()
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

    def synpred251(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred251_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred257(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred257_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred254(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred254_fragment()
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

    def synpred118(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred118_fragment()
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

    def synpred38(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred38_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred114(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred114_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred111(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred111_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred76(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred76_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred77(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred77_fragment()
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

    def synpred226(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred226_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred150(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred150_fragment()
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

    def synpred228(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred228_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred324(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred324_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred195(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred195_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred325(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred325_fragment()
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

    def synpred320(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred320_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred191(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred191_fragment()
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

    def synpred145(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred145_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred147(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred147_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred148(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred148_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred101(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred101_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred61(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred61_fragment()
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

    def synpred104(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred104_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred60(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred60_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred107(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred107_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred231(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred231_fragment()
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

    def synpred187(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred187_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred330(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred330_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred184(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred184_fragment()
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

    def synpred332(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred332_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred236(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred236_fragment()
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

    def synpred96(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred96_fragment()
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

    def synpred94(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred94_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred133(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred133_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred58(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred58_fragment()
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

    def synpred18(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred18_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred55(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred55_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred444(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred444_fragment()
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

    def synpred283(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred283_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred284(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred284_fragment()
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

    def synpred131(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred131_fragment()
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

    def synpred3(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred3_fragment()
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

    def synpred170(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred170_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred242(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred242_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred171(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred171_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred174(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred174_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred200(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred200_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred173(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred173_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred201(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred201_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred176(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred176_fragment()
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

    def synpred175(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred175_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred248(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred248_fragment()
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

    def synpred16(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred16_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred345(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred345_fragment()
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

    def synpred245(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred245_fragment()
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
        u"\1\3\1\uffff\2\3\2\uffff\11\3\1\uffff\4\3\1\uffff\4\3\1\uffff\2"
        u"\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\1\3\1\uffff\2\3\2\uffff\11\3\1\uffff\4\3\1\uffff\4\3\1\uffff\2"
        u"\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1\3\1\uffff\15\3"),
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
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\12\uffff"
        u"\1\3\64\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\12\uffff"
        u"\1\3\64\uffff\2\3"),
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
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\12\uffff"
        u"\1\3\64\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\12\uffff"
        u"\1\3\64\uffff\2\3"),
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
        DFA.unpack(u"\1\5\34\uffff\1\4\11\uffff\3\5\12\uffff\1\5\64\uffff"
        u"\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\2\6\7\uffff\3\10"
        u"\12\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\13\46\uffff\3\13\12\uffff\1\13\64\uffff\2\13"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\11\uffff\3\10\12"
        u"\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\2\6\7\uffff\3\10"
        u"\12\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\16\46\uffff\3\16\12\uffff\1\16\64\uffff\2\16"),
        DFA.unpack(u"\1\20\43\uffff\1\17"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\11\1\12\11\uffff\3\10\12"
        u"\uffff\1\10\64\uffff\2\10")
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
    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\104\2\35\2\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\104\2\u008b\2\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA26_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\3\uffff\1\4\43\uffff\1\3\2\uffff\3\4\12\uffff\1"
        u"\4\64\uffff\2\4"),
        DFA.unpack(u"\1\2\3\uffff\1\4\43\uffff\1\3\2\uffff\3\4\12\uffff\1"
        u"\4\64\uffff\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    DFA26 = DFA
    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA31_max = DFA.unpack(
        u"\2\u008b\2\uffff"
        )

    DFA31_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA31_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\12\uffff\1\2\64\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\12\uffff\1\2\64\uffff"
        u"\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #31

    DFA31 = DFA
    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\2\107\2\uffff"
        )

    DFA30_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA30_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA30_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    DFA30 = DFA
    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\103\1\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA38_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\4\1\1\uffff\4\1\1\uffff\2\1\2"
        u"\uffff\1\1\1\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #38

    DFA38 = DFA
    # lookup tables for DFA #49

    DFA49_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA49_eof = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\2"
        )

    DFA49_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA49_max = DFA.unpack(
        u"\1\113\1\u008e\2\uffff\1\u008e"
        )

    DFA49_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA49_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA49_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\4\2\1\3\1\uffff\16\2\1\uffff\7\2\2\uffff\1\2\1\uffff\1\2\35\uffff"
        u"\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\4\2\1\3\1\uffff\16\2\1\uffff\7\2\2\uffff\1\2\1\uffff\1\2\35\uffff"
        u"\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #49

    DFA49 = DFA
    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA52_max = DFA.unpack(
        u"\2\113\2\uffff"
        )

    DFA52_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA52_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA52_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #52

    DFA52 = DFA
    # lookup tables for DFA #54

    DFA54_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA54_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA54_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA54_max = DFA.unpack(
        u"\1\113\1\u008e\2\uffff\1\u008e"
        )

    DFA54_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA54_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA54_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3"),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\16\3\1\uffff\7\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\16\3\1\uffff\7\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3")
    ]

    # class definition for DFA #54

    DFA54 = DFA
    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA56_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA56_max = DFA.unpack(
        u"\2\126\2\uffff"
        )

    DFA56_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA56_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA56_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\12\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\12\uffff\1"
        u"\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #56

    DFA56 = DFA
    # lookup tables for DFA #76

    DFA76_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA76_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA76_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA76_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA76_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA76_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA76_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\1\uffff\1\2\5\uffff"
        u"\1\2\12\uffff\1\2\1\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\1\uffff\1\2\5\uffff"
        u"\1\2\12\uffff\1\2\1\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #76

    DFA76 = DFA
    # lookup tables for DFA #79

    DFA79_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA79_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA79_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA79_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA79_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA79_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA79_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #79

    DFA79 = DFA
    # lookup tables for DFA #82

    DFA82_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA82_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA82_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA82_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA82_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA82_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA82_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #82

    DFA82 = DFA
    # lookup tables for DFA #111

    DFA111_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA111_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA111_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA111_max = DFA.unpack(
        u"\2\133\2\uffff"
        )

    DFA111_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA111_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA111_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\22\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\22\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #111

    DFA111 = DFA
    # lookup tables for DFA #115

    DFA115_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA115_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA115_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA115_max = DFA.unpack(
        u"\2\110\2\uffff"
        )

    DFA115_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA115_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA115_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\45\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #115

    DFA115 = DFA
    # lookup tables for DFA #114

    DFA114_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA114_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA114_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA114_max = DFA.unpack(
        u"\2\133\2\uffff"
        )

    DFA114_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA114_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA114_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\27\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\27\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #114

    DFA114 = DFA
    # lookup tables for DFA #123

    DFA123_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA123_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA123_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA123_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\133\1\uffff"
        )

    DFA123_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA123_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA123_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\4\1\1\uffff\4\1\1\3\2\1\2\uffff"
        u"\1\1\1\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3\27\uffff"
        u"\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #123

    DFA123 = DFA
    # lookup tables for DFA #127

    DFA127_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA127_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA127_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA127_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA127_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA127_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA127_transition = [
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\16\3\1\uffff\7\3\1\uffff\1\2\1\3\1\uffff\1\3\35\uffff"
        u"\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\16\3\1\uffff\7\3\1\uffff\1\2\1\3\1\uffff\1\3\35\uffff"
        u"\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #127

    DFA127 = DFA
    # lookup tables for DFA #136

    DFA136_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA136_eof = DFA.unpack(
        u"\1\1\1\uffff\1\1\1\uffff\1\1"
        )

    DFA136_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff\1\35"
        )

    DFA136_max = DFA.unpack(
        u"\1\143\1\uffff\1\u008e\1\uffff\1\u008e"
        )

    DFA136_accept = DFA.unpack(
        u"\1\uffff\1\2\1\uffff\1\1\1\uffff"
        )

    DFA136_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA136_transition = [
        DFA.unpack(u"\1\2\41\uffff\1\1\3\uffff\1\1\2\uffff\1\3\1\1\3\uffff"
        u"\1\1\27\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\1\31\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\3\17"
        u"\1\1\uffff\7\1\2\uffff\1\1\1\uffff\2\1\34\uffff\1\1\1\uffff\15"
        u"\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\1\31\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\3\17"
        u"\1\1\uffff\7\1\2\uffff\1\1\1\uffff\2\1\34\uffff\1\1\1\uffff\15"
        u"\1")
    ]

    # class definition for DFA #136

    DFA136 = DFA
    # lookup tables for DFA #139

    DFA139_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA139_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA139_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA139_max = DFA.unpack(
        u"\2\113\2\uffff"
        )

    DFA139_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA139_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA139_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u"\1\1\50\uffff\1\3\4\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #139

    DFA139 = DFA
    # lookup tables for DFA #170

    DFA170_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA170_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA170_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA170_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA170_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA170_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA170_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #170

    DFA170 = DFA
    # lookup tables for DFA #183

    DFA183_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA183_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA183_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA183_max = DFA.unpack(
        u"\1\160\1\u008e\2\uffff\1\u008e"
        )

    DFA183_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA183_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA183_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\3\uffff\1\3\2\uffff\2\3\3\uffff\1"
        u"\3\27\uffff\1\3\14\uffff\1\2"),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\3\3\1\uffff\24\3\1\uffff"
        u"\7\3\2\uffff\1\3\1\uffff\2\3\14\uffff\1\2\17\uffff\1\3\1\uffff"
        u"\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\3\3\1\uffff\24\3\1\uffff"
        u"\7\3\2\uffff\1\3\1\uffff\2\3\14\uffff\1\2\17\uffff\1\3\1\uffff"
        u"\15\3")
    ]

    # class definition for DFA #183

    DFA183 = DFA
    # lookup tables for DFA #188

    DFA188_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA188_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA188_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA188_max = DFA.unpack(
        u"\2\160\2\uffff"
        )

    DFA188_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA188_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA188_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\12\uffff\1"
        u"\3\31\uffff\1\2"),
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\12\uffff\1"
        u"\3\31\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #188

    DFA188 = DFA
    # lookup tables for DFA #191

    DFA191_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA191_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA191_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA191_max = DFA.unpack(
        u"\1\161\1\u008e\2\uffff\1\u008e"
        )

    DFA191_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA191_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA191_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\1\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\1\2\1\3\16\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\1\2\1\3\16\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #191

    DFA191 = DFA
    # lookup tables for DFA #194

    DFA194_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA194_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA194_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA194_max = DFA.unpack(
        u"\2\161\2\uffff"
        )

    DFA194_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA194_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA194_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #194

    DFA194 = DFA
    # lookup tables for DFA #197

    DFA197_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA197_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA197_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA197_max = DFA.unpack(
        u"\1\162\1\u008e\2\uffff\1\u008e"
        )

    DFA197_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA197_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA197_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\2\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\2\2\1\3\15\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\2\2\1\3\15\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #197

    DFA197 = DFA
    # lookup tables for DFA #200

    DFA200_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA200_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA200_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA200_max = DFA.unpack(
        u"\2\162\2\uffff"
        )

    DFA200_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA200_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA200_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #200

    DFA200 = DFA
    # lookup tables for DFA #203

    DFA203_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA203_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA203_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA203_max = DFA.unpack(
        u"\1\163\1\u008e\2\uffff\1\u008e"
        )

    DFA203_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA203_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA203_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\3\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\3\2\1\3\14\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\3\2\1\3\14\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #203

    DFA203 = DFA
    # lookup tables for DFA #206

    DFA206_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA206_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA206_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA206_max = DFA.unpack(
        u"\2\163\2\uffff"
        )

    DFA206_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA206_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA206_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #206

    DFA206 = DFA
    # lookup tables for DFA #209

    DFA209_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA209_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA209_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA209_max = DFA.unpack(
        u"\1\164\1\u008e\2\uffff\1\u008e"
        )

    DFA209_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA209_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA209_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\4\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\4\2\1\3\13\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\4\2\1\3\13\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #209

    DFA209 = DFA
    # lookup tables for DFA #212

    DFA212_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA212_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA212_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA212_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA212_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA212_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA212_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\4\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #212

    DFA212 = DFA
    # lookup tables for DFA #215

    DFA215_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA215_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA215_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA215_max = DFA.unpack(
        u"\1\165\1\u008e\2\uffff\1\u008e"
        )

    DFA215_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA215_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA215_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\5\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\5\2\1\3\12\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\5\2\1\3\12\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #215

    DFA215 = DFA
    # lookup tables for DFA #218

    DFA218_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA218_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA218_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA218_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA218_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA218_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA218_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\5\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #218

    DFA218 = DFA
    # lookup tables for DFA #221

    DFA221_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA221_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA221_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA221_max = DFA.unpack(
        u"\1\171\1\u008e\2\uffff\1\u008e"
        )

    DFA221_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA221_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA221_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\27\uffff\1\2\14\uffff\6\2\4\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\6\2\4\3\6\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\24\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\6\2\4\3\6\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #221

    DFA221 = DFA
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
        u"\2\171\2\uffff"
        )

    DFA224_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA224_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA224_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\12\uffff\1"
        u"\2\31\uffff\6\2\4\3"),
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
        u"\2\174\2\uffff"
        )

    DFA230_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA230_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA230_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\12\uffff\1\2\31\uffff\12\2\3\3"),
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\12\uffff\1\2\31\uffff\12\2\3\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #230

    DFA230 = DFA
    # lookup tables for DFA #233

    DFA233_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA233_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA233_min = DFA.unpack(
        u"\2\35\2\uffff\1\35"
        )

    DFA233_max = DFA.unpack(
        u"\1\177\1\u008e\2\uffff\1\u008e"
        )

    DFA233_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA233_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA233_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\3\uffff\1\2\2\uffff\2"
        u"\2\3\uffff\1\2\12\uffff\1\2\14\uffff\1\2\14\uffff\15\2\3\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\5\2\1\uffff\34\2\2\uffff\1\2\1\uffff"
        u"\2\2\14\uffff\15\2\3\3\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\5\2\1\uffff\34\2\2\uffff\1\2\1\uffff"
        u"\2\2\14\uffff\15\2\3\3\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #233

    DFA233 = DFA
    # lookup tables for DFA #246

    DFA246_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA246_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA246_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA246_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\143\1\uffff"
        )

    DFA246_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA246_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA246_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\uffff\2\1\1\3\1\uffff\3\1\12\uffff\1\1\12\uffff\1\1\1\uffff"
        u"\1\1\1\3\34\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\3\uffff\1"
        u"\3\34\uffff\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #246

    DFA246 = DFA
    # lookup tables for DFA #250

    DFA250_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA250_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA250_min = DFA.unpack(
        u"\2\35\1\0\2\uffff"
        )

    DFA250_max = DFA.unpack(
        u"\2\143\1\0\2\uffff"
        )

    DFA250_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA250_special = DFA.unpack(
        u"\2\uffff\1\0\2\uffff"
        )

            
    DFA250_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\2\34\uffff\1\3"),
        DFA.unpack(u"\1\1\50\uffff\1\2\34\uffff\1\3"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #250

    class DFA250(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA250_2 = input.LA(1)

                 
                index250_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred332()):
                    s = 4

                elif (True):
                    s = 3

                 
                input.seek(index250_2)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 250, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #249

    DFA249_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA249_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA249_min = DFA.unpack(
        u"\2\35\2\uffff"
        )

    DFA249_max = DFA.unpack(
        u"\2\u008e\2\uffff"
        )

    DFA249_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA249_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA249_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\1\3\34\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\12\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\1\3\34\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #249

    DFA249 = DFA
    # lookup tables for DFA #258

    DFA258_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA258_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA258_min = DFA.unpack(
        u"\3\35\1\uffff\1\35\1\uffff"
        )

    DFA258_max = DFA.unpack(
        u"\2\106\1\u008b\1\uffff\1\u008b\1\uffff"
        )

    DFA258_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1"
        )

    DFA258_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA258_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\12\uffff"
        u"\1\5\64\uffff\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\12\uffff"
        u"\1\5\64\uffff\2\5"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #258

    DFA258 = DFA
    # lookup tables for DFA #272

    DFA272_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA272_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA272_min = DFA.unpack(
        u"\1\36\1\35\1\uffff\4\35\2\uffff"
        )

    DFA272_max = DFA.unpack(
        u"\2\u008b\1\uffff\4\u008b\2\uffff"
        )

    DFA272_accept = DFA.unpack(
        u"\2\uffff\1\1\4\uffff\1\3\1\2"
        )

    DFA272_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA272_transition = [
        DFA.unpack(u"\1\2\1\uffff\2\2\46\uffff\3\2\12\uffff\1\2\64\uffff"
        u"\1\1\1\3"),
        DFA.unpack(u"\1\5\3\uffff\1\4\35\uffff\1\2\10\uffff\3\4\12\uffff"
        u"\1\4\64\uffff\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\3\uffff\1\4\35\uffff\1\2\10\uffff\3\4\12\uffff"
        u"\1\4\64\uffff\2\4"),
        DFA.unpack(u"\1\6\3\uffff\1\10\43\uffff\1\7\2\uffff\3\10\12\uffff"
        u"\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\5\3\uffff\1\7\35\uffff\1\2\10\uffff\3\7\12\uffff"
        u"\1\7\64\uffff\2\7"),
        DFA.unpack(u"\1\6\3\uffff\1\10\43\uffff\1\7\2\uffff\3\10\12\uffff"
        u"\1\10\64\uffff\2\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #272

    DFA272 = DFA
    # lookup tables for DFA #295

    DFA295_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA295_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA295_min = DFA.unpack(
        u"\1\35\1\uffff\1\35\1\uffff"
        )

    DFA295_max = DFA.unpack(
        u"\1\u008e\1\uffff\1\103\1\uffff"
        )

    DFA295_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA295_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA295_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\11\1\1\uffff\4\1\1\uffff\4\1\1\uffff\2\1\2"
        u"\uffff\1\1\1\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #295

    DFA295 = DFA
 

    FOLLOW_LT_in_program147 = frozenset([1])
    FOLLOW_sourceElements_in_program151 = frozenset([29])
    FOLLOW_LT_in_program153 = frozenset([1])
    FOLLOW_EOF_in_program157 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements170 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_sourceElements173 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_sourceElement_in_sourceElements177 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_functionDeclaration_in_sourceElement196 = frozenset([1])
    FOLLOW_statement_in_sourceElement201 = frozenset([1])
    FOLLOW_60_in_xmlStartTag219 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_xmlTagName_in_xmlStartTag221 = frozenset([29, 33, 61, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_xmlStartTag224 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_xmlAttribute_in_xmlStartTag228 = frozenset([29, 33, 61, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_xmlStartTag232 = frozenset([1])
    FOLLOW_61_in_xmlStartTag236 = frozenset([1])
    FOLLOW_60_in_xmlEndTag254 = frozenset([62])
    FOLLOW_62_in_xmlEndTag256 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_xmlTagName_in_xmlEndTag258 = frozenset([61])
    FOLLOW_61_in_xmlEndTag260 = frozenset([1])
    FOLLOW_60_in_xmlEmptyTag278 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_xmlTagName_in_xmlEmptyTag280 = frozenset([29, 33, 62, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_xmlEmptyTag283 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_xmlAttribute_in_xmlEmptyTag287 = frozenset([29, 33, 62, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_xmlEmptyTag291 = frozenset([1])
    FOLLOW_62_in_xmlEmptyTag295 = frozenset([61])
    FOLLOW_61_in_xmlEmptyTag297 = frozenset([1])
    FOLLOW_identifier_in_xmlTagName315 = frozenset([1, 63, 64])
    FOLLOW_set_in_xmlTagName319 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_xmlTagName325 = frozenset([1, 63, 64])
    FOLLOW_xmlAttributeName_in_xmlAttribute345 = frozenset([65])
    FOLLOW_65_in_xmlAttribute347 = frozenset([30, 66])
    FOLLOW_xmlAttributeValue_in_xmlAttribute349 = frozenset([1])
    FOLLOW_identifier_in_xmlAttributeName368 = frozenset([1, 63, 64])
    FOLLOW_set_in_xmlAttributeName372 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_xmlAttributeName378 = frozenset([1, 63, 64])
    FOLLOW_e4xSplice_in_xmlAttributeValue403 = frozenset([1])
    FOLLOW_StringLiteral_in_xmlAttributeValue408 = frozenset([1])
    FOLLOW_66_in_e4xSplice426 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_e4xSplice428 = frozenset([67])
    FOLLOW_67_in_e4xSplice430 = frozenset([1])
    FOLLOW_xmlEndTag_in_xmlPayload444 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_xmlPayload449 = frozenset([1])
    FOLLOW_xmlStartTag_in_xmlPayload454 = frozenset([1])
    FOLLOW_e4xSplice_in_xmlPayload459 = frozenset([1])
    FOLLOW_XMLComment_in_xmlPayload464 = frozenset([1])
    FOLLOW_LT_in_xmlLiteral477 = frozenset([29, 31, 60, 66])
    FOLLOW_xmlPayload_in_xmlLiteral480 = frozenset([1, 29, 31, 60, 66])
    FOLLOW_68_in_functionDeclaration495 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_functionDeclaration497 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_functionDeclaration500 = frozenset([29, 69])
    FOLLOW_LT_in_functionDeclaration502 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_functionDeclaration505 = frozenset([29, 66])
    FOLLOW_LT_in_functionDeclaration507 = frozenset([29, 66])
    FOLLOW_statementBlock_in_functionDeclaration510 = frozenset([1])
    FOLLOW_68_in_functionExpression536 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_functionExpression538 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
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
    FOLLOW_69_in_formalParameterList609 = frozenset([29, 33, 71, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_formalParameterList612 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_formalParameterList615 = frozenset([29, 70, 71])
    FOLLOW_LT_in_formalParameterList618 = frozenset([29, 70])
    FOLLOW_70_in_formalParameterList621 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_formalParameterList623 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_formalParameterList626 = frozenset([29, 70, 71])
    FOLLOW_LT_in_formalParameterList632 = frozenset([29, 71])
    FOLLOW_71_in_formalParameterList635 = frozenset([1])
    FOLLOW_statementBlock_in_statement658 = frozenset([1])
    FOLLOW_variableStatement_in_statement663 = frozenset([1])
    FOLLOW_emptyStatement_in_statement668 = frozenset([1])
    FOLLOW_expressionStatement_in_statement673 = frozenset([1])
    FOLLOW_ifStatement_in_statement678 = frozenset([1])
    FOLLOW_iterationStatement_in_statement683 = frozenset([1])
    FOLLOW_continueStatement_in_statement688 = frozenset([1])
    FOLLOW_breakStatement_in_statement693 = frozenset([1])
    FOLLOW_returnStatement_in_statement698 = frozenset([1])
    FOLLOW_withStatement_in_statement703 = frozenset([1])
    FOLLOW_labelledStatement_in_statement708 = frozenset([1])
    FOLLOW_switchStatement_in_statement713 = frozenset([1])
    FOLLOW_throwStatement_in_statement718 = frozenset([1])
    FOLLOW_tryStatement_in_statement723 = frozenset([1])
    FOLLOW_defaultXmlNamespaceStatement_in_statement728 = frozenset([1])
    FOLLOW_72_in_defaultXmlNamespaceStatement739 = frozenset([73])
    FOLLOW_73_in_defaultXmlNamespaceStatement741 = frozenset([74])
    FOLLOW_74_in_defaultXmlNamespaceStatement743 = frozenset([29, 65])
    FOLLOW_LT_in_defaultXmlNamespaceStatement745 = frozenset([29, 65])
    FOLLOW_65_in_defaultXmlNamespaceStatement748 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_defaultXmlNamespaceStatement750 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_defaultXmlNamespaceStatement753 = frozenset([29, 75])
    FOLLOW_LT_in_defaultXmlNamespaceStatement756 = frozenset([1])
    FOLLOW_75_in_defaultXmlNamespaceStatement760 = frozenset([1])
    FOLLOW_66_in_statementBlock782 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_statementBlock784 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statementList_in_statementBlock788 = frozenset([29, 67])
    FOLLOW_LT_in_statementBlock791 = frozenset([29, 67])
    FOLLOW_67_in_statementBlock795 = frozenset([1])
    FOLLOW_66_in_statementBlock800 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 76, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_76_in_statementBlock802 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_statementBlock805 = frozenset([67])
    FOLLOW_67_in_statementBlock807 = frozenset([1])
    FOLLOW_statement_in_statementList820 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_statementList823 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_statementList827 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_77_in_variableStatement843 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_78_in_variableStatement847 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_79_in_variableStatement851 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_variableStatement854 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_variableDeclarationList_in_variableStatement857 = frozenset([29, 75])
    FOLLOW_LT_in_variableStatement860 = frozenset([1])
    FOLLOW_75_in_variableStatement864 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList889 = frozenset([1, 29, 70])
    FOLLOW_LT_in_variableDeclarationList892 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclarationList896 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_variableDeclarationList898 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_variableDeclaration_in_variableDeclarationList902 = frozenset([1, 29, 70])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn916 = frozenset([1, 29, 70])
    FOLLOW_LT_in_variableDeclarationListNoIn919 = frozenset([29, 70])
    FOLLOW_70_in_variableDeclarationListNoIn923 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_variableDeclarationListNoIn925 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn929 = frozenset([1, 29, 70])
    FOLLOW_identifier_in_variableDeclaration943 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclaration946 = frozenset([29, 65])
    FOLLOW_initialiser_in_variableDeclaration949 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn976 = frozenset([1, 29, 65])
    FOLLOW_LT_in_variableDeclarationNoIn979 = frozenset([29, 65])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn982 = frozenset([1])
    FOLLOW_65_in_initialiser1009 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_initialiser1011 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_initialiser1014 = frozenset([1])
    FOLLOW_65_in_initialiserNoIn1032 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_initialiserNoIn1034 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn1037 = frozenset([1])
    FOLLOW_75_in_emptyStatement1055 = frozenset([1])
    FOLLOW_expression_in_expressionStatement1067 = frozenset([29, 75])
    FOLLOW_set_in_expressionStatement1069 = frozenset([1])
    FOLLOW_80_in_ifStatement1088 = frozenset([29, 69])
    FOLLOW_LT_in_ifStatement1090 = frozenset([1])
    FOLLOW_69_in_ifStatement1094 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1096 = frozenset([1])
    FOLLOW_expression_in_ifStatement1100 = frozenset([29, 71])
    FOLLOW_LT_in_ifStatement1102 = frozenset([1])
    FOLLOW_71_in_ifStatement1106 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1108 = frozenset([1])
    FOLLOW_statement_in_ifStatement1112 = frozenset([1, 29, 81])
    FOLLOW_LT_in_ifStatement1115 = frozenset([29, 81])
    FOLLOW_81_in_ifStatement1119 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_ifStatement1121 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_ifStatement1125 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement1139 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement1144 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement1149 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement1154 = frozenset([1])
    FOLLOW_82_in_doWhileStatement1166 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_doWhileStatement1168 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement1172 = frozenset([29, 83])
    FOLLOW_LT_in_doWhileStatement1174 = frozenset([1])
    FOLLOW_83_in_doWhileStatement1178 = frozenset([29, 69])
    FOLLOW_LT_in_doWhileStatement1180 = frozenset([1])
    FOLLOW_69_in_doWhileStatement1184 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_doWhileStatement1186 = frozenset([71])
    FOLLOW_71_in_doWhileStatement1188 = frozenset([29, 75])
    FOLLOW_set_in_doWhileStatement1190 = frozenset([1])
    FOLLOW_83_in_whileStatement1209 = frozenset([29, 69])
    FOLLOW_LT_in_whileStatement1211 = frozenset([1])
    FOLLOW_69_in_whileStatement1215 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_whileStatement1217 = frozenset([1])
    FOLLOW_expression_in_whileStatement1221 = frozenset([29, 71])
    FOLLOW_LT_in_whileStatement1223 = frozenset([1])
    FOLLOW_71_in_whileStatement1227 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_whileStatement1229 = frozenset([1])
    FOLLOW_statement_in_whileStatement1233 = frozenset([1])
    FOLLOW_84_in_forStatement1245 = frozenset([29, 69])
    FOLLOW_LT_in_forStatement1247 = frozenset([1])
    FOLLOW_69_in_forStatement1251 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 77, 79, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1254 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 77, 79, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_forStatementInitialiserPart_in_forStatement1258 = frozenset([29, 75])
    FOLLOW_LT_in_forStatement1262 = frozenset([1])
    FOLLOW_75_in_forStatement1266 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1269 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_forStatement1273 = frozenset([29, 75])
    FOLLOW_LT_in_forStatement1277 = frozenset([1])
    FOLLOW_75_in_forStatement1281 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 71, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1284 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_forStatement1288 = frozenset([29, 71])
    FOLLOW_LT_in_forStatement1292 = frozenset([1])
    FOLLOW_71_in_forStatement1296 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forStatement1298 = frozenset([1])
    FOLLOW_statement_in_forStatement1302 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart1314 = frozenset([1])
    FOLLOW_set_in_forStatementInitialiserPart1319 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_forStatementInitialiserPart1325 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1329 = frozenset([1])
    FOLLOW_84_in_forInStatement1341 = frozenset([29, 69, 85])
    FOLLOW_LT_in_forInStatement1343 = frozenset([1])
    FOLLOW_85_in_forInStatement1347 = frozenset([29, 69])
    FOLLOW_LT_in_forInStatement1350 = frozenset([1])
    FOLLOW_69_in_forInStatement1354 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 77, 79, 85, 96, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1356 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement1360 = frozenset([29, 86])
    FOLLOW_LT_in_forInStatement1362 = frozenset([1])
    FOLLOW_86_in_forInStatement1366 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1368 = frozenset([1])
    FOLLOW_expression_in_forInStatement1372 = frozenset([29, 71])
    FOLLOW_LT_in_forInStatement1374 = frozenset([1])
    FOLLOW_71_in_forInStatement1378 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_forInStatement1380 = frozenset([1])
    FOLLOW_statement_in_forInStatement1384 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1396 = frozenset([1])
    FOLLOW_set_in_forInStatementInitialiserPart1401 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_forInStatementInitialiserPart1407 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1411 = frozenset([1])
    FOLLOW_87_in_continueStatement1422 = frozenset([29, 33, 72, 73, 74, 75, 85, 138, 139])
    FOLLOW_identifier_in_continueStatement1424 = frozenset([29, 75])
    FOLLOW_set_in_continueStatement1427 = frozenset([1])
    FOLLOW_88_in_breakStatement1445 = frozenset([29, 33, 72, 73, 74, 75, 85, 138, 139])
    FOLLOW_identifier_in_breakStatement1447 = frozenset([29, 75])
    FOLLOW_set_in_breakStatement1450 = frozenset([1])
    FOLLOW_76_in_returnStatement1468 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_returnStatement1470 = frozenset([29, 75])
    FOLLOW_set_in_returnStatement1473 = frozenset([1])
    FOLLOW_89_in_withStatement1492 = frozenset([29, 69])
    FOLLOW_LT_in_withStatement1494 = frozenset([1])
    FOLLOW_69_in_withStatement1498 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_withStatement1500 = frozenset([1])
    FOLLOW_expression_in_withStatement1504 = frozenset([29, 71])
    FOLLOW_LT_in_withStatement1506 = frozenset([1])
    FOLLOW_71_in_withStatement1510 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_withStatement1512 = frozenset([1])
    FOLLOW_statement_in_withStatement1516 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1527 = frozenset([29, 63])
    FOLLOW_LT_in_labelledStatement1529 = frozenset([1])
    FOLLOW_63_in_labelledStatement1533 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_labelledStatement1535 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1539 = frozenset([1])
    FOLLOW_90_in_switchStatement1551 = frozenset([29, 69])
    FOLLOW_LT_in_switchStatement1553 = frozenset([1])
    FOLLOW_69_in_switchStatement1557 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_switchStatement1559 = frozenset([1])
    FOLLOW_expression_in_switchStatement1563 = frozenset([29, 71])
    FOLLOW_LT_in_switchStatement1565 = frozenset([1])
    FOLLOW_71_in_switchStatement1569 = frozenset([29, 66])
    FOLLOW_LT_in_switchStatement1571 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1575 = frozenset([1])
    FOLLOW_66_in_caseBlock1587 = frozenset([29, 67, 72, 91])
    FOLLOW_LT_in_caseBlock1590 = frozenset([29, 91])
    FOLLOW_caseClause_in_caseBlock1594 = frozenset([29, 67, 72, 91])
    FOLLOW_LT_in_caseBlock1599 = frozenset([29, 72])
    FOLLOW_defaultClause_in_caseBlock1603 = frozenset([29, 67, 91])
    FOLLOW_LT_in_caseBlock1606 = frozenset([29, 91])
    FOLLOW_caseClause_in_caseBlock1610 = frozenset([29, 67, 91])
    FOLLOW_LT_in_caseBlock1616 = frozenset([1])
    FOLLOW_67_in_caseBlock1620 = frozenset([1])
    FOLLOW_91_in_caseClause1631 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_caseClause1633 = frozenset([1])
    FOLLOW_expression_in_caseClause1637 = frozenset([29, 63])
    FOLLOW_LT_in_caseClause1639 = frozenset([1])
    FOLLOW_63_in_caseClause1643 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_caseClause1645 = frozenset([1])
    FOLLOW_statementList_in_caseClause1649 = frozenset([1])
    FOLLOW_72_in_defaultClause1662 = frozenset([29, 63])
    FOLLOW_LT_in_defaultClause1664 = frozenset([1])
    FOLLOW_63_in_defaultClause1668 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_defaultClause1670 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1674 = frozenset([1])
    FOLLOW_92_in_throwStatement1687 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_throwStatement1689 = frozenset([29, 75])
    FOLLOW_set_in_throwStatement1691 = frozenset([1])
    FOLLOW_93_in_tryStatement1709 = frozenset([29, 66])
    FOLLOW_LT_in_tryStatement1711 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1715 = frozenset([29, 94, 95])
    FOLLOW_LT_in_tryStatement1717 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1722 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1726 = frozenset([1, 29, 95])
    FOLLOW_LT_in_tryStatement1729 = frozenset([29, 95])
    FOLLOW_finallyClause_in_tryStatement1733 = frozenset([1])
    FOLLOW_94_in_catchClause1754 = frozenset([29, 69])
    FOLLOW_LT_in_catchClause1756 = frozenset([1])
    FOLLOW_69_in_catchClause1760 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_catchClause1762 = frozenset([1])
    FOLLOW_identifier_in_catchClause1766 = frozenset([29, 71])
    FOLLOW_LT_in_catchClause1768 = frozenset([1])
    FOLLOW_71_in_catchClause1772 = frozenset([29, 66])
    FOLLOW_LT_in_catchClause1774 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1778 = frozenset([1])
    FOLLOW_95_in_finallyClause1790 = frozenset([29, 66])
    FOLLOW_LT_in_finallyClause1792 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause1796 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1808 = frozenset([1, 29, 70])
    FOLLOW_LT_in_expression1811 = frozenset([29, 70])
    FOLLOW_70_in_expression1815 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_expression1817 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_expression1821 = frozenset([1, 29, 70])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1835 = frozenset([1, 29, 70])
    FOLLOW_LT_in_expressionNoIn1838 = frozenset([29, 70])
    FOLLOW_70_in_expressionNoIn1842 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_expressionNoIn1844 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1848 = frozenset([1, 29, 70])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1862 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_assignmentExpression1864 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_assignmentExpression1867 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_assignmentExpression1869 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_assignmentExpression1872 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpression1891 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1903 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_assignmentExpressionNoIn1905 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1908 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_assignmentExpressionNoIn1910 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1913 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1932 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression1944 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression1949 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1961 = frozenset([1])
    FOLLOW_96_in_newExpression1966 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 85, 96, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_newExpression1968 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 85, 96, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_newExpression_in_newExpression1971 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1993 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_LT_in_memberExpression1996 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_memberExpression1999 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_functionExpression_in_memberExpression2019 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_LT_in_memberExpression2022 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_memberExpression2026 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_96_in_memberExpression2033 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 85, 96, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_memberExpression2035 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 66, 68, 69, 72, 73, 74, 85, 96, 98, 137, 138, 139, 140, 141, 142])
    FOLLOW_memberExpression_in_memberExpression2038 = frozenset([29, 69])
    FOLLOW_LT_in_memberExpression2040 = frozenset([29, 69])
    FOLLOW_arguments_in_memberExpression2043 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_LT_in_memberExpression2046 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_memberExpression2049 = frozenset([1, 29, 63, 97, 98])
    FOLLOW_indexSuffix_in_memberExpressionSuffix2086 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix2091 = frozenset([1])
    FOLLOW_descendentSuffix_in_memberExpressionSuffix2096 = frozenset([1])
    FOLLOW_namespaceSuffix_in_memberExpressionSuffix2102 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression2117 = frozenset([29, 69, 97])
    FOLLOW_LT_in_callExpression2119 = frozenset([29, 69, 97])
    FOLLOW_97_in_callExpression2122 = frozenset([29, 69])
    FOLLOW_LT_in_callExpression2125 = frozenset([29, 69])
    FOLLOW_arguments_in_callExpression2128 = frozenset([1, 29, 63, 69, 97, 98])
    FOLLOW_LT_in_callExpression2131 = frozenset([29, 63, 69, 97, 98])
    FOLLOW_callExpressionSuffix_in_callExpression2134 = frozenset([1, 29, 63, 69, 97, 98])
    FOLLOW_arguments_in_callExpressionSuffix2163 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix2168 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2173 = frozenset([1])
    FOLLOW_descendentSuffix_in_callExpressionSuffix2178 = frozenset([1])
    FOLLOW_namespaceSuffix_in_callExpressionSuffix2184 = frozenset([1])
    FOLLOW_69_in_arguments2199 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 71, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arguments2202 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arguments2205 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2207 = frozenset([29, 70, 71])
    FOLLOW_70_in_arguments2211 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arguments2213 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arguments2216 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2218 = frozenset([29, 70, 71])
    FOLLOW_LT_in_arguments2225 = frozenset([29, 71])
    FOLLOW_71_in_arguments2228 = frozenset([1])
    FOLLOW_98_in_indexSuffix2251 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_indexSuffix2253 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_expression_in_indexSuffix2256 = frozenset([29, 99])
    FOLLOW_LT_in_indexSuffix2258 = frozenset([29, 99])
    FOLLOW_99_in_indexSuffix2261 = frozenset([1])
    FOLLOW_97_in_propertyReferenceSuffix2284 = frozenset([29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_LT_in_propertyReferenceSuffix2286 = frozenset([29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2289 = frozenset([1])
    FOLLOW_97_in_descendentSuffix2310 = frozenset([97])
    FOLLOW_97_in_descendentSuffix2312 = frozenset([29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_LT_in_descendentSuffix2314 = frozenset([29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_descendentSuffix2317 = frozenset([1])
    FOLLOW_63_in_namespaceSuffix2338 = frozenset([63])
    FOLLOW_63_in_namespaceSuffix2340 = frozenset([1, 29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_LT_in_namespaceSuffix2342 = frozenset([1, 29, 33, 72, 73, 74, 85, 100, 138, 139])
    FOLLOW_e4xIdentifier_in_namespaceSuffix2345 = frozenset([1])
    FOLLOW_identifier_in_e4xIdentifier2368 = frozenset([1])
    FOLLOW_100_in_e4xIdentifier2373 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression2440 = frozenset([1, 29, 112])
    FOLLOW_LT_in_conditionalExpression2443 = frozenset([29, 112])
    FOLLOW_112_in_conditionalExpression2447 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpression2449 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_conditionalExpression2453 = frozenset([29, 63])
    FOLLOW_LT_in_conditionalExpression2455 = frozenset([29, 63])
    FOLLOW_63_in_conditionalExpression2459 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpression2461 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_conditionalExpression2465 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2478 = frozenset([1, 29, 112])
    FOLLOW_LT_in_conditionalExpressionNoIn2481 = frozenset([29, 112])
    FOLLOW_112_in_conditionalExpressionNoIn2485 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpressionNoIn2487 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2491 = frozenset([29, 63])
    FOLLOW_LT_in_conditionalExpressionNoIn2493 = frozenset([29, 63])
    FOLLOW_63_in_conditionalExpressionNoIn2497 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_conditionalExpressionNoIn2499 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2503 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression2516 = frozenset([1, 29, 113])
    FOLLOW_LT_in_logicalORExpression2519 = frozenset([29, 113])
    FOLLOW_113_in_logicalORExpression2523 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalORExpression2525 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_logicalANDExpression_in_logicalORExpression2529 = frozenset([1, 29, 113])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2543 = frozenset([1, 29, 113])
    FOLLOW_LT_in_logicalORExpressionNoIn2546 = frozenset([29, 113])
    FOLLOW_113_in_logicalORExpressionNoIn2550 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalORExpressionNoIn2552 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2556 = frozenset([1, 29, 113])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2570 = frozenset([1, 29, 114])
    FOLLOW_LT_in_logicalANDExpression2573 = frozenset([29, 114])
    FOLLOW_114_in_logicalANDExpression2577 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalANDExpression2579 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2583 = frozenset([1, 29, 114])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2597 = frozenset([1, 29, 114])
    FOLLOW_LT_in_logicalANDExpressionNoIn2600 = frozenset([29, 114])
    FOLLOW_114_in_logicalANDExpressionNoIn2604 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_logicalANDExpressionNoIn2606 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2610 = frozenset([1, 29, 114])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2624 = frozenset([1, 29, 115])
    FOLLOW_LT_in_bitwiseORExpression2627 = frozenset([29, 115])
    FOLLOW_115_in_bitwiseORExpression2631 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseORExpression2633 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2637 = frozenset([1, 29, 115])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2651 = frozenset([1, 29, 115])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2654 = frozenset([29, 115])
    FOLLOW_115_in_bitwiseORExpressionNoIn2658 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2660 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2664 = frozenset([1, 29, 115])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2678 = frozenset([1, 29, 116])
    FOLLOW_LT_in_bitwiseXORExpression2681 = frozenset([29, 116])
    FOLLOW_116_in_bitwiseXORExpression2685 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseXORExpression2687 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2691 = frozenset([1, 29, 116])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2705 = frozenset([1, 29, 116])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2708 = frozenset([29, 116])
    FOLLOW_116_in_bitwiseXORExpressionNoIn2712 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2714 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2718 = frozenset([1, 29, 116])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2732 = frozenset([1, 29, 117])
    FOLLOW_LT_in_bitwiseANDExpression2735 = frozenset([29, 117])
    FOLLOW_117_in_bitwiseANDExpression2739 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseANDExpression2741 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2745 = frozenset([1, 29, 117])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2759 = frozenset([1, 29, 117])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2762 = frozenset([29, 117])
    FOLLOW_117_in_bitwiseANDExpressionNoIn2766 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2768 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2772 = frozenset([1, 29, 117])
    FOLLOW_relationalExpression_in_equalityExpression2786 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpression2789 = frozenset([29, 118, 119, 120, 121])
    FOLLOW_set_in_equalityExpression2793 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_equalityExpression2809 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_relationalExpression_in_equalityExpression2813 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2826 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpressionNoIn2829 = frozenset([29, 118, 119, 120, 121])
    FOLLOW_set_in_equalityExpressionNoIn2833 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_equalityExpressionNoIn2849 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2853 = frozenset([1, 29, 118, 119, 120, 121])
    FOLLOW_shiftExpression_in_relationalExpression2867 = frozenset([1, 29, 60, 61, 86, 122, 123, 124])
    FOLLOW_LT_in_relationalExpression2870 = frozenset([29, 60, 61, 86, 122, 123, 124])
    FOLLOW_set_in_relationalExpression2874 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_relationalExpression2898 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_relationalExpression2902 = frozenset([1, 29, 60, 61, 86, 122, 123, 124])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2915 = frozenset([1, 29, 60, 61, 122, 123, 124])
    FOLLOW_LT_in_relationalExpressionNoIn2918 = frozenset([29, 60, 61, 122, 123, 124])
    FOLLOW_set_in_relationalExpressionNoIn2922 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_relationalExpressionNoIn2942 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2946 = frozenset([1, 29, 60, 61, 122, 123, 124])
    FOLLOW_additiveExpression_in_shiftExpression2959 = frozenset([1, 29, 125, 126, 127])
    FOLLOW_LT_in_shiftExpression2962 = frozenset([29, 125, 126, 127])
    FOLLOW_set_in_shiftExpression2966 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_shiftExpression2978 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_additiveExpression_in_shiftExpression2982 = frozenset([1, 29, 125, 126, 127])
    FOLLOW_multiplicativeExpression_in_additiveExpression2995 = frozenset([1, 29, 64, 128])
    FOLLOW_LT_in_additiveExpression2998 = frozenset([29, 64, 128])
    FOLLOW_set_in_additiveExpression3002 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_additiveExpression3010 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_multiplicativeExpression_in_additiveExpression3014 = frozenset([1, 29, 64, 128])
    FOLLOW_unaryExpression_in_multiplicativeExpression3027 = frozenset([1, 29, 62, 100, 129])
    FOLLOW_LT_in_multiplicativeExpression3030 = frozenset([29, 62, 100, 129])
    FOLLOW_set_in_multiplicativeExpression3034 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_multiplicativeExpression3046 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_multiplicativeExpression3050 = frozenset([1, 29, 62, 100, 129])
    FOLLOW_postfixExpression_in_unaryExpression3063 = frozenset([1])
    FOLLOW_set_in_unaryExpression3068 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_unaryExpression3104 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression3116 = frozenset([1, 133, 134])
    FOLLOW_set_in_postfixExpression3118 = frozenset([1])
    FOLLOW_137_in_primaryExpression3136 = frozenset([1])
    FOLLOW_xmlLiteral_in_primaryExpression3153 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression3158 = frozenset([1])
    FOLLOW_literal_in_primaryExpression3173 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression3178 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression3183 = frozenset([1])
    FOLLOW_69_in_primaryExpression3188 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_primaryExpression3190 = frozenset([1])
    FOLLOW_expression_in_primaryExpression3194 = frozenset([29, 71])
    FOLLOW_LT_in_primaryExpression3196 = frozenset([1])
    FOLLOW_71_in_primaryExpression3200 = frozenset([1])
    FOLLOW_98_in_arrayLiteral3213 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 85, 96, 98, 99, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arrayLiteral3215 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 85, 96, 98, 99, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arrayLiteral3218 = frozenset([29, 70, 99])
    FOLLOW_LT_in_arrayLiteral3222 = frozenset([29, 70])
    FOLLOW_70_in_arrayLiteral3225 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 70, 72, 73, 74, 85, 96, 98, 99, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_arrayLiteral3228 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_arrayLiteral3231 = frozenset([29, 70, 99])
    FOLLOW_LT_in_arrayLiteral3237 = frozenset([29, 70, 99])
    FOLLOW_70_in_arrayLiteral3241 = frozenset([29, 99])
    FOLLOW_LT_in_arrayLiteral3243 = frozenset([29, 99])
    FOLLOW_99_in_arrayLiteral3248 = frozenset([1])
    FOLLOW_66_in_objectLiteral3278 = frozenset([29, 30, 32, 33, 67, 70, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_objectLiteral3280 = frozenset([29, 30, 32, 33, 67, 70, 72, 73, 74, 85, 138, 139])
    FOLLOW_propertyNameAndValue_in_objectLiteral3283 = frozenset([29, 67, 70])
    FOLLOW_LT_in_objectLiteral3287 = frozenset([29, 70])
    FOLLOW_70_in_objectLiteral3290 = frozenset([29, 30, 32, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_objectLiteral3292 = frozenset([29, 30, 32, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_propertyNameAndValue_in_objectLiteral3295 = frozenset([29, 67, 70])
    FOLLOW_LT_in_objectLiteral3299 = frozenset([29, 67, 70])
    FOLLOW_70_in_objectLiteral3303 = frozenset([29, 67])
    FOLLOW_LT_in_objectLiteral3305 = frozenset([29, 67])
    FOLLOW_67_in_objectLiteral3310 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue3334 = frozenset([29, 63])
    FOLLOW_LT_in_propertyNameAndValue3336 = frozenset([29, 63])
    FOLLOW_63_in_propertyNameAndValue3339 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_propertyNameAndValue3341 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_propertyNameAndValue3344 = frozenset([1])
    FOLLOW_138_in_propertyNameAndValue3366 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_139_in_propertyNameAndValue3370 = frozenset([33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3375 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_propertyNameAndValue3377 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3382 = frozenset([29, 69])
    FOLLOW_LT_in_propertyNameAndValue3384 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_propertyNameAndValue3387 = frozenset([29, 66])
    FOLLOW_LT_in_propertyNameAndValue3389 = frozenset([29, 66])
    FOLLOW_statementBlock_in_propertyNameAndValue3392 = frozenset([1])
    FOLLOW_138_in_propertyNameAndValue3425 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_139_in_propertyNameAndValue3429 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_LT_in_propertyNameAndValue3432 = frozenset([29, 33, 72, 73, 74, 85, 138, 139])
    FOLLOW_identifier_in_propertyNameAndValue3437 = frozenset([29, 69])
    FOLLOW_LT_in_propertyNameAndValue3439 = frozenset([29, 69])
    FOLLOW_formalParameterList_in_propertyNameAndValue3442 = frozenset([29, 66])
    FOLLOW_LT_in_propertyNameAndValue3444 = frozenset([29, 66])
    FOLLOW_statementBlock_in_propertyNameAndValue3447 = frozenset([1])
    FOLLOW_identifier_in_propertyName3482 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName3487 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName3492 = frozenset([1])
    FOLLOW_140_in_literal3504 = frozenset([1])
    FOLLOW_141_in_literal3513 = frozenset([1])
    FOLLOW_142_in_literal3522 = frozenset([1])
    FOLLOW_StringLiteral_in_literal3531 = frozenset([1])
    FOLLOW_NumericLiteral_in_literal3544 = frozenset([1])
    FOLLOW_regularExpressionLiteral_in_literal3557 = frozenset([1])
    FOLLOW_set_in_reFirstChar0 = frozenset([1])
    FOLLOW_reFirstChar_in_reChars3958 = frozenset([1])
    FOLLOW_100_in_reChars3963 = frozenset([1])
    FOLLOW_62_in_regularExpressionLiteral3977 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_reFirstChar_in_regularExpressionLiteral3979 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_reChars_in_regularExpressionLiteral3982 = frozenset([30, 32, 33, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143])
    FOLLOW_62_in_regularExpressionLiteral3985 = frozenset([1, 33])
    FOLLOW_Identifier_in_regularExpressionLiteral3987 = frozenset([1])
    FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral3993 = frozenset([1, 33])
    FOLLOW_Identifier_in_regularExpressionLiteral3995 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_LT_in_synpred1147 = frozenset([1])
    FOLLOW_LT_in_synpred3173 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_functionDeclaration_in_synpred5192 = frozenset([1])
    FOLLOW_66_in_synpred16399 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_synpred18449 = frozenset([1])
    FOLLOW_xmlStartTag_in_synpred19454 = frozenset([1])
    FOLLOW_LT_in_synpred22477 = frozenset([29, 31, 60, 66])
    FOLLOW_xmlPayload_in_synpred22480 = frozenset([1])
    FOLLOW_statementBlock_in_synpred38658 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred41673 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred48708 = frozenset([1])
    FOLLOW_LT_in_synpred55784 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_66_in_synpred58782 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred58784 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statementList_in_synpred58788 = frozenset([29, 67])
    FOLLOW_LT_in_synpred58791 = frozenset([29, 67])
    FOLLOW_67_in_synpred58795 = frozenset([1])
    FOLLOW_LT_in_synpred60823 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred61823 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_synpred61827 = frozenset([1])
    FOLLOW_LT_in_synpred761011 = frozenset([1])
    FOLLOW_LT_in_synpred771034 = frozenset([1])
    FOLLOW_LT_in_synpred801096 = frozenset([1])
    FOLLOW_LT_in_synpred821108 = frozenset([1])
    FOLLOW_LT_in_synpred841121 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred851115 = frozenset([29, 81])
    FOLLOW_81_in_synpred851119 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred851121 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89, 90, 92, 93, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_statement_in_synpred851125 = frozenset([1])
    FOLLOW_forStatement_in_synpred881149 = frozenset([1])
    FOLLOW_LT_in_synpred891168 = frozenset([1])
    FOLLOW_LT_in_synpred941217 = frozenset([1])
    FOLLOW_LT_in_synpred961229 = frozenset([1])
    FOLLOW_LT_in_synpred981254 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 77, 79, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1011269 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1041284 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1071298 = frozenset([1])
    FOLLOW_LT_in_synpred1111343 = frozenset([1])
    FOLLOW_LT_in_synpred1141356 = frozenset([1])
    FOLLOW_LT_in_synpred1161368 = frozenset([1])
    FOLLOW_LT_in_synpred1181380 = frozenset([1])
    FOLLOW_expression_in_synpred1261470 = frozenset([1])
    FOLLOW_LT_in_synpred1291500 = frozenset([1])
    FOLLOW_LT_in_synpred1311512 = frozenset([1])
    FOLLOW_LT_in_synpred1331535 = frozenset([1])
    FOLLOW_LT_in_synpred1351559 = frozenset([1])
    FOLLOW_LT_in_synpred1451633 = frozenset([1])
    FOLLOW_LT_in_synpred1471645 = frozenset([1])
    FOLLOW_statementList_in_synpred1481649 = frozenset([1])
    FOLLOW_LT_in_synpred1501670 = frozenset([1])
    FOLLOW_LT_in_synpred1641817 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1671844 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1701869 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred1711862 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_synpred1711864 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_synpred1711867 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1711869 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred1711872 = frozenset([1])
    FOLLOW_LT_in_synpred1731910 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_synpred1741903 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_LT_in_synpred1741905 = frozenset([29, 65, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
    FOLLOW_assignmentOperator_in_synpred1741908 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred1741910 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpressionNoIn_in_synpred1741913 = frozenset([1])
    FOLLOW_callExpression_in_synpred1751944 = frozenset([1])
    FOLLOW_memberExpression_in_synpred1761961 = frozenset([1])
    FOLLOW_LT_in_synpred1771968 = frozenset([1])
    FOLLOW_LT_in_synpred1791996 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_synpred1791999 = frozenset([1])
    FOLLOW_LT_in_synpred1822022 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_synpred1822026 = frozenset([1])
    FOLLOW_LT_in_synpred1842035 = frozenset([1])
    FOLLOW_LT_in_synpred1872046 = frozenset([29, 63, 97, 98])
    FOLLOW_memberExpressionSuffix_in_synpred1872049 = frozenset([1])
    FOLLOW_LT_in_synpred1912119 = frozenset([1])
    FOLLOW_LT_in_synpred1952131 = frozenset([29, 63, 69, 97, 98])
    FOLLOW_callExpressionSuffix_in_synpred1952134 = frozenset([1])
    FOLLOW_LT_in_synpred2002202 = frozenset([1])
    FOLLOW_LT_in_synpred2012207 = frozenset([1])
    FOLLOW_LT_in_synpred2022213 = frozenset([1])
    FOLLOW_LT_in_synpred2032218 = frozenset([1])
    FOLLOW_LT_in_synpred2072253 = frozenset([1])
    FOLLOW_LT_in_synpred2112342 = frozenset([1])
    FOLLOW_e4xIdentifier_in_synpred2122345 = frozenset([1])
    FOLLOW_LT_in_synpred2262449 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2282461 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2312487 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2332499 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2362525 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2392552 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2422579 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2452606 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2482633 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2512660 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2542687 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2572714 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2602741 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2632768 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2692809 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2752849 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2832898 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2842870 = frozenset([29, 60, 61, 86, 122, 123, 124])
    FOLLOW_set_in_synpred2842874 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2842898 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_shiftExpression_in_synpred2842902 = frozenset([1])
    FOLLOW_LT_in_synpred2902942 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2952978 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred2993010 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3002998 = frozenset([29, 64, 128])
    FOLLOW_set_in_synpred3003002 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3003010 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_multiplicativeExpression_in_synpred3003014 = frozenset([1])
    FOLLOW_LT_in_synpred3043046 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3053030 = frozenset([29, 62, 100, 129])
    FOLLOW_set_in_synpred3053034 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3053046 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_unaryExpression_in_synpred3053050 = frozenset([1])
    FOLLOW_LT_in_synpred3203142 = frozenset([29, 31, 60])
    FOLLOW_set_in_synpred3203145 = frozenset([1])
    FOLLOW_objectLiteral_in_synpred3243183 = frozenset([1])
    FOLLOW_LT_in_synpred3253190 = frozenset([1])
    FOLLOW_LT_in_synpred3273215 = frozenset([1])
    FOLLOW_LT_in_synpred3303228 = frozenset([1])
    FOLLOW_LT_in_synpred3323222 = frozenset([29, 70])
    FOLLOW_70_in_synpred3323225 = frozenset([1, 29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_LT_in_synpred3323228 = frozenset([29, 30, 31, 32, 33, 34, 60, 62, 64, 66, 68, 69, 72, 73, 74, 85, 96, 98, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142])
    FOLLOW_assignmentExpression_in_synpred3323231 = frozenset([1])
    FOLLOW_LT_in_synpred3363280 = frozenset([1])
    FOLLOW_LT_in_synpred3453341 = frozenset([1])
    FOLLOW_reFirstChar_in_synpred4443979 = frozenset([1])

