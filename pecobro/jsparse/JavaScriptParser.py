# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-07 17:33:42

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
RegularExpressionLiteral=11
SingleEscapeCharacter=22
Comment=35
IdentifierPart=15
Identifier=12
HexDigit=26
PROP=7
RegularExpressionChars=14
DecimalDigit=25
LT=8
StringLiteral=9
UnicodeLetter=31
ANONYMOUS=4
NonEscapeCharacter=23
HexIntegerLiteral=28
NumericLiteral=10
ExponentPart=29
UnicodeConnectorPunctuation=33
RegularExpressionFirstChar=13
CharacterEscapeSequence=19
IdentifierStart=30
UnicodeDigit=32
EscapeSequence=16
EscapeCharacter=24
EOF=-1
DecimalLiteral=27
HexEscapeSequence=20
FUNC=5
UnicodeEscapeSequence=21
UnicodeCombiningMark=34
SingleStringCharacter=18
WhiteSpace=37
OBJ=6
LineComment=36
DoubleStringCharacter=17

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ANONYMOUS", "FUNC", "OBJ", "PROP", "LT", "StringLiteral", "NumericLiteral", 
    "RegularExpressionLiteral", "Identifier", "RegularExpressionFirstChar", 
    "RegularExpressionChars", "IdentifierPart", "EscapeSequence", "DoubleStringCharacter", 
    "SingleStringCharacter", "CharacterEscapeSequence", "HexEscapeSequence", 
    "UnicodeEscapeSequence", "SingleEscapeCharacter", "NonEscapeCharacter", 
    "EscapeCharacter", "DecimalDigit", "HexDigit", "DecimalLiteral", "HexIntegerLiteral", 
    "ExponentPart", "IdentifierStart", "UnicodeLetter", "UnicodeDigit", 
    "UnicodeConnectorPunctuation", "UnicodeCombiningMark", "Comment", "LineComment", 
    "WhiteSpace", "'function'", "'('", "','", "')'", "'{'", "'}'", "'var'", 
    "'const'", "';'", "'='", "'if'", "'else'", "'do'", "'while'", "'for'", 
    "'each'", "'in'", "'continue'", "'break'", "'return'", "'with'", "':'", 
    "'switch'", "'case'", "'default'", "'throw'", "'try'", "'catch'", "'finally'", 
    "'new'", "'['", "']'", "'.'", "'*='", "'/='", "'%='", "'+='", "'-='", 
    "'<<='", "'>>='", "'>>>='", "'&='", "'^='", "'|='", "'?'", "'||'", "'&&'", 
    "'|'", "'^'", "'&'", "'=='", "'!='", "'==='", "'!=='", "'<'", "'>'", 
    "'<='", "'>='", "'instanceof'", "'<<'", "'>>'", "'>>>'", "'+'", "'-'", 
    "'*'", "'/'", "'%'", "'delete'", "'void'", "'typeof'", "'++'", "'--'", 
    "'~'", "'!'", "'this'", "'get'", "'set'", "'null'", "'true'", "'false'"
]



