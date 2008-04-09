# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-09 13:55:28

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
LT=16
HexEscapeSequence=28
LineComment=45
DecimalDigit=33
PROP=12
EOF=-1
HexDigit=34
RegularExpressionHacks=21
Identifier=20
SingleStringCharacter=26
XMLComment=18
Comment=44
OBJ=11
SingleEscapeCharacter=30
PROPREF=13
ExponentPart=37
UnicodeLetter=40
EscapeCharacter=32
WhiteSpace=46
VARDEFS=15
VARDEF=14
INDEXREF=9
IdentifierPart=39
UnicodeCombiningMark=43
UnicodeDigit=41
NumericLiteral=19
RegularExpressionChars=22
UnicodeEscapeSequence=29
IdentifierStart=38
DoubleStringCharacter=25
DecimalLiteral=35
NSREF=10
DESCREF=7
StringLiteral=17
RegularExpressionFirstChar=24
FUNC=8
HexIntegerLiteral=36
NonEscapeCharacter=31
CALL=5
DEFAULTNS=6
CharacterEscapeSequence=27
EscapeSequence=23
ANONYMOUS=4
UnicodeConnectorPunctuation=42

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ANONYMOUS", "CALL", "DEFAULTNS", "DESCREF", "FUNC", "INDEXREF", "NSREF", 
    "OBJ", "PROP", "PROPREF", "VARDEF", "VARDEFS", "LT", "StringLiteral", 
    "XMLComment", "NumericLiteral", "Identifier", "RegularExpressionHacks", 
    "RegularExpressionChars", "EscapeSequence", "RegularExpressionFirstChar", 
    "DoubleStringCharacter", "SingleStringCharacter", "CharacterEscapeSequence", 
    "HexEscapeSequence", "UnicodeEscapeSequence", "SingleEscapeCharacter", 
    "NonEscapeCharacter", "EscapeCharacter", "DecimalDigit", "HexDigit", 
    "DecimalLiteral", "HexIntegerLiteral", "ExponentPart", "IdentifierStart", 
    "IdentifierPart", "UnicodeLetter", "UnicodeDigit", "UnicodeConnectorPunctuation", 
    "UnicodeCombiningMark", "Comment", "LineComment", "WhiteSpace", "'<'", 
    "'>'", "'/'", "':'", "'-'", "'='", "'{'", "'}'", "'function'", "'('", 
    "','", "')'", "'default'", "'xml'", "'namespace'", "';'", "'return'", 
    "'var'", "'const'", "'if'", "'else'", "'do'", "'while'", "'for'", "'each'", 
    "'in'", "'continue'", "'break'", "'with'", "'switch'", "'case'", "'throw'", 
    "'try'", "'catch'", "'finally'", "'new'", "'.'", "'['", "']'", "'*'", 
    "'*='", "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", 
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
        self.dfa166 = self.DFA166(
            self, 166,
            eot = self.DFA166_eot,
            eof = self.DFA166_eof,
            min = self.DFA166_min,
            max = self.DFA166_max,
            accept = self.DFA166_accept,
            special = self.DFA166_special,
            transition = self.DFA166_transition
            )
        self.dfa179 = self.DFA179(
            self, 179,
            eot = self.DFA179_eot,
            eof = self.DFA179_eof,
            min = self.DFA179_min,
            max = self.DFA179_max,
            accept = self.DFA179_accept,
            special = self.DFA179_special,
            transition = self.DFA179_transition
            )
        self.dfa184 = self.DFA184(
            self, 184,
            eot = self.DFA184_eot,
            eof = self.DFA184_eof,
            min = self.DFA184_min,
            max = self.DFA184_max,
            accept = self.DFA184_accept,
            special = self.DFA184_special,
            transition = self.DFA184_transition
            )
        self.dfa187 = self.DFA187(
            self, 187,
            eot = self.DFA187_eot,
            eof = self.DFA187_eof,
            min = self.DFA187_min,
            max = self.DFA187_max,
            accept = self.DFA187_accept,
            special = self.DFA187_special,
            transition = self.DFA187_transition
            )
        self.dfa190 = self.DFA190(
            self, 190,
            eot = self.DFA190_eot,
            eof = self.DFA190_eof,
            min = self.DFA190_min,
            max = self.DFA190_max,
            accept = self.DFA190_accept,
            special = self.DFA190_special,
            transition = self.DFA190_transition
            )
        self.dfa193 = self.DFA193(
            self, 193,
            eot = self.DFA193_eot,
            eof = self.DFA193_eof,
            min = self.DFA193_min,
            max = self.DFA193_max,
            accept = self.DFA193_accept,
            special = self.DFA193_special,
            transition = self.DFA193_transition
            )
        self.dfa196 = self.DFA196(
            self, 196,
            eot = self.DFA196_eot,
            eof = self.DFA196_eof,
            min = self.DFA196_min,
            max = self.DFA196_max,
            accept = self.DFA196_accept,
            special = self.DFA196_special,
            transition = self.DFA196_transition
            )
        self.dfa199 = self.DFA199(
            self, 199,
            eot = self.DFA199_eot,
            eof = self.DFA199_eof,
            min = self.DFA199_min,
            max = self.DFA199_max,
            accept = self.DFA199_accept,
            special = self.DFA199_special,
            transition = self.DFA199_transition
            )
        self.dfa202 = self.DFA202(
            self, 202,
            eot = self.DFA202_eot,
            eof = self.DFA202_eof,
            min = self.DFA202_min,
            max = self.DFA202_max,
            accept = self.DFA202_accept,
            special = self.DFA202_special,
            transition = self.DFA202_transition
            )
        self.dfa205 = self.DFA205(
            self, 205,
            eot = self.DFA205_eot,
            eof = self.DFA205_eof,
            min = self.DFA205_min,
            max = self.DFA205_max,
            accept = self.DFA205_accept,
            special = self.DFA205_special,
            transition = self.DFA205_transition
            )
        self.dfa208 = self.DFA208(
            self, 208,
            eot = self.DFA208_eot,
            eof = self.DFA208_eof,
            min = self.DFA208_min,
            max = self.DFA208_max,
            accept = self.DFA208_accept,
            special = self.DFA208_special,
            transition = self.DFA208_transition
            )
        self.dfa211 = self.DFA211(
            self, 211,
            eot = self.DFA211_eot,
            eof = self.DFA211_eof,
            min = self.DFA211_min,
            max = self.DFA211_max,
            accept = self.DFA211_accept,
            special = self.DFA211_special,
            transition = self.DFA211_transition
            )
        self.dfa214 = self.DFA214(
            self, 214,
            eot = self.DFA214_eot,
            eof = self.DFA214_eof,
            min = self.DFA214_min,
            max = self.DFA214_max,
            accept = self.DFA214_accept,
            special = self.DFA214_special,
            transition = self.DFA214_transition
            )
        self.dfa217 = self.DFA217(
            self, 217,
            eot = self.DFA217_eot,
            eof = self.DFA217_eof,
            min = self.DFA217_min,
            max = self.DFA217_max,
            accept = self.DFA217_accept,
            special = self.DFA217_special,
            transition = self.DFA217_transition
            )
        self.dfa220 = self.DFA220(
            self, 220,
            eot = self.DFA220_eot,
            eof = self.DFA220_eof,
            min = self.DFA220_min,
            max = self.DFA220_max,
            accept = self.DFA220_accept,
            special = self.DFA220_special,
            transition = self.DFA220_transition
            )
        self.dfa226 = self.DFA226(
            self, 226,
            eot = self.DFA226_eot,
            eof = self.DFA226_eof,
            min = self.DFA226_min,
            max = self.DFA226_max,
            accept = self.DFA226_accept,
            special = self.DFA226_special,
            transition = self.DFA226_transition
            )
        self.dfa229 = self.DFA229(
            self, 229,
            eot = self.DFA229_eot,
            eof = self.DFA229_eof,
            min = self.DFA229_min,
            max = self.DFA229_max,
            accept = self.DFA229_accept,
            special = self.DFA229_special,
            transition = self.DFA229_transition
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
        self.dfa245 = self.DFA245(
            self, 245,
            eot = self.DFA245_eot,
            eof = self.DFA245_eof,
            min = self.DFA245_min,
            max = self.DFA245_max,
            accept = self.DFA245_accept,
            special = self.DFA245_special,
            transition = self.DFA245_transition
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
        self.dfa268 = self.DFA268(
            self, 268,
            eot = self.DFA268_eot,
            eof = self.DFA268_eof,
            min = self.DFA268_min,
            max = self.DFA268_max,
            accept = self.DFA268_accept,
            special = self.DFA268_special,
            transition = self.DFA268_transition
            )
        self.dfa290 = self.DFA290(
            self, 290,
            eot = self.DFA290_eot,
            eof = self.DFA290_eof,
            min = self.DFA290_min,
            max = self.DFA290_max,
            accept = self.DFA290_accept,
            special = self.DFA290_special,
            transition = self.DFA290_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class program_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start program
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:1: program : ( LT )* sourceElements ( LT )* EOF ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:2: ( ( LT )* sourceElements ( LT )* EOF )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: ( LT )* sourceElements ( LT )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:6: ( LT )*
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
                        self.match(self.input, LT, self.FOLLOW_LT_in_program96)
                        if self.failed:
                            return retval


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_sourceElements_in_program100)
                sourceElements2 = self.sourceElements()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElements2.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT3 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program102)
                        if self.failed:
                            return retval


                    else:
                        break #loop2


                EOF4 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_program106)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:36:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:2: ( sourceElement ( ( LT )* sourceElement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:4: sourceElement ( ( LT )* sourceElement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_sourceElement_in_sourceElements119)
                sourceElement5 = self.sourceElement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElement5.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:19: ( LT )* sourceElement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:21: ( LT )*
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
                                self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements122)
                                if self.failed:
                                    return retval


                            else:
                                break #loop3


                        self.following.append(self.FOLLOW_sourceElement_in_sourceElements126)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:40:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:41:2: ( ( functionDeclaration )=> functionDeclaration | statement )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 55) :
                    LA5_1 = self.input.LA(2)

                    if (self.synpred5()) :
                        alt5 = 1
                    elif (True) :
                        alt5 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("40:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 1, self.input)

                        raise nvae

                elif ((LT <= LA5_0 <= RegularExpressionHacks) or LA5_0 == 47 or LA5_0 == 49 or LA5_0 == 51 or LA5_0 == 53 or LA5_0 == 56 or (59 <= LA5_0 <= 66) or (68 <= LA5_0 <= 71) or (73 <= LA5_0 <= 76) or (78 <= LA5_0 <= 79) or LA5_0 == 82 or LA5_0 == 84 or LA5_0 == 114 or (116 <= LA5_0 <= 128)) :
                    alt5 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("40:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:41:4: ( functionDeclaration )=> functionDeclaration
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionDeclaration_in_sourceElement145)
                    functionDeclaration8 = self.functionDeclaration()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:42:4: statement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statement_in_sourceElement150)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:1: xmlStartTag options {backtrack=false; } : '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>' ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:2: ( '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:4: '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '>'
                root_0 = self.adaptor.nil()

                char_literal10 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_xmlStartTag168)
                if self.failed:
                    return retval

                char_literal10_tree = self.adaptor.createWithPayload(char_literal10)
                self.adaptor.addChild(root_0, char_literal10_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlStartTag170)
                xmlTagName11 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName11.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:19: ( ( LT )* xmlAttribute )*
                while True: #loop7
                    alt7 = 2
                    alt7 = self.dfa7.predict(self.input)
                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:20: ( LT )* xmlAttribute
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:22: ( LT )*
                        while True: #loop6
                            alt6 = 2
                            LA6_0 = self.input.LA(1)

                            if (LA6_0 == LT) :
                                alt6 = 1


                            if alt6 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT12 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlStartTag173)
                                if self.failed:
                                    return retval


                            else:
                                break #loop6


                        self.following.append(self.FOLLOW_xmlAttribute_in_xmlStartTag177)
                        xmlAttribute13 = self.xmlAttribute()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, xmlAttribute13.tree)


                    else:
                        break #loop7


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:42: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT14 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_xmlStartTag181)
                        if self.failed:
                            return retval


                    else:
                        break #loop8


                char_literal15 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_xmlStartTag185)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:50:1: xmlEndTag options {backtrack=false; } : '<' '/' xmlTagName '>' ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:2: ( '<' '/' xmlTagName '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:4: '<' '/' xmlTagName '>'
                root_0 = self.adaptor.nil()

                char_literal16 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_xmlEndTag203)
                if self.failed:
                    return retval

                char_literal16_tree = self.adaptor.createWithPayload(char_literal16)
                self.adaptor.addChild(root_0, char_literal16_tree)

                char_literal17 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_xmlEndTag205)
                if self.failed:
                    return retval

                char_literal17_tree = self.adaptor.createWithPayload(char_literal17)
                self.adaptor.addChild(root_0, char_literal17_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlEndTag207)
                xmlTagName18 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName18.tree)
                char_literal19 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_xmlEndTag209)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:1: xmlEmptyTag options {backtrack=false; } : '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>' ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:2: ( '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:4: '<' xmlTagName ( ( LT )* xmlAttribute )* ( LT )* '/' '>'
                root_0 = self.adaptor.nil()

                char_literal20 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_xmlEmptyTag227)
                if self.failed:
                    return retval

                char_literal20_tree = self.adaptor.createWithPayload(char_literal20)
                self.adaptor.addChild(root_0, char_literal20_tree)

                self.following.append(self.FOLLOW_xmlTagName_in_xmlEmptyTag229)
                xmlTagName21 = self.xmlTagName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlTagName21.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:19: ( ( LT )* xmlAttribute )*
                while True: #loop10
                    alt10 = 2
                    alt10 = self.dfa10.predict(self.input)
                    if alt10 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:20: ( LT )* xmlAttribute
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:22: ( LT )*
                        while True: #loop9
                            alt9 = 2
                            LA9_0 = self.input.LA(1)

                            if (LA9_0 == LT) :
                                alt9 = 1


                            if alt9 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT22 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlEmptyTag232)
                                if self.failed:
                                    return retval


                            else:
                                break #loop9


                        self.following.append(self.FOLLOW_xmlAttribute_in_xmlEmptyTag236)
                        xmlAttribute23 = self.xmlAttribute()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, xmlAttribute23.tree)


                    else:
                        break #loop10


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:42: ( LT )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == LT) :
                        alt11 = 1


                    if alt11 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT24 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_xmlEmptyTag240)
                        if self.failed:
                            return retval


                    else:
                        break #loop11


                char_literal25 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_xmlEmptyTag244)
                if self.failed:
                    return retval

                char_literal25_tree = self.adaptor.createWithPayload(char_literal25)
                self.adaptor.addChild(root_0, char_literal25_tree)

                char_literal26 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_xmlEmptyTag246)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:1: xmlTagName options {backtrack=false; } : identifier ( ( ':' | '-' ) identifier )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:2: ( identifier ( ( ':' | '-' ) identifier )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:4: identifier ( ( ':' | '-' ) identifier )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_xmlTagName264)
                identifier27 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier27.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:15: ( ( ':' | '-' ) identifier )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((50 <= LA12_0 <= 51)) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:17: ( ':' | '-' ) identifier
                        set28 = self.input.LT(1)
                        if (50 <= self.input.LA(1) <= 51):
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
                                self.input, mse, self.FOLLOW_set_in_xmlTagName268
                                )
                            raise mse


                        self.following.append(self.FOLLOW_identifier_in_xmlTagName274)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:65:1: xmlAttribute options {backtrack=false; } : xmlAttributeName '=' xmlAttributeValue ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:2: ( xmlAttributeName '=' xmlAttributeValue )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: xmlAttributeName '=' xmlAttributeValue
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_xmlAttributeName_in_xmlAttribute294)
                xmlAttributeName30 = self.xmlAttributeName()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, xmlAttributeName30.tree)
                char_literal31 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_xmlAttribute296)
                if self.failed:
                    return retval

                char_literal31_tree = self.adaptor.createWithPayload(char_literal31)
                self.adaptor.addChild(root_0, char_literal31_tree)

                self.following.append(self.FOLLOW_xmlAttributeValue_in_xmlAttribute298)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:71:1: xmlAttributeName options {backtrack=false; } : identifier ( ( ':' | '-' ) identifier )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:2: ( identifier ( ( ':' | '-' ) identifier )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:4: identifier ( ( ':' | '-' ) identifier )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_xmlAttributeName317)
                identifier33 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier33.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:15: ( ( ':' | '-' ) identifier )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((50 <= LA13_0 <= 51)) :
                        alt13 = 1


                    if alt13 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:17: ( ':' | '-' ) identifier
                        set34 = self.input.LT(1)
                        if (50 <= self.input.LA(1) <= 51):
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
                                self.input, mse, self.FOLLOW_set_in_xmlAttributeName321
                                )
                            raise mse


                        self.following.append(self.FOLLOW_identifier_in_xmlAttributeName327)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:76:1: xmlAttributeValue options {backtrack=false; } : ( ( '{' )=> e4xSplice | StringLiteral );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:2: ( ( '{' )=> e4xSplice | StringLiteral )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 53) and (self.synpred16()):
                    alt14 = 1
                elif (LA14_0 == StringLiteral) :
                    alt14 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("76:1: xmlAttributeValue options {backtrack=false; } : ( ( '{' )=> e4xSplice | StringLiteral );", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:4: ( '{' )=> e4xSplice
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_e4xSplice_in_xmlAttributeValue352)
                    e4xSplice36 = self.e4xSplice()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, e4xSplice36.tree)


                elif alt14 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:79:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral37 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_xmlAttributeValue357)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:1: e4xSplice options {backtrack=false; } : '{' expression '}' ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:84:2: ( '{' expression '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:84:4: '{' expression '}'
                root_0 = self.adaptor.nil()

                char_literal38 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_e4xSplice375)
                if self.failed:
                    return retval

                char_literal38_tree = self.adaptor.createWithPayload(char_literal38)
                self.adaptor.addChild(root_0, char_literal38_tree)

                self.following.append(self.FOLLOW_expression_in_e4xSplice377)
                expression39 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression39.tree)
                char_literal40 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_e4xSplice379)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:87:1: xmlPayload : ( xmlEndTag | xmlEmptyTag | xmlStartTag | e4xSplice | XMLComment );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:96:2: ( xmlEndTag | xmlEmptyTag | xmlStartTag | e4xSplice | XMLComment )
                alt15 = 5
                alt15 = self.dfa15.predict(self.input)
                if alt15 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:96:4: xmlEndTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlEndTag_in_xmlPayload393)
                    xmlEndTag41 = self.xmlEndTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlEndTag41.tree)


                elif alt15 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:4: xmlEmptyTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlEmptyTag_in_xmlPayload398)
                    xmlEmptyTag42 = self.xmlEmptyTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlEmptyTag42.tree)


                elif alt15 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:4: xmlStartTag
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlStartTag_in_xmlPayload403)
                    xmlStartTag43 = self.xmlStartTag()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlStartTag43.tree)


                elif alt15 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:4: e4xSplice
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_e4xSplice_in_xmlPayload408)
                    e4xSplice44 = self.e4xSplice()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, e4xSplice44.tree)


                elif alt15 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:100:4: XMLComment
                    root_0 = self.adaptor.nil()

                    XMLComment45 = self.input.LT(1)
                    self.match(self.input, XMLComment, self.FOLLOW_XMLComment_in_xmlPayload413)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:103:1: xmlLiteral : ( ( LT )* xmlPayload )+ ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:2: ( ( ( LT )* xmlPayload )+ )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:4: ( ( LT )* xmlPayload )+
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:4: ( ( LT )* xmlPayload )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17 = self.input.LA(1)
                    if LA17 == LT:
                        LA17_1 = self.input.LA(2)

                        if (self.synpred22()) :
                            alt17 = 1


                    elif LA17 == 47:
                        LA17_11 = self.input.LA(2)

                        if (self.synpred22()) :
                            alt17 = 1


                    elif LA17 == XMLComment or LA17 == 53:
                        alt17 = 1

                    if alt17 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:5: ( LT )* xmlPayload
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:5: ( LT )*
                        while True: #loop16
                            alt16 = 2
                            LA16_0 = self.input.LA(1)

                            if (LA16_0 == LT) :
                                alt16 = 1


                            if alt16 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT46 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_xmlLiteral426)
                                if self.failed:
                                    return retval

                                LT46_tree = self.adaptor.createWithPayload(LT46)
                                self.adaptor.addChild(root_0, LT46_tree)



                            else:
                                break #loop16


                        self.following.append(self.FOLLOW_xmlPayload_in_xmlLiteral429)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:1: functionDeclaration : 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_55 = RewriteRuleTokenStream(self.adaptor, "token 55")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                string_literal48 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_functionDeclaration444)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_55.add(string_literal48)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:15: ( LT )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == LT) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT49 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration446)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT49)


                    else:
                        break #loop18


                self.following.append(self.FOLLOW_identifier_in_functionDeclaration449)
                identifier50 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier50.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:30: ( LT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == LT) :
                        alt19 = 1


                    if alt19 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT51 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration451)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT51)


                    else:
                        break #loop19


                self.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration454)
                formalParameterList52 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList52.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:111:54: ( LT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == LT) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT53 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration456)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT53)


                    else:
                        break #loop20


                self.following.append(self.FOLLOW_statementBlock_in_functionDeclaration459)
                statementBlock54 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_statementBlock.add(statementBlock54.tree)
                # AST Rewrite
                # elements: formalParameterList, statementBlock, identifier
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
                    # 112:3: -> ^( FUNC identifier formalParameterList statementBlock )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:112:6: ^( FUNC identifier formalParameterList statementBlock )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:115:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS formalParameterList statementBlock ) );
    def functionExpression(self, ):

        retval = self.functionExpression_return()
        retval.start = self.input.LT(1)
        functionExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal55 = None
        LT56 = None
        LT58 = None
        LT60 = None
        string_literal62 = None
        LT63 = None
        LT65 = None
        identifier57 = None

        formalParameterList59 = None

        statementBlock61 = None

        formalParameterList64 = None

        statementBlock66 = None


        string_literal55_tree = None
        LT56_tree = None
        LT58_tree = None
        LT60_tree = None
        string_literal62_tree = None
        LT63_tree = None
        LT65_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_55 = RewriteRuleTokenStream(self.adaptor, "token 55")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                alt26 = 2
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                    string_literal55 = self.input.LT(1)
                    self.match(self.input, 55, self.FOLLOW_55_in_functionExpression485)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_55.add(string_literal55)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:15: ( LT )*
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == LT) :
                            alt21 = 1


                        if alt21 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT56 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression487)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT56)


                        else:
                            break #loop21


                    self.following.append(self.FOLLOW_identifier_in_functionExpression490)
                    identifier57 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier57.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:30: ( LT )*
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == LT) :
                            alt22 = 1


                        if alt22 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT58 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression492)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT58)


                        else:
                            break #loop22


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression495)
                    formalParameterList59 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList59.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:54: ( LT )*
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == LT) :
                            alt23 = 1


                        if alt23 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT60 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression497)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT60)


                        else:
                            break #loop23


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression500)
                    statementBlock61 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock61.tree)
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
                        # 117:3: -> ^( FUNC identifier formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:6: ^( FUNC identifier formalParameterList statementBlock )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_statementBlock.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt26 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:4: 'function' ( LT )* formalParameterList ( LT )* statementBlock
                    string_literal62 = self.input.LT(1)
                    self.match(self.input, 55, self.FOLLOW_55_in_functionExpression519)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_55.add(string_literal62)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:15: ( LT )*
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == LT) :
                            alt24 = 1


                        if alt24 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT63 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression521)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT63)


                        else:
                            break #loop24


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression524)
                    formalParameterList64 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList64.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:39: ( LT )*
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == LT) :
                            alt25 = 1


                        if alt25 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT65 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression526)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT65)


                        else:
                            break #loop25


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression529)
                    statementBlock66 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock66.tree)
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
                        # 119:3: -> ^( FUNC ANONYMOUS formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:119:6: ^( FUNC ANONYMOUS formalParameterList statementBlock )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, self.adaptor.createFromType(ANONYMOUS, "ANONYMOUS"))
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:122:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal67 = None
        LT68 = None
        LT70 = None
        char_literal71 = None
        LT72 = None
        LT74 = None
        char_literal75 = None
        identifier69 = None

        identifier73 = None


        char_literal67_tree = None
        LT68_tree = None
        LT70_tree = None
        char_literal71_tree = None
        LT72_tree = None
        LT74_tree = None
        char_literal75_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal67 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_formalParameterList555)
                if self.failed:
                    return retval

                char_literal67_tree = self.adaptor.createWithPayload(char_literal67)
                self.adaptor.addChild(root_0, char_literal67_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt31 = 2
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:11: ( LT )*
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == LT) :
                            alt27 = 1


                        if alt27 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT68 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList558)
                            if self.failed:
                                return retval


                        else:
                            break #loop27


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList562)
                    identifier69 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier69.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:25: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop30
                        alt30 = 2
                        alt30 = self.dfa30.predict(self.input)
                        if alt30 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:26: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:28: ( LT )*
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == LT) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT70 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList565)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop28


                            char_literal71 = self.input.LT(1)
                            self.match(self.input, 57, self.FOLLOW_57_in_formalParameterList569)
                            if self.failed:
                                return retval

                            char_literal71_tree = self.adaptor.createWithPayload(char_literal71)
                            self.adaptor.addChild(root_0, char_literal71_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:37: ( LT )*
                            while True: #loop29
                                alt29 = 2
                                LA29_0 = self.input.LA(1)

                                if (LA29_0 == LT) :
                                    alt29 = 1


                                if alt29 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT72 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList571)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop29


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList575)
                            identifier73 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, identifier73.tree)


                        else:
                            break #loop30





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:57: ( LT )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == LT) :
                        alt32 = 1


                    if alt32 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT74 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList581)
                        if self.failed:
                            return retval


                    else:
                        break #loop32


                char_literal75 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_formalParameterList585)
                if self.failed:
                    return retval

                char_literal75_tree = self.adaptor.createWithPayload(char_literal75)
                self.adaptor.addChild(root_0, char_literal75_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        statementBlock76 = None

        variableStatement77 = None

        emptyStatement78 = None

        expressionStatement79 = None

        ifStatement80 = None

        iterationStatement81 = None

        continueStatement82 = None

        breakStatement83 = None

        returnStatement84 = None

        withStatement85 = None

        labelledStatement86 = None

        switchStatement87 = None

        throwStatement88 = None

        tryStatement89 = None

        defaultXmlNamespaceStatement90 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement )
                alt33 = 15
                LA33 = self.input.LA(1)
                if LA33 == 53:
                    LA33_1 = self.input.LA(2)

                    if (self.synpred38()) :
                        alt33 = 1
                    elif (self.synpred41()) :
                        alt33 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("127:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 1, self.input)

                        raise nvae

                elif LA33 == 64 or LA33 == 65:
                    alt33 = 2
                elif LA33 == 62:
                    alt33 = 3
                elif LA33 == LT or LA33 == StringLiteral or LA33 == XMLComment or LA33 == NumericLiteral or LA33 == RegularExpressionHacks or LA33 == 47 or LA33 == 49 or LA33 == 51 or LA33 == 55 or LA33 == 56 or LA33 == 82 or LA33 == 84 or LA33 == 114 or LA33 == 116 or LA33 == 117 or LA33 == 118 or LA33 == 119 or LA33 == 120 or LA33 == 121 or LA33 == 122 or LA33 == 123 or LA33 == 126 or LA33 == 127 or LA33 == 128:
                    alt33 = 4
                elif LA33 == 59:
                    LA33_9 = self.input.LA(2)

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

                        nvae = NoViableAltException("127:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 9, self.input)

                        raise nvae

                elif LA33 == 66:
                    alt33 = 5
                elif LA33 == 68 or LA33 == 69 or LA33 == 70:
                    alt33 = 6
                elif LA33 == 73:
                    alt33 = 7
                elif LA33 == 74:
                    alt33 = 8
                elif LA33 == 63:
                    alt33 = 9
                elif LA33 == 75:
                    alt33 = 10
                elif LA33 == 76:
                    alt33 = 12
                elif LA33 == 78:
                    alt33 = 13
                elif LA33 == 79:
                    alt33 = 14
                elif LA33 == Identifier or LA33 == 60 or LA33 == 61 or LA33 == 71 or LA33 == 124 or LA33 == 125:
                    LA33_33 = self.input.LA(2)

                    if (self.synpred41()) :
                        alt33 = 4
                    elif (self.synpred48()) :
                        alt33 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("127:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 33, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("127:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement | defaultXmlNamespaceStatement );", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement597)
                    statementBlock76 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock76.tree)


                elif alt33 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement602)
                    variableStatement77 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement77.tree)


                elif alt33 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement607)
                    emptyStatement78 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement78.tree)


                elif alt33 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement612)
                    expressionStatement79 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement79.tree)


                elif alt33 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement617)
                    ifStatement80 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement80.tree)


                elif alt33 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement622)
                    iterationStatement81 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement81.tree)


                elif alt33 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:134:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement627)
                    continueStatement82 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement82.tree)


                elif alt33 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement632)
                    breakStatement83 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement83.tree)


                elif alt33 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement637)
                    returnStatement84 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement84.tree)


                elif alt33 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement642)
                    withStatement85 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement85.tree)


                elif alt33 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement647)
                    labelledStatement86 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement86.tree)


                elif alt33 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:139:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement652)
                    switchStatement87 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement87.tree)


                elif alt33 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement657)
                    throwStatement88 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement88.tree)


                elif alt33 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement662)
                    tryStatement89 = self.tryStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, tryStatement89.tree)


                elif alt33 == 15:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:4: defaultXmlNamespaceStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_defaultXmlNamespaceStatement_in_statement667)
                    defaultXmlNamespaceStatement90 = self.defaultXmlNamespaceStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultXmlNamespaceStatement90.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:1: defaultXmlNamespaceStatement : 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) ;
    def defaultXmlNamespaceStatement(self, ):

        retval = self.defaultXmlNamespaceStatement_return()
        retval.start = self.input.LT(1)
        defaultXmlNamespaceStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal91 = None
        string_literal92 = None
        string_literal93 = None
        LT94 = None
        char_literal95 = None
        LT96 = None
        LT98 = None
        char_literal99 = None
        identifier97 = None


        string_literal91_tree = None
        string_literal92_tree = None
        string_literal93_tree = None
        LT94_tree = None
        char_literal95_tree = None
        LT96_tree = None
        LT98_tree = None
        char_literal99_tree = None
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_62 = RewriteRuleTokenStream(self.adaptor, "token 62")
        stream_60 = RewriteRuleTokenStream(self.adaptor, "token 60")
        stream_61 = RewriteRuleTokenStream(self.adaptor, "token 61")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:2: ( 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' ) -> ^( DEFAULTNS identifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: 'default' 'xml' 'namespace' ( LT )* '=' ( LT )* identifier ( LT | ';' )
                string_literal91 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_defaultXmlNamespaceStatement678)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_59.add(string_literal91)
                string_literal92 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_defaultXmlNamespaceStatement680)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_60.add(string_literal92)
                string_literal93 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_defaultXmlNamespaceStatement682)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_61.add(string_literal93)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:32: ( LT )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == LT) :
                        alt34 = 1


                    if alt34 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT94 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement684)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT94)


                    else:
                        break #loop34


                char_literal95 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_defaultXmlNamespaceStatement687)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_52.add(char_literal95)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:40: ( LT )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == LT) :
                        alt35 = 1


                    if alt35 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT96 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement689)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT96)


                    else:
                        break #loop35


                self.following.append(self.FOLLOW_identifier_in_defaultXmlNamespaceStatement692)
                identifier97 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier97.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:55: ( LT | ';' )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == LT) :
                    alt36 = 1
                elif (LA36_0 == 62) :
                    alt36 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("146:55: ( LT | ';' )", 36, 0, self.input)

                    raise nvae

                if alt36 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:56: LT
                    LT98 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_defaultXmlNamespaceStatement695)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT98)


                elif alt36 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:61: ';'
                    char_literal99 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_defaultXmlNamespaceStatement699)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_62.add(char_literal99)



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
                    # 147:3: -> ^( DEFAULTNS identifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:147:6: ^( DEFAULTNS identifier )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal100 = None
        LT101 = None
        LT103 = None
        char_literal104 = None
        char_literal105 = None
        string_literal106 = None
        char_literal108 = None
        statementList102 = None

        expression107 = None


        char_literal100_tree = None
        LT101_tree = None
        LT103_tree = None
        char_literal104_tree = None
        char_literal105_tree = None
        string_literal106_tree = None
        char_literal108_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == 53) :
                    LA41_1 = self.input.LA(2)

                    if (self.synpred58()) :
                        alt41 = 1
                    elif (True) :
                        alt41 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("150:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 41, 1, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("150:1: statementBlock : ( '{' ( LT )* ( statementList )? ( LT )* '}' | '{' ( 'return' )? expression '}' );", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                    root_0 = self.adaptor.nil()

                    char_literal100 = self.input.LT(1)
                    self.match(self.input, 53, self.FOLLOW_53_in_statementBlock721)
                    if self.failed:
                        return retval

                    char_literal100_tree = self.adaptor.createWithPayload(char_literal100)
                    self.adaptor.addChild(root_0, char_literal100_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:10: ( LT )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LT) :
                            LA37_2 = self.input.LA(2)

                            if (self.synpred55()) :
                                alt37 = 1




                        if alt37 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT101 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock723)
                            if self.failed:
                                return retval


                        else:
                            break #loop37


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:13: ( statementList )?
                    alt38 = 2
                    alt38 = self.dfa38.predict(self.input)
                    if alt38 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                        self.following.append(self.FOLLOW_statementList_in_statementBlock727)
                        statementList102 = self.statementList()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statementList102.tree)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:30: ( LT )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == LT) :
                            alt39 = 1


                        if alt39 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT103 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock730)
                            if self.failed:
                                return retval


                        else:
                            break #loop39


                    char_literal104 = self.input.LT(1)
                    self.match(self.input, 54, self.FOLLOW_54_in_statementBlock734)
                    if self.failed:
                        return retval

                    char_literal104_tree = self.adaptor.createWithPayload(char_literal104)
                    self.adaptor.addChild(root_0, char_literal104_tree)



                elif alt41 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:152:4: '{' ( 'return' )? expression '}'
                    root_0 = self.adaptor.nil()

                    char_literal105 = self.input.LT(1)
                    self.match(self.input, 53, self.FOLLOW_53_in_statementBlock739)
                    if self.failed:
                        return retval

                    char_literal105_tree = self.adaptor.createWithPayload(char_literal105)
                    self.adaptor.addChild(root_0, char_literal105_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:152:8: ( 'return' )?
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 63) :
                        alt40 = 1
                    if alt40 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'return'
                        string_literal106 = self.input.LT(1)
                        self.match(self.input, 63, self.FOLLOW_63_in_statementBlock741)
                        if self.failed:
                            return retval

                        string_literal106_tree = self.adaptor.createWithPayload(string_literal106)
                        self.adaptor.addChild(root_0, string_literal106_tree)




                    self.following.append(self.FOLLOW_expression_in_statementBlock744)
                    expression107 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression107.tree)
                    char_literal108 = self.input.LT(1)
                    self.match(self.input, 54, self.FOLLOW_54_in_statementBlock746)
                    if self.failed:
                        return retval

                    char_literal108_tree = self.adaptor.createWithPayload(char_literal108)
                    self.adaptor.addChild(root_0, char_literal108_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT110 = None
        statement109 = None

        statement111 = None


        LT110_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList759)
                statement109 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement109.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:14: ( ( LT )* statement )*
                while True: #loop43
                    alt43 = 2
                    LA43 = self.input.LA(1)
                    if LA43 == LT:
                        LA43_1 = self.input.LA(2)

                        if (self.synpred61()) :
                            alt43 = 1


                    elif LA43 == 59:
                        LA43_3 = self.input.LA(2)

                        if (self.synpred61()) :
                            alt43 = 1


                    elif LA43 == StringLiteral or LA43 == XMLComment or LA43 == NumericLiteral or LA43 == Identifier or LA43 == RegularExpressionHacks or LA43 == 47 or LA43 == 49 or LA43 == 51 or LA43 == 53 or LA43 == 55 or LA43 == 56 or LA43 == 60 or LA43 == 61 or LA43 == 62 or LA43 == 63 or LA43 == 64 or LA43 == 65 or LA43 == 66 or LA43 == 68 or LA43 == 69 or LA43 == 70 or LA43 == 71 or LA43 == 73 or LA43 == 74 or LA43 == 75 or LA43 == 76 or LA43 == 78 or LA43 == 79 or LA43 == 82 or LA43 == 84 or LA43 == 114 or LA43 == 116 or LA43 == 117 or LA43 == 118 or LA43 == 119 or LA43 == 120 or LA43 == 121 or LA43 == 122 or LA43 == 123 or LA43 == 124 or LA43 == 125 or LA43 == 126 or LA43 == 127 or LA43 == 128:
                        alt43 = 1

                    if alt43 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:17: ( LT )*
                        while True: #loop42
                            alt42 = 2
                            LA42_0 = self.input.LA(1)

                            if (LA42_0 == LT) :
                                LA42_2 = self.input.LA(2)

                                if (self.synpred60()) :
                                    alt42 = 1




                            if alt42 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT110 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList762)
                                if self.failed:
                                    return retval


                            else:
                                break #loop42


                        self.following.append(self.FOLLOW_statement_in_statementList766)
                        statement111 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement111.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:1: variableStatement : (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        mod = None
        LT112 = None
        LT114 = None
        char_literal115 = None
        variableDeclarationList113 = None


        mod_tree = None
        LT112_tree = None
        LT114_tree = None
        char_literal115_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_64 = RewriteRuleTokenStream(self.adaptor, "token 64")
        stream_65 = RewriteRuleTokenStream(self.adaptor, "token 65")
        stream_62 = RewriteRuleTokenStream(self.adaptor, "token 62")
        stream_variableDeclarationList = RewriteRuleSubtreeStream(self.adaptor, "rule variableDeclarationList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:2: ( (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:4: (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:4: (mod= 'var' | mod= 'const' )
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == 64) :
                    alt44 = 1
                elif (LA44_0 == 65) :
                    alt44 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("160:4: (mod= 'var' | mod= 'const' )", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:5: mod= 'var'
                    mod = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_variableStatement782)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_64.add(mod)


                elif alt44 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:15: mod= 'const'
                    mod = self.input.LT(1)
                    self.match(self.input, 65, self.FOLLOW_65_in_variableStatement786)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_65.add(mod)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:28: ( LT )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT112 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement789)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT112)


                    else:
                        break #loop45


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement792)
                variableDeclarationList113 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_variableDeclarationList.add(variableDeclarationList113.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:56: ( LT | ';' )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == LT) :
                    alt46 = 1
                elif (LA46_0 == 62) :
                    alt46 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("160:56: ( LT | ';' )", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:57: LT
                    LT114 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement795)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT114)


                elif alt46 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:62: ';'
                    char_literal115 = self.input.LT(1)
                    self.match(self.input, 62, self.FOLLOW_62_in_variableStatement799)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_62.add(char_literal115)



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
                    # 161:3: -> ^( VARDEFS $mod variableDeclarationList )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:161:6: ^( VARDEFS $mod variableDeclarationList )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT117 = None
        char_literal118 = None
        LT119 = None
        variableDeclaration116 = None

        variableDeclaration120 = None


        LT117_tree = None
        char_literal118_tree = None
        LT119_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList824)
                variableDeclaration116 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration116.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop49
                    alt49 = 2
                    alt49 = self.dfa49.predict(self.input)
                    if alt49 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:27: ( LT )*
                        while True: #loop47
                            alt47 = 2
                            LA47_0 = self.input.LA(1)

                            if (LA47_0 == LT) :
                                alt47 = 1


                            if alt47 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT117 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList827)
                                if self.failed:
                                    return retval


                            else:
                                break #loop47


                        char_literal118 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_variableDeclarationList831)
                        if self.failed:
                            return retval

                        char_literal118_tree = self.adaptor.createWithPayload(char_literal118)
                        self.adaptor.addChild(root_0, char_literal118_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:36: ( LT )*
                        while True: #loop48
                            alt48 = 2
                            LA48_0 = self.input.LA(1)

                            if (LA48_0 == LT) :
                                alt48 = 1


                            if alt48 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT119 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList833)
                                if self.failed:
                                    return retval


                            else:
                                break #loop48


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList837)
                        variableDeclaration120 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration120.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT122 = None
        char_literal123 = None
        LT124 = None
        variableDeclarationNoIn121 = None

        variableDeclarationNoIn125 = None


        LT122_tree = None
        char_literal123_tree = None
        LT124_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn851)
                variableDeclarationNoIn121 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn121.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop52
                    alt52 = 2
                    alt52 = self.dfa52.predict(self.input)
                    if alt52 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:31: ( LT )*
                        while True: #loop50
                            alt50 = 2
                            LA50_0 = self.input.LA(1)

                            if (LA50_0 == LT) :
                                alt50 = 1


                            if alt50 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT122 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn854)
                                if self.failed:
                                    return retval


                            else:
                                break #loop50


                        char_literal123 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_variableDeclarationListNoIn858)
                        if self.failed:
                            return retval

                        char_literal123_tree = self.adaptor.createWithPayload(char_literal123)
                        self.adaptor.addChild(root_0, char_literal123_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:40: ( LT )*
                        while True: #loop51
                            alt51 = 2
                            LA51_0 = self.input.LA(1)

                            if (LA51_0 == LT) :
                                alt51 = 1


                            if alt51 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT124 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn860)
                                if self.failed:
                                    return retval


                            else:
                                break #loop51


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn864)
                        variableDeclarationNoIn125 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn125.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:1: variableDeclaration : identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT127 = None
        identifier126 = None

        initialiser128 = None


        LT127_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiser = RewriteRuleSubtreeStream(self.adaptor, "rule initialiser")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:2: ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:4: identifier ( ( LT )* initialiser )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclaration878)
                identifier126 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier126.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:15: ( ( LT )* initialiser )?
                alt54 = 2
                alt54 = self.dfa54.predict(self.input)
                if alt54 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:16: ( LT )* initialiser
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:16: ( LT )*
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == LT) :
                            alt53 = 1


                        if alt53 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT127 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration881)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT127)


                        else:
                            break #loop53


                    self.following.append(self.FOLLOW_initialiser_in_variableDeclaration884)
                    initialiser128 = self.initialiser()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiser.add(initialiser128.tree)



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
                    # 174:3: -> ^( VARDEF identifier ( initialiser )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:6: ^( VARDEF identifier ( initialiser )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:26: ( initialiser )?
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:177:1: variableDeclarationNoIn : identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT130 = None
        identifier129 = None

        initialiserNoIn131 = None


        LT130_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiserNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule initialiserNoIn")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:2: ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:4: identifier ( ( LT )* initialiserNoIn )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn911)
                identifier129 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier129.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:15: ( ( LT )* initialiserNoIn )?
                alt56 = 2
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:16: ( LT )* initialiserNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:16: ( LT )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == LT) :
                            alt55 = 1


                        if alt55 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT130 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn914)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT130)


                        else:
                            break #loop55


                    self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn917)
                    initialiserNoIn131 = self.initialiserNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiserNoIn.add(initialiserNoIn131.tree)



                # AST Rewrite
                # elements: identifier, initialiserNoIn
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
                    # 179:3: -> ^( VARDEF identifier ( initialiserNoIn )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:6: ^( VARDEF identifier ( initialiserNoIn )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:26: ( initialiserNoIn )?
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:1: initialiser : '=' ( LT )* assignmentExpression -> assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal132 = None
        LT133 = None
        assignmentExpression134 = None


        char_literal132_tree = None
        LT133_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:2: ( '=' ( LT )* assignmentExpression -> assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:4: '=' ( LT )* assignmentExpression
                char_literal132 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_initialiser944)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_52.add(char_literal132)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:8: ( LT )*
                while True: #loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == LT) :
                        LA57_2 = self.input.LA(2)

                        if (self.synpred75()) :
                            alt57 = 1




                    if alt57 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT133 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser946)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT133)


                    else:
                        break #loop57


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser949)
                assignmentExpression134 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression134.tree)
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
                    # 184:3: -> assignmentExpression
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal135 = None
        LT136 = None
        assignmentExpressionNoIn137 = None


        char_literal135_tree = None
        LT136_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_52 = RewriteRuleTokenStream(self.adaptor, "token 52")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:2: ( '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:4: '=' ( LT )* assignmentExpressionNoIn
                char_literal135 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_initialiserNoIn967)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_52.add(char_literal135)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:8: ( LT )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == LT) :
                        LA58_2 = self.input.LA(2)

                        if (self.synpred76()) :
                            alt58 = 1




                    if alt58 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT136 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn969)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT136)


                    else:
                        break #loop58


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn972)
                assignmentExpressionNoIn137 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn137.tree)
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
                    # 189:3: -> assignmentExpressionNoIn
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal138 = None

        char_literal138_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:193:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:193:4: ';'
                root_0 = self.adaptor.nil()

                char_literal138 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_emptyStatement990)
                if self.failed:
                    return retval

                char_literal138_tree = self.adaptor.createWithPayload(char_literal138)
                self.adaptor.addChild(root_0, char_literal138_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:1: expressionStatement : expression ( LT | ';' ) ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        set140 = None
        expression139 = None


        set140_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:197:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:197:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement1002)
                expression139 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression139.tree)
                set140 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_expressionStatement1004
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:200:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal141 = None
        LT142 = None
        char_literal143 = None
        LT144 = None
        LT146 = None
        char_literal147 = None
        LT148 = None
        LT150 = None
        string_literal151 = None
        LT152 = None
        expression145 = None

        statement149 = None

        statement153 = None


        string_literal141_tree = None
        LT142_tree = None
        char_literal143_tree = None
        LT144_tree = None
        LT146_tree = None
        char_literal147_tree = None
        LT148_tree = None
        LT150_tree = None
        string_literal151_tree = None
        LT152_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal141 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_ifStatement1023)
                if self.failed:
                    return retval

                string_literal141_tree = self.adaptor.createWithPayload(string_literal141)
                self.adaptor.addChild(root_0, string_literal141_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:11: ( LT )*
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == LT) :
                        alt59 = 1


                    if alt59 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT142 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1025)
                        if self.failed:
                            return retval


                    else:
                        break #loop59


                char_literal143 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_ifStatement1029)
                if self.failed:
                    return retval

                char_literal143_tree = self.adaptor.createWithPayload(char_literal143)
                self.adaptor.addChild(root_0, char_literal143_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:20: ( LT )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == LT) :
                        LA60_2 = self.input.LA(2)

                        if (self.synpred79()) :
                            alt60 = 1




                    if alt60 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT144 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1031)
                        if self.failed:
                            return retval


                    else:
                        break #loop60


                self.following.append(self.FOLLOW_expression_in_ifStatement1035)
                expression145 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression145.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:36: ( LT )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == LT) :
                        alt61 = 1


                    if alt61 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT146 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1037)
                        if self.failed:
                            return retval


                    else:
                        break #loop61


                char_literal147 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_ifStatement1041)
                if self.failed:
                    return retval

                char_literal147_tree = self.adaptor.createWithPayload(char_literal147)
                self.adaptor.addChild(root_0, char_literal147_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:45: ( LT )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == LT) :
                        LA62_2 = self.input.LA(2)

                        if (self.synpred81()) :
                            alt62 = 1




                    if alt62 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT148 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1043)
                        if self.failed:
                            return retval


                    else:
                        break #loop62


                self.following.append(self.FOLLOW_statement_in_ifStatement1047)
                statement149 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement149.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:58: ( ( LT )* 'else' ( LT )* statement )?
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == LT) :
                    LA65_1 = self.input.LA(2)

                    if (self.synpred84()) :
                        alt65 = 1
                elif (LA65_0 == 67) :
                    LA65_2 = self.input.LA(2)

                    if (self.synpred84()) :
                        alt65 = 1
                if alt65 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:61: ( LT )*
                    while True: #loop63
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if (LA63_0 == LT) :
                            alt63 = 1


                        if alt63 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT150 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1050)
                            if self.failed:
                                return retval


                        else:
                            break #loop63


                    string_literal151 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_ifStatement1054)
                    if self.failed:
                        return retval

                    string_literal151_tree = self.adaptor.createWithPayload(string_literal151)
                    self.adaptor.addChild(root_0, string_literal151_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:73: ( LT )*
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == LT) :
                            LA64_2 = self.input.LA(2)

                            if (self.synpred83()) :
                                alt64 = 1




                        if alt64 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT152 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement1056)
                            if self.failed:
                                return retval


                        else:
                            break #loop64


                    self.following.append(self.FOLLOW_statement_in_ifStatement1060)
                    statement153 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement153.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement154 = None

        whileStatement155 = None

        forStatement156 = None

        forInStatement157 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:205:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt66 = 4
                LA66 = self.input.LA(1)
                if LA66 == 68:
                    alt66 = 1
                elif LA66 == 69:
                    alt66 = 2
                elif LA66 == 70:
                    LA66_3 = self.input.LA(2)

                    if (self.synpred87()) :
                        alt66 = 3
                    elif (True) :
                        alt66 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("204:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 66, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("204:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 66, 0, self.input)

                    raise nvae

                if alt66 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:205:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement1074)
                    doWhileStatement154 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement154.tree)


                elif alt66 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement1079)
                    whileStatement155 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement155.tree)


                elif alt66 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement1084)
                    forStatement156 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement156.tree)


                elif alt66 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement1089)
                    forInStatement157 = self.forInStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forInStatement157.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal158 = None
        LT159 = None
        LT161 = None
        string_literal162 = None
        LT163 = None
        char_literal164 = None
        char_literal166 = None
        set167 = None
        statement160 = None

        expression165 = None


        string_literal158_tree = None
        LT159_tree = None
        LT161_tree = None
        string_literal162_tree = None
        LT163_tree = None
        char_literal164_tree = None
        char_literal166_tree = None
        set167_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal158 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_doWhileStatement1101)
                if self.failed:
                    return retval

                string_literal158_tree = self.adaptor.createWithPayload(string_literal158)
                self.adaptor.addChild(root_0, string_literal158_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:11: ( LT )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == LT) :
                        LA67_2 = self.input.LA(2)

                        if (self.synpred88()) :
                            alt67 = 1




                    if alt67 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT159 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1103)
                        if self.failed:
                            return retval


                    else:
                        break #loop67


                self.following.append(self.FOLLOW_statement_in_doWhileStatement1107)
                statement160 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement160.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:26: ( LT )*
                while True: #loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == LT) :
                        alt68 = 1


                    if alt68 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT161 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1109)
                        if self.failed:
                            return retval


                    else:
                        break #loop68


                string_literal162 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_doWhileStatement1113)
                if self.failed:
                    return retval

                string_literal162_tree = self.adaptor.createWithPayload(string_literal162)
                self.adaptor.addChild(root_0, string_literal162_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:39: ( LT )*
                while True: #loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == LT) :
                        alt69 = 1


                    if alt69 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT163 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement1115)
                        if self.failed:
                            return retval


                    else:
                        break #loop69


                char_literal164 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_doWhileStatement1119)
                if self.failed:
                    return retval

                char_literal164_tree = self.adaptor.createWithPayload(char_literal164)
                self.adaptor.addChild(root_0, char_literal164_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement1121)
                expression165 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression165.tree)
                char_literal166 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_doWhileStatement1123)
                if self.failed:
                    return retval

                char_literal166_tree = self.adaptor.createWithPayload(char_literal166)
                self.adaptor.addChild(root_0, char_literal166_tree)

                set167 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement1125
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal168 = None
        LT169 = None
        char_literal170 = None
        LT171 = None
        LT173 = None
        char_literal174 = None
        LT175 = None
        expression172 = None

        statement176 = None


        string_literal168_tree = None
        LT169_tree = None
        char_literal170_tree = None
        LT171_tree = None
        LT173_tree = None
        char_literal174_tree = None
        LT175_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal168 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_whileStatement1144)
                if self.failed:
                    return retval

                string_literal168_tree = self.adaptor.createWithPayload(string_literal168)
                self.adaptor.addChild(root_0, string_literal168_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:14: ( LT )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == LT) :
                        alt70 = 1


                    if alt70 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT169 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1146)
                        if self.failed:
                            return retval


                    else:
                        break #loop70


                char_literal170 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_whileStatement1150)
                if self.failed:
                    return retval

                char_literal170_tree = self.adaptor.createWithPayload(char_literal170)
                self.adaptor.addChild(root_0, char_literal170_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:23: ( LT )*
                while True: #loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == LT) :
                        LA71_2 = self.input.LA(2)

                        if (self.synpred93()) :
                            alt71 = 1




                    if alt71 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT171 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1152)
                        if self.failed:
                            return retval


                    else:
                        break #loop71


                self.following.append(self.FOLLOW_expression_in_whileStatement1156)
                expression172 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression172.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:39: ( LT )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == LT) :
                        alt72 = 1


                    if alt72 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT173 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1158)
                        if self.failed:
                            return retval


                    else:
                        break #loop72


                char_literal174 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_whileStatement1162)
                if self.failed:
                    return retval

                char_literal174_tree = self.adaptor.createWithPayload(char_literal174)
                self.adaptor.addChild(root_0, char_literal174_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:48: ( LT )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == LT) :
                        LA73_2 = self.input.LA(2)

                        if (self.synpred95()) :
                            alt73 = 1




                    if alt73 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT175 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement1164)
                        if self.failed:
                            return retval


                    else:
                        break #loop73


                self.following.append(self.FOLLOW_statement_in_whileStatement1168)
                statement176 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement176.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal177 = None
        LT178 = None
        char_literal179 = None
        LT180 = None
        LT182 = None
        char_literal183 = None
        LT184 = None
        LT186 = None
        char_literal187 = None
        LT188 = None
        LT190 = None
        char_literal191 = None
        LT192 = None
        forStatementInitialiserPart181 = None

        expression185 = None

        expression189 = None

        statement193 = None


        string_literal177_tree = None
        LT178_tree = None
        char_literal179_tree = None
        LT180_tree = None
        LT182_tree = None
        char_literal183_tree = None
        LT184_tree = None
        LT186_tree = None
        char_literal187_tree = None
        LT188_tree = None
        LT190_tree = None
        char_literal191_tree = None
        LT192_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal177 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_forStatement1180)
                if self.failed:
                    return retval

                string_literal177_tree = self.adaptor.createWithPayload(string_literal177)
                self.adaptor.addChild(root_0, string_literal177_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:12: ( LT )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == LT) :
                        alt74 = 1


                    if alt74 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT178 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1182)
                        if self.failed:
                            return retval


                    else:
                        break #loop74


                char_literal179 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_forStatement1186)
                if self.failed:
                    return retval

                char_literal179_tree = self.adaptor.createWithPayload(char_literal179)
                self.adaptor.addChild(root_0, char_literal179_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:19: ( ( LT )* forStatementInitialiserPart )?
                alt76 = 2
                alt76 = self.dfa76.predict(self.input)
                if alt76 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:22: ( LT )*
                    while True: #loop75
                        alt75 = 2
                        LA75_0 = self.input.LA(1)

                        if (LA75_0 == LT) :
                            LA75_2 = self.input.LA(2)

                            if (self.synpred97()) :
                                alt75 = 1




                        if alt75 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT180 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1189)
                            if self.failed:
                                return retval


                        else:
                            break #loop75


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement1193)
                    forStatementInitialiserPart181 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart181.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:57: ( LT )*
                while True: #loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == LT) :
                        alt77 = 1


                    if alt77 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT182 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1197)
                        if self.failed:
                            return retval


                    else:
                        break #loop77


                char_literal183 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_forStatement1201)
                if self.failed:
                    return retval

                char_literal183_tree = self.adaptor.createWithPayload(char_literal183)
                self.adaptor.addChild(root_0, char_literal183_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:64: ( ( LT )* expression )?
                alt79 = 2
                alt79 = self.dfa79.predict(self.input)
                if alt79 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:67: ( LT )*
                    while True: #loop78
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == LT) :
                            LA78_2 = self.input.LA(2)

                            if (self.synpred100()) :
                                alt78 = 1




                        if alt78 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT184 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1204)
                            if self.failed:
                                return retval


                        else:
                            break #loop78


                    self.following.append(self.FOLLOW_expression_in_forStatement1208)
                    expression185 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression185.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:85: ( LT )*
                while True: #loop80
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if (LA80_0 == LT) :
                        alt80 = 1


                    if alt80 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT186 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1212)
                        if self.failed:
                            return retval


                    else:
                        break #loop80


                char_literal187 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_forStatement1216)
                if self.failed:
                    return retval

                char_literal187_tree = self.adaptor.createWithPayload(char_literal187)
                self.adaptor.addChild(root_0, char_literal187_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:92: ( ( LT )* expression )?
                alt82 = 2
                alt82 = self.dfa82.predict(self.input)
                if alt82 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:95: ( LT )*
                    while True: #loop81
                        alt81 = 2
                        LA81_0 = self.input.LA(1)

                        if (LA81_0 == LT) :
                            LA81_2 = self.input.LA(2)

                            if (self.synpred103()) :
                                alt81 = 1




                        if alt81 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT188 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1219)
                            if self.failed:
                                return retval


                        else:
                            break #loop81


                    self.following.append(self.FOLLOW_expression_in_forStatement1223)
                    expression189 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression189.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:113: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        alt83 = 1


                    if alt83 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT190 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1227)
                        if self.failed:
                            return retval


                    else:
                        break #loop83


                char_literal191 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_forStatement1231)
                if self.failed:
                    return retval

                char_literal191_tree = self.adaptor.createWithPayload(char_literal191)
                self.adaptor.addChild(root_0, char_literal191_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:122: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        LA84_2 = self.input.LA(2)

                        if (self.synpred106()) :
                            alt84 = 1




                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT192 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement1233)
                        if self.failed:
                            return retval


                    else:
                        break #loop84


                self.following.append(self.FOLLOW_statement_in_forStatement1237)
                statement193 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement193.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:223:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal195 = None
        LT196 = None
        expressionNoIn194 = None

        variableDeclarationListNoIn197 = None


        string_literal195_tree = None
        LT196_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:2: ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn )
                alt86 = 2
                LA86_0 = self.input.LA(1)

                if ((LT <= LA86_0 <= RegularExpressionHacks) or LA86_0 == 47 or LA86_0 == 49 or LA86_0 == 51 or LA86_0 == 53 or (55 <= LA86_0 <= 56) or (59 <= LA86_0 <= 61) or LA86_0 == 71 or LA86_0 == 82 or LA86_0 == 84 or LA86_0 == 114 or (116 <= LA86_0 <= 128)) :
                    alt86 = 1
                elif (LA86_0 == 64) :
                    alt86 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("223:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );", 86, 0, self.input)

                    raise nvae

                if alt86 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart1249)
                    expressionNoIn194 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn194.tree)


                elif alt86 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: 'var' ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    string_literal195 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_forStatementInitialiserPart1254)
                    if self.failed:
                        return retval

                    string_literal195_tree = self.adaptor.createWithPayload(string_literal195)
                    self.adaptor.addChild(root_0, string_literal195_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:12: ( LT )*
                    while True: #loop85
                        alt85 = 2
                        LA85_0 = self.input.LA(1)

                        if (LA85_0 == LT) :
                            alt85 = 1


                        if alt85 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT196 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart1256)
                            if self.failed:
                                return retval


                        else:
                            break #loop85


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1260)
                    variableDeclarationListNoIn197 = self.variableDeclarationListNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationListNoIn197.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:228:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal198 = None
        LT199 = None
        string_literal200 = None
        LT201 = None
        char_literal202 = None
        LT203 = None
        LT205 = None
        string_literal206 = None
        LT207 = None
        LT209 = None
        char_literal210 = None
        LT211 = None
        forInStatementInitialiserPart204 = None

        expression208 = None

        statement212 = None


        string_literal198_tree = None
        LT199_tree = None
        string_literal200_tree = None
        LT201_tree = None
        char_literal202_tree = None
        LT203_tree = None
        LT205_tree = None
        string_literal206_tree = None
        LT207_tree = None
        LT209_tree = None
        char_literal210_tree = None
        LT211_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal198 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_forInStatement1272)
                if self.failed:
                    return retval

                string_literal198_tree = self.adaptor.createWithPayload(string_literal198)
                self.adaptor.addChild(root_0, string_literal198_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:12: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        LA87_2 = self.input.LA(2)

                        if (self.synpred109()) :
                            alt87 = 1




                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT199 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1274)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:15: ( 'each' )?
                alt88 = 2
                LA88_0 = self.input.LA(1)

                if (LA88_0 == 71) :
                    alt88 = 1
                if alt88 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal200 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_forInStatement1278)
                    if self.failed:
                        return retval

                    string_literal200_tree = self.adaptor.createWithPayload(string_literal200)
                    self.adaptor.addChild(root_0, string_literal200_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:25: ( LT )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LT) :
                        alt89 = 1


                    if alt89 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT201 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1281)
                        if self.failed:
                            return retval


                    else:
                        break #loop89


                char_literal202 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_forInStatement1285)
                if self.failed:
                    return retval

                char_literal202_tree = self.adaptor.createWithPayload(char_literal202)
                self.adaptor.addChild(root_0, char_literal202_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:34: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        LA90_2 = self.input.LA(2)

                        if (self.synpred112()) :
                            alt90 = 1




                    if alt90 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT203 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1287)
                        if self.failed:
                            return retval


                    else:
                        break #loop90


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement1291)
                forInStatementInitialiserPart204 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart204.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:69: ( LT )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == LT) :
                        alt91 = 1


                    if alt91 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT205 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1293)
                        if self.failed:
                            return retval


                    else:
                        break #loop91


                string_literal206 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_forInStatement1297)
                if self.failed:
                    return retval

                string_literal206_tree = self.adaptor.createWithPayload(string_literal206)
                self.adaptor.addChild(root_0, string_literal206_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:79: ( LT )*
                while True: #loop92
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == LT) :
                        LA92_2 = self.input.LA(2)

                        if (self.synpred114()) :
                            alt92 = 1




                    if alt92 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT207 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1299)
                        if self.failed:
                            return retval


                    else:
                        break #loop92


                self.following.append(self.FOLLOW_expression_in_forInStatement1303)
                expression208 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression208.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:95: ( LT )*
                while True: #loop93
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == LT) :
                        alt93 = 1


                    if alt93 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT209 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1305)
                        if self.failed:
                            return retval


                    else:
                        break #loop93


                char_literal210 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_forInStatement1309)
                if self.failed:
                    return retval

                char_literal210_tree = self.adaptor.createWithPayload(char_literal210)
                self.adaptor.addChild(root_0, char_literal210_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:104: ( LT )*
                while True: #loop94
                    alt94 = 2
                    LA94_0 = self.input.LA(1)

                    if (LA94_0 == LT) :
                        LA94_2 = self.input.LA(2)

                        if (self.synpred116()) :
                            alt94 = 1




                    if alt94 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT211 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement1311)
                        if self.failed:
                            return retval


                    else:
                        break #loop94


                self.following.append(self.FOLLOW_statement_in_forInStatement1315)
                statement212 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement212.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal214 = None
        LT215 = None
        leftHandSideExpression213 = None

        variableDeclarationNoIn216 = None


        string_literal214_tree = None
        LT215_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:2: ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn )
                alt96 = 2
                LA96_0 = self.input.LA(1)

                if ((LT <= LA96_0 <= RegularExpressionHacks) or LA96_0 == 47 or LA96_0 == 49 or LA96_0 == 53 or (55 <= LA96_0 <= 56) or (59 <= LA96_0 <= 61) or LA96_0 == 71 or LA96_0 == 82 or LA96_0 == 84 or (123 <= LA96_0 <= 128)) :
                    alt96 = 1
                elif (LA96_0 == 64) :
                    alt96 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("232:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );", 96, 0, self.input)

                    raise nvae

                if alt96 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1327)
                    leftHandSideExpression213 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression213.tree)


                elif alt96 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:4: 'var' ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    string_literal214 = self.input.LT(1)
                    self.match(self.input, 64, self.FOLLOW_64_in_forInStatementInitialiserPart1332)
                    if self.failed:
                        return retval

                    string_literal214_tree = self.adaptor.createWithPayload(string_literal214)
                    self.adaptor.addChild(root_0, string_literal214_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:12: ( LT )*
                    while True: #loop95
                        alt95 = 2
                        LA95_0 = self.input.LA(1)

                        if (LA95_0 == LT) :
                            alt95 = 1


                        if alt95 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT215 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart1334)
                            if self.failed:
                                return retval


                        else:
                            break #loop95


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1338)
                    variableDeclarationNoIn216 = self.variableDeclarationNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationNoIn216.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:237:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal217 = None
        set219 = None
        identifier218 = None


        string_literal217_tree = None
        set219_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal217 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_continueStatement1349)
                if self.failed:
                    return retval

                string_literal217_tree = self.adaptor.createWithPayload(string_literal217)
                self.adaptor.addChild(root_0, string_literal217_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:15: ( identifier )?
                alt97 = 2
                LA97_0 = self.input.LA(1)

                if (LA97_0 == Identifier or (59 <= LA97_0 <= 61) or LA97_0 == 71 or (124 <= LA97_0 <= 125)) :
                    alt97 = 1
                if alt97 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement1351)
                    identifier218 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier218.tree)



                set219 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_continueStatement1354
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:241:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal220 = None
        set222 = None
        identifier221 = None


        string_literal220_tree = None
        set222_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal220 = self.input.LT(1)
                self.match(self.input, 74, self.FOLLOW_74_in_breakStatement1372)
                if self.failed:
                    return retval

                string_literal220_tree = self.adaptor.createWithPayload(string_literal220)
                self.adaptor.addChild(root_0, string_literal220_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:12: ( identifier )?
                alt98 = 2
                LA98_0 = self.input.LA(1)

                if (LA98_0 == Identifier or (59 <= LA98_0 <= 61) or LA98_0 == 71 or (124 <= LA98_0 <= 125)) :
                    alt98 = 1
                if alt98 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement1374)
                    identifier221 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier221.tree)



                set222 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_breakStatement1377
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal223 = None
        set225 = None
        expression224 = None


        string_literal223_tree = None
        set225_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal223 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_returnStatement1395)
                if self.failed:
                    return retval

                string_literal223_tree = self.adaptor.createWithPayload(string_literal223)
                self.adaptor.addChild(root_0, string_literal223_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:13: ( expression )?
                alt99 = 2
                LA99_0 = self.input.LA(1)

                if ((StringLiteral <= LA99_0 <= RegularExpressionHacks) or LA99_0 == 47 or LA99_0 == 49 or LA99_0 == 51 or LA99_0 == 53 or (55 <= LA99_0 <= 56) or (59 <= LA99_0 <= 61) or LA99_0 == 71 or LA99_0 == 82 or LA99_0 == 84 or LA99_0 == 114 or (116 <= LA99_0 <= 128)) :
                    alt99 = 1
                elif (LA99_0 == LT) :
                    LA99_2 = self.input.LA(2)

                    if (self.synpred123()) :
                        alt99 = 1
                if alt99 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement1397)
                    expression224 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression224.tree)



                set225 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_returnStatement1400
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal226 = None
        LT227 = None
        char_literal228 = None
        LT229 = None
        LT231 = None
        char_literal232 = None
        LT233 = None
        expression230 = None

        statement234 = None


        string_literal226_tree = None
        LT227_tree = None
        char_literal228_tree = None
        LT229_tree = None
        LT231_tree = None
        char_literal232_tree = None
        LT233_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal226 = self.input.LT(1)
                self.match(self.input, 75, self.FOLLOW_75_in_withStatement1419)
                if self.failed:
                    return retval

                string_literal226_tree = self.adaptor.createWithPayload(string_literal226)
                self.adaptor.addChild(root_0, string_literal226_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:13: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT227 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1421)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                char_literal228 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_withStatement1425)
                if self.failed:
                    return retval

                char_literal228_tree = self.adaptor.createWithPayload(char_literal228)
                self.adaptor.addChild(root_0, char_literal228_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:22: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        LA101_2 = self.input.LA(2)

                        if (self.synpred126()) :
                            alt101 = 1




                    if alt101 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT229 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1427)
                        if self.failed:
                            return retval


                    else:
                        break #loop101


                self.following.append(self.FOLLOW_expression_in_withStatement1431)
                expression230 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression230.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:38: ( LT )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == LT) :
                        alt102 = 1


                    if alt102 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT231 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1433)
                        if self.failed:
                            return retval


                    else:
                        break #loop102


                char_literal232 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_withStatement1437)
                if self.failed:
                    return retval

                char_literal232_tree = self.adaptor.createWithPayload(char_literal232)
                self.adaptor.addChild(root_0, char_literal232_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:47: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        LA103_2 = self.input.LA(2)

                        if (self.synpred128()) :
                            alt103 = 1




                    if alt103 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT233 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1439)
                        if self.failed:
                            return retval


                    else:
                        break #loop103


                self.following.append(self.FOLLOW_statement_in_withStatement1443)
                statement234 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement234.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:253:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        LT236 = None
        char_literal237 = None
        LT238 = None
        identifier235 = None

        statement239 = None


        LT236_tree = None
        char_literal237_tree = None
        LT238_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1454)
                identifier235 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier235.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:17: ( LT )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == LT) :
                        alt104 = 1


                    if alt104 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT236 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1456)
                        if self.failed:
                            return retval


                    else:
                        break #loop104


                char_literal237 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_labelledStatement1460)
                if self.failed:
                    return retval

                char_literal237_tree = self.adaptor.createWithPayload(char_literal237)
                self.adaptor.addChild(root_0, char_literal237_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:26: ( LT )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == LT) :
                        LA105_2 = self.input.LA(2)

                        if (self.synpred130()) :
                            alt105 = 1




                    if alt105 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT238 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1462)
                        if self.failed:
                            return retval


                    else:
                        break #loop105


                self.following.append(self.FOLLOW_statement_in_labelledStatement1466)
                statement239 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement239.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:257:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal240 = None
        LT241 = None
        char_literal242 = None
        LT243 = None
        LT245 = None
        char_literal246 = None
        LT247 = None
        expression244 = None

        caseBlock248 = None


        string_literal240_tree = None
        LT241_tree = None
        char_literal242_tree = None
        LT243_tree = None
        LT245_tree = None
        char_literal246_tree = None
        LT247_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal240 = self.input.LT(1)
                self.match(self.input, 76, self.FOLLOW_76_in_switchStatement1478)
                if self.failed:
                    return retval

                string_literal240_tree = self.adaptor.createWithPayload(string_literal240)
                self.adaptor.addChild(root_0, string_literal240_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:15: ( LT )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == LT) :
                        alt106 = 1


                    if alt106 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT241 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1480)
                        if self.failed:
                            return retval


                    else:
                        break #loop106


                char_literal242 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_switchStatement1484)
                if self.failed:
                    return retval

                char_literal242_tree = self.adaptor.createWithPayload(char_literal242)
                self.adaptor.addChild(root_0, char_literal242_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:24: ( LT )*
                while True: #loop107
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if (LA107_0 == LT) :
                        LA107_2 = self.input.LA(2)

                        if (self.synpred132()) :
                            alt107 = 1




                    if alt107 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT243 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1486)
                        if self.failed:
                            return retval


                    else:
                        break #loop107


                self.following.append(self.FOLLOW_expression_in_switchStatement1490)
                expression244 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression244.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:40: ( LT )*
                while True: #loop108
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == LT) :
                        alt108 = 1


                    if alt108 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT245 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1492)
                        if self.failed:
                            return retval


                    else:
                        break #loop108


                char_literal246 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_switchStatement1496)
                if self.failed:
                    return retval

                char_literal246_tree = self.adaptor.createWithPayload(char_literal246)
                self.adaptor.addChild(root_0, char_literal246_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:49: ( LT )*
                while True: #loop109
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == LT) :
                        alt109 = 1


                    if alt109 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT247 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1498)
                        if self.failed:
                            return retval


                    else:
                        break #loop109


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1502)
                caseBlock248 = self.caseBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, caseBlock248.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:261:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal249 = None
        LT250 = None
        LT252 = None
        LT254 = None
        LT256 = None
        char_literal257 = None
        caseClause251 = None

        defaultClause253 = None

        caseClause255 = None


        char_literal249_tree = None
        LT250_tree = None
        LT252_tree = None
        LT254_tree = None
        LT256_tree = None
        char_literal257_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal249 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_caseBlock1514)
                if self.failed:
                    return retval

                char_literal249_tree = self.adaptor.createWithPayload(char_literal249)
                self.adaptor.addChild(root_0, char_literal249_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:8: ( ( LT )* caseClause )*
                while True: #loop111
                    alt111 = 2
                    alt111 = self.dfa111.predict(self.input)
                    if alt111 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:11: ( LT )*
                        while True: #loop110
                            alt110 = 2
                            LA110_0 = self.input.LA(1)

                            if (LA110_0 == LT) :
                                alt110 = 1


                            if alt110 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT250 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1517)
                                if self.failed:
                                    return retval


                            else:
                                break #loop110


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1521)
                        caseClause251 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause251.tree)


                    else:
                        break #loop111


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt115 = 2
                alt115 = self.dfa115.predict(self.input)
                if alt115 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:30: ( LT )*
                    while True: #loop112
                        alt112 = 2
                        LA112_0 = self.input.LA(1)

                        if (LA112_0 == LT) :
                            alt112 = 1


                        if alt112 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT252 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1526)
                            if self.failed:
                                return retval


                        else:
                            break #loop112


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1530)
                    defaultClause253 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause253.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:47: ( ( LT )* caseClause )*
                    while True: #loop114
                        alt114 = 2
                        alt114 = self.dfa114.predict(self.input)
                        if alt114 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:50: ( LT )*
                            while True: #loop113
                                alt113 = 2
                                LA113_0 = self.input.LA(1)

                                if (LA113_0 == LT) :
                                    alt113 = 1


                                if alt113 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT254 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1533)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop113


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1537)
                            caseClause255 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause255.tree)


                        else:
                            break #loop114





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:70: ( LT )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == LT) :
                        alt116 = 1


                    if alt116 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT256 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1543)
                        if self.failed:
                            return retval


                    else:
                        break #loop116


                char_literal257 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_caseBlock1547)
                if self.failed:
                    return retval

                char_literal257_tree = self.adaptor.createWithPayload(char_literal257)
                self.adaptor.addChild(root_0, char_literal257_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal258 = None
        LT259 = None
        LT261 = None
        char_literal262 = None
        LT263 = None
        expression260 = None

        statementList264 = None


        string_literal258_tree = None
        LT259_tree = None
        LT261_tree = None
        char_literal262_tree = None
        LT263_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal258 = self.input.LT(1)
                self.match(self.input, 77, self.FOLLOW_77_in_caseClause1558)
                if self.failed:
                    return retval

                string_literal258_tree = self.adaptor.createWithPayload(string_literal258)
                self.adaptor.addChild(root_0, string_literal258_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:13: ( LT )*
                while True: #loop117
                    alt117 = 2
                    LA117_0 = self.input.LA(1)

                    if (LA117_0 == LT) :
                        LA117_2 = self.input.LA(2)

                        if (self.synpred142()) :
                            alt117 = 1




                    if alt117 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT259 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1560)
                        if self.failed:
                            return retval


                    else:
                        break #loop117


                self.following.append(self.FOLLOW_expression_in_caseClause1564)
                expression260 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression260.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:29: ( LT )*
                while True: #loop118
                    alt118 = 2
                    LA118_0 = self.input.LA(1)

                    if (LA118_0 == LT) :
                        alt118 = 1


                    if alt118 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT261 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1566)
                        if self.failed:
                            return retval


                    else:
                        break #loop118


                char_literal262 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_caseClause1570)
                if self.failed:
                    return retval

                char_literal262_tree = self.adaptor.createWithPayload(char_literal262)
                self.adaptor.addChild(root_0, char_literal262_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:38: ( LT )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if (LA119_0 == LT) :
                        LA119_2 = self.input.LA(2)

                        if (self.synpred144()) :
                            alt119 = 1




                    if alt119 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT263 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1572)
                        if self.failed:
                            return retval


                    else:
                        break #loop119


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:41: ( statementList )?
                alt120 = 2
                LA120 = self.input.LA(1)
                if LA120 == StringLiteral or LA120 == XMLComment or LA120 == NumericLiteral or LA120 == Identifier or LA120 == RegularExpressionHacks or LA120 == 47 or LA120 == 49 or LA120 == 51 or LA120 == 53 or LA120 == 55 or LA120 == 56 or LA120 == 60 or LA120 == 61 or LA120 == 62 or LA120 == 63 or LA120 == 64 or LA120 == 65 or LA120 == 66 or LA120 == 68 or LA120 == 69 or LA120 == 70 or LA120 == 71 or LA120 == 73 or LA120 == 74 or LA120 == 75 or LA120 == 76 or LA120 == 78 or LA120 == 79 or LA120 == 82 or LA120 == 84 or LA120 == 114 or LA120 == 116 or LA120 == 117 or LA120 == 118 or LA120 == 119 or LA120 == 120 or LA120 == 121 or LA120 == 122 or LA120 == 123 or LA120 == 124 or LA120 == 125 or LA120 == 126 or LA120 == 127 or LA120 == 128:
                    alt120 = 1
                elif LA120 == LT:
                    LA120_6 = self.input.LA(2)

                    if (self.synpred145()) :
                        alt120 = 1
                elif LA120 == 59:
                    LA120_9 = self.input.LA(2)

                    if (self.synpred145()) :
                        alt120 = 1
                if alt120 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1576)
                    statementList264 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList264.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal265 = None
        LT266 = None
        char_literal267 = None
        LT268 = None
        statementList269 = None


        string_literal265_tree = None
        LT266_tree = None
        char_literal267_tree = None
        LT268_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal265 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_defaultClause1589)
                if self.failed:
                    return retval

                string_literal265_tree = self.adaptor.createWithPayload(string_literal265)
                self.adaptor.addChild(root_0, string_literal265_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:16: ( LT )*
                while True: #loop121
                    alt121 = 2
                    LA121_0 = self.input.LA(1)

                    if (LA121_0 == LT) :
                        alt121 = 1


                    if alt121 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT266 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1591)
                        if self.failed:
                            return retval


                    else:
                        break #loop121


                char_literal267 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_defaultClause1595)
                if self.failed:
                    return retval

                char_literal267_tree = self.adaptor.createWithPayload(char_literal267)
                self.adaptor.addChild(root_0, char_literal267_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:25: ( LT )*
                while True: #loop122
                    alt122 = 2
                    LA122_0 = self.input.LA(1)

                    if (LA122_0 == LT) :
                        LA122_2 = self.input.LA(2)

                        if (self.synpred147()) :
                            alt122 = 1




                    if alt122 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT268 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1597)
                        if self.failed:
                            return retval


                    else:
                        break #loop122


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:28: ( statementList )?
                alt123 = 2
                alt123 = self.dfa123.predict(self.input)
                if alt123 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1601)
                    statementList269 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList269.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:273:1: throwStatement : 'throw' expression ( LT | ';' ) ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal270 = None
        set272 = None
        expression271 = None


        string_literal270_tree = None
        set272_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal270 = self.input.LT(1)
                self.match(self.input, 78, self.FOLLOW_78_in_throwStatement1614)
                if self.failed:
                    return retval

                string_literal270_tree = self.adaptor.createWithPayload(string_literal270)
                self.adaptor.addChild(root_0, string_literal270_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1616)
                expression271 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression271.tree)
                set272 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 62:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_throwStatement1618
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:277:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal273 = None
        LT274 = None
        LT276 = None
        LT279 = None
        statementBlock275 = None

        finallyClause277 = None

        catchClause278 = None

        finallyClause280 = None


        string_literal273_tree = None
        LT274_tree = None
        LT276_tree = None
        LT279_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal273 = self.input.LT(1)
                self.match(self.input, 79, self.FOLLOW_79_in_tryStatement1636)
                if self.failed:
                    return retval

                string_literal273_tree = self.adaptor.createWithPayload(string_literal273)
                self.adaptor.addChild(root_0, string_literal273_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:12: ( LT )*
                while True: #loop124
                    alt124 = 2
                    LA124_0 = self.input.LA(1)

                    if (LA124_0 == LT) :
                        alt124 = 1


                    if alt124 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT274 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1638)
                        if self.failed:
                            return retval


                    else:
                        break #loop124


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1642)
                statementBlock275 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock275.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:32: ( LT )*
                while True: #loop125
                    alt125 = 2
                    LA125_0 = self.input.LA(1)

                    if (LA125_0 == LT) :
                        alt125 = 1


                    if alt125 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT276 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1644)
                        if self.failed:
                            return retval


                    else:
                        break #loop125


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt128 = 2
                LA128_0 = self.input.LA(1)

                if (LA128_0 == 81) :
                    alt128 = 1
                elif (LA128_0 == 80) :
                    alt128 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("278:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 128, 0, self.input)

                    raise nvae

                if alt128 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1649)
                    finallyClause277 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause277.tree)


                elif alt128 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1653)
                    catchClause278 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause278.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:64: ( ( LT )* finallyClause )?
                    alt127 = 2
                    alt127 = self.dfa127.predict(self.input)
                    if alt127 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:67: ( LT )*
                        while True: #loop126
                            alt126 = 2
                            LA126_0 = self.input.LA(1)

                            if (LA126_0 == LT) :
                                alt126 = 1


                            if alt126 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT279 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1656)
                                if self.failed:
                                    return retval


                            else:
                                break #loop126


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1660)
                        finallyClause280 = self.finallyClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, finallyClause280.tree)









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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:281:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal281 = None
        LT282 = None
        char_literal283 = None
        LT284 = None
        LT286 = None
        char_literal287 = None
        LT288 = None
        identifier285 = None

        statementBlock289 = None


        string_literal281_tree = None
        LT282_tree = None
        char_literal283_tree = None
        LT284_tree = None
        LT286_tree = None
        char_literal287_tree = None
        LT288_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal281 = self.input.LT(1)
                self.match(self.input, 80, self.FOLLOW_80_in_catchClause1681)
                if self.failed:
                    return retval

                string_literal281_tree = self.adaptor.createWithPayload(string_literal281)
                self.adaptor.addChild(root_0, string_literal281_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:14: ( LT )*
                while True: #loop129
                    alt129 = 2
                    LA129_0 = self.input.LA(1)

                    if (LA129_0 == LT) :
                        alt129 = 1


                    if alt129 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT282 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1683)
                        if self.failed:
                            return retval


                    else:
                        break #loop129


                char_literal283 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_catchClause1687)
                if self.failed:
                    return retval

                char_literal283_tree = self.adaptor.createWithPayload(char_literal283)
                self.adaptor.addChild(root_0, char_literal283_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:23: ( LT )*
                while True: #loop130
                    alt130 = 2
                    LA130_0 = self.input.LA(1)

                    if (LA130_0 == LT) :
                        alt130 = 1


                    if alt130 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT284 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1689)
                        if self.failed:
                            return retval


                    else:
                        break #loop130


                self.following.append(self.FOLLOW_identifier_in_catchClause1693)
                identifier285 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier285.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:39: ( LT )*
                while True: #loop131
                    alt131 = 2
                    LA131_0 = self.input.LA(1)

                    if (LA131_0 == LT) :
                        alt131 = 1


                    if alt131 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT286 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1695)
                        if self.failed:
                            return retval


                    else:
                        break #loop131


                char_literal287 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_catchClause1699)
                if self.failed:
                    return retval

                char_literal287_tree = self.adaptor.createWithPayload(char_literal287)
                self.adaptor.addChild(root_0, char_literal287_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:48: ( LT )*
                while True: #loop132
                    alt132 = 2
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == LT) :
                        alt132 = 1


                    if alt132 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT288 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1701)
                        if self.failed:
                            return retval


                    else:
                        break #loop132


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1705)
                statementBlock289 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock289.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:285:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal290 = None
        LT291 = None
        statementBlock292 = None


        string_literal290_tree = None
        LT291_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal290 = self.input.LT(1)
                self.match(self.input, 81, self.FOLLOW_81_in_finallyClause1717)
                if self.failed:
                    return retval

                string_literal290_tree = self.adaptor.createWithPayload(string_literal290)
                self.adaptor.addChild(root_0, string_literal290_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:16: ( LT )*
                while True: #loop133
                    alt133 = 2
                    LA133_0 = self.input.LA(1)

                    if (LA133_0 == LT) :
                        alt133 = 1


                    if alt133 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT291 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1719)
                        if self.failed:
                            return retval


                    else:
                        break #loop133


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause1723)
                statementBlock292 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock292.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT294 = None
        char_literal295 = None
        LT296 = None
        assignmentExpression293 = None

        assignmentExpression297 = None


        LT294_tree = None
        char_literal295_tree = None
        LT296_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression1735)
                assignmentExpression293 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression293.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop136
                    alt136 = 2
                    alt136 = self.dfa136.predict(self.input)
                    if alt136 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:28: ( LT )*
                        while True: #loop134
                            alt134 = 2
                            LA134_0 = self.input.LA(1)

                            if (LA134_0 == LT) :
                                alt134 = 1


                            if alt134 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT294 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1738)
                                if self.failed:
                                    return retval


                            else:
                                break #loop134


                        char_literal295 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_expression1742)
                        if self.failed:
                            return retval

                        char_literal295_tree = self.adaptor.createWithPayload(char_literal295)
                        self.adaptor.addChild(root_0, char_literal295_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:37: ( LT )*
                        while True: #loop135
                            alt135 = 2
                            LA135_0 = self.input.LA(1)

                            if (LA135_0 == LT) :
                                LA135_2 = self.input.LA(2)

                                if (self.synpred161()) :
                                    alt135 = 1




                            if alt135 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT296 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1744)
                                if self.failed:
                                    return retval


                            else:
                                break #loop135


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression1748)
                        assignmentExpression297 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression297.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT299 = None
        char_literal300 = None
        LT301 = None
        assignmentExpressionNoIn298 = None

        assignmentExpressionNoIn302 = None


        LT299_tree = None
        char_literal300_tree = None
        LT301_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1762)
                assignmentExpressionNoIn298 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn298.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop139
                    alt139 = 2
                    alt139 = self.dfa139.predict(self.input)
                    if alt139 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:32: ( LT )*
                        while True: #loop137
                            alt137 = 2
                            LA137_0 = self.input.LA(1)

                            if (LA137_0 == LT) :
                                alt137 = 1


                            if alt137 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT299 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1765)
                                if self.failed:
                                    return retval


                            else:
                                break #loop137


                        char_literal300 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_expressionNoIn1769)
                        if self.failed:
                            return retval

                        char_literal300_tree = self.adaptor.createWithPayload(char_literal300)
                        self.adaptor.addChild(root_0, char_literal300_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:41: ( LT )*
                        while True: #loop138
                            alt138 = 2
                            LA138_0 = self.input.LA(1)

                            if (LA138_0 == LT) :
                                LA138_2 = self.input.LA(2)

                                if (self.synpred164()) :
                                    alt138 = 1




                            if alt138 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT301 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1771)
                                if self.failed:
                                    return retval


                            else:
                                break #loop138


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1775)
                        assignmentExpressionNoIn302 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn302.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT304 = None
        LT306 = None
        leftHandSideExpression303 = None

        assignmentOperator305 = None

        assignmentExpression307 = None

        conditionalExpression308 = None


        LT304_tree = None
        LT306_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression )
                alt142 = 2
                LA142 = self.input.LA(1)
                if LA142 == 123:
                    LA142_1 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 1, self.input)

                        raise nvae

                elif LA142 == LT:
                    LA142_2 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 2, self.input)

                        raise nvae

                elif LA142 == 47:
                    LA142_3 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 3, self.input)

                        raise nvae

                elif LA142 == 53:
                    LA142_4 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 4, self.input)

                        raise nvae

                elif LA142 == XMLComment:
                    LA142_5 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 5, self.input)

                        raise nvae

                elif LA142 == Identifier or LA142 == 59 or LA142 == 60 or LA142 == 61 or LA142 == 71 or LA142 == 124 or LA142 == 125:
                    LA142_6 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 6, self.input)

                        raise nvae

                elif LA142 == 126:
                    LA142_7 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 7, self.input)

                        raise nvae

                elif LA142 == 127:
                    LA142_8 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 8, self.input)

                        raise nvae

                elif LA142 == 128:
                    LA142_9 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 9, self.input)

                        raise nvae

                elif LA142 == StringLiteral:
                    LA142_10 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 10, self.input)

                        raise nvae

                elif LA142 == NumericLiteral:
                    LA142_11 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 11, self.input)

                        raise nvae

                elif LA142 == 49:
                    LA142_12 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 12, self.input)

                        raise nvae

                elif LA142 == RegularExpressionHacks:
                    LA142_13 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 13, self.input)

                        raise nvae

                elif LA142 == 84:
                    LA142_14 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 14, self.input)

                        raise nvae

                elif LA142 == 56:
                    LA142_15 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 15, self.input)

                        raise nvae

                elif LA142 == 55:
                    LA142_16 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 16, self.input)

                        raise nvae

                elif LA142 == 82:
                    LA142_17 = self.input.LA(2)

                    if (self.synpred168()) :
                        alt142 = 1
                    elif (True) :
                        alt142 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 17, self.input)

                        raise nvae

                elif LA142 == 51 or LA142 == 114 or LA142 == 116 or LA142 == 117 or LA142 == 118 or LA142 == 119 or LA142 == 120 or LA142 == 121 or LA142 == 122:
                    alt142 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("298:1: assignmentExpression : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression | conditionalExpression );", 142, 0, self.input)

                    raise nvae

                if alt142 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1789)
                    leftHandSideExpression303 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression303.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:29: ( LT )*
                    while True: #loop140
                        alt140 = 2
                        LA140_0 = self.input.LA(1)

                        if (LA140_0 == LT) :
                            alt140 = 1


                        if alt140 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT304 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1791)
                            if self.failed:
                                return retval


                        else:
                            break #loop140


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1795)
                    assignmentOperator305 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator305.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:53: ( LT )*
                    while True: #loop141
                        alt141 = 2
                        LA141_0 = self.input.LA(1)

                        if (LA141_0 == LT) :
                            LA141_2 = self.input.LA(2)

                            if (self.synpred167()) :
                                alt141 = 1




                        if alt141 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT306 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1797)
                            if self.failed:
                                return retval


                        else:
                            break #loop141


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1801)
                    assignmentExpression307 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression307.tree)


                elif alt142 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:300:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression1806)
                    conditionalExpression308 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression308.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT310 = None
        LT312 = None
        leftHandSideExpression309 = None

        assignmentOperator311 = None

        assignmentExpressionNoIn313 = None

        conditionalExpressionNoIn314 = None


        LT310_tree = None
        LT312_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:2: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn )
                alt145 = 2
                LA145 = self.input.LA(1)
                if LA145 == 123:
                    LA145_1 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 1, self.input)

                        raise nvae

                elif LA145 == LT:
                    LA145_2 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 2, self.input)

                        raise nvae

                elif LA145 == 47:
                    LA145_3 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 3, self.input)

                        raise nvae

                elif LA145 == 53:
                    LA145_4 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 4, self.input)

                        raise nvae

                elif LA145 == XMLComment:
                    LA145_5 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 5, self.input)

                        raise nvae

                elif LA145 == Identifier or LA145 == 59 or LA145 == 60 or LA145 == 61 or LA145 == 71 or LA145 == 124 or LA145 == 125:
                    LA145_6 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 6, self.input)

                        raise nvae

                elif LA145 == 126:
                    LA145_7 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 7, self.input)

                        raise nvae

                elif LA145 == 127:
                    LA145_8 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 8, self.input)

                        raise nvae

                elif LA145 == 128:
                    LA145_9 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 9, self.input)

                        raise nvae

                elif LA145 == StringLiteral:
                    LA145_10 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 10, self.input)

                        raise nvae

                elif LA145 == NumericLiteral:
                    LA145_11 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 11, self.input)

                        raise nvae

                elif LA145 == 49:
                    LA145_12 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 12, self.input)

                        raise nvae

                elif LA145 == RegularExpressionHacks:
                    LA145_13 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 13, self.input)

                        raise nvae

                elif LA145 == 84:
                    LA145_14 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 14, self.input)

                        raise nvae

                elif LA145 == 56:
                    LA145_15 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 15, self.input)

                        raise nvae

                elif LA145 == 55:
                    LA145_16 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 16, self.input)

                        raise nvae

                elif LA145 == 82:
                    LA145_17 = self.input.LA(2)

                    if (self.synpred171()) :
                        alt145 = 1
                    elif (True) :
                        alt145 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 17, self.input)

                        raise nvae

                elif LA145 == 51 or LA145 == 114 or LA145 == 116 or LA145 == 117 or LA145 == 118 or LA145 == 119 or LA145 == 120 or LA145 == 121 or LA145 == 122:
                    alt145 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("303:1: assignmentExpressionNoIn : ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn | conditionalExpressionNoIn );", 145, 0, self.input)

                    raise nvae

                if alt145 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1818)
                    leftHandSideExpression309 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression309.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:29: ( LT )*
                    while True: #loop143
                        alt143 = 2
                        LA143_0 = self.input.LA(1)

                        if (LA143_0 == LT) :
                            alt143 = 1


                        if alt143 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT310 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1820)
                            if self.failed:
                                return retval


                        else:
                            break #loop143


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1824)
                    assignmentOperator311 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator311.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:53: ( LT )*
                    while True: #loop144
                        alt144 = 2
                        LA144_0 = self.input.LA(1)

                        if (LA144_0 == LT) :
                            LA144_2 = self.input.LA(2)

                            if (self.synpred170()) :
                                alt144 = 1




                        if alt144 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT312 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1826)
                            if self.failed:
                                return retval


                        else:
                            break #loop144


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1830)
                    assignmentExpressionNoIn313 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn313.tree)


                elif alt145 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:305:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1835)
                    conditionalExpressionNoIn314 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn314.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:308:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression315 = None

        newExpression316 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:2: ( callExpression | newExpression )
                alt146 = 2
                LA146 = self.input.LA(1)
                if LA146 == 123:
                    LA146_1 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 1, self.input)

                        raise nvae

                elif LA146 == LT:
                    LA146_2 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 2, self.input)

                        raise nvae

                elif LA146 == 47:
                    LA146_3 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 3, self.input)

                        raise nvae

                elif LA146 == 53:
                    LA146_4 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 4, self.input)

                        raise nvae

                elif LA146 == XMLComment:
                    LA146_5 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 5, self.input)

                        raise nvae

                elif LA146 == Identifier or LA146 == 59 or LA146 == 60 or LA146 == 61 or LA146 == 71 or LA146 == 124 or LA146 == 125:
                    LA146_6 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 6, self.input)

                        raise nvae

                elif LA146 == 126:
                    LA146_7 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 7, self.input)

                        raise nvae

                elif LA146 == 127:
                    LA146_8 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 8, self.input)

                        raise nvae

                elif LA146 == 128:
                    LA146_9 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 9, self.input)

                        raise nvae

                elif LA146 == StringLiteral:
                    LA146_10 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 10, self.input)

                        raise nvae

                elif LA146 == NumericLiteral:
                    LA146_11 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 11, self.input)

                        raise nvae

                elif LA146 == 49:
                    LA146_12 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 12, self.input)

                        raise nvae

                elif LA146 == RegularExpressionHacks:
                    LA146_13 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 13, self.input)

                        raise nvae

                elif LA146 == 84:
                    LA146_14 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 14, self.input)

                        raise nvae

                elif LA146 == 56:
                    LA146_15 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 15, self.input)

                        raise nvae

                elif LA146 == 55:
                    LA146_16 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 16, self.input)

                        raise nvae

                elif LA146 == 82:
                    LA146_17 = self.input.LA(2)

                    if (self.synpred172()) :
                        alt146 = 1
                    elif (True) :
                        alt146 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("308:1: leftHandSideExpression : ( callExpression | newExpression );", 146, 0, self.input)

                    raise nvae

                if alt146 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression1847)
                    callExpression315 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression315.tree)


                elif alt146 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression1852)
                    newExpression316 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression316.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:313:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal318 = None
        LT319 = None
        memberExpression317 = None

        newExpression320 = None


        string_literal318_tree = None
        LT319_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:2: ( memberExpression | 'new' ( LT )* newExpression )
                alt148 = 2
                LA148_0 = self.input.LA(1)

                if ((LT <= LA148_0 <= RegularExpressionHacks) or LA148_0 == 47 or LA148_0 == 49 or LA148_0 == 53 or (55 <= LA148_0 <= 56) or (59 <= LA148_0 <= 61) or LA148_0 == 71 or LA148_0 == 84 or (123 <= LA148_0 <= 128)) :
                    alt148 = 1
                elif (LA148_0 == 82) :
                    LA148_17 = self.input.LA(2)

                    if (self.synpred173()) :
                        alt148 = 1
                    elif (True) :
                        alt148 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("313:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 148, 17, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("313:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 148, 0, self.input)

                    raise nvae

                if alt148 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression1864)
                    memberExpression317 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression317.tree)


                elif alt148 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:4: 'new' ( LT )* newExpression
                    root_0 = self.adaptor.nil()

                    string_literal318 = self.input.LT(1)
                    self.match(self.input, 82, self.FOLLOW_82_in_newExpression1869)
                    if self.failed:
                        return retval

                    string_literal318_tree = self.adaptor.createWithPayload(string_literal318)
                    self.adaptor.addChild(root_0, string_literal318_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:12: ( LT )*
                    while True: #loop147
                        alt147 = 2
                        LA147_0 = self.input.LA(1)

                        if (LA147_0 == LT) :
                            LA147_2 = self.input.LA(2)

                            if (self.synpred174()) :
                                alt147 = 1




                        if alt147 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT319 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1871)
                            if self.failed:
                                return retval


                        else:
                            break #loop147


                    self.following.append(self.FOLLOW_newExpression_in_newExpression1875)
                    newExpression320 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression320.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:1: memberExpression : ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* ;
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal323 = None
        LT324 = None
        LT326 = None
        LT328 = None
        primaryExpression321 = None

        functionExpression322 = None

        memberExpression325 = None

        arguments327 = None

        memberExpressionSuffix329 = None


        string_literal323_tree = None
        LT324_tree = None
        LT326_tree = None
        LT328_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:2: ( ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )
                alt151 = 3
                LA151 = self.input.LA(1)
                if LA151 == LT or LA151 == StringLiteral or LA151 == XMLComment or LA151 == NumericLiteral or LA151 == Identifier or LA151 == RegularExpressionHacks or LA151 == 47 or LA151 == 49 or LA151 == 53 or LA151 == 56 or LA151 == 59 or LA151 == 60 or LA151 == 61 or LA151 == 71 or LA151 == 84 or LA151 == 123 or LA151 == 124 or LA151 == 125 or LA151 == 126 or LA151 == 127 or LA151 == 128:
                    alt151 = 1
                elif LA151 == 55:
                    alt151 = 2
                elif LA151 == 82:
                    alt151 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("319:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )", 151, 0, self.input)

                    raise nvae

                if alt151 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:5: primaryExpression
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression1888)
                    primaryExpression321 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, primaryExpression321.tree)


                elif alt151 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:25: functionExpression
                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression1892)
                    functionExpression322 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression322.tree)


                elif alt151 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:46: 'new' ( LT )* memberExpression ( LT )* arguments
                    string_literal323 = self.input.LT(1)
                    self.match(self.input, 82, self.FOLLOW_82_in_memberExpression1896)
                    if self.failed:
                        return retval

                    string_literal323_tree = self.adaptor.createWithPayload(string_literal323)
                    self.adaptor.addChild(root_0, string_literal323_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:54: ( LT )*
                    while True: #loop149
                        alt149 = 2
                        LA149_0 = self.input.LA(1)

                        if (LA149_0 == LT) :
                            LA149_2 = self.input.LA(2)

                            if (self.synpred177()) :
                                alt149 = 1




                        if alt149 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT324 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1898)
                            if self.failed:
                                return retval


                        else:
                            break #loop149


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression1902)
                    memberExpression325 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression325.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:76: ( LT )*
                    while True: #loop150
                        alt150 = 2
                        LA150_0 = self.input.LA(1)

                        if (LA150_0 == LT) :
                            alt150 = 1


                        if alt150 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT326 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1904)
                            if self.failed:
                                return retval


                        else:
                            break #loop150


                    self.following.append(self.FOLLOW_arguments_in_memberExpression1908)
                    arguments327 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments327.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:90: ( ( LT )* memberExpressionSuffix )*
                while True: #loop153
                    alt153 = 2
                    LA153 = self.input.LA(1)
                    if LA153 == LT:
                        LA153_1 = self.input.LA(2)

                        if (self.synpred180()) :
                            alt153 = 1


                    elif LA153 == 50:
                        LA153_21 = self.input.LA(2)

                        if (self.synpred180()) :
                            alt153 = 1


                    elif LA153 == 83:
                        LA153_24 = self.input.LA(2)

                        if (self.synpred180()) :
                            alt153 = 1


                    elif LA153 == 84:
                        alt153 = 1

                    if alt153 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:91: ( LT )* memberExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:93: ( LT )*
                        while True: #loop152
                            alt152 = 2
                            LA152_0 = self.input.LA(1)

                            if (LA152_0 == LT) :
                                alt152 = 1


                            if alt152 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT328 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1912)
                                if self.failed:
                                    return retval


                            else:
                                break #loop152


                        self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1916)
                        memberExpressionSuffix329 = self.memberExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, memberExpressionSuffix329.tree)


                    else:
                        break #loop153





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix330 = None

        propertyReferenceSuffix331 = None

        descendentSuffix332 = None

        namespaceSuffix333 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:2: ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt154 = 4
                LA154 = self.input.LA(1)
                if LA154 == 84:
                    alt154 = 1
                elif LA154 == 83:
                    LA154_2 = self.input.LA(2)

                    if (LA154_2 == 83) :
                        alt154 = 3
                    elif (LA154_2 == LT or LA154_2 == Identifier or (59 <= LA154_2 <= 61) or LA154_2 == 71 or LA154_2 == 86 or (124 <= LA154_2 <= 125)) :
                        alt154 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("322:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 154, 2, self.input)

                        raise nvae

                elif LA154 == 50:
                    alt154 = 4
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("322:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 154, 0, self.input)

                    raise nvae

                if alt154 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix1930)
                    indexSuffix330 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix330.tree)


                elif alt154 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:324:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1935)
                    propertyReferenceSuffix331 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix331.tree)


                elif alt154 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:325:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_memberExpressionSuffix1940)
                    descendentSuffix332 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix332.tree)


                elif alt154 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_memberExpressionSuffix1946)
                    namespaceSuffix333 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix333.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:332:1: callExpression : memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT335 = None
        char_literal336 = None
        LT337 = None
        LT339 = None
        memberExpression334 = None

        arguments338 = None

        callExpressionSuffix340 = None


        LT335_tree = None
        char_literal336_tree = None
        LT337_tree = None
        LT339_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_83 = RewriteRuleTokenStream(self.adaptor, "token 83")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_callExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule callExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:2: ( memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:4: memberExpression ( LT )* ( '.' )? ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                self.following.append(self.FOLLOW_memberExpression_in_callExpression1961)
                memberExpression334 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_memberExpression.add(memberExpression334.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:21: ( LT )*
                while True: #loop155
                    alt155 = 2
                    LA155_0 = self.input.LA(1)

                    if (LA155_0 == LT) :
                        LA155_2 = self.input.LA(2)

                        if (self.synpred184()) :
                            alt155 = 1




                    if alt155 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT335 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1963)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT335)


                    else:
                        break #loop155


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:25: ( '.' )?
                alt156 = 2
                LA156_0 = self.input.LA(1)

                if (LA156_0 == 83) :
                    alt156 = 1
                if alt156 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: '.'
                    char_literal336 = self.input.LT(1)
                    self.match(self.input, 83, self.FOLLOW_83_in_callExpression1966)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_83.add(char_literal336)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:30: ( LT )*
                while True: #loop157
                    alt157 = 2
                    LA157_0 = self.input.LA(1)

                    if (LA157_0 == LT) :
                        alt157 = 1


                    if alt157 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT337 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1969)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT337)


                    else:
                        break #loop157


                self.following.append(self.FOLLOW_arguments_in_callExpression1972)
                arguments338 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_arguments.add(arguments338.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:44: ( ( LT )* callExpressionSuffix )*
                while True: #loop159
                    alt159 = 2
                    LA159 = self.input.LA(1)
                    if LA159 == LT:
                        LA159_1 = self.input.LA(2)

                        if (self.synpred188()) :
                            alt159 = 1


                    elif LA159 == 50:
                        LA159_21 = self.input.LA(2)

                        if (self.synpred188()) :
                            alt159 = 1


                    elif LA159 == 56 or LA159 == 83 or LA159 == 84:
                        alt159 = 1

                    if alt159 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:45: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:45: ( LT )*
                        while True: #loop158
                            alt158 = 2
                            LA158_0 = self.input.LA(1)

                            if (LA158_0 == LT) :
                                alt158 = 1


                            if alt158 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT339 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1975)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT339)


                            else:
                                break #loop158


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression1978)
                        callExpressionSuffix340 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_callExpressionSuffix.add(callExpressionSuffix340.tree)


                    else:
                        break #loop159


                # AST Rewrite
                # elements: callExpressionSuffix, arguments, memberExpression
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
                    # 334:3: -> ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:6: ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_1)

                    self.adaptor.addChild(root_1, stream_memberExpression.next())
                    self.adaptor.addChild(root_1, stream_arguments.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:40: ( callExpressionSuffix )*
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments341 = None

        indexSuffix342 = None

        propertyReferenceSuffix343 = None

        descendentSuffix344 = None

        namespaceSuffix345 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:2: ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix )
                alt160 = 5
                LA160 = self.input.LA(1)
                if LA160 == 56:
                    alt160 = 1
                elif LA160 == 84:
                    alt160 = 2
                elif LA160 == 83:
                    LA160_3 = self.input.LA(2)

                    if (LA160_3 == 83) :
                        alt160 = 4
                    elif (LA160_3 == LT or LA160_3 == Identifier or (59 <= LA160_3 <= 61) or LA160_3 == 71 or LA160_3 == 86 or (124 <= LA160_3 <= 125)) :
                        alt160 = 3
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("337:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 160, 3, self.input)

                        raise nvae

                elif LA160 == 50:
                    alt160 = 5
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("337:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix | descendentSuffix | namespaceSuffix );", 160, 0, self.input)

                    raise nvae

                if alt160 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix2007)
                    arguments341 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments341.tree)


                elif alt160 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix2012)
                    indexSuffix342 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix342.tree)


                elif alt160 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:340:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2017)
                    propertyReferenceSuffix343 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix343.tree)


                elif alt160 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:4: descendentSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_descendentSuffix_in_callExpressionSuffix2022)
                    descendentSuffix344 = self.descendentSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, descendentSuffix344.tree)


                elif alt160 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:4: namespaceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_namespaceSuffix_in_callExpressionSuffix2028)
                    namespaceSuffix345 = self.namespaceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, namespaceSuffix345.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:1: arguments : '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal346 = None
        LT347 = None
        LT349 = None
        char_literal350 = None
        LT351 = None
        LT353 = None
        LT354 = None
        char_literal355 = None
        assignmentExpression348 = None

        assignmentExpression352 = None


        char_literal346_tree = None
        LT347_tree = None
        LT349_tree = None
        char_literal350_tree = None
        LT351_tree = None
        LT353_tree = None
        LT354_tree = None
        char_literal355_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:2: ( '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:4: '(' ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal346 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_arguments2043)
                if self.failed:
                    return retval

                char_literal346_tree = self.adaptor.createWithPayload(char_literal346)
                self.adaptor.addChild(root_0, char_literal346_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:8: ( ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )* )?
                alt166 = 2
                alt166 = self.dfa166.predict(self.input)
                if alt166 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:9: ( LT )* assignmentExpression ( LT )* ( ',' ( LT )* assignmentExpression ( LT )* )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:11: ( LT )*
                    while True: #loop161
                        alt161 = 2
                        LA161_0 = self.input.LA(1)

                        if (LA161_0 == LT) :
                            LA161_2 = self.input.LA(2)

                            if (self.synpred193()) :
                                alt161 = 1




                        if alt161 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT347 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2046)
                            if self.failed:
                                return retval


                        else:
                            break #loop161


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments2050)
                    assignmentExpression348 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression348.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:37: ( LT )*
                    while True: #loop162
                        alt162 = 2
                        LA162_0 = self.input.LA(1)

                        if (LA162_0 == LT) :
                            LA162_2 = self.input.LA(2)

                            if (self.synpred194()) :
                                alt162 = 1




                        if alt162 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT349 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments2052)
                            if self.failed:
                                return retval


                        else:
                            break #loop162


                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:40: ( ',' ( LT )* assignmentExpression ( LT )* )*
                    while True: #loop165
                        alt165 = 2
                        LA165_0 = self.input.LA(1)

                        if (LA165_0 == 57) :
                            alt165 = 1


                        if alt165 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:41: ',' ( LT )* assignmentExpression ( LT )*
                            char_literal350 = self.input.LT(1)
                            self.match(self.input, 57, self.FOLLOW_57_in_arguments2057)
                            if self.failed:
                                return retval

                            char_literal350_tree = self.adaptor.createWithPayload(char_literal350)
                            self.adaptor.addChild(root_0, char_literal350_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:47: ( LT )*
                            while True: #loop163
                                alt163 = 2
                                LA163_0 = self.input.LA(1)

                                if (LA163_0 == LT) :
                                    LA163_2 = self.input.LA(2)

                                    if (self.synpred195()) :
                                        alt163 = 1




                                if alt163 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT351 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2059)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop163


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments2063)
                            assignmentExpression352 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression352.tree)
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:73: ( LT )*
                            while True: #loop164
                                alt164 = 2
                                LA164_0 = self.input.LA(1)

                                if (LA164_0 == LT) :
                                    LA164_1 = self.input.LA(2)

                                    if (self.synpred196()) :
                                        alt164 = 1




                                if alt164 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT353 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments2065)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop164




                        else:
                            break #loop165





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:82: ( LT )*
                while True: #loop167
                    alt167 = 2
                    LA167_0 = self.input.LA(1)

                    if (LA167_0 == LT) :
                        alt167 = 1


                    if alt167 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT354 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments2073)
                        if self.failed:
                            return retval


                    else:
                        break #loop167


                char_literal355 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_arguments2077)
                if self.failed:
                    return retval

                char_literal355_tree = self.adaptor.createWithPayload(char_literal355)
                self.adaptor.addChild(root_0, char_literal355_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:352:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal356 = None
        LT357 = None
        LT359 = None
        char_literal360 = None
        expression358 = None


        char_literal356_tree = None
        LT357_tree = None
        LT359_tree = None
        char_literal360_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_84 = RewriteRuleTokenStream(self.adaptor, "token 84")
        stream_85 = RewriteRuleTokenStream(self.adaptor, "token 85")
        stream_expression = RewriteRuleSubtreeStream(self.adaptor, "rule expression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:2: ( '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:4: '[' ( LT )* expression ( LT )* ']'
                char_literal356 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_indexSuffix2089)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_84.add(char_literal356)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:8: ( LT )*
                while True: #loop168
                    alt168 = 2
                    LA168_0 = self.input.LA(1)

                    if (LA168_0 == LT) :
                        LA168_2 = self.input.LA(2)

                        if (self.synpred200()) :
                            alt168 = 1




                    if alt168 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT357 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2091)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT357)


                    else:
                        break #loop168


                self.following.append(self.FOLLOW_expression_in_indexSuffix2094)
                expression358 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_expression.add(expression358.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:23: ( LT )*
                while True: #loop169
                    alt169 = 2
                    LA169_0 = self.input.LA(1)

                    if (LA169_0 == LT) :
                        alt169 = 1


                    if alt169 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT359 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix2096)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT359)


                    else:
                        break #loop169


                char_literal360 = self.input.LT(1)
                self.match(self.input, 85, self.FOLLOW_85_in_indexSuffix2099)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_85.add(char_literal360)
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
                    # 354:3: -> ^( INDEXREF expression )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:6: ^( INDEXREF expression )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:357:1: propertyReferenceSuffix : '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal361 = None
        LT362 = None
        e4xIdentifier363 = None


        char_literal361_tree = None
        LT362_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_83 = RewriteRuleTokenStream(self.adaptor, "token 83")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:2: ( '.' ( LT )* e4xIdentifier -> ^( PROPREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:4: '.' ( LT )* e4xIdentifier
                char_literal361 = self.input.LT(1)
                self.match(self.input, 83, self.FOLLOW_83_in_propertyReferenceSuffix2122)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_83.add(char_literal361)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:8: ( LT )*
                while True: #loop170
                    alt170 = 2
                    LA170_0 = self.input.LA(1)

                    if (LA170_0 == LT) :
                        alt170 = 1


                    if alt170 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT362 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix2124)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT362)


                    else:
                        break #loop170


                self.following.append(self.FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2127)
                e4xIdentifier363 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier363.tree)
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
                    # 359:3: -> ^( PROPREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:6: ^( PROPREF e4xIdentifier )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:362:1: descendentSuffix : '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) ;
    def descendentSuffix(self, ):

        retval = self.descendentSuffix_return()
        retval.start = self.input.LT(1)
        descendentSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal364 = None
        char_literal365 = None
        LT366 = None
        e4xIdentifier367 = None


        char_literal364_tree = None
        char_literal365_tree = None
        LT366_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_83 = RewriteRuleTokenStream(self.adaptor, "token 83")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:2: ( '.' '.' ( LT )* e4xIdentifier -> ^( DESCREF e4xIdentifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:4: '.' '.' ( LT )* e4xIdentifier
                char_literal364 = self.input.LT(1)
                self.match(self.input, 83, self.FOLLOW_83_in_descendentSuffix2148)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_83.add(char_literal364)
                char_literal365 = self.input.LT(1)
                self.match(self.input, 83, self.FOLLOW_83_in_descendentSuffix2150)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_83.add(char_literal365)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:12: ( LT )*
                while True: #loop171
                    alt171 = 2
                    LA171_0 = self.input.LA(1)

                    if (LA171_0 == LT) :
                        alt171 = 1


                    if alt171 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT366 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_descendentSuffix2152)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT366)


                    else:
                        break #loop171


                self.following.append(self.FOLLOW_e4xIdentifier_in_descendentSuffix2155)
                e4xIdentifier367 = self.e4xIdentifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_e4xIdentifier.add(e4xIdentifier367.tree)
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
                    # 364:3: -> ^( DESCREF e4xIdentifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:6: ^( DESCREF e4xIdentifier )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:367:1: namespaceSuffix : ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) ;
    def namespaceSuffix(self, ):

        retval = self.namespaceSuffix_return()
        retval.start = self.input.LT(1)
        namespaceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal368 = None
        char_literal369 = None
        LT370 = None
        e4xIdentifier371 = None


        char_literal368_tree = None
        char_literal369_tree = None
        LT370_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_e4xIdentifier = RewriteRuleSubtreeStream(self.adaptor, "rule e4xIdentifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:2: ( ':' ':' ( LT )* ( e4xIdentifier )? -> ^( NSREF ( e4xIdentifier )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:4: ':' ':' ( LT )* ( e4xIdentifier )?
                char_literal368 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_namespaceSuffix2176)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal368)
                char_literal369 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_namespaceSuffix2178)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_50.add(char_literal369)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:12: ( LT )*
                while True: #loop172
                    alt172 = 2
                    LA172_0 = self.input.LA(1)

                    if (LA172_0 == LT) :
                        LA172_2 = self.input.LA(2)

                        if (self.synpred204()) :
                            alt172 = 1




                    if alt172 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT370 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_namespaceSuffix2180)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT370)


                    else:
                        break #loop172


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:16: ( e4xIdentifier )?
                alt173 = 2
                LA173_0 = self.input.LA(1)

                if (LA173_0 == Identifier or (59 <= LA173_0 <= 61) or LA173_0 == 71 or (124 <= LA173_0 <= 125)) :
                    alt173 = 1
                elif (LA173_0 == 86) :
                    LA173_2 = self.input.LA(2)

                    if (self.synpred205()) :
                        alt173 = 1
                if alt173 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: e4xIdentifier
                    self.following.append(self.FOLLOW_e4xIdentifier_in_namespaceSuffix2183)
                    e4xIdentifier371 = self.e4xIdentifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_e4xIdentifier.add(e4xIdentifier371.tree)



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
                    # 369:3: -> ^( NSREF ( e4xIdentifier )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:6: ^( NSREF ( e4xIdentifier )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(NSREF, "NSREF"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:14: ( e4xIdentifier )?
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:372:1: e4xIdentifier : ( identifier | '*' );
    def e4xIdentifier(self, ):

        retval = self.e4xIdentifier_return()
        retval.start = self.input.LT(1)
        e4xIdentifier_StartIndex = self.input.index()
        root_0 = None

        char_literal373 = None
        identifier372 = None


        char_literal373_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:2: ( identifier | '*' )
                alt174 = 2
                LA174_0 = self.input.LA(1)

                if (LA174_0 == Identifier or (59 <= LA174_0 <= 61) or LA174_0 == 71 or (124 <= LA174_0 <= 125)) :
                    alt174 = 1
                elif (LA174_0 == 86) :
                    alt174 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("372:1: e4xIdentifier : ( identifier | '*' );", 174, 0, self.input)

                    raise nvae

                if alt174 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_e4xIdentifier2206)
                    identifier372 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier372.tree)


                elif alt174 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal373 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_e4xIdentifier2211)
                    if self.failed:
                        return retval

                    char_literal373_tree = self.adaptor.createWithPayload(char_literal373)
                    self.adaptor.addChild(root_0, char_literal373_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:377:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set374 = None

        set374_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set374 = self.input.LT(1)
                if self.input.LA(1) == 52 or (87 <= self.input.LA(1) <= 97):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set374))
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT376 = None
        char_literal377 = None
        LT378 = None
        LT380 = None
        char_literal381 = None
        LT382 = None
        logicalORExpression375 = None

        assignmentExpression379 = None

        assignmentExpression383 = None


        LT376_tree = None
        char_literal377_tree = None
        LT378_tree = None
        LT380_tree = None
        char_literal381_tree = None
        LT382_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression2278)
                logicalORExpression375 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression375.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt179 = 2
                alt179 = self.dfa179.predict(self.input)
                if alt179 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:27: ( LT )*
                    while True: #loop175
                        alt175 = 2
                        LA175_0 = self.input.LA(1)

                        if (LA175_0 == LT) :
                            alt175 = 1


                        if alt175 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT376 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2281)
                            if self.failed:
                                return retval


                        else:
                            break #loop175


                    char_literal377 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_conditionalExpression2285)
                    if self.failed:
                        return retval

                    char_literal377_tree = self.adaptor.createWithPayload(char_literal377)
                    self.adaptor.addChild(root_0, char_literal377_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:36: ( LT )*
                    while True: #loop176
                        alt176 = 2
                        LA176_0 = self.input.LA(1)

                        if (LA176_0 == LT) :
                            LA176_2 = self.input.LA(2)

                            if (self.synpred219()) :
                                alt176 = 1




                        if alt176 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT378 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2287)
                            if self.failed:
                                return retval


                        else:
                            break #loop176


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2291)
                    assignmentExpression379 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression379.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:62: ( LT )*
                    while True: #loop177
                        alt177 = 2
                        LA177_0 = self.input.LA(1)

                        if (LA177_0 == LT) :
                            alt177 = 1


                        if alt177 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT380 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2293)
                            if self.failed:
                                return retval


                        else:
                            break #loop177


                    char_literal381 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_conditionalExpression2297)
                    if self.failed:
                        return retval

                    char_literal381_tree = self.adaptor.createWithPayload(char_literal381)
                    self.adaptor.addChild(root_0, char_literal381_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:71: ( LT )*
                    while True: #loop178
                        alt178 = 2
                        LA178_0 = self.input.LA(1)

                        if (LA178_0 == LT) :
                            LA178_2 = self.input.LA(2)

                            if (self.synpred221()) :
                                alt178 = 1




                        if alt178 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT382 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression2299)
                            if self.failed:
                                return retval


                        else:
                            break #loop178


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression2303)
                    assignmentExpression383 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression383.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
    def conditionalExpressionNoIn(self, ):

        retval = self.conditionalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        conditionalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT385 = None
        char_literal386 = None
        LT387 = None
        LT389 = None
        char_literal390 = None
        LT391 = None
        logicalORExpressionNoIn384 = None

        assignmentExpressionNoIn388 = None

        assignmentExpressionNoIn392 = None


        LT385_tree = None
        char_literal386_tree = None
        LT387_tree = None
        LT389_tree = None
        char_literal390_tree = None
        LT391_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2316)
                logicalORExpressionNoIn384 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn384.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt184 = 2
                alt184 = self.dfa184.predict(self.input)
                if alt184 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:31: ( LT )*
                    while True: #loop180
                        alt180 = 2
                        LA180_0 = self.input.LA(1)

                        if (LA180_0 == LT) :
                            alt180 = 1


                        if alt180 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT385 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2319)
                            if self.failed:
                                return retval


                        else:
                            break #loop180


                    char_literal386 = self.input.LT(1)
                    self.match(self.input, 98, self.FOLLOW_98_in_conditionalExpressionNoIn2323)
                    if self.failed:
                        return retval

                    char_literal386_tree = self.adaptor.createWithPayload(char_literal386)
                    self.adaptor.addChild(root_0, char_literal386_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:40: ( LT )*
                    while True: #loop181
                        alt181 = 2
                        LA181_0 = self.input.LA(1)

                        if (LA181_0 == LT) :
                            LA181_2 = self.input.LA(2)

                            if (self.synpred224()) :
                                alt181 = 1




                        if alt181 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT387 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2325)
                            if self.failed:
                                return retval


                        else:
                            break #loop181


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2329)
                    assignmentExpressionNoIn388 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn388.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:70: ( LT )*
                    while True: #loop182
                        alt182 = 2
                        LA182_0 = self.input.LA(1)

                        if (LA182_0 == LT) :
                            alt182 = 1


                        if alt182 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT389 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2331)
                            if self.failed:
                                return retval


                        else:
                            break #loop182


                    char_literal390 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_conditionalExpressionNoIn2335)
                    if self.failed:
                        return retval

                    char_literal390_tree = self.adaptor.createWithPayload(char_literal390)
                    self.adaptor.addChild(root_0, char_literal390_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:79: ( LT )*
                    while True: #loop183
                        alt183 = 2
                        LA183_0 = self.input.LA(1)

                        if (LA183_0 == LT) :
                            LA183_2 = self.input.LA(2)

                            if (self.synpred226()) :
                                alt183 = 1




                        if alt183 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT391 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn2337)
                            if self.failed:
                                return retval


                        else:
                            break #loop183


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2341)
                    assignmentExpressionNoIn392 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn392.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
    def logicalORExpression(self, ):

        retval = self.logicalORExpression_return()
        retval.start = self.input.LT(1)
        logicalORExpression_StartIndex = self.input.index()
        root_0 = None

        LT394 = None
        string_literal395 = None
        LT396 = None
        logicalANDExpression393 = None

        logicalANDExpression397 = None


        LT394_tree = None
        string_literal395_tree = None
        LT396_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2354)
                logicalANDExpression393 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression393.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop187
                    alt187 = 2
                    alt187 = self.dfa187.predict(self.input)
                    if alt187 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:28: ( LT )*
                        while True: #loop185
                            alt185 = 2
                            LA185_0 = self.input.LA(1)

                            if (LA185_0 == LT) :
                                alt185 = 1


                            if alt185 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT394 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2357)
                                if self.failed:
                                    return retval


                            else:
                                break #loop185


                        string_literal395 = self.input.LT(1)
                        self.match(self.input, 99, self.FOLLOW_99_in_logicalORExpression2361)
                        if self.failed:
                            return retval

                        string_literal395_tree = self.adaptor.createWithPayload(string_literal395)
                        self.adaptor.addChild(root_0, string_literal395_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:38: ( LT )*
                        while True: #loop186
                            alt186 = 2
                            LA186_0 = self.input.LA(1)

                            if (LA186_0 == LT) :
                                LA186_2 = self.input.LA(2)

                                if (self.synpred229()) :
                                    alt186 = 1




                            if alt186 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT396 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression2363)
                                if self.failed:
                                    return retval


                            else:
                                break #loop186


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression2367)
                        logicalANDExpression397 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression397.tree)


                    else:
                        break #loop187





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:393:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
    def logicalORExpressionNoIn(self, ):

        retval = self.logicalORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT399 = None
        string_literal400 = None
        LT401 = None
        logicalANDExpressionNoIn398 = None

        logicalANDExpressionNoIn402 = None


        LT399_tree = None
        string_literal400_tree = None
        LT401_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2381)
                logicalANDExpressionNoIn398 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn398.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop190
                    alt190 = 2
                    alt190 = self.dfa190.predict(self.input)
                    if alt190 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:32: ( LT )*
                        while True: #loop188
                            alt188 = 2
                            LA188_0 = self.input.LA(1)

                            if (LA188_0 == LT) :
                                alt188 = 1


                            if alt188 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT399 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2384)
                                if self.failed:
                                    return retval


                            else:
                                break #loop188


                        string_literal400 = self.input.LT(1)
                        self.match(self.input, 99, self.FOLLOW_99_in_logicalORExpressionNoIn2388)
                        if self.failed:
                            return retval

                        string_literal400_tree = self.adaptor.createWithPayload(string_literal400)
                        self.adaptor.addChild(root_0, string_literal400_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:42: ( LT )*
                        while True: #loop189
                            alt189 = 2
                            LA189_0 = self.input.LA(1)

                            if (LA189_0 == LT) :
                                LA189_2 = self.input.LA(2)

                                if (self.synpred232()) :
                                    alt189 = 1




                            if alt189 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT401 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn2390)
                                if self.failed:
                                    return retval


                            else:
                                break #loop189


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2394)
                        logicalANDExpressionNoIn402 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn402.tree)


                    else:
                        break #loop190





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:397:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
    def logicalANDExpression(self, ):

        retval = self.logicalANDExpression_return()
        retval.start = self.input.LT(1)
        logicalANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT404 = None
        string_literal405 = None
        LT406 = None
        bitwiseORExpression403 = None

        bitwiseORExpression407 = None


        LT404_tree = None
        string_literal405_tree = None
        LT406_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2408)
                bitwiseORExpression403 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression403.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop193
                    alt193 = 2
                    alt193 = self.dfa193.predict(self.input)
                    if alt193 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:27: ( LT )*
                        while True: #loop191
                            alt191 = 2
                            LA191_0 = self.input.LA(1)

                            if (LA191_0 == LT) :
                                alt191 = 1


                            if alt191 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT404 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2411)
                                if self.failed:
                                    return retval


                            else:
                                break #loop191


                        string_literal405 = self.input.LT(1)
                        self.match(self.input, 100, self.FOLLOW_100_in_logicalANDExpression2415)
                        if self.failed:
                            return retval

                        string_literal405_tree = self.adaptor.createWithPayload(string_literal405)
                        self.adaptor.addChild(root_0, string_literal405_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:37: ( LT )*
                        while True: #loop192
                            alt192 = 2
                            LA192_0 = self.input.LA(1)

                            if (LA192_0 == LT) :
                                LA192_2 = self.input.LA(2)

                                if (self.synpred235()) :
                                    alt192 = 1




                            if alt192 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT406 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression2417)
                                if self.failed:
                                    return retval


                            else:
                                break #loop192


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression2421)
                        bitwiseORExpression407 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression407.tree)


                    else:
                        break #loop193





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:401:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
    def logicalANDExpressionNoIn(self, ):

        retval = self.logicalANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT409 = None
        string_literal410 = None
        LT411 = None
        bitwiseORExpressionNoIn408 = None

        bitwiseORExpressionNoIn412 = None


        LT409_tree = None
        string_literal410_tree = None
        LT411_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2435)
                bitwiseORExpressionNoIn408 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn408.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop196
                    alt196 = 2
                    alt196 = self.dfa196.predict(self.input)
                    if alt196 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:31: ( LT )*
                        while True: #loop194
                            alt194 = 2
                            LA194_0 = self.input.LA(1)

                            if (LA194_0 == LT) :
                                alt194 = 1


                            if alt194 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT409 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2438)
                                if self.failed:
                                    return retval


                            else:
                                break #loop194


                        string_literal410 = self.input.LT(1)
                        self.match(self.input, 100, self.FOLLOW_100_in_logicalANDExpressionNoIn2442)
                        if self.failed:
                            return retval

                        string_literal410_tree = self.adaptor.createWithPayload(string_literal410)
                        self.adaptor.addChild(root_0, string_literal410_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:41: ( LT )*
                        while True: #loop195
                            alt195 = 2
                            LA195_0 = self.input.LA(1)

                            if (LA195_0 == LT) :
                                LA195_2 = self.input.LA(2)

                                if (self.synpred238()) :
                                    alt195 = 1




                            if alt195 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT411 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn2444)
                                if self.failed:
                                    return retval


                            else:
                                break #loop195


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2448)
                        bitwiseORExpressionNoIn412 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn412.tree)


                    else:
                        break #loop196





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:405:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
    def bitwiseORExpression(self, ):

        retval = self.bitwiseORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseORExpression_StartIndex = self.input.index()
        root_0 = None

        LT414 = None
        char_literal415 = None
        LT416 = None
        bitwiseXORExpression413 = None

        bitwiseXORExpression417 = None


        LT414_tree = None
        char_literal415_tree = None
        LT416_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2462)
                bitwiseXORExpression413 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression413.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop199
                    alt199 = 2
                    alt199 = self.dfa199.predict(self.input)
                    if alt199 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:28: ( LT )*
                        while True: #loop197
                            alt197 = 2
                            LA197_0 = self.input.LA(1)

                            if (LA197_0 == LT) :
                                alt197 = 1


                            if alt197 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT414 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2465)
                                if self.failed:
                                    return retval


                            else:
                                break #loop197


                        char_literal415 = self.input.LT(1)
                        self.match(self.input, 101, self.FOLLOW_101_in_bitwiseORExpression2469)
                        if self.failed:
                            return retval

                        char_literal415_tree = self.adaptor.createWithPayload(char_literal415)
                        self.adaptor.addChild(root_0, char_literal415_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:37: ( LT )*
                        while True: #loop198
                            alt198 = 2
                            LA198_0 = self.input.LA(1)

                            if (LA198_0 == LT) :
                                LA198_2 = self.input.LA(2)

                                if (self.synpred241()) :
                                    alt198 = 1




                            if alt198 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT416 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2471)
                                if self.failed:
                                    return retval


                            else:
                                break #loop198


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2475)
                        bitwiseXORExpression417 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression417.tree)


                    else:
                        break #loop199





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:409:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
    def bitwiseORExpressionNoIn(self, ):

        retval = self.bitwiseORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT419 = None
        char_literal420 = None
        LT421 = None
        bitwiseXORExpressionNoIn418 = None

        bitwiseXORExpressionNoIn422 = None


        LT419_tree = None
        char_literal420_tree = None
        LT421_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2489)
                bitwiseXORExpressionNoIn418 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn418.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop202
                    alt202 = 2
                    alt202 = self.dfa202.predict(self.input)
                    if alt202 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:32: ( LT )*
                        while True: #loop200
                            alt200 = 2
                            LA200_0 = self.input.LA(1)

                            if (LA200_0 == LT) :
                                alt200 = 1


                            if alt200 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT419 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2492)
                                if self.failed:
                                    return retval


                            else:
                                break #loop200


                        char_literal420 = self.input.LT(1)
                        self.match(self.input, 101, self.FOLLOW_101_in_bitwiseORExpressionNoIn2496)
                        if self.failed:
                            return retval

                        char_literal420_tree = self.adaptor.createWithPayload(char_literal420)
                        self.adaptor.addChild(root_0, char_literal420_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:41: ( LT )*
                        while True: #loop201
                            alt201 = 2
                            LA201_0 = self.input.LA(1)

                            if (LA201_0 == LT) :
                                LA201_2 = self.input.LA(2)

                                if (self.synpred244()) :
                                    alt201 = 1




                            if alt201 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT421 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2498)
                                if self.failed:
                                    return retval


                            else:
                                break #loop201


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2502)
                        bitwiseXORExpressionNoIn422 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn422.tree)


                    else:
                        break #loop202





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:413:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
    def bitwiseXORExpression(self, ):

        retval = self.bitwiseXORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpression_StartIndex = self.input.index()
        root_0 = None

        LT424 = None
        char_literal425 = None
        LT426 = None
        bitwiseANDExpression423 = None

        bitwiseANDExpression427 = None


        LT424_tree = None
        char_literal425_tree = None
        LT426_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2516)
                bitwiseANDExpression423 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression423.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop205
                    alt205 = 2
                    alt205 = self.dfa205.predict(self.input)
                    if alt205 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:28: ( LT )*
                        while True: #loop203
                            alt203 = 2
                            LA203_0 = self.input.LA(1)

                            if (LA203_0 == LT) :
                                alt203 = 1


                            if alt203 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT424 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2519)
                                if self.failed:
                                    return retval


                            else:
                                break #loop203


                        char_literal425 = self.input.LT(1)
                        self.match(self.input, 102, self.FOLLOW_102_in_bitwiseXORExpression2523)
                        if self.failed:
                            return retval

                        char_literal425_tree = self.adaptor.createWithPayload(char_literal425)
                        self.adaptor.addChild(root_0, char_literal425_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:37: ( LT )*
                        while True: #loop204
                            alt204 = 2
                            LA204_0 = self.input.LA(1)

                            if (LA204_0 == LT) :
                                LA204_2 = self.input.LA(2)

                                if (self.synpred247()) :
                                    alt204 = 1




                            if alt204 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT426 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2525)
                                if self.failed:
                                    return retval


                            else:
                                break #loop204


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2529)
                        bitwiseANDExpression427 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression427.tree)


                    else:
                        break #loop205





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:417:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
    def bitwiseXORExpressionNoIn(self, ):

        retval = self.bitwiseXORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT429 = None
        char_literal430 = None
        LT431 = None
        bitwiseANDExpressionNoIn428 = None

        bitwiseANDExpressionNoIn432 = None


        LT429_tree = None
        char_literal430_tree = None
        LT431_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2543)
                bitwiseANDExpressionNoIn428 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn428.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop208
                    alt208 = 2
                    alt208 = self.dfa208.predict(self.input)
                    if alt208 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:32: ( LT )*
                        while True: #loop206
                            alt206 = 2
                            LA206_0 = self.input.LA(1)

                            if (LA206_0 == LT) :
                                alt206 = 1


                            if alt206 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT429 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2546)
                                if self.failed:
                                    return retval


                            else:
                                break #loop206


                        char_literal430 = self.input.LT(1)
                        self.match(self.input, 102, self.FOLLOW_102_in_bitwiseXORExpressionNoIn2550)
                        if self.failed:
                            return retval

                        char_literal430_tree = self.adaptor.createWithPayload(char_literal430)
                        self.adaptor.addChild(root_0, char_literal430_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:41: ( LT )*
                        while True: #loop207
                            alt207 = 2
                            LA207_0 = self.input.LA(1)

                            if (LA207_0 == LT) :
                                LA207_2 = self.input.LA(2)

                                if (self.synpred250()) :
                                    alt207 = 1




                            if alt207 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT431 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2552)
                                if self.failed:
                                    return retval


                            else:
                                break #loop207


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2556)
                        bitwiseANDExpressionNoIn432 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn432.tree)


                    else:
                        break #loop208





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:421:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
    def bitwiseANDExpression(self, ):

        retval = self.bitwiseANDExpression_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT434 = None
        char_literal435 = None
        LT436 = None
        equalityExpression433 = None

        equalityExpression437 = None


        LT434_tree = None
        char_literal435_tree = None
        LT436_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2570)
                equalityExpression433 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression433.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop211
                    alt211 = 2
                    alt211 = self.dfa211.predict(self.input)
                    if alt211 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:26: ( LT )*
                        while True: #loop209
                            alt209 = 2
                            LA209_0 = self.input.LA(1)

                            if (LA209_0 == LT) :
                                alt209 = 1


                            if alt209 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT434 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2573)
                                if self.failed:
                                    return retval


                            else:
                                break #loop209


                        char_literal435 = self.input.LT(1)
                        self.match(self.input, 103, self.FOLLOW_103_in_bitwiseANDExpression2577)
                        if self.failed:
                            return retval

                        char_literal435_tree = self.adaptor.createWithPayload(char_literal435)
                        self.adaptor.addChild(root_0, char_literal435_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:35: ( LT )*
                        while True: #loop210
                            alt210 = 2
                            LA210_0 = self.input.LA(1)

                            if (LA210_0 == LT) :
                                LA210_2 = self.input.LA(2)

                                if (self.synpred253()) :
                                    alt210 = 1




                            if alt210 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT436 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2579)
                                if self.failed:
                                    return retval


                            else:
                                break #loop210


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2583)
                        equalityExpression437 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression437.tree)


                    else:
                        break #loop211





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:425:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
    def bitwiseANDExpressionNoIn(self, ):

        retval = self.bitwiseANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT439 = None
        char_literal440 = None
        LT441 = None
        equalityExpressionNoIn438 = None

        equalityExpressionNoIn442 = None


        LT439_tree = None
        char_literal440_tree = None
        LT441_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2597)
                equalityExpressionNoIn438 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn438.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop214
                    alt214 = 2
                    alt214 = self.dfa214.predict(self.input)
                    if alt214 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:30: ( LT )*
                        while True: #loop212
                            alt212 = 2
                            LA212_0 = self.input.LA(1)

                            if (LA212_0 == LT) :
                                alt212 = 1


                            if alt212 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT439 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2600)
                                if self.failed:
                                    return retval


                            else:
                                break #loop212


                        char_literal440 = self.input.LT(1)
                        self.match(self.input, 103, self.FOLLOW_103_in_bitwiseANDExpressionNoIn2604)
                        if self.failed:
                            return retval

                        char_literal440_tree = self.adaptor.createWithPayload(char_literal440)
                        self.adaptor.addChild(root_0, char_literal440_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:39: ( LT )*
                        while True: #loop213
                            alt213 = 2
                            LA213_0 = self.input.LA(1)

                            if (LA213_0 == LT) :
                                LA213_2 = self.input.LA(2)

                                if (self.synpred256()) :
                                    alt213 = 1




                            if alt213 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT441 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2606)
                                if self.failed:
                                    return retval


                            else:
                                break #loop213


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2610)
                        equalityExpressionNoIn442 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn442.tree)


                    else:
                        break #loop214





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:429:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        LT444 = None
        set445 = None
        LT446 = None
        relationalExpression443 = None

        relationalExpression447 = None


        LT444_tree = None
        set445_tree = None
        LT446_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2624)
                relationalExpression443 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression443.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop217
                    alt217 = 2
                    alt217 = self.dfa217.predict(self.input)
                    if alt217 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:28: ( LT )*
                        while True: #loop215
                            alt215 = 2
                            LA215_0 = self.input.LA(1)

                            if (LA215_0 == LT) :
                                alt215 = 1


                            if alt215 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT444 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2627)
                                if self.failed:
                                    return retval


                            else:
                                break #loop215


                        set445 = self.input.LT(1)
                        if (104 <= self.input.LA(1) <= 107):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set445))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2631
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:63: ( LT )*
                        while True: #loop216
                            alt216 = 2
                            LA216_0 = self.input.LA(1)

                            if (LA216_0 == LT) :
                                LA216_2 = self.input.LA(2)

                                if (self.synpred262()) :
                                    alt216 = 1




                            if alt216 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT446 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2647)
                                if self.failed:
                                    return retval


                            else:
                                break #loop216


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2651)
                        relationalExpression447 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression447.tree)


                    else:
                        break #loop217





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:433:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
    def equalityExpressionNoIn(self, ):

        retval = self.equalityExpressionNoIn_return()
        retval.start = self.input.LT(1)
        equalityExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT449 = None
        set450 = None
        LT451 = None
        relationalExpressionNoIn448 = None

        relationalExpressionNoIn452 = None


        LT449_tree = None
        set450_tree = None
        LT451_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2664)
                relationalExpressionNoIn448 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn448.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop220
                    alt220 = 2
                    alt220 = self.dfa220.predict(self.input)
                    if alt220 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:32: ( LT )*
                        while True: #loop218
                            alt218 = 2
                            LA218_0 = self.input.LA(1)

                            if (LA218_0 == LT) :
                                alt218 = 1


                            if alt218 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT449 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2667)
                                if self.failed:
                                    return retval


                            else:
                                break #loop218


                        set450 = self.input.LT(1)
                        if (104 <= self.input.LA(1) <= 107):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set450))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn2671
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:67: ( LT )*
                        while True: #loop219
                            alt219 = 2
                            LA219_0 = self.input.LA(1)

                            if (LA219_0 == LT) :
                                LA219_2 = self.input.LA(2)

                                if (self.synpred268()) :
                                    alt219 = 1




                            if alt219 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT451 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2687)
                                if self.failed:
                                    return retval


                            else:
                                break #loop219


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2691)
                        relationalExpressionNoIn452 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn452.tree)


                    else:
                        break #loop220





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:437:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LT454 = None
        set455 = None
        LT456 = None
        shiftExpression453 = None

        shiftExpression457 = None


        LT454_tree = None
        set455_tree = None
        LT456_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2705)
                shiftExpression453 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression453.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop223
                    alt223 = 2
                    LA223_0 = self.input.LA(1)

                    if (LA223_0 == LT) :
                        LA223_1 = self.input.LA(2)

                        if (self.synpred277()) :
                            alt223 = 1


                    elif ((47 <= LA223_0 <= 48) or LA223_0 == 72 or (108 <= LA223_0 <= 110)) :
                        alt223 = 1


                    if alt223 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:23: ( LT )*
                        while True: #loop221
                            alt221 = 2
                            LA221_0 = self.input.LA(1)

                            if (LA221_0 == LT) :
                                alt221 = 1


                            if alt221 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT454 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2708)
                                if self.failed:
                                    return retval


                            else:
                                break #loop221


                        set455 = self.input.LT(1)
                        if (47 <= self.input.LA(1) <= 48) or self.input.LA(1) == 72 or (108 <= self.input.LA(1) <= 110):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set455))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpression2712
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:76: ( LT )*
                        while True: #loop222
                            alt222 = 2
                            LA222_0 = self.input.LA(1)

                            if (LA222_0 == LT) :
                                LA222_2 = self.input.LA(2)

                                if (self.synpred276()) :
                                    alt222 = 1




                            if alt222 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT456 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2736)
                                if self.failed:
                                    return retval


                            else:
                                break #loop222


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2740)
                        shiftExpression457 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression457.tree)


                    else:
                        break #loop223





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:441:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
    def relationalExpressionNoIn(self, ):

        retval = self.relationalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        relationalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT459 = None
        set460 = None
        LT461 = None
        shiftExpression458 = None

        shiftExpression462 = None


        LT459_tree = None
        set460_tree = None
        LT461_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2753)
                shiftExpression458 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression458.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop226
                    alt226 = 2
                    alt226 = self.dfa226.predict(self.input)
                    if alt226 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:23: ( LT )*
                        while True: #loop224
                            alt224 = 2
                            LA224_0 = self.input.LA(1)

                            if (LA224_0 == LT) :
                                alt224 = 1


                            if alt224 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT459 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2756)
                                if self.failed:
                                    return retval


                            else:
                                break #loop224


                        set460 = self.input.LT(1)
                        if (47 <= self.input.LA(1) <= 48) or (108 <= self.input.LA(1) <= 110):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set460))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn2760
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:69: ( LT )*
                        while True: #loop225
                            alt225 = 2
                            LA225_0 = self.input.LA(1)

                            if (LA225_0 == LT) :
                                LA225_2 = self.input.LA(2)

                                if (self.synpred283()) :
                                    alt225 = 1




                            if alt225 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT461 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2780)
                                if self.failed:
                                    return retval


                            else:
                                break #loop225


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2784)
                        shiftExpression462 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression462.tree)


                    else:
                        break #loop226





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:445:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        LT464 = None
        set465 = None
        LT466 = None
        additiveExpression463 = None

        additiveExpression467 = None


        LT464_tree = None
        set465_tree = None
        LT466_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2797)
                additiveExpression463 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression463.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop229
                    alt229 = 2
                    alt229 = self.dfa229.predict(self.input)
                    if alt229 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:26: ( LT )*
                        while True: #loop227
                            alt227 = 2
                            LA227_0 = self.input.LA(1)

                            if (LA227_0 == LT) :
                                alt227 = 1


                            if alt227 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT464 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2800)
                                if self.failed:
                                    return retval


                            else:
                                break #loop227


                        set465 = self.input.LT(1)
                        if (111 <= self.input.LA(1) <= 113):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set465))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_shiftExpression2804
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:53: ( LT )*
                        while True: #loop228
                            alt228 = 2
                            LA228_0 = self.input.LA(1)

                            if (LA228_0 == LT) :
                                LA228_2 = self.input.LA(2)

                                if (self.synpred288()) :
                                    alt228 = 1




                            if alt228 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT466 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2816)
                                if self.failed:
                                    return retval


                            else:
                                break #loop228


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2820)
                        additiveExpression467 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression467.tree)


                    else:
                        break #loop229





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:449:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        LT469 = None
        set470 = None
        LT471 = None
        multiplicativeExpression468 = None

        multiplicativeExpression472 = None


        LT469_tree = None
        set470_tree = None
        LT471_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 85):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2833)
                multiplicativeExpression468 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression468.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop232
                    alt232 = 2
                    LA232_0 = self.input.LA(1)

                    if (LA232_0 == LT) :
                        LA232_1 = self.input.LA(2)

                        if (self.synpred293()) :
                            alt232 = 1


                    elif (LA232_0 == 51 or LA232_0 == 114) :
                        alt232 = 1


                    if alt232 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:32: ( LT )*
                        while True: #loop230
                            alt230 = 2
                            LA230_0 = self.input.LA(1)

                            if (LA230_0 == LT) :
                                alt230 = 1


                            if alt230 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT469 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2836)
                                if self.failed:
                                    return retval


                            else:
                                break #loop230


                        set470 = self.input.LT(1)
                        if self.input.LA(1) == 51 or self.input.LA(1) == 114:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set470))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_additiveExpression2840
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:49: ( LT )*
                        while True: #loop231
                            alt231 = 2
                            LA231_0 = self.input.LA(1)

                            if (LA231_0 == LT) :
                                LA231_2 = self.input.LA(2)

                                if (self.synpred292()) :
                                    alt231 = 1




                            if alt231 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT471 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2848)
                                if self.failed:
                                    return retval


                            else:
                                break #loop231


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2852)
                        multiplicativeExpression472 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression472.tree)


                    else:
                        break #loop232





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:453:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        LT474 = None
        set475 = None
        LT476 = None
        unaryExpression473 = None

        unaryExpression477 = None


        LT474_tree = None
        set475_tree = None
        LT476_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 86):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2865)
                unaryExpression473 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression473.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop235
                    alt235 = 2
                    LA235_0 = self.input.LA(1)

                    if (LA235_0 == LT) :
                        LA235_1 = self.input.LA(2)

                        if (self.synpred298()) :
                            alt235 = 1


                    elif (LA235_0 == 49 or LA235_0 == 86 or LA235_0 == 115) :
                        alt235 = 1


                    if alt235 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:23: ( LT )*
                        while True: #loop233
                            alt233 = 2
                            LA233_0 = self.input.LA(1)

                            if (LA233_0 == LT) :
                                alt233 = 1


                            if alt233 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT474 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2868)
                                if self.failed:
                                    return retval


                            else:
                                break #loop233


                        set475 = self.input.LT(1)
                        if self.input.LA(1) == 49 or self.input.LA(1) == 86 or self.input.LA(1) == 115:
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set475))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression2872
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:46: ( LT )*
                        while True: #loop234
                            alt234 = 2
                            LA234_0 = self.input.LA(1)

                            if (LA234_0 == LT) :
                                LA234_2 = self.input.LA(2)

                                if (self.synpred297()) :
                                    alt234 = 1




                            if alt234 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT476 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2884)
                                if self.failed:
                                    return retval


                            else:
                                break #loop234


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2888)
                        unaryExpression477 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression477.tree)


                    else:
                        break #loop235





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:457:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set479 = None
        postfixExpression478 = None

        unaryExpression480 = None


        set479_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 87):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt236 = 2
                LA236_0 = self.input.LA(1)

                if ((LT <= LA236_0 <= RegularExpressionHacks) or LA236_0 == 47 or LA236_0 == 49 or LA236_0 == 53 or (55 <= LA236_0 <= 56) or (59 <= LA236_0 <= 61) or LA236_0 == 71 or LA236_0 == 82 or LA236_0 == 84 or (123 <= LA236_0 <= 128)) :
                    alt236 = 1
                elif (LA236_0 == 51 or LA236_0 == 114 or (116 <= LA236_0 <= 122)) :
                    alt236 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("457:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 236, 0, self.input)

                    raise nvae

                if alt236 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:458:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression2901)
                    postfixExpression478 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression478.tree)


                elif alt236 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:459:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set479 = self.input.LT(1)
                    if self.input.LA(1) == 51 or self.input.LA(1) == 114 or (116 <= self.input.LA(1) <= 122):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set479))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_unaryExpression2906
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression2942)
                    unaryExpression480 = self.unaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unaryExpression480.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:462:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set482 = None
        leftHandSideExpression481 = None


        set482_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 88):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression2954)
                leftHandSideExpression481 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression481.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:463:27: ( '++' | '--' )?
                alt237 = 2
                LA237_0 = self.input.LA(1)

                if ((119 <= LA237_0 <= 120)) :
                    alt237 = 1
                if alt237 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set482 = self.input.LT(1)
                    if (119 <= self.input.LA(1) <= 120):
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
                            self.input, mse, self.FOLLOW_set_in_postfixExpression2956
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:466:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal483 = None
        char_literal489 = None
        LT490 = None
        LT492 = None
        char_literal493 = None
        xmlLiteral484 = None

        identifier485 = None

        literal486 = None

        arrayLiteral487 = None

        objectLiteral488 = None

        expression491 = None


        string_literal483_tree = None
        char_literal489_tree = None
        LT490_tree = None
        LT492_tree = None
        char_literal493_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 89):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:2: ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt240 = 7
                LA240_0 = self.input.LA(1)

                if (LA240_0 == 123) :
                    alt240 = 1
                elif (LA240_0 == LT) and (self.synpred313()):
                    alt240 = 2
                elif (LA240_0 == 47) and (self.synpred313()):
                    alt240 = 2
                elif (LA240_0 == 53) :
                    LA240_4 = self.input.LA(2)

                    if (self.synpred313()) :
                        alt240 = 2
                    elif (self.synpred317()) :
                        alt240 = 6
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("466:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 240, 4, self.input)

                        raise nvae

                elif (LA240_0 == XMLComment) and (self.synpred313()):
                    alt240 = 2
                elif (LA240_0 == Identifier or (59 <= LA240_0 <= 61) or LA240_0 == 71 or (124 <= LA240_0 <= 125)) :
                    alt240 = 3
                elif (LA240_0 == StringLiteral or LA240_0 == NumericLiteral or LA240_0 == RegularExpressionHacks or LA240_0 == 49 or (126 <= LA240_0 <= 128)) :
                    alt240 = 4
                elif (LA240_0 == 84) :
                    alt240 = 5
                elif (LA240_0 == 56) :
                    alt240 = 7
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("466:1: primaryExpression : ( 'this' | ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 240, 0, self.input)

                    raise nvae

                if alt240 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:467:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal483 = self.input.LT(1)
                    self.match(self.input, 123, self.FOLLOW_123_in_primaryExpression2974)
                    if self.failed:
                        return retval

                    string_literal483_tree = self.adaptor.createWithPayload(string_literal483)
                    self.adaptor.addChild(root_0, string_literal483_tree)



                elif alt240 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:468:4: ( ( LT )* ( '<' | XMLComment ) )=> xmlLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_xmlLiteral_in_primaryExpression2991)
                    xmlLiteral484 = self.xmlLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, xmlLiteral484.tree)


                elif alt240 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:469:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_primaryExpression2996)
                    identifier485 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier485.tree)


                elif alt240 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:470:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression3001)
                    literal486 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal486.tree)


                elif alt240 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:471:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression3006)
                    arrayLiteral487 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral487.tree)


                elif alt240 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:472:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression3011)
                    objectLiteral488 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral488.tree)


                elif alt240 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal489 = self.input.LT(1)
                    self.match(self.input, 56, self.FOLLOW_56_in_primaryExpression3016)
                    if self.failed:
                        return retval

                    char_literal489_tree = self.adaptor.createWithPayload(char_literal489)
                    self.adaptor.addChild(root_0, char_literal489_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:10: ( LT )*
                    while True: #loop238
                        alt238 = 2
                        LA238_0 = self.input.LA(1)

                        if (LA238_0 == LT) :
                            LA238_2 = self.input.LA(2)

                            if (self.synpred318()) :
                                alt238 = 1




                        if alt238 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT490 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3018)
                            if self.failed:
                                return retval


                        else:
                            break #loop238


                    self.following.append(self.FOLLOW_expression_in_primaryExpression3022)
                    expression491 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression491.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:26: ( LT )*
                    while True: #loop239
                        alt239 = 2
                        LA239_0 = self.input.LA(1)

                        if (LA239_0 == LT) :
                            alt239 = 1


                        if alt239 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT492 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression3024)
                            if self.failed:
                                return retval


                        else:
                            break #loop239


                    char_literal493 = self.input.LT(1)
                    self.match(self.input, 58, self.FOLLOW_58_in_primaryExpression3028)
                    if self.failed:
                        return retval

                    char_literal493_tree = self.adaptor.createWithPayload(char_literal493)
                    self.adaptor.addChild(root_0, char_literal493_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:477:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal494 = None
        LT495 = None
        LT497 = None
        char_literal498 = None
        LT499 = None
        LT501 = None
        char_literal502 = None
        LT503 = None
        char_literal504 = None
        assignmentExpression496 = None

        assignmentExpression500 = None


        char_literal494_tree = None
        LT495_tree = None
        LT497_tree = None
        char_literal498_tree = None
        LT499_tree = None
        LT501_tree = None
        char_literal502_tree = None
        LT503_tree = None
        char_literal504_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 90):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ( ',' ( LT )* )? ']'
                root_0 = self.adaptor.nil()

                char_literal494 = self.input.LT(1)
                self.match(self.input, 84, self.FOLLOW_84_in_arrayLiteral3041)
                if self.failed:
                    return retval

                char_literal494_tree = self.adaptor.createWithPayload(char_literal494)
                self.adaptor.addChild(root_0, char_literal494_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:10: ( LT )*
                while True: #loop241
                    alt241 = 2
                    LA241_0 = self.input.LA(1)

                    if (LA241_0 == LT) :
                        LA241_2 = self.input.LA(2)

                        if (self.synpred320()) :
                            alt241 = 1




                    if alt241 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT495 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3043)
                        if self.failed:
                            return retval


                    else:
                        break #loop241


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:13: ( assignmentExpression )?
                alt242 = 2
                alt242 = self.dfa242.predict(self.input)
                if alt242 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3047)
                    assignmentExpression496 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression496.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop246
                    alt246 = 2
                    alt246 = self.dfa246.predict(self.input)
                    if alt246 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:36: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:38: ( LT )*
                        while True: #loop243
                            alt243 = 2
                            LA243_0 = self.input.LA(1)

                            if (LA243_0 == LT) :
                                alt243 = 1


                            if alt243 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT497 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3051)
                                if self.failed:
                                    return retval


                            else:
                                break #loop243


                        char_literal498 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_arrayLiteral3055)
                        if self.failed:
                            return retval

                        char_literal498_tree = self.adaptor.createWithPayload(char_literal498)
                        self.adaptor.addChild(root_0, char_literal498_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:45: ( ( LT )* assignmentExpression )?
                        alt245 = 2
                        alt245 = self.dfa245.predict(self.input)
                        if alt245 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:46: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:48: ( LT )*
                            while True: #loop244
                                alt244 = 2
                                LA244_0 = self.input.LA(1)

                                if (LA244_0 == LT) :
                                    LA244_2 = self.input.LA(2)

                                    if (self.synpred323()) :
                                        alt244 = 1




                                if alt244 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT499 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3058)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop244


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral3062)
                            assignmentExpression500 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression500.tree)





                    else:
                        break #loop246


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:78: ( LT )*
                while True: #loop247
                    alt247 = 2
                    LA247_0 = self.input.LA(1)

                    if (LA247_0 == LT) :
                        alt247 = 1


                    if alt247 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT501 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3068)
                        if self.failed:
                            return retval


                    else:
                        break #loop247


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:81: ( ',' ( LT )* )?
                alt249 = 2
                LA249_0 = self.input.LA(1)

                if (LA249_0 == 57) :
                    alt249 = 1
                if alt249 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:82: ',' ( LT )*
                    char_literal502 = self.input.LT(1)
                    self.match(self.input, 57, self.FOLLOW_57_in_arrayLiteral3073)
                    if self.failed:
                        return retval

                    char_literal502_tree = self.adaptor.createWithPayload(char_literal502)
                    self.adaptor.addChild(root_0, char_literal502_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:88: ( LT )*
                    while True: #loop248
                        alt248 = 2
                        LA248_0 = self.input.LA(1)

                        if (LA248_0 == LT) :
                            alt248 = 1


                        if alt248 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT503 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral3075)
                            if self.failed:
                                return retval


                        else:
                            break #loop248





                char_literal504 = self.input.LT(1)
                self.match(self.input, 85, self.FOLLOW_85_in_arrayLiteral3081)
                if self.failed:
                    return retval

                char_literal504_tree = self.adaptor.createWithPayload(char_literal504)
                self.adaptor.addChild(root_0, char_literal504_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:482:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal505 = None
        LT506 = None
        LT508 = None
        char_literal509 = None
        LT510 = None
        LT512 = None
        char_literal513 = None
        LT514 = None
        char_literal515 = None
        propertyNameAndValue507 = None

        propertyNameAndValue511 = None


        char_literal505_tree = None
        LT506_tree = None
        LT508_tree = None
        char_literal509_tree = None
        LT510_tree = None
        LT512_tree = None
        char_literal513_tree = None
        LT514_tree = None
        char_literal515_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_57 = RewriteRuleTokenStream(self.adaptor, "token 57")
        stream_53 = RewriteRuleTokenStream(self.adaptor, "token 53")
        stream_54 = RewriteRuleTokenStream(self.adaptor, "token 54")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 91):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* ( ',' ( LT )* )? '}'
                char_literal505 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_objectLiteral3100)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_53.add(char_literal505)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:8: ( LT )*
                while True: #loop250
                    alt250 = 2
                    LA250_0 = self.input.LA(1)

                    if (LA250_0 == LT) :
                        LA250_2 = self.input.LA(2)

                        if (self.synpred329()) :
                            alt250 = 1




                    if alt250 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT506 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3102)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT506)


                    else:
                        break #loop250


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:12: ( propertyNameAndValue )?
                alt251 = 2
                LA251_0 = self.input.LA(1)

                if (LA251_0 == StringLiteral or (NumericLiteral <= LA251_0 <= Identifier) or (59 <= LA251_0 <= 61) or LA251_0 == 71 or (124 <= LA251_0 <= 125)) :
                    alt251 = 1
                if alt251 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3105)
                    propertyNameAndValue507 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue507.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop254
                    alt254 = 2
                    alt254 = self.dfa254.predict(self.input)
                    if alt254 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:35: ( LT )*
                        while True: #loop252
                            alt252 = 2
                            LA252_0 = self.input.LA(1)

                            if (LA252_0 == LT) :
                                alt252 = 1


                            if alt252 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT508 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3109)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT508)


                            else:
                                break #loop252


                        char_literal509 = self.input.LT(1)
                        self.match(self.input, 57, self.FOLLOW_57_in_objectLiteral3112)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_57.add(char_literal509)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:43: ( LT )*
                        while True: #loop253
                            alt253 = 2
                            LA253_0 = self.input.LA(1)

                            if (LA253_0 == LT) :
                                alt253 = 1


                            if alt253 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT510 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3114)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT510)


                            else:
                                break #loop253


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral3117)
                        propertyNameAndValue511 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue511.tree)


                    else:
                        break #loop254


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:70: ( LT )*
                while True: #loop255
                    alt255 = 2
                    LA255_0 = self.input.LA(1)

                    if (LA255_0 == LT) :
                        alt255 = 1


                    if alt255 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT512 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3121)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT512)


                    else:
                        break #loop255


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:74: ( ',' ( LT )* )?
                alt257 = 2
                LA257_0 = self.input.LA(1)

                if (LA257_0 == 57) :
                    alt257 = 1
                if alt257 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:75: ',' ( LT )*
                    char_literal513 = self.input.LT(1)
                    self.match(self.input, 57, self.FOLLOW_57_in_objectLiteral3125)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_57.add(char_literal513)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:79: ( LT )*
                    while True: #loop256
                        alt256 = 2
                        LA256_0 = self.input.LA(1)

                        if (LA256_0 == LT) :
                            alt256 = 1


                        if alt256 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT514 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral3127)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT514)


                        else:
                            break #loop256





                char_literal515 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_objectLiteral3132)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_54.add(char_literal515)
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
                    # 484:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:484:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:484:12: ( propertyNameAndValue )*
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:487:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        action = None
        LT517 = None
        char_literal518 = None
        LT519 = None
        LT521 = None
        LT522 = None
        LT524 = None
        LT526 = None
        LT528 = None
        LT530 = None
        propname = None

        funcname = None

        propertyName516 = None

        assignmentExpression520 = None

        formalParameterList523 = None

        statementBlock525 = None

        identifier527 = None

        formalParameterList529 = None

        statementBlock531 = None


        action_tree = None
        LT517_tree = None
        char_literal518_tree = None
        LT519_tree = None
        LT521_tree = None
        LT522_tree = None
        LT524_tree = None
        LT526_tree = None
        LT528_tree = None
        LT530_tree = None
        stream_125 = RewriteRuleTokenStream(self.adaptor, "token 125")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_124 = RewriteRuleTokenStream(self.adaptor, "token 124")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_propertyName = RewriteRuleSubtreeStream(self.adaptor, "rule propertyName")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 92):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) )
                alt268 = 3
                alt268 = self.dfa268.predict(self.input)
                if alt268 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue3156)
                    propertyName516 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName516.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:17: ( LT )*
                    while True: #loop258
                        alt258 = 2
                        LA258_0 = self.input.LA(1)

                        if (LA258_0 == LT) :
                            alt258 = 1


                        if alt258 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT517 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3158)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT517)


                        else:
                            break #loop258


                    char_literal518 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_propertyNameAndValue3161)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_50.add(char_literal518)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:25: ( LT )*
                    while True: #loop259
                        alt259 = 2
                        LA259_0 = self.input.LA(1)

                        if (LA259_0 == LT) :
                            LA259_2 = self.input.LA(2)

                            if (self.synpred338()) :
                                alt259 = 1




                        if alt259 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT519 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3163)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT519)


                        else:
                            break #loop259


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue3166)
                    assignmentExpression520 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression520.tree)
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
                        # 489:3: -> ^( PROP propertyName PROP assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:489:6: ^( PROP propertyName PROP assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, self.adaptor.createFromType(PROP, "PROP"))
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt268 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:4: (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:4: (action= 'get' | action= 'set' )
                    alt260 = 2
                    LA260_0 = self.input.LA(1)

                    if (LA260_0 == 124) :
                        alt260 = 1
                    elif (LA260_0 == 125) :
                        alt260 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("490:4: (action= 'get' | action= 'set' )", 260, 0, self.input)

                        raise nvae

                    if alt260 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 124, self.FOLLOW_124_in_propertyNameAndValue3188)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_124.add(action)


                    elif alt260 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 125, self.FOLLOW_125_in_propertyNameAndValue3192)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_125.add(action)



                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3197)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:52: ( LT )*
                    while True: #loop261
                        alt261 = 2
                        LA261_0 = self.input.LA(1)

                        if (LA261_0 == LT) :
                            alt261 = 1


                        if alt261 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT521 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3199)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT521)


                        else:
                            break #loop261


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3204)
                    funcname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(funcname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:76: ( LT )*
                    while True: #loop262
                        alt262 = 2
                        LA262_0 = self.input.LA(1)

                        if (LA262_0 == LT) :
                            alt262 = 1


                        if alt262 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT522 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3206)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT522)


                        else:
                            break #loop262


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3209)
                    formalParameterList523 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList523.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:490:100: ( LT )*
                    while True: #loop263
                        alt263 = 2
                        LA263_0 = self.input.LA(1)

                        if (LA263_0 == LT) :
                            alt263 = 1


                        if alt263 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT524 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3211)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT524)


                        else:
                            break #loop263


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3214)
                    statementBlock525 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock525.tree)
                    # AST Rewrite
                    # elements: formalParameterList, funcname, action, propname, statementBlock
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
                        # 491:3: -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:491:6: ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:491:31: ^( FUNC $funcname formalParameterList statementBlock )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_funcname.next())
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_statementBlock.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                elif alt268 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:4: (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:4: (action= 'get' | action= 'set' )
                    alt264 = 2
                    LA264_0 = self.input.LA(1)

                    if (LA264_0 == 124) :
                        alt264 = 1
                    elif (LA264_0 == 125) :
                        alt264 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("492:4: (action= 'get' | action= 'set' )", 264, 0, self.input)

                        raise nvae

                    if alt264 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 124, self.FOLLOW_124_in_propertyNameAndValue3247)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_124.add(action)


                    elif alt264 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 125, self.FOLLOW_125_in_propertyNameAndValue3251)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_125.add(action)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:32: ( LT )*
                    while True: #loop265
                        alt265 = 2
                        LA265_0 = self.input.LA(1)

                        if (LA265_0 == LT) :
                            alt265 = 1


                        if alt265 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT526 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3254)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT526)


                        else:
                            break #loop265


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue3257)
                    identifier527 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier527.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:47: ( LT )*
                    while True: #loop266
                        alt266 = 2
                        LA266_0 = self.input.LA(1)

                        if (LA266_0 == LT) :
                            alt266 = 1


                        if alt266 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT528 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3259)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT528)


                        else:
                            break #loop266


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue3262)
                    formalParameterList529 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList529.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:492:71: ( LT )*
                    while True: #loop267
                        alt267 = 2
                        LA267_0 = self.input.LA(1)

                        if (LA267_0 == LT) :
                            alt267 = 1


                        if alt267 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT530 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue3264)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT530)


                        else:
                            break #loop267


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue3267)
                    statementBlock531 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock531.tree)
                    # AST Rewrite
                    # elements: statementBlock, identifier, formalParameterList, action
                    # token labels: action
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0
                        stream_action = RewriteRuleTokenStream(self.adaptor, "token action", action)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        root_0 = self.adaptor.nil()
                        # 493:3: -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:493:6: ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:493:32: ^( FUNC ANONYMOUS formalParameterList statementBlock )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:496:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral533 = None
        NumericLiteral534 = None
        identifier532 = None


        StringLiteral533_tree = None
        NumericLiteral534_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 93):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:497:2: ( identifier | StringLiteral | NumericLiteral )
                alt269 = 3
                LA269 = self.input.LA(1)
                if LA269 == Identifier or LA269 == 59 or LA269 == 60 or LA269 == 61 or LA269 == 71 or LA269 == 124 or LA269 == 125:
                    alt269 = 1
                elif LA269 == StringLiteral:
                    alt269 = 2
                elif LA269 == NumericLiteral:
                    alt269 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("496:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 269, 0, self.input)

                    raise nvae

                if alt269 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:497:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName3301)
                    identifier532 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier532.tree)


                elif alt269 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:498:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral533 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName3306)
                    if self.failed:
                        return retval

                    StringLiteral533_tree = self.adaptor.createWithPayload(StringLiteral533)
                    self.adaptor.addChild(root_0, StringLiteral533_tree)



                elif alt269 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:499:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral534 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName3311)
                    if self.failed:
                        return retval

                    NumericLiteral534_tree = self.adaptor.createWithPayload(NumericLiteral534)
                    self.adaptor.addChild(root_0, NumericLiteral534_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:503:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        string_literal535 = None
        string_literal536 = None
        string_literal537 = None
        StringLiteral538 = None
        NumericLiteral539 = None
        regularExpressionLiteral540 = None


        string_literal535_tree = None
        string_literal536_tree = None
        string_literal537_tree = None
        StringLiteral538_tree = None
        NumericLiteral539_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 94):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:504:2: ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral )
                alt270 = 6
                LA270 = self.input.LA(1)
                if LA270 == 126:
                    alt270 = 1
                elif LA270 == 127:
                    alt270 = 2
                elif LA270 == 128:
                    alt270 = 3
                elif LA270 == StringLiteral:
                    alt270 = 4
                elif LA270 == NumericLiteral:
                    alt270 = 5
                elif LA270 == RegularExpressionHacks or LA270 == 49:
                    alt270 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("503:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral );", 270, 0, self.input)

                    raise nvae

                if alt270 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:504:4: 'null'
                    root_0 = self.adaptor.nil()

                    string_literal535 = self.input.LT(1)
                    self.match(self.input, 126, self.FOLLOW_126_in_literal3323)
                    if self.failed:
                        return retval

                    string_literal535_tree = self.adaptor.createWithPayload(string_literal535)
                    self.adaptor.addChild(root_0, string_literal535_tree)



                elif alt270 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:505:4: 'true'
                    root_0 = self.adaptor.nil()

                    string_literal536 = self.input.LT(1)
                    self.match(self.input, 127, self.FOLLOW_127_in_literal3328)
                    if self.failed:
                        return retval

                    string_literal536_tree = self.adaptor.createWithPayload(string_literal536)
                    self.adaptor.addChild(root_0, string_literal536_tree)



                elif alt270 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:506:4: 'false'
                    root_0 = self.adaptor.nil()

                    string_literal537 = self.input.LT(1)
                    self.match(self.input, 128, self.FOLLOW_128_in_literal3333)
                    if self.failed:
                        return retval

                    string_literal537_tree = self.adaptor.createWithPayload(string_literal537)
                    self.adaptor.addChild(root_0, string_literal537_tree)



                elif alt270 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:507:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral538 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_literal3338)
                    if self.failed:
                        return retval

                    StringLiteral538_tree = self.adaptor.createWithPayload(StringLiteral538)
                    self.adaptor.addChild(root_0, StringLiteral538_tree)



                elif alt270 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:508:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral539 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_literal3343)
                    if self.failed:
                        return retval

                    NumericLiteral539_tree = self.adaptor.createWithPayload(NumericLiteral539)
                    self.adaptor.addChild(root_0, NumericLiteral539_tree)



                elif alt270 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:509:4: regularExpressionLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_regularExpressionLiteral_in_literal3348)
                    regularExpressionLiteral540 = self.regularExpressionLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, regularExpressionLiteral540.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:519:1: reFirstChar : ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier );
    def reFirstChar(self, ):

        retval = self.reFirstChar_return()
        retval.start = self.input.LT(1)
        reFirstChar_StartIndex = self.input.index()
        root_0 = None

        set541 = None

        set541_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 95):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:520:2: ( ';' | ',' | '.' | ':' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'instanceof' | 'namespace' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | 'xml' | StringLiteral | NumericLiteral | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set541 = self.input.LT(1)
                if self.input.LA(1) == StringLiteral or (NumericLiteral <= self.input.LA(1) <= Identifier) or (47 <= self.input.LA(1) <= 48) or (50 <= self.input.LA(1) <= 85) or (87 <= self.input.LA(1) <= 103) or (108 <= self.input.LA(1) <= 129):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set541))
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:538:1: reChars : ( reFirstChar | '*' );
    def reChars(self, ):

        retval = self.reChars_return()
        retval.start = self.input.LT(1)
        reChars_StartIndex = self.input.index()
        root_0 = None

        char_literal543 = None
        reFirstChar542 = None


        char_literal543_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 96):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:539:2: ( reFirstChar | '*' )
                alt271 = 2
                LA271_0 = self.input.LA(1)

                if (LA271_0 == StringLiteral or (NumericLiteral <= LA271_0 <= Identifier) or (47 <= LA271_0 <= 48) or (50 <= LA271_0 <= 85) or (87 <= LA271_0 <= 103) or (108 <= LA271_0 <= 129)) :
                    alt271 = 1
                elif (LA271_0 == 86) :
                    alt271 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("538:1: reChars : ( reFirstChar | '*' );", 271, 0, self.input)

                    raise nvae

                if alt271 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:539:4: reFirstChar
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_reFirstChar_in_reChars3738)
                    reFirstChar542 = self.reFirstChar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, reFirstChar542.tree)


                elif alt271 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:540:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal543 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_reChars3743)
                    if self.failed:
                        return retval

                    char_literal543_tree = self.adaptor.createWithPayload(char_literal543)
                    self.adaptor.addChild(root_0, char_literal543_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:543:1: regularExpressionLiteral : ( '/' reFirstChar ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal544 = None
        char_literal547 = None
        Identifier548 = None
        RegularExpressionHacks549 = None
        Identifier550 = None
        reFirstChar545 = None

        reChars546 = None


        char_literal544_tree = None
        char_literal547_tree = None
        Identifier548_tree = None
        RegularExpressionHacks549_tree = None
        Identifier550_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 97):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:544:2: ( '/' reFirstChar ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? )
                alt275 = 2
                LA275_0 = self.input.LA(1)

                if (LA275_0 == 49) :
                    alt275 = 1
                elif (LA275_0 == RegularExpressionHacks) :
                    alt275 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("543:1: regularExpressionLiteral : ( '/' reFirstChar ( reChars )* '/' ( Identifier )? | RegularExpressionHacks ( Identifier )? );", 275, 0, self.input)

                    raise nvae

                if alt275 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:544:4: '/' reFirstChar ( reChars )* '/' ( Identifier )?
                    root_0 = self.adaptor.nil()

                    char_literal544 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_regularExpressionLiteral3754)
                    if self.failed:
                        return retval

                    char_literal544_tree = self.adaptor.createWithPayload(char_literal544)
                    self.adaptor.addChild(root_0, char_literal544_tree)

                    self.following.append(self.FOLLOW_reFirstChar_in_regularExpressionLiteral3756)
                    reFirstChar545 = self.reFirstChar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, reFirstChar545.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:544:20: ( reChars )*
                    while True: #loop272
                        alt272 = 2
                        LA272_0 = self.input.LA(1)

                        if (LA272_0 == StringLiteral or (NumericLiteral <= LA272_0 <= Identifier) or (47 <= LA272_0 <= 48) or (50 <= LA272_0 <= 103) or (108 <= LA272_0 <= 129)) :
                            alt272 = 1


                        if alt272 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reChars
                            self.following.append(self.FOLLOW_reChars_in_regularExpressionLiteral3758)
                            reChars546 = self.reChars()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, reChars546.tree)


                        else:
                            break #loop272


                    char_literal547 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_regularExpressionLiteral3761)
                    if self.failed:
                        return retval

                    char_literal547_tree = self.adaptor.createWithPayload(char_literal547)
                    self.adaptor.addChild(root_0, char_literal547_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:544:33: ( Identifier )?
                    alt273 = 2
                    LA273_0 = self.input.LA(1)

                    if (LA273_0 == Identifier) :
                        alt273 = 1
                    if alt273 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier548 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral3763)
                        if self.failed:
                            return retval

                        Identifier548_tree = self.adaptor.createWithPayload(Identifier548)
                        self.adaptor.addChild(root_0, Identifier548_tree)






                elif alt275 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:545:4: RegularExpressionHacks ( Identifier )?
                    root_0 = self.adaptor.nil()

                    RegularExpressionHacks549 = self.input.LT(1)
                    self.match(self.input, RegularExpressionHacks, self.FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral3769)
                    if self.failed:
                        return retval

                    RegularExpressionHacks549_tree = self.adaptor.createWithPayload(RegularExpressionHacks549)
                    self.adaptor.addChild(root_0, RegularExpressionHacks549_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:545:27: ( Identifier )?
                    alt274 = 2
                    LA274_0 = self.input.LA(1)

                    if (LA274_0 == Identifier) :
                        alt274 = 1
                    if alt274 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                        Identifier550 = self.input.LT(1)
                        self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral3771)
                        if self.failed:
                            return retval

                        Identifier550_tree = self.adaptor.createWithPayload(Identifier550)
                        self.adaptor.addChild(root_0, Identifier550_tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:550:1: identifier : ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set551 = None

        set551_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 98):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:551:2: ( 'get' | 'set' | 'each' | 'default' | 'xml' | 'namespace' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set551 = self.input.LT(1)
                if self.input.LA(1) == Identifier or (59 <= self.input.LA(1) <= 61) or self.input.LA(1) == 71 or (124 <= self.input.LA(1) <= 125):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set551))
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
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred196)
        if self.failed:
            return 


    # $ANTLR end synpred1



    # $ANTLR start synpred3
    def synpred3_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:19: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:19: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3122)
        if self.failed:
            return 


    # $ANTLR end synpred3



    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:41:4: ( functionDeclaration )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:41:5: functionDeclaration
        self.following.append(self.FOLLOW_functionDeclaration_in_synpred5141)
        self.functionDeclaration()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred16
    def synpred16_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:4: ( '{' )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:5: '{'
        self.match(self.input, 53, self.FOLLOW_53_in_synpred16348)
        if self.failed:
            return 


    # $ANTLR end synpred16



    # $ANTLR start synpred18
    def synpred18_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:4: ( xmlEmptyTag )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:4: xmlEmptyTag
        self.following.append(self.FOLLOW_xmlEmptyTag_in_synpred18398)
        self.xmlEmptyTag()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred18



    # $ANTLR start synpred19
    def synpred19_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:4: ( xmlStartTag )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:4: xmlStartTag
        self.following.append(self.FOLLOW_xmlStartTag_in_synpred19403)
        self.xmlStartTag()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred19



    # $ANTLR start synpred22
    def synpred22_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:5: ( ( LT )* xmlPayload )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:5: ( LT )* xmlPayload
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:5: ( LT )*
        while True: #loop279
            alt279 = 2
            LA279_0 = self.input.LA(1)

            if (LA279_0 == LT) :
                alt279 = 1


            if alt279 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred22426)
                if self.failed:
                    return 


            else:
                break #loop279


        self.following.append(self.FOLLOW_xmlPayload_in_synpred22429)
        self.xmlPayload()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred22



    # $ANTLR start synpred38
    def synpred38_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred38597)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred38



    # $ANTLR start synpred41
    def synpred41_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred41612)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred41



    # $ANTLR start synpred48
    def synpred48_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred48647)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred48



    # $ANTLR start synpred55
    def synpred55_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred55723)
        if self.failed:
            return 


    # $ANTLR end synpred55



    # $ANTLR start synpred58
    def synpred58_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: '{' ( LT )* ( statementList )? ( LT )* '}'
        self.match(self.input, 53, self.FOLLOW_53_in_synpred58721)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:10: ( LT )*
        while True: #loop289
            alt289 = 2
            LA289_0 = self.input.LA(1)

            if (LA289_0 == LT) :
                LA289_2 = self.input.LA(2)

                if (self.synpred55()) :
                    alt289 = 1




            if alt289 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred58723)
                if self.failed:
                    return 


            else:
                break #loop289


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:13: ( statementList )?
        alt290 = 2
        alt290 = self.dfa290.predict(self.input)
        if alt290 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
            self.following.append(self.FOLLOW_statementList_in_synpred58727)
            self.statementList()
            self.following.pop()
            if self.failed:
                return 



        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:30: ( LT )*
        while True: #loop291
            alt291 = 2
            LA291_0 = self.input.LA(1)

            if (LA291_0 == LT) :
                alt291 = 1


            if alt291 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred58730)
                if self.failed:
                    return 


            else:
                break #loop291


        self.match(self.input, 54, self.FOLLOW_54_in_synpred58734)
        if self.failed:
            return 


    # $ANTLR end synpred58



    # $ANTLR start synpred60
    def synpred60_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:15: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:15: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred60762)
        if self.failed:
            return 


    # $ANTLR end synpred60



    # $ANTLR start synpred61
    def synpred61_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:15: ( ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:15: ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:156:17: ( LT )*
        while True: #loop292
            alt292 = 2
            LA292_0 = self.input.LA(1)

            if (LA292_0 == LT) :
                LA292_2 = self.input.LA(2)

                if (self.synpred60()) :
                    alt292 = 1




            if alt292 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred61762)
                if self.failed:
                    return 


            else:
                break #loop292


        self.following.append(self.FOLLOW_statement_in_synpred61766)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred61



    # $ANTLR start synpred75
    def synpred75_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred75946)
        if self.failed:
            return 


    # $ANTLR end synpred75



    # $ANTLR start synpred76
    def synpred76_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred76969)
        if self.failed:
            return 


    # $ANTLR end synpred76



    # $ANTLR start synpred79
    def synpred79_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:18: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:18: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred791031)
        if self.failed:
            return 


    # $ANTLR end synpred79



    # $ANTLR start synpred81
    def synpred81_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:43: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:43: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred811043)
        if self.failed:
            return 


    # $ANTLR end synpred81



    # $ANTLR start synpred83
    def synpred83_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:71: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:71: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred831056)
        if self.failed:
            return 


    # $ANTLR end synpred83



    # $ANTLR start synpred84
    def synpred84_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:61: ( LT )*
        while True: #loop299
            alt299 = 2
            LA299_0 = self.input.LA(1)

            if (LA299_0 == LT) :
                alt299 = 1


            if alt299 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred841050)
                if self.failed:
                    return 


            else:
                break #loop299


        self.match(self.input, 67, self.FOLLOW_67_in_synpred841054)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:73: ( LT )*
        while True: #loop300
            alt300 = 2
            LA300_0 = self.input.LA(1)

            if (LA300_0 == LT) :
                LA300_2 = self.input.LA(2)

                if (self.synpred83()) :
                    alt300 = 1




            if alt300 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred841056)
                if self.failed:
                    return 


            else:
                break #loop300


        self.following.append(self.FOLLOW_statement_in_synpred841060)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred84



    # $ANTLR start synpred87
    def synpred87_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred871084)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred87



    # $ANTLR start synpred88
    def synpred88_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred881103)
        if self.failed:
            return 


    # $ANTLR end synpred88



    # $ANTLR start synpred93
    def synpred93_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred931152)
        if self.failed:
            return 


    # $ANTLR end synpred93



    # $ANTLR start synpred95
    def synpred95_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:46: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:46: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred951164)
        if self.failed:
            return 


    # $ANTLR end synpred95



    # $ANTLR start synpred97
    def synpred97_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred971189)
        if self.failed:
            return 


    # $ANTLR end synpred97



    # $ANTLR start synpred100
    def synpred100_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1001204)
        if self.failed:
            return 


    # $ANTLR end synpred100



    # $ANTLR start synpred103
    def synpred103_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:93: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:93: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1031219)
        if self.failed:
            return 


    # $ANTLR end synpred103



    # $ANTLR start synpred106
    def synpred106_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:120: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:120: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1061233)
        if self.failed:
            return 


    # $ANTLR end synpred106



    # $ANTLR start synpred109
    def synpred109_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1091274)
        if self.failed:
            return 


    # $ANTLR end synpred109



    # $ANTLR start synpred112
    def synpred112_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:32: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:32: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1121287)
        if self.failed:
            return 


    # $ANTLR end synpred112



    # $ANTLR start synpred114
    def synpred114_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1141299)
        if self.failed:
            return 


    # $ANTLR end synpred114



    # $ANTLR start synpred116
    def synpred116_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:102: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:102: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1161311)
        if self.failed:
            return 


    # $ANTLR end synpred116



    # $ANTLR start synpred123
    def synpred123_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:13: ( expression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:246:13: expression
        self.following.append(self.FOLLOW_expression_in_synpred1231397)
        self.expression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred123



    # $ANTLR start synpred126
    def synpred126_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:20: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:20: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1261427)
        if self.failed:
            return 


    # $ANTLR end synpred126



    # $ANTLR start synpred128
    def synpred128_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:45: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:45: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1281439)
        if self.failed:
            return 


    # $ANTLR end synpred128



    # $ANTLR start synpred130
    def synpred130_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:24: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:24: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1301462)
        if self.failed:
            return 


    # $ANTLR end synpred130



    # $ANTLR start synpred132
    def synpred132_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:22: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:22: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1321486)
        if self.failed:
            return 


    # $ANTLR end synpred132



    # $ANTLR start synpred142
    def synpred142_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:11: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:11: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1421560)
        if self.failed:
            return 


    # $ANTLR end synpred142



    # $ANTLR start synpred144
    def synpred144_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1441572)
        if self.failed:
            return 


    # $ANTLR end synpred144



    # $ANTLR start synpred145
    def synpred145_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:41: ( statementList )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:41: statementList
        self.following.append(self.FOLLOW_statementList_in_synpred1451576)
        self.statementList()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred145



    # $ANTLR start synpred147
    def synpred147_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1471597)
        if self.failed:
            return 


    # $ANTLR end synpred147



    # $ANTLR start synpred161
    def synpred161_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1611744)
        if self.failed:
            return 


    # $ANTLR end synpred161



    # $ANTLR start synpred164
    def synpred164_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1641771)
        if self.failed:
            return 


    # $ANTLR end synpred164



    # $ANTLR start synpred167
    def synpred167_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:51: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:51: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1671797)
        if self.failed:
            return 


    # $ANTLR end synpred167



    # $ANTLR start synpred168
    def synpred168_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred1681789)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:29: ( LT )*
        while True: #loop314
            alt314 = 2
            LA314_0 = self.input.LA(1)

            if (LA314_0 == LT) :
                alt314 = 1


            if alt314 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1681791)
                if self.failed:
                    return 


            else:
                break #loop314


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred1681795)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:53: ( LT )*
        while True: #loop315
            alt315 = 2
            LA315_0 = self.input.LA(1)

            if (LA315_0 == LT) :
                LA315_2 = self.input.LA(2)

                if (self.synpred167()) :
                    alt315 = 1




            if alt315 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1681797)
                if self.failed:
                    return 


            else:
                break #loop315


        self.following.append(self.FOLLOW_assignmentExpression_in_synpred1681801)
        self.assignmentExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred168



    # $ANTLR start synpred170
    def synpred170_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:51: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:51: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1701826)
        if self.failed:
            return 


    # $ANTLR end synpred170



    # $ANTLR start synpred171
    def synpred171_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:4: ( leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
        self.following.append(self.FOLLOW_leftHandSideExpression_in_synpred1711818)
        self.leftHandSideExpression()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:29: ( LT )*
        while True: #loop316
            alt316 = 2
            LA316_0 = self.input.LA(1)

            if (LA316_0 == LT) :
                alt316 = 1


            if alt316 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1711820)
                if self.failed:
                    return 


            else:
                break #loop316


        self.following.append(self.FOLLOW_assignmentOperator_in_synpred1711824)
        self.assignmentOperator()
        self.following.pop()
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:304:53: ( LT )*
        while True: #loop317
            alt317 = 2
            LA317_0 = self.input.LA(1)

            if (LA317_0 == LT) :
                LA317_2 = self.input.LA(2)

                if (self.synpred170()) :
                    alt317 = 1




            if alt317 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1711826)
                if self.failed:
                    return 


            else:
                break #loop317


        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_synpred1711830)
        self.assignmentExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred171



    # $ANTLR start synpred172
    def synpred172_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred1721847)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred172



    # $ANTLR start synpred173
    def synpred173_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred1731864)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred173



    # $ANTLR start synpred174
    def synpred174_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1741871)
        if self.failed:
            return 


    # $ANTLR end synpred174



    # $ANTLR start synpred177
    def synpred177_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:52: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:52: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1771898)
        if self.failed:
            return 


    # $ANTLR end synpred177



    # $ANTLR start synpred180
    def synpred180_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:91: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:91: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:93: ( LT )*
        while True: #loop318
            alt318 = 2
            LA318_0 = self.input.LA(1)

            if (LA318_0 == LT) :
                alt318 = 1


            if alt318 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1801912)
                if self.failed:
                    return 


            else:
                break #loop318


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1801916)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred180



    # $ANTLR start synpred184
    def synpred184_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:21: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:21: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1841963)
        if self.failed:
            return 


    # $ANTLR end synpred184



    # $ANTLR start synpred188
    def synpred188_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:45: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:45: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:45: ( LT )*
        while True: #loop319
            alt319 = 2
            LA319_0 = self.input.LA(1)

            if (LA319_0 == LT) :
                alt319 = 1


            if alt319 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1881975)
                if self.failed:
                    return 


            else:
                break #loop319


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred1881978)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred188



    # $ANTLR start synpred193
    def synpred193_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:9: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:9: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1932046)
        if self.failed:
            return 


    # $ANTLR end synpred193



    # $ANTLR start synpred194
    def synpred194_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1942052)
        if self.failed:
            return 


    # $ANTLR end synpred194



    # $ANTLR start synpred195
    def synpred195_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:45: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:45: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1952059)
        if self.failed:
            return 


    # $ANTLR end synpred195



    # $ANTLR start synpred196
    def synpred196_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:71: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:71: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1962065)
        if self.failed:
            return 


    # $ANTLR end synpred196



    # $ANTLR start synpred200
    def synpred200_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:353:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2002091)
        if self.failed:
            return 


    # $ANTLR end synpred200



    # $ANTLR start synpred204
    def synpred204_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:12: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:12: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2042180)
        if self.failed:
            return 


    # $ANTLR end synpred204



    # $ANTLR start synpred205
    def synpred205_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:16: ( e4xIdentifier )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:16: e4xIdentifier
        self.following.append(self.FOLLOW_e4xIdentifier_in_synpred2052183)
        self.e4xIdentifier()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred205



    # $ANTLR start synpred219
    def synpred219_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:34: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:34: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2192287)
        if self.failed:
            return 


    # $ANTLR end synpred219



    # $ANTLR start synpred221
    def synpred221_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:69: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:69: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2212299)
        if self.failed:
            return 


    # $ANTLR end synpred221



    # $ANTLR start synpred224
    def synpred224_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:38: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:38: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2242325)
        if self.failed:
            return 


    # $ANTLR end synpred224



    # $ANTLR start synpred226
    def synpred226_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:77: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:386:77: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2262337)
        if self.failed:
            return 


    # $ANTLR end synpred226



    # $ANTLR start synpred229
    def synpred229_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2292363)
        if self.failed:
            return 


    # $ANTLR end synpred229



    # $ANTLR start synpred232
    def synpred232_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:40: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:40: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2322390)
        if self.failed:
            return 


    # $ANTLR end synpred232



    # $ANTLR start synpred235
    def synpred235_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2352417)
        if self.failed:
            return 


    # $ANTLR end synpred235



    # $ANTLR start synpred238
    def synpred238_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:402:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2382444)
        if self.failed:
            return 


    # $ANTLR end synpred238



    # $ANTLR start synpred241
    def synpred241_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2412471)
        if self.failed:
            return 


    # $ANTLR end synpred241



    # $ANTLR start synpred244
    def synpred244_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2442498)
        if self.failed:
            return 


    # $ANTLR end synpred244



    # $ANTLR start synpred247
    def synpred247_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:35: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:414:35: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2472525)
        if self.failed:
            return 


    # $ANTLR end synpred247



    # $ANTLR start synpred250
    def synpred250_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:39: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:418:39: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2502552)
        if self.failed:
            return 


    # $ANTLR end synpred250



    # $ANTLR start synpred253
    def synpred253_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:33: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:422:33: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2532579)
        if self.failed:
            return 


    # $ANTLR end synpred253



    # $ANTLR start synpred256
    def synpred256_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:37: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:426:37: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2562606)
        if self.failed:
            return 


    # $ANTLR end synpred256



    # $ANTLR start synpred262
    def synpred262_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:61: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:430:61: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2622647)
        if self.failed:
            return 


    # $ANTLR end synpred262



    # $ANTLR start synpred268
    def synpred268_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:65: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:434:65: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2682687)
        if self.failed:
            return 


    # $ANTLR end synpred268



    # $ANTLR start synpred276
    def synpred276_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:74: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:74: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2762736)
        if self.failed:
            return 


    # $ANTLR end synpred276



    # $ANTLR start synpred277
    def synpred277_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:21: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:23: ( LT )*
        while True: #loop359
            alt359 = 2
            LA359_0 = self.input.LA(1)

            if (LA359_0 == LT) :
                alt359 = 1


            if alt359 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2772708)
                if self.failed:
                    return 


            else:
                break #loop359


        if (47 <= self.input.LA(1) <= 48) or self.input.LA(1) == 72 or (108 <= self.input.LA(1) <= 110):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2772712
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:76: ( LT )*
        while True: #loop360
            alt360 = 2
            LA360_0 = self.input.LA(1)

            if (LA360_0 == LT) :
                LA360_2 = self.input.LA(2)

                if (self.synpred276()) :
                    alt360 = 1




            if alt360 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2772736)
                if self.failed:
                    return 


            else:
                break #loop360


        self.following.append(self.FOLLOW_shiftExpression_in_synpred2772740)
        self.shiftExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred277



    # $ANTLR start synpred283
    def synpred283_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:67: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:442:67: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2832780)
        if self.failed:
            return 


    # $ANTLR end synpred283



    # $ANTLR start synpred288
    def synpred288_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:51: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:446:51: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2882816)
        if self.failed:
            return 


    # $ANTLR end synpred288



    # $ANTLR start synpred292
    def synpred292_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:47: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:47: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2922848)
        if self.failed:
            return 


    # $ANTLR end synpred292



    # $ANTLR start synpred293
    def synpred293_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:32: ( LT )*
        while True: #loop365
            alt365 = 2
            LA365_0 = self.input.LA(1)

            if (LA365_0 == LT) :
                alt365 = 1


            if alt365 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2932836)
                if self.failed:
                    return 


            else:
                break #loop365


        if self.input.LA(1) == 51 or self.input.LA(1) == 114:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2932840
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:49: ( LT )*
        while True: #loop366
            alt366 = 2
            LA366_0 = self.input.LA(1)

            if (LA366_0 == LT) :
                LA366_2 = self.input.LA(2)

                if (self.synpred292()) :
                    alt366 = 1




            if alt366 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2932848)
                if self.failed:
                    return 


            else:
                break #loop366


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred2932852)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred293



    # $ANTLR start synpred297
    def synpred297_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:44: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:44: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2972884)
        if self.failed:
            return 


    # $ANTLR end synpred297



    # $ANTLR start synpred298
    def synpred298_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:21: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:23: ( LT )*
        while True: #loop367
            alt367 = 2
            LA367_0 = self.input.LA(1)

            if (LA367_0 == LT) :
                alt367 = 1


            if alt367 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2982868)
                if self.failed:
                    return 


            else:
                break #loop367


        if self.input.LA(1) == 49 or self.input.LA(1) == 86 or self.input.LA(1) == 115:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2982872
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:454:46: ( LT )*
        while True: #loop368
            alt368 = 2
            LA368_0 = self.input.LA(1)

            if (LA368_0 == LT) :
                LA368_2 = self.input.LA(2)

                if (self.synpred297()) :
                    alt368 = 1




            if alt368 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2982884)
                if self.failed:
                    return 


            else:
                break #loop368


        self.following.append(self.FOLLOW_unaryExpression_in_synpred2982888)
        self.unaryExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred298



    # $ANTLR start synpred313
    def synpred313_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:468:4: ( ( LT )* ( '<' | XMLComment ) )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:468:5: ( LT )* ( '<' | XMLComment )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:468:5: ( LT )*
        while True: #loop369
            alt369 = 2
            LA369_0 = self.input.LA(1)

            if (LA369_0 == LT) :
                alt369 = 1


            if alt369 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3132980)
                if self.failed:
                    return 


            else:
                break #loop369


        if self.input.LA(1) == XMLComment or self.input.LA(1) == 47:
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred3132983
                )
            raise mse




    # $ANTLR end synpred313



    # $ANTLR start synpred317
    def synpred317_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:472:4: ( objectLiteral )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:472:4: objectLiteral
        self.following.append(self.FOLLOW_objectLiteral_in_synpred3173011)
        self.objectLiteral()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred317



    # $ANTLR start synpred318
    def synpred318_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:473:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3183018)
        if self.failed:
            return 


    # $ANTLR end synpred318



    # $ANTLR start synpred320
    def synpred320_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3203043)
        if self.failed:
            return 


    # $ANTLR end synpred320



    # $ANTLR start synpred323
    def synpred323_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:46: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:46: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3233058)
        if self.failed:
            return 


    # $ANTLR end synpred323



    # $ANTLR start synpred325
    def synpred325_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:36: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:36: ( LT )* ',' ( ( LT )* assignmentExpression )?
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:38: ( LT )*
        while True: #loop371
            alt371 = 2
            LA371_0 = self.input.LA(1)

            if (LA371_0 == LT) :
                alt371 = 1


            if alt371 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred3253051)
                if self.failed:
                    return 


            else:
                break #loop371


        self.match(self.input, 57, self.FOLLOW_57_in_synpred3253055)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:45: ( ( LT )* assignmentExpression )?
        alt373 = 2
        LA373_0 = self.input.LA(1)

        if ((LT <= LA373_0 <= RegularExpressionHacks) or LA373_0 == 47 or LA373_0 == 49 or LA373_0 == 51 or LA373_0 == 53 or (55 <= LA373_0 <= 56) or (59 <= LA373_0 <= 61) or LA373_0 == 71 or LA373_0 == 82 or LA373_0 == 84 or LA373_0 == 114 or (116 <= LA373_0 <= 128)) :
            alt373 = 1
        if alt373 == 1:
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:46: ( LT )* assignmentExpression
            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:478:48: ( LT )*
            while True: #loop372
                alt372 = 2
                LA372_0 = self.input.LA(1)

                if (LA372_0 == LT) :
                    LA372_2 = self.input.LA(2)

                    if (self.synpred323()) :
                        alt372 = 1




                if alt372 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                    self.match(self.input, LT, self.FOLLOW_LT_in_synpred3253058)
                    if self.failed:
                        return 


                else:
                    break #loop372


            self.following.append(self.FOLLOW_assignmentExpression_in_synpred3253062)
            self.assignmentExpression()
            self.following.pop()
            if self.failed:
                return 





    # $ANTLR end synpred325



    # $ANTLR start synpred329
    def synpred329_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:483:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3293102)
        if self.failed:
            return 


    # $ANTLR end synpred329



    # $ANTLR start synpred338
    def synpred338_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:25: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:488:25: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred3383163)
        if self.failed:
            return 


    # $ANTLR end synpred338



    def synpred298(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred298_fragment()
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

    def synpred81(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred81_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred128(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred128_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred83(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred83_fragment()
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

    def synpred123(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred123_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred318(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred318_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred317(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred317_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred87(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred87_fragment()
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

    def synpred292(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred292_fragment()
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

    def synpred293(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred293_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred297(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred297_fragment()
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

    def synpred164(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred164_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred253(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred253_fragment()
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

    def synpred250(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred250_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred256(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred256_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred313(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred313_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred168(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred168_fragment()
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

    def synpred116(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred116_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred329(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred329_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred75(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred75_fragment()
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

    def synpred112(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred112_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred229(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred229_fragment()
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

    def synpred76(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred76_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred221(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred221_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred224(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred224_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred262(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred262_fragment()
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

    def synpred196(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred196_fragment()
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

    def synpred320(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred320_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred193(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred193_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred323(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred323_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred194(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred194_fragment()
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

    def synpred276(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred276_fragment()
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

    def synpred61(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred61_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred100(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred100_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred103(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred103_fragment()
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

    def synpred142(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred142_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred106(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred106_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred109(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred109_fragment()
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

    def synpred184(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred184_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred238(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred238_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred188(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred188_fragment()
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

    def synpred338(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred338_fragment()
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

    def synpred22(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred22_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred97(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred97_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred95(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred95_fragment()
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

    def synpred93(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred93_fragment()
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

    def synpred288(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred288_fragment()
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

    def synpred1(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred1_fragment()
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

    def synpred3(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred3_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred130(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred130_fragment()
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

    def synpred204(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred204_fragment()
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

    def synpred172(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred172_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred241(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred241_fragment()
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

    def synpred247(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred247_fragment()
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

    def synpred244(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred244_fragment()
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
        u"\2\20\2\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA4_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\1\3\1\uffff\2\3\2\uffff\10\3\1\uffff\4\3\1\uffff\4\3\1\uffff\2"
        u"\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\1\3\1\uffff\2\3\2\uffff\10\3\1\uffff\4\3\1\uffff\4\3\1\uffff\2"
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
        u"\2\20\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\2\175\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA7_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\11\uffff"
        u"\1\3\64\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\33\uffff\1\2\12\uffff\3\3\11\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\2\175\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA10_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\11\uffff"
        u"\1\3\64\uffff\2\3"),
        DFA.unpack(u"\1\1\3\uffff\1\3\34\uffff\1\2\11\uffff\3\3\11\uffff"
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
        u"\1\22\1\24\3\uffff\1\20\1\24\1\20\1\62\2\uffff\1\20\1\24\1\21\1"
        u"\62\1\0\1\20"
        )

    DFA15_max = DFA.unpack(
        u"\1\65\1\175\3\uffff\3\175\1\64\2\uffff\2\175\1\65\1\64\1\0\1\175"
        )

    DFA15_accept = DFA.unpack(
        u"\2\uffff\1\4\1\5\1\1\4\uffff\1\2\1\3\6\uffff"
        )

    DFA15_special = DFA.unpack(
        u"\17\uffff\1\0\1\uffff"
        )

            
    DFA15_transition = [
        DFA.unpack(u"\1\3\34\uffff\1\1\5\uffff\1\2"),
        DFA.unpack(u"\1\5\34\uffff\1\4\11\uffff\3\5\11\uffff\1\5\64\uffff"
        u"\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\12\1\11\2\6\7\uffff\3\10"
        u"\11\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\13\46\uffff\3\13\11\uffff\1\13\64\uffff\2\13"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\12\1\11\11\uffff\3\10\11"
        u"\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\12\1\11\2\6\7\uffff\3\10"
        u"\11\uffff\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\16\46\uffff\3\16\11\uffff\1\16\64\uffff\2\16"),
        DFA.unpack(u"\1\20\43\uffff\1\17"),
        DFA.unpack(u"\2\14\1\15"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\7\3\uffff\1\10\33\uffff\1\12\1\11\11\uffff\3\10\11"
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
                    s = 9

                elif (self.synpred19()):
                    s = 10

                 
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
        u"\1\67\2\20\2\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\67\2\175\2\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2"
        )

    DFA26_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\3\uffff\1\3\43\uffff\1\4\2\uffff\3\3\11\uffff\1"
        u"\3\64\uffff\2\3"),
        DFA.unpack(u"\1\2\3\uffff\1\3\43\uffff\1\4\2\uffff\3\3\11\uffff\1"
        u"\3\64\uffff\2\3"),
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
        u"\2\20\2\uffff"
        )

    DFA31_max = DFA.unpack(
        u"\2\175\2\uffff"
        )

    DFA31_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA31_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\11\uffff\1\2\64\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\45\uffff\1\3\3\2\11\uffff\1\2\64\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\2\72\2\uffff"
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
        u"\1\20\1\uffff\1\20\1\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\1\u0080\1\uffff\1\66\1\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA38_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\10\1\1\uffff\4\1\1\uffff\4\1\1\uffff\2\1\2"
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
        u"\2\20\2\uffff\1\20"
        )

    DFA49_max = DFA.unpack(
        u"\1\76\1\u0080\2\uffff\1\u0080"
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
        u"\4\2\1\3\1\uffff\15\2\1\uffff\7\2\2\uffff\1\2\1\uffff\1\2\35\uffff"
        u"\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\4\2\1\3\1\uffff\15\2\1\uffff\7\2\2\uffff\1\2\1\uffff\1\2\35\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA52_max = DFA.unpack(
        u"\2\76\2\uffff"
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
        u"\2\20\2\uffff\1\20"
        )

    DFA54_max = DFA.unpack(
        u"\1\76\1\u0080\2\uffff\1\u0080"
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
        u"\3\1\uffff\15\3\1\uffff\7\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1"
        u"\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\5"
        u"\3\1\uffff\15\3\1\uffff\7\3\2\uffff\1\3\1\uffff\1\3\35\uffff\1"
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
        u"\2\20\2\uffff"
        )

    DFA56_max = DFA.unpack(
        u"\2\110\2\uffff"
        )

    DFA56_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA56_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA56_transition = [
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\11\uffff\1"
        u"\3"),
        DFA.unpack(u"\1\1\43\uffff\1\2\4\uffff\1\3\4\uffff\1\3\11\uffff\1"
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
        u"\2\20\2\uffff"
        )

    DFA76_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA76_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA76_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA76_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\1\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\1\uffff\1\2\6\uffff\1\2\12\uffff"
        u"\1\2\1\uffff\1\2\35\uffff\1\2\1\uffff\15\2"),
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
        u"\2\20\2\uffff"
        )

    DFA79_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA79_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA79_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA79_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\10\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\2\uffff\3\2\1\3\10\uffff\1\2\12\uffff\1\2\1\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA82_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA82_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA82_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA82_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA111_max = DFA.unpack(
        u"\2\115\2\uffff"
        )

    DFA111_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA111_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA111_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\4\uffff\1\2\21\uffff\1\3"),
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
        u"\2\20\2\uffff"
        )

    DFA115_max = DFA.unpack(
        u"\2\73\2\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA114_max = DFA.unpack(
        u"\2\115\2\uffff"
        )

    DFA114_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA114_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA114_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\2\26\uffff\1\3"),
        DFA.unpack(u"\1\1\45\uffff\1\2\26\uffff\1\3"),
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
        u"\1\20\1\uffff\1\20\1\uffff"
        )

    DFA123_max = DFA.unpack(
        u"\1\u0080\1\uffff\1\115\1\uffff"
        )

    DFA123_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA123_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA123_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\10\1\1\uffff\4\1\1\uffff\4\1\1\3\2\1\2\uffff"
        u"\1\1\1\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3\26\uffff"
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
        u"\2\20\2\uffff"
        )

    DFA127_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA127_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA127_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA127_transition = [
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\15\3\1\uffff\7\3\1\uffff\1\2\1\3\1\uffff\1\3\35\uffff"
        u"\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\5\3\31\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\uffff"
        u"\4\3\2\uffff\15\3\1\uffff\7\3\1\uffff\1\2\1\3\1\uffff\1\3\35\uffff"
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
        u"\1\20\1\uffff\1\20\1\uffff\1\20"
        )

    DFA136_max = DFA.unpack(
        u"\1\125\1\uffff\1\u0080\1\uffff\1\u0080"
        )

    DFA136_accept = DFA.unpack(
        u"\1\uffff\1\2\1\uffff\1\1\1\uffff"
        )

    DFA136_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA136_transition = [
        DFA.unpack(u"\1\2\41\uffff\1\1\3\uffff\1\1\2\uffff\1\3\1\1\3\uffff"
        u"\1\1\26\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\1\31\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\3\16"
        u"\1\1\uffff\7\1\2\uffff\1\1\1\uffff\2\1\34\uffff\1\1\1\uffff\15"
        u"\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\1\31\uffff\1\1\1\uffff\3\1\1\uffff\4\1\1\3\16"
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
        u"\2\20\2\uffff"
        )

    DFA139_max = DFA.unpack(
        u"\2\76\2\uffff"
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
    # lookup tables for DFA #166

    DFA166_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA166_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA166_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA166_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA166_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA166_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA166_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\uffff\1\3\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\35\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #166

    DFA166 = DFA
    # lookup tables for DFA #179

    DFA179_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA179_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA179_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA179_max = DFA.unpack(
        u"\1\142\1\u0080\2\uffff\1\u0080"
        )

    DFA179_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA179_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA179_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\3\uffff\1\3\2\uffff\2\3\3\uffff\1"
        u"\3\26\uffff\1\3\14\uffff\1\2"),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\3\3\1\uffff\23\3\1\uffff"
        u"\7\3\2\uffff\1\3\1\uffff\2\3\14\uffff\1\2\17\uffff\1\3\1\uffff"
        u"\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\3\31\uffff\1\3\1\uffff\3\3\1\uffff\23\3\1\uffff"
        u"\7\3\2\uffff\1\3\1\uffff\2\3\14\uffff\1\2\17\uffff\1\3\1\uffff"
        u"\15\3")
    ]

    # class definition for DFA #179

    DFA179 = DFA
    # lookup tables for DFA #184

    DFA184_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA184_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA184_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA184_max = DFA.unpack(
        u"\2\142\2\uffff"
        )

    DFA184_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA184_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA184_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\11\uffff\1"
        u"\3\31\uffff\1\2"),
        DFA.unpack(u"\1\1\41\uffff\1\3\6\uffff\1\3\4\uffff\1\3\11\uffff\1"
        u"\3\31\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #184

    DFA184 = DFA
    # lookup tables for DFA #187

    DFA187_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA187_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA187_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA187_max = DFA.unpack(
        u"\1\143\1\u0080\2\uffff\1\u0080"
        )

    DFA187_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA187_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA187_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\1\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\1\2\1\3\16\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\1\2\1\3\16\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #187

    DFA187 = DFA
    # lookup tables for DFA #190

    DFA190_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA190_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA190_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA190_max = DFA.unpack(
        u"\2\143\2\uffff"
        )

    DFA190_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA190_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA190_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #190

    DFA190 = DFA
    # lookup tables for DFA #193

    DFA193_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA193_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA193_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA193_max = DFA.unpack(
        u"\1\144\1\u0080\2\uffff\1\u0080"
        )

    DFA193_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA193_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA193_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\2\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\2\2\1\3\15\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\2\2\1\3\15\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #193

    DFA193 = DFA
    # lookup tables for DFA #196

    DFA196_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA196_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA196_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA196_max = DFA.unpack(
        u"\2\144\2\uffff"
        )

    DFA196_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA196_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA196_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #196

    DFA196 = DFA
    # lookup tables for DFA #199

    DFA199_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA199_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA199_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA199_max = DFA.unpack(
        u"\1\145\1\u0080\2\uffff\1\u0080"
        )

    DFA199_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA199_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA199_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\3\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\3\2\1\3\14\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\3\2\1\3\14\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #199

    DFA199 = DFA
    # lookup tables for DFA #202

    DFA202_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA202_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA202_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA202_max = DFA.unpack(
        u"\2\145\2\uffff"
        )

    DFA202_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA202_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA202_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #202

    DFA202 = DFA
    # lookup tables for DFA #205

    DFA205_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA205_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA205_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA205_max = DFA.unpack(
        u"\1\146\1\u0080\2\uffff\1\u0080"
        )

    DFA205_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA205_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA205_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\4\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\4\2\1\3\13\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\4\2\1\3\13\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #205

    DFA205 = DFA
    # lookup tables for DFA #208

    DFA208_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA208_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA208_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA208_max = DFA.unpack(
        u"\2\146\2\uffff"
        )

    DFA208_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA208_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA208_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\4\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #208

    DFA208 = DFA
    # lookup tables for DFA #211

    DFA211_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA211_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA211_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA211_max = DFA.unpack(
        u"\1\147\1\u0080\2\uffff\1\u0080"
        )

    DFA211_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA211_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA211_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\5\2\1\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\5\2\1\3\12\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\5\2\1\3\12\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #211

    DFA211 = DFA
    # lookup tables for DFA #214

    DFA214_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA214_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA214_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA214_max = DFA.unpack(
        u"\2\147\2\uffff"
        )

    DFA214_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA214_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA214_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\5\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #214

    DFA214 = DFA
    # lookup tables for DFA #217

    DFA217_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA217_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA217_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA217_max = DFA.unpack(
        u"\1\153\1\u0080\2\uffff\1\u0080"
        )

    DFA217_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA217_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA217_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\3\uffff\1\2\2\uffff\2\2\3\uffff\1"
        u"\2\26\uffff\1\2\14\uffff\6\2\4\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\6\2\4\3\6\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\1\2\1\uffff\3\2\1\uffff\23\2\1\uffff"
        u"\7\2\2\uffff\1\2\1\uffff\2\2\14\uffff\6\2\4\3\6\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #217

    DFA217 = DFA
    # lookup tables for DFA #220

    DFA220_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA220_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA220_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA220_max = DFA.unpack(
        u"\2\153\2\uffff"
        )

    DFA220_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA220_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA220_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\6\uffff\1\2\4\uffff\1\2\11\uffff\1"
        u"\2\31\uffff\6\2\4\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #220

    DFA220 = DFA
    # lookup tables for DFA #226

    DFA226_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA226_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA226_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA226_max = DFA.unpack(
        u"\2\156\2\uffff"
        )

    DFA226_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA226_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA226_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\11\uffff\1\2\31\uffff\12\2\3\3"),
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\2\6\uffff\1\2\4\uffff\1"
        u"\2\11\uffff\1\2\31\uffff\12\2\3\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #226

    DFA226 = DFA
    # lookup tables for DFA #229

    DFA229_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA229_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA229_min = DFA.unpack(
        u"\2\20\2\uffff\1\20"
        )

    DFA229_max = DFA.unpack(
        u"\1\161\1\u0080\2\uffff\1\u0080"
        )

    DFA229_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA229_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA229_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\3\uffff\1\2\2\uffff\2"
        u"\2\3\uffff\1\2\11\uffff\1\2\14\uffff\1\2\14\uffff\15\2\3\3"),
        DFA.unpack(u"\1\4\5\2\31\uffff\5\2\1\uffff\33\2\2\uffff\1\2\1\uffff"
        u"\2\2\14\uffff\15\2\3\3\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\5\2\31\uffff\5\2\1\uffff\33\2\2\uffff\1\2\1\uffff"
        u"\2\2\14\uffff\15\2\3\3\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #229

    DFA229 = DFA
    # lookup tables for DFA #242

    DFA242_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA242_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA242_min = DFA.unpack(
        u"\1\20\1\uffff\1\20\1\uffff"
        )

    DFA242_max = DFA.unpack(
        u"\1\u0080\1\uffff\1\125\1\uffff"
        )

    DFA242_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA242_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA242_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\uffff\2\1\1\3\1\uffff\3\1\11\uffff\1\1\12\uffff\1\1\1\uffff"
        u"\1\1\1\3\34\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\3\uffff\1"
        u"\3\33\uffff\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #242

    DFA242 = DFA
    # lookup tables for DFA #246

    DFA246_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA246_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA246_min = DFA.unpack(
        u"\2\20\1\0\2\uffff"
        )

    DFA246_max = DFA.unpack(
        u"\2\125\1\0\2\uffff"
        )

    DFA246_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA246_special = DFA.unpack(
        u"\2\uffff\1\0\2\uffff"
        )

            
    DFA246_transition = [
        DFA.unpack(u"\1\1\50\uffff\1\2\33\uffff\1\3"),
        DFA.unpack(u"\1\1\50\uffff\1\2\33\uffff\1\3"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #246

    class DFA246(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA246_2 = input.LA(1)

                 
                index246_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred325()):
                    s = 4

                elif (True):
                    s = 3

                 
                input.seek(index246_2)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 246, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #245

    DFA245_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA245_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA245_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA245_max = DFA.unpack(
        u"\2\u0080\2\uffff"
        )

    DFA245_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA245_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA245_transition = [
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\1\3\34\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\5\2\31\uffff\1\2\1\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\2\1\uffff\2\2\1\3\1\uffff\3\2\11\uffff\1\2\12\uffff\1\2\1\uffff"
        u"\1\2\1\3\34\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #245

    DFA245 = DFA
    # lookup tables for DFA #254

    DFA254_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA254_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA254_min = DFA.unpack(
        u"\3\20\1\uffff\1\20\1\uffff"
        )

    DFA254_max = DFA.unpack(
        u"\2\71\1\175\1\uffff\1\175\1\uffff"
        )

    DFA254_accept = DFA.unpack(
        u"\3\uffff\1\2\1\uffff\1\1"
        )

    DFA254_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA254_transition = [
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\45\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\11\uffff"
        u"\1\5\64\uffff\2\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\5\1\uffff\2\5\41\uffff\1\3\4\uffff\3\5\11\uffff"
        u"\1\5\64\uffff\2\5"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #254

    DFA254 = DFA
    # lookup tables for DFA #268

    DFA268_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA268_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA268_min = DFA.unpack(
        u"\1\21\1\20\1\uffff\4\20\2\uffff"
        )

    DFA268_max = DFA.unpack(
        u"\2\175\1\uffff\4\175\2\uffff"
        )

    DFA268_accept = DFA.unpack(
        u"\2\uffff\1\1\4\uffff\1\3\1\2"
        )

    DFA268_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA268_transition = [
        DFA.unpack(u"\1\2\1\uffff\2\2\46\uffff\3\2\11\uffff\1\2\64\uffff"
        u"\1\1\1\3"),
        DFA.unpack(u"\1\5\3\uffff\1\4\35\uffff\1\2\10\uffff\3\4\11\uffff"
        u"\1\4\64\uffff\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\3\uffff\1\4\35\uffff\1\2\10\uffff\3\4\11\uffff"
        u"\1\4\64\uffff\2\4"),
        DFA.unpack(u"\1\6\3\uffff\1\10\43\uffff\1\7\2\uffff\3\10\11\uffff"
        u"\1\10\64\uffff\2\10"),
        DFA.unpack(u"\1\5\3\uffff\1\7\35\uffff\1\2\10\uffff\3\7\11\uffff"
        u"\1\7\64\uffff\2\7"),
        DFA.unpack(u"\1\6\3\uffff\1\10\43\uffff\1\7\2\uffff\3\10\11\uffff"
        u"\1\10\64\uffff\2\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #268

    DFA268 = DFA
    # lookup tables for DFA #290

    DFA290_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA290_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA290_min = DFA.unpack(
        u"\1\20\1\uffff\1\20\1\uffff"
        )

    DFA290_max = DFA.unpack(
        u"\1\u0080\1\uffff\1\66\1\uffff"
        )

    DFA290_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2"
        )

    DFA290_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA290_transition = [
        DFA.unpack(u"\1\2\5\1\31\uffff\1\1\1\uffff\1\1\1\uffff\1\1\1\uffff"
        u"\1\1\1\3\2\1\2\uffff\10\1\1\uffff\4\1\1\uffff\4\1\1\uffff\2\1\2"
        u"\uffff\1\1\1\uffff\1\1\35\uffff\1\1\1\uffff\15\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\uffff\1\1\34\uffff\1\1\5\uffff\1\1\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #290

    DFA290 = DFA
 

    FOLLOW_LT_in_program96 = frozenset([1])
    FOLLOW_sourceElements_in_program100 = frozenset([16])
    FOLLOW_LT_in_program102 = frozenset([1])
    FOLLOW_EOF_in_program106 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements119 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_sourceElements122 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_sourceElement_in_sourceElements126 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_functionDeclaration_in_sourceElement145 = frozenset([1])
    FOLLOW_statement_in_sourceElement150 = frozenset([1])
    FOLLOW_47_in_xmlStartTag168 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_xmlTagName_in_xmlStartTag170 = frozenset([16, 20, 48, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_xmlStartTag173 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_xmlAttribute_in_xmlStartTag177 = frozenset([16, 20, 48, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_xmlStartTag181 = frozenset([1])
    FOLLOW_48_in_xmlStartTag185 = frozenset([1])
    FOLLOW_47_in_xmlEndTag203 = frozenset([49])
    FOLLOW_49_in_xmlEndTag205 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_xmlTagName_in_xmlEndTag207 = frozenset([48])
    FOLLOW_48_in_xmlEndTag209 = frozenset([1])
    FOLLOW_47_in_xmlEmptyTag227 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_xmlTagName_in_xmlEmptyTag229 = frozenset([16, 20, 49, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_xmlEmptyTag232 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_xmlAttribute_in_xmlEmptyTag236 = frozenset([16, 20, 49, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_xmlEmptyTag240 = frozenset([1])
    FOLLOW_49_in_xmlEmptyTag244 = frozenset([48])
    FOLLOW_48_in_xmlEmptyTag246 = frozenset([1])
    FOLLOW_identifier_in_xmlTagName264 = frozenset([1, 50, 51])
    FOLLOW_set_in_xmlTagName268 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_xmlTagName274 = frozenset([1, 50, 51])
    FOLLOW_xmlAttributeName_in_xmlAttribute294 = frozenset([52])
    FOLLOW_52_in_xmlAttribute296 = frozenset([17, 53])
    FOLLOW_xmlAttributeValue_in_xmlAttribute298 = frozenset([1])
    FOLLOW_identifier_in_xmlAttributeName317 = frozenset([1, 50, 51])
    FOLLOW_set_in_xmlAttributeName321 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_xmlAttributeName327 = frozenset([1, 50, 51])
    FOLLOW_e4xSplice_in_xmlAttributeValue352 = frozenset([1])
    FOLLOW_StringLiteral_in_xmlAttributeValue357 = frozenset([1])
    FOLLOW_53_in_e4xSplice375 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_e4xSplice377 = frozenset([54])
    FOLLOW_54_in_e4xSplice379 = frozenset([1])
    FOLLOW_xmlEndTag_in_xmlPayload393 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_xmlPayload398 = frozenset([1])
    FOLLOW_xmlStartTag_in_xmlPayload403 = frozenset([1])
    FOLLOW_e4xSplice_in_xmlPayload408 = frozenset([1])
    FOLLOW_XMLComment_in_xmlPayload413 = frozenset([1])
    FOLLOW_LT_in_xmlLiteral426 = frozenset([16, 18, 47, 53])
    FOLLOW_xmlPayload_in_xmlLiteral429 = frozenset([1, 16, 18, 47, 53])
    FOLLOW_55_in_functionDeclaration444 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_functionDeclaration446 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_functionDeclaration449 = frozenset([16, 56])
    FOLLOW_LT_in_functionDeclaration451 = frozenset([16, 56])
    FOLLOW_formalParameterList_in_functionDeclaration454 = frozenset([16, 53])
    FOLLOW_LT_in_functionDeclaration456 = frozenset([16, 53])
    FOLLOW_statementBlock_in_functionDeclaration459 = frozenset([1])
    FOLLOW_55_in_functionExpression485 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_functionExpression487 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_functionExpression490 = frozenset([16, 56])
    FOLLOW_LT_in_functionExpression492 = frozenset([16, 56])
    FOLLOW_formalParameterList_in_functionExpression495 = frozenset([16, 53])
    FOLLOW_LT_in_functionExpression497 = frozenset([16, 53])
    FOLLOW_statementBlock_in_functionExpression500 = frozenset([1])
    FOLLOW_55_in_functionExpression519 = frozenset([16, 56])
    FOLLOW_LT_in_functionExpression521 = frozenset([16, 56])
    FOLLOW_formalParameterList_in_functionExpression524 = frozenset([16, 53])
    FOLLOW_LT_in_functionExpression526 = frozenset([16, 53])
    FOLLOW_statementBlock_in_functionExpression529 = frozenset([1])
    FOLLOW_56_in_formalParameterList555 = frozenset([16, 20, 58, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_formalParameterList558 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_formalParameterList562 = frozenset([16, 57, 58])
    FOLLOW_LT_in_formalParameterList565 = frozenset([16, 57])
    FOLLOW_57_in_formalParameterList569 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_formalParameterList571 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_formalParameterList575 = frozenset([16, 57, 58])
    FOLLOW_LT_in_formalParameterList581 = frozenset([1])
    FOLLOW_58_in_formalParameterList585 = frozenset([1])
    FOLLOW_statementBlock_in_statement597 = frozenset([1])
    FOLLOW_variableStatement_in_statement602 = frozenset([1])
    FOLLOW_emptyStatement_in_statement607 = frozenset([1])
    FOLLOW_expressionStatement_in_statement612 = frozenset([1])
    FOLLOW_ifStatement_in_statement617 = frozenset([1])
    FOLLOW_iterationStatement_in_statement622 = frozenset([1])
    FOLLOW_continueStatement_in_statement627 = frozenset([1])
    FOLLOW_breakStatement_in_statement632 = frozenset([1])
    FOLLOW_returnStatement_in_statement637 = frozenset([1])
    FOLLOW_withStatement_in_statement642 = frozenset([1])
    FOLLOW_labelledStatement_in_statement647 = frozenset([1])
    FOLLOW_switchStatement_in_statement652 = frozenset([1])
    FOLLOW_throwStatement_in_statement657 = frozenset([1])
    FOLLOW_tryStatement_in_statement662 = frozenset([1])
    FOLLOW_defaultXmlNamespaceStatement_in_statement667 = frozenset([1])
    FOLLOW_59_in_defaultXmlNamespaceStatement678 = frozenset([60])
    FOLLOW_60_in_defaultXmlNamespaceStatement680 = frozenset([61])
    FOLLOW_61_in_defaultXmlNamespaceStatement682 = frozenset([16, 52])
    FOLLOW_LT_in_defaultXmlNamespaceStatement684 = frozenset([16, 52])
    FOLLOW_52_in_defaultXmlNamespaceStatement687 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_defaultXmlNamespaceStatement689 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_defaultXmlNamespaceStatement692 = frozenset([16, 62])
    FOLLOW_LT_in_defaultXmlNamespaceStatement695 = frozenset([1])
    FOLLOW_62_in_defaultXmlNamespaceStatement699 = frozenset([1])
    FOLLOW_53_in_statementBlock721 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_statementBlock723 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statementList_in_statementBlock727 = frozenset([16, 54])
    FOLLOW_LT_in_statementBlock730 = frozenset([16, 54])
    FOLLOW_54_in_statementBlock734 = frozenset([1])
    FOLLOW_53_in_statementBlock739 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 63, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_63_in_statementBlock741 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_statementBlock744 = frozenset([54])
    FOLLOW_54_in_statementBlock746 = frozenset([1])
    FOLLOW_statement_in_statementList759 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_statementList762 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statement_in_statementList766 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_64_in_variableStatement782 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_65_in_variableStatement786 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_variableStatement789 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_variableDeclarationList_in_variableStatement792 = frozenset([16, 62])
    FOLLOW_LT_in_variableStatement795 = frozenset([1])
    FOLLOW_62_in_variableStatement799 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList824 = frozenset([1, 16, 57])
    FOLLOW_LT_in_variableDeclarationList827 = frozenset([16, 57])
    FOLLOW_57_in_variableDeclarationList831 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_variableDeclarationList833 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_variableDeclaration_in_variableDeclarationList837 = frozenset([1, 16, 57])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn851 = frozenset([1, 16, 57])
    FOLLOW_LT_in_variableDeclarationListNoIn854 = frozenset([16, 57])
    FOLLOW_57_in_variableDeclarationListNoIn858 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_variableDeclarationListNoIn860 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn864 = frozenset([1, 16, 57])
    FOLLOW_identifier_in_variableDeclaration878 = frozenset([1, 16, 52])
    FOLLOW_LT_in_variableDeclaration881 = frozenset([16, 52])
    FOLLOW_initialiser_in_variableDeclaration884 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn911 = frozenset([1, 16, 52])
    FOLLOW_LT_in_variableDeclarationNoIn914 = frozenset([16, 52])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn917 = frozenset([1])
    FOLLOW_52_in_initialiser944 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_initialiser946 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_initialiser949 = frozenset([1])
    FOLLOW_52_in_initialiserNoIn967 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_initialiserNoIn969 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn972 = frozenset([1])
    FOLLOW_62_in_emptyStatement990 = frozenset([1])
    FOLLOW_expression_in_expressionStatement1002 = frozenset([16, 62])
    FOLLOW_set_in_expressionStatement1004 = frozenset([1])
    FOLLOW_66_in_ifStatement1023 = frozenset([16, 56])
    FOLLOW_LT_in_ifStatement1025 = frozenset([1])
    FOLLOW_56_in_ifStatement1029 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_ifStatement1031 = frozenset([1])
    FOLLOW_expression_in_ifStatement1035 = frozenset([16, 58])
    FOLLOW_LT_in_ifStatement1037 = frozenset([1])
    FOLLOW_58_in_ifStatement1041 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_ifStatement1043 = frozenset([1])
    FOLLOW_statement_in_ifStatement1047 = frozenset([1, 16, 67])
    FOLLOW_LT_in_ifStatement1050 = frozenset([16, 67])
    FOLLOW_67_in_ifStatement1054 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_ifStatement1056 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statement_in_ifStatement1060 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement1074 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement1079 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement1084 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement1089 = frozenset([1])
    FOLLOW_68_in_doWhileStatement1101 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_doWhileStatement1103 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement1107 = frozenset([16, 69])
    FOLLOW_LT_in_doWhileStatement1109 = frozenset([1])
    FOLLOW_69_in_doWhileStatement1113 = frozenset([16, 56])
    FOLLOW_LT_in_doWhileStatement1115 = frozenset([1])
    FOLLOW_56_in_doWhileStatement1119 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_doWhileStatement1121 = frozenset([58])
    FOLLOW_58_in_doWhileStatement1123 = frozenset([16, 62])
    FOLLOW_set_in_doWhileStatement1125 = frozenset([1])
    FOLLOW_69_in_whileStatement1144 = frozenset([16, 56])
    FOLLOW_LT_in_whileStatement1146 = frozenset([1])
    FOLLOW_56_in_whileStatement1150 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_whileStatement1152 = frozenset([1])
    FOLLOW_expression_in_whileStatement1156 = frozenset([16, 58])
    FOLLOW_LT_in_whileStatement1158 = frozenset([1])
    FOLLOW_58_in_whileStatement1162 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_whileStatement1164 = frozenset([1])
    FOLLOW_statement_in_whileStatement1168 = frozenset([1])
    FOLLOW_70_in_forStatement1180 = frozenset([16, 56])
    FOLLOW_LT_in_forStatement1182 = frozenset([1])
    FOLLOW_56_in_forStatement1186 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 64, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forStatement1189 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 64, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_forStatementInitialiserPart_in_forStatement1193 = frozenset([16, 62])
    FOLLOW_LT_in_forStatement1197 = frozenset([1])
    FOLLOW_62_in_forStatement1201 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forStatement1204 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_forStatement1208 = frozenset([16, 62])
    FOLLOW_LT_in_forStatement1212 = frozenset([1])
    FOLLOW_62_in_forStatement1216 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 58, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forStatement1219 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_forStatement1223 = frozenset([16, 58])
    FOLLOW_LT_in_forStatement1227 = frozenset([1])
    FOLLOW_58_in_forStatement1231 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forStatement1233 = frozenset([1])
    FOLLOW_statement_in_forStatement1237 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart1249 = frozenset([1])
    FOLLOW_64_in_forStatementInitialiserPart1254 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_forStatementInitialiserPart1256 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart1260 = frozenset([1])
    FOLLOW_70_in_forInStatement1272 = frozenset([16, 56, 71])
    FOLLOW_LT_in_forInStatement1274 = frozenset([1])
    FOLLOW_71_in_forInStatement1278 = frozenset([16, 56])
    FOLLOW_LT_in_forInStatement1281 = frozenset([1])
    FOLLOW_56_in_forInStatement1285 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 53, 55, 56, 59, 60, 61, 64, 71, 82, 84, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forInStatement1287 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement1291 = frozenset([16, 72])
    FOLLOW_LT_in_forInStatement1293 = frozenset([1])
    FOLLOW_72_in_forInStatement1297 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forInStatement1299 = frozenset([1])
    FOLLOW_expression_in_forInStatement1303 = frozenset([16, 58])
    FOLLOW_LT_in_forInStatement1305 = frozenset([1])
    FOLLOW_58_in_forInStatement1309 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_forInStatement1311 = frozenset([1])
    FOLLOW_statement_in_forInStatement1315 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart1327 = frozenset([1])
    FOLLOW_64_in_forInStatementInitialiserPart1332 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_forInStatementInitialiserPart1334 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart1338 = frozenset([1])
    FOLLOW_73_in_continueStatement1349 = frozenset([16, 20, 59, 60, 61, 62, 71, 124, 125])
    FOLLOW_identifier_in_continueStatement1351 = frozenset([16, 62])
    FOLLOW_set_in_continueStatement1354 = frozenset([1])
    FOLLOW_74_in_breakStatement1372 = frozenset([16, 20, 59, 60, 61, 62, 71, 124, 125])
    FOLLOW_identifier_in_breakStatement1374 = frozenset([16, 62])
    FOLLOW_set_in_breakStatement1377 = frozenset([1])
    FOLLOW_63_in_returnStatement1395 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_returnStatement1397 = frozenset([16, 62])
    FOLLOW_set_in_returnStatement1400 = frozenset([1])
    FOLLOW_75_in_withStatement1419 = frozenset([16, 56])
    FOLLOW_LT_in_withStatement1421 = frozenset([1])
    FOLLOW_56_in_withStatement1425 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_withStatement1427 = frozenset([1])
    FOLLOW_expression_in_withStatement1431 = frozenset([16, 58])
    FOLLOW_LT_in_withStatement1433 = frozenset([1])
    FOLLOW_58_in_withStatement1437 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_withStatement1439 = frozenset([1])
    FOLLOW_statement_in_withStatement1443 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1454 = frozenset([16, 50])
    FOLLOW_LT_in_labelledStatement1456 = frozenset([1])
    FOLLOW_50_in_labelledStatement1460 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_labelledStatement1462 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1466 = frozenset([1])
    FOLLOW_76_in_switchStatement1478 = frozenset([16, 56])
    FOLLOW_LT_in_switchStatement1480 = frozenset([1])
    FOLLOW_56_in_switchStatement1484 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_switchStatement1486 = frozenset([1])
    FOLLOW_expression_in_switchStatement1490 = frozenset([16, 58])
    FOLLOW_LT_in_switchStatement1492 = frozenset([1])
    FOLLOW_58_in_switchStatement1496 = frozenset([16, 53])
    FOLLOW_LT_in_switchStatement1498 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1502 = frozenset([1])
    FOLLOW_53_in_caseBlock1514 = frozenset([16, 54, 59, 77])
    FOLLOW_LT_in_caseBlock1517 = frozenset([16, 77])
    FOLLOW_caseClause_in_caseBlock1521 = frozenset([16, 54, 59, 77])
    FOLLOW_LT_in_caseBlock1526 = frozenset([16, 59])
    FOLLOW_defaultClause_in_caseBlock1530 = frozenset([16, 54, 77])
    FOLLOW_LT_in_caseBlock1533 = frozenset([16, 77])
    FOLLOW_caseClause_in_caseBlock1537 = frozenset([16, 54, 77])
    FOLLOW_LT_in_caseBlock1543 = frozenset([1])
    FOLLOW_54_in_caseBlock1547 = frozenset([1])
    FOLLOW_77_in_caseClause1558 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_caseClause1560 = frozenset([1])
    FOLLOW_expression_in_caseClause1564 = frozenset([16, 50])
    FOLLOW_LT_in_caseClause1566 = frozenset([1])
    FOLLOW_50_in_caseClause1570 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_caseClause1572 = frozenset([1])
    FOLLOW_statementList_in_caseClause1576 = frozenset([1])
    FOLLOW_59_in_defaultClause1589 = frozenset([16, 50])
    FOLLOW_LT_in_defaultClause1591 = frozenset([1])
    FOLLOW_50_in_defaultClause1595 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_defaultClause1597 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1601 = frozenset([1])
    FOLLOW_78_in_throwStatement1614 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_throwStatement1616 = frozenset([16, 62])
    FOLLOW_set_in_throwStatement1618 = frozenset([1])
    FOLLOW_79_in_tryStatement1636 = frozenset([16, 53])
    FOLLOW_LT_in_tryStatement1638 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1642 = frozenset([16, 80, 81])
    FOLLOW_LT_in_tryStatement1644 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1649 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1653 = frozenset([1, 16, 81])
    FOLLOW_LT_in_tryStatement1656 = frozenset([16, 81])
    FOLLOW_finallyClause_in_tryStatement1660 = frozenset([1])
    FOLLOW_80_in_catchClause1681 = frozenset([16, 56])
    FOLLOW_LT_in_catchClause1683 = frozenset([1])
    FOLLOW_56_in_catchClause1687 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_catchClause1689 = frozenset([1])
    FOLLOW_identifier_in_catchClause1693 = frozenset([16, 58])
    FOLLOW_LT_in_catchClause1695 = frozenset([1])
    FOLLOW_58_in_catchClause1699 = frozenset([16, 53])
    FOLLOW_LT_in_catchClause1701 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1705 = frozenset([1])
    FOLLOW_81_in_finallyClause1717 = frozenset([16, 53])
    FOLLOW_LT_in_finallyClause1719 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause1723 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1735 = frozenset([1, 16, 57])
    FOLLOW_LT_in_expression1738 = frozenset([16, 57])
    FOLLOW_57_in_expression1742 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_expression1744 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_expression1748 = frozenset([1, 16, 57])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1762 = frozenset([1, 16, 57])
    FOLLOW_LT_in_expressionNoIn1765 = frozenset([16, 57])
    FOLLOW_57_in_expressionNoIn1769 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_expressionNoIn1771 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1775 = frozenset([1, 16, 57])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1789 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_LT_in_assignmentExpression1791 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_assignmentOperator_in_assignmentExpression1795 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_assignmentExpression1797 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_assignmentExpression1801 = frozenset([1])
    FOLLOW_conditionalExpression_in_assignmentExpression1806 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1818 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_LT_in_assignmentExpressionNoIn1820 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1824 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_assignmentExpressionNoIn1826 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1830 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1835 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression1847 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression1852 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1864 = frozenset([1])
    FOLLOW_82_in_newExpression1869 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 53, 55, 56, 59, 60, 61, 71, 82, 84, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_newExpression1871 = frozenset([1])
    FOLLOW_newExpression_in_newExpression1875 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1888 = frozenset([1, 16, 50, 83, 84])
    FOLLOW_functionExpression_in_memberExpression1892 = frozenset([1, 16, 50, 83, 84])
    FOLLOW_82_in_memberExpression1896 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 53, 55, 56, 59, 60, 61, 71, 82, 84, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_memberExpression1898 = frozenset([1])
    FOLLOW_memberExpression_in_memberExpression1902 = frozenset([16, 56])
    FOLLOW_LT_in_memberExpression1904 = frozenset([1])
    FOLLOW_arguments_in_memberExpression1908 = frozenset([1, 16, 50, 83, 84])
    FOLLOW_LT_in_memberExpression1912 = frozenset([16, 50, 83, 84])
    FOLLOW_memberExpressionSuffix_in_memberExpression1916 = frozenset([1, 16, 50, 83, 84])
    FOLLOW_indexSuffix_in_memberExpressionSuffix1930 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1935 = frozenset([1])
    FOLLOW_descendentSuffix_in_memberExpressionSuffix1940 = frozenset([1])
    FOLLOW_namespaceSuffix_in_memberExpressionSuffix1946 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression1961 = frozenset([16, 56, 83])
    FOLLOW_LT_in_callExpression1963 = frozenset([16, 56, 83])
    FOLLOW_83_in_callExpression1966 = frozenset([16, 56])
    FOLLOW_LT_in_callExpression1969 = frozenset([16, 56])
    FOLLOW_arguments_in_callExpression1972 = frozenset([1, 16, 50, 56, 83, 84])
    FOLLOW_LT_in_callExpression1975 = frozenset([16, 50, 56, 83, 84])
    FOLLOW_callExpressionSuffix_in_callExpression1978 = frozenset([1, 16, 50, 56, 83, 84])
    FOLLOW_arguments_in_callExpressionSuffix2007 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix2012 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix2017 = frozenset([1])
    FOLLOW_descendentSuffix_in_callExpressionSuffix2022 = frozenset([1])
    FOLLOW_namespaceSuffix_in_callExpressionSuffix2028 = frozenset([1])
    FOLLOW_56_in_arguments2043 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 58, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_arguments2046 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_arguments2050 = frozenset([16, 57, 58])
    FOLLOW_LT_in_arguments2052 = frozenset([1, 16, 57])
    FOLLOW_57_in_arguments2057 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_arguments2059 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_arguments2063 = frozenset([16, 57, 58])
    FOLLOW_LT_in_arguments2065 = frozenset([1, 16, 57])
    FOLLOW_LT_in_arguments2073 = frozenset([1])
    FOLLOW_58_in_arguments2077 = frozenset([1])
    FOLLOW_84_in_indexSuffix2089 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_indexSuffix2091 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_expression_in_indexSuffix2094 = frozenset([16, 85])
    FOLLOW_LT_in_indexSuffix2096 = frozenset([16, 85])
    FOLLOW_85_in_indexSuffix2099 = frozenset([1])
    FOLLOW_83_in_propertyReferenceSuffix2122 = frozenset([16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_LT_in_propertyReferenceSuffix2124 = frozenset([16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_e4xIdentifier_in_propertyReferenceSuffix2127 = frozenset([1])
    FOLLOW_83_in_descendentSuffix2148 = frozenset([83])
    FOLLOW_83_in_descendentSuffix2150 = frozenset([16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_LT_in_descendentSuffix2152 = frozenset([16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_e4xIdentifier_in_descendentSuffix2155 = frozenset([1])
    FOLLOW_50_in_namespaceSuffix2176 = frozenset([50])
    FOLLOW_50_in_namespaceSuffix2178 = frozenset([1, 16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_LT_in_namespaceSuffix2180 = frozenset([1, 16, 20, 59, 60, 61, 71, 86, 124, 125])
    FOLLOW_e4xIdentifier_in_namespaceSuffix2183 = frozenset([1])
    FOLLOW_identifier_in_e4xIdentifier2206 = frozenset([1])
    FOLLOW_86_in_e4xIdentifier2211 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression2278 = frozenset([1, 16, 98])
    FOLLOW_LT_in_conditionalExpression2281 = frozenset([16, 98])
    FOLLOW_98_in_conditionalExpression2285 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_conditionalExpression2287 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_conditionalExpression2291 = frozenset([16, 50])
    FOLLOW_LT_in_conditionalExpression2293 = frozenset([16, 50])
    FOLLOW_50_in_conditionalExpression2297 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_conditionalExpression2299 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_conditionalExpression2303 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn2316 = frozenset([1, 16, 98])
    FOLLOW_LT_in_conditionalExpressionNoIn2319 = frozenset([16, 98])
    FOLLOW_98_in_conditionalExpressionNoIn2323 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_conditionalExpressionNoIn2325 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2329 = frozenset([16, 50])
    FOLLOW_LT_in_conditionalExpressionNoIn2331 = frozenset([16, 50])
    FOLLOW_50_in_conditionalExpressionNoIn2335 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_conditionalExpressionNoIn2337 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn2341 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression2354 = frozenset([1, 16, 99])
    FOLLOW_LT_in_logicalORExpression2357 = frozenset([16, 99])
    FOLLOW_99_in_logicalORExpression2361 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_logicalORExpression2363 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_logicalANDExpression_in_logicalORExpression2367 = frozenset([1, 16, 99])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2381 = frozenset([1, 16, 99])
    FOLLOW_LT_in_logicalORExpressionNoIn2384 = frozenset([16, 99])
    FOLLOW_99_in_logicalORExpressionNoIn2388 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_logicalORExpressionNoIn2390 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn2394 = frozenset([1, 16, 99])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2408 = frozenset([1, 16, 100])
    FOLLOW_LT_in_logicalANDExpression2411 = frozenset([16, 100])
    FOLLOW_100_in_logicalANDExpression2415 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_logicalANDExpression2417 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression2421 = frozenset([1, 16, 100])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2435 = frozenset([1, 16, 100])
    FOLLOW_LT_in_logicalANDExpressionNoIn2438 = frozenset([16, 100])
    FOLLOW_100_in_logicalANDExpressionNoIn2442 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_logicalANDExpressionNoIn2444 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn2448 = frozenset([1, 16, 100])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2462 = frozenset([1, 16, 101])
    FOLLOW_LT_in_bitwiseORExpression2465 = frozenset([16, 101])
    FOLLOW_101_in_bitwiseORExpression2469 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseORExpression2471 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2475 = frozenset([1, 16, 101])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2489 = frozenset([1, 16, 101])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2492 = frozenset([16, 101])
    FOLLOW_101_in_bitwiseORExpressionNoIn2496 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2498 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2502 = frozenset([1, 16, 101])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2516 = frozenset([1, 16, 102])
    FOLLOW_LT_in_bitwiseXORExpression2519 = frozenset([16, 102])
    FOLLOW_102_in_bitwiseXORExpression2523 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseXORExpression2525 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2529 = frozenset([1, 16, 102])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2543 = frozenset([1, 16, 102])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2546 = frozenset([16, 102])
    FOLLOW_102_in_bitwiseXORExpressionNoIn2550 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2552 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2556 = frozenset([1, 16, 102])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2570 = frozenset([1, 16, 103])
    FOLLOW_LT_in_bitwiseANDExpression2573 = frozenset([16, 103])
    FOLLOW_103_in_bitwiseANDExpression2577 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseANDExpression2579 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2583 = frozenset([1, 16, 103])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2597 = frozenset([1, 16, 103])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2600 = frozenset([16, 103])
    FOLLOW_103_in_bitwiseANDExpressionNoIn2604 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2606 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2610 = frozenset([1, 16, 103])
    FOLLOW_relationalExpression_in_equalityExpression2624 = frozenset([1, 16, 104, 105, 106, 107])
    FOLLOW_LT_in_equalityExpression2627 = frozenset([16, 104, 105, 106, 107])
    FOLLOW_set_in_equalityExpression2631 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_equalityExpression2647 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_relationalExpression_in_equalityExpression2651 = frozenset([1, 16, 104, 105, 106, 107])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2664 = frozenset([1, 16, 104, 105, 106, 107])
    FOLLOW_LT_in_equalityExpressionNoIn2667 = frozenset([16, 104, 105, 106, 107])
    FOLLOW_set_in_equalityExpressionNoIn2671 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_equalityExpressionNoIn2687 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2691 = frozenset([1, 16, 104, 105, 106, 107])
    FOLLOW_shiftExpression_in_relationalExpression2705 = frozenset([1, 16, 47, 48, 72, 108, 109, 110])
    FOLLOW_LT_in_relationalExpression2708 = frozenset([16, 47, 48, 72, 108, 109, 110])
    FOLLOW_set_in_relationalExpression2712 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_relationalExpression2736 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_shiftExpression_in_relationalExpression2740 = frozenset([1, 16, 47, 48, 72, 108, 109, 110])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2753 = frozenset([1, 16, 47, 48, 108, 109, 110])
    FOLLOW_LT_in_relationalExpressionNoIn2756 = frozenset([16, 47, 48, 108, 109, 110])
    FOLLOW_set_in_relationalExpressionNoIn2760 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_relationalExpressionNoIn2780 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2784 = frozenset([1, 16, 47, 48, 108, 109, 110])
    FOLLOW_additiveExpression_in_shiftExpression2797 = frozenset([1, 16, 111, 112, 113])
    FOLLOW_LT_in_shiftExpression2800 = frozenset([16, 111, 112, 113])
    FOLLOW_set_in_shiftExpression2804 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_shiftExpression2816 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_additiveExpression_in_shiftExpression2820 = frozenset([1, 16, 111, 112, 113])
    FOLLOW_multiplicativeExpression_in_additiveExpression2833 = frozenset([1, 16, 51, 114])
    FOLLOW_LT_in_additiveExpression2836 = frozenset([16, 51, 114])
    FOLLOW_set_in_additiveExpression2840 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_additiveExpression2848 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_multiplicativeExpression_in_additiveExpression2852 = frozenset([1, 16, 51, 114])
    FOLLOW_unaryExpression_in_multiplicativeExpression2865 = frozenset([1, 16, 49, 86, 115])
    FOLLOW_LT_in_multiplicativeExpression2868 = frozenset([16, 49, 86, 115])
    FOLLOW_set_in_multiplicativeExpression2872 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_multiplicativeExpression2884 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_unaryExpression_in_multiplicativeExpression2888 = frozenset([1, 16, 49, 86, 115])
    FOLLOW_postfixExpression_in_unaryExpression2901 = frozenset([1])
    FOLLOW_set_in_unaryExpression2906 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_unaryExpression_in_unaryExpression2942 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression2954 = frozenset([1, 119, 120])
    FOLLOW_set_in_postfixExpression2956 = frozenset([1])
    FOLLOW_123_in_primaryExpression2974 = frozenset([1])
    FOLLOW_xmlLiteral_in_primaryExpression2991 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression2996 = frozenset([1])
    FOLLOW_literal_in_primaryExpression3001 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression3006 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression3011 = frozenset([1])
    FOLLOW_56_in_primaryExpression3016 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_primaryExpression3018 = frozenset([1])
    FOLLOW_expression_in_primaryExpression3022 = frozenset([16, 58])
    FOLLOW_LT_in_primaryExpression3024 = frozenset([1])
    FOLLOW_58_in_primaryExpression3028 = frozenset([1])
    FOLLOW_84_in_arrayLiteral3041 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 57, 59, 60, 61, 71, 82, 84, 85, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_arrayLiteral3043 = frozenset([1])
    FOLLOW_assignmentExpression_in_arrayLiteral3047 = frozenset([16, 57, 85])
    FOLLOW_LT_in_arrayLiteral3051 = frozenset([16, 57])
    FOLLOW_57_in_arrayLiteral3055 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 57, 59, 60, 61, 71, 82, 84, 85, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_arrayLiteral3058 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_arrayLiteral3062 = frozenset([16, 57, 85])
    FOLLOW_LT_in_arrayLiteral3068 = frozenset([1])
    FOLLOW_57_in_arrayLiteral3073 = frozenset([16, 85])
    FOLLOW_LT_in_arrayLiteral3075 = frozenset([1, 16])
    FOLLOW_85_in_arrayLiteral3081 = frozenset([1])
    FOLLOW_53_in_objectLiteral3100 = frozenset([16, 17, 19, 20, 54, 57, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_objectLiteral3102 = frozenset([16, 17, 19, 20, 54, 57, 59, 60, 61, 71, 124, 125])
    FOLLOW_propertyNameAndValue_in_objectLiteral3105 = frozenset([16, 54, 57])
    FOLLOW_LT_in_objectLiteral3109 = frozenset([16, 57])
    FOLLOW_57_in_objectLiteral3112 = frozenset([16, 17, 19, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_objectLiteral3114 = frozenset([16, 17, 19, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_propertyNameAndValue_in_objectLiteral3117 = frozenset([16, 54, 57])
    FOLLOW_LT_in_objectLiteral3121 = frozenset([16, 54, 57])
    FOLLOW_57_in_objectLiteral3125 = frozenset([16, 54])
    FOLLOW_LT_in_objectLiteral3127 = frozenset([16, 54])
    FOLLOW_54_in_objectLiteral3132 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue3156 = frozenset([16, 50])
    FOLLOW_LT_in_propertyNameAndValue3158 = frozenset([16, 50])
    FOLLOW_50_in_propertyNameAndValue3161 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_propertyNameAndValue3163 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_propertyNameAndValue3166 = frozenset([1])
    FOLLOW_124_in_propertyNameAndValue3188 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_125_in_propertyNameAndValue3192 = frozenset([20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_propertyNameAndValue3197 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_propertyNameAndValue3199 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_propertyNameAndValue3204 = frozenset([16, 56])
    FOLLOW_LT_in_propertyNameAndValue3206 = frozenset([16, 56])
    FOLLOW_formalParameterList_in_propertyNameAndValue3209 = frozenset([16, 53])
    FOLLOW_LT_in_propertyNameAndValue3211 = frozenset([16, 53])
    FOLLOW_statementBlock_in_propertyNameAndValue3214 = frozenset([1])
    FOLLOW_124_in_propertyNameAndValue3247 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_125_in_propertyNameAndValue3251 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_LT_in_propertyNameAndValue3254 = frozenset([16, 20, 59, 60, 61, 71, 124, 125])
    FOLLOW_identifier_in_propertyNameAndValue3257 = frozenset([16, 56])
    FOLLOW_LT_in_propertyNameAndValue3259 = frozenset([16, 56])
    FOLLOW_formalParameterList_in_propertyNameAndValue3262 = frozenset([16, 53])
    FOLLOW_LT_in_propertyNameAndValue3264 = frozenset([16, 53])
    FOLLOW_statementBlock_in_propertyNameAndValue3267 = frozenset([1])
    FOLLOW_identifier_in_propertyName3301 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName3306 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName3311 = frozenset([1])
    FOLLOW_126_in_literal3323 = frozenset([1])
    FOLLOW_127_in_literal3328 = frozenset([1])
    FOLLOW_128_in_literal3333 = frozenset([1])
    FOLLOW_StringLiteral_in_literal3338 = frozenset([1])
    FOLLOW_NumericLiteral_in_literal3343 = frozenset([1])
    FOLLOW_regularExpressionLiteral_in_literal3348 = frozenset([1])
    FOLLOW_set_in_reFirstChar0 = frozenset([1])
    FOLLOW_reFirstChar_in_reChars3738 = frozenset([1])
    FOLLOW_86_in_reChars3743 = frozenset([1])
    FOLLOW_49_in_regularExpressionLiteral3754 = frozenset([17, 19, 20, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129])
    FOLLOW_reFirstChar_in_regularExpressionLiteral3756 = frozenset([17, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129])
    FOLLOW_reChars_in_regularExpressionLiteral3758 = frozenset([17, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129])
    FOLLOW_49_in_regularExpressionLiteral3761 = frozenset([1, 20])
    FOLLOW_Identifier_in_regularExpressionLiteral3763 = frozenset([1])
    FOLLOW_RegularExpressionHacks_in_regularExpressionLiteral3769 = frozenset([1, 20])
    FOLLOW_Identifier_in_regularExpressionLiteral3771 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_LT_in_synpred196 = frozenset([1])
    FOLLOW_LT_in_synpred3122 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_functionDeclaration_in_synpred5141 = frozenset([1])
    FOLLOW_53_in_synpred16348 = frozenset([1])
    FOLLOW_xmlEmptyTag_in_synpred18398 = frozenset([1])
    FOLLOW_xmlStartTag_in_synpred19403 = frozenset([1])
    FOLLOW_LT_in_synpred22426 = frozenset([16, 18, 47, 53])
    FOLLOW_xmlPayload_in_synpred22429 = frozenset([1])
    FOLLOW_statementBlock_in_synpred38597 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred41612 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred48647 = frozenset([1])
    FOLLOW_LT_in_synpred55723 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_53_in_synpred58721 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred58723 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statementList_in_synpred58727 = frozenset([16, 54])
    FOLLOW_LT_in_synpred58730 = frozenset([16, 54])
    FOLLOW_54_in_synpred58734 = frozenset([1])
    FOLLOW_LT_in_synpred60762 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred61762 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statement_in_synpred61766 = frozenset([1])
    FOLLOW_LT_in_synpred75946 = frozenset([1])
    FOLLOW_LT_in_synpred76969 = frozenset([1])
    FOLLOW_LT_in_synpred791031 = frozenset([1])
    FOLLOW_LT_in_synpred811043 = frozenset([1])
    FOLLOW_LT_in_synpred831056 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred841050 = frozenset([16, 67])
    FOLLOW_67_in_synpred841054 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred841056 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_statement_in_synpred841060 = frozenset([1])
    FOLLOW_forStatement_in_synpred871084 = frozenset([1])
    FOLLOW_LT_in_synpred881103 = frozenset([1])
    FOLLOW_LT_in_synpred931152 = frozenset([1])
    FOLLOW_LT_in_synpred951164 = frozenset([1])
    FOLLOW_LT_in_synpred971189 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 64, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1001204 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1031219 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1061233 = frozenset([1])
    FOLLOW_LT_in_synpred1091274 = frozenset([1])
    FOLLOW_LT_in_synpred1121287 = frozenset([1])
    FOLLOW_LT_in_synpred1141299 = frozenset([1])
    FOLLOW_LT_in_synpred1161311 = frozenset([1])
    FOLLOW_expression_in_synpred1231397 = frozenset([1])
    FOLLOW_LT_in_synpred1261427 = frozenset([1])
    FOLLOW_LT_in_synpred1281439 = frozenset([1])
    FOLLOW_LT_in_synpred1301462 = frozenset([1])
    FOLLOW_LT_in_synpred1321486 = frozenset([1])
    FOLLOW_LT_in_synpred1421560 = frozenset([1])
    FOLLOW_LT_in_synpred1441572 = frozenset([1])
    FOLLOW_statementList_in_synpred1451576 = frozenset([1])
    FOLLOW_LT_in_synpred1471597 = frozenset([1])
    FOLLOW_LT_in_synpred1611744 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1641771 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1671797 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_leftHandSideExpression_in_synpred1681789 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_LT_in_synpred1681791 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_assignmentOperator_in_synpred1681795 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1681797 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_synpred1681801 = frozenset([1])
    FOLLOW_LT_in_synpred1701826 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_leftHandSideExpression_in_synpred1711818 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_LT_in_synpred1711820 = frozenset([16, 52, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    FOLLOW_assignmentOperator_in_synpred1711824 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1711826 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpressionNoIn_in_synpred1711830 = frozenset([1])
    FOLLOW_callExpression_in_synpred1721847 = frozenset([1])
    FOLLOW_memberExpression_in_synpred1731864 = frozenset([1])
    FOLLOW_LT_in_synpred1741871 = frozenset([1])
    FOLLOW_LT_in_synpred1771898 = frozenset([1])
    FOLLOW_LT_in_synpred1801912 = frozenset([16, 50, 83, 84])
    FOLLOW_memberExpressionSuffix_in_synpred1801916 = frozenset([1])
    FOLLOW_LT_in_synpred1841963 = frozenset([1])
    FOLLOW_LT_in_synpred1881975 = frozenset([16, 50, 56, 83, 84])
    FOLLOW_callExpressionSuffix_in_synpred1881978 = frozenset([1])
    FOLLOW_LT_in_synpred1932046 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1942052 = frozenset([1, 16, 57])
    FOLLOW_LT_in_synpred1952059 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred1962065 = frozenset([1, 16, 57])
    FOLLOW_LT_in_synpred2002091 = frozenset([1])
    FOLLOW_LT_in_synpred2042180 = frozenset([1])
    FOLLOW_e4xIdentifier_in_synpred2052183 = frozenset([1])
    FOLLOW_LT_in_synpred2192287 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2212299 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2242325 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2262337 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2292363 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2322390 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2352417 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2382444 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2412471 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2442498 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2472525 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2502552 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2532579 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2562606 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2622647 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2682687 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2762736 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2772708 = frozenset([16, 47, 48, 72, 108, 109, 110])
    FOLLOW_set_in_synpred2772712 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2772736 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_shiftExpression_in_synpred2772740 = frozenset([1])
    FOLLOW_LT_in_synpred2832780 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2882816 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2922848 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2932836 = frozenset([16, 51, 114])
    FOLLOW_set_in_synpred2932840 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2932848 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_multiplicativeExpression_in_synpred2932852 = frozenset([1])
    FOLLOW_LT_in_synpred2972884 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2982868 = frozenset([16, 49, 86, 115])
    FOLLOW_set_in_synpred2982872 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred2982884 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_unaryExpression_in_synpred2982888 = frozenset([1])
    FOLLOW_LT_in_synpred3132980 = frozenset([16, 18, 47])
    FOLLOW_set_in_synpred3132983 = frozenset([1])
    FOLLOW_objectLiteral_in_synpred3173011 = frozenset([1])
    FOLLOW_LT_in_synpred3183018 = frozenset([1])
    FOLLOW_LT_in_synpred3203043 = frozenset([1])
    FOLLOW_LT_in_synpred3233058 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred3253051 = frozenset([16, 57])
    FOLLOW_57_in_synpred3253055 = frozenset([1, 16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_LT_in_synpred3253058 = frozenset([16, 17, 18, 19, 20, 21, 47, 49, 51, 53, 55, 56, 59, 60, 61, 71, 82, 84, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128])
    FOLLOW_assignmentExpression_in_synpred3253062 = frozenset([1])
    FOLLOW_LT_in_synpred3293102 = frozenset([1])
    FOLLOW_LT_in_synpred3383163 = frozenset([1])