class JavaScriptParser(Parser):
    grammarFileName = "/home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)
        self.ruleMemo = {}
        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )
        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )
        self.dfa19 = self.DFA19(
            self, 19,
            eot = self.DFA19_eot,
            eof = self.DFA19_eof,
            min = self.DFA19_min,
            max = self.DFA19_max,
            accept = self.DFA19_accept,
            special = self.DFA19_special,
            transition = self.DFA19_transition
            )
        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )
        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
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
        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
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
        self.dfa60 = self.DFA60(
            self, 60,
            eot = self.DFA60_eot,
            eof = self.DFA60_eof,
            min = self.DFA60_min,
            max = self.DFA60_max,
            accept = self.DFA60_accept,
            special = self.DFA60_special,
            transition = self.DFA60_transition
            )
        self.dfa63 = self.DFA63(
            self, 63,
            eot = self.DFA63_eot,
            eof = self.DFA63_eof,
            min = self.DFA63_min,
            max = self.DFA63_max,
            accept = self.DFA63_accept,
            special = self.DFA63_special,
            transition = self.DFA63_transition
            )
        self.dfa66 = self.DFA66(
            self, 66,
            eot = self.DFA66_eot,
            eof = self.DFA66_eof,
            min = self.DFA66_min,
            max = self.DFA66_max,
            accept = self.DFA66_accept,
            special = self.DFA66_special,
            transition = self.DFA66_transition
            )
        self.dfa95 = self.DFA95(
            self, 95,
            eot = self.DFA95_eot,
            eof = self.DFA95_eof,
            min = self.DFA95_min,
            max = self.DFA95_max,
            accept = self.DFA95_accept,
            special = self.DFA95_special,
            transition = self.DFA95_transition
            )
        self.dfa99 = self.DFA99(
            self, 99,
            eot = self.DFA99_eot,
            eof = self.DFA99_eof,
            min = self.DFA99_min,
            max = self.DFA99_max,
            accept = self.DFA99_accept,
            special = self.DFA99_special,
            transition = self.DFA99_transition
            )
        self.dfa98 = self.DFA98(
            self, 98,
            eot = self.DFA98_eot,
            eof = self.DFA98_eof,
            min = self.DFA98_min,
            max = self.DFA98_max,
            accept = self.DFA98_accept,
            special = self.DFA98_special,
            transition = self.DFA98_transition
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
        self.dfa120 = self.DFA120(
            self, 120,
            eot = self.DFA120_eot,
            eof = self.DFA120_eof,
            min = self.DFA120_min,
            max = self.DFA120_max,
            accept = self.DFA120_accept,
            special = self.DFA120_special,
            transition = self.DFA120_transition
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
        self.dfa147 = self.DFA147(
            self, 147,
            eot = self.DFA147_eot,
            eof = self.DFA147_eof,
            min = self.DFA147_min,
            max = self.DFA147_max,
            accept = self.DFA147_accept,
            special = self.DFA147_special,
            transition = self.DFA147_transition
            )
        self.dfa146 = self.DFA146(
            self, 146,
            eot = self.DFA146_eot,
            eof = self.DFA146_eof,
            min = self.DFA146_min,
            max = self.DFA146_max,
            accept = self.DFA146_accept,
            special = self.DFA146_special,
            transition = self.DFA146_transition
            )
        self.dfa156 = self.DFA156(
            self, 156,
            eot = self.DFA156_eot,
            eof = self.DFA156_eof,
            min = self.DFA156_min,
            max = self.DFA156_max,
            accept = self.DFA156_accept,
            special = self.DFA156_special,
            transition = self.DFA156_transition
            )
        self.dfa161 = self.DFA161(
            self, 161,
            eot = self.DFA161_eot,
            eof = self.DFA161_eof,
            min = self.DFA161_min,
            max = self.DFA161_max,
            accept = self.DFA161_accept,
            special = self.DFA161_special,
            transition = self.DFA161_transition
            )
        self.dfa164 = self.DFA164(
            self, 164,
            eot = self.DFA164_eot,
            eof = self.DFA164_eof,
            min = self.DFA164_min,
            max = self.DFA164_max,
            accept = self.DFA164_accept,
            special = self.DFA164_special,
            transition = self.DFA164_transition
            )
        self.dfa167 = self.DFA167(
            self, 167,
            eot = self.DFA167_eot,
            eof = self.DFA167_eof,
            min = self.DFA167_min,
            max = self.DFA167_max,
            accept = self.DFA167_accept,
            special = self.DFA167_special,
            transition = self.DFA167_transition
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
        self.dfa173 = self.DFA173(
            self, 173,
            eot = self.DFA173_eot,
            eof = self.DFA173_eof,
            min = self.DFA173_min,
            max = self.DFA173_max,
            accept = self.DFA173_accept,
            special = self.DFA173_special,
            transition = self.DFA173_transition
            )
        self.dfa176 = self.DFA176(
            self, 176,
            eot = self.DFA176_eot,
            eof = self.DFA176_eof,
            min = self.DFA176_min,
            max = self.DFA176_max,
            accept = self.DFA176_accept,
            special = self.DFA176_special,
            transition = self.DFA176_transition
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
        self.dfa182 = self.DFA182(
            self, 182,
            eot = self.DFA182_eot,
            eof = self.DFA182_eof,
            min = self.DFA182_min,
            max = self.DFA182_max,
            accept = self.DFA182_accept,
            special = self.DFA182_special,
            transition = self.DFA182_transition
            )
        self.dfa185 = self.DFA185(
            self, 185,
            eot = self.DFA185_eot,
            eof = self.DFA185_eof,
            min = self.DFA185_min,
            max = self.DFA185_max,
            accept = self.DFA185_accept,
            special = self.DFA185_special,
            transition = self.DFA185_transition
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
        self.dfa223 = self.DFA223(
            self, 223,
            eot = self.DFA223_eot,
            eof = self.DFA223_eof,
            min = self.DFA223_min,
            max = self.DFA223_max,
            accept = self.DFA223_accept,
            special = self.DFA223_special,
            transition = self.DFA223_transition
            )
        self.dfa222 = self.DFA222(
            self, 222,
            eot = self.DFA222_eot,
            eof = self.DFA222_eof,
            min = self.DFA222_min,
            max = self.DFA222_max,
            accept = self.DFA222_accept,
            special = self.DFA222_special,
            transition = self.DFA222_transition
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
        self.dfa241 = self.DFA241(
            self, 241,
            eot = self.DFA241_eot,
            eof = self.DFA241_eof,
            min = self.DFA241_min,
            max = self.DFA241_max,
            accept = self.DFA241_accept,
            special = self.DFA241_special,
            transition = self.DFA241_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class program_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start program
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:24:1: program : ( LT )* sourceElements ( LT )* EOF ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:25:2: ( ( LT )* sourceElements ( LT )* EOF )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:25:4: ( LT )* sourceElements ( LT )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:25:6: ( LT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == LT) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT1 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program64)
                        if self.failed:
                            return retval


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_sourceElements_in_program68)
                sourceElements2 = self.sourceElements()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElements2.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:25:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT3 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program70)
                        if self.failed:
                            return retval


                    else:
                        break #loop2


                EOF4 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_program74)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:2: ( sourceElement ( ( LT )* sourceElement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:4: sourceElement ( ( LT )* sourceElement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_sourceElement_in_sourceElements87)
                sourceElement5 = self.sourceElement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElement5.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    LA4 = self.input.LA(1)
                    if LA4 == LT:
                        LA4_1 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 38:
                        LA4_4 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 42:
                        LA4_5 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 44 or LA4 == 45:
                        LA4_6 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 46:
                        LA4_7 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 112:
                        LA4_8 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == Identifier or LA4 == 53 or LA4 == 113 or LA4 == 114:
                        LA4_9 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == StringLiteral or LA4 == NumericLiteral or LA4 == RegularExpressionLiteral or LA4 == 115 or LA4 == 116 or LA4 == 117:
                        LA4_10 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 68:
                        LA4_11 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 39:
                        LA4_12 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 67:
                        LA4_13 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 100 or LA4 == 101 or LA4 == 105 or LA4 == 106 or LA4 == 107 or LA4 == 108 or LA4 == 109 or LA4 == 110 or LA4 == 111:
                        LA4_14 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 48:
                        LA4_15 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 50:
                        LA4_16 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 51:
                        LA4_17 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 52:
                        LA4_18 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 55:
                        LA4_19 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 56:
                        LA4_20 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 57:
                        LA4_21 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 58:
                        LA4_22 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 60:
                        LA4_23 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 63:
                        LA4_24 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 64:
                        LA4_25 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1



                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:19: ( LT )* sourceElement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:21: ( LT )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if (LA3_0 == LT) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT6 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements90)
                                if self.failed:
                                    return retval


                            else:
                                break #loop3


                        self.following.append(self.FOLLOW_sourceElement_in_sourceElements94)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:1: sourceElement : ( functionDeclaration | statement );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:2: ( functionDeclaration | statement )
                alt5 = 2
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: functionDeclaration
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionDeclaration_in_sourceElement108)
                    functionDeclaration8 = self.functionDeclaration()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:4: statement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statement_in_sourceElement113)
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

    class functionDeclaration_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start functionDeclaration
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:1: functionDeclaration : 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) ;
    def functionDeclaration(self, ):

        retval = self.functionDeclaration_return()
        retval.start = self.input.LT(1)
        functionDeclaration_StartIndex = self.input.index()
        root_0 = None

        string_literal10 = None
        LT11 = None
        LT13 = None
        LT15 = None
        identifier12 = None

        formalParameterList14 = None

        functionBody16 = None


        string_literal10_tree = None
        LT11_tree = None
        LT13_tree = None
        LT15_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self.adaptor, "rule functionBody")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody
                string_literal10 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_functionDeclaration126)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_38.add(string_literal10)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:15: ( LT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LT) :
                        alt6 = 1


                    if alt6 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT11 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration128)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT11)


                    else:
                        break #loop6


                self.following.append(self.FOLLOW_identifier_in_functionDeclaration131)
                identifier12 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier12.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:30: ( LT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == LT) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT13 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration133)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT13)


                    else:
                        break #loop7


                self.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration136)
                formalParameterList14 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList14.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:54: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT15 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration138)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT15)


                    else:
                        break #loop8


                self.following.append(self.FOLLOW_functionBody_in_functionDeclaration141)
                functionBody16 = self.functionBody()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_functionBody.add(functionBody16.tree)
                # AST Rewrite
                # elements: identifier, functionBody, formalParameterList
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
                    # 40:3: -> ^( FUNC identifier formalParameterList functionBody )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:40:6: ^( FUNC identifier formalParameterList functionBody )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    self.adaptor.addChild(root_1, stream_formalParameterList.next())
                    self.adaptor.addChild(root_1, stream_functionBody.next())

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
                self.memoize(self.input, 4, functionDeclaration_StartIndex)

            pass

        return retval

    # $ANTLR end functionDeclaration

    class functionExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start functionExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) | 'function' ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC ANONYMOUS formalParameterList functionBody ) );
    def functionExpression(self, ):

        retval = self.functionExpression_return()
        retval.start = self.input.LT(1)
        functionExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal17 = None
        LT18 = None
        LT20 = None
        LT22 = None
        string_literal24 = None
        LT25 = None
        LT27 = None
        identifier19 = None

        formalParameterList21 = None

        functionBody23 = None

        formalParameterList26 = None

        functionBody28 = None


        string_literal17_tree = None
        LT18_tree = None
        LT20_tree = None
        LT22_tree = None
        string_literal24_tree = None
        LT25_tree = None
        LT27_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_38 = RewriteRuleTokenStream(self.adaptor, "token 38")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self.adaptor, "rule functionBody")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) | 'function' ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC ANONYMOUS formalParameterList functionBody ) )
                alt14 = 2
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody
                    string_literal17 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_functionExpression167)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_38.add(string_literal17)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:15: ( LT )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == LT) :
                            alt9 = 1


                        if alt9 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT18 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression169)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT18)


                        else:
                            break #loop9


                    self.following.append(self.FOLLOW_identifier_in_functionExpression172)
                    identifier19 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier19.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:30: ( LT )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == LT) :
                            alt10 = 1


                        if alt10 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT20 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression174)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT20)


                        else:
                            break #loop10


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression177)
                    formalParameterList21 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList21.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:54: ( LT )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == LT) :
                            alt11 = 1


                        if alt11 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT22 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression179)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT22)


                        else:
                            break #loop11


                    self.following.append(self.FOLLOW_functionBody_in_functionExpression182)
                    functionBody23 = self.functionBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_functionBody.add(functionBody23.tree)
                    # AST Rewrite
                    # elements: functionBody, identifier, formalParameterList
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
                        # 45:3: -> ^( FUNC identifier formalParameterList functionBody )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:6: ^( FUNC identifier formalParameterList functionBody )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_functionBody.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt14 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:46:4: 'function' ( LT )* formalParameterList ( LT )* functionBody
                    string_literal24 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_functionExpression201)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_38.add(string_literal24)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:46:15: ( LT )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == LT) :
                            alt12 = 1


                        if alt12 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT25 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression203)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT25)


                        else:
                            break #loop12


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression206)
                    formalParameterList26 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList26.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:46:39: ( LT )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == LT) :
                            alt13 = 1


                        if alt13 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT27 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression208)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT27)


                        else:
                            break #loop13


                    self.following.append(self.FOLLOW_functionBody_in_functionExpression211)
                    functionBody28 = self.functionBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_functionBody.add(functionBody28.tree)
                    # AST Rewrite
                    # elements: formalParameterList, functionBody
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
                        # 47:3: -> ^( FUNC ANONYMOUS formalParameterList functionBody )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:6: ^( FUNC ANONYMOUS formalParameterList functionBody )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, self.adaptor.createFromType(ANONYMOUS, "ANONYMOUS"))
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_functionBody.next())

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
                self.memoize(self.input, 5, functionExpression_StartIndex)

            pass

        return retval

    # $ANTLR end functionExpression

    class formalParameterList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start formalParameterList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:50:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal29 = None
        LT30 = None
        LT32 = None
        char_literal33 = None
        LT34 = None
        LT36 = None
        char_literal37 = None
        identifier31 = None

        identifier35 = None


        char_literal29_tree = None
        LT30_tree = None
        LT32_tree = None
        char_literal33_tree = None
        LT34_tree = None
        LT36_tree = None
        char_literal37_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal29 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_formalParameterList237)
                if self.failed:
                    return retval

                char_literal29_tree = self.adaptor.createWithPayload(char_literal29)
                self.adaptor.addChild(root_0, char_literal29_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt19 = 2
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:11: ( LT )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == LT) :
                            alt15 = 1


                        if alt15 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT30 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList240)
                            if self.failed:
                                return retval


                        else:
                            break #loop15


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList244)
                    identifier31 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier31.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:25: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop18
                        alt18 = 2
                        alt18 = self.dfa18.predict(self.input)
                        if alt18 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:26: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:28: ( LT )*
                            while True: #loop16
                                alt16 = 2
                                LA16_0 = self.input.LA(1)

                                if (LA16_0 == LT) :
                                    alt16 = 1


                                if alt16 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT32 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList247)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop16


                            char_literal33 = self.input.LT(1)
                            self.match(self.input, 40, self.FOLLOW_40_in_formalParameterList251)
                            if self.failed:
                                return retval

                            char_literal33_tree = self.adaptor.createWithPayload(char_literal33)
                            self.adaptor.addChild(root_0, char_literal33_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:37: ( LT )*
                            while True: #loop17
                                alt17 = 2
                                LA17_0 = self.input.LA(1)

                                if (LA17_0 == LT) :
                                    alt17 = 1


                                if alt17 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT34 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList253)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop17


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList257)
                            identifier35 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, identifier35.tree)


                        else:
                            break #loop18





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:57: ( LT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == LT) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT36 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList263)
                        if self.failed:
                            return retval


                    else:
                        break #loop20


                char_literal37 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_formalParameterList267)
                if self.failed:
                    return retval

                char_literal37_tree = self.adaptor.createWithPayload(char_literal37)
                self.adaptor.addChild(root_0, char_literal37_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 6, formalParameterList_StartIndex)

            pass

        return retval

    # $ANTLR end formalParameterList

    class functionBody_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start functionBody
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:54:1: functionBody : '{' ( LT )* ( sourceElements )* ( LT )* '}' ;
    def functionBody(self, ):

        retval = self.functionBody_return()
        retval.start = self.input.LT(1)
        functionBody_StartIndex = self.input.index()
        root_0 = None

        char_literal38 = None
        LT39 = None
        LT41 = None
        char_literal42 = None
        sourceElements40 = None


        char_literal38_tree = None
        LT39_tree = None
        LT41_tree = None
        char_literal42_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:2: ( '{' ( LT )* ( sourceElements )* ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:4: '{' ( LT )* ( sourceElements )* ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal38 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_functionBody278)
                if self.failed:
                    return retval

                char_literal38_tree = self.adaptor.createWithPayload(char_literal38)
                self.adaptor.addChild(root_0, char_literal38_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:10: ( LT )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == LT) :
                        LA21_2 = self.input.LA(2)

                        if (self.synpred21()) :
                            alt21 = 1




                    if alt21 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT39 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionBody280)
                        if self.failed:
                            return retval


                    else:
                        break #loop21


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:13: ( sourceElements )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((StringLiteral <= LA22_0 <= Identifier) or (38 <= LA22_0 <= 39) or LA22_0 == 42 or (44 <= LA22_0 <= 46) or LA22_0 == 48 or (50 <= LA22_0 <= 53) or (55 <= LA22_0 <= 58) or LA22_0 == 60 or (63 <= LA22_0 <= 64) or (67 <= LA22_0 <= 68) or (100 <= LA22_0 <= 101) or (105 <= LA22_0 <= 117)) :
                        alt22 = 1


                    if alt22 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: sourceElements
                        self.following.append(self.FOLLOW_sourceElements_in_functionBody284)
                        sourceElements40 = self.sourceElements()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, sourceElements40.tree)


                    else:
                        break #loop22


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:31: ( LT )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == LT) :
                        alt23 = 1


                    if alt23 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT41 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionBody287)
                        if self.failed:
                            return retval


                    else:
                        break #loop23


                char_literal42 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_functionBody291)
                if self.failed:
                    return retval

                char_literal42_tree = self.adaptor.createWithPayload(char_literal42)
                self.adaptor.addChild(root_0, char_literal42_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 7, functionBody_StartIndex)

            pass

        return retval

    # $ANTLR end functionBody

    class statement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        statementBlock43 = None

        variableStatement44 = None

        emptyStatement45 = None

        expressionStatement46 = None

        ifStatement47 = None

        iterationStatement48 = None

        continueStatement49 = None

        breakStatement50 = None

        returnStatement51 = None

        withStatement52 = None

        labelledStatement53 = None

        switchStatement54 = None

        throwStatement55 = None

        tryStatement56 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement )
                alt24 = 14
                LA24 = self.input.LA(1)
                if LA24 == 42:
                    LA24_1 = self.input.LA(2)

                    if (self.synpred24()) :
                        alt24 = 1
                    elif (self.synpred27()) :
                        alt24 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("59:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 24, 1, self.input)

                        raise nvae

                elif LA24 == 44 or LA24 == 45:
                    alt24 = 2
                elif LA24 == 46:
                    alt24 = 3
                elif LA24 == StringLiteral or LA24 == NumericLiteral or LA24 == RegularExpressionLiteral or LA24 == 38 or LA24 == 39 or LA24 == 67 or LA24 == 68 or LA24 == 100 or LA24 == 101 or LA24 == 105 or LA24 == 106 or LA24 == 107 or LA24 == 108 or LA24 == 109 or LA24 == 110 or LA24 == 111 or LA24 == 112 or LA24 == 115 or LA24 == 116 or LA24 == 117:
                    alt24 = 4
                elif LA24 == Identifier or LA24 == 53 or LA24 == 113 or LA24 == 114:
                    LA24_5 = self.input.LA(2)

                    if (self.synpred27()) :
                        alt24 = 4
                    elif (self.synpred34()) :
                        alt24 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("59:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 24, 5, self.input)

                        raise nvae

                elif LA24 == 48:
                    alt24 = 5
                elif LA24 == 50 or LA24 == 51 or LA24 == 52:
                    alt24 = 6
                elif LA24 == 55:
                    alt24 = 7
                elif LA24 == 56:
                    alt24 = 8
                elif LA24 == 57:
                    alt24 = 9
                elif LA24 == 58:
                    alt24 = 10
                elif LA24 == 60:
                    alt24 = 12
                elif LA24 == 63:
                    alt24 = 13
                elif LA24 == 64:
                    alt24 = 14
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("59:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement303)
                    statementBlock43 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock43.tree)


                elif alt24 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement308)
                    variableStatement44 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement44.tree)


                elif alt24 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement313)
                    emptyStatement45 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement45.tree)


                elif alt24 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:63:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement318)
                    expressionStatement46 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement46.tree)


                elif alt24 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement323)
                    ifStatement47 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement47.tree)


                elif alt24 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:65:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement328)
                    iterationStatement48 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement48.tree)


                elif alt24 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:66:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement333)
                    continueStatement49 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement49.tree)


                elif alt24 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement338)
                    breakStatement50 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement50.tree)


                elif alt24 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:68:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement343)
                    returnStatement51 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement51.tree)


                elif alt24 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement348)
                    withStatement52 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement52.tree)


                elif alt24 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:70:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement353)
                    labelledStatement53 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement53.tree)


                elif alt24 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:71:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement358)
                    switchStatement54 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement54.tree)


                elif alt24 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:72:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement363)
                    throwStatement55 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement55.tree)


                elif alt24 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement368)
                    tryStatement56 = self.tryStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, tryStatement56.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 8, statement_StartIndex)

            pass

        return retval

    # $ANTLR end statement

    class statementBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:76:1: statementBlock : '{' ( LT )* ( statementList )? ( LT )* '}' ;
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal57 = None
        LT58 = None
        LT60 = None
        char_literal61 = None
        statementList59 = None


        char_literal57_tree = None
        LT58_tree = None
        LT60_tree = None
        char_literal61_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal57 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_statementBlock380)
                if self.failed:
                    return retval

                char_literal57_tree = self.adaptor.createWithPayload(char_literal57)
                self.adaptor.addChild(root_0, char_literal57_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:10: ( LT )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LT) :
                        LA25_2 = self.input.LA(2)

                        if (self.synpred37()) :
                            alt25 = 1




                    if alt25 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT58 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock382)
                        if self.failed:
                            return retval


                    else:
                        break #loop25


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:13: ( statementList )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if ((StringLiteral <= LA26_0 <= Identifier) or (38 <= LA26_0 <= 39) or LA26_0 == 42 or (44 <= LA26_0 <= 46) or LA26_0 == 48 or (50 <= LA26_0 <= 53) or (55 <= LA26_0 <= 58) or LA26_0 == 60 or (63 <= LA26_0 <= 64) or (67 <= LA26_0 <= 68) or (100 <= LA26_0 <= 101) or (105 <= LA26_0 <= 117)) :
                    alt26 = 1
                if alt26 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_statementBlock386)
                    statementList59 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList59.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:30: ( LT )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == LT) :
                        alt27 = 1


                    if alt27 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT60 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock389)
                        if self.failed:
                            return retval


                    else:
                        break #loop27


                char_literal61 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_statementBlock393)
                if self.failed:
                    return retval

                char_literal61_tree = self.adaptor.createWithPayload(char_literal61)
                self.adaptor.addChild(root_0, char_literal61_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 9, statementBlock_StartIndex)

            pass

        return retval

    # $ANTLR end statementBlock

    class statementList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:80:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT63 = None
        statement62 = None

        statement64 = None


        LT63_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList405)
                statement62 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement62.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:14: ( ( LT )* statement )*
                while True: #loop29
                    alt29 = 2
                    alt29 = self.dfa29.predict(self.input)
                    if alt29 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:17: ( LT )*
                        while True: #loop28
                            alt28 = 2
                            LA28_0 = self.input.LA(1)

                            if (LA28_0 == LT) :
                                alt28 = 1


                            if alt28 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT63 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList408)
                                if self.failed:
                                    return retval


                            else:
                                break #loop28


                        self.following.append(self.FOLLOW_statement_in_statementList412)
                        statement64 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement64.tree)


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
            if self.backtracking > 0:
                self.memoize(self.input, 10, statementList_StartIndex)

            pass

        return retval

    # $ANTLR end statementList

    class variableStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:84:1: variableStatement : ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        set65 = None
        LT66 = None
        set68 = None
        variableDeclarationList67 = None


        set65_tree = None
        LT66_tree = None
        set68_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:2: ( ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:4: ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' )
                root_0 = self.adaptor.nil()

                set65 = self.input.LT(1)
                if (44 <= self.input.LA(1) <= 45):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set65))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_variableStatement426
                        )
                    raise mse


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:22: ( LT )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == LT) :
                        alt30 = 1


                    if alt30 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT66 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement432)
                        if self.failed:
                            return retval


                    else:
                        break #loop30


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement436)
                variableDeclarationList67 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationList67.tree)
                set68 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_variableStatement438
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
                self.memoize(self.input, 11, variableStatement_StartIndex)

            pass

        return retval

    # $ANTLR end variableStatement

    class variableDeclarationList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:88:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT70 = None
        char_literal71 = None
        LT72 = None
        variableDeclaration69 = None

        variableDeclaration73 = None


        LT70_tree = None
        char_literal71_tree = None
        LT72_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList456)
                variableDeclaration69 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration69.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop33
                    alt33 = 2
                    alt33 = self.dfa33.predict(self.input)
                    if alt33 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:27: ( LT )*
                        while True: #loop31
                            alt31 = 2
                            LA31_0 = self.input.LA(1)

                            if (LA31_0 == LT) :
                                alt31 = 1


                            if alt31 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT70 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList459)
                                if self.failed:
                                    return retval


                            else:
                                break #loop31


                        char_literal71 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_variableDeclarationList463)
                        if self.failed:
                            return retval

                        char_literal71_tree = self.adaptor.createWithPayload(char_literal71)
                        self.adaptor.addChild(root_0, char_literal71_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:36: ( LT )*
                        while True: #loop32
                            alt32 = 2
                            LA32_0 = self.input.LA(1)

                            if (LA32_0 == LT) :
                                alt32 = 1


                            if alt32 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT72 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList465)
                                if self.failed:
                                    return retval


                            else:
                                break #loop32


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList469)
                        variableDeclaration73 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration73.tree)


                    else:
                        break #loop33





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 12, variableDeclarationList_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationList

    class variableDeclarationListNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationListNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:92:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT75 = None
        char_literal76 = None
        LT77 = None
        variableDeclarationNoIn74 = None

        variableDeclarationNoIn78 = None


        LT75_tree = None
        char_literal76_tree = None
        LT77_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn483)
                variableDeclarationNoIn74 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn74.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop36
                    alt36 = 2
                    alt36 = self.dfa36.predict(self.input)
                    if alt36 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:31: ( LT )*
                        while True: #loop34
                            alt34 = 2
                            LA34_0 = self.input.LA(1)

                            if (LA34_0 == LT) :
                                alt34 = 1


                            if alt34 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT75 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn486)
                                if self.failed:
                                    return retval


                            else:
                                break #loop34


                        char_literal76 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_variableDeclarationListNoIn490)
                        if self.failed:
                            return retval

                        char_literal76_tree = self.adaptor.createWithPayload(char_literal76)
                        self.adaptor.addChild(root_0, char_literal76_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:40: ( LT )*
                        while True: #loop35
                            alt35 = 2
                            LA35_0 = self.input.LA(1)

                            if (LA35_0 == LT) :
                                alt35 = 1


                            if alt35 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT77 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn492)
                                if self.failed:
                                    return retval


                            else:
                                break #loop35


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn496)
                        variableDeclarationNoIn78 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn78.tree)


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
            if self.backtracking > 0:
                self.memoize(self.input, 13, variableDeclarationListNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationListNoIn

    class variableDeclaration_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclaration
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:96:1: variableDeclaration : identifier ( ( LT )* initialiser )? ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT80 = None
        identifier79 = None

        initialiser81 = None


        LT80_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:2: ( identifier ( ( LT )* initialiser )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:4: identifier ( ( LT )* initialiser )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_variableDeclaration510)
                identifier79 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier79.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:15: ( ( LT )* initialiser )?
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:16: ( LT )* initialiser
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:18: ( LT )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LT) :
                            alt37 = 1


                        if alt37 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT80 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration513)
                            if self.failed:
                                return retval


                        else:
                            break #loop37


                    self.following.append(self.FOLLOW_initialiser_in_variableDeclaration517)
                    initialiser81 = self.initialiser()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, initialiser81.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 14, variableDeclaration_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclaration

    class variableDeclarationNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:100:1: variableDeclarationNoIn : identifier ( ( LT )* initialiserNoIn )? ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT83 = None
        identifier82 = None

        initialiserNoIn84 = None


        LT83_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:2: ( identifier ( ( LT )* initialiserNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:4: identifier ( ( LT )* initialiserNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn531)
                identifier82 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier82.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:15: ( ( LT )* initialiserNoIn )?
                alt40 = 2
                alt40 = self.dfa40.predict(self.input)
                if alt40 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:16: ( LT )* initialiserNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:18: ( LT )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == LT) :
                            alt39 = 1


                        if alt39 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT83 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn534)
                            if self.failed:
                                return retval


                        else:
                            break #loop39


                    self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn538)
                    initialiserNoIn84 = self.initialiserNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, initialiserNoIn84.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 15, variableDeclarationNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationNoIn

    class initialiser_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiser
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:1: initialiser : '=' ( LT )* assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal85 = None
        LT86 = None
        assignmentExpression87 = None


        char_literal85_tree = None
        LT86_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:2: ( '=' ( LT )* assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:4: '=' ( LT )* assignmentExpression
                root_0 = self.adaptor.nil()

                char_literal85 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_initialiser552)
                if self.failed:
                    return retval

                char_literal85_tree = self.adaptor.createWithPayload(char_literal85)
                self.adaptor.addChild(root_0, char_literal85_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:10: ( LT )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == LT) :
                        alt41 = 1


                    if alt41 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT86 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser554)
                        if self.failed:
                            return retval


                    else:
                        break #loop41


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser558)
                assignmentExpression87 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression87.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 16, initialiser_StartIndex)

            pass

        return retval

    # $ANTLR end initialiser

    class initialiserNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiserNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:108:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal88 = None
        LT89 = None
        assignmentExpressionNoIn90 = None


        char_literal88_tree = None
        LT89_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:2: ( '=' ( LT )* assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:4: '=' ( LT )* assignmentExpressionNoIn
                root_0 = self.adaptor.nil()

                char_literal88 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_initialiserNoIn570)
                if self.failed:
                    return retval

                char_literal88_tree = self.adaptor.createWithPayload(char_literal88)
                self.adaptor.addChild(root_0, char_literal88_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:10: ( LT )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == LT) :
                        alt42 = 1


                    if alt42 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT89 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn572)
                        if self.failed:
                            return retval


                    else:
                        break #loop42


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn576)
                assignmentExpressionNoIn90 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn90.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 17, initialiserNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end initialiserNoIn

    class emptyStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start emptyStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:112:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal91 = None

        char_literal91_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:113:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:113:4: ';'
                root_0 = self.adaptor.nil()

                char_literal91 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_emptyStatement588)
                if self.failed:
                    return retval

                char_literal91_tree = self.adaptor.createWithPayload(char_literal91)
                self.adaptor.addChild(root_0, char_literal91_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 18, emptyStatement_StartIndex)

            pass

        return retval

    # $ANTLR end emptyStatement

    class expressionStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:116:1: expressionStatement : expression ( LT | ';' ) ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        set93 = None
        expression92 = None


        set93_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement600)
                expression92 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression92.tree)
                set93 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_expressionStatement602
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
                self.memoize(self.input, 19, expressionStatement_StartIndex)

            pass

        return retval

    # $ANTLR end expressionStatement

    class ifStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start ifStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:120:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal94 = None
        LT95 = None
        char_literal96 = None
        LT97 = None
        LT99 = None
        char_literal100 = None
        LT101 = None
        LT103 = None
        string_literal104 = None
        LT105 = None
        expression98 = None

        statement102 = None

        statement106 = None


        string_literal94_tree = None
        LT95_tree = None
        char_literal96_tree = None
        LT97_tree = None
        LT99_tree = None
        char_literal100_tree = None
        LT101_tree = None
        LT103_tree = None
        string_literal104_tree = None
        LT105_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal94 = self.input.LT(1)
                self.match(self.input, 48, self.FOLLOW_48_in_ifStatement621)
                if self.failed:
                    return retval

                string_literal94_tree = self.adaptor.createWithPayload(string_literal94)
                self.adaptor.addChild(root_0, string_literal94_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:11: ( LT )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == LT) :
                        alt43 = 1


                    if alt43 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT95 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement623)
                        if self.failed:
                            return retval


                    else:
                        break #loop43


                char_literal96 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_ifStatement627)
                if self.failed:
                    return retval

                char_literal96_tree = self.adaptor.createWithPayload(char_literal96)
                self.adaptor.addChild(root_0, char_literal96_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:20: ( LT )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == LT) :
                        alt44 = 1


                    if alt44 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT97 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement629)
                        if self.failed:
                            return retval


                    else:
                        break #loop44


                self.following.append(self.FOLLOW_expression_in_ifStatement633)
                expression98 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression98.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:36: ( LT )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT99 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement635)
                        if self.failed:
                            return retval


                    else:
                        break #loop45


                char_literal100 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_ifStatement639)
                if self.failed:
                    return retval

                char_literal100_tree = self.adaptor.createWithPayload(char_literal100)
                self.adaptor.addChild(root_0, char_literal100_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:45: ( LT )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == LT) :
                        alt46 = 1


                    if alt46 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT101 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement641)
                        if self.failed:
                            return retval


                    else:
                        break #loop46


                self.following.append(self.FOLLOW_statement_in_ifStatement645)
                statement102 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement102.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:58: ( ( LT )* 'else' ( LT )* statement )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == LT) :
                    LA49_1 = self.input.LA(2)

                    if (self.synpred64()) :
                        alt49 = 1
                elif (LA49_0 == 49) :
                    LA49_2 = self.input.LA(2)

                    if (self.synpred64()) :
                        alt49 = 1
                if alt49 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:61: ( LT )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == LT) :
                            alt47 = 1


                        if alt47 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT103 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement648)
                            if self.failed:
                                return retval


                        else:
                            break #loop47


                    string_literal104 = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_ifStatement652)
                    if self.failed:
                        return retval

                    string_literal104_tree = self.adaptor.createWithPayload(string_literal104)
                    self.adaptor.addChild(root_0, string_literal104_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:73: ( LT )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == LT) :
                            alt48 = 1


                        if alt48 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT105 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement654)
                            if self.failed:
                                return retval


                        else:
                            break #loop48


                    self.following.append(self.FOLLOW_statement_in_ifStatement658)
                    statement106 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement106.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 20, ifStatement_StartIndex)

            pass

        return retval

    # $ANTLR end ifStatement

    class iterationStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start iterationStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:124:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement107 = None

        whileStatement108 = None

        forStatement109 = None

        forInStatement110 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:125:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt50 = 4
                LA50 = self.input.LA(1)
                if LA50 == 50:
                    alt50 = 1
                elif LA50 == 51:
                    alt50 = 2
                elif LA50 == 52:
                    LA50_3 = self.input.LA(2)

                    if (self.synpred67()) :
                        alt50 = 3
                    elif (True) :
                        alt50 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("124:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 50, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("124:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 50, 0, self.input)

                    raise nvae

                if alt50 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:125:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement672)
                    doWhileStatement107 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement107.tree)


                elif alt50 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:126:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement677)
                    whileStatement108 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement108.tree)


                elif alt50 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement682)
                    forStatement109 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement109.tree)


                elif alt50 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement687)
                    forInStatement110 = self.forInStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forInStatement110.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 21, iterationStatement_StartIndex)

            pass

        return retval

    # $ANTLR end iterationStatement

    class doWhileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start doWhileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal111 = None
        LT112 = None
        LT114 = None
        string_literal115 = None
        LT116 = None
        char_literal117 = None
        char_literal119 = None
        set120 = None
        statement113 = None

        expression118 = None


        string_literal111_tree = None
        LT112_tree = None
        LT114_tree = None
        string_literal115_tree = None
        LT116_tree = None
        char_literal117_tree = None
        char_literal119_tree = None
        set120_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal111 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_doWhileStatement699)
                if self.failed:
                    return retval

                string_literal111_tree = self.adaptor.createWithPayload(string_literal111)
                self.adaptor.addChild(root_0, string_literal111_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:11: ( LT )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == LT) :
                        alt51 = 1


                    if alt51 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT112 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement701)
                        if self.failed:
                            return retval


                    else:
                        break #loop51


                self.following.append(self.FOLLOW_statement_in_doWhileStatement705)
                statement113 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement113.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:26: ( LT )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == LT) :
                        alt52 = 1


                    if alt52 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT114 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement707)
                        if self.failed:
                            return retval


                    else:
                        break #loop52


                string_literal115 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_doWhileStatement711)
                if self.failed:
                    return retval

                string_literal115_tree = self.adaptor.createWithPayload(string_literal115)
                self.adaptor.addChild(root_0, string_literal115_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:39: ( LT )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == LT) :
                        alt53 = 1


                    if alt53 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT116 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement713)
                        if self.failed:
                            return retval


                    else:
                        break #loop53


                char_literal117 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_doWhileStatement717)
                if self.failed:
                    return retval

                char_literal117_tree = self.adaptor.createWithPayload(char_literal117)
                self.adaptor.addChild(root_0, char_literal117_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement719)
                expression118 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression118.tree)
                char_literal119 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_doWhileStatement721)
                if self.failed:
                    return retval

                char_literal119_tree = self.adaptor.createWithPayload(char_literal119)
                self.adaptor.addChild(root_0, char_literal119_tree)

                set120 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement723
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
                self.memoize(self.input, 22, doWhileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end doWhileStatement

    class whileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start whileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:135:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal121 = None
        LT122 = None
        char_literal123 = None
        LT124 = None
        LT126 = None
        char_literal127 = None
        LT128 = None
        expression125 = None

        statement129 = None


        string_literal121_tree = None
        LT122_tree = None
        char_literal123_tree = None
        LT124_tree = None
        LT126_tree = None
        char_literal127_tree = None
        LT128_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal121 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_whileStatement742)
                if self.failed:
                    return retval

                string_literal121_tree = self.adaptor.createWithPayload(string_literal121)
                self.adaptor.addChild(root_0, string_literal121_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:14: ( LT )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == LT) :
                        alt54 = 1


                    if alt54 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT122 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement744)
                        if self.failed:
                            return retval


                    else:
                        break #loop54


                char_literal123 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_whileStatement748)
                if self.failed:
                    return retval

                char_literal123_tree = self.adaptor.createWithPayload(char_literal123)
                self.adaptor.addChild(root_0, char_literal123_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:23: ( LT )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == LT) :
                        alt55 = 1


                    if alt55 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT124 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement750)
                        if self.failed:
                            return retval


                    else:
                        break #loop55


                self.following.append(self.FOLLOW_expression_in_whileStatement754)
                expression125 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression125.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:39: ( LT )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == LT) :
                        alt56 = 1


                    if alt56 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT126 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement756)
                        if self.failed:
                            return retval


                    else:
                        break #loop56


                char_literal127 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_whileStatement760)
                if self.failed:
                    return retval

                char_literal127_tree = self.adaptor.createWithPayload(char_literal127)
                self.adaptor.addChild(root_0, char_literal127_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:48: ( LT )*
                while True: #loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == LT) :
                        alt57 = 1


                    if alt57 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT128 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement762)
                        if self.failed:
                            return retval


                    else:
                        break #loop57


                self.following.append(self.FOLLOW_statement_in_whileStatement766)
                statement129 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement129.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 23, whileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end whileStatement

    class forStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:139:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal130 = None
        LT131 = None
        char_literal132 = None
        LT133 = None
        LT135 = None
        char_literal136 = None
        LT137 = None
        LT139 = None
        char_literal140 = None
        LT141 = None
        LT143 = None
        char_literal144 = None
        LT145 = None
        forStatementInitialiserPart134 = None

        expression138 = None

        expression142 = None

        statement146 = None


        string_literal130_tree = None
        LT131_tree = None
        char_literal132_tree = None
        LT133_tree = None
        LT135_tree = None
        char_literal136_tree = None
        LT137_tree = None
        LT139_tree = None
        char_literal140_tree = None
        LT141_tree = None
        LT143_tree = None
        char_literal144_tree = None
        LT145_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal130 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_forStatement778)
                if self.failed:
                    return retval

                string_literal130_tree = self.adaptor.createWithPayload(string_literal130)
                self.adaptor.addChild(root_0, string_literal130_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:12: ( LT )*
                while True: #loop58
                    alt58 = 2
                    LA58_0 = self.input.LA(1)

                    if (LA58_0 == LT) :
                        alt58 = 1


                    if alt58 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT131 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement780)
                        if self.failed:
                            return retval


                    else:
                        break #loop58


                char_literal132 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_forStatement784)
                if self.failed:
                    return retval

                char_literal132_tree = self.adaptor.createWithPayload(char_literal132)
                self.adaptor.addChild(root_0, char_literal132_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:19: ( ( LT )* forStatementInitialiserPart )?
                alt60 = 2
                alt60 = self.dfa60.predict(self.input)
                if alt60 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:22: ( LT )*
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == LT) :
                            alt59 = 1


                        if alt59 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT133 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement787)
                            if self.failed:
                                return retval


                        else:
                            break #loop59


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement791)
                    forStatementInitialiserPart134 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart134.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:57: ( LT )*
                while True: #loop61
                    alt61 = 2
                    LA61_0 = self.input.LA(1)

                    if (LA61_0 == LT) :
                        alt61 = 1


                    if alt61 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT135 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement795)
                        if self.failed:
                            return retval


                    else:
                        break #loop61


                char_literal136 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_forStatement799)
                if self.failed:
                    return retval

                char_literal136_tree = self.adaptor.createWithPayload(char_literal136)
                self.adaptor.addChild(root_0, char_literal136_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:64: ( ( LT )* expression )?
                alt63 = 2
                alt63 = self.dfa63.predict(self.input)
                if alt63 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:67: ( LT )*
                    while True: #loop62
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if (LA62_0 == LT) :
                            alt62 = 1


                        if alt62 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT137 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement802)
                            if self.failed:
                                return retval


                        else:
                            break #loop62


                    self.following.append(self.FOLLOW_expression_in_forStatement806)
                    expression138 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression138.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:85: ( LT )*
                while True: #loop64
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if (LA64_0 == LT) :
                        alt64 = 1


                    if alt64 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT139 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement810)
                        if self.failed:
                            return retval


                    else:
                        break #loop64


                char_literal140 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_forStatement814)
                if self.failed:
                    return retval

                char_literal140_tree = self.adaptor.createWithPayload(char_literal140)
                self.adaptor.addChild(root_0, char_literal140_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:92: ( ( LT )* expression )?
                alt66 = 2
                alt66 = self.dfa66.predict(self.input)
                if alt66 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:95: ( LT )*
                    while True: #loop65
                        alt65 = 2
                        LA65_0 = self.input.LA(1)

                        if (LA65_0 == LT) :
                            alt65 = 1


                        if alt65 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT141 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement817)
                            if self.failed:
                                return retval


                        else:
                            break #loop65


                    self.following.append(self.FOLLOW_expression_in_forStatement821)
                    expression142 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression142.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:113: ( LT )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == LT) :
                        alt67 = 1


                    if alt67 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT143 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement825)
                        if self.failed:
                            return retval


                    else:
                        break #loop67


                char_literal144 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_forStatement829)
                if self.failed:
                    return retval

                char_literal144_tree = self.adaptor.createWithPayload(char_literal144)
                self.adaptor.addChild(root_0, char_literal144_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:122: ( LT )*
                while True: #loop68
                    alt68 = 2
                    LA68_0 = self.input.LA(1)

                    if (LA68_0 == LT) :
                        alt68 = 1


                    if alt68 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT145 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement831)
                        if self.failed:
                            return retval


                    else:
                        break #loop68


                self.following.append(self.FOLLOW_statement_in_forStatement835)
                statement146 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement146.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 24, forStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forStatement

    class forStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:143:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal148 = None
        LT149 = None
        expressionNoIn147 = None

        variableDeclarationListNoIn150 = None


        string_literal148_tree = None
        LT149_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:2: ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn )
                alt70 = 2
                LA70_0 = self.input.LA(1)

                if ((StringLiteral <= LA70_0 <= Identifier) or (38 <= LA70_0 <= 39) or LA70_0 == 42 or LA70_0 == 53 or (67 <= LA70_0 <= 68) or (100 <= LA70_0 <= 101) or (105 <= LA70_0 <= 117)) :
                    alt70 = 1
                elif (LA70_0 == 44) :
                    alt70 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("143:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:144:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart847)
                    expressionNoIn147 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn147.tree)


                elif alt70 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:4: 'var' ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    string_literal148 = self.input.LT(1)
                    self.match(self.input, 44, self.FOLLOW_44_in_forStatementInitialiserPart852)
                    if self.failed:
                        return retval

                    string_literal148_tree = self.adaptor.createWithPayload(string_literal148)
                    self.adaptor.addChild(root_0, string_literal148_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:12: ( LT )*
                    while True: #loop69
                        alt69 = 2
                        LA69_0 = self.input.LA(1)

                        if (LA69_0 == LT) :
                            alt69 = 1


                        if alt69 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT149 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart854)
                            if self.failed:
                                return retval


                        else:
                            break #loop69


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart858)
                    variableDeclarationListNoIn150 = self.variableDeclarationListNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationListNoIn150.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 25, forStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forStatementInitialiserPart

    class forInStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:148:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal151 = None
        LT152 = None
        string_literal153 = None
        LT154 = None
        char_literal155 = None
        LT156 = None
        LT158 = None
        string_literal159 = None
        LT160 = None
        LT162 = None
        char_literal163 = None
        LT164 = None
        forInStatementInitialiserPart157 = None

        expression161 = None

        statement165 = None


        string_literal151_tree = None
        LT152_tree = None
        string_literal153_tree = None
        LT154_tree = None
        char_literal155_tree = None
        LT156_tree = None
        LT158_tree = None
        string_literal159_tree = None
        LT160_tree = None
        LT162_tree = None
        char_literal163_tree = None
        LT164_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal151 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_forInStatement870)
                if self.failed:
                    return retval

                string_literal151_tree = self.adaptor.createWithPayload(string_literal151)
                self.adaptor.addChild(root_0, string_literal151_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:12: ( LT )*
                while True: #loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == LT) :
                        LA71_2 = self.input.LA(2)

                        if (self.synpred89()) :
                            alt71 = 1




                    if alt71 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT152 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement872)
                        if self.failed:
                            return retval


                    else:
                        break #loop71


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:15: ( 'each' )?
                alt72 = 2
                LA72_0 = self.input.LA(1)

                if (LA72_0 == 53) :
                    alt72 = 1
                if alt72 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal153 = self.input.LT(1)
                    self.match(self.input, 53, self.FOLLOW_53_in_forInStatement876)
                    if self.failed:
                        return retval

                    string_literal153_tree = self.adaptor.createWithPayload(string_literal153)
                    self.adaptor.addChild(root_0, string_literal153_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:25: ( LT )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == LT) :
                        alt73 = 1


                    if alt73 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT154 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement879)
                        if self.failed:
                            return retval


                    else:
                        break #loop73


                char_literal155 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_forInStatement883)
                if self.failed:
                    return retval

                char_literal155_tree = self.adaptor.createWithPayload(char_literal155)
                self.adaptor.addChild(root_0, char_literal155_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:34: ( LT )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == LT) :
                        alt74 = 1


                    if alt74 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT156 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement885)
                        if self.failed:
                            return retval


                    else:
                        break #loop74


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement889)
                forInStatementInitialiserPart157 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart157.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:69: ( LT )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == LT) :
                        alt75 = 1


                    if alt75 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT158 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement891)
                        if self.failed:
                            return retval


                    else:
                        break #loop75


                string_literal159 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_forInStatement895)
                if self.failed:
                    return retval

                string_literal159_tree = self.adaptor.createWithPayload(string_literal159)
                self.adaptor.addChild(root_0, string_literal159_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:79: ( LT )*
                while True: #loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == LT) :
                        alt76 = 1


                    if alt76 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT160 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement897)
                        if self.failed:
                            return retval


                    else:
                        break #loop76


                self.following.append(self.FOLLOW_expression_in_forInStatement901)
                expression161 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression161.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:95: ( LT )*
                while True: #loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == LT) :
                        alt77 = 1


                    if alt77 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT162 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement903)
                        if self.failed:
                            return retval


                    else:
                        break #loop77


                char_literal163 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_forInStatement907)
                if self.failed:
                    return retval

                char_literal163_tree = self.adaptor.createWithPayload(char_literal163)
                self.adaptor.addChild(root_0, char_literal163_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:104: ( LT )*
                while True: #loop78
                    alt78 = 2
                    LA78_0 = self.input.LA(1)

                    if (LA78_0 == LT) :
                        alt78 = 1


                    if alt78 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT164 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement909)
                        if self.failed:
                            return retval


                    else:
                        break #loop78


                self.following.append(self.FOLLOW_statement_in_forInStatement913)
                statement165 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement165.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 26, forInStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatement

    class forInStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:152:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal167 = None
        LT168 = None
        leftHandSideExpression166 = None

        variableDeclarationNoIn169 = None


        string_literal167_tree = None
        LT168_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:2: ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn )
                alt80 = 2
                LA80_0 = self.input.LA(1)

                if ((StringLiteral <= LA80_0 <= Identifier) or (38 <= LA80_0 <= 39) or LA80_0 == 42 or LA80_0 == 53 or (67 <= LA80_0 <= 68) or (112 <= LA80_0 <= 117)) :
                    alt80 = 1
                elif (LA80_0 == 44) :
                    alt80 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("152:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );", 80, 0, self.input)

                    raise nvae

                if alt80 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:153:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart925)
                    leftHandSideExpression166 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression166.tree)


                elif alt80 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:4: 'var' ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    string_literal167 = self.input.LT(1)
                    self.match(self.input, 44, self.FOLLOW_44_in_forInStatementInitialiserPart930)
                    if self.failed:
                        return retval

                    string_literal167_tree = self.adaptor.createWithPayload(string_literal167)
                    self.adaptor.addChild(root_0, string_literal167_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:12: ( LT )*
                    while True: #loop79
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if (LA79_0 == LT) :
                            alt79 = 1


                        if alt79 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT168 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart932)
                            if self.failed:
                                return retval


                        else:
                            break #loop79


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart936)
                    variableDeclarationNoIn169 = self.variableDeclarationNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationNoIn169.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 27, forInStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatementInitialiserPart

    class continueStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start continueStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:157:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal170 = None
        set172 = None
        identifier171 = None


        string_literal170_tree = None
        set172_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal170 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_continueStatement947)
                if self.failed:
                    return retval

                string_literal170_tree = self.adaptor.createWithPayload(string_literal170)
                self.adaptor.addChild(root_0, string_literal170_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:15: ( identifier )?
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if (LA81_0 == Identifier or LA81_0 == 53 or (113 <= LA81_0 <= 114)) :
                    alt81 = 1
                if alt81 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement949)
                    identifier171 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier171.tree)



                set172 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_continueStatement952
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
                self.memoize(self.input, 28, continueStatement_StartIndex)

            pass

        return retval

    # $ANTLR end continueStatement

    class breakStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start breakStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:161:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal173 = None
        set175 = None
        identifier174 = None


        string_literal173_tree = None
        set175_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal173 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_breakStatement970)
                if self.failed:
                    return retval

                string_literal173_tree = self.adaptor.createWithPayload(string_literal173)
                self.adaptor.addChild(root_0, string_literal173_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:12: ( identifier )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if (LA82_0 == Identifier or LA82_0 == 53 or (113 <= LA82_0 <= 114)) :
                    alt82 = 1
                if alt82 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement972)
                    identifier174 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier174.tree)



                set175 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_breakStatement975
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
                self.memoize(self.input, 29, breakStatement_StartIndex)

            pass

        return retval

    # $ANTLR end breakStatement

    class returnStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start returnStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:165:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal176 = None
        set178 = None
        expression177 = None


        string_literal176_tree = None
        set178_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:166:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:166:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal176 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_returnStatement993)
                if self.failed:
                    return retval

                string_literal176_tree = self.adaptor.createWithPayload(string_literal176)
                self.adaptor.addChild(root_0, string_literal176_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:166:13: ( expression )?
                alt83 = 2
                LA83_0 = self.input.LA(1)

                if ((StringLiteral <= LA83_0 <= Identifier) or (38 <= LA83_0 <= 39) or LA83_0 == 42 or LA83_0 == 53 or (67 <= LA83_0 <= 68) or (100 <= LA83_0 <= 101) or (105 <= LA83_0 <= 117)) :
                    alt83 = 1
                if alt83 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement995)
                    expression177 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression177.tree)



                set178 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_returnStatement998
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
                self.memoize(self.input, 30, returnStatement_StartIndex)

            pass

        return retval

    # $ANTLR end returnStatement

    class withStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start withStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:169:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal179 = None
        LT180 = None
        char_literal181 = None
        LT182 = None
        LT184 = None
        char_literal185 = None
        LT186 = None
        expression183 = None

        statement187 = None


        string_literal179_tree = None
        LT180_tree = None
        char_literal181_tree = None
        LT182_tree = None
        LT184_tree = None
        char_literal185_tree = None
        LT186_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal179 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_withStatement1017)
                if self.failed:
                    return retval

                string_literal179_tree = self.adaptor.createWithPayload(string_literal179)
                self.adaptor.addChild(root_0, string_literal179_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:13: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        alt84 = 1


                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT180 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1019)
                        if self.failed:
                            return retval


                    else:
                        break #loop84


                char_literal181 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_withStatement1023)
                if self.failed:
                    return retval

                char_literal181_tree = self.adaptor.createWithPayload(char_literal181)
                self.adaptor.addChild(root_0, char_literal181_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:22: ( LT )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == LT) :
                        alt85 = 1


                    if alt85 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT182 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1025)
                        if self.failed:
                            return retval


                    else:
                        break #loop85


                self.following.append(self.FOLLOW_expression_in_withStatement1029)
                expression183 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression183.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:38: ( LT )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == LT) :
                        alt86 = 1


                    if alt86 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT184 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1031)
                        if self.failed:
                            return retval


                    else:
                        break #loop86


                char_literal185 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_withStatement1035)
                if self.failed:
                    return retval

                char_literal185_tree = self.adaptor.createWithPayload(char_literal185)
                self.adaptor.addChild(root_0, char_literal185_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:47: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        alt87 = 1


                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT186 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1037)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                self.following.append(self.FOLLOW_statement_in_withStatement1041)
                statement187 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement187.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 31, withStatement_StartIndex)

            pass

        return retval

    # $ANTLR end withStatement

    class labelledStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start labelledStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:173:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        LT189 = None
        char_literal190 = None
        LT191 = None
        identifier188 = None

        statement192 = None


        LT189_tree = None
        char_literal190_tree = None
        LT191_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1052)
                identifier188 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier188.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:17: ( LT )*
                while True: #loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == LT) :
                        alt88 = 1


                    if alt88 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT189 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1054)
                        if self.failed:
                            return retval


                    else:
                        break #loop88


                char_literal190 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_labelledStatement1058)
                if self.failed:
                    return retval

                char_literal190_tree = self.adaptor.createWithPayload(char_literal190)
                self.adaptor.addChild(root_0, char_literal190_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:26: ( LT )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LT) :
                        alt89 = 1


                    if alt89 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT191 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1060)
                        if self.failed:
                            return retval


                    else:
                        break #loop89


                self.following.append(self.FOLLOW_statement_in_labelledStatement1064)
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
                self.memoize(self.input, 32, labelledStatement_StartIndex)

            pass

        return retval

    # $ANTLR end labelledStatement

    class switchStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start switchStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:177:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal193 = None
        LT194 = None
        char_literal195 = None
        LT196 = None
        LT198 = None
        char_literal199 = None
        LT200 = None
        expression197 = None

        caseBlock201 = None


        string_literal193_tree = None
        LT194_tree = None
        char_literal195_tree = None
        LT196_tree = None
        LT198_tree = None
        char_literal199_tree = None
        LT200_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal193 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_switchStatement1076)
                if self.failed:
                    return retval

                string_literal193_tree = self.adaptor.createWithPayload(string_literal193)
                self.adaptor.addChild(root_0, string_literal193_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:15: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        alt90 = 1


                    if alt90 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT194 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1078)
                        if self.failed:
                            return retval


                    else:
                        break #loop90


                char_literal195 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_switchStatement1082)
                if self.failed:
                    return retval

                char_literal195_tree = self.adaptor.createWithPayload(char_literal195)
                self.adaptor.addChild(root_0, char_literal195_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:24: ( LT )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == LT) :
                        alt91 = 1


                    if alt91 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT196 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1084)
                        if self.failed:
                            return retval


                    else:
                        break #loop91


                self.following.append(self.FOLLOW_expression_in_switchStatement1088)
                expression197 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression197.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:40: ( LT )*
                while True: #loop92
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == LT) :
                        alt92 = 1


                    if alt92 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT198 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1090)
                        if self.failed:
                            return retval


                    else:
                        break #loop92


                char_literal199 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_switchStatement1094)
                if self.failed:
                    return retval

                char_literal199_tree = self.adaptor.createWithPayload(char_literal199)
                self.adaptor.addChild(root_0, char_literal199_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:49: ( LT )*
                while True: #loop93
                    alt93 = 2
                    LA93_0 = self.input.LA(1)

                    if (LA93_0 == LT) :
                        alt93 = 1


                    if alt93 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT200 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1096)
                        if self.failed:
                            return retval


                    else:
                        break #loop93


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1100)
                caseBlock201 = self.caseBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, caseBlock201.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 33, switchStatement_StartIndex)

            pass

        return retval

    # $ANTLR end switchStatement

    class caseBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:181:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal202 = None
        LT203 = None
        LT205 = None
        LT207 = None
        LT209 = None
        char_literal210 = None
        caseClause204 = None

        defaultClause206 = None

        caseClause208 = None


        char_literal202_tree = None
        LT203_tree = None
        LT205_tree = None
        LT207_tree = None
        LT209_tree = None
        char_literal210_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal202 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_caseBlock1112)
                if self.failed:
                    return retval

                char_literal202_tree = self.adaptor.createWithPayload(char_literal202)
                self.adaptor.addChild(root_0, char_literal202_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:8: ( ( LT )* caseClause )*
                while True: #loop95
                    alt95 = 2
                    alt95 = self.dfa95.predict(self.input)
                    if alt95 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:11: ( LT )*
                        while True: #loop94
                            alt94 = 2
                            LA94_0 = self.input.LA(1)

                            if (LA94_0 == LT) :
                                alt94 = 1


                            if alt94 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT203 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1115)
                                if self.failed:
                                    return retval


                            else:
                                break #loop94


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1119)
                        caseClause204 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause204.tree)


                    else:
                        break #loop95


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt99 = 2
                alt99 = self.dfa99.predict(self.input)
                if alt99 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:30: ( LT )*
                    while True: #loop96
                        alt96 = 2
                        LA96_0 = self.input.LA(1)

                        if (LA96_0 == LT) :
                            alt96 = 1


                        if alt96 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT205 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1124)
                            if self.failed:
                                return retval


                        else:
                            break #loop96


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1128)
                    defaultClause206 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause206.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:47: ( ( LT )* caseClause )*
                    while True: #loop98
                        alt98 = 2
                        alt98 = self.dfa98.predict(self.input)
                        if alt98 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:50: ( LT )*
                            while True: #loop97
                                alt97 = 2
                                LA97_0 = self.input.LA(1)

                                if (LA97_0 == LT) :
                                    alt97 = 1


                                if alt97 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT207 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1131)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop97


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1135)
                            caseClause208 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause208.tree)


                        else:
                            break #loop98





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:70: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT209 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1141)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                char_literal210 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_caseBlock1145)
                if self.failed:
                    return retval

                char_literal210_tree = self.adaptor.createWithPayload(char_literal210)
                self.adaptor.addChild(root_0, char_literal210_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 34, caseBlock_StartIndex)

            pass

        return retval

    # $ANTLR end caseBlock

    class caseClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:185:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal211 = None
        LT212 = None
        LT214 = None
        char_literal215 = None
        LT216 = None
        expression213 = None

        statementList217 = None


        string_literal211_tree = None
        LT212_tree = None
        LT214_tree = None
        char_literal215_tree = None
        LT216_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal211 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_caseClause1156)
                if self.failed:
                    return retval

                string_literal211_tree = self.adaptor.createWithPayload(string_literal211)
                self.adaptor.addChild(root_0, string_literal211_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:13: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        alt101 = 1


                    if alt101 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT212 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1158)
                        if self.failed:
                            return retval


                    else:
                        break #loop101


                self.following.append(self.FOLLOW_expression_in_caseClause1162)
                expression213 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression213.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:29: ( LT )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == LT) :
                        alt102 = 1


                    if alt102 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT214 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1164)
                        if self.failed:
                            return retval


                    else:
                        break #loop102


                char_literal215 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_caseClause1168)
                if self.failed:
                    return retval

                char_literal215_tree = self.adaptor.createWithPayload(char_literal215)
                self.adaptor.addChild(root_0, char_literal215_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:38: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        LA103_2 = self.input.LA(2)

                        if (self.synpred124()) :
                            alt103 = 1




                    if alt103 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT216 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1170)
                        if self.failed:
                            return retval


                    else:
                        break #loop103


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:41: ( statementList )?
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if ((StringLiteral <= LA104_0 <= Identifier) or (38 <= LA104_0 <= 39) or LA104_0 == 42 or (44 <= LA104_0 <= 46) or LA104_0 == 48 or (50 <= LA104_0 <= 53) or (55 <= LA104_0 <= 58) or LA104_0 == 60 or (63 <= LA104_0 <= 64) or (67 <= LA104_0 <= 68) or (100 <= LA104_0 <= 101) or (105 <= LA104_0 <= 117)) :
                    alt104 = 1
                if alt104 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1174)
                    statementList217 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList217.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 35, caseClause_StartIndex)

            pass

        return retval

    # $ANTLR end caseClause

    class defaultClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start defaultClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:189:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal218 = None
        LT219 = None
        char_literal220 = None
        LT221 = None
        statementList222 = None


        string_literal218_tree = None
        LT219_tree = None
        char_literal220_tree = None
        LT221_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal218 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_defaultClause1187)
                if self.failed:
                    return retval

                string_literal218_tree = self.adaptor.createWithPayload(string_literal218)
                self.adaptor.addChild(root_0, string_literal218_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:16: ( LT )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == LT) :
                        alt105 = 1


                    if alt105 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT219 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1189)
                        if self.failed:
                            return retval


                    else:
                        break #loop105


                char_literal220 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_defaultClause1193)
                if self.failed:
                    return retval

                char_literal220_tree = self.adaptor.createWithPayload(char_literal220)
                self.adaptor.addChild(root_0, char_literal220_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:25: ( LT )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == LT) :
                        LA106_2 = self.input.LA(2)

                        if (self.synpred127()) :
                            alt106 = 1




                    if alt106 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT221 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1195)
                        if self.failed:
                            return retval


                    else:
                        break #loop106


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:28: ( statementList )?
                alt107 = 2
                LA107_0 = self.input.LA(1)

                if ((StringLiteral <= LA107_0 <= Identifier) or (38 <= LA107_0 <= 39) or LA107_0 == 42 or (44 <= LA107_0 <= 46) or LA107_0 == 48 or (50 <= LA107_0 <= 53) or (55 <= LA107_0 <= 58) or LA107_0 == 60 or (63 <= LA107_0 <= 64) or (67 <= LA107_0 <= 68) or (100 <= LA107_0 <= 101) or (105 <= LA107_0 <= 117)) :
                    alt107 = 1
                if alt107 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1199)
                    statementList222 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList222.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 36, defaultClause_StartIndex)

            pass

        return retval

    # $ANTLR end defaultClause

    class throwStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start throwStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:193:1: throwStatement : 'throw' expression ( LT | ';' ) ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal223 = None
        set225 = None
        expression224 = None


        string_literal223_tree = None
        set225_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:194:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:194:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal223 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_throwStatement1212)
                if self.failed:
                    return retval

                string_literal223_tree = self.adaptor.createWithPayload(string_literal223)
                self.adaptor.addChild(root_0, string_literal223_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1214)
                expression224 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression224.tree)
                set225 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 46:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_throwStatement1216
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
                self.memoize(self.input, 37, throwStatement_StartIndex)

            pass

        return retval

    # $ANTLR end throwStatement

    class tryStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start tryStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:197:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal226 = None
        LT227 = None
        LT229 = None
        LT232 = None
        statementBlock228 = None

        finallyClause230 = None

        catchClause231 = None

        finallyClause233 = None


        string_literal226_tree = None
        LT227_tree = None
        LT229_tree = None
        LT232_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal226 = self.input.LT(1)
                self.match(self.input, 64, self.FOLLOW_64_in_tryStatement1234)
                if self.failed:
                    return retval

                string_literal226_tree = self.adaptor.createWithPayload(string_literal226)
                self.adaptor.addChild(root_0, string_literal226_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:12: ( LT )*
                while True: #loop108
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == LT) :
                        alt108 = 1


                    if alt108 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT227 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1236)
                        if self.failed:
                            return retval


                    else:
                        break #loop108


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1240)
                statementBlock228 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock228.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:32: ( LT )*
                while True: #loop109
                    alt109 = 2
                    LA109_0 = self.input.LA(1)

                    if (LA109_0 == LT) :
                        alt109 = 1


                    if alt109 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT229 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1242)
                        if self.failed:
                            return retval


                    else:
                        break #loop109


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt112 = 2
                LA112_0 = self.input.LA(1)

                if (LA112_0 == 66) :
                    alt112 = 1
                elif (LA112_0 == 65) :
                    alt112 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("198:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 112, 0, self.input)

                    raise nvae

                if alt112 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1247)
                    finallyClause230 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause230.tree)


                elif alt112 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1251)
                    catchClause231 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause231.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:64: ( ( LT )* finallyClause )?
                    alt111 = 2
                    alt111 = self.dfa111.predict(self.input)
                    if alt111 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:67: ( LT )*
                        while True: #loop110
                            alt110 = 2
                            LA110_0 = self.input.LA(1)

                            if (LA110_0 == LT) :
                                alt110 = 1


                            if alt110 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT232 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1254)
                                if self.failed:
                                    return retval


                            else:
                                break #loop110


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1258)
                        finallyClause233 = self.finallyClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, finallyClause233.tree)









                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 38, tryStatement_StartIndex)

            pass

        return retval

    # $ANTLR end tryStatement

    class catchClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start catchClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:201:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal234 = None
        LT235 = None
        char_literal236 = None
        LT237 = None
        LT239 = None
        char_literal240 = None
        LT241 = None
        identifier238 = None

        statementBlock242 = None


        string_literal234_tree = None
        LT235_tree = None
        char_literal236_tree = None
        LT237_tree = None
        LT239_tree = None
        char_literal240_tree = None
        LT241_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal234 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_catchClause1279)
                if self.failed:
                    return retval

                string_literal234_tree = self.adaptor.createWithPayload(string_literal234)
                self.adaptor.addChild(root_0, string_literal234_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:14: ( LT )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == LT) :
                        alt113 = 1


                    if alt113 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT235 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1281)
                        if self.failed:
                            return retval


                    else:
                        break #loop113


                char_literal236 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_catchClause1285)
                if self.failed:
                    return retval

                char_literal236_tree = self.adaptor.createWithPayload(char_literal236)
                self.adaptor.addChild(root_0, char_literal236_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:23: ( LT )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == LT) :
                        alt114 = 1


                    if alt114 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT237 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1287)
                        if self.failed:
                            return retval


                    else:
                        break #loop114


                self.following.append(self.FOLLOW_identifier_in_catchClause1291)
                identifier238 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier238.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:39: ( LT )*
                while True: #loop115
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == LT) :
                        alt115 = 1


                    if alt115 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT239 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1293)
                        if self.failed:
                            return retval


                    else:
                        break #loop115


                char_literal240 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_catchClause1297)
                if self.failed:
                    return retval

                char_literal240_tree = self.adaptor.createWithPayload(char_literal240)
                self.adaptor.addChild(root_0, char_literal240_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:48: ( LT )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == LT) :
                        alt116 = 1


                    if alt116 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT241 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1299)
                        if self.failed:
                            return retval


                    else:
                        break #loop116


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1303)
                statementBlock242 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock242.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 39, catchClause_StartIndex)

            pass

        return retval

    # $ANTLR end catchClause

    class finallyClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start finallyClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:205:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal243 = None
        LT244 = None
        statementBlock245 = None


        string_literal243_tree = None
        LT244_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal243 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_finallyClause1315)
                if self.failed:
                    return retval

                string_literal243_tree = self.adaptor.createWithPayload(string_literal243)
                self.adaptor.addChild(root_0, string_literal243_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:206:16: ( LT )*
                while True: #loop117
                    alt117 = 2
                    LA117_0 = self.input.LA(1)

                    if (LA117_0 == LT) :
                        alt117 = 1


                    if alt117 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT244 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1317)
                        if self.failed:
                            return retval


                    else:
                        break #loop117


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause1321)
                statementBlock245 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock245.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 40, finallyClause_StartIndex)

            pass

        return retval

    # $ANTLR end finallyClause

    class expression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:210:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT247 = None
        char_literal248 = None
        LT249 = None
        assignmentExpression246 = None

        assignmentExpression250 = None


        LT247_tree = None
        char_literal248_tree = None
        LT249_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression1333)
                assignmentExpression246 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression246.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop120
                    alt120 = 2
                    alt120 = self.dfa120.predict(self.input)
                    if alt120 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:28: ( LT )*
                        while True: #loop118
                            alt118 = 2
                            LA118_0 = self.input.LA(1)

                            if (LA118_0 == LT) :
                                alt118 = 1


                            if alt118 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT247 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1336)
                                if self.failed:
                                    return retval


                            else:
                                break #loop118


                        char_literal248 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_expression1340)
                        if self.failed:
                            return retval

                        char_literal248_tree = self.adaptor.createWithPayload(char_literal248)
                        self.adaptor.addChild(root_0, char_literal248_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:37: ( LT )*
                        while True: #loop119
                            alt119 = 2
                            LA119_0 = self.input.LA(1)

                            if (LA119_0 == LT) :
                                alt119 = 1


                            if alt119 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT249 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1342)
                                if self.failed:
                                    return retval


                            else:
                                break #loop119


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression1346)
                        assignmentExpression250 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression250.tree)


                    else:
                        break #loop120





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 41, expression_StartIndex)

            pass

        return retval

    # $ANTLR end expression

    class expressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:214:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT252 = None
        char_literal253 = None
        LT254 = None
        assignmentExpressionNoIn251 = None

        assignmentExpressionNoIn255 = None


        LT252_tree = None
        char_literal253_tree = None
        LT254_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1360)
                assignmentExpressionNoIn251 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn251.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop123
                    alt123 = 2
                    alt123 = self.dfa123.predict(self.input)
                    if alt123 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:32: ( LT )*
                        while True: #loop121
                            alt121 = 2
                            LA121_0 = self.input.LA(1)

                            if (LA121_0 == LT) :
                                alt121 = 1


                            if alt121 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT252 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1363)
                                if self.failed:
                                    return retval


                            else:
                                break #loop121


                        char_literal253 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_expressionNoIn1367)
                        if self.failed:
                            return retval

                        char_literal253_tree = self.adaptor.createWithPayload(char_literal253)
                        self.adaptor.addChild(root_0, char_literal253_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:41: ( LT )*
                        while True: #loop122
                            alt122 = 2
                            LA122_0 = self.input.LA(1)

                            if (LA122_0 == LT) :
                                alt122 = 1


                            if alt122 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT254 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1369)
                                if self.failed:
                                    return retval


                            else:
                                break #loop122


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1373)
                        assignmentExpressionNoIn255 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn255.tree)


                    else:
                        break #loop123





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 42, expressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end expressionNoIn

    class assignmentExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT258 = None
        LT260 = None
        conditionalExpression256 = None

        leftHandSideExpression257 = None

        assignmentOperator259 = None

        assignmentExpression261 = None


        LT258_tree = None
        LT260_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:2: ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
                alt126 = 2
                LA126 = self.input.LA(1)
                if LA126 == 112:
                    LA126_1 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 1, self.input)

                        raise nvae

                elif LA126 == Identifier or LA126 == 53 or LA126 == 113 or LA126 == 114:
                    LA126_2 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 2, self.input)

                        raise nvae

                elif LA126 == StringLiteral or LA126 == NumericLiteral or LA126 == RegularExpressionLiteral or LA126 == 115 or LA126 == 116 or LA126 == 117:
                    LA126_3 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 3, self.input)

                        raise nvae

                elif LA126 == 68:
                    LA126_4 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 4, self.input)

                        raise nvae

                elif LA126 == 42:
                    LA126_5 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 5, self.input)

                        raise nvae

                elif LA126 == 39:
                    LA126_6 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 6, self.input)

                        raise nvae

                elif LA126 == 38:
                    LA126_7 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 7, self.input)

                        raise nvae

                elif LA126 == 67:
                    LA126_8 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt126 = 1
                    elif (True) :
                        alt126 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 8, self.input)

                        raise nvae

                elif LA126 == 100 or LA126 == 101 or LA126 == 105 or LA126 == 106 or LA126 == 107 or LA126 == 108 or LA126 == 109 or LA126 == 110 or LA126 == 111:
                    alt126 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("218:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 126, 0, self.input)

                    raise nvae

                if alt126 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression1387)
                    conditionalExpression256 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression256.tree)


                elif alt126 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1392)
                    leftHandSideExpression257 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression257.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:29: ( LT )*
                    while True: #loop124
                        alt124 = 2
                        LA124_0 = self.input.LA(1)

                        if (LA124_0 == LT) :
                            alt124 = 1


                        if alt124 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT258 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1394)
                            if self.failed:
                                return retval


                        else:
                            break #loop124


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1398)
                    assignmentOperator259 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator259.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:53: ( LT )*
                    while True: #loop125
                        alt125 = 2
                        LA125_0 = self.input.LA(1)

                        if (LA125_0 == LT) :
                            alt125 = 1


                        if alt125 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT260 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1400)
                            if self.failed:
                                return retval


                        else:
                            break #loop125


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1404)
                    assignmentExpression261 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression261.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 43, assignmentExpression_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpression

    class assignmentExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT264 = None
        LT266 = None
        conditionalExpressionNoIn262 = None

        leftHandSideExpression263 = None

        assignmentOperator265 = None

        assignmentExpressionNoIn267 = None


        LT264_tree = None
        LT266_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:2: ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
                alt129 = 2
                LA129 = self.input.LA(1)
                if LA129 == 112:
                    LA129_1 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 1, self.input)

                        raise nvae

                elif LA129 == Identifier or LA129 == 53 or LA129 == 113 or LA129 == 114:
                    LA129_2 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 2, self.input)

                        raise nvae

                elif LA129 == StringLiteral or LA129 == NumericLiteral or LA129 == RegularExpressionLiteral or LA129 == 115 or LA129 == 116 or LA129 == 117:
                    LA129_3 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 3, self.input)

                        raise nvae

                elif LA129 == 68:
                    LA129_4 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 4, self.input)

                        raise nvae

                elif LA129 == 42:
                    LA129_5 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 5, self.input)

                        raise nvae

                elif LA129 == 39:
                    LA129_6 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 6, self.input)

                        raise nvae

                elif LA129 == 38:
                    LA129_7 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 7, self.input)

                        raise nvae

                elif LA129 == 67:
                    LA129_8 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 8, self.input)

                        raise nvae

                elif LA129 == 100 or LA129 == 101 or LA129 == 105 or LA129 == 106 or LA129 == 107 or LA129 == 108 or LA129 == 109 or LA129 == 110 or LA129 == 111:
                    alt129 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("223:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 129, 0, self.input)

                    raise nvae

                if alt129 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1416)
                    conditionalExpressionNoIn262 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn262.tree)


                elif alt129 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1421)
                    leftHandSideExpression263 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression263.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:29: ( LT )*
                    while True: #loop127
                        alt127 = 2
                        LA127_0 = self.input.LA(1)

                        if (LA127_0 == LT) :
                            alt127 = 1


                        if alt127 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT264 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1423)
                            if self.failed:
                                return retval


                        else:
                            break #loop127


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1427)
                    assignmentOperator265 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator265.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:53: ( LT )*
                    while True: #loop128
                        alt128 = 2
                        LA128_0 = self.input.LA(1)

                        if (LA128_0 == LT) :
                            alt128 = 1


                        if alt128 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT266 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1429)
                            if self.failed:
                                return retval


                        else:
                            break #loop128


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1433)
                    assignmentExpressionNoIn267 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn267.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 44, assignmentExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpressionNoIn

    class leftHandSideExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start leftHandSideExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:228:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression268 = None

        newExpression269 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:2: ( callExpression | newExpression )
                alt130 = 2
                LA130 = self.input.LA(1)
                if LA130 == 112:
                    LA130_1 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 1, self.input)

                        raise nvae

                elif LA130 == Identifier or LA130 == 53 or LA130 == 113 or LA130 == 114:
                    LA130_2 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 2, self.input)

                        raise nvae

                elif LA130 == StringLiteral or LA130 == NumericLiteral or LA130 == RegularExpressionLiteral or LA130 == 115 or LA130 == 116 or LA130 == 117:
                    LA130_3 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 3, self.input)

                        raise nvae

                elif LA130 == 68:
                    LA130_4 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 4, self.input)

                        raise nvae

                elif LA130 == 42:
                    LA130_5 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 5, self.input)

                        raise nvae

                elif LA130 == 39:
                    LA130_6 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 6, self.input)

                        raise nvae

                elif LA130 == 38:
                    LA130_7 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 7, self.input)

                        raise nvae

                elif LA130 == 67:
                    LA130_8 = self.input.LA(2)

                    if (self.synpred152()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 8, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("228:1: leftHandSideExpression : ( callExpression | newExpression );", 130, 0, self.input)

                    raise nvae

                if alt130 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression1445)
                    callExpression268 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression268.tree)


                elif alt130 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression1450)
                    newExpression269 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression269.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 45, leftHandSideExpression_StartIndex)

            pass

        return retval

    # $ANTLR end leftHandSideExpression

    class newExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start newExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:233:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal271 = None
        LT272 = None
        memberExpression270 = None

        newExpression273 = None


        string_literal271_tree = None
        LT272_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:2: ( memberExpression | 'new' ( LT )* newExpression )
                alt132 = 2
                LA132_0 = self.input.LA(1)

                if ((StringLiteral <= LA132_0 <= Identifier) or (38 <= LA132_0 <= 39) or LA132_0 == 42 or LA132_0 == 53 or LA132_0 == 68 or (112 <= LA132_0 <= 117)) :
                    alt132 = 1
                elif (LA132_0 == 67) :
                    LA132_8 = self.input.LA(2)

                    if (self.synpred153()) :
                        alt132 = 1
                    elif (True) :
                        alt132 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("233:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 132, 8, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("233:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 132, 0, self.input)

                    raise nvae

                if alt132 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression1462)
                    memberExpression270 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression270.tree)


                elif alt132 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:4: 'new' ( LT )* newExpression
                    root_0 = self.adaptor.nil()

                    string_literal271 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_newExpression1467)
                    if self.failed:
                        return retval

                    string_literal271_tree = self.adaptor.createWithPayload(string_literal271)
                    self.adaptor.addChild(root_0, string_literal271_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:12: ( LT )*
                    while True: #loop131
                        alt131 = 2
                        LA131_0 = self.input.LA(1)

                        if (LA131_0 == LT) :
                            alt131 = 1


                        if alt131 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT272 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1469)
                            if self.failed:
                                return retval


                        else:
                            break #loop131


                    self.following.append(self.FOLLOW_newExpression_in_newExpression1473)
                    newExpression273 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression273.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 46, newExpression_StartIndex)

            pass

        return retval

    # $ANTLR end newExpression

    class memberExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:238:1: memberExpression : ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* ;
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal276 = None
        LT277 = None
        LT279 = None
        LT281 = None
        primaryExpression274 = None

        functionExpression275 = None

        memberExpression278 = None

        arguments280 = None

        memberExpressionSuffix282 = None


        string_literal276_tree = None
        LT277_tree = None
        LT279_tree = None
        LT281_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:2: ( ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )
                alt135 = 3
                LA135 = self.input.LA(1)
                if LA135 == StringLiteral or LA135 == NumericLiteral or LA135 == RegularExpressionLiteral or LA135 == Identifier or LA135 == 39 or LA135 == 42 or LA135 == 53 or LA135 == 68 or LA135 == 112 or LA135 == 113 or LA135 == 114 or LA135 == 115 or LA135 == 116 or LA135 == 117:
                    alt135 = 1
                elif LA135 == 38:
                    alt135 = 2
                elif LA135 == 67:
                    alt135 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("239:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )", 135, 0, self.input)

                    raise nvae

                if alt135 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:5: primaryExpression
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression1486)
                    primaryExpression274 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, primaryExpression274.tree)


                elif alt135 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:25: functionExpression
                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression1490)
                    functionExpression275 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression275.tree)


                elif alt135 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:46: 'new' ( LT )* memberExpression ( LT )* arguments
                    string_literal276 = self.input.LT(1)
                    self.match(self.input, 67, self.FOLLOW_67_in_memberExpression1494)
                    if self.failed:
                        return retval

                    string_literal276_tree = self.adaptor.createWithPayload(string_literal276)
                    self.adaptor.addChild(root_0, string_literal276_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:54: ( LT )*
                    while True: #loop133
                        alt133 = 2
                        LA133_0 = self.input.LA(1)

                        if (LA133_0 == LT) :
                            alt133 = 1


                        if alt133 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT277 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1496)
                            if self.failed:
                                return retval


                        else:
                            break #loop133


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression1500)
                    memberExpression278 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression278.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:76: ( LT )*
                    while True: #loop134
                        alt134 = 2
                        LA134_0 = self.input.LA(1)

                        if (LA134_0 == LT) :
                            alt134 = 1


                        if alt134 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT279 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1502)
                            if self.failed:
                                return retval


                        else:
                            break #loop134


                    self.following.append(self.FOLLOW_arguments_in_memberExpression1506)
                    arguments280 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments280.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:90: ( ( LT )* memberExpressionSuffix )*
                while True: #loop137
                    alt137 = 2
                    LA137_0 = self.input.LA(1)

                    if (LA137_0 == LT) :
                        LA137_1 = self.input.LA(2)

                        if (self.synpred160()) :
                            alt137 = 1


                    elif (LA137_0 == 68 or LA137_0 == 70) :
                        alt137 = 1


                    if alt137 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:91: ( LT )* memberExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:93: ( LT )*
                        while True: #loop136
                            alt136 = 2
                            LA136_0 = self.input.LA(1)

                            if (LA136_0 == LT) :
                                alt136 = 1


                            if alt136 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT281 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1510)
                                if self.failed:
                                    return retval


                            else:
                                break #loop136


                        self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1514)
                        memberExpressionSuffix282 = self.memberExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, memberExpressionSuffix282.tree)


                    else:
                        break #loop137





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 47, memberExpression_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpression

    class memberExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:242:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix283 = None

        propertyReferenceSuffix284 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:243:2: ( indexSuffix | propertyReferenceSuffix )
                alt138 = 2
                LA138_0 = self.input.LA(1)

                if (LA138_0 == 68) :
                    alt138 = 1
                elif (LA138_0 == 70) :
                    alt138 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("242:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );", 138, 0, self.input)

                    raise nvae

                if alt138 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:243:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix1528)
                    indexSuffix283 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix283.tree)


                elif alt138 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:244:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1533)
                    propertyReferenceSuffix284 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix284.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 48, memberExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpressionSuffix

    class callExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:247:1: callExpression : memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT286 = None
        LT288 = None
        memberExpression285 = None

        arguments287 = None

        callExpressionSuffix289 = None


        LT286_tree = None
        LT288_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:2: ( memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:4: memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_memberExpression_in_callExpression1544)
                memberExpression285 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, memberExpression285.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:23: ( LT )*
                while True: #loop139
                    alt139 = 2
                    LA139_0 = self.input.LA(1)

                    if (LA139_0 == LT) :
                        alt139 = 1


                    if alt139 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT286 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1546)
                        if self.failed:
                            return retval


                    else:
                        break #loop139


                self.following.append(self.FOLLOW_arguments_in_callExpression1550)
                arguments287 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, arguments287.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:36: ( ( LT )* callExpressionSuffix )*
                while True: #loop141
                    alt141 = 2
                    LA141_0 = self.input.LA(1)

                    if (LA141_0 == LT) :
                        LA141_1 = self.input.LA(2)

                        if (self.synpred164()) :
                            alt141 = 1


                    elif (LA141_0 == 39 or LA141_0 == 68 or LA141_0 == 70) :
                        alt141 = 1


                    if alt141 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:37: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:39: ( LT )*
                        while True: #loop140
                            alt140 = 2
                            LA140_0 = self.input.LA(1)

                            if (LA140_0 == LT) :
                                alt140 = 1


                            if alt140 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT288 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1553)
                                if self.failed:
                                    return retval


                            else:
                                break #loop140


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression1557)
                        callExpressionSuffix289 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, callExpressionSuffix289.tree)


                    else:
                        break #loop141





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 49, callExpression_StartIndex)

            pass

        return retval

    # $ANTLR end callExpression

    class callExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:251:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments290 = None

        indexSuffix291 = None

        propertyReferenceSuffix292 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:252:2: ( arguments | indexSuffix | propertyReferenceSuffix )
                alt142 = 3
                LA142 = self.input.LA(1)
                if LA142 == 39:
                    alt142 = 1
                elif LA142 == 68:
                    alt142 = 2
                elif LA142 == 70:
                    alt142 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("251:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );", 142, 0, self.input)

                    raise nvae

                if alt142 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:252:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix1571)
                    arguments290 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments290.tree)


                elif alt142 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:253:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix1576)
                    indexSuffix291 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix291.tree)


                elif alt142 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1581)
                    propertyReferenceSuffix292 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix292.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 50, callExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end callExpressionSuffix

    class arguments_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arguments
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:257:1: arguments : '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal293 = None
        LT294 = None
        LT296 = None
        char_literal297 = None
        LT298 = None
        LT300 = None
        char_literal301 = None
        assignmentExpression295 = None

        assignmentExpression299 = None


        char_literal293_tree = None
        LT294_tree = None
        LT296_tree = None
        char_literal297_tree = None
        LT298_tree = None
        LT300_tree = None
        char_literal301_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:2: ( '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:4: '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal293 = self.input.LT(1)
                self.match(self.input, 39, self.FOLLOW_39_in_arguments1592)
                if self.failed:
                    return retval

                char_literal293_tree = self.adaptor.createWithPayload(char_literal293)
                self.adaptor.addChild(root_0, char_literal293_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:8: ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )?
                alt147 = 2
                alt147 = self.dfa147.predict(self.input)
                if alt147 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:9: ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:11: ( LT )*
                    while True: #loop143
                        alt143 = 2
                        LA143_0 = self.input.LA(1)

                        if (LA143_0 == LT) :
                            alt143 = 1


                        if alt143 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT294 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments1595)
                            if self.failed:
                                return retval


                        else:
                            break #loop143


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments1599)
                    assignmentExpression295 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression295.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:35: ( ( LT )* ',' ( LT )* assignmentExpression )*
                    while True: #loop146
                        alt146 = 2
                        alt146 = self.dfa146.predict(self.input)
                        if alt146 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:36: ( LT )* ',' ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:38: ( LT )*
                            while True: #loop144
                                alt144 = 2
                                LA144_0 = self.input.LA(1)

                                if (LA144_0 == LT) :
                                    alt144 = 1


                                if alt144 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT296 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1602)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop144


                            char_literal297 = self.input.LT(1)
                            self.match(self.input, 40, self.FOLLOW_40_in_arguments1606)
                            if self.failed:
                                return retval

                            char_literal297_tree = self.adaptor.createWithPayload(char_literal297)
                            self.adaptor.addChild(root_0, char_literal297_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:47: ( LT )*
                            while True: #loop145
                                alt145 = 2
                                LA145_0 = self.input.LA(1)

                                if (LA145_0 == LT) :
                                    alt145 = 1


                                if alt145 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT298 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1608)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop145


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments1612)
                            assignmentExpression299 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression299.tree)


                        else:
                            break #loop146





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:77: ( LT )*
                while True: #loop148
                    alt148 = 2
                    LA148_0 = self.input.LA(1)

                    if (LA148_0 == LT) :
                        alt148 = 1


                    if alt148 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT300 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments1618)
                        if self.failed:
                            return retval


                    else:
                        break #loop148


                char_literal301 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_arguments1622)
                if self.failed:
                    return retval

                char_literal301_tree = self.adaptor.createWithPayload(char_literal301)
                self.adaptor.addChild(root_0, char_literal301_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 51, arguments_StartIndex)

            pass

        return retval

    # $ANTLR end arguments

    class indexSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start indexSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:261:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal302 = None
        LT303 = None
        LT305 = None
        char_literal306 = None
        expression304 = None


        char_literal302_tree = None
        LT303_tree = None
        LT305_tree = None
        char_literal306_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:2: ( '[' ( LT )* expression ( LT )* ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:4: '[' ( LT )* expression ( LT )* ']'
                root_0 = self.adaptor.nil()

                char_literal302 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_indexSuffix1634)
                if self.failed:
                    return retval

                char_literal302_tree = self.adaptor.createWithPayload(char_literal302)
                self.adaptor.addChild(root_0, char_literal302_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:10: ( LT )*
                while True: #loop149
                    alt149 = 2
                    LA149_0 = self.input.LA(1)

                    if (LA149_0 == LT) :
                        alt149 = 1


                    if alt149 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT303 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1636)
                        if self.failed:
                            return retval


                    else:
                        break #loop149


                self.following.append(self.FOLLOW_expression_in_indexSuffix1640)
                expression304 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression304.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:26: ( LT )*
                while True: #loop150
                    alt150 = 2
                    LA150_0 = self.input.LA(1)

                    if (LA150_0 == LT) :
                        alt150 = 1


                    if alt150 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT305 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1642)
                        if self.failed:
                            return retval


                    else:
                        break #loop150


                char_literal306 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_indexSuffix1646)
                if self.failed:
                    return retval

                char_literal306_tree = self.adaptor.createWithPayload(char_literal306)
                self.adaptor.addChild(root_0, char_literal306_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 52, indexSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end indexSuffix

    class propertyReferenceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyReferenceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:1: propertyReferenceSuffix : '.' ( LT )* identifier ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal307 = None
        LT308 = None
        identifier309 = None


        char_literal307_tree = None
        LT308_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:2: ( '.' ( LT )* identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:4: '.' ( LT )* identifier
                root_0 = self.adaptor.nil()

                char_literal307 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_propertyReferenceSuffix1659)
                if self.failed:
                    return retval

                char_literal307_tree = self.adaptor.createWithPayload(char_literal307)
                self.adaptor.addChild(root_0, char_literal307_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:10: ( LT )*
                while True: #loop151
                    alt151 = 2
                    LA151_0 = self.input.LA(1)

                    if (LA151_0 == LT) :
                        alt151 = 1


                    if alt151 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT308 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix1661)
                        if self.failed:
                            return retval


                    else:
                        break #loop151


                self.following.append(self.FOLLOW_identifier_in_propertyReferenceSuffix1665)
                identifier309 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier309.tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 53, propertyReferenceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end propertyReferenceSuffix

    class assignmentOperator_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentOperator
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set310 = None

        set310_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set310 = self.input.LT(1)
                if self.input.LA(1) == 47 or (71 <= self.input.LA(1) <= 81):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set310))
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
                self.memoize(self.input, 54, assignmentOperator_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentOperator

    class conditionalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:273:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT312 = None
        char_literal313 = None
        LT314 = None
        LT316 = None
        char_literal317 = None
        LT318 = None
        logicalORExpression311 = None

        assignmentExpression315 = None

        assignmentExpression319 = None


        LT312_tree = None
        char_literal313_tree = None
        LT314_tree = None
        LT316_tree = None
        char_literal317_tree = None
        LT318_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression1732)
                logicalORExpression311 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression311.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt156 = 2
                alt156 = self.dfa156.predict(self.input)
                if alt156 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:27: ( LT )*
                    while True: #loop152
                        alt152 = 2
                        LA152_0 = self.input.LA(1)

                        if (LA152_0 == LT) :
                            alt152 = 1


                        if alt152 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT312 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1735)
                            if self.failed:
                                return retval


                        else:
                            break #loop152


                    char_literal313 = self.input.LT(1)
                    self.match(self.input, 82, self.FOLLOW_82_in_conditionalExpression1739)
                    if self.failed:
                        return retval

                    char_literal313_tree = self.adaptor.createWithPayload(char_literal313)
                    self.adaptor.addChild(root_0, char_literal313_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:36: ( LT )*
                    while True: #loop153
                        alt153 = 2
                        LA153_0 = self.input.LA(1)

                        if (LA153_0 == LT) :
                            alt153 = 1


                        if alt153 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT314 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1741)
                            if self.failed:
                                return retval


                        else:
                            break #loop153


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1745)
                    assignmentExpression315 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression315.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:62: ( LT )*
                    while True: #loop154
                        alt154 = 2
                        LA154_0 = self.input.LA(1)

                        if (LA154_0 == LT) :
                            alt154 = 1


                        if alt154 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT316 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1747)
                            if self.failed:
                                return retval


                        else:
                            break #loop154


                    char_literal317 = self.input.LT(1)
                    self.match(self.input, 59, self.FOLLOW_59_in_conditionalExpression1751)
                    if self.failed:
                        return retval

                    char_literal317_tree = self.adaptor.createWithPayload(char_literal317)
                    self.adaptor.addChild(root_0, char_literal317_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:71: ( LT )*
                    while True: #loop155
                        alt155 = 2
                        LA155_0 = self.input.LA(1)

                        if (LA155_0 == LT) :
                            alt155 = 1


                        if alt155 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT318 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1753)
                            if self.failed:
                                return retval


                        else:
                            break #loop155


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1757)
                    assignmentExpression319 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression319.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 55, conditionalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpression

    class conditionalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:277:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
    def conditionalExpressionNoIn(self, ):

        retval = self.conditionalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        conditionalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT321 = None
        char_literal322 = None
        LT323 = None
        LT325 = None
        char_literal326 = None
        LT327 = None
        logicalORExpressionNoIn320 = None

        assignmentExpressionNoIn324 = None

        assignmentExpressionNoIn328 = None


        LT321_tree = None
        char_literal322_tree = None
        LT323_tree = None
        LT325_tree = None
        char_literal326_tree = None
        LT327_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1770)
                logicalORExpressionNoIn320 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn320.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt161 = 2
                alt161 = self.dfa161.predict(self.input)
                if alt161 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:31: ( LT )*
                    while True: #loop157
                        alt157 = 2
                        LA157_0 = self.input.LA(1)

                        if (LA157_0 == LT) :
                            alt157 = 1


                        if alt157 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT321 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1773)
                            if self.failed:
                                return retval


                        else:
                            break #loop157


                    char_literal322 = self.input.LT(1)
                    self.match(self.input, 82, self.FOLLOW_82_in_conditionalExpressionNoIn1777)
                    if self.failed:
                        return retval

                    char_literal322_tree = self.adaptor.createWithPayload(char_literal322)
                    self.adaptor.addChild(root_0, char_literal322_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:40: ( LT )*
                    while True: #loop158
                        alt158 = 2
                        LA158_0 = self.input.LA(1)

                        if (LA158_0 == LT) :
                            alt158 = 1


                        if alt158 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT323 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1779)
                            if self.failed:
                                return retval


                        else:
                            break #loop158


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1783)
                    assignmentExpressionNoIn324 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn324.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:70: ( LT )*
                    while True: #loop159
                        alt159 = 2
                        LA159_0 = self.input.LA(1)

                        if (LA159_0 == LT) :
                            alt159 = 1


                        if alt159 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT325 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1785)
                            if self.failed:
                                return retval


                        else:
                            break #loop159


                    char_literal326 = self.input.LT(1)
                    self.match(self.input, 59, self.FOLLOW_59_in_conditionalExpressionNoIn1789)
                    if self.failed:
                        return retval

                    char_literal326_tree = self.adaptor.createWithPayload(char_literal326)
                    self.adaptor.addChild(root_0, char_literal326_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:79: ( LT )*
                    while True: #loop160
                        alt160 = 2
                        LA160_0 = self.input.LA(1)

                        if (LA160_0 == LT) :
                            alt160 = 1


                        if alt160 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT327 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1791)
                            if self.failed:
                                return retval


                        else:
                            break #loop160


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1795)
                    assignmentExpressionNoIn328 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn328.tree)






                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 56, conditionalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpressionNoIn

    class logicalORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:281:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
    def logicalORExpression(self, ):

        retval = self.logicalORExpression_return()
        retval.start = self.input.LT(1)
        logicalORExpression_StartIndex = self.input.index()
        root_0 = None

        LT330 = None
        string_literal331 = None
        LT332 = None
        logicalANDExpression329 = None

        logicalANDExpression333 = None


        LT330_tree = None
        string_literal331_tree = None
        LT332_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1808)
                logicalANDExpression329 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression329.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop164
                    alt164 = 2
                    alt164 = self.dfa164.predict(self.input)
                    if alt164 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:28: ( LT )*
                        while True: #loop162
                            alt162 = 2
                            LA162_0 = self.input.LA(1)

                            if (LA162_0 == LT) :
                                alt162 = 1


                            if alt162 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT330 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1811)
                                if self.failed:
                                    return retval


                            else:
                                break #loop162


                        string_literal331 = self.input.LT(1)
                        self.match(self.input, 83, self.FOLLOW_83_in_logicalORExpression1815)
                        if self.failed:
                            return retval

                        string_literal331_tree = self.adaptor.createWithPayload(string_literal331)
                        self.adaptor.addChild(root_0, string_literal331_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:38: ( LT )*
                        while True: #loop163
                            alt163 = 2
                            LA163_0 = self.input.LA(1)

                            if (LA163_0 == LT) :
                                alt163 = 1


                            if alt163 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT332 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1817)
                                if self.failed:
                                    return retval


                            else:
                                break #loop163


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1821)
                        logicalANDExpression333 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression333.tree)


                    else:
                        break #loop164





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 57, logicalORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpression

    class logicalORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:285:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
    def logicalORExpressionNoIn(self, ):

        retval = self.logicalORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT335 = None
        string_literal336 = None
        LT337 = None
        logicalANDExpressionNoIn334 = None

        logicalANDExpressionNoIn338 = None


        LT335_tree = None
        string_literal336_tree = None
        LT337_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1835)
                logicalANDExpressionNoIn334 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn334.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop167
                    alt167 = 2
                    alt167 = self.dfa167.predict(self.input)
                    if alt167 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:32: ( LT )*
                        while True: #loop165
                            alt165 = 2
                            LA165_0 = self.input.LA(1)

                            if (LA165_0 == LT) :
                                alt165 = 1


                            if alt165 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT335 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1838)
                                if self.failed:
                                    return retval


                            else:
                                break #loop165


                        string_literal336 = self.input.LT(1)
                        self.match(self.input, 83, self.FOLLOW_83_in_logicalORExpressionNoIn1842)
                        if self.failed:
                            return retval

                        string_literal336_tree = self.adaptor.createWithPayload(string_literal336)
                        self.adaptor.addChild(root_0, string_literal336_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:42: ( LT )*
                        while True: #loop166
                            alt166 = 2
                            LA166_0 = self.input.LA(1)

                            if (LA166_0 == LT) :
                                alt166 = 1


                            if alt166 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT337 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1844)
                                if self.failed:
                                    return retval


                            else:
                                break #loop166


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1848)
                        logicalANDExpressionNoIn338 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn338.tree)


                    else:
                        break #loop167





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 58, logicalORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpressionNoIn

    class logicalANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:289:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
    def logicalANDExpression(self, ):

        retval = self.logicalANDExpression_return()
        retval.start = self.input.LT(1)
        logicalANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT340 = None
        string_literal341 = None
        LT342 = None
        bitwiseORExpression339 = None

        bitwiseORExpression343 = None


        LT340_tree = None
        string_literal341_tree = None
        LT342_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1862)
                bitwiseORExpression339 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression339.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop170
                    alt170 = 2
                    alt170 = self.dfa170.predict(self.input)
                    if alt170 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:27: ( LT )*
                        while True: #loop168
                            alt168 = 2
                            LA168_0 = self.input.LA(1)

                            if (LA168_0 == LT) :
                                alt168 = 1


                            if alt168 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT340 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1865)
                                if self.failed:
                                    return retval


                            else:
                                break #loop168


                        string_literal341 = self.input.LT(1)
                        self.match(self.input, 84, self.FOLLOW_84_in_logicalANDExpression1869)
                        if self.failed:
                            return retval

                        string_literal341_tree = self.adaptor.createWithPayload(string_literal341)
                        self.adaptor.addChild(root_0, string_literal341_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:37: ( LT )*
                        while True: #loop169
                            alt169 = 2
                            LA169_0 = self.input.LA(1)

                            if (LA169_0 == LT) :
                                alt169 = 1


                            if alt169 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT342 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1871)
                                if self.failed:
                                    return retval


                            else:
                                break #loop169


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1875)
                        bitwiseORExpression343 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression343.tree)


                    else:
                        break #loop170





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 59, logicalANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpression

    class logicalANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:293:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
    def logicalANDExpressionNoIn(self, ):

        retval = self.logicalANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT345 = None
        string_literal346 = None
        LT347 = None
        bitwiseORExpressionNoIn344 = None

        bitwiseORExpressionNoIn348 = None


        LT345_tree = None
        string_literal346_tree = None
        LT347_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1889)
                bitwiseORExpressionNoIn344 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn344.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop173
                    alt173 = 2
                    alt173 = self.dfa173.predict(self.input)
                    if alt173 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:31: ( LT )*
                        while True: #loop171
                            alt171 = 2
                            LA171_0 = self.input.LA(1)

                            if (LA171_0 == LT) :
                                alt171 = 1


                            if alt171 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT345 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1892)
                                if self.failed:
                                    return retval


                            else:
                                break #loop171


                        string_literal346 = self.input.LT(1)
                        self.match(self.input, 84, self.FOLLOW_84_in_logicalANDExpressionNoIn1896)
                        if self.failed:
                            return retval

                        string_literal346_tree = self.adaptor.createWithPayload(string_literal346)
                        self.adaptor.addChild(root_0, string_literal346_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:41: ( LT )*
                        while True: #loop172
                            alt172 = 2
                            LA172_0 = self.input.LA(1)

                            if (LA172_0 == LT) :
                                alt172 = 1


                            if alt172 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT347 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1898)
                                if self.failed:
                                    return retval


                            else:
                                break #loop172


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1902)
                        bitwiseORExpressionNoIn348 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn348.tree)


                    else:
                        break #loop173





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 60, logicalANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpressionNoIn

    class bitwiseORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:297:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
    def bitwiseORExpression(self, ):

        retval = self.bitwiseORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseORExpression_StartIndex = self.input.index()
        root_0 = None

        LT350 = None
        char_literal351 = None
        LT352 = None
        bitwiseXORExpression349 = None

        bitwiseXORExpression353 = None


        LT350_tree = None
        char_literal351_tree = None
        LT352_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1916)
                bitwiseXORExpression349 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression349.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop176
                    alt176 = 2
                    alt176 = self.dfa176.predict(self.input)
                    if alt176 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:28: ( LT )*
                        while True: #loop174
                            alt174 = 2
                            LA174_0 = self.input.LA(1)

                            if (LA174_0 == LT) :
                                alt174 = 1


                            if alt174 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT350 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression1919)
                                if self.failed:
                                    return retval


                            else:
                                break #loop174


                        char_literal351 = self.input.LT(1)
                        self.match(self.input, 85, self.FOLLOW_85_in_bitwiseORExpression1923)
                        if self.failed:
                            return retval

                        char_literal351_tree = self.adaptor.createWithPayload(char_literal351)
                        self.adaptor.addChild(root_0, char_literal351_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:37: ( LT )*
                        while True: #loop175
                            alt175 = 2
                            LA175_0 = self.input.LA(1)

                            if (LA175_0 == LT) :
                                alt175 = 1


                            if alt175 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT352 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression1925)
                                if self.failed:
                                    return retval


                            else:
                                break #loop175


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1929)
                        bitwiseXORExpression353 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression353.tree)


                    else:
                        break #loop176





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 61, bitwiseORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpression

    class bitwiseORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:301:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
    def bitwiseORExpressionNoIn(self, ):

        retval = self.bitwiseORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT355 = None
        char_literal356 = None
        LT357 = None
        bitwiseXORExpressionNoIn354 = None

        bitwiseXORExpressionNoIn358 = None


        LT355_tree = None
        char_literal356_tree = None
        LT357_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1943)
                bitwiseXORExpressionNoIn354 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn354.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop179
                    alt179 = 2
                    alt179 = self.dfa179.predict(self.input)
                    if alt179 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:32: ( LT )*
                        while True: #loop177
                            alt177 = 2
                            LA177_0 = self.input.LA(1)

                            if (LA177_0 == LT) :
                                alt177 = 1


                            if alt177 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT355 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn1946)
                                if self.failed:
                                    return retval


                            else:
                                break #loop177


                        char_literal356 = self.input.LT(1)
                        self.match(self.input, 85, self.FOLLOW_85_in_bitwiseORExpressionNoIn1950)
                        if self.failed:
                            return retval

                        char_literal356_tree = self.adaptor.createWithPayload(char_literal356)
                        self.adaptor.addChild(root_0, char_literal356_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:41: ( LT )*
                        while True: #loop178
                            alt178 = 2
                            LA178_0 = self.input.LA(1)

                            if (LA178_0 == LT) :
                                alt178 = 1


                            if alt178 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT357 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn1952)
                                if self.failed:
                                    return retval


                            else:
                                break #loop178


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1956)
                        bitwiseXORExpressionNoIn358 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn358.tree)


                    else:
                        break #loop179





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 62, bitwiseORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpressionNoIn

    class bitwiseXORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:305:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
    def bitwiseXORExpression(self, ):

        retval = self.bitwiseXORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpression_StartIndex = self.input.index()
        root_0 = None

        LT360 = None
        char_literal361 = None
        LT362 = None
        bitwiseANDExpression359 = None

        bitwiseANDExpression363 = None


        LT360_tree = None
        char_literal361_tree = None
        LT362_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1970)
                bitwiseANDExpression359 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression359.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop182
                    alt182 = 2
                    alt182 = self.dfa182.predict(self.input)
                    if alt182 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:28: ( LT )*
                        while True: #loop180
                            alt180 = 2
                            LA180_0 = self.input.LA(1)

                            if (LA180_0 == LT) :
                                alt180 = 1


                            if alt180 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT360 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression1973)
                                if self.failed:
                                    return retval


                            else:
                                break #loop180


                        char_literal361 = self.input.LT(1)
                        self.match(self.input, 86, self.FOLLOW_86_in_bitwiseXORExpression1977)
                        if self.failed:
                            return retval

                        char_literal361_tree = self.adaptor.createWithPayload(char_literal361)
                        self.adaptor.addChild(root_0, char_literal361_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:37: ( LT )*
                        while True: #loop181
                            alt181 = 2
                            LA181_0 = self.input.LA(1)

                            if (LA181_0 == LT) :
                                alt181 = 1


                            if alt181 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT362 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression1979)
                                if self.failed:
                                    return retval


                            else:
                                break #loop181


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1983)
                        bitwiseANDExpression363 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression363.tree)


                    else:
                        break #loop182





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 63, bitwiseXORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpression

    class bitwiseXORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:309:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
    def bitwiseXORExpressionNoIn(self, ):

        retval = self.bitwiseXORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT365 = None
        char_literal366 = None
        LT367 = None
        bitwiseANDExpressionNoIn364 = None

        bitwiseANDExpressionNoIn368 = None


        LT365_tree = None
        char_literal366_tree = None
        LT367_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1997)
                bitwiseANDExpressionNoIn364 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn364.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop185
                    alt185 = 2
                    alt185 = self.dfa185.predict(self.input)
                    if alt185 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:32: ( LT )*
                        while True: #loop183
                            alt183 = 2
                            LA183_0 = self.input.LA(1)

                            if (LA183_0 == LT) :
                                alt183 = 1


                            if alt183 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT365 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2000)
                                if self.failed:
                                    return retval


                            else:
                                break #loop183


                        char_literal366 = self.input.LT(1)
                        self.match(self.input, 86, self.FOLLOW_86_in_bitwiseXORExpressionNoIn2004)
                        if self.failed:
                            return retval

                        char_literal366_tree = self.adaptor.createWithPayload(char_literal366)
                        self.adaptor.addChild(root_0, char_literal366_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:41: ( LT )*
                        while True: #loop184
                            alt184 = 2
                            LA184_0 = self.input.LA(1)

                            if (LA184_0 == LT) :
                                alt184 = 1


                            if alt184 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT367 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2006)
                                if self.failed:
                                    return retval


                            else:
                                break #loop184


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2010)
                        bitwiseANDExpressionNoIn368 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn368.tree)


                    else:
                        break #loop185





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 64, bitwiseXORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpressionNoIn

    class bitwiseANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:313:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
    def bitwiseANDExpression(self, ):

        retval = self.bitwiseANDExpression_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT370 = None
        char_literal371 = None
        LT372 = None
        equalityExpression369 = None

        equalityExpression373 = None


        LT370_tree = None
        char_literal371_tree = None
        LT372_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2024)
                equalityExpression369 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression369.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop188
                    alt188 = 2
                    alt188 = self.dfa188.predict(self.input)
                    if alt188 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:26: ( LT )*
                        while True: #loop186
                            alt186 = 2
                            LA186_0 = self.input.LA(1)

                            if (LA186_0 == LT) :
                                alt186 = 1


                            if alt186 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT370 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2027)
                                if self.failed:
                                    return retval


                            else:
                                break #loop186


                        char_literal371 = self.input.LT(1)
                        self.match(self.input, 87, self.FOLLOW_87_in_bitwiseANDExpression2031)
                        if self.failed:
                            return retval

                        char_literal371_tree = self.adaptor.createWithPayload(char_literal371)
                        self.adaptor.addChild(root_0, char_literal371_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:35: ( LT )*
                        while True: #loop187
                            alt187 = 2
                            LA187_0 = self.input.LA(1)

                            if (LA187_0 == LT) :
                                alt187 = 1


                            if alt187 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT372 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2033)
                                if self.failed:
                                    return retval


                            else:
                                break #loop187


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2037)
                        equalityExpression373 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression373.tree)


                    else:
                        break #loop188





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 65, bitwiseANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpression

    class bitwiseANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:317:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
    def bitwiseANDExpressionNoIn(self, ):

        retval = self.bitwiseANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT375 = None
        char_literal376 = None
        LT377 = None
        equalityExpressionNoIn374 = None

        equalityExpressionNoIn378 = None


        LT375_tree = None
        char_literal376_tree = None
        LT377_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2051)
                equalityExpressionNoIn374 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn374.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop191
                    alt191 = 2
                    alt191 = self.dfa191.predict(self.input)
                    if alt191 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:30: ( LT )*
                        while True: #loop189
                            alt189 = 2
                            LA189_0 = self.input.LA(1)

                            if (LA189_0 == LT) :
                                alt189 = 1


                            if alt189 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT375 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2054)
                                if self.failed:
                                    return retval


                            else:
                                break #loop189


                        char_literal376 = self.input.LT(1)
                        self.match(self.input, 87, self.FOLLOW_87_in_bitwiseANDExpressionNoIn2058)
                        if self.failed:
                            return retval

                        char_literal376_tree = self.adaptor.createWithPayload(char_literal376)
                        self.adaptor.addChild(root_0, char_literal376_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:39: ( LT )*
                        while True: #loop190
                            alt190 = 2
                            LA190_0 = self.input.LA(1)

                            if (LA190_0 == LT) :
                                alt190 = 1


                            if alt190 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT377 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2060)
                                if self.failed:
                                    return retval


                            else:
                                break #loop190


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2064)
                        equalityExpressionNoIn378 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn378.tree)


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
                self.memoize(self.input, 66, bitwiseANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpressionNoIn

    class equalityExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:321:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        LT380 = None
        set381 = None
        LT382 = None
        relationalExpression379 = None

        relationalExpression383 = None


        LT380_tree = None
        set381_tree = None
        LT382_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2078)
                relationalExpression379 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression379.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop194
                    alt194 = 2
                    alt194 = self.dfa194.predict(self.input)
                    if alt194 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:28: ( LT )*
                        while True: #loop192
                            alt192 = 2
                            LA192_0 = self.input.LA(1)

                            if (LA192_0 == LT) :
                                alt192 = 1


                            if alt192 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT380 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2081)
                                if self.failed:
                                    return retval


                            else:
                                break #loop192


                        set381 = self.input.LT(1)
                        if (88 <= self.input.LA(1) <= 91):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set381))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2085
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:63: ( LT )*
                        while True: #loop193
                            alt193 = 2
                            LA193_0 = self.input.LA(1)

                            if (LA193_0 == LT) :
                                alt193 = 1


                            if alt193 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT382 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2101)
                                if self.failed:
                                    return retval


                            else:
                                break #loop193


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2105)
                        relationalExpression383 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression383.tree)


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
                self.memoize(self.input, 67, equalityExpression_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpression

    class equalityExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:325:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
    def equalityExpressionNoIn(self, ):

        retval = self.equalityExpressionNoIn_return()
        retval.start = self.input.LT(1)
        equalityExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT385 = None
        set386 = None
        LT387 = None
        relationalExpressionNoIn384 = None

        relationalExpressionNoIn388 = None


        LT385_tree = None
        set386_tree = None
        LT387_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2118)
                relationalExpressionNoIn384 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn384.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop197
                    alt197 = 2
                    alt197 = self.dfa197.predict(self.input)
                    if alt197 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:32: ( LT )*
                        while True: #loop195
                            alt195 = 2
                            LA195_0 = self.input.LA(1)

                            if (LA195_0 == LT) :
                                alt195 = 1


                            if alt195 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT385 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2121)
                                if self.failed:
                                    return retval


                            else:
                                break #loop195


                        set386 = self.input.LT(1)
                        if (88 <= self.input.LA(1) <= 91):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set386))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn2125
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:67: ( LT )*
                        while True: #loop196
                            alt196 = 2
                            LA196_0 = self.input.LA(1)

                            if (LA196_0 == LT) :
                                alt196 = 1


                            if alt196 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT387 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2141)
                                if self.failed:
                                    return retval


                            else:
                                break #loop196


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2145)
                        relationalExpressionNoIn388 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn388.tree)


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
                self.memoize(self.input, 68, equalityExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpressionNoIn

    class relationalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:329:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LT390 = None
        set391 = None
        LT392 = None
        shiftExpression389 = None

        shiftExpression393 = None


        LT390_tree = None
        set391_tree = None
        LT392_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2159)
                shiftExpression389 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression389.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop200
                    alt200 = 2
                    alt200 = self.dfa200.predict(self.input)
                    if alt200 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:23: ( LT )*
                        while True: #loop198
                            alt198 = 2
                            LA198_0 = self.input.LA(1)

                            if (LA198_0 == LT) :
                                alt198 = 1


                            if alt198 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT390 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2162)
                                if self.failed:
                                    return retval


                            else:
                                break #loop198


                        set391 = self.input.LT(1)
                        if self.input.LA(1) == 54 or (92 <= self.input.LA(1) <= 96):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set391))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpression2166
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:76: ( LT )*
                        while True: #loop199
                            alt199 = 2
                            LA199_0 = self.input.LA(1)

                            if (LA199_0 == LT) :
                                alt199 = 1


                            if alt199 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT392 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2190)
                                if self.failed:
                                    return retval


                            else:
                                break #loop199


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2194)
                        shiftExpression393 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression393.tree)


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
                self.memoize(self.input, 69, relationalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpression

    class relationalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:333:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
    def relationalExpressionNoIn(self, ):

        retval = self.relationalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        relationalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT395 = None
        set396 = None
        LT397 = None
        shiftExpression394 = None

        shiftExpression398 = None


        LT395_tree = None
        set396_tree = None
        LT397_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2207)
                shiftExpression394 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression394.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop203
                    alt203 = 2
                    alt203 = self.dfa203.predict(self.input)
                    if alt203 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:23: ( LT )*
                        while True: #loop201
                            alt201 = 2
                            LA201_0 = self.input.LA(1)

                            if (LA201_0 == LT) :
                                alt201 = 1


                            if alt201 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT395 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2210)
                                if self.failed:
                                    return retval


                            else:
                                break #loop201


                        set396 = self.input.LT(1)
                        if (92 <= self.input.LA(1) <= 96):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set396))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn2214
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:69: ( LT )*
                        while True: #loop202
                            alt202 = 2
                            LA202_0 = self.input.LA(1)

                            if (LA202_0 == LT) :
                                alt202 = 1


                            if alt202 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT397 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2234)
                                if self.failed:
                                    return retval


                            else:
                                break #loop202


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2238)
                        shiftExpression398 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression398.tree)


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
                self.memoize(self.input, 70, relationalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpressionNoIn

    class shiftExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start shiftExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:337:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        LT400 = None
        set401 = None
        LT402 = None
        additiveExpression399 = None

        additiveExpression403 = None


        LT400_tree = None
        set401_tree = None
        LT402_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2251)
                additiveExpression399 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression399.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop206
                    alt206 = 2
                    alt206 = self.dfa206.predict(self.input)
                    if alt206 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:26: ( LT )*
                        while True: #loop204
                            alt204 = 2
                            LA204_0 = self.input.LA(1)

                            if (LA204_0 == LT) :
                                alt204 = 1


                            if alt204 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT400 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2254)
                                if self.failed:
                                    return retval


                            else:
                                break #loop204


                        set401 = self.input.LT(1)
                        if (97 <= self.input.LA(1) <= 99):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set401))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_shiftExpression2258
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:53: ( LT )*
                        while True: #loop205
                            alt205 = 2
                            LA205_0 = self.input.LA(1)

                            if (LA205_0 == LT) :
                                alt205 = 1


                            if alt205 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT402 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2270)
                                if self.failed:
                                    return retval


                            else:
                                break #loop205


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2274)
                        additiveExpression403 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression403.tree)


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
                self.memoize(self.input, 71, shiftExpression_StartIndex)

            pass

        return retval

    # $ANTLR end shiftExpression

    class additiveExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start additiveExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:341:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        LT405 = None
        set406 = None
        LT407 = None
        multiplicativeExpression404 = None

        multiplicativeExpression408 = None


        LT405_tree = None
        set406_tree = None
        LT407_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2287)
                multiplicativeExpression404 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression404.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop209
                    alt209 = 2
                    LA209_0 = self.input.LA(1)

                    if (LA209_0 == LT) :
                        LA209_1 = self.input.LA(2)

                        if (self.synpred262()) :
                            alt209 = 1


                    elif ((100 <= LA209_0 <= 101)) :
                        alt209 = 1


                    if alt209 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:32: ( LT )*
                        while True: #loop207
                            alt207 = 2
                            LA207_0 = self.input.LA(1)

                            if (LA207_0 == LT) :
                                alt207 = 1


                            if alt207 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT405 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2290)
                                if self.failed:
                                    return retval


                            else:
                                break #loop207


                        set406 = self.input.LT(1)
                        if (100 <= self.input.LA(1) <= 101):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set406))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_additiveExpression2294
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:49: ( LT )*
                        while True: #loop208
                            alt208 = 2
                            LA208_0 = self.input.LA(1)

                            if (LA208_0 == LT) :
                                alt208 = 1


                            if alt208 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT407 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2302)
                                if self.failed:
                                    return retval


                            else:
                                break #loop208


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2306)
                        multiplicativeExpression408 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression408.tree)


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
                self.memoize(self.input, 72, additiveExpression_StartIndex)

            pass

        return retval

    # $ANTLR end additiveExpression

    class multiplicativeExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start multiplicativeExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:345:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        LT410 = None
        set411 = None
        LT412 = None
        unaryExpression409 = None

        unaryExpression413 = None


        LT410_tree = None
        set411_tree = None
        LT412_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2319)
                unaryExpression409 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression409.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop212
                    alt212 = 2
                    alt212 = self.dfa212.predict(self.input)
                    if alt212 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:23: ( LT )*
                        while True: #loop210
                            alt210 = 2
                            LA210_0 = self.input.LA(1)

                            if (LA210_0 == LT) :
                                alt210 = 1


                            if alt210 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT410 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2322)
                                if self.failed:
                                    return retval


                            else:
                                break #loop210


                        set411 = self.input.LT(1)
                        if (102 <= self.input.LA(1) <= 104):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set411))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression2326
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:46: ( LT )*
                        while True: #loop211
                            alt211 = 2
                            LA211_0 = self.input.LA(1)

                            if (LA211_0 == LT) :
                                alt211 = 1


                            if alt211 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT412 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2338)
                                if self.failed:
                                    return retval


                            else:
                                break #loop211


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2342)
                        unaryExpression413 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression413.tree)


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
                self.memoize(self.input, 73, multiplicativeExpression_StartIndex)

            pass

        return retval

    # $ANTLR end multiplicativeExpression

    class unaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start unaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:349:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set415 = None
        postfixExpression414 = None

        unaryExpression416 = None


        set415_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt213 = 2
                LA213_0 = self.input.LA(1)

                if ((StringLiteral <= LA213_0 <= Identifier) or (38 <= LA213_0 <= 39) or LA213_0 == 42 or LA213_0 == 53 or (67 <= LA213_0 <= 68) or (112 <= LA213_0 <= 117)) :
                    alt213 = 1
                elif ((100 <= LA213_0 <= 101) or (105 <= LA213_0 <= 111)) :
                    alt213 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("349:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 213, 0, self.input)

                    raise nvae

                if alt213 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression2355)
                    postfixExpression414 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression414.tree)


                elif alt213 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set415 = self.input.LT(1)
                    if (100 <= self.input.LA(1) <= 101) or (105 <= self.input.LA(1) <= 111):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set415))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_unaryExpression2360
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression2396)
                    unaryExpression416 = self.unaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unaryExpression416.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 74, unaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end unaryExpression

    class postfixExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start postfixExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set418 = None
        leftHandSideExpression417 = None


        set418_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression2408)
                leftHandSideExpression417 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression417.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:27: ( '++' | '--' )?
                alt214 = 2
                LA214_0 = self.input.LA(1)

                if ((108 <= LA214_0 <= 109)) :
                    alt214 = 1
                if alt214 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set418 = self.input.LT(1)
                    if (108 <= self.input.LA(1) <= 109):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set418))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_postfixExpression2410
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
                self.memoize(self.input, 75, postfixExpression_StartIndex)

            pass

        return retval

    # $ANTLR end postfixExpression

    class primaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start primaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal419 = None
        char_literal424 = None
        LT425 = None
        LT427 = None
        char_literal428 = None
        identifier420 = None

        literal421 = None

        arrayLiteral422 = None

        objectLiteral423 = None

        expression426 = None


        string_literal419_tree = None
        char_literal424_tree = None
        LT425_tree = None
        LT427_tree = None
        char_literal428_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:2: ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt217 = 6
                LA217 = self.input.LA(1)
                if LA217 == 112:
                    alt217 = 1
                elif LA217 == Identifier or LA217 == 53 or LA217 == 113 or LA217 == 114:
                    alt217 = 2
                elif LA217 == StringLiteral or LA217 == NumericLiteral or LA217 == RegularExpressionLiteral or LA217 == 115 or LA217 == 116 or LA217 == 117:
                    alt217 = 3
                elif LA217 == 68:
                    alt217 = 4
                elif LA217 == 42:
                    alt217 = 5
                elif LA217 == 39:
                    alt217 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("358:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 217, 0, self.input)

                    raise nvae

                if alt217 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal419 = self.input.LT(1)
                    self.match(self.input, 112, self.FOLLOW_112_in_primaryExpression2428)
                    if self.failed:
                        return retval

                    string_literal419_tree = self.adaptor.createWithPayload(string_literal419)
                    self.adaptor.addChild(root_0, string_literal419_tree)



                elif alt217 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:360:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_primaryExpression2433)
                    identifier420 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier420.tree)


                elif alt217 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:361:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression2438)
                    literal421 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal421.tree)


                elif alt217 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:362:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression2443)
                    arrayLiteral422 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral422.tree)


                elif alt217 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression2448)
                    objectLiteral423 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral423.tree)


                elif alt217 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal424 = self.input.LT(1)
                    self.match(self.input, 39, self.FOLLOW_39_in_primaryExpression2453)
                    if self.failed:
                        return retval

                    char_literal424_tree = self.adaptor.createWithPayload(char_literal424)
                    self.adaptor.addChild(root_0, char_literal424_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:10: ( LT )*
                    while True: #loop215
                        alt215 = 2
                        LA215_0 = self.input.LA(1)

                        if (LA215_0 == LT) :
                            alt215 = 1


                        if alt215 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT425 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2455)
                            if self.failed:
                                return retval


                        else:
                            break #loop215


                    self.following.append(self.FOLLOW_expression_in_primaryExpression2459)
                    expression426 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression426.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:26: ( LT )*
                    while True: #loop216
                        alt216 = 2
                        LA216_0 = self.input.LA(1)

                        if (LA216_0 == LT) :
                            alt216 = 1


                        if alt216 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT427 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2461)
                            if self.failed:
                                return retval


                        else:
                            break #loop216


                    char_literal428 = self.input.LT(1)
                    self.match(self.input, 41, self.FOLLOW_41_in_primaryExpression2465)
                    if self.failed:
                        return retval

                    char_literal428_tree = self.adaptor.createWithPayload(char_literal428)
                    self.adaptor.addChild(root_0, char_literal428_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 76, primaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end primaryExpression

    class arrayLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arrayLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal429 = None
        LT430 = None
        LT432 = None
        char_literal433 = None
        LT434 = None
        LT436 = None
        char_literal437 = None
        assignmentExpression431 = None

        assignmentExpression435 = None


        char_literal429_tree = None
        LT430_tree = None
        LT432_tree = None
        char_literal433_tree = None
        LT434_tree = None
        LT436_tree = None
        char_literal437_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']'
                root_0 = self.adaptor.nil()

                char_literal429 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_arrayLiteral2478)
                if self.failed:
                    return retval

                char_literal429_tree = self.adaptor.createWithPayload(char_literal429)
                self.adaptor.addChild(root_0, char_literal429_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:10: ( LT )*
                while True: #loop218
                    alt218 = 2
                    LA218_0 = self.input.LA(1)

                    if (LA218_0 == LT) :
                        LA218_2 = self.input.LA(2)

                        if (self.synpred286()) :
                            alt218 = 1




                    if alt218 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT430 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2480)
                        if self.failed:
                            return retval


                    else:
                        break #loop218


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:13: ( assignmentExpression )?
                alt219 = 2
                LA219_0 = self.input.LA(1)

                if ((StringLiteral <= LA219_0 <= Identifier) or (38 <= LA219_0 <= 39) or LA219_0 == 42 or LA219_0 == 53 or (67 <= LA219_0 <= 68) or (100 <= LA219_0 <= 101) or (105 <= LA219_0 <= 117)) :
                    alt219 = 1
                if alt219 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2484)
                    assignmentExpression431 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression431.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop223
                    alt223 = 2
                    alt223 = self.dfa223.predict(self.input)
                    if alt223 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:36: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:38: ( LT )*
                        while True: #loop220
                            alt220 = 2
                            LA220_0 = self.input.LA(1)

                            if (LA220_0 == LT) :
                                alt220 = 1


                            if alt220 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT432 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2488)
                                if self.failed:
                                    return retval


                            else:
                                break #loop220


                        char_literal433 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_arrayLiteral2492)
                        if self.failed:
                            return retval

                        char_literal433_tree = self.adaptor.createWithPayload(char_literal433)
                        self.adaptor.addChild(root_0, char_literal433_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:45: ( ( LT )* assignmentExpression )?
                        alt222 = 2
                        alt222 = self.dfa222.predict(self.input)
                        if alt222 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:46: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:48: ( LT )*
                            while True: #loop221
                                alt221 = 2
                                LA221_0 = self.input.LA(1)

                                if (LA221_0 == LT) :
                                    alt221 = 1


                                if alt221 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT434 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2495)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop221


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2499)
                            assignmentExpression435 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression435.tree)





                    else:
                        break #loop223


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:78: ( LT )*
                while True: #loop224
                    alt224 = 2
                    LA224_0 = self.input.LA(1)

                    if (LA224_0 == LT) :
                        alt224 = 1


                    if alt224 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT436 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2505)
                        if self.failed:
                            return retval


                    else:
                        break #loop224


                char_literal437 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_arrayLiteral2509)
                if self.failed:
                    return retval

                char_literal437_tree = self.adaptor.createWithPayload(char_literal437)
                self.adaptor.addChild(root_0, char_literal437_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 77, arrayLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end arrayLiteral

    class objectLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start objectLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal438 = None
        LT439 = None
        LT441 = None
        char_literal442 = None
        LT443 = None
        LT445 = None
        char_literal446 = None
        propertyNameAndValue440 = None

        propertyNameAndValue444 = None


        char_literal438_tree = None
        LT439_tree = None
        LT441_tree = None
        char_literal442_tree = None
        LT443_tree = None
        LT445_tree = None
        char_literal446_tree = None
        stream_43 = RewriteRuleTokenStream(self.adaptor, "token 43")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_40 = RewriteRuleTokenStream(self.adaptor, "token 40")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}'
                char_literal438 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_objectLiteral2528)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_42.add(char_literal438)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: ( LT )*
                while True: #loop225
                    alt225 = 2
                    LA225_0 = self.input.LA(1)

                    if (LA225_0 == LT) :
                        LA225_2 = self.input.LA(2)

                        if (self.synpred293()) :
                            alt225 = 1




                    if alt225 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT439 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2530)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT439)


                    else:
                        break #loop225


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:12: ( propertyNameAndValue )?
                alt226 = 2
                LA226_0 = self.input.LA(1)

                if ((StringLiteral <= LA226_0 <= NumericLiteral) or LA226_0 == Identifier or LA226_0 == 53 or (113 <= LA226_0 <= 114)) :
                    alt226 = 1
                if alt226 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2533)
                    propertyNameAndValue440 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue440.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop229
                    alt229 = 2
                    alt229 = self.dfa229.predict(self.input)
                    if alt229 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:35: ( LT )*
                        while True: #loop227
                            alt227 = 2
                            LA227_0 = self.input.LA(1)

                            if (LA227_0 == LT) :
                                alt227 = 1


                            if alt227 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT441 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2537)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT441)


                            else:
                                break #loop227


                        char_literal442 = self.input.LT(1)
                        self.match(self.input, 40, self.FOLLOW_40_in_objectLiteral2540)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_40.add(char_literal442)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:43: ( LT )*
                        while True: #loop228
                            alt228 = 2
                            LA228_0 = self.input.LA(1)

                            if (LA228_0 == LT) :
                                alt228 = 1


                            if alt228 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT443 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2542)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT443)


                            else:
                                break #loop228


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2545)
                        propertyNameAndValue444 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue444.tree)


                    else:
                        break #loop229


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:70: ( LT )*
                while True: #loop230
                    alt230 = 2
                    LA230_0 = self.input.LA(1)

                    if (LA230_0 == LT) :
                        alt230 = 1


                    if alt230 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT445 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2549)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT445)


                    else:
                        break #loop230


                char_literal446 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_objectLiteral2552)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_43.add(char_literal446)
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
                    # 375:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:375:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:375:12: ( propertyNameAndValue )*
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
                self.memoize(self.input, 78, objectLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end objectLiteral

    class propertyNameAndValue_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyNameAndValue
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList functionBody ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList functionBody ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        action = None
        LT448 = None
        char_literal449 = None
        LT450 = None
        LT452 = None
        LT453 = None
        LT455 = None
        LT457 = None
        LT459 = None
        LT461 = None
        propname = None

        funcname = None

        propertyName447 = None

        assignmentExpression451 = None

        formalParameterList454 = None

        functionBody456 = None

        identifier458 = None

        formalParameterList460 = None

        functionBody462 = None


        action_tree = None
        LT448_tree = None
        char_literal449_tree = None
        LT450_tree = None
        LT452_tree = None
        LT453_tree = None
        LT455_tree = None
        LT457_tree = None
        LT459_tree = None
        LT461_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_59 = RewriteRuleTokenStream(self.adaptor, "token 59")
        stream_114 = RewriteRuleTokenStream(self.adaptor, "token 114")
        stream_113 = RewriteRuleTokenStream(self.adaptor, "token 113")
        stream_propertyName = RewriteRuleSubtreeStream(self.adaptor, "rule propertyName")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self.adaptor, "rule functionBody")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList functionBody ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList functionBody ) ) )
                alt241 = 3
                alt241 = self.dfa241.predict(self.input)
                if alt241 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue2576)
                    propertyName447 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName447.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:17: ( LT )*
                    while True: #loop231
                        alt231 = 2
                        LA231_0 = self.input.LA(1)

                        if (LA231_0 == LT) :
                            alt231 = 1


                        if alt231 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT448 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2578)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT448)


                        else:
                            break #loop231


                    char_literal449 = self.input.LT(1)
                    self.match(self.input, 59, self.FOLLOW_59_in_propertyNameAndValue2581)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_59.add(char_literal449)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:25: ( LT )*
                    while True: #loop232
                        alt232 = 2
                        LA232_0 = self.input.LA(1)

                        if (LA232_0 == LT) :
                            alt232 = 1


                        if alt232 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT450 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2583)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT450)


                        else:
                            break #loop232


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue2586)
                    assignmentExpression451 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression451.tree)
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
                        # 380:3: -> ^( PROP propertyName PROP assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:380:6: ^( PROP propertyName PROP assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, self.adaptor.createFromType(PROP, "PROP"))
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt241 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:4: (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* functionBody
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:4: (action= 'get' | action= 'set' )
                    alt233 = 2
                    LA233_0 = self.input.LA(1)

                    if (LA233_0 == 113) :
                        alt233 = 1
                    elif (LA233_0 == 114) :
                        alt233 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("381:4: (action= 'get' | action= 'set' )", 233, 0, self.input)

                        raise nvae

                    if alt233 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_propertyNameAndValue2608)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_113.add(action)


                    elif alt233 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_propertyNameAndValue2612)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_114.add(action)



                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2617)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:52: ( LT )*
                    while True: #loop234
                        alt234 = 2
                        LA234_0 = self.input.LA(1)

                        if (LA234_0 == LT) :
                            alt234 = 1


                        if alt234 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT452 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2619)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT452)


                        else:
                            break #loop234


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2624)
                    funcname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(funcname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:76: ( LT )*
                    while True: #loop235
                        alt235 = 2
                        LA235_0 = self.input.LA(1)

                        if (LA235_0 == LT) :
                            alt235 = 1


                        if alt235 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT453 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2626)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT453)


                        else:
                            break #loop235


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue2629)
                    formalParameterList454 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList454.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:381:100: ( LT )*
                    while True: #loop236
                        alt236 = 2
                        LA236_0 = self.input.LA(1)

                        if (LA236_0 == LT) :
                            alt236 = 1


                        if alt236 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT455 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2631)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT455)


                        else:
                            break #loop236


                    self.following.append(self.FOLLOW_functionBody_in_propertyNameAndValue2634)
                    functionBody456 = self.functionBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_functionBody.add(functionBody456.tree)
                    # AST Rewrite
                    # elements: action, formalParameterList, propname, functionBody, funcname
                    # token labels: action
                    # rule labels: retval, funcname, propname
                    # token list labels: 
                    # rule list labels: 
                    if self.backtracking == 0:

                        retval.tree = root_0
                        stream_action = RewriteRuleTokenStream(self.adaptor, "token action", action)

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self.adaptor, "token retval", None)


                        if funcname is not None:
                            stream_funcname = RewriteRuleSubtreeStream(self.adaptor, "token funcname", funcname.tree)
                        else:
                            stream_funcname = RewriteRuleSubtreeStream(self.adaptor, "token funcname", None)


                        if propname is not None:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", propname.tree)
                        else:
                            stream_propname = RewriteRuleSubtreeStream(self.adaptor, "token propname", None)


                        root_0 = self.adaptor.nil()
                        # 382:3: -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList functionBody ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:6: ^( PROP $propname $action ^( FUNC $funcname formalParameterList functionBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:31: ^( FUNC $funcname formalParameterList functionBody )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_funcname.next())
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_functionBody.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                elif alt241 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:4: (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:4: (action= 'get' | action= 'set' )
                    alt237 = 2
                    LA237_0 = self.input.LA(1)

                    if (LA237_0 == 113) :
                        alt237 = 1
                    elif (LA237_0 == 114) :
                        alt237 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("383:4: (action= 'get' | action= 'set' )", 237, 0, self.input)

                        raise nvae

                    if alt237 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_propertyNameAndValue2667)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_113.add(action)


                    elif alt237 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 114, self.FOLLOW_114_in_propertyNameAndValue2671)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_114.add(action)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:32: ( LT )*
                    while True: #loop238
                        alt238 = 2
                        LA238_0 = self.input.LA(1)

                        if (LA238_0 == LT) :
                            alt238 = 1


                        if alt238 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT457 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2674)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT457)


                        else:
                            break #loop238


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2677)
                    identifier458 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier458.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:47: ( LT )*
                    while True: #loop239
                        alt239 = 2
                        LA239_0 = self.input.LA(1)

                        if (LA239_0 == LT) :
                            alt239 = 1


                        if alt239 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT459 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2679)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT459)


                        else:
                            break #loop239


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue2682)
                    formalParameterList460 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList460.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:71: ( LT )*
                    while True: #loop240
                        alt240 = 2
                        LA240_0 = self.input.LA(1)

                        if (LA240_0 == LT) :
                            alt240 = 1


                        if alt240 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT461 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2684)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT461)


                        else:
                            break #loop240


                    self.following.append(self.FOLLOW_functionBody_in_propertyNameAndValue2687)
                    functionBody462 = self.functionBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_functionBody.add(functionBody462.tree)
                    # AST Rewrite
                    # elements: identifier, action, functionBody, formalParameterList
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
                        # 384:3: -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList functionBody ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:6: ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList functionBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:32: ^( FUNC ANONYMOUS formalParameterList functionBody )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, self.adaptor.createFromType(ANONYMOUS, "ANONYMOUS"))
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_functionBody.next())

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
                self.memoize(self.input, 79, propertyNameAndValue_StartIndex)

            pass

        return retval

    # $ANTLR end propertyNameAndValue

    class propertyName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:387:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral464 = None
        NumericLiteral465 = None
        identifier463 = None


        StringLiteral464_tree = None
        NumericLiteral465_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:2: ( identifier | StringLiteral | NumericLiteral )
                alt242 = 3
                LA242 = self.input.LA(1)
                if LA242 == Identifier or LA242 == 53 or LA242 == 113 or LA242 == 114:
                    alt242 = 1
                elif LA242 == StringLiteral:
                    alt242 = 2
                elif LA242 == NumericLiteral:
                    alt242 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("387:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 242, 0, self.input)

                    raise nvae

                if alt242 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName2721)
                    identifier463 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier463.tree)


                elif alt242 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral464 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName2726)
                    if self.failed:
                        return retval

                    StringLiteral464_tree = self.adaptor.createWithPayload(StringLiteral464)
                    self.adaptor.addChild(root_0, StringLiteral464_tree)



                elif alt242 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral465 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName2731)
                    if self.failed:
                        return retval

                    NumericLiteral465_tree = self.adaptor.createWithPayload(NumericLiteral465)
                    self.adaptor.addChild(root_0, NumericLiteral465_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 80, propertyName_StartIndex)

            pass

        return retval

    # $ANTLR end propertyName

    class literal_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start literal
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:394:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | RegularExpressionLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        set466 = None

        set466_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:395:2: ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | RegularExpressionLiteral )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set466 = self.input.LT(1)
                if (StringLiteral <= self.input.LA(1) <= RegularExpressionLiteral) or (115 <= self.input.LA(1) <= 117):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set466))
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_literal0
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
                self.memoize(self.input, 81, literal_StartIndex)

            pass

        return retval

    # $ANTLR end literal

    class regularExpressionLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start regularExpressionLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:1: regularExpressionLiteral : '/' RegularExpressionLiteral '/' Identifier ;
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal467 = None
        RegularExpressionLiteral468 = None
        char_literal469 = None
        Identifier470 = None

        char_literal467_tree = None
        RegularExpressionLiteral468_tree = None
        char_literal469_tree = None
        Identifier470_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:2: ( '/' RegularExpressionLiteral '/' Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:4: '/' RegularExpressionLiteral '/' Identifier
                root_0 = self.adaptor.nil()

                char_literal467 = self.input.LT(1)
                self.match(self.input, 103, self.FOLLOW_103_in_regularExpressionLiteral2779)
                if self.failed:
                    return retval

                char_literal467_tree = self.adaptor.createWithPayload(char_literal467)
                self.adaptor.addChild(root_0, char_literal467_tree)

                RegularExpressionLiteral468 = self.input.LT(1)
                self.match(self.input, RegularExpressionLiteral, self.FOLLOW_RegularExpressionLiteral_in_regularExpressionLiteral2781)
                if self.failed:
                    return retval

                RegularExpressionLiteral468_tree = self.adaptor.createWithPayload(RegularExpressionLiteral468)
                self.adaptor.addChild(root_0, RegularExpressionLiteral468_tree)

                char_literal469 = self.input.LT(1)
                self.match(self.input, 103, self.FOLLOW_103_in_regularExpressionLiteral2783)
                if self.failed:
                    return retval

                char_literal469_tree = self.adaptor.createWithPayload(char_literal469)
                self.adaptor.addChild(root_0, char_literal469_tree)

                Identifier470 = self.input.LT(1)
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral2785)
                if self.failed:
                    return retval

                Identifier470_tree = self.adaptor.createWithPayload(Identifier470)
                self.adaptor.addChild(root_0, Identifier470_tree)




                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 82, regularExpressionLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end regularExpressionLiteral

    class identifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start identifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:409:1: identifier : ( 'get' | 'set' | 'each' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set471 = None

        set471_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:410:2: ( 'get' | 'set' | 'each' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set471 = self.input.LT(1)
                if self.input.LA(1) == Identifier or self.input.LA(1) == 53 or (113 <= self.input.LA(1) <= 114):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set471))
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
                self.memoize(self.input, 83, identifier_StartIndex)

            pass

        return retval

    # $ANTLR end identifier

    # $ANTLR start synpred4
    def synpred4_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:19: ( ( LT )* sourceElement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:19: ( LT )* sourceElement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:21: ( LT )*
        while True: #loop243
            alt243 = 2
            LA243_0 = self.input.LA(1)

            if (LA243_0 == LT) :
                alt243 = 1


            if alt243 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred490)
                if self.failed:
                    return 


            else:
                break #loop243


        self.following.append(self.FOLLOW_sourceElement_in_synpred494)
        self.sourceElement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred4



    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: ( functionDeclaration )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: functionDeclaration
        self.following.append(self.FOLLOW_functionDeclaration_in_synpred5108)
        self.functionDeclaration()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred21
    def synpred21_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred21280)
        if self.failed:
            return 


    # $ANTLR end synpred21



    # $ANTLR start synpred24
    def synpred24_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred24303)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred24



    # $ANTLR start synpred27
    def synpred27_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:63:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:63:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred27318)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred27



    # $ANTLR start synpred34
    def synpred34_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:70:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:70:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred34353)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred34



    # $ANTLR start synpred37
    def synpred37_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred37382)
        if self.failed:
            return 


    # $ANTLR end synpred37



    # $ANTLR start synpred64
    def synpred64_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:61: ( LT )*
        while True: #loop260
            alt260 = 2
            LA260_0 = self.input.LA(1)

            if (LA260_0 == LT) :
                alt260 = 1


            if alt260 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred64648)
                if self.failed:
                    return 


            else:
                break #loop260


        self.match(self.input, 49, self.FOLLOW_49_in_synpred64652)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:73: ( LT )*
        while True: #loop261
            alt261 = 2
            LA261_0 = self.input.LA(1)

            if (LA261_0 == LT) :
                alt261 = 1


            if alt261 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred64654)
                if self.failed:
                    return 


            else:
                break #loop261


        self.following.append(self.FOLLOW_statement_in_synpred64658)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred64



    # $ANTLR start synpred67
    def synpred67_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred67682)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred67



    # $ANTLR start synpred89
    def synpred89_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred89872)
        if self.failed:
            return 


    # $ANTLR end synpred89



    # $ANTLR start synpred124
    def synpred124_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1241170)
        if self.failed:
            return 


    # $ANTLR end synpred124



    # $ANTLR start synpred127
    def synpred127_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1271195)
        if self.failed:
            return 


    # $ANTLR end synpred127



    # $ANTLR start synpred146
    def synpred146_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:4: ( conditionalExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:219:4: conditionalExpression
        self.following.append(self.FOLLOW_conditionalExpression_in_synpred1461387)
        self.conditionalExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred146



    # $ANTLR start synpred149
    def synpred149_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:4: ( conditionalExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:4: conditionalExpressionNoIn
        self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_synpred1491416)
        self.conditionalExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred149



    # $ANTLR start synpred152
    def synpred152_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred1521445)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred152



    # $ANTLR start synpred153
    def synpred153_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred1531462)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred153



    # $ANTLR start synpred160
    def synpred160_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:91: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:91: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:93: ( LT )*
        while True: #loop275
            alt275 = 2
            LA275_0 = self.input.LA(1)

            if (LA275_0 == LT) :
                alt275 = 1


            if alt275 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1601510)
                if self.failed:
                    return 


            else:
                break #loop275


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1601514)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred160



    # $ANTLR start synpred164
    def synpred164_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:37: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:37: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:39: ( LT )*
        while True: #loop276
            alt276 = 2
            LA276_0 = self.input.LA(1)

            if (LA276_0 == LT) :
                alt276 = 1


            if alt276 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1641553)
                if self.failed:
                    return 


            else:
                break #loop276


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred1641557)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred164



    # $ANTLR start synpred262
    def synpred262_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:32: ( LT )*
        while True: #loop321
            alt321 = 2
            LA321_0 = self.input.LA(1)

            if (LA321_0 == LT) :
                alt321 = 1


            if alt321 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2622290)
                if self.failed:
                    return 


            else:
                break #loop321


        if (100 <= self.input.LA(1) <= 101):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2622294
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:49: ( LT )*
        while True: #loop322
            alt322 = 2
            LA322_0 = self.input.LA(1)

            if (LA322_0 == LT) :
                alt322 = 1


            if alt322 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2622302)
                if self.failed:
                    return 


            else:
                break #loop322


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred2622306)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred262



    # $ANTLR start synpred286
    def synpred286_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2862480)
        if self.failed:
            return 


    # $ANTLR end synpred286



    # $ANTLR start synpred293
    def synpred293_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:374:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2932530)
        if self.failed:
            return 


    # $ANTLR end synpred293



    def synpred152(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred152_fragment()
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

    def synpred160(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred160_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred37(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred37_fragment()
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

    def synpred293(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred293_fragment()
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

    def synpred124(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred124_fragment()
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

    def synpred89(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred89_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred21(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred21_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred4(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred4_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred27(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred27_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred127(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred127_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred67(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred67_fragment()
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

    def synpred24(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred24_fragment()
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

    def synpred149(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred149_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred153(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred153_fragment()
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



    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\11\1\10\1\uffff\12\10\1\0\2\10\1\0\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\165\1\162\1\uffff\1\162\2\47\2\162\1\51\1\52\1\51\1\162\1\52"
        u"\1\0\1\162\1\51\1\0\2\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\2\uffff\1\2\16\uffff\2\1"
        )

    DFA5_special = DFA.unpack(
        u"\15\uffff\1\1\2\uffff\1\0\2\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\4\2\31\uffff\1\1\1\2\2\uffff\1\2\1\uffff\3\2\1\uffff"
        u"\1\2\1\uffff\4\2\1\uffff\4\2\1\uffff\1\2\2\uffff\2\2\2\uffff\2"
        u"\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\3\3\uffff\1\4\32\uffff\1\2\15\uffff\1\4\73\uffff"
        u"\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\3\uffff\1\4\32\uffff\1\2\15\uffff\1\4\73\uffff"
        u"\2\4"),
        DFA.unpack(u"\1\5\36\uffff\1\6"),
        DFA.unpack(u"\1\5\36\uffff\1\6"),
        DFA.unpack(u"\1\7\3\uffff\1\10\34\uffff\1\11\13\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u"\1\7\3\uffff\1\10\34\uffff\1\11\13\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u"\1\12\37\uffff\1\13\1\11"),
        DFA.unpack(u"\1\14\41\uffff\1\15"),
        DFA.unpack(u"\1\12\37\uffff\1\13\1\11"),
        DFA.unpack(u"\1\16\3\uffff\1\17\50\uffff\1\17\73\uffff\2\17"),
        DFA.unpack(u"\1\14\41\uffff\1\20"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\16\3\uffff\1\17\50\uffff\1\17\73\uffff\2\17"),
        DFA.unpack(u"\1\12\37\uffff\1\13\1\11"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA5_16 = input.LA(1)

                 
                index5_16 = input.index()
                input.rewind()
                s = -1
                if (self.synpred5()):
                    s = 18

                elif (True):
                    s = 2

                 
                input.seek(index5_16)
                if s >= 0:
                    return s
            elif s == 1: 
                LA5_13 = input.LA(1)

                 
                index5_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred5()):
                    s = 17

                elif (True):
                    s = 2

                 
                input.seek(index5_13)
                if s >= 0:
                    return s

            if self.backtracking >0:
                self.failed = True
                return -1
            nvae = NoViableAltException(self_.getDescription(), 5, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\46\2\10\2\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\46\2\162\2\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA14_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\3\uffff\1\4\32\uffff\1\3\15\uffff\1\4\73\uffff"
        u"\2\4"),
        DFA.unpack(u"\1\2\3\uffff\1\4\32\uffff\1\3\15\uffff\1\4\73\uffff"
        u"\2\4"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #14

    DFA14 = DFA
    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA19_max = DFA.unpack(
        u"\2\162\2\uffff"
        )

    DFA19_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA19_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA19_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
        u"\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #19

    DFA19 = DFA
    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\2\51\2\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA18_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    DFA18 = DFA
    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA29_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA29_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA29_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\3\uffff\15\3"),
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #29

    DFA29 = DFA
    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\2"
        )

    DFA33_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA33_max = DFA.unpack(
        u"\1\56\1\165\2\uffff\1\165"
        )

    DFA33_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA33_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA33_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #33

    DFA33 = DFA
    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA36_max = DFA.unpack(
        u"\2\56\2\uffff"
        )

    DFA36_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA36_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #36

    DFA36 = DFA
    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA38_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA38_max = DFA.unpack(
        u"\1\57\1\165\2\uffff\1\165"
        )

    DFA38_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA38_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2"),
        DFA.unpack(u"\1\4\4\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\3\uffff\15\3")
    ]

    # class definition for DFA #38

    DFA38 = DFA
    # lookup tables for DFA #40

    DFA40_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA40_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA40_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA40_max = DFA.unpack(
        u"\2\66\2\uffff"
        )

    DFA40_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA40_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA40_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #40

    DFA40 = DFA
    # lookup tables for DFA #60

    DFA60_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA60_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA60_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA60_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA60_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA60_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA60_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #60

    DFA60 = DFA
    # lookup tables for DFA #63

    DFA63_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA63_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA63_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA63_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA63_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA63_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA63_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #63

    DFA63 = DFA
    # lookup tables for DFA #66

    DFA66_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA66_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA66_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA66_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA66_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA66_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA66_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #66

    DFA66 = DFA
    # lookup tables for DFA #95

    DFA95_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA95_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA95_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA95_max = DFA.unpack(
        u"\2\76\2\uffff"
        )

    DFA95_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA95_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA95_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #95

    DFA95 = DFA
    # lookup tables for DFA #99

    DFA99_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA99_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA99_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA99_max = DFA.unpack(
        u"\2\76\2\uffff"
        )

    DFA99_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA99_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA99_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u"\1\1\42\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #99

    DFA99 = DFA
    # lookup tables for DFA #98

    DFA98_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA98_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA98_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA98_max = DFA.unpack(
        u"\2\75\2\uffff"
        )

    DFA98_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA98_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA98_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #98

    DFA98 = DFA
    # lookup tables for DFA #111

    DFA111_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA111_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA111_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA111_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA111_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA111_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA111_transition = [
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #111

    DFA111 = DFA
    # lookup tables for DFA #120

    DFA120_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA120_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA120_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA120_max = DFA.unpack(
        u"\1\105\1\165\2\uffff\1\165"
        )

    DFA120_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA120_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA120_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2\4\uffff\1\2\14\uffff\1\2\11\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #120

    DFA120 = DFA
    # lookup tables for DFA #123

    DFA123_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA123_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA123_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA123_max = DFA.unpack(
        u"\2\56\2\uffff"
        )

    DFA123_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA123_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA123_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #123

    DFA123 = DFA
    # lookup tables for DFA #147

    DFA147_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA147_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA147_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA147_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA147_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA147_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA147_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #147

    DFA147 = DFA
    # lookup tables for DFA #146

    DFA146_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA146_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA146_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA146_max = DFA.unpack(
        u"\2\51\2\uffff"
        )

    DFA146_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA146_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA146_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #146

    DFA146 = DFA
    # lookup tables for DFA #156

    DFA156_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA156_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA156_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA156_max = DFA.unpack(
        u"\1\122\1\165\2\uffff\1\165"
        )

    DFA156_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA156_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA156_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\3\1\uffff\1\3\2\uffff\1\3\14\uffff\1"
        u"\3\11\uffff\1\3\14\uffff\1\2"),
        DFA.unpack(u"\1\4\4\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\3\uffff\15\3")
    ]

    # class definition for DFA #156

    DFA156 = DFA
    # lookup tables for DFA #161

    DFA161_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA161_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA161_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA161_max = DFA.unpack(
        u"\2\122\2\uffff"
        )

    DFA161_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA161_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA161_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #161

    DFA161 = DFA
    # lookup tables for DFA #164

    DFA164_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA164_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA164_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA164_max = DFA.unpack(
        u"\1\123\1\165\2\uffff\1\165"
        )

    DFA164_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA164_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA164_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\1\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #164

    DFA164 = DFA
    # lookup tables for DFA #167

    DFA167_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA167_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA167_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA167_max = DFA.unpack(
        u"\2\123\2\uffff"
        )

    DFA167_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA167_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA167_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #167

    DFA167 = DFA
    # lookup tables for DFA #170

    DFA170_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA170_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA170_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA170_max = DFA.unpack(
        u"\1\124\1\165\2\uffff\1\165"
        )

    DFA170_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA170_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA170_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\2\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #170

    DFA170 = DFA
    # lookup tables for DFA #173

    DFA173_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA173_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA173_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA173_max = DFA.unpack(
        u"\2\124\2\uffff"
        )

    DFA173_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA173_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA173_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #173

    DFA173 = DFA
    # lookup tables for DFA #176

    DFA176_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA176_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA176_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA176_max = DFA.unpack(
        u"\1\125\1\165\2\uffff\1\165"
        )

    DFA176_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA176_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA176_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\3\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #176

    DFA176 = DFA
    # lookup tables for DFA #179

    DFA179_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA179_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA179_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA179_max = DFA.unpack(
        u"\2\125\2\uffff"
        )

    DFA179_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA179_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA179_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #179

    DFA179 = DFA
    # lookup tables for DFA #182

    DFA182_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA182_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA182_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA182_max = DFA.unpack(
        u"\1\126\1\165\2\uffff\1\165"
        )

    DFA182_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA182_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA182_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\4\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #182

    DFA182 = DFA
    # lookup tables for DFA #185

    DFA185_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA185_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA185_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA185_max = DFA.unpack(
        u"\2\126\2\uffff"
        )

    DFA185_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA185_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA185_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #185

    DFA185 = DFA
    # lookup tables for DFA #188

    DFA188_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA188_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA188_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA188_max = DFA.unpack(
        u"\1\127\1\165\2\uffff\1\165"
        )

    DFA188_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA188_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA188_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\5\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #188

    DFA188 = DFA
    # lookup tables for DFA #191

    DFA191_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA191_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA191_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA191_max = DFA.unpack(
        u"\2\127\2\uffff"
        )

    DFA191_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA191_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA191_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #191

    DFA191 = DFA
    # lookup tables for DFA #194

    DFA194_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA194_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA194_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA194_max = DFA.unpack(
        u"\1\133\1\165\2\uffff\1\165"
        )

    DFA194_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA194_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA194_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\6\2\4\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #194

    DFA194 = DFA
    # lookup tables for DFA #197

    DFA197_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA197_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA197_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA197_max = DFA.unpack(
        u"\2\133\2\uffff"
        )

    DFA197_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA197_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA197_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #197

    DFA197 = DFA
    # lookup tables for DFA #200

    DFA200_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA200_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA200_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA200_max = DFA.unpack(
        u"\1\140\1\165\2\uffff\1\165"
        )

    DFA200_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA200_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA200_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\3\4\uffff\1\2\11\uffff\1\2\14\uffff\12\2\5\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #200

    DFA200 = DFA
    # lookup tables for DFA #203

    DFA203_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA203_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA203_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA203_max = DFA.unpack(
        u"\2\140\2\uffff"
        )

    DFA203_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA203_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA203_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #203

    DFA203 = DFA
    # lookup tables for DFA #206

    DFA206_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA206_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA206_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA206_max = DFA.unpack(
        u"\1\143\1\165\2\uffff\1\165"
        )

    DFA206_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA206_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA206_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\4\uffff\1\2\11\uffff\1\2\14\uffff\17\2\3\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #206

    DFA206 = DFA
    # lookup tables for DFA #212

    DFA212_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA212_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA212_min = DFA.unpack(
        u"\2\10\2\uffff\1\10"
        )

    DFA212_max = DFA.unpack(
        u"\1\150\1\165\2\uffff\1\165"
        )

    DFA212_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA212_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA212_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\4\uffff\1\2\11\uffff\1\2\14\uffff\24\2\3\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\24\2\3\3\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\24\2\3\3\15\2")
    ]

    # class definition for DFA #212

    DFA212 = DFA
    # lookup tables for DFA #223

    DFA223_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA223_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA223_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA223_max = DFA.unpack(
        u"\2\105\2\uffff"
        )

    DFA223_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA223_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA223_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #223

    DFA223 = DFA
    # lookup tables for DFA #222

    DFA222_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA222_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA222_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA222_max = DFA.unpack(
        u"\2\165\2\uffff"
        )

    DFA222_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA222_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA222_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #222

    DFA222 = DFA
    # lookup tables for DFA #229

    DFA229_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA229_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA229_min = DFA.unpack(
        u"\2\10\2\uffff"
        )

    DFA229_max = DFA.unpack(
        u"\2\53\2\uffff"
        )

    DFA229_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA229_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA229_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #229

    DFA229 = DFA
    # lookup tables for DFA #241

    DFA241_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA241_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA241_min = DFA.unpack(
        u"\1\11\1\10\1\uffff\4\10\2\uffff"
        )

    DFA241_max = DFA.unpack(
        u"\2\162\1\uffff\4\162\2\uffff"
        )

    DFA241_accept = DFA.unpack(
        u"\2\uffff\1\1\4\uffff\1\3\1\2"
        )

    DFA241_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA241_transition = [
        DFA.unpack(u"\2\2\1\uffff\1\2\50\uffff\1\2\73\uffff\1\1\1\3"),
        DFA.unpack(u"\1\5\3\uffff\1\4\50\uffff\1\4\5\uffff\1\2\65\uffff\2"
        u"\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\3\uffff\1\4\50\uffff\1\4\5\uffff\1\2\65\uffff\2"
        u"\4"),
        DFA.unpack(u"\1\6\3\uffff\1\10\32\uffff\1\7\15\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u"\1\5\3\uffff\1\7\50\uffff\1\7\5\uffff\1\2\65\uffff\2"
        u"\7"),
        DFA.unpack(u"\1\6\3\uffff\1\10\32\uffff\1\7\15\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #241

    DFA241 = DFA
 

    FOLLOW_LT_in_program64 = frozenset([1])
    FOLLOW_sourceElements_in_program68 = frozenset([8])
    FOLLOW_LT_in_program70 = frozenset([1])
    FOLLOW_EOF_in_program74 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements87 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_sourceElements90 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_sourceElement_in_sourceElements94 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_functionDeclaration_in_sourceElement108 = frozenset([1])
    FOLLOW_statement_in_sourceElement113 = frozenset([1])
    FOLLOW_38_in_functionDeclaration126 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_functionDeclaration128 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_functionDeclaration131 = frozenset([8, 39])
    FOLLOW_LT_in_functionDeclaration133 = frozenset([8, 39])
    FOLLOW_formalParameterList_in_functionDeclaration136 = frozenset([8, 42])
    FOLLOW_LT_in_functionDeclaration138 = frozenset([8, 42])
    FOLLOW_functionBody_in_functionDeclaration141 = frozenset([1])
    FOLLOW_38_in_functionExpression167 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_functionExpression169 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_functionExpression172 = frozenset([8, 39])
    FOLLOW_LT_in_functionExpression174 = frozenset([8, 39])
    FOLLOW_formalParameterList_in_functionExpression177 = frozenset([8, 42])
    FOLLOW_LT_in_functionExpression179 = frozenset([8, 42])
    FOLLOW_functionBody_in_functionExpression182 = frozenset([1])
    FOLLOW_38_in_functionExpression201 = frozenset([8, 39])
    FOLLOW_LT_in_functionExpression203 = frozenset([8, 39])
    FOLLOW_formalParameterList_in_functionExpression206 = frozenset([8, 42])
    FOLLOW_LT_in_functionExpression208 = frozenset([8, 42])
    FOLLOW_functionBody_in_functionExpression211 = frozenset([1])
    FOLLOW_39_in_formalParameterList237 = frozenset([8, 12, 41, 53, 113, 114])
    FOLLOW_LT_in_formalParameterList240 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_formalParameterList244 = frozenset([8, 40, 41])
    FOLLOW_LT_in_formalParameterList247 = frozenset([8, 40])
    FOLLOW_40_in_formalParameterList251 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_formalParameterList253 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_formalParameterList257 = frozenset([8, 40, 41])
    FOLLOW_LT_in_formalParameterList263 = frozenset([1])
    FOLLOW_41_in_formalParameterList267 = frozenset([1])
    FOLLOW_42_in_functionBody278 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 43, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_functionBody280 = frozenset([1])
    FOLLOW_sourceElements_in_functionBody284 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 43, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_functionBody287 = frozenset([1])
    FOLLOW_43_in_functionBody291 = frozenset([1])
    FOLLOW_statementBlock_in_statement303 = frozenset([1])
    FOLLOW_variableStatement_in_statement308 = frozenset([1])
    FOLLOW_emptyStatement_in_statement313 = frozenset([1])
    FOLLOW_expressionStatement_in_statement318 = frozenset([1])
    FOLLOW_ifStatement_in_statement323 = frozenset([1])
    FOLLOW_iterationStatement_in_statement328 = frozenset([1])
    FOLLOW_continueStatement_in_statement333 = frozenset([1])
    FOLLOW_breakStatement_in_statement338 = frozenset([1])
    FOLLOW_returnStatement_in_statement343 = frozenset([1])
    FOLLOW_withStatement_in_statement348 = frozenset([1])
    FOLLOW_labelledStatement_in_statement353 = frozenset([1])
    FOLLOW_switchStatement_in_statement358 = frozenset([1])
    FOLLOW_throwStatement_in_statement363 = frozenset([1])
    FOLLOW_tryStatement_in_statement368 = frozenset([1])
    FOLLOW_42_in_statementBlock380 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 43, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_statementBlock382 = frozenset([1])
    FOLLOW_statementList_in_statementBlock386 = frozenset([8, 43])
    FOLLOW_LT_in_statementBlock389 = frozenset([1])
    FOLLOW_43_in_statementBlock393 = frozenset([1])
    FOLLOW_statement_in_statementList405 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_statementList408 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_statement_in_statementList412 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_set_in_variableStatement426 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_variableStatement432 = frozenset([1])
    FOLLOW_variableDeclarationList_in_variableStatement436 = frozenset([8, 46])
    FOLLOW_set_in_variableStatement438 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList456 = frozenset([1, 8, 40])
    FOLLOW_LT_in_variableDeclarationList459 = frozenset([8, 40])
    FOLLOW_40_in_variableDeclarationList463 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_variableDeclarationList465 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_variableDeclaration_in_variableDeclarationList469 = frozenset([1, 8, 40])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn483 = frozenset([1, 8, 40])
    FOLLOW_LT_in_variableDeclarationListNoIn486 = frozenset([8, 40])
    FOLLOW_40_in_variableDeclarationListNoIn490 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_variableDeclarationListNoIn492 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn496 = frozenset([1, 8, 40])
    FOLLOW_identifier_in_variableDeclaration510 = frozenset([1, 8, 47])
    FOLLOW_LT_in_variableDeclaration513 = frozenset([8, 47])
    FOLLOW_initialiser_in_variableDeclaration517 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn531 = frozenset([1, 8, 47])
    FOLLOW_LT_in_variableDeclarationNoIn534 = frozenset([8, 47])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn538 = frozenset([1])
    FOLLOW_47_in_initialiser552 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_initialiser554 = frozenset([1])
    FOLLOW_assignmentExpression_in_initialiser558 = frozenset([1])
    FOLLOW_47_in_initialiserNoIn570 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_initialiserNoIn572 = frozenset([1])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn576 = frozenset([1])
    FOLLOW_46_in_emptyStatement588 = frozenset([1])
    FOLLOW_expression_in_expressionStatement600 = frozenset([8, 46])
    FOLLOW_set_in_expressionStatement602 = frozenset([1])
    FOLLOW_48_in_ifStatement621 = frozenset([8, 39])
    FOLLOW_LT_in_ifStatement623 = frozenset([1])
    FOLLOW_39_in_ifStatement627 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_ifStatement629 = frozenset([1])
    FOLLOW_expression_in_ifStatement633 = frozenset([8, 41])
    FOLLOW_LT_in_ifStatement635 = frozenset([1])
    FOLLOW_41_in_ifStatement639 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_ifStatement641 = frozenset([1])
    FOLLOW_statement_in_ifStatement645 = frozenset([1, 8, 49])
    FOLLOW_LT_in_ifStatement648 = frozenset([8, 49])
    FOLLOW_49_in_ifStatement652 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_ifStatement654 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_statement_in_ifStatement658 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement672 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement677 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement682 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement687 = frozenset([1])
    FOLLOW_50_in_doWhileStatement699 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_doWhileStatement701 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement705 = frozenset([8, 51])
    FOLLOW_LT_in_doWhileStatement707 = frozenset([1])
    FOLLOW_51_in_doWhileStatement711 = frozenset([8, 39])
    FOLLOW_LT_in_doWhileStatement713 = frozenset([1])
    FOLLOW_39_in_doWhileStatement717 = frozenset([9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_expression_in_doWhileStatement719 = frozenset([41])
    FOLLOW_41_in_doWhileStatement721 = frozenset([8, 46])
    FOLLOW_set_in_doWhileStatement723 = frozenset([1])
    FOLLOW_51_in_whileStatement742 = frozenset([8, 39])
    FOLLOW_LT_in_whileStatement744 = frozenset([1])
    FOLLOW_39_in_whileStatement748 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_whileStatement750 = frozenset([1])
    FOLLOW_expression_in_whileStatement754 = frozenset([8, 41])
    FOLLOW_LT_in_whileStatement756 = frozenset([1])
    FOLLOW_41_in_whileStatement760 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_whileStatement762 = frozenset([1])
    FOLLOW_statement_in_whileStatement766 = frozenset([1])
    FOLLOW_52_in_forStatement778 = frozenset([8, 39])
    FOLLOW_LT_in_forStatement780 = frozenset([1])
    FOLLOW_39_in_forStatement784 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 46, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forStatement787 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_forStatementInitialiserPart_in_forStatement791 = frozenset([8, 46])
    FOLLOW_LT_in_forStatement795 = frozenset([1])
    FOLLOW_46_in_forStatement799 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 46, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forStatement802 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_expression_in_forStatement806 = frozenset([8, 46])
    FOLLOW_LT_in_forStatement810 = frozenset([1])
    FOLLOW_46_in_forStatement814 = frozenset([8, 9, 10, 11, 12, 38, 39, 41, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forStatement817 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_expression_in_forStatement821 = frozenset([8, 41])
    FOLLOW_LT_in_forStatement825 = frozenset([1])
    FOLLOW_41_in_forStatement829 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forStatement831 = frozenset([1])
    FOLLOW_statement_in_forStatement835 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart847 = frozenset([1])
    FOLLOW_44_in_forStatementInitialiserPart852 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_forStatementInitialiserPart854 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart858 = frozenset([1])
    FOLLOW_52_in_forInStatement870 = frozenset([8, 39, 53])
    FOLLOW_LT_in_forInStatement872 = frozenset([1])
    FOLLOW_53_in_forInStatement876 = frozenset([8, 39])
    FOLLOW_LT_in_forInStatement879 = frozenset([1])
    FOLLOW_39_in_forInStatement883 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 53, 67, 68, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forInStatement885 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement889 = frozenset([8, 54])
    FOLLOW_LT_in_forInStatement891 = frozenset([1])
    FOLLOW_54_in_forInStatement895 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forInStatement897 = frozenset([1])
    FOLLOW_expression_in_forInStatement901 = frozenset([8, 41])
    FOLLOW_LT_in_forInStatement903 = frozenset([1])
    FOLLOW_41_in_forInStatement907 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_forInStatement909 = frozenset([1])
    FOLLOW_statement_in_forInStatement913 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart925 = frozenset([1])
    FOLLOW_44_in_forInStatementInitialiserPart930 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_forInStatementInitialiserPart932 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart936 = frozenset([1])
    FOLLOW_55_in_continueStatement947 = frozenset([8, 12, 46, 53, 113, 114])
    FOLLOW_identifier_in_continueStatement949 = frozenset([8, 46])
    FOLLOW_set_in_continueStatement952 = frozenset([1])
    FOLLOW_56_in_breakStatement970 = frozenset([8, 12, 46, 53, 113, 114])
    FOLLOW_identifier_in_breakStatement972 = frozenset([8, 46])
    FOLLOW_set_in_breakStatement975 = frozenset([1])
    FOLLOW_57_in_returnStatement993 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 46, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_expression_in_returnStatement995 = frozenset([8, 46])
    FOLLOW_set_in_returnStatement998 = frozenset([1])
    FOLLOW_58_in_withStatement1017 = frozenset([8, 39])
    FOLLOW_LT_in_withStatement1019 = frozenset([1])
    FOLLOW_39_in_withStatement1023 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_withStatement1025 = frozenset([1])
    FOLLOW_expression_in_withStatement1029 = frozenset([8, 41])
    FOLLOW_LT_in_withStatement1031 = frozenset([1])
    FOLLOW_41_in_withStatement1035 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_withStatement1037 = frozenset([1])
    FOLLOW_statement_in_withStatement1041 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1052 = frozenset([8, 59])
    FOLLOW_LT_in_labelledStatement1054 = frozenset([1])
    FOLLOW_59_in_labelledStatement1058 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_labelledStatement1060 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1064 = frozenset([1])
    FOLLOW_60_in_switchStatement1076 = frozenset([8, 39])
    FOLLOW_LT_in_switchStatement1078 = frozenset([1])
    FOLLOW_39_in_switchStatement1082 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_switchStatement1084 = frozenset([1])
    FOLLOW_expression_in_switchStatement1088 = frozenset([8, 41])
    FOLLOW_LT_in_switchStatement1090 = frozenset([1])
    FOLLOW_41_in_switchStatement1094 = frozenset([8, 42])
    FOLLOW_LT_in_switchStatement1096 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1100 = frozenset([1])
    FOLLOW_42_in_caseBlock1112 = frozenset([8, 43, 61, 62])
    FOLLOW_LT_in_caseBlock1115 = frozenset([8, 61])
    FOLLOW_caseClause_in_caseBlock1119 = frozenset([8, 43, 61, 62])
    FOLLOW_LT_in_caseBlock1124 = frozenset([8, 62])
    FOLLOW_defaultClause_in_caseBlock1128 = frozenset([8, 43, 61])
    FOLLOW_LT_in_caseBlock1131 = frozenset([8, 61])
    FOLLOW_caseClause_in_caseBlock1135 = frozenset([8, 43, 61])
    FOLLOW_LT_in_caseBlock1141 = frozenset([1])
    FOLLOW_43_in_caseBlock1145 = frozenset([1])
    FOLLOW_61_in_caseClause1156 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_caseClause1158 = frozenset([1])
    FOLLOW_expression_in_caseClause1162 = frozenset([8, 59])
    FOLLOW_LT_in_caseClause1164 = frozenset([1])
    FOLLOW_59_in_caseClause1168 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_caseClause1170 = frozenset([1])
    FOLLOW_statementList_in_caseClause1174 = frozenset([1])
    FOLLOW_62_in_defaultClause1187 = frozenset([8, 59])
    FOLLOW_LT_in_defaultClause1189 = frozenset([1])
    FOLLOW_59_in_defaultClause1193 = frozenset([1, 8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_defaultClause1195 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1199 = frozenset([1])
    FOLLOW_63_in_throwStatement1212 = frozenset([9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_expression_in_throwStatement1214 = frozenset([8, 46])
    FOLLOW_set_in_throwStatement1216 = frozenset([1])
    FOLLOW_64_in_tryStatement1234 = frozenset([8, 42])
    FOLLOW_LT_in_tryStatement1236 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1240 = frozenset([8, 65, 66])
    FOLLOW_LT_in_tryStatement1242 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1247 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1251 = frozenset([1, 8, 66])
    FOLLOW_LT_in_tryStatement1254 = frozenset([8, 66])
    FOLLOW_finallyClause_in_tryStatement1258 = frozenset([1])
    FOLLOW_65_in_catchClause1279 = frozenset([8, 39])
    FOLLOW_LT_in_catchClause1281 = frozenset([1])
    FOLLOW_39_in_catchClause1285 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_catchClause1287 = frozenset([1])
    FOLLOW_identifier_in_catchClause1291 = frozenset([8, 41])
    FOLLOW_LT_in_catchClause1293 = frozenset([1])
    FOLLOW_41_in_catchClause1297 = frozenset([8, 42])
    FOLLOW_LT_in_catchClause1299 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1303 = frozenset([1])
    FOLLOW_66_in_finallyClause1315 = frozenset([8, 42])
    FOLLOW_LT_in_finallyClause1317 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause1321 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1333 = frozenset([1, 8, 40])
    FOLLOW_LT_in_expression1336 = frozenset([8, 40])
    FOLLOW_40_in_expression1340 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_expression1342 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_expression1346 = frozenset([1, 8, 40])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1360 = frozenset([1, 8, 40])
    FOLLOW_LT_in_expressionNoIn1363 = frozenset([8, 40])
    FOLLOW_40_in_expressionNoIn1367 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_expressionNoIn1369 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1373 = frozenset([1, 8, 40])
    FOLLOW_conditionalExpression_in_assignmentExpression1387 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1392 = frozenset([8, 47, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_LT_in_assignmentExpression1394 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpression1398 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_assignmentExpression1400 = frozenset([1])
    FOLLOW_assignmentExpression_in_assignmentExpression1404 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1416 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1421 = frozenset([8, 47, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81])
    FOLLOW_LT_in_assignmentExpressionNoIn1423 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1427 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_assignmentExpressionNoIn1429 = frozenset([1])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1433 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression1445 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression1450 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1462 = frozenset([1])
    FOLLOW_67_in_newExpression1467 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_newExpression1469 = frozenset([1])
    FOLLOW_newExpression_in_newExpression1473 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1486 = frozenset([1, 8, 68, 70])
    FOLLOW_functionExpression_in_memberExpression1490 = frozenset([1, 8, 68, 70])
    FOLLOW_67_in_memberExpression1494 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_memberExpression1496 = frozenset([1])
    FOLLOW_memberExpression_in_memberExpression1500 = frozenset([8, 39])
    FOLLOW_LT_in_memberExpression1502 = frozenset([1])
    FOLLOW_arguments_in_memberExpression1506 = frozenset([1, 8, 68, 70])
    FOLLOW_LT_in_memberExpression1510 = frozenset([8, 68, 70])
    FOLLOW_memberExpressionSuffix_in_memberExpression1514 = frozenset([1, 8, 68, 70])
    FOLLOW_indexSuffix_in_memberExpressionSuffix1528 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1533 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression1544 = frozenset([8, 39])
    FOLLOW_LT_in_callExpression1546 = frozenset([1])
    FOLLOW_arguments_in_callExpression1550 = frozenset([1, 8, 39, 68, 70])
    FOLLOW_LT_in_callExpression1553 = frozenset([8, 39, 68, 70])
    FOLLOW_callExpressionSuffix_in_callExpression1557 = frozenset([1, 8, 39, 68, 70])
    FOLLOW_arguments_in_callExpressionSuffix1571 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix1576 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1581 = frozenset([1])
    FOLLOW_39_in_arguments1592 = frozenset([8, 9, 10, 11, 12, 38, 39, 41, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_arguments1595 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_arguments1599 = frozenset([8, 40, 41])
    FOLLOW_LT_in_arguments1602 = frozenset([8, 40])
    FOLLOW_40_in_arguments1606 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_arguments1608 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_arguments1612 = frozenset([8, 40, 41])
    FOLLOW_LT_in_arguments1618 = frozenset([1])
    FOLLOW_41_in_arguments1622 = frozenset([1])
    FOLLOW_68_in_indexSuffix1634 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_indexSuffix1636 = frozenset([1])
    FOLLOW_expression_in_indexSuffix1640 = frozenset([8, 69])
    FOLLOW_LT_in_indexSuffix1642 = frozenset([1])
    FOLLOW_69_in_indexSuffix1646 = frozenset([1])
    FOLLOW_70_in_propertyReferenceSuffix1659 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_propertyReferenceSuffix1661 = frozenset([1])
    FOLLOW_identifier_in_propertyReferenceSuffix1665 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression1732 = frozenset([1, 8, 82])
    FOLLOW_LT_in_conditionalExpression1735 = frozenset([8, 82])
    FOLLOW_82_in_conditionalExpression1739 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_conditionalExpression1741 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_conditionalExpression1745 = frozenset([8, 59])
    FOLLOW_LT_in_conditionalExpression1747 = frozenset([8, 59])
    FOLLOW_59_in_conditionalExpression1751 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_conditionalExpression1753 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_conditionalExpression1757 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1770 = frozenset([1, 8, 82])
    FOLLOW_LT_in_conditionalExpressionNoIn1773 = frozenset([8, 82])
    FOLLOW_82_in_conditionalExpressionNoIn1777 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_conditionalExpressionNoIn1779 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1783 = frozenset([8, 59])
    FOLLOW_LT_in_conditionalExpressionNoIn1785 = frozenset([8, 59])
    FOLLOW_59_in_conditionalExpressionNoIn1789 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_conditionalExpressionNoIn1791 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1795 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression1808 = frozenset([1, 8, 83])
    FOLLOW_LT_in_logicalORExpression1811 = frozenset([8, 83])
    FOLLOW_83_in_logicalORExpression1815 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_logicalORExpression1817 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_logicalANDExpression_in_logicalORExpression1821 = frozenset([1, 8, 83])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1835 = frozenset([1, 8, 83])
    FOLLOW_LT_in_logicalORExpressionNoIn1838 = frozenset([8, 83])
    FOLLOW_83_in_logicalORExpressionNoIn1842 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_logicalORExpressionNoIn1844 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1848 = frozenset([1, 8, 83])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1862 = frozenset([1, 8, 84])
    FOLLOW_LT_in_logicalANDExpression1865 = frozenset([8, 84])
    FOLLOW_84_in_logicalANDExpression1869 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_logicalANDExpression1871 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1875 = frozenset([1, 8, 84])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1889 = frozenset([1, 8, 84])
    FOLLOW_LT_in_logicalANDExpressionNoIn1892 = frozenset([8, 84])
    FOLLOW_84_in_logicalANDExpressionNoIn1896 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_logicalANDExpressionNoIn1898 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1902 = frozenset([1, 8, 84])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1916 = frozenset([1, 8, 85])
    FOLLOW_LT_in_bitwiseORExpression1919 = frozenset([8, 85])
    FOLLOW_85_in_bitwiseORExpression1923 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseORExpression1925 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1929 = frozenset([1, 8, 85])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1943 = frozenset([1, 8, 85])
    FOLLOW_LT_in_bitwiseORExpressionNoIn1946 = frozenset([8, 85])
    FOLLOW_85_in_bitwiseORExpressionNoIn1950 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseORExpressionNoIn1952 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1956 = frozenset([1, 8, 85])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1970 = frozenset([1, 8, 86])
    FOLLOW_LT_in_bitwiseXORExpression1973 = frozenset([8, 86])
    FOLLOW_86_in_bitwiseXORExpression1977 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseXORExpression1979 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1983 = frozenset([1, 8, 86])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1997 = frozenset([1, 8, 86])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2000 = frozenset([8, 86])
    FOLLOW_86_in_bitwiseXORExpressionNoIn2004 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2006 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2010 = frozenset([1, 8, 86])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2024 = frozenset([1, 8, 87])
    FOLLOW_LT_in_bitwiseANDExpression2027 = frozenset([8, 87])
    FOLLOW_87_in_bitwiseANDExpression2031 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseANDExpression2033 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2037 = frozenset([1, 8, 87])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2051 = frozenset([1, 8, 87])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2054 = frozenset([8, 87])
    FOLLOW_87_in_bitwiseANDExpressionNoIn2058 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2060 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2064 = frozenset([1, 8, 87])
    FOLLOW_relationalExpression_in_equalityExpression2078 = frozenset([1, 8, 88, 89, 90, 91])
    FOLLOW_LT_in_equalityExpression2081 = frozenset([8, 88, 89, 90, 91])
    FOLLOW_set_in_equalityExpression2085 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_equalityExpression2101 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_relationalExpression_in_equalityExpression2105 = frozenset([1, 8, 88, 89, 90, 91])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2118 = frozenset([1, 8, 88, 89, 90, 91])
    FOLLOW_LT_in_equalityExpressionNoIn2121 = frozenset([8, 88, 89, 90, 91])
    FOLLOW_set_in_equalityExpressionNoIn2125 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_equalityExpressionNoIn2141 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2145 = frozenset([1, 8, 88, 89, 90, 91])
    FOLLOW_shiftExpression_in_relationalExpression2159 = frozenset([1, 8, 54, 92, 93, 94, 95, 96])
    FOLLOW_LT_in_relationalExpression2162 = frozenset([8, 54, 92, 93, 94, 95, 96])
    FOLLOW_set_in_relationalExpression2166 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_relationalExpression2190 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_shiftExpression_in_relationalExpression2194 = frozenset([1, 8, 54, 92, 93, 94, 95, 96])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2207 = frozenset([1, 8, 92, 93, 94, 95, 96])
    FOLLOW_LT_in_relationalExpressionNoIn2210 = frozenset([8, 92, 93, 94, 95, 96])
    FOLLOW_set_in_relationalExpressionNoIn2214 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_relationalExpressionNoIn2234 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2238 = frozenset([1, 8, 92, 93, 94, 95, 96])
    FOLLOW_additiveExpression_in_shiftExpression2251 = frozenset([1, 8, 97, 98, 99])
    FOLLOW_LT_in_shiftExpression2254 = frozenset([8, 97, 98, 99])
    FOLLOW_set_in_shiftExpression2258 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_shiftExpression2270 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_additiveExpression_in_shiftExpression2274 = frozenset([1, 8, 97, 98, 99])
    FOLLOW_multiplicativeExpression_in_additiveExpression2287 = frozenset([1, 8, 100, 101])
    FOLLOW_LT_in_additiveExpression2290 = frozenset([8, 100, 101])
    FOLLOW_set_in_additiveExpression2294 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_additiveExpression2302 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_multiplicativeExpression_in_additiveExpression2306 = frozenset([1, 8, 100, 101])
    FOLLOW_unaryExpression_in_multiplicativeExpression2319 = frozenset([1, 8, 102, 103, 104])
    FOLLOW_LT_in_multiplicativeExpression2322 = frozenset([8, 102, 103, 104])
    FOLLOW_set_in_multiplicativeExpression2326 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_multiplicativeExpression2338 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_unaryExpression_in_multiplicativeExpression2342 = frozenset([1, 8, 102, 103, 104])
    FOLLOW_postfixExpression_in_unaryExpression2355 = frozenset([1])
    FOLLOW_set_in_unaryExpression2360 = frozenset([9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_unaryExpression_in_unaryExpression2396 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression2408 = frozenset([1, 108, 109])
    FOLLOW_set_in_postfixExpression2410 = frozenset([1])
    FOLLOW_112_in_primaryExpression2428 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression2433 = frozenset([1])
    FOLLOW_literal_in_primaryExpression2438 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression2443 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression2448 = frozenset([1])
    FOLLOW_39_in_primaryExpression2453 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_primaryExpression2455 = frozenset([1])
    FOLLOW_expression_in_primaryExpression2459 = frozenset([8, 41])
    FOLLOW_LT_in_primaryExpression2461 = frozenset([1])
    FOLLOW_41_in_primaryExpression2465 = frozenset([1])
    FOLLOW_68_in_arrayLiteral2478 = frozenset([8, 9, 10, 11, 12, 38, 39, 40, 42, 53, 67, 68, 69, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_arrayLiteral2480 = frozenset([1])
    FOLLOW_assignmentExpression_in_arrayLiteral2484 = frozenset([8, 40, 69])
    FOLLOW_LT_in_arrayLiteral2488 = frozenset([8, 40])
    FOLLOW_40_in_arrayLiteral2492 = frozenset([8, 9, 10, 11, 12, 38, 39, 40, 42, 53, 67, 68, 69, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_arrayLiteral2495 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_arrayLiteral2499 = frozenset([8, 40, 69])
    FOLLOW_LT_in_arrayLiteral2505 = frozenset([1])
    FOLLOW_69_in_arrayLiteral2509 = frozenset([1])
    FOLLOW_42_in_objectLiteral2528 = frozenset([8, 9, 10, 12, 40, 43, 53, 113, 114])
    FOLLOW_LT_in_objectLiteral2530 = frozenset([8, 9, 10, 12, 40, 43, 53, 113, 114])
    FOLLOW_propertyNameAndValue_in_objectLiteral2533 = frozenset([8, 40, 43])
    FOLLOW_LT_in_objectLiteral2537 = frozenset([8, 40])
    FOLLOW_40_in_objectLiteral2540 = frozenset([8, 9, 10, 12, 53, 113, 114])
    FOLLOW_LT_in_objectLiteral2542 = frozenset([8, 9, 10, 12, 53, 113, 114])
    FOLLOW_propertyNameAndValue_in_objectLiteral2545 = frozenset([8, 40, 43])
    FOLLOW_LT_in_objectLiteral2549 = frozenset([8, 43])
    FOLLOW_43_in_objectLiteral2552 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue2576 = frozenset([8, 59])
    FOLLOW_LT_in_propertyNameAndValue2578 = frozenset([8, 59])
    FOLLOW_59_in_propertyNameAndValue2581 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_propertyNameAndValue2583 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_assignmentExpression_in_propertyNameAndValue2586 = frozenset([1])
    FOLLOW_113_in_propertyNameAndValue2608 = frozenset([12, 53, 113, 114])
    FOLLOW_114_in_propertyNameAndValue2612 = frozenset([12, 53, 113, 114])
    FOLLOW_identifier_in_propertyNameAndValue2617 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_propertyNameAndValue2619 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_propertyNameAndValue2624 = frozenset([8, 39])
    FOLLOW_LT_in_propertyNameAndValue2626 = frozenset([8, 39])
    FOLLOW_formalParameterList_in_propertyNameAndValue2629 = frozenset([8, 42])
    FOLLOW_LT_in_propertyNameAndValue2631 = frozenset([8, 42])
    FOLLOW_functionBody_in_propertyNameAndValue2634 = frozenset([1])
    FOLLOW_113_in_propertyNameAndValue2667 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_114_in_propertyNameAndValue2671 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_LT_in_propertyNameAndValue2674 = frozenset([8, 12, 53, 113, 114])
    FOLLOW_identifier_in_propertyNameAndValue2677 = frozenset([8, 39])
    FOLLOW_LT_in_propertyNameAndValue2679 = frozenset([8, 39])
    FOLLOW_formalParameterList_in_propertyNameAndValue2682 = frozenset([8, 42])
    FOLLOW_LT_in_propertyNameAndValue2684 = frozenset([8, 42])
    FOLLOW_functionBody_in_propertyNameAndValue2687 = frozenset([1])
    FOLLOW_identifier_in_propertyName2721 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName2726 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName2731 = frozenset([1])
    FOLLOW_set_in_literal0 = frozenset([1])
    FOLLOW_103_in_regularExpressionLiteral2779 = frozenset([11])
    FOLLOW_RegularExpressionLiteral_in_regularExpressionLiteral2781 = frozenset([103])
    FOLLOW_103_in_regularExpressionLiteral2783 = frozenset([12])
    FOLLOW_Identifier_in_regularExpressionLiteral2785 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_LT_in_synpred490 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_sourceElement_in_synpred494 = frozenset([1])
    FOLLOW_functionDeclaration_in_synpred5108 = frozenset([1])
    FOLLOW_LT_in_synpred21280 = frozenset([1])
    FOLLOW_statementBlock_in_synpred24303 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred27318 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred34353 = frozenset([1])
    FOLLOW_LT_in_synpred37382 = frozenset([1])
    FOLLOW_LT_in_synpred64648 = frozenset([8, 49])
    FOLLOW_49_in_synpred64652 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_synpred64654 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 44, 45, 46, 48, 50, 51, 52, 53, 55, 56, 57, 58, 60, 63, 64, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_statement_in_synpred64658 = frozenset([1])
    FOLLOW_forStatement_in_synpred67682 = frozenset([1])
    FOLLOW_LT_in_synpred89872 = frozenset([1])
    FOLLOW_LT_in_synpred1241170 = frozenset([1])
    FOLLOW_LT_in_synpred1271195 = frozenset([1])
    FOLLOW_conditionalExpression_in_synpred1461387 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_synpred1491416 = frozenset([1])
    FOLLOW_callExpression_in_synpred1521445 = frozenset([1])
    FOLLOW_memberExpression_in_synpred1531462 = frozenset([1])
    FOLLOW_LT_in_synpred1601510 = frozenset([8, 68, 70])
    FOLLOW_memberExpressionSuffix_in_synpred1601514 = frozenset([1])
    FOLLOW_LT_in_synpred1641553 = frozenset([8, 39, 68, 70])
    FOLLOW_callExpressionSuffix_in_synpred1641557 = frozenset([1])
    FOLLOW_LT_in_synpred2622290 = frozenset([8, 100, 101])
    FOLLOW_set_in_synpred2622294 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_LT_in_synpred2622302 = frozenset([8, 9, 10, 11, 12, 38, 39, 42, 53, 67, 68, 100, 101, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
    FOLLOW_multiplicativeExpression_in_synpred2622306 = frozenset([1])
    FOLLOW_LT_in_synpred2862480 = frozenset([1])
    FOLLOW_LT_in_synpred2932530 = frozenset([1])

