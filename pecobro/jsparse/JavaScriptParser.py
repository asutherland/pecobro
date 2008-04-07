# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-07 14:26:52

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
RegularExpressionLiteral=10
SingleEscapeCharacter=21
Comment=34
IdentifierPart=14
Identifier=11
HexDigit=25
PROP=6
RegularExpressionChars=13
DecimalDigit=24
LT=7
StringLiteral=8
UnicodeLetter=30
NonEscapeCharacter=22
HexIntegerLiteral=27
NumericLiteral=9
ExponentPart=28
UnicodeConnectorPunctuation=32
RegularExpressionFirstChar=12
CharacterEscapeSequence=18
IdentifierStart=29
UnicodeDigit=31
EscapeSequence=15
EscapeCharacter=23
EOF=-1
DecimalLiteral=26
FUNC=4
HexEscapeSequence=19
UnicodeEscapeSequence=20
UnicodeCombiningMark=33
SingleStringCharacter=17
WhiteSpace=36
OBJ=5
LineComment=35
DoubleStringCharacter=16

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "FUNC", "OBJ", "PROP", "LT", "StringLiteral", "NumericLiteral", "RegularExpressionLiteral", 
    "Identifier", "RegularExpressionFirstChar", "RegularExpressionChars", 
    "IdentifierPart", "EscapeSequence", "DoubleStringCharacter", "SingleStringCharacter", 
    "CharacterEscapeSequence", "HexEscapeSequence", "UnicodeEscapeSequence", 
    "SingleEscapeCharacter", "NonEscapeCharacter", "EscapeCharacter", "DecimalDigit", 
    "HexDigit", "DecimalLiteral", "HexIntegerLiteral", "ExponentPart", "IdentifierStart", 
    "UnicodeLetter", "UnicodeDigit", "UnicodeConnectorPunctuation", "UnicodeCombiningMark", 
    "Comment", "LineComment", "WhiteSpace", "'function'", "'('", "','", 
    "')'", "'{'", "'}'", "'var'", "'const'", "';'", "'='", "'if'", "'else'", 
    "'do'", "'while'", "'for'", "'each'", "'in'", "'continue'", "'break'", 
    "'return'", "'with'", "':'", "'switch'", "'case'", "'default'", "'throw'", 
    "'try'", "'catch'", "'finally'", "'new'", "'['", "']'", "'.'", "'*='", 
    "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", "'&='", 
    "'^='", "'|='", "'?'", "'||'", "'&&'", "'|'", "'^'", "'&'", "'=='", 
    "'!='", "'==='", "'!=='", "'<'", "'>'", "'<='", "'>='", "'instanceof'", 
    "'<<'", "'>>'", "'>>>'", "'+'", "'-'", "'*'", "'/'", "'%'", "'delete'", 
    "'void'", "'typeof'", "'++'", "'--'", "'~'", "'!'", "'this'", "'get'", 
    "'set'", "'null'", "'true'", "'false'"
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
        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )
        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )
        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
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
        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
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
        self.dfa58 = self.DFA58(
            self, 58,
            eot = self.DFA58_eot,
            eof = self.DFA58_eof,
            min = self.DFA58_min,
            max = self.DFA58_max,
            accept = self.DFA58_accept,
            special = self.DFA58_special,
            transition = self.DFA58_transition
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
        self.dfa64 = self.DFA64(
            self, 64,
            eot = self.DFA64_eot,
            eof = self.DFA64_eof,
            min = self.DFA64_min,
            max = self.DFA64_max,
            accept = self.DFA64_accept,
            special = self.DFA64_special,
            transition = self.DFA64_transition
            )
        self.dfa93 = self.DFA93(
            self, 93,
            eot = self.DFA93_eot,
            eof = self.DFA93_eof,
            min = self.DFA93_min,
            max = self.DFA93_max,
            accept = self.DFA93_accept,
            special = self.DFA93_special,
            transition = self.DFA93_transition
            )
        self.dfa97 = self.DFA97(
            self, 97,
            eot = self.DFA97_eot,
            eof = self.DFA97_eof,
            min = self.DFA97_min,
            max = self.DFA97_max,
            accept = self.DFA97_accept,
            special = self.DFA97_special,
            transition = self.DFA97_transition
            )
        self.dfa96 = self.DFA96(
            self, 96,
            eot = self.DFA96_eot,
            eof = self.DFA96_eof,
            min = self.DFA96_min,
            max = self.DFA96_max,
            accept = self.DFA96_accept,
            special = self.DFA96_special,
            transition = self.DFA96_transition
            )
        self.dfa109 = self.DFA109(
            self, 109,
            eot = self.DFA109_eot,
            eof = self.DFA109_eof,
            min = self.DFA109_min,
            max = self.DFA109_max,
            accept = self.DFA109_accept,
            special = self.DFA109_special,
            transition = self.DFA109_transition
            )
        self.dfa118 = self.DFA118(
            self, 118,
            eot = self.DFA118_eot,
            eof = self.DFA118_eof,
            min = self.DFA118_min,
            max = self.DFA118_max,
            accept = self.DFA118_accept,
            special = self.DFA118_special,
            transition = self.DFA118_transition
            )
        self.dfa121 = self.DFA121(
            self, 121,
            eot = self.DFA121_eot,
            eof = self.DFA121_eof,
            min = self.DFA121_min,
            max = self.DFA121_max,
            accept = self.DFA121_accept,
            special = self.DFA121_special,
            transition = self.DFA121_transition
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
        self.dfa154 = self.DFA154(
            self, 154,
            eot = self.DFA154_eot,
            eof = self.DFA154_eof,
            min = self.DFA154_min,
            max = self.DFA154_max,
            accept = self.DFA154_accept,
            special = self.DFA154_special,
            transition = self.DFA154_transition
            )
        self.dfa159 = self.DFA159(
            self, 159,
            eot = self.DFA159_eot,
            eof = self.DFA159_eof,
            min = self.DFA159_min,
            max = self.DFA159_max,
            accept = self.DFA159_accept,
            special = self.DFA159_special,
            transition = self.DFA159_transition
            )
        self.dfa162 = self.DFA162(
            self, 162,
            eot = self.DFA162_eot,
            eof = self.DFA162_eof,
            min = self.DFA162_min,
            max = self.DFA162_max,
            accept = self.DFA162_accept,
            special = self.DFA162_special,
            transition = self.DFA162_transition
            )
        self.dfa165 = self.DFA165(
            self, 165,
            eot = self.DFA165_eot,
            eof = self.DFA165_eof,
            min = self.DFA165_min,
            max = self.DFA165_max,
            accept = self.DFA165_accept,
            special = self.DFA165_special,
            transition = self.DFA165_transition
            )
        self.dfa168 = self.DFA168(
            self, 168,
            eot = self.DFA168_eot,
            eof = self.DFA168_eof,
            min = self.DFA168_min,
            max = self.DFA168_max,
            accept = self.DFA168_accept,
            special = self.DFA168_special,
            transition = self.DFA168_transition
            )
        self.dfa171 = self.DFA171(
            self, 171,
            eot = self.DFA171_eot,
            eof = self.DFA171_eof,
            min = self.DFA171_min,
            max = self.DFA171_max,
            accept = self.DFA171_accept,
            special = self.DFA171_special,
            transition = self.DFA171_transition
            )
        self.dfa174 = self.DFA174(
            self, 174,
            eot = self.DFA174_eot,
            eof = self.DFA174_eof,
            min = self.DFA174_min,
            max = self.DFA174_max,
            accept = self.DFA174_accept,
            special = self.DFA174_special,
            transition = self.DFA174_transition
            )
        self.dfa177 = self.DFA177(
            self, 177,
            eot = self.DFA177_eot,
            eof = self.DFA177_eof,
            min = self.DFA177_min,
            max = self.DFA177_max,
            accept = self.DFA177_accept,
            special = self.DFA177_special,
            transition = self.DFA177_transition
            )
        self.dfa180 = self.DFA180(
            self, 180,
            eot = self.DFA180_eot,
            eof = self.DFA180_eof,
            min = self.DFA180_min,
            max = self.DFA180_max,
            accept = self.DFA180_accept,
            special = self.DFA180_special,
            transition = self.DFA180_transition
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
        self.dfa186 = self.DFA186(
            self, 186,
            eot = self.DFA186_eot,
            eof = self.DFA186_eof,
            min = self.DFA186_min,
            max = self.DFA186_max,
            accept = self.DFA186_accept,
            special = self.DFA186_special,
            transition = self.DFA186_transition
            )
        self.dfa189 = self.DFA189(
            self, 189,
            eot = self.DFA189_eot,
            eof = self.DFA189_eof,
            min = self.DFA189_min,
            max = self.DFA189_max,
            accept = self.DFA189_accept,
            special = self.DFA189_special,
            transition = self.DFA189_transition
            )
        self.dfa192 = self.DFA192(
            self, 192,
            eot = self.DFA192_eot,
            eof = self.DFA192_eof,
            min = self.DFA192_min,
            max = self.DFA192_max,
            accept = self.DFA192_accept,
            special = self.DFA192_special,
            transition = self.DFA192_transition
            )
        self.dfa195 = self.DFA195(
            self, 195,
            eot = self.DFA195_eot,
            eof = self.DFA195_eof,
            min = self.DFA195_min,
            max = self.DFA195_max,
            accept = self.DFA195_accept,
            special = self.DFA195_special,
            transition = self.DFA195_transition
            )
        self.dfa198 = self.DFA198(
            self, 198,
            eot = self.DFA198_eot,
            eof = self.DFA198_eof,
            min = self.DFA198_min,
            max = self.DFA198_max,
            accept = self.DFA198_accept,
            special = self.DFA198_special,
            transition = self.DFA198_transition
            )
        self.dfa201 = self.DFA201(
            self, 201,
            eot = self.DFA201_eot,
            eof = self.DFA201_eof,
            min = self.DFA201_min,
            max = self.DFA201_max,
            accept = self.DFA201_accept,
            special = self.DFA201_special,
            transition = self.DFA201_transition
            )
        self.dfa204 = self.DFA204(
            self, 204,
            eot = self.DFA204_eot,
            eof = self.DFA204_eof,
            min = self.DFA204_min,
            max = self.DFA204_max,
            accept = self.DFA204_accept,
            special = self.DFA204_special,
            transition = self.DFA204_transition
            )
        self.dfa210 = self.DFA210(
            self, 210,
            eot = self.DFA210_eot,
            eof = self.DFA210_eof,
            min = self.DFA210_min,
            max = self.DFA210_max,
            accept = self.DFA210_accept,
            special = self.DFA210_special,
            transition = self.DFA210_transition
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
        self.dfa227 = self.DFA227(
            self, 227,
            eot = self.DFA227_eot,
            eof = self.DFA227_eof,
            min = self.DFA227_min,
            max = self.DFA227_max,
            accept = self.DFA227_accept,
            special = self.DFA227_special,
            transition = self.DFA227_transition
            )
        self.dfa235 = self.DFA235(
            self, 235,
            eot = self.DFA235_eot,
            eof = self.DFA235_eof,
            min = self.DFA235_min,
            max = self.DFA235_max,
            accept = self.DFA235_accept,
            special = self.DFA235_special,
            transition = self.DFA235_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class program_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start program
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:23:1: program : ( LT )* sourceElements ( LT )* EOF ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:24:2: ( ( LT )* sourceElements ( LT )* EOF )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:24:4: ( LT )* sourceElements ( LT )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:24:6: ( LT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == LT) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT1 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program60)
                        if self.failed:
                            return retval


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_sourceElements_in_program64)
                sourceElements2 = self.sourceElements()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElements2.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:24:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT3 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program66)
                        if self.failed:
                            return retval


                    else:
                        break #loop2


                EOF4 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_program70)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:27:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:2: ( sourceElement ( ( LT )* sourceElement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:4: sourceElement ( ( LT )* sourceElement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_sourceElement_in_sourceElements83)
                sourceElement5 = self.sourceElement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElement5.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    LA4 = self.input.LA(1)
                    if LA4 == LT:
                        LA4_1 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 37:
                        LA4_4 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 41:
                        LA4_5 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 43 or LA4 == 44:
                        LA4_6 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 45:
                        LA4_7 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 111:
                        LA4_8 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == Identifier or LA4 == 52 or LA4 == 112 or LA4 == 113:
                        LA4_9 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == StringLiteral or LA4 == NumericLiteral or LA4 == RegularExpressionLiteral or LA4 == 114 or LA4 == 115 or LA4 == 116:
                        LA4_10 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 67:
                        LA4_11 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 38:
                        LA4_12 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 66:
                        LA4_13 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 99 or LA4 == 100 or LA4 == 104 or LA4 == 105 or LA4 == 106 or LA4 == 107 or LA4 == 108 or LA4 == 109 or LA4 == 110:
                        LA4_14 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 47:
                        LA4_15 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 49:
                        LA4_16 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 50:
                        LA4_17 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 51:
                        LA4_18 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 54:
                        LA4_19 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 55:
                        LA4_20 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 56:
                        LA4_21 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 57:
                        LA4_22 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 59:
                        LA4_23 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 62:
                        LA4_24 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1


                    elif LA4 == 63:
                        LA4_25 = self.input.LA(2)

                        if (self.synpred4()) :
                            alt4 = 1



                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:19: ( LT )* sourceElement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:21: ( LT )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if (LA3_0 == LT) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT6 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements86)
                                if self.failed:
                                    return retval


                            else:
                                break #loop3


                        self.following.append(self.FOLLOW_sourceElement_in_sourceElements90)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:31:1: sourceElement : ( functionDeclaration | statement );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:2: ( functionDeclaration | statement )
                alt5 = 2
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:4: functionDeclaration
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionDeclaration_in_sourceElement104)
                    functionDeclaration8 = self.functionDeclaration()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:4: statement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statement_in_sourceElement109)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:1: functionDeclaration : 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) ;
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
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self.adaptor, "rule functionBody")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC identifier formalParameterList functionBody ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody
                string_literal10 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_functionDeclaration122)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_37.add(string_literal10)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:15: ( LT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LT) :
                        alt6 = 1


                    if alt6 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT11 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration124)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT11)


                    else:
                        break #loop6


                self.following.append(self.FOLLOW_identifier_in_functionDeclaration127)
                identifier12 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier12.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:30: ( LT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == LT) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT13 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration129)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT13)


                    else:
                        break #loop7


                self.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration132)
                formalParameterList14 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList14.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:54: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT15 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration134)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT15)


                    else:
                        break #loop8


                self.following.append(self.FOLLOW_functionBody_in_functionDeclaration137)
                functionBody16 = self.functionBody()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_functionBody.add(functionBody16.tree)
                # AST Rewrite
                # elements: functionBody, formalParameterList, identifier
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
                    # 39:3: -> ^( FUNC identifier formalParameterList functionBody )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:6: ^( FUNC identifier formalParameterList functionBody )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:42:1: functionExpression : 'function' ( LT )* ( identifier )? ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC ( identifier )? formalParameterList functionBody ) ;
    def functionExpression(self, ):

        retval = self.functionExpression_return()
        retval.start = self.input.LT(1)
        functionExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal17 = None
        LT18 = None
        LT20 = None
        LT22 = None
        identifier19 = None

        formalParameterList21 = None

        functionBody23 = None


        string_literal17_tree = None
        LT18_tree = None
        LT20_tree = None
        LT22_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_37 = RewriteRuleTokenStream(self.adaptor, "token 37")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_functionBody = RewriteRuleSubtreeStream(self.adaptor, "rule functionBody")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:2: ( 'function' ( LT )* ( identifier )? ( LT )* formalParameterList ( LT )* functionBody -> ^( FUNC ( identifier )? formalParameterList functionBody ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:4: 'function' ( LT )* ( identifier )? ( LT )* formalParameterList ( LT )* functionBody
                string_literal17 = self.input.LT(1)
                self.match(self.input, 37, self.FOLLOW_37_in_functionExpression163)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_37.add(string_literal17)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:15: ( LT )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == LT) :
                        LA9_2 = self.input.LA(2)

                        if (self.synpred9()) :
                            alt9 = 1




                    if alt9 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT18 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression165)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT18)


                    else:
                        break #loop9


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:19: ( identifier )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == Identifier or LA10_0 == 52 or (112 <= LA10_0 <= 113)) :
                    alt10 = 1
                if alt10 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_functionExpression168)
                    identifier19 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier19.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:31: ( LT )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == LT) :
                        alt11 = 1


                    if alt11 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT20 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression171)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT20)


                    else:
                        break #loop11


                self.following.append(self.FOLLOW_formalParameterList_in_functionExpression174)
                formalParameterList21 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList21.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:55: ( LT )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == LT) :
                        alt12 = 1


                    if alt12 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT22 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression176)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT22)


                    else:
                        break #loop12


                self.following.append(self.FOLLOW_functionBody_in_functionExpression179)
                functionBody23 = self.functionBody()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_functionBody.add(functionBody23.tree)
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
                    # 44:3: -> ^( FUNC ( identifier )? formalParameterList functionBody )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:6: ^( FUNC ( identifier )? formalParameterList functionBody )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:13: ( identifier )?
                    if stream_identifier.hasNext():
                        self.adaptor.addChild(root_1, stream_identifier.next())


                    stream_identifier.reset();
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:47:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' ;
    def formalParameterList(self, ):

        retval = self.formalParameterList_return()
        retval.start = self.input.LT(1)
        formalParameterList_StartIndex = self.input.index()
        root_0 = None

        char_literal24 = None
        LT25 = None
        LT27 = None
        char_literal28 = None
        LT29 = None
        LT31 = None
        char_literal32 = None
        identifier26 = None

        identifier30 = None


        char_literal24_tree = None
        LT25_tree = None
        LT27_tree = None
        char_literal28_tree = None
        LT29_tree = None
        LT31_tree = None
        char_literal32_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 6):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal24 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_formalParameterList206)
                if self.failed:
                    return retval

                char_literal24_tree = self.adaptor.createWithPayload(char_literal24)
                self.adaptor.addChild(root_0, char_literal24_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:11: ( LT )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == LT) :
                            alt13 = 1


                        if alt13 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT25 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList209)
                            if self.failed:
                                return retval


                        else:
                            break #loop13


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList213)
                    identifier26 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier26.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:25: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop16
                        alt16 = 2
                        alt16 = self.dfa16.predict(self.input)
                        if alt16 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:26: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:28: ( LT )*
                            while True: #loop14
                                alt14 = 2
                                LA14_0 = self.input.LA(1)

                                if (LA14_0 == LT) :
                                    alt14 = 1


                                if alt14 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT27 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList216)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop14


                            char_literal28 = self.input.LT(1)
                            self.match(self.input, 39, self.FOLLOW_39_in_formalParameterList220)
                            if self.failed:
                                return retval

                            char_literal28_tree = self.adaptor.createWithPayload(char_literal28)
                            self.adaptor.addChild(root_0, char_literal28_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:37: ( LT )*
                            while True: #loop15
                                alt15 = 2
                                LA15_0 = self.input.LA(1)

                                if (LA15_0 == LT) :
                                    alt15 = 1


                                if alt15 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT29 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList222)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop15


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList226)
                            identifier30 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, identifier30.tree)


                        else:
                            break #loop16





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:57: ( LT )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == LT) :
                        alt18 = 1


                    if alt18 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT31 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList232)
                        if self.failed:
                            return retval


                    else:
                        break #loop18


                char_literal32 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_formalParameterList236)
                if self.failed:
                    return retval

                char_literal32_tree = self.adaptor.createWithPayload(char_literal32)
                self.adaptor.addChild(root_0, char_literal32_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:1: functionBody : '{' ( LT )* ( sourceElements )* ( LT )* '}' ;
    def functionBody(self, ):

        retval = self.functionBody_return()
        retval.start = self.input.LT(1)
        functionBody_StartIndex = self.input.index()
        root_0 = None

        char_literal33 = None
        LT34 = None
        LT36 = None
        char_literal37 = None
        sourceElements35 = None


        char_literal33_tree = None
        LT34_tree = None
        LT36_tree = None
        char_literal37_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:2: ( '{' ( LT )* ( sourceElements )* ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:4: '{' ( LT )* ( sourceElements )* ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal33 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_functionBody247)
                if self.failed:
                    return retval

                char_literal33_tree = self.adaptor.createWithPayload(char_literal33)
                self.adaptor.addChild(root_0, char_literal33_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:10: ( LT )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == LT) :
                        LA19_2 = self.input.LA(2)

                        if (self.synpred19()) :
                            alt19 = 1




                    if alt19 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT34 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionBody249)
                        if self.failed:
                            return retval


                    else:
                        break #loop19


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:13: ( sourceElements )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((StringLiteral <= LA20_0 <= Identifier) or (37 <= LA20_0 <= 38) or LA20_0 == 41 or (43 <= LA20_0 <= 45) or LA20_0 == 47 or (49 <= LA20_0 <= 52) or (54 <= LA20_0 <= 57) or LA20_0 == 59 or (62 <= LA20_0 <= 63) or (66 <= LA20_0 <= 67) or (99 <= LA20_0 <= 100) or (104 <= LA20_0 <= 116)) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: sourceElements
                        self.following.append(self.FOLLOW_sourceElements_in_functionBody253)
                        sourceElements35 = self.sourceElements()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, sourceElements35.tree)


                    else:
                        break #loop20


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:31: ( LT )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == LT) :
                        alt21 = 1


                    if alt21 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT36 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionBody256)
                        if self.failed:
                            return retval


                    else:
                        break #loop21


                char_literal37 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_functionBody260)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)
        statement_StartIndex = self.input.index()
        root_0 = None

        statementBlock38 = None

        variableStatement39 = None

        emptyStatement40 = None

        expressionStatement41 = None

        ifStatement42 = None

        iterationStatement43 = None

        continueStatement44 = None

        breakStatement45 = None

        returnStatement46 = None

        withStatement47 = None

        labelledStatement48 = None

        switchStatement49 = None

        throwStatement50 = None

        tryStatement51 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement )
                alt22 = 14
                LA22 = self.input.LA(1)
                if LA22 == 41:
                    LA22_1 = self.input.LA(2)

                    if (self.synpred22()) :
                        alt22 = 1
                    elif (self.synpred25()) :
                        alt22 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("56:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 22, 1, self.input)

                        raise nvae

                elif LA22 == 43 or LA22 == 44:
                    alt22 = 2
                elif LA22 == 45:
                    alt22 = 3
                elif LA22 == StringLiteral or LA22 == NumericLiteral or LA22 == RegularExpressionLiteral or LA22 == 37 or LA22 == 38 or LA22 == 66 or LA22 == 67 or LA22 == 99 or LA22 == 100 or LA22 == 104 or LA22 == 105 or LA22 == 106 or LA22 == 107 or LA22 == 108 or LA22 == 109 or LA22 == 110 or LA22 == 111 or LA22 == 114 or LA22 == 115 or LA22 == 116:
                    alt22 = 4
                elif LA22 == Identifier or LA22 == 52 or LA22 == 112 or LA22 == 113:
                    LA22_5 = self.input.LA(2)

                    if (self.synpred25()) :
                        alt22 = 4
                    elif (self.synpred32()) :
                        alt22 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("56:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 22, 5, self.input)

                        raise nvae

                elif LA22 == 47:
                    alt22 = 5
                elif LA22 == 49 or LA22 == 50 or LA22 == 51:
                    alt22 = 6
                elif LA22 == 54:
                    alt22 = 7
                elif LA22 == 55:
                    alt22 = 8
                elif LA22 == 56:
                    alt22 = 9
                elif LA22 == 57:
                    alt22 = 10
                elif LA22 == 59:
                    alt22 = 12
                elif LA22 == 62:
                    alt22 = 13
                elif LA22 == 63:
                    alt22 = 14
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("56:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement272)
                    statementBlock38 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock38.tree)


                elif alt22 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:58:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement277)
                    variableStatement39 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement39.tree)


                elif alt22 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:59:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement282)
                    emptyStatement40 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement40.tree)


                elif alt22 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement287)
                    expressionStatement41 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement41.tree)


                elif alt22 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement292)
                    ifStatement42 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement42.tree)


                elif alt22 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement297)
                    iterationStatement43 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement43.tree)


                elif alt22 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:63:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement302)
                    continueStatement44 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement44.tree)


                elif alt22 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement307)
                    breakStatement45 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement45.tree)


                elif alt22 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:65:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement312)
                    returnStatement46 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement46.tree)


                elif alt22 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:66:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement317)
                    withStatement47 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement47.tree)


                elif alt22 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement322)
                    labelledStatement48 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement48.tree)


                elif alt22 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:68:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement327)
                    switchStatement49 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement49.tree)


                elif alt22 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement332)
                    throwStatement50 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement50.tree)


                elif alt22 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:70:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement337)
                    tryStatement51 = self.tryStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, tryStatement51.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:1: statementBlock : '{' ( LT )* ( statementList )? ( LT )* '}' ;
    def statementBlock(self, ):

        retval = self.statementBlock_return()
        retval.start = self.input.LT(1)
        statementBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal52 = None
        LT53 = None
        LT55 = None
        char_literal56 = None
        statementList54 = None


        char_literal52_tree = None
        LT53_tree = None
        LT55_tree = None
        char_literal56_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal52 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_statementBlock349)
                if self.failed:
                    return retval

                char_literal52_tree = self.adaptor.createWithPayload(char_literal52)
                self.adaptor.addChild(root_0, char_literal52_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:10: ( LT )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == LT) :
                        LA23_2 = self.input.LA(2)

                        if (self.synpred35()) :
                            alt23 = 1




                    if alt23 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT53 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock351)
                        if self.failed:
                            return retval


                    else:
                        break #loop23


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:13: ( statementList )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((StringLiteral <= LA24_0 <= Identifier) or (37 <= LA24_0 <= 38) or LA24_0 == 41 or (43 <= LA24_0 <= 45) or LA24_0 == 47 or (49 <= LA24_0 <= 52) or (54 <= LA24_0 <= 57) or LA24_0 == 59 or (62 <= LA24_0 <= 63) or (66 <= LA24_0 <= 67) or (99 <= LA24_0 <= 100) or (104 <= LA24_0 <= 116)) :
                    alt24 = 1
                if alt24 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_statementBlock355)
                    statementList54 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList54.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:30: ( LT )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == LT) :
                        alt25 = 1


                    if alt25 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT55 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock358)
                        if self.failed:
                            return retval


                    else:
                        break #loop25


                char_literal56 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_statementBlock362)
                if self.failed:
                    return retval

                char_literal56_tree = self.adaptor.createWithPayload(char_literal56)
                self.adaptor.addChild(root_0, char_literal56_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:1: statementList : statement ( ( LT )* statement )* ;
    def statementList(self, ):

        retval = self.statementList_return()
        retval.start = self.input.LT(1)
        statementList_StartIndex = self.input.index()
        root_0 = None

        LT58 = None
        statement57 = None

        statement59 = None


        LT58_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList374)
                statement57 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement57.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:14: ( ( LT )* statement )*
                while True: #loop27
                    alt27 = 2
                    alt27 = self.dfa27.predict(self.input)
                    if alt27 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:17: ( LT )*
                        while True: #loop26
                            alt26 = 2
                            LA26_0 = self.input.LA(1)

                            if (LA26_0 == LT) :
                                alt26 = 1


                            if alt26 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT58 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList377)
                                if self.failed:
                                    return retval


                            else:
                                break #loop26


                        self.following.append(self.FOLLOW_statement_in_statementList381)
                        statement59 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement59.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:1: variableStatement : ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        set60 = None
        LT61 = None
        set63 = None
        variableDeclarationList62 = None


        set60_tree = None
        LT61_tree = None
        set63_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:2: ( ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:4: ( 'var' | 'const' ) ( LT )* variableDeclarationList ( LT | ';' )
                root_0 = self.adaptor.nil()

                set60 = self.input.LT(1)
                if (43 <= self.input.LA(1) <= 44):
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
                        self.input, mse, self.FOLLOW_set_in_variableStatement395
                        )
                    raise mse


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:22: ( LT )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == LT) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT61 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement401)
                        if self.failed:
                            return retval


                    else:
                        break #loop28


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement405)
                variableDeclarationList62 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationList62.tree)
                set63 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_variableStatement407
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
    def variableDeclarationList(self, ):

        retval = self.variableDeclarationList_return()
        retval.start = self.input.LT(1)
        variableDeclarationList_StartIndex = self.input.index()
        root_0 = None

        LT65 = None
        char_literal66 = None
        LT67 = None
        variableDeclaration64 = None

        variableDeclaration68 = None


        LT65_tree = None
        char_literal66_tree = None
        LT67_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList425)
                variableDeclaration64 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration64.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop31
                    alt31 = 2
                    alt31 = self.dfa31.predict(self.input)
                    if alt31 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:27: ( LT )*
                        while True: #loop29
                            alt29 = 2
                            LA29_0 = self.input.LA(1)

                            if (LA29_0 == LT) :
                                alt29 = 1


                            if alt29 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT65 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList428)
                                if self.failed:
                                    return retval


                            else:
                                break #loop29


                        char_literal66 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_variableDeclarationList432)
                        if self.failed:
                            return retval

                        char_literal66_tree = self.adaptor.createWithPayload(char_literal66)
                        self.adaptor.addChild(root_0, char_literal66_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:36: ( LT )*
                        while True: #loop30
                            alt30 = 2
                            LA30_0 = self.input.LA(1)

                            if (LA30_0 == LT) :
                                alt30 = 1


                            if alt30 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT67 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList434)
                                if self.failed:
                                    return retval


                            else:
                                break #loop30


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList438)
                        variableDeclaration68 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration68.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:89:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
    def variableDeclarationListNoIn(self, ):

        retval = self.variableDeclarationListNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationListNoIn_StartIndex = self.input.index()
        root_0 = None

        LT70 = None
        char_literal71 = None
        LT72 = None
        variableDeclarationNoIn69 = None

        variableDeclarationNoIn73 = None


        LT70_tree = None
        char_literal71_tree = None
        LT72_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn452)
                variableDeclarationNoIn69 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn69.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop34
                    alt34 = 2
                    alt34 = self.dfa34.predict(self.input)
                    if alt34 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:31: ( LT )*
                        while True: #loop32
                            alt32 = 2
                            LA32_0 = self.input.LA(1)

                            if (LA32_0 == LT) :
                                alt32 = 1


                            if alt32 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT70 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn455)
                                if self.failed:
                                    return retval


                            else:
                                break #loop32


                        char_literal71 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_variableDeclarationListNoIn459)
                        if self.failed:
                            return retval

                        char_literal71_tree = self.adaptor.createWithPayload(char_literal71)
                        self.adaptor.addChild(root_0, char_literal71_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:40: ( LT )*
                        while True: #loop33
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == LT) :
                                alt33 = 1


                            if alt33 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT72 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn461)
                                if self.failed:
                                    return retval


                            else:
                                break #loop33


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn465)
                        variableDeclarationNoIn73 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn73.tree)


                    else:
                        break #loop34





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:93:1: variableDeclaration : identifier ( ( LT )* initialiser )? ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT75 = None
        identifier74 = None

        initialiser76 = None


        LT75_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:2: ( identifier ( ( LT )* initialiser )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:4: identifier ( ( LT )* initialiser )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_variableDeclaration479)
                identifier74 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier74.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:15: ( ( LT )* initialiser )?
                alt36 = 2
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:16: ( LT )* initialiser
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:18: ( LT )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == LT) :
                            alt35 = 1


                        if alt35 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT75 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration482)
                            if self.failed:
                                return retval


                        else:
                            break #loop35


                    self.following.append(self.FOLLOW_initialiser_in_variableDeclaration486)
                    initialiser76 = self.initialiser()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, initialiser76.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:97:1: variableDeclarationNoIn : identifier ( ( LT )* initialiserNoIn )? ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT78 = None
        identifier77 = None

        initialiserNoIn79 = None


        LT78_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:2: ( identifier ( ( LT )* initialiserNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:4: identifier ( ( LT )* initialiserNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn500)
                identifier77 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier77.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:15: ( ( LT )* initialiserNoIn )?
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:16: ( LT )* initialiserNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:18: ( LT )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == LT) :
                            alt37 = 1


                        if alt37 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT78 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn503)
                            if self.failed:
                                return retval


                        else:
                            break #loop37


                    self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn507)
                    initialiserNoIn79 = self.initialiserNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, initialiserNoIn79.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:101:1: initialiser : '=' ( LT )* assignmentExpression ;
    def initialiser(self, ):

        retval = self.initialiser_return()
        retval.start = self.input.LT(1)
        initialiser_StartIndex = self.input.index()
        root_0 = None

        char_literal80 = None
        LT81 = None
        assignmentExpression82 = None


        char_literal80_tree = None
        LT81_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:102:2: ( '=' ( LT )* assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:102:4: '=' ( LT )* assignmentExpression
                root_0 = self.adaptor.nil()

                char_literal80 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_initialiser521)
                if self.failed:
                    return retval

                char_literal80_tree = self.adaptor.createWithPayload(char_literal80)
                self.adaptor.addChild(root_0, char_literal80_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:102:10: ( LT )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == LT) :
                        alt39 = 1


                    if alt39 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT81 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser523)
                        if self.failed:
                            return retval


                    else:
                        break #loop39


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser527)
                assignmentExpression82 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression82.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn ;
    def initialiserNoIn(self, ):

        retval = self.initialiserNoIn_return()
        retval.start = self.input.LT(1)
        initialiserNoIn_StartIndex = self.input.index()
        root_0 = None

        char_literal83 = None
        LT84 = None
        assignmentExpressionNoIn85 = None


        char_literal83_tree = None
        LT84_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:106:2: ( '=' ( LT )* assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:106:4: '=' ( LT )* assignmentExpressionNoIn
                root_0 = self.adaptor.nil()

                char_literal83 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_initialiserNoIn539)
                if self.failed:
                    return retval

                char_literal83_tree = self.adaptor.createWithPayload(char_literal83)
                self.adaptor.addChild(root_0, char_literal83_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:106:10: ( LT )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == LT) :
                        alt40 = 1


                    if alt40 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT84 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn541)
                        if self.failed:
                            return retval


                    else:
                        break #loop40


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn545)
                assignmentExpressionNoIn85 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn85.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal86 = None

        char_literal86_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:110:4: ';'
                root_0 = self.adaptor.nil()

                char_literal86 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_emptyStatement557)
                if self.failed:
                    return retval

                char_literal86_tree = self.adaptor.createWithPayload(char_literal86)
                self.adaptor.addChild(root_0, char_literal86_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:113:1: expressionStatement : expression ( LT | ';' ) ;
    def expressionStatement(self, ):

        retval = self.expressionStatement_return()
        retval.start = self.input.LT(1)
        expressionStatement_StartIndex = self.input.index()
        root_0 = None

        set88 = None
        expression87 = None


        set88_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:114:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:114:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement569)
                expression87 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression87.tree)
                set88 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_expressionStatement571
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:117:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
    def ifStatement(self, ):

        retval = self.ifStatement_return()
        retval.start = self.input.LT(1)
        ifStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal89 = None
        LT90 = None
        char_literal91 = None
        LT92 = None
        LT94 = None
        char_literal95 = None
        LT96 = None
        LT98 = None
        string_literal99 = None
        LT100 = None
        expression93 = None

        statement97 = None

        statement101 = None


        string_literal89_tree = None
        LT90_tree = None
        char_literal91_tree = None
        LT92_tree = None
        LT94_tree = None
        char_literal95_tree = None
        LT96_tree = None
        LT98_tree = None
        string_literal99_tree = None
        LT100_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal89 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_ifStatement590)
                if self.failed:
                    return retval

                string_literal89_tree = self.adaptor.createWithPayload(string_literal89)
                self.adaptor.addChild(root_0, string_literal89_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:11: ( LT )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == LT) :
                        alt41 = 1


                    if alt41 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT90 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement592)
                        if self.failed:
                            return retval


                    else:
                        break #loop41


                char_literal91 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_ifStatement596)
                if self.failed:
                    return retval

                char_literal91_tree = self.adaptor.createWithPayload(char_literal91)
                self.adaptor.addChild(root_0, char_literal91_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:20: ( LT )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == LT) :
                        alt42 = 1


                    if alt42 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT92 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement598)
                        if self.failed:
                            return retval


                    else:
                        break #loop42


                self.following.append(self.FOLLOW_expression_in_ifStatement602)
                expression93 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression93.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:36: ( LT )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == LT) :
                        alt43 = 1


                    if alt43 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT94 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement604)
                        if self.failed:
                            return retval


                    else:
                        break #loop43


                char_literal95 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_ifStatement608)
                if self.failed:
                    return retval

                char_literal95_tree = self.adaptor.createWithPayload(char_literal95)
                self.adaptor.addChild(root_0, char_literal95_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:45: ( LT )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == LT) :
                        alt44 = 1


                    if alt44 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT96 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement610)
                        if self.failed:
                            return retval


                    else:
                        break #loop44


                self.following.append(self.FOLLOW_statement_in_ifStatement614)
                statement97 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement97.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:58: ( ( LT )* 'else' ( LT )* statement )?
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == LT) :
                    LA47_1 = self.input.LA(2)

                    if (self.synpred62()) :
                        alt47 = 1
                elif (LA47_0 == 48) :
                    LA47_2 = self.input.LA(2)

                    if (self.synpred62()) :
                        alt47 = 1
                if alt47 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:61: ( LT )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == LT) :
                            alt45 = 1


                        if alt45 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT98 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement617)
                            if self.failed:
                                return retval


                        else:
                            break #loop45


                    string_literal99 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_ifStatement621)
                    if self.failed:
                        return retval

                    string_literal99_tree = self.adaptor.createWithPayload(string_literal99)
                    self.adaptor.addChild(root_0, string_literal99_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:73: ( LT )*
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == LT) :
                            alt46 = 1


                        if alt46 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT100 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement623)
                            if self.failed:
                                return retval


                        else:
                            break #loop46


                    self.following.append(self.FOLLOW_statement_in_ifStatement627)
                    statement101 = self.statement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statement101.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:121:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
    def iterationStatement(self, ):

        retval = self.iterationStatement_return()
        retval.start = self.input.LT(1)
        iterationStatement_StartIndex = self.input.index()
        root_0 = None

        doWhileStatement102 = None

        whileStatement103 = None

        forStatement104 = None

        forInStatement105 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:122:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt48 = 4
                LA48 = self.input.LA(1)
                if LA48 == 49:
                    alt48 = 1
                elif LA48 == 50:
                    alt48 = 2
                elif LA48 == 51:
                    LA48_3 = self.input.LA(2)

                    if (self.synpred65()) :
                        alt48 = 3
                    elif (True) :
                        alt48 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("121:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 48, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("121:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 48, 0, self.input)

                    raise nvae

                if alt48 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:122:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement641)
                    doWhileStatement102 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement102.tree)


                elif alt48 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement646)
                    whileStatement103 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement103.tree)


                elif alt48 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:124:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement651)
                    forStatement104 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement104.tree)


                elif alt48 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:125:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement656)
                    forInStatement105 = self.forInStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forInStatement105.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:128:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
    def doWhileStatement(self, ):

        retval = self.doWhileStatement_return()
        retval.start = self.input.LT(1)
        doWhileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal106 = None
        LT107 = None
        LT109 = None
        string_literal110 = None
        LT111 = None
        char_literal112 = None
        char_literal114 = None
        set115 = None
        statement108 = None

        expression113 = None


        string_literal106_tree = None
        LT107_tree = None
        LT109_tree = None
        string_literal110_tree = None
        LT111_tree = None
        char_literal112_tree = None
        char_literal114_tree = None
        set115_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal106 = self.input.LT(1)
                self.match(self.input, 49, self.FOLLOW_49_in_doWhileStatement668)
                if self.failed:
                    return retval

                string_literal106_tree = self.adaptor.createWithPayload(string_literal106)
                self.adaptor.addChild(root_0, string_literal106_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:11: ( LT )*
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == LT) :
                        alt49 = 1


                    if alt49 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT107 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement670)
                        if self.failed:
                            return retval


                    else:
                        break #loop49


                self.following.append(self.FOLLOW_statement_in_doWhileStatement674)
                statement108 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement108.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:26: ( LT )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == LT) :
                        alt50 = 1


                    if alt50 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT109 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement676)
                        if self.failed:
                            return retval


                    else:
                        break #loop50


                string_literal110 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_doWhileStatement680)
                if self.failed:
                    return retval

                string_literal110_tree = self.adaptor.createWithPayload(string_literal110)
                self.adaptor.addChild(root_0, string_literal110_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:129:39: ( LT )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == LT) :
                        alt51 = 1


                    if alt51 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT111 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement682)
                        if self.failed:
                            return retval


                    else:
                        break #loop51


                char_literal112 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_doWhileStatement686)
                if self.failed:
                    return retval

                char_literal112_tree = self.adaptor.createWithPayload(char_literal112)
                self.adaptor.addChild(root_0, char_literal112_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement688)
                expression113 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression113.tree)
                char_literal114 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_doWhileStatement690)
                if self.failed:
                    return retval

                char_literal114_tree = self.adaptor.createWithPayload(char_literal114)
                self.adaptor.addChild(root_0, char_literal114_tree)

                set115 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement692
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def whileStatement(self, ):

        retval = self.whileStatement_return()
        retval.start = self.input.LT(1)
        whileStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal116 = None
        LT117 = None
        char_literal118 = None
        LT119 = None
        LT121 = None
        char_literal122 = None
        LT123 = None
        expression120 = None

        statement124 = None


        string_literal116_tree = None
        LT117_tree = None
        char_literal118_tree = None
        LT119_tree = None
        LT121_tree = None
        char_literal122_tree = None
        LT123_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal116 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_whileStatement711)
                if self.failed:
                    return retval

                string_literal116_tree = self.adaptor.createWithPayload(string_literal116)
                self.adaptor.addChild(root_0, string_literal116_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:14: ( LT )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == LT) :
                        alt52 = 1


                    if alt52 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT117 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement713)
                        if self.failed:
                            return retval


                    else:
                        break #loop52


                char_literal118 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_whileStatement717)
                if self.failed:
                    return retval

                char_literal118_tree = self.adaptor.createWithPayload(char_literal118)
                self.adaptor.addChild(root_0, char_literal118_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:23: ( LT )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == LT) :
                        alt53 = 1


                    if alt53 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT119 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement719)
                        if self.failed:
                            return retval


                    else:
                        break #loop53


                self.following.append(self.FOLLOW_expression_in_whileStatement723)
                expression120 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression120.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:39: ( LT )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == LT) :
                        alt54 = 1


                    if alt54 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT121 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement725)
                        if self.failed:
                            return retval


                    else:
                        break #loop54


                char_literal122 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_whileStatement729)
                if self.failed:
                    return retval

                char_literal122_tree = self.adaptor.createWithPayload(char_literal122)
                self.adaptor.addChild(root_0, char_literal122_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:48: ( LT )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == LT) :
                        alt55 = 1


                    if alt55 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT123 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement731)
                        if self.failed:
                            return retval


                    else:
                        break #loop55


                self.following.append(self.FOLLOW_statement_in_whileStatement735)
                statement124 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement124.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:136:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
    def forStatement(self, ):

        retval = self.forStatement_return()
        retval.start = self.input.LT(1)
        forStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal125 = None
        LT126 = None
        char_literal127 = None
        LT128 = None
        LT130 = None
        char_literal131 = None
        LT132 = None
        LT134 = None
        char_literal135 = None
        LT136 = None
        LT138 = None
        char_literal139 = None
        LT140 = None
        forStatementInitialiserPart129 = None

        expression133 = None

        expression137 = None

        statement141 = None


        string_literal125_tree = None
        LT126_tree = None
        char_literal127_tree = None
        LT128_tree = None
        LT130_tree = None
        char_literal131_tree = None
        LT132_tree = None
        LT134_tree = None
        char_literal135_tree = None
        LT136_tree = None
        LT138_tree = None
        char_literal139_tree = None
        LT140_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal125 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_forStatement747)
                if self.failed:
                    return retval

                string_literal125_tree = self.adaptor.createWithPayload(string_literal125)
                self.adaptor.addChild(root_0, string_literal125_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:12: ( LT )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == LT) :
                        alt56 = 1


                    if alt56 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT126 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement749)
                        if self.failed:
                            return retval


                    else:
                        break #loop56


                char_literal127 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_forStatement753)
                if self.failed:
                    return retval

                char_literal127_tree = self.adaptor.createWithPayload(char_literal127)
                self.adaptor.addChild(root_0, char_literal127_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:19: ( ( LT )* forStatementInitialiserPart )?
                alt58 = 2
                alt58 = self.dfa58.predict(self.input)
                if alt58 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:22: ( LT )*
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == LT) :
                            alt57 = 1


                        if alt57 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT128 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement756)
                            if self.failed:
                                return retval


                        else:
                            break #loop57


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement760)
                    forStatementInitialiserPart129 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart129.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:57: ( LT )*
                while True: #loop59
                    alt59 = 2
                    LA59_0 = self.input.LA(1)

                    if (LA59_0 == LT) :
                        alt59 = 1


                    if alt59 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT130 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement764)
                        if self.failed:
                            return retval


                    else:
                        break #loop59


                char_literal131 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_forStatement768)
                if self.failed:
                    return retval

                char_literal131_tree = self.adaptor.createWithPayload(char_literal131)
                self.adaptor.addChild(root_0, char_literal131_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:64: ( ( LT )* expression )?
                alt61 = 2
                alt61 = self.dfa61.predict(self.input)
                if alt61 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:67: ( LT )*
                    while True: #loop60
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if (LA60_0 == LT) :
                            alt60 = 1


                        if alt60 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT132 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement771)
                            if self.failed:
                                return retval


                        else:
                            break #loop60


                    self.following.append(self.FOLLOW_expression_in_forStatement775)
                    expression133 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression133.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:85: ( LT )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == LT) :
                        alt62 = 1


                    if alt62 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT134 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement779)
                        if self.failed:
                            return retval


                    else:
                        break #loop62


                char_literal135 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_forStatement783)
                if self.failed:
                    return retval

                char_literal135_tree = self.adaptor.createWithPayload(char_literal135)
                self.adaptor.addChild(root_0, char_literal135_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:92: ( ( LT )* expression )?
                alt64 = 2
                alt64 = self.dfa64.predict(self.input)
                if alt64 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:95: ( LT )*
                    while True: #loop63
                        alt63 = 2
                        LA63_0 = self.input.LA(1)

                        if (LA63_0 == LT) :
                            alt63 = 1


                        if alt63 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT136 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement786)
                            if self.failed:
                                return retval


                        else:
                            break #loop63


                    self.following.append(self.FOLLOW_expression_in_forStatement790)
                    expression137 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression137.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:113: ( LT )*
                while True: #loop65
                    alt65 = 2
                    LA65_0 = self.input.LA(1)

                    if (LA65_0 == LT) :
                        alt65 = 1


                    if alt65 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT138 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement794)
                        if self.failed:
                            return retval


                    else:
                        break #loop65


                char_literal139 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_forStatement798)
                if self.failed:
                    return retval

                char_literal139_tree = self.adaptor.createWithPayload(char_literal139)
                self.adaptor.addChild(root_0, char_literal139_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:122: ( LT )*
                while True: #loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == LT) :
                        alt66 = 1


                    if alt66 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT140 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement800)
                        if self.failed:
                            return retval


                    else:
                        break #loop66


                self.following.append(self.FOLLOW_statement_in_forStatement804)
                statement141 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement141.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:140:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );
    def forStatementInitialiserPart(self, ):

        retval = self.forStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal143 = None
        LT144 = None
        expressionNoIn142 = None

        variableDeclarationListNoIn145 = None


        string_literal143_tree = None
        LT144_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:2: ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn )
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if ((StringLiteral <= LA68_0 <= Identifier) or (37 <= LA68_0 <= 38) or LA68_0 == 41 or LA68_0 == 52 or (66 <= LA68_0 <= 67) or (99 <= LA68_0 <= 100) or (104 <= LA68_0 <= 116)) :
                    alt68 = 1
                elif (LA68_0 == 43) :
                    alt68 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("140:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );", 68, 0, self.input)

                    raise nvae

                if alt68 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart816)
                    expressionNoIn142 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn142.tree)


                elif alt68 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:4: 'var' ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    string_literal143 = self.input.LT(1)
                    self.match(self.input, 43, self.FOLLOW_43_in_forStatementInitialiserPart821)
                    if self.failed:
                        return retval

                    string_literal143_tree = self.adaptor.createWithPayload(string_literal143)
                    self.adaptor.addChild(root_0, string_literal143_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:12: ( LT )*
                    while True: #loop67
                        alt67 = 2
                        LA67_0 = self.input.LA(1)

                        if (LA67_0 == LT) :
                            alt67 = 1


                        if alt67 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT144 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart823)
                            if self.failed:
                                return retval


                        else:
                            break #loop67


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart827)
                    variableDeclarationListNoIn145 = self.variableDeclarationListNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationListNoIn145.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def forInStatement(self, ):

        retval = self.forInStatement_return()
        retval.start = self.input.LT(1)
        forInStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal146 = None
        LT147 = None
        string_literal148 = None
        LT149 = None
        char_literal150 = None
        LT151 = None
        LT153 = None
        string_literal154 = None
        LT155 = None
        LT157 = None
        char_literal158 = None
        LT159 = None
        forInStatementInitialiserPart152 = None

        expression156 = None

        statement160 = None


        string_literal146_tree = None
        LT147_tree = None
        string_literal148_tree = None
        LT149_tree = None
        char_literal150_tree = None
        LT151_tree = None
        LT153_tree = None
        string_literal154_tree = None
        LT155_tree = None
        LT157_tree = None
        char_literal158_tree = None
        LT159_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal146 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_forInStatement839)
                if self.failed:
                    return retval

                string_literal146_tree = self.adaptor.createWithPayload(string_literal146)
                self.adaptor.addChild(root_0, string_literal146_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:12: ( LT )*
                while True: #loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == LT) :
                        LA69_2 = self.input.LA(2)

                        if (self.synpred87()) :
                            alt69 = 1




                    if alt69 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT147 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement841)
                        if self.failed:
                            return retval


                    else:
                        break #loop69


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:15: ( 'each' )?
                alt70 = 2
                LA70_0 = self.input.LA(1)

                if (LA70_0 == 52) :
                    alt70 = 1
                if alt70 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal148 = self.input.LT(1)
                    self.match(self.input, 52, self.FOLLOW_52_in_forInStatement845)
                    if self.failed:
                        return retval

                    string_literal148_tree = self.adaptor.createWithPayload(string_literal148)
                    self.adaptor.addChild(root_0, string_literal148_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:25: ( LT )*
                while True: #loop71
                    alt71 = 2
                    LA71_0 = self.input.LA(1)

                    if (LA71_0 == LT) :
                        alt71 = 1


                    if alt71 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT149 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement848)
                        if self.failed:
                            return retval


                    else:
                        break #loop71


                char_literal150 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_forInStatement852)
                if self.failed:
                    return retval

                char_literal150_tree = self.adaptor.createWithPayload(char_literal150)
                self.adaptor.addChild(root_0, char_literal150_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:34: ( LT )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == LT) :
                        alt72 = 1


                    if alt72 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT151 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement854)
                        if self.failed:
                            return retval


                    else:
                        break #loop72


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement858)
                forInStatementInitialiserPart152 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart152.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:69: ( LT )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == LT) :
                        alt73 = 1


                    if alt73 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT153 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement860)
                        if self.failed:
                            return retval


                    else:
                        break #loop73


                string_literal154 = self.input.LT(1)
                self.match(self.input, 53, self.FOLLOW_53_in_forInStatement864)
                if self.failed:
                    return retval

                string_literal154_tree = self.adaptor.createWithPayload(string_literal154)
                self.adaptor.addChild(root_0, string_literal154_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:79: ( LT )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == LT) :
                        alt74 = 1


                    if alt74 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT155 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement866)
                        if self.failed:
                            return retval


                    else:
                        break #loop74


                self.following.append(self.FOLLOW_expression_in_forInStatement870)
                expression156 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression156.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:95: ( LT )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == LT) :
                        alt75 = 1


                    if alt75 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT157 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement872)
                        if self.failed:
                            return retval


                    else:
                        break #loop75


                char_literal158 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_forInStatement876)
                if self.failed:
                    return retval

                char_literal158_tree = self.adaptor.createWithPayload(char_literal158)
                self.adaptor.addChild(root_0, char_literal158_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:104: ( LT )*
                while True: #loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == LT) :
                        alt76 = 1


                    if alt76 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT159 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement878)
                        if self.failed:
                            return retval


                    else:
                        break #loop76


                self.following.append(self.FOLLOW_statement_in_forInStatement882)
                statement160 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement160.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );
    def forInStatementInitialiserPart(self, ):

        retval = self.forInStatementInitialiserPart_return()
        retval.start = self.input.LT(1)
        forInStatementInitialiserPart_StartIndex = self.input.index()
        root_0 = None

        string_literal162 = None
        LT163 = None
        leftHandSideExpression161 = None

        variableDeclarationNoIn164 = None


        string_literal162_tree = None
        LT163_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:2: ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn )
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if ((StringLiteral <= LA78_0 <= Identifier) or (37 <= LA78_0 <= 38) or LA78_0 == 41 or LA78_0 == 52 or (66 <= LA78_0 <= 67) or (111 <= LA78_0 <= 116)) :
                    alt78 = 1
                elif (LA78_0 == 43) :
                    alt78 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("149:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );", 78, 0, self.input)

                    raise nvae

                if alt78 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart894)
                    leftHandSideExpression161 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression161.tree)


                elif alt78 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: 'var' ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    string_literal162 = self.input.LT(1)
                    self.match(self.input, 43, self.FOLLOW_43_in_forInStatementInitialiserPart899)
                    if self.failed:
                        return retval

                    string_literal162_tree = self.adaptor.createWithPayload(string_literal162)
                    self.adaptor.addChild(root_0, string_literal162_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:12: ( LT )*
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == LT) :
                            alt77 = 1


                        if alt77 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT163 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart901)
                            if self.failed:
                                return retval


                        else:
                            break #loop77


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart905)
                    variableDeclarationNoIn164 = self.variableDeclarationNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableDeclarationNoIn164.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
    def continueStatement(self, ):

        retval = self.continueStatement_return()
        retval.start = self.input.LT(1)
        continueStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal165 = None
        set167 = None
        identifier166 = None


        string_literal165_tree = None
        set167_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal165 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_continueStatement916)
                if self.failed:
                    return retval

                string_literal165_tree = self.adaptor.createWithPayload(string_literal165)
                self.adaptor.addChild(root_0, string_literal165_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:15: ( identifier )?
                alt79 = 2
                LA79_0 = self.input.LA(1)

                if (LA79_0 == Identifier or LA79_0 == 52 or (112 <= LA79_0 <= 113)) :
                    alt79 = 1
                if alt79 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement918)
                    identifier166 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier166.tree)



                set167 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_continueStatement921
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
    def breakStatement(self, ):

        retval = self.breakStatement_return()
        retval.start = self.input.LT(1)
        breakStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal168 = None
        set170 = None
        identifier169 = None


        string_literal168_tree = None
        set170_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal168 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_breakStatement939)
                if self.failed:
                    return retval

                string_literal168_tree = self.adaptor.createWithPayload(string_literal168)
                self.adaptor.addChild(root_0, string_literal168_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:12: ( identifier )?
                alt80 = 2
                LA80_0 = self.input.LA(1)

                if (LA80_0 == Identifier or LA80_0 == 52 or (112 <= LA80_0 <= 113)) :
                    alt80 = 1
                if alt80 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement941)
                    identifier169 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier169.tree)



                set170 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_breakStatement944
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:162:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
    def returnStatement(self, ):

        retval = self.returnStatement_return()
        retval.start = self.input.LT(1)
        returnStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal171 = None
        set173 = None
        expression172 = None


        string_literal171_tree = None
        set173_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal171 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_returnStatement962)
                if self.failed:
                    return retval

                string_literal171_tree = self.adaptor.createWithPayload(string_literal171)
                self.adaptor.addChild(root_0, string_literal171_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:13: ( expression )?
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if ((StringLiteral <= LA81_0 <= Identifier) or (37 <= LA81_0 <= 38) or LA81_0 == 41 or LA81_0 == 52 or (66 <= LA81_0 <= 67) or (99 <= LA81_0 <= 100) or (104 <= LA81_0 <= 116)) :
                    alt81 = 1
                if alt81 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement964)
                    expression172 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression172.tree)



                set173 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_returnStatement967
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:166:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
    def withStatement(self, ):

        retval = self.withStatement_return()
        retval.start = self.input.LT(1)
        withStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal174 = None
        LT175 = None
        char_literal176 = None
        LT177 = None
        LT179 = None
        char_literal180 = None
        LT181 = None
        expression178 = None

        statement182 = None


        string_literal174_tree = None
        LT175_tree = None
        char_literal176_tree = None
        LT177_tree = None
        LT179_tree = None
        char_literal180_tree = None
        LT181_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal174 = self.input.LT(1)
                self.match(self.input, 57, self.FOLLOW_57_in_withStatement986)
                if self.failed:
                    return retval

                string_literal174_tree = self.adaptor.createWithPayload(string_literal174)
                self.adaptor.addChild(root_0, string_literal174_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:13: ( LT )*
                while True: #loop82
                    alt82 = 2
                    LA82_0 = self.input.LA(1)

                    if (LA82_0 == LT) :
                        alt82 = 1


                    if alt82 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT175 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement988)
                        if self.failed:
                            return retval


                    else:
                        break #loop82


                char_literal176 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_withStatement992)
                if self.failed:
                    return retval

                char_literal176_tree = self.adaptor.createWithPayload(char_literal176)
                self.adaptor.addChild(root_0, char_literal176_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:22: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        alt83 = 1


                    if alt83 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT177 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement994)
                        if self.failed:
                            return retval


                    else:
                        break #loop83


                self.following.append(self.FOLLOW_expression_in_withStatement998)
                expression178 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression178.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:38: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        alt84 = 1


                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT179 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1000)
                        if self.failed:
                            return retval


                    else:
                        break #loop84


                char_literal180 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_withStatement1004)
                if self.failed:
                    return retval

                char_literal180_tree = self.adaptor.createWithPayload(char_literal180)
                self.adaptor.addChild(root_0, char_literal180_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:47: ( LT )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == LT) :
                        alt85 = 1


                    if alt85 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT181 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1006)
                        if self.failed:
                            return retval


                    else:
                        break #loop85


                self.following.append(self.FOLLOW_statement_in_withStatement1010)
                statement182 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement182.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:170:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
    def labelledStatement(self, ):

        retval = self.labelledStatement_return()
        retval.start = self.input.LT(1)
        labelledStatement_StartIndex = self.input.index()
        root_0 = None

        LT184 = None
        char_literal185 = None
        LT186 = None
        identifier183 = None

        statement187 = None


        LT184_tree = None
        char_literal185_tree = None
        LT186_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1021)
                identifier183 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier183.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:17: ( LT )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == LT) :
                        alt86 = 1


                    if alt86 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT184 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1023)
                        if self.failed:
                            return retval


                    else:
                        break #loop86


                char_literal185 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_labelledStatement1027)
                if self.failed:
                    return retval

                char_literal185_tree = self.adaptor.createWithPayload(char_literal185)
                self.adaptor.addChild(root_0, char_literal185_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:26: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        alt87 = 1


                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT186 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1029)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                self.following.append(self.FOLLOW_statement_in_labelledStatement1033)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:174:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
    def switchStatement(self, ):

        retval = self.switchStatement_return()
        retval.start = self.input.LT(1)
        switchStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal188 = None
        LT189 = None
        char_literal190 = None
        LT191 = None
        LT193 = None
        char_literal194 = None
        LT195 = None
        expression192 = None

        caseBlock196 = None


        string_literal188_tree = None
        LT189_tree = None
        char_literal190_tree = None
        LT191_tree = None
        LT193_tree = None
        char_literal194_tree = None
        LT195_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal188 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_switchStatement1045)
                if self.failed:
                    return retval

                string_literal188_tree = self.adaptor.createWithPayload(string_literal188)
                self.adaptor.addChild(root_0, string_literal188_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:15: ( LT )*
                while True: #loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == LT) :
                        alt88 = 1


                    if alt88 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT189 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1047)
                        if self.failed:
                            return retval


                    else:
                        break #loop88


                char_literal190 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_switchStatement1051)
                if self.failed:
                    return retval

                char_literal190_tree = self.adaptor.createWithPayload(char_literal190)
                self.adaptor.addChild(root_0, char_literal190_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:24: ( LT )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LT) :
                        alt89 = 1


                    if alt89 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT191 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1053)
                        if self.failed:
                            return retval


                    else:
                        break #loop89


                self.following.append(self.FOLLOW_expression_in_switchStatement1057)
                expression192 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression192.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:40: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        alt90 = 1


                    if alt90 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT193 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1059)
                        if self.failed:
                            return retval


                    else:
                        break #loop90


                char_literal194 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_switchStatement1063)
                if self.failed:
                    return retval

                char_literal194_tree = self.adaptor.createWithPayload(char_literal194)
                self.adaptor.addChild(root_0, char_literal194_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:49: ( LT )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == LT) :
                        alt91 = 1


                    if alt91 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT195 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1065)
                        if self.failed:
                            return retval


                    else:
                        break #loop91


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1069)
                caseBlock196 = self.caseBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, caseBlock196.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:178:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
    def caseBlock(self, ):

        retval = self.caseBlock_return()
        retval.start = self.input.LT(1)
        caseBlock_StartIndex = self.input.index()
        root_0 = None

        char_literal197 = None
        LT198 = None
        LT200 = None
        LT202 = None
        LT204 = None
        char_literal205 = None
        caseClause199 = None

        defaultClause201 = None

        caseClause203 = None


        char_literal197_tree = None
        LT198_tree = None
        LT200_tree = None
        LT202_tree = None
        LT204_tree = None
        char_literal205_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal197 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_caseBlock1081)
                if self.failed:
                    return retval

                char_literal197_tree = self.adaptor.createWithPayload(char_literal197)
                self.adaptor.addChild(root_0, char_literal197_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:8: ( ( LT )* caseClause )*
                while True: #loop93
                    alt93 = 2
                    alt93 = self.dfa93.predict(self.input)
                    if alt93 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:11: ( LT )*
                        while True: #loop92
                            alt92 = 2
                            LA92_0 = self.input.LA(1)

                            if (LA92_0 == LT) :
                                alt92 = 1


                            if alt92 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT198 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1084)
                                if self.failed:
                                    return retval


                            else:
                                break #loop92


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1088)
                        caseClause199 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause199.tree)


                    else:
                        break #loop93


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt97 = 2
                alt97 = self.dfa97.predict(self.input)
                if alt97 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:30: ( LT )*
                    while True: #loop94
                        alt94 = 2
                        LA94_0 = self.input.LA(1)

                        if (LA94_0 == LT) :
                            alt94 = 1


                        if alt94 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT200 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1093)
                            if self.failed:
                                return retval


                        else:
                            break #loop94


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1097)
                    defaultClause201 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause201.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:47: ( ( LT )* caseClause )*
                    while True: #loop96
                        alt96 = 2
                        alt96 = self.dfa96.predict(self.input)
                        if alt96 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:50: ( LT )*
                            while True: #loop95
                                alt95 = 2
                                LA95_0 = self.input.LA(1)

                                if (LA95_0 == LT) :
                                    alt95 = 1


                                if alt95 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT202 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1100)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop95


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1104)
                            caseClause203 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause203.tree)


                        else:
                            break #loop96





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:70: ( LT )*
                while True: #loop98
                    alt98 = 2
                    LA98_0 = self.input.LA(1)

                    if (LA98_0 == LT) :
                        alt98 = 1


                    if alt98 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT204 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1110)
                        if self.failed:
                            return retval


                    else:
                        break #loop98


                char_literal205 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_caseBlock1114)
                if self.failed:
                    return retval

                char_literal205_tree = self.adaptor.createWithPayload(char_literal205)
                self.adaptor.addChild(root_0, char_literal205_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:182:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
    def caseClause(self, ):

        retval = self.caseClause_return()
        retval.start = self.input.LT(1)
        caseClause_StartIndex = self.input.index()
        root_0 = None

        string_literal206 = None
        LT207 = None
        LT209 = None
        char_literal210 = None
        LT211 = None
        expression208 = None

        statementList212 = None


        string_literal206_tree = None
        LT207_tree = None
        LT209_tree = None
        char_literal210_tree = None
        LT211_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal206 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_caseClause1125)
                if self.failed:
                    return retval

                string_literal206_tree = self.adaptor.createWithPayload(string_literal206)
                self.adaptor.addChild(root_0, string_literal206_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:13: ( LT )*
                while True: #loop99
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if (LA99_0 == LT) :
                        alt99 = 1


                    if alt99 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT207 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1127)
                        if self.failed:
                            return retval


                    else:
                        break #loop99


                self.following.append(self.FOLLOW_expression_in_caseClause1131)
                expression208 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression208.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:29: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT209 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1133)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                char_literal210 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_caseClause1137)
                if self.failed:
                    return retval

                char_literal210_tree = self.adaptor.createWithPayload(char_literal210)
                self.adaptor.addChild(root_0, char_literal210_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:38: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        LA101_2 = self.input.LA(2)

                        if (self.synpred122()) :
                            alt101 = 1




                    if alt101 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT211 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1139)
                        if self.failed:
                            return retval


                    else:
                        break #loop101


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:41: ( statementList )?
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if ((StringLiteral <= LA102_0 <= Identifier) or (37 <= LA102_0 <= 38) or LA102_0 == 41 or (43 <= LA102_0 <= 45) or LA102_0 == 47 or (49 <= LA102_0 <= 52) or (54 <= LA102_0 <= 57) or LA102_0 == 59 or (62 <= LA102_0 <= 63) or (66 <= LA102_0 <= 67) or (99 <= LA102_0 <= 100) or (104 <= LA102_0 <= 116)) :
                    alt102 = 1
                if alt102 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1143)
                    statementList212 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList212.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:186:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
    def defaultClause(self, ):

        retval = self.defaultClause_return()
        retval.start = self.input.LT(1)
        defaultClause_StartIndex = self.input.index()
        root_0 = None

        string_literal213 = None
        LT214 = None
        char_literal215 = None
        LT216 = None
        statementList217 = None


        string_literal213_tree = None
        LT214_tree = None
        char_literal215_tree = None
        LT216_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal213 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_defaultClause1156)
                if self.failed:
                    return retval

                string_literal213_tree = self.adaptor.createWithPayload(string_literal213)
                self.adaptor.addChild(root_0, string_literal213_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:16: ( LT )*
                while True: #loop103
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if (LA103_0 == LT) :
                        alt103 = 1


                    if alt103 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT214 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1158)
                        if self.failed:
                            return retval


                    else:
                        break #loop103


                char_literal215 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_defaultClause1162)
                if self.failed:
                    return retval

                char_literal215_tree = self.adaptor.createWithPayload(char_literal215)
                self.adaptor.addChild(root_0, char_literal215_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:25: ( LT )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == LT) :
                        LA104_2 = self.input.LA(2)

                        if (self.synpred125()) :
                            alt104 = 1




                    if alt104 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT216 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1164)
                        if self.failed:
                            return retval


                    else:
                        break #loop104


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:28: ( statementList )?
                alt105 = 2
                LA105_0 = self.input.LA(1)

                if ((StringLiteral <= LA105_0 <= Identifier) or (37 <= LA105_0 <= 38) or LA105_0 == 41 or (43 <= LA105_0 <= 45) or LA105_0 == 47 or (49 <= LA105_0 <= 52) or (54 <= LA105_0 <= 57) or LA105_0 == 59 or (62 <= LA105_0 <= 63) or (66 <= LA105_0 <= 67) or (99 <= LA105_0 <= 100) or (104 <= LA105_0 <= 116)) :
                    alt105 = 1
                if alt105 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1168)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:190:1: throwStatement : 'throw' expression ( LT | ';' ) ;
    def throwStatement(self, ):

        retval = self.throwStatement_return()
        retval.start = self.input.LT(1)
        throwStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal218 = None
        set220 = None
        expression219 = None


        string_literal218_tree = None
        set220_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal218 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_throwStatement1181)
                if self.failed:
                    return retval

                string_literal218_tree = self.adaptor.createWithPayload(string_literal218)
                self.adaptor.addChild(root_0, string_literal218_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1183)
                expression219 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression219.tree)
                set220 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 45:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_throwStatement1185
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:194:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
    def tryStatement(self, ):

        retval = self.tryStatement_return()
        retval.start = self.input.LT(1)
        tryStatement_StartIndex = self.input.index()
        root_0 = None

        string_literal221 = None
        LT222 = None
        LT224 = None
        LT227 = None
        statementBlock223 = None

        finallyClause225 = None

        catchClause226 = None

        finallyClause228 = None


        string_literal221_tree = None
        LT222_tree = None
        LT224_tree = None
        LT227_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal221 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_tryStatement1203)
                if self.failed:
                    return retval

                string_literal221_tree = self.adaptor.createWithPayload(string_literal221)
                self.adaptor.addChild(root_0, string_literal221_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:12: ( LT )*
                while True: #loop106
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if (LA106_0 == LT) :
                        alt106 = 1


                    if alt106 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT222 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1205)
                        if self.failed:
                            return retval


                    else:
                        break #loop106


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1209)
                statementBlock223 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock223.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:32: ( LT )*
                while True: #loop107
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if (LA107_0 == LT) :
                        alt107 = 1


                    if alt107 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT224 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1211)
                        if self.failed:
                            return retval


                    else:
                        break #loop107


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt110 = 2
                LA110_0 = self.input.LA(1)

                if (LA110_0 == 65) :
                    alt110 = 1
                elif (LA110_0 == 64) :
                    alt110 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("195:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 110, 0, self.input)

                    raise nvae

                if alt110 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1216)
                    finallyClause225 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause225.tree)


                elif alt110 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1220)
                    catchClause226 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause226.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:64: ( ( LT )* finallyClause )?
                    alt109 = 2
                    alt109 = self.dfa109.predict(self.input)
                    if alt109 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:67: ( LT )*
                        while True: #loop108
                            alt108 = 2
                            LA108_0 = self.input.LA(1)

                            if (LA108_0 == LT) :
                                alt108 = 1


                            if alt108 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT227 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1223)
                                if self.failed:
                                    return retval


                            else:
                                break #loop108


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1227)
                        finallyClause228 = self.finallyClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, finallyClause228.tree)









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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:198:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
    def catchClause(self, ):

        retval = self.catchClause_return()
        retval.start = self.input.LT(1)
        catchClause_StartIndex = self.input.index()
        root_0 = None

        string_literal229 = None
        LT230 = None
        char_literal231 = None
        LT232 = None
        LT234 = None
        char_literal235 = None
        LT236 = None
        identifier233 = None

        statementBlock237 = None


        string_literal229_tree = None
        LT230_tree = None
        char_literal231_tree = None
        LT232_tree = None
        LT234_tree = None
        char_literal235_tree = None
        LT236_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal229 = self.input.LT(1)
                self.match(self.input, 64, self.FOLLOW_64_in_catchClause1248)
                if self.failed:
                    return retval

                string_literal229_tree = self.adaptor.createWithPayload(string_literal229)
                self.adaptor.addChild(root_0, string_literal229_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:14: ( LT )*
                while True: #loop111
                    alt111 = 2
                    LA111_0 = self.input.LA(1)

                    if (LA111_0 == LT) :
                        alt111 = 1


                    if alt111 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT230 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1250)
                        if self.failed:
                            return retval


                    else:
                        break #loop111


                char_literal231 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_catchClause1254)
                if self.failed:
                    return retval

                char_literal231_tree = self.adaptor.createWithPayload(char_literal231)
                self.adaptor.addChild(root_0, char_literal231_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:23: ( LT )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == LT) :
                        alt112 = 1


                    if alt112 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT232 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1256)
                        if self.failed:
                            return retval


                    else:
                        break #loop112


                self.following.append(self.FOLLOW_identifier_in_catchClause1260)
                identifier233 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier233.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:39: ( LT )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == LT) :
                        alt113 = 1


                    if alt113 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT234 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1262)
                        if self.failed:
                            return retval


                    else:
                        break #loop113


                char_literal235 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_catchClause1266)
                if self.failed:
                    return retval

                char_literal235_tree = self.adaptor.createWithPayload(char_literal235)
                self.adaptor.addChild(root_0, char_literal235_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:48: ( LT )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == LT) :
                        alt114 = 1


                    if alt114 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT236 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1268)
                        if self.failed:
                            return retval


                    else:
                        break #loop114


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1272)
                statementBlock237 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock237.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:202:1: finallyClause : 'finally' ( LT )* statementBlock ;
    def finallyClause(self, ):

        retval = self.finallyClause_return()
        retval.start = self.input.LT(1)
        finallyClause_StartIndex = self.input.index()
        root_0 = None

        string_literal238 = None
        LT239 = None
        statementBlock240 = None


        string_literal238_tree = None
        LT239_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal238 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_finallyClause1284)
                if self.failed:
                    return retval

                string_literal238_tree = self.adaptor.createWithPayload(string_literal238)
                self.adaptor.addChild(root_0, string_literal238_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:16: ( LT )*
                while True: #loop115
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == LT) :
                        alt115 = 1


                    if alt115 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT239 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1286)
                        if self.failed:
                            return retval


                    else:
                        break #loop115


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause1290)
                statementBlock240 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock240.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
    def expression(self, ):

        retval = self.expression_return()
        retval.start = self.input.LT(1)
        expression_StartIndex = self.input.index()
        root_0 = None

        LT242 = None
        char_literal243 = None
        LT244 = None
        assignmentExpression241 = None

        assignmentExpression245 = None


        LT242_tree = None
        char_literal243_tree = None
        LT244_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression1302)
                assignmentExpression241 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression241.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop118
                    alt118 = 2
                    alt118 = self.dfa118.predict(self.input)
                    if alt118 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:28: ( LT )*
                        while True: #loop116
                            alt116 = 2
                            LA116_0 = self.input.LA(1)

                            if (LA116_0 == LT) :
                                alt116 = 1


                            if alt116 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT242 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1305)
                                if self.failed:
                                    return retval


                            else:
                                break #loop116


                        char_literal243 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_expression1309)
                        if self.failed:
                            return retval

                        char_literal243_tree = self.adaptor.createWithPayload(char_literal243)
                        self.adaptor.addChild(root_0, char_literal243_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:37: ( LT )*
                        while True: #loop117
                            alt117 = 2
                            LA117_0 = self.input.LA(1)

                            if (LA117_0 == LT) :
                                alt117 = 1


                            if alt117 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT244 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1311)
                                if self.failed:
                                    return retval


                            else:
                                break #loop117


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression1315)
                        assignmentExpression245 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression245.tree)


                    else:
                        break #loop118





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
    def expressionNoIn(self, ):

        retval = self.expressionNoIn_return()
        retval.start = self.input.LT(1)
        expressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT247 = None
        char_literal248 = None
        LT249 = None
        assignmentExpressionNoIn246 = None

        assignmentExpressionNoIn250 = None


        LT247_tree = None
        char_literal248_tree = None
        LT249_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1329)
                assignmentExpressionNoIn246 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn246.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop121
                    alt121 = 2
                    alt121 = self.dfa121.predict(self.input)
                    if alt121 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:32: ( LT )*
                        while True: #loop119
                            alt119 = 2
                            LA119_0 = self.input.LA(1)

                            if (LA119_0 == LT) :
                                alt119 = 1


                            if alt119 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT247 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1332)
                                if self.failed:
                                    return retval


                            else:
                                break #loop119


                        char_literal248 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_expressionNoIn1336)
                        if self.failed:
                            return retval

                        char_literal248_tree = self.adaptor.createWithPayload(char_literal248)
                        self.adaptor.addChild(root_0, char_literal248_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:41: ( LT )*
                        while True: #loop120
                            alt120 = 2
                            LA120_0 = self.input.LA(1)

                            if (LA120_0 == LT) :
                                alt120 = 1


                            if alt120 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT249 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1338)
                                if self.failed:
                                    return retval


                            else:
                                break #loop120


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1342)
                        assignmentExpressionNoIn250 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn250.tree)


                    else:
                        break #loop121





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );
    def assignmentExpression(self, ):

        retval = self.assignmentExpression_return()
        retval.start = self.input.LT(1)
        assignmentExpression_StartIndex = self.input.index()
        root_0 = None

        LT253 = None
        LT255 = None
        conditionalExpression251 = None

        leftHandSideExpression252 = None

        assignmentOperator254 = None

        assignmentExpression256 = None


        LT253_tree = None
        LT255_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:2: ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
                alt124 = 2
                LA124 = self.input.LA(1)
                if LA124 == 111:
                    LA124_1 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 1, self.input)

                        raise nvae

                elif LA124 == Identifier or LA124 == 52 or LA124 == 112 or LA124 == 113:
                    LA124_2 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 2, self.input)

                        raise nvae

                elif LA124 == StringLiteral or LA124 == NumericLiteral or LA124 == RegularExpressionLiteral or LA124 == 114 or LA124 == 115 or LA124 == 116:
                    LA124_3 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 3, self.input)

                        raise nvae

                elif LA124 == 67:
                    LA124_4 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 4, self.input)

                        raise nvae

                elif LA124 == 41:
                    LA124_5 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 5, self.input)

                        raise nvae

                elif LA124 == 38:
                    LA124_6 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 6, self.input)

                        raise nvae

                elif LA124 == 37:
                    LA124_7 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 7, self.input)

                        raise nvae

                elif LA124 == 66:
                    LA124_8 = self.input.LA(2)

                    if (self.synpred144()) :
                        alt124 = 1
                    elif (True) :
                        alt124 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 8, self.input)

                        raise nvae

                elif LA124 == 99 or LA124 == 100 or LA124 == 104 or LA124 == 105 or LA124 == 106 or LA124 == 107 or LA124 == 108 or LA124 == 109 or LA124 == 110:
                    alt124 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("215:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 124, 0, self.input)

                    raise nvae

                if alt124 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression1356)
                    conditionalExpression251 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression251.tree)


                elif alt124 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1361)
                    leftHandSideExpression252 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression252.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:29: ( LT )*
                    while True: #loop122
                        alt122 = 2
                        LA122_0 = self.input.LA(1)

                        if (LA122_0 == LT) :
                            alt122 = 1


                        if alt122 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT253 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1363)
                            if self.failed:
                                return retval


                        else:
                            break #loop122


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1367)
                    assignmentOperator254 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator254.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:53: ( LT )*
                    while True: #loop123
                        alt123 = 2
                        LA123_0 = self.input.LA(1)

                        if (LA123_0 == LT) :
                            alt123 = 1


                        if alt123 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT255 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1369)
                            if self.failed:
                                return retval


                        else:
                            break #loop123


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1373)
                    assignmentExpression256 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression256.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );
    def assignmentExpressionNoIn(self, ):

        retval = self.assignmentExpressionNoIn_return()
        retval.start = self.input.LT(1)
        assignmentExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT259 = None
        LT261 = None
        conditionalExpressionNoIn257 = None

        leftHandSideExpression258 = None

        assignmentOperator260 = None

        assignmentExpressionNoIn262 = None


        LT259_tree = None
        LT261_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:2: ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
                alt127 = 2
                LA127 = self.input.LA(1)
                if LA127 == 111:
                    LA127_1 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 1, self.input)

                        raise nvae

                elif LA127 == Identifier or LA127 == 52 or LA127 == 112 or LA127 == 113:
                    LA127_2 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 2, self.input)

                        raise nvae

                elif LA127 == StringLiteral or LA127 == NumericLiteral or LA127 == RegularExpressionLiteral or LA127 == 114 or LA127 == 115 or LA127 == 116:
                    LA127_3 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 3, self.input)

                        raise nvae

                elif LA127 == 67:
                    LA127_4 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 4, self.input)

                        raise nvae

                elif LA127 == 41:
                    LA127_5 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 5, self.input)

                        raise nvae

                elif LA127 == 38:
                    LA127_6 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 6, self.input)

                        raise nvae

                elif LA127 == 37:
                    LA127_7 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 7, self.input)

                        raise nvae

                elif LA127 == 66:
                    LA127_8 = self.input.LA(2)

                    if (self.synpred147()) :
                        alt127 = 1
                    elif (True) :
                        alt127 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 8, self.input)

                        raise nvae

                elif LA127 == 99 or LA127 == 100 or LA127 == 104 or LA127 == 105 or LA127 == 106 or LA127 == 107 or LA127 == 108 or LA127 == 109 or LA127 == 110:
                    alt127 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("220:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 127, 0, self.input)

                    raise nvae

                if alt127 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1385)
                    conditionalExpressionNoIn257 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn257.tree)


                elif alt127 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:222:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1390)
                    leftHandSideExpression258 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression258.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:222:29: ( LT )*
                    while True: #loop125
                        alt125 = 2
                        LA125_0 = self.input.LA(1)

                        if (LA125_0 == LT) :
                            alt125 = 1


                        if alt125 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT259 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1392)
                            if self.failed:
                                return retval


                        else:
                            break #loop125


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1396)
                    assignmentOperator260 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator260.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:222:53: ( LT )*
                    while True: #loop126
                        alt126 = 2
                        LA126_0 = self.input.LA(1)

                        if (LA126_0 == LT) :
                            alt126 = 1


                        if alt126 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT261 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1398)
                            if self.failed:
                                return retval


                        else:
                            break #loop126


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1402)
                    assignmentExpressionNoIn262 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn262.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression263 = None

        newExpression264 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:2: ( callExpression | newExpression )
                alt128 = 2
                LA128 = self.input.LA(1)
                if LA128 == 111:
                    LA128_1 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 1, self.input)

                        raise nvae

                elif LA128 == Identifier or LA128 == 52 or LA128 == 112 or LA128 == 113:
                    LA128_2 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 2, self.input)

                        raise nvae

                elif LA128 == StringLiteral or LA128 == NumericLiteral or LA128 == RegularExpressionLiteral or LA128 == 114 or LA128 == 115 or LA128 == 116:
                    LA128_3 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 3, self.input)

                        raise nvae

                elif LA128 == 67:
                    LA128_4 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 4, self.input)

                        raise nvae

                elif LA128 == 41:
                    LA128_5 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 5, self.input)

                        raise nvae

                elif LA128 == 38:
                    LA128_6 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 6, self.input)

                        raise nvae

                elif LA128 == 37:
                    LA128_7 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 7, self.input)

                        raise nvae

                elif LA128 == 66:
                    LA128_8 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 8, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("225:1: leftHandSideExpression : ( callExpression | newExpression );", 128, 0, self.input)

                    raise nvae

                if alt128 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression1414)
                    callExpression263 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression263.tree)


                elif alt128 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:227:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression1419)
                    newExpression264 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression264.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );
    def newExpression(self, ):

        retval = self.newExpression_return()
        retval.start = self.input.LT(1)
        newExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal266 = None
        LT267 = None
        memberExpression265 = None

        newExpression268 = None


        string_literal266_tree = None
        LT267_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:2: ( memberExpression | 'new' ( LT )* newExpression )
                alt130 = 2
                LA130_0 = self.input.LA(1)

                if ((StringLiteral <= LA130_0 <= Identifier) or (37 <= LA130_0 <= 38) or LA130_0 == 41 or LA130_0 == 52 or LA130_0 == 67 or (111 <= LA130_0 <= 116)) :
                    alt130 = 1
                elif (LA130_0 == 66) :
                    LA130_8 = self.input.LA(2)

                    if (self.synpred151()) :
                        alt130 = 1
                    elif (True) :
                        alt130 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("230:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 130, 8, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("230:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 130, 0, self.input)

                    raise nvae

                if alt130 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression1431)
                    memberExpression265 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression265.tree)


                elif alt130 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:4: 'new' ( LT )* newExpression
                    root_0 = self.adaptor.nil()

                    string_literal266 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_newExpression1436)
                    if self.failed:
                        return retval

                    string_literal266_tree = self.adaptor.createWithPayload(string_literal266)
                    self.adaptor.addChild(root_0, string_literal266_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:232:12: ( LT )*
                    while True: #loop129
                        alt129 = 2
                        LA129_0 = self.input.LA(1)

                        if (LA129_0 == LT) :
                            alt129 = 1


                        if alt129 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT267 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1438)
                            if self.failed:
                                return retval


                        else:
                            break #loop129


                    self.following.append(self.FOLLOW_newExpression_in_newExpression1442)
                    newExpression268 = self.newExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, newExpression268.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:1: memberExpression : ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* ;
    def memberExpression(self, ):

        retval = self.memberExpression_return()
        retval.start = self.input.LT(1)
        memberExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal271 = None
        LT272 = None
        LT274 = None
        LT276 = None
        primaryExpression269 = None

        functionExpression270 = None

        memberExpression273 = None

        arguments275 = None

        memberExpressionSuffix277 = None


        string_literal271_tree = None
        LT272_tree = None
        LT274_tree = None
        LT276_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:2: ( ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )
                alt133 = 3
                LA133 = self.input.LA(1)
                if LA133 == StringLiteral or LA133 == NumericLiteral or LA133 == RegularExpressionLiteral or LA133 == Identifier or LA133 == 38 or LA133 == 41 or LA133 == 52 or LA133 == 67 or LA133 == 111 or LA133 == 112 or LA133 == 113 or LA133 == 114 or LA133 == 115 or LA133 == 116:
                    alt133 = 1
                elif LA133 == 37:
                    alt133 = 2
                elif LA133 == 66:
                    alt133 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("236:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )", 133, 0, self.input)

                    raise nvae

                if alt133 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:5: primaryExpression
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression1455)
                    primaryExpression269 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, primaryExpression269.tree)


                elif alt133 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:25: functionExpression
                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression1459)
                    functionExpression270 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression270.tree)


                elif alt133 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:46: 'new' ( LT )* memberExpression ( LT )* arguments
                    string_literal271 = self.input.LT(1)
                    self.match(self.input, 66, self.FOLLOW_66_in_memberExpression1463)
                    if self.failed:
                        return retval

                    string_literal271_tree = self.adaptor.createWithPayload(string_literal271)
                    self.adaptor.addChild(root_0, string_literal271_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:54: ( LT )*
                    while True: #loop131
                        alt131 = 2
                        LA131_0 = self.input.LA(1)

                        if (LA131_0 == LT) :
                            alt131 = 1


                        if alt131 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT272 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1465)
                            if self.failed:
                                return retval


                        else:
                            break #loop131


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression1469)
                    memberExpression273 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression273.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:76: ( LT )*
                    while True: #loop132
                        alt132 = 2
                        LA132_0 = self.input.LA(1)

                        if (LA132_0 == LT) :
                            alt132 = 1


                        if alt132 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT274 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1471)
                            if self.failed:
                                return retval


                        else:
                            break #loop132


                    self.following.append(self.FOLLOW_arguments_in_memberExpression1475)
                    arguments275 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments275.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:90: ( ( LT )* memberExpressionSuffix )*
                while True: #loop135
                    alt135 = 2
                    LA135_0 = self.input.LA(1)

                    if (LA135_0 == LT) :
                        LA135_1 = self.input.LA(2)

                        if (self.synpred158()) :
                            alt135 = 1


                    elif (LA135_0 == 67 or LA135_0 == 69) :
                        alt135 = 1


                    if alt135 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:91: ( LT )* memberExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:93: ( LT )*
                        while True: #loop134
                            alt134 = 2
                            LA134_0 = self.input.LA(1)

                            if (LA134_0 == LT) :
                                alt134 = 1


                            if alt134 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT276 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1479)
                                if self.failed:
                                    return retval


                            else:
                                break #loop134


                        self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1483)
                        memberExpressionSuffix277 = self.memberExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, memberExpressionSuffix277.tree)


                    else:
                        break #loop135





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix278 = None

        propertyReferenceSuffix279 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:2: ( indexSuffix | propertyReferenceSuffix )
                alt136 = 2
                LA136_0 = self.input.LA(1)

                if (LA136_0 == 67) :
                    alt136 = 1
                elif (LA136_0 == 69) :
                    alt136 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("239:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );", 136, 0, self.input)

                    raise nvae

                if alt136 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix1497)
                    indexSuffix278 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix278.tree)


                elif alt136 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:241:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1502)
                    propertyReferenceSuffix279 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix279.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:244:1: callExpression : memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* ;
    def callExpression(self, ):

        retval = self.callExpression_return()
        retval.start = self.input.LT(1)
        callExpression_StartIndex = self.input.index()
        root_0 = None

        LT281 = None
        LT283 = None
        memberExpression280 = None

        arguments282 = None

        callExpressionSuffix284 = None


        LT281_tree = None
        LT283_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:2: ( memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:4: memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_memberExpression_in_callExpression1513)
                memberExpression280 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, memberExpression280.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:23: ( LT )*
                while True: #loop137
                    alt137 = 2
                    LA137_0 = self.input.LA(1)

                    if (LA137_0 == LT) :
                        alt137 = 1


                    if alt137 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT281 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1515)
                        if self.failed:
                            return retval


                    else:
                        break #loop137


                self.following.append(self.FOLLOW_arguments_in_callExpression1519)
                arguments282 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, arguments282.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:36: ( ( LT )* callExpressionSuffix )*
                while True: #loop139
                    alt139 = 2
                    LA139_0 = self.input.LA(1)

                    if (LA139_0 == LT) :
                        LA139_1 = self.input.LA(2)

                        if (self.synpred162()) :
                            alt139 = 1


                    elif (LA139_0 == 38 or LA139_0 == 67 or LA139_0 == 69) :
                        alt139 = 1


                    if alt139 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:37: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:39: ( LT )*
                        while True: #loop138
                            alt138 = 2
                            LA138_0 = self.input.LA(1)

                            if (LA138_0 == LT) :
                                alt138 = 1


                            if alt138 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT283 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1522)
                                if self.failed:
                                    return retval


                            else:
                                break #loop138


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression1526)
                        callExpressionSuffix284 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, callExpressionSuffix284.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );
    def callExpressionSuffix(self, ):

        retval = self.callExpressionSuffix_return()
        retval.start = self.input.LT(1)
        callExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        arguments285 = None

        indexSuffix286 = None

        propertyReferenceSuffix287 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:2: ( arguments | indexSuffix | propertyReferenceSuffix )
                alt140 = 3
                LA140 = self.input.LA(1)
                if LA140 == 38:
                    alt140 = 1
                elif LA140 == 67:
                    alt140 = 2
                elif LA140 == 69:
                    alt140 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("248:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );", 140, 0, self.input)

                    raise nvae

                if alt140 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix1540)
                    arguments285 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments285.tree)


                elif alt140 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix1545)
                    indexSuffix286 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix286.tree)


                elif alt140 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:251:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1550)
                    propertyReferenceSuffix287 = self.propertyReferenceSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, propertyReferenceSuffix287.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:1: arguments : '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' ;
    def arguments(self, ):

        retval = self.arguments_return()
        retval.start = self.input.LT(1)
        arguments_StartIndex = self.input.index()
        root_0 = None

        char_literal288 = None
        LT289 = None
        LT291 = None
        char_literal292 = None
        LT293 = None
        LT295 = None
        char_literal296 = None
        assignmentExpression290 = None

        assignmentExpression294 = None


        char_literal288_tree = None
        LT289_tree = None
        LT291_tree = None
        char_literal292_tree = None
        LT293_tree = None
        LT295_tree = None
        char_literal296_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:2: ( '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:4: '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal288 = self.input.LT(1)
                self.match(self.input, 38, self.FOLLOW_38_in_arguments1561)
                if self.failed:
                    return retval

                char_literal288_tree = self.adaptor.createWithPayload(char_literal288)
                self.adaptor.addChild(root_0, char_literal288_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:8: ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )?
                alt145 = 2
                alt145 = self.dfa145.predict(self.input)
                if alt145 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:9: ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:11: ( LT )*
                    while True: #loop141
                        alt141 = 2
                        LA141_0 = self.input.LA(1)

                        if (LA141_0 == LT) :
                            alt141 = 1


                        if alt141 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT289 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments1564)
                            if self.failed:
                                return retval


                        else:
                            break #loop141


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments1568)
                    assignmentExpression290 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression290.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:35: ( ( LT )* ',' ( LT )* assignmentExpression )*
                    while True: #loop144
                        alt144 = 2
                        alt144 = self.dfa144.predict(self.input)
                        if alt144 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:36: ( LT )* ',' ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:38: ( LT )*
                            while True: #loop142
                                alt142 = 2
                                LA142_0 = self.input.LA(1)

                                if (LA142_0 == LT) :
                                    alt142 = 1


                                if alt142 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT291 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1571)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop142


                            char_literal292 = self.input.LT(1)
                            self.match(self.input, 39, self.FOLLOW_39_in_arguments1575)
                            if self.failed:
                                return retval

                            char_literal292_tree = self.adaptor.createWithPayload(char_literal292)
                            self.adaptor.addChild(root_0, char_literal292_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:47: ( LT )*
                            while True: #loop143
                                alt143 = 2
                                LA143_0 = self.input.LA(1)

                                if (LA143_0 == LT) :
                                    alt143 = 1


                                if alt143 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT293 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1577)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop143


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments1581)
                            assignmentExpression294 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression294.tree)


                        else:
                            break #loop144





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:77: ( LT )*
                while True: #loop146
                    alt146 = 2
                    LA146_0 = self.input.LA(1)

                    if (LA146_0 == LT) :
                        alt146 = 1


                    if alt146 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT295 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments1587)
                        if self.failed:
                            return retval


                    else:
                        break #loop146


                char_literal296 = self.input.LT(1)
                self.match(self.input, 40, self.FOLLOW_40_in_arguments1591)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' ;
    def indexSuffix(self, ):

        retval = self.indexSuffix_return()
        retval.start = self.input.LT(1)
        indexSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal297 = None
        LT298 = None
        LT300 = None
        char_literal301 = None
        expression299 = None


        char_literal297_tree = None
        LT298_tree = None
        LT300_tree = None
        char_literal301_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:2: ( '[' ( LT )* expression ( LT )* ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:4: '[' ( LT )* expression ( LT )* ']'
                root_0 = self.adaptor.nil()

                char_literal297 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_indexSuffix1603)
                if self.failed:
                    return retval

                char_literal297_tree = self.adaptor.createWithPayload(char_literal297)
                self.adaptor.addChild(root_0, char_literal297_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:10: ( LT )*
                while True: #loop147
                    alt147 = 2
                    LA147_0 = self.input.LA(1)

                    if (LA147_0 == LT) :
                        alt147 = 1


                    if alt147 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT298 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1605)
                        if self.failed:
                            return retval


                    else:
                        break #loop147


                self.following.append(self.FOLLOW_expression_in_indexSuffix1609)
                expression299 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression299.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:26: ( LT )*
                while True: #loop148
                    alt148 = 2
                    LA148_0 = self.input.LA(1)

                    if (LA148_0 == LT) :
                        alt148 = 1


                    if alt148 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT300 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1611)
                        if self.failed:
                            return retval


                    else:
                        break #loop148


                char_literal301 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_indexSuffix1615)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:262:1: propertyReferenceSuffix : '.' ( LT )* identifier ;
    def propertyReferenceSuffix(self, ):

        retval = self.propertyReferenceSuffix_return()
        retval.start = self.input.LT(1)
        propertyReferenceSuffix_StartIndex = self.input.index()
        root_0 = None

        char_literal302 = None
        LT303 = None
        identifier304 = None


        char_literal302_tree = None
        LT303_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:2: ( '.' ( LT )* identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:4: '.' ( LT )* identifier
                root_0 = self.adaptor.nil()

                char_literal302 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_propertyReferenceSuffix1628)
                if self.failed:
                    return retval

                char_literal302_tree = self.adaptor.createWithPayload(char_literal302)
                self.adaptor.addChild(root_0, char_literal302_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:263:10: ( LT )*
                while True: #loop149
                    alt149 = 2
                    LA149_0 = self.input.LA(1)

                    if (LA149_0 == LT) :
                        alt149 = 1


                    if alt149 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT303 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix1630)
                        if self.failed:
                            return retval


                    else:
                        break #loop149


                self.following.append(self.FOLLOW_identifier_in_propertyReferenceSuffix1634)
                identifier304 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier304.tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:266:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set305 = None

        set305_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:267:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set305 = self.input.LT(1)
                if self.input.LA(1) == 46 or (70 <= self.input.LA(1) <= 80):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set305))
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
    def conditionalExpression(self, ):

        retval = self.conditionalExpression_return()
        retval.start = self.input.LT(1)
        conditionalExpression_StartIndex = self.input.index()
        root_0 = None

        LT307 = None
        char_literal308 = None
        LT309 = None
        LT311 = None
        char_literal312 = None
        LT313 = None
        logicalORExpression306 = None

        assignmentExpression310 = None

        assignmentExpression314 = None


        LT307_tree = None
        char_literal308_tree = None
        LT309_tree = None
        LT311_tree = None
        char_literal312_tree = None
        LT313_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression1701)
                logicalORExpression306 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression306.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt154 = 2
                alt154 = self.dfa154.predict(self.input)
                if alt154 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:27: ( LT )*
                    while True: #loop150
                        alt150 = 2
                        LA150_0 = self.input.LA(1)

                        if (LA150_0 == LT) :
                            alt150 = 1


                        if alt150 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT307 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1704)
                            if self.failed:
                                return retval


                        else:
                            break #loop150


                    char_literal308 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_conditionalExpression1708)
                    if self.failed:
                        return retval

                    char_literal308_tree = self.adaptor.createWithPayload(char_literal308)
                    self.adaptor.addChild(root_0, char_literal308_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:36: ( LT )*
                    while True: #loop151
                        alt151 = 2
                        LA151_0 = self.input.LA(1)

                        if (LA151_0 == LT) :
                            alt151 = 1


                        if alt151 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT309 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1710)
                            if self.failed:
                                return retval


                        else:
                            break #loop151


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1714)
                    assignmentExpression310 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression310.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:62: ( LT )*
                    while True: #loop152
                        alt152 = 2
                        LA152_0 = self.input.LA(1)

                        if (LA152_0 == LT) :
                            alt152 = 1


                        if alt152 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT311 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1716)
                            if self.failed:
                                return retval


                        else:
                            break #loop152


                    char_literal312 = self.input.LT(1)
                    self.match(self.input, 58, self.FOLLOW_58_in_conditionalExpression1720)
                    if self.failed:
                        return retval

                    char_literal312_tree = self.adaptor.createWithPayload(char_literal312)
                    self.adaptor.addChild(root_0, char_literal312_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:271:71: ( LT )*
                    while True: #loop153
                        alt153 = 2
                        LA153_0 = self.input.LA(1)

                        if (LA153_0 == LT) :
                            alt153 = 1


                        if alt153 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT313 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1722)
                            if self.failed:
                                return retval


                        else:
                            break #loop153


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1726)
                    assignmentExpression314 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression314.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
    def conditionalExpressionNoIn(self, ):

        retval = self.conditionalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        conditionalExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT316 = None
        char_literal317 = None
        LT318 = None
        LT320 = None
        char_literal321 = None
        LT322 = None
        logicalORExpressionNoIn315 = None

        assignmentExpressionNoIn319 = None

        assignmentExpressionNoIn323 = None


        LT316_tree = None
        char_literal317_tree = None
        LT318_tree = None
        LT320_tree = None
        char_literal321_tree = None
        LT322_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1739)
                logicalORExpressionNoIn315 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn315.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt159 = 2
                alt159 = self.dfa159.predict(self.input)
                if alt159 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:31: ( LT )*
                    while True: #loop155
                        alt155 = 2
                        LA155_0 = self.input.LA(1)

                        if (LA155_0 == LT) :
                            alt155 = 1


                        if alt155 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT316 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1742)
                            if self.failed:
                                return retval


                        else:
                            break #loop155


                    char_literal317 = self.input.LT(1)
                    self.match(self.input, 81, self.FOLLOW_81_in_conditionalExpressionNoIn1746)
                    if self.failed:
                        return retval

                    char_literal317_tree = self.adaptor.createWithPayload(char_literal317)
                    self.adaptor.addChild(root_0, char_literal317_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:40: ( LT )*
                    while True: #loop156
                        alt156 = 2
                        LA156_0 = self.input.LA(1)

                        if (LA156_0 == LT) :
                            alt156 = 1


                        if alt156 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT318 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1748)
                            if self.failed:
                                return retval


                        else:
                            break #loop156


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1752)
                    assignmentExpressionNoIn319 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn319.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:70: ( LT )*
                    while True: #loop157
                        alt157 = 2
                        LA157_0 = self.input.LA(1)

                        if (LA157_0 == LT) :
                            alt157 = 1


                        if alt157 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT320 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1754)
                            if self.failed:
                                return retval


                        else:
                            break #loop157


                    char_literal321 = self.input.LT(1)
                    self.match(self.input, 58, self.FOLLOW_58_in_conditionalExpressionNoIn1758)
                    if self.failed:
                        return retval

                    char_literal321_tree = self.adaptor.createWithPayload(char_literal321)
                    self.adaptor.addChild(root_0, char_literal321_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:79: ( LT )*
                    while True: #loop158
                        alt158 = 2
                        LA158_0 = self.input.LA(1)

                        if (LA158_0 == LT) :
                            alt158 = 1


                        if alt158 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT322 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1760)
                            if self.failed:
                                return retval


                        else:
                            break #loop158


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1764)
                    assignmentExpressionNoIn323 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn323.tree)






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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
    def logicalORExpression(self, ):

        retval = self.logicalORExpression_return()
        retval.start = self.input.LT(1)
        logicalORExpression_StartIndex = self.input.index()
        root_0 = None

        LT325 = None
        string_literal326 = None
        LT327 = None
        logicalANDExpression324 = None

        logicalANDExpression328 = None


        LT325_tree = None
        string_literal326_tree = None
        LT327_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1777)
                logicalANDExpression324 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression324.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop162
                    alt162 = 2
                    alt162 = self.dfa162.predict(self.input)
                    if alt162 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:28: ( LT )*
                        while True: #loop160
                            alt160 = 2
                            LA160_0 = self.input.LA(1)

                            if (LA160_0 == LT) :
                                alt160 = 1


                            if alt160 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT325 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1780)
                                if self.failed:
                                    return retval


                            else:
                                break #loop160


                        string_literal326 = self.input.LT(1)
                        self.match(self.input, 82, self.FOLLOW_82_in_logicalORExpression1784)
                        if self.failed:
                            return retval

                        string_literal326_tree = self.adaptor.createWithPayload(string_literal326)
                        self.adaptor.addChild(root_0, string_literal326_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:38: ( LT )*
                        while True: #loop161
                            alt161 = 2
                            LA161_0 = self.input.LA(1)

                            if (LA161_0 == LT) :
                                alt161 = 1


                            if alt161 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT327 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1786)
                                if self.failed:
                                    return retval


                            else:
                                break #loop161


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1790)
                        logicalANDExpression328 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression328.tree)


                    else:
                        break #loop162





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
    def logicalORExpressionNoIn(self, ):

        retval = self.logicalORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT330 = None
        string_literal331 = None
        LT332 = None
        logicalANDExpressionNoIn329 = None

        logicalANDExpressionNoIn333 = None


        LT330_tree = None
        string_literal331_tree = None
        LT332_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1804)
                logicalANDExpressionNoIn329 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn329.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop165
                    alt165 = 2
                    alt165 = self.dfa165.predict(self.input)
                    if alt165 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:32: ( LT )*
                        while True: #loop163
                            alt163 = 2
                            LA163_0 = self.input.LA(1)

                            if (LA163_0 == LT) :
                                alt163 = 1


                            if alt163 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT330 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1807)
                                if self.failed:
                                    return retval


                            else:
                                break #loop163


                        string_literal331 = self.input.LT(1)
                        self.match(self.input, 82, self.FOLLOW_82_in_logicalORExpressionNoIn1811)
                        if self.failed:
                            return retval

                        string_literal331_tree = self.adaptor.createWithPayload(string_literal331)
                        self.adaptor.addChild(root_0, string_literal331_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:42: ( LT )*
                        while True: #loop164
                            alt164 = 2
                            LA164_0 = self.input.LA(1)

                            if (LA164_0 == LT) :
                                alt164 = 1


                            if alt164 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT332 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1813)
                                if self.failed:
                                    return retval


                            else:
                                break #loop164


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1817)
                        logicalANDExpressionNoIn333 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn333.tree)


                    else:
                        break #loop165





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
    def logicalANDExpression(self, ):

        retval = self.logicalANDExpression_return()
        retval.start = self.input.LT(1)
        logicalANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT335 = None
        string_literal336 = None
        LT337 = None
        bitwiseORExpression334 = None

        bitwiseORExpression338 = None


        LT335_tree = None
        string_literal336_tree = None
        LT337_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1831)
                bitwiseORExpression334 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression334.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop168
                    alt168 = 2
                    alt168 = self.dfa168.predict(self.input)
                    if alt168 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:27: ( LT )*
                        while True: #loop166
                            alt166 = 2
                            LA166_0 = self.input.LA(1)

                            if (LA166_0 == LT) :
                                alt166 = 1


                            if alt166 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT335 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1834)
                                if self.failed:
                                    return retval


                            else:
                                break #loop166


                        string_literal336 = self.input.LT(1)
                        self.match(self.input, 83, self.FOLLOW_83_in_logicalANDExpression1838)
                        if self.failed:
                            return retval

                        string_literal336_tree = self.adaptor.createWithPayload(string_literal336)
                        self.adaptor.addChild(root_0, string_literal336_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:37: ( LT )*
                        while True: #loop167
                            alt167 = 2
                            LA167_0 = self.input.LA(1)

                            if (LA167_0 == LT) :
                                alt167 = 1


                            if alt167 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT337 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1840)
                                if self.failed:
                                    return retval


                            else:
                                break #loop167


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1844)
                        bitwiseORExpression338 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression338.tree)


                    else:
                        break #loop168





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
    def logicalANDExpressionNoIn(self, ):

        retval = self.logicalANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        logicalANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT340 = None
        string_literal341 = None
        LT342 = None
        bitwiseORExpressionNoIn339 = None

        bitwiseORExpressionNoIn343 = None


        LT340_tree = None
        string_literal341_tree = None
        LT342_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1858)
                bitwiseORExpressionNoIn339 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn339.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop171
                    alt171 = 2
                    alt171 = self.dfa171.predict(self.input)
                    if alt171 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:31: ( LT )*
                        while True: #loop169
                            alt169 = 2
                            LA169_0 = self.input.LA(1)

                            if (LA169_0 == LT) :
                                alt169 = 1


                            if alt169 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT340 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1861)
                                if self.failed:
                                    return retval


                            else:
                                break #loop169


                        string_literal341 = self.input.LT(1)
                        self.match(self.input, 83, self.FOLLOW_83_in_logicalANDExpressionNoIn1865)
                        if self.failed:
                            return retval

                        string_literal341_tree = self.adaptor.createWithPayload(string_literal341)
                        self.adaptor.addChild(root_0, string_literal341_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:41: ( LT )*
                        while True: #loop170
                            alt170 = 2
                            LA170_0 = self.input.LA(1)

                            if (LA170_0 == LT) :
                                alt170 = 1


                            if alt170 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT342 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1867)
                                if self.failed:
                                    return retval


                            else:
                                break #loop170


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1871)
                        bitwiseORExpressionNoIn343 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn343.tree)


                    else:
                        break #loop171





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
    def bitwiseORExpression(self, ):

        retval = self.bitwiseORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseORExpression_StartIndex = self.input.index()
        root_0 = None

        LT345 = None
        char_literal346 = None
        LT347 = None
        bitwiseXORExpression344 = None

        bitwiseXORExpression348 = None


        LT345_tree = None
        char_literal346_tree = None
        LT347_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1885)
                bitwiseXORExpression344 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression344.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop174
                    alt174 = 2
                    alt174 = self.dfa174.predict(self.input)
                    if alt174 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:28: ( LT )*
                        while True: #loop172
                            alt172 = 2
                            LA172_0 = self.input.LA(1)

                            if (LA172_0 == LT) :
                                alt172 = 1


                            if alt172 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT345 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression1888)
                                if self.failed:
                                    return retval


                            else:
                                break #loop172


                        char_literal346 = self.input.LT(1)
                        self.match(self.input, 84, self.FOLLOW_84_in_bitwiseORExpression1892)
                        if self.failed:
                            return retval

                        char_literal346_tree = self.adaptor.createWithPayload(char_literal346)
                        self.adaptor.addChild(root_0, char_literal346_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:37: ( LT )*
                        while True: #loop173
                            alt173 = 2
                            LA173_0 = self.input.LA(1)

                            if (LA173_0 == LT) :
                                alt173 = 1


                            if alt173 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT347 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression1894)
                                if self.failed:
                                    return retval


                            else:
                                break #loop173


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1898)
                        bitwiseXORExpression348 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression348.tree)


                    else:
                        break #loop174





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
    def bitwiseORExpressionNoIn(self, ):

        retval = self.bitwiseORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT350 = None
        char_literal351 = None
        LT352 = None
        bitwiseXORExpressionNoIn349 = None

        bitwiseXORExpressionNoIn353 = None


        LT350_tree = None
        char_literal351_tree = None
        LT352_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1912)
                bitwiseXORExpressionNoIn349 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn349.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop177
                    alt177 = 2
                    alt177 = self.dfa177.predict(self.input)
                    if alt177 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:32: ( LT )*
                        while True: #loop175
                            alt175 = 2
                            LA175_0 = self.input.LA(1)

                            if (LA175_0 == LT) :
                                alt175 = 1


                            if alt175 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT350 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn1915)
                                if self.failed:
                                    return retval


                            else:
                                break #loop175


                        char_literal351 = self.input.LT(1)
                        self.match(self.input, 84, self.FOLLOW_84_in_bitwiseORExpressionNoIn1919)
                        if self.failed:
                            return retval

                        char_literal351_tree = self.adaptor.createWithPayload(char_literal351)
                        self.adaptor.addChild(root_0, char_literal351_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:41: ( LT )*
                        while True: #loop176
                            alt176 = 2
                            LA176_0 = self.input.LA(1)

                            if (LA176_0 == LT) :
                                alt176 = 1


                            if alt176 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT352 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn1921)
                                if self.failed:
                                    return retval


                            else:
                                break #loop176


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1925)
                        bitwiseXORExpressionNoIn353 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn353.tree)


                    else:
                        break #loop177





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
    def bitwiseXORExpression(self, ):

        retval = self.bitwiseXORExpression_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpression_StartIndex = self.input.index()
        root_0 = None

        LT355 = None
        char_literal356 = None
        LT357 = None
        bitwiseANDExpression354 = None

        bitwiseANDExpression358 = None


        LT355_tree = None
        char_literal356_tree = None
        LT357_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1939)
                bitwiseANDExpression354 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression354.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop180
                    alt180 = 2
                    alt180 = self.dfa180.predict(self.input)
                    if alt180 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:28: ( LT )*
                        while True: #loop178
                            alt178 = 2
                            LA178_0 = self.input.LA(1)

                            if (LA178_0 == LT) :
                                alt178 = 1


                            if alt178 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT355 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression1942)
                                if self.failed:
                                    return retval


                            else:
                                break #loop178


                        char_literal356 = self.input.LT(1)
                        self.match(self.input, 85, self.FOLLOW_85_in_bitwiseXORExpression1946)
                        if self.failed:
                            return retval

                        char_literal356_tree = self.adaptor.createWithPayload(char_literal356)
                        self.adaptor.addChild(root_0, char_literal356_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:37: ( LT )*
                        while True: #loop179
                            alt179 = 2
                            LA179_0 = self.input.LA(1)

                            if (LA179_0 == LT) :
                                alt179 = 1


                            if alt179 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT357 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression1948)
                                if self.failed:
                                    return retval


                            else:
                                break #loop179


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1952)
                        bitwiseANDExpression358 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression358.tree)


                    else:
                        break #loop180





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
    def bitwiseXORExpressionNoIn(self, ):

        retval = self.bitwiseXORExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseXORExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT360 = None
        char_literal361 = None
        LT362 = None
        bitwiseANDExpressionNoIn359 = None

        bitwiseANDExpressionNoIn363 = None


        LT360_tree = None
        char_literal361_tree = None
        LT362_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1966)
                bitwiseANDExpressionNoIn359 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn359.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop183
                    alt183 = 2
                    alt183 = self.dfa183.predict(self.input)
                    if alt183 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:32: ( LT )*
                        while True: #loop181
                            alt181 = 2
                            LA181_0 = self.input.LA(1)

                            if (LA181_0 == LT) :
                                alt181 = 1


                            if alt181 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT360 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn1969)
                                if self.failed:
                                    return retval


                            else:
                                break #loop181


                        char_literal361 = self.input.LT(1)
                        self.match(self.input, 85, self.FOLLOW_85_in_bitwiseXORExpressionNoIn1973)
                        if self.failed:
                            return retval

                        char_literal361_tree = self.adaptor.createWithPayload(char_literal361)
                        self.adaptor.addChild(root_0, char_literal361_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:41: ( LT )*
                        while True: #loop182
                            alt182 = 2
                            LA182_0 = self.input.LA(1)

                            if (LA182_0 == LT) :
                                alt182 = 1


                            if alt182 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT362 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn1975)
                                if self.failed:
                                    return retval


                            else:
                                break #loop182


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1979)
                        bitwiseANDExpressionNoIn363 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn363.tree)


                    else:
                        break #loop183





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
    def bitwiseANDExpression(self, ):

        retval = self.bitwiseANDExpression_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpression_StartIndex = self.input.index()
        root_0 = None

        LT365 = None
        char_literal366 = None
        LT367 = None
        equalityExpression364 = None

        equalityExpression368 = None


        LT365_tree = None
        char_literal366_tree = None
        LT367_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression1993)
                equalityExpression364 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression364.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop186
                    alt186 = 2
                    alt186 = self.dfa186.predict(self.input)
                    if alt186 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:26: ( LT )*
                        while True: #loop184
                            alt184 = 2
                            LA184_0 = self.input.LA(1)

                            if (LA184_0 == LT) :
                                alt184 = 1


                            if alt184 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT365 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression1996)
                                if self.failed:
                                    return retval


                            else:
                                break #loop184


                        char_literal366 = self.input.LT(1)
                        self.match(self.input, 86, self.FOLLOW_86_in_bitwiseANDExpression2000)
                        if self.failed:
                            return retval

                        char_literal366_tree = self.adaptor.createWithPayload(char_literal366)
                        self.adaptor.addChild(root_0, char_literal366_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:35: ( LT )*
                        while True: #loop185
                            alt185 = 2
                            LA185_0 = self.input.LA(1)

                            if (LA185_0 == LT) :
                                alt185 = 1


                            if alt185 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT367 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2002)
                                if self.failed:
                                    return retval


                            else:
                                break #loop185


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2006)
                        equalityExpression368 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression368.tree)


                    else:
                        break #loop186





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
    def bitwiseANDExpressionNoIn(self, ):

        retval = self.bitwiseANDExpressionNoIn_return()
        retval.start = self.input.LT(1)
        bitwiseANDExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT370 = None
        char_literal371 = None
        LT372 = None
        equalityExpressionNoIn369 = None

        equalityExpressionNoIn373 = None


        LT370_tree = None
        char_literal371_tree = None
        LT372_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2020)
                equalityExpressionNoIn369 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn369.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop189
                    alt189 = 2
                    alt189 = self.dfa189.predict(self.input)
                    if alt189 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:30: ( LT )*
                        while True: #loop187
                            alt187 = 2
                            LA187_0 = self.input.LA(1)

                            if (LA187_0 == LT) :
                                alt187 = 1


                            if alt187 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT370 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2023)
                                if self.failed:
                                    return retval


                            else:
                                break #loop187


                        char_literal371 = self.input.LT(1)
                        self.match(self.input, 86, self.FOLLOW_86_in_bitwiseANDExpressionNoIn2027)
                        if self.failed:
                            return retval

                        char_literal371_tree = self.adaptor.createWithPayload(char_literal371)
                        self.adaptor.addChild(root_0, char_literal371_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:39: ( LT )*
                        while True: #loop188
                            alt188 = 2
                            LA188_0 = self.input.LA(1)

                            if (LA188_0 == LT) :
                                alt188 = 1


                            if alt188 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT372 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2029)
                                if self.failed:
                                    return retval


                            else:
                                break #loop188


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2033)
                        equalityExpressionNoIn373 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn373.tree)


                    else:
                        break #loop189





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
    def equalityExpression(self, ):

        retval = self.equalityExpression_return()
        retval.start = self.input.LT(1)
        equalityExpression_StartIndex = self.input.index()
        root_0 = None

        LT375 = None
        set376 = None
        LT377 = None
        relationalExpression374 = None

        relationalExpression378 = None


        LT375_tree = None
        set376_tree = None
        LT377_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2047)
                relationalExpression374 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression374.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop192
                    alt192 = 2
                    alt192 = self.dfa192.predict(self.input)
                    if alt192 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:28: ( LT )*
                        while True: #loop190
                            alt190 = 2
                            LA190_0 = self.input.LA(1)

                            if (LA190_0 == LT) :
                                alt190 = 1


                            if alt190 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT375 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2050)
                                if self.failed:
                                    return retval


                            else:
                                break #loop190


                        set376 = self.input.LT(1)
                        if (87 <= self.input.LA(1) <= 90):
                            self.input.consume();
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set376))
                            self.errorRecovery = False
                            self.failed = False

                        else:
                            if self.backtracking > 0:
                                self.failed = True
                                return retval

                            mse = MismatchedSetException(None, self.input)
                            self.recoverFromMismatchedSet(
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2054
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:63: ( LT )*
                        while True: #loop191
                            alt191 = 2
                            LA191_0 = self.input.LA(1)

                            if (LA191_0 == LT) :
                                alt191 = 1


                            if alt191 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT377 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2070)
                                if self.failed:
                                    return retval


                            else:
                                break #loop191


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2074)
                        relationalExpression378 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression378.tree)


                    else:
                        break #loop192





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
    def equalityExpressionNoIn(self, ):

        retval = self.equalityExpressionNoIn_return()
        retval.start = self.input.LT(1)
        equalityExpressionNoIn_StartIndex = self.input.index()
        root_0 = None

        LT380 = None
        set381 = None
        LT382 = None
        relationalExpressionNoIn379 = None

        relationalExpressionNoIn383 = None


        LT380_tree = None
        set381_tree = None
        LT382_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2087)
                relationalExpressionNoIn379 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn379.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop195
                    alt195 = 2
                    alt195 = self.dfa195.predict(self.input)
                    if alt195 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:32: ( LT )*
                        while True: #loop193
                            alt193 = 2
                            LA193_0 = self.input.LA(1)

                            if (LA193_0 == LT) :
                                alt193 = 1


                            if alt193 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT380 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2090)
                                if self.failed:
                                    return retval


                            else:
                                break #loop193


                        set381 = self.input.LT(1)
                        if (87 <= self.input.LA(1) <= 90):
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
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn2094
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:67: ( LT )*
                        while True: #loop194
                            alt194 = 2
                            LA194_0 = self.input.LA(1)

                            if (LA194_0 == LT) :
                                alt194 = 1


                            if alt194 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT382 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2110)
                                if self.failed:
                                    return retval


                            else:
                                break #loop194


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2114)
                        relationalExpressionNoIn383 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn383.tree)


                    else:
                        break #loop195





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
    def relationalExpression(self, ):

        retval = self.relationalExpression_return()
        retval.start = self.input.LT(1)
        relationalExpression_StartIndex = self.input.index()
        root_0 = None

        LT385 = None
        set386 = None
        LT387 = None
        shiftExpression384 = None

        shiftExpression388 = None


        LT385_tree = None
        set386_tree = None
        LT387_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2128)
                shiftExpression384 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression384.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop198
                    alt198 = 2
                    alt198 = self.dfa198.predict(self.input)
                    if alt198 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:23: ( LT )*
                        while True: #loop196
                            alt196 = 2
                            LA196_0 = self.input.LA(1)

                            if (LA196_0 == LT) :
                                alt196 = 1


                            if alt196 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT385 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2131)
                                if self.failed:
                                    return retval


                            else:
                                break #loop196


                        set386 = self.input.LT(1)
                        if self.input.LA(1) == 53 or (91 <= self.input.LA(1) <= 95):
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
                                self.input, mse, self.FOLLOW_set_in_relationalExpression2135
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:76: ( LT )*
                        while True: #loop197
                            alt197 = 2
                            LA197_0 = self.input.LA(1)

                            if (LA197_0 == LT) :
                                alt197 = 1


                            if alt197 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT387 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2159)
                                if self.failed:
                                    return retval


                            else:
                                break #loop197


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2163)
                        shiftExpression388 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression388.tree)


                    else:
                        break #loop198





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
    def relationalExpressionNoIn(self, ):

        retval = self.relationalExpressionNoIn_return()
        retval.start = self.input.LT(1)
        relationalExpressionNoIn_StartIndex = self.input.index()
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2176)
                shiftExpression389 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression389.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop201
                    alt201 = 2
                    alt201 = self.dfa201.predict(self.input)
                    if alt201 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:23: ( LT )*
                        while True: #loop199
                            alt199 = 2
                            LA199_0 = self.input.LA(1)

                            if (LA199_0 == LT) :
                                alt199 = 1


                            if alt199 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT390 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2179)
                                if self.failed:
                                    return retval


                            else:
                                break #loop199


                        set391 = self.input.LT(1)
                        if (91 <= self.input.LA(1) <= 95):
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
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn2183
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:69: ( LT )*
                        while True: #loop200
                            alt200 = 2
                            LA200_0 = self.input.LA(1)

                            if (LA200_0 == LT) :
                                alt200 = 1


                            if alt200 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT392 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2203)
                                if self.failed:
                                    return retval


                            else:
                                break #loop200


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2207)
                        shiftExpression393 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression393.tree)


                    else:
                        break #loop201





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
    def shiftExpression(self, ):

        retval = self.shiftExpression_return()
        retval.start = self.input.LT(1)
        shiftExpression_StartIndex = self.input.index()
        root_0 = None

        LT395 = None
        set396 = None
        LT397 = None
        additiveExpression394 = None

        additiveExpression398 = None


        LT395_tree = None
        set396_tree = None
        LT397_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2220)
                additiveExpression394 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression394.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop204
                    alt204 = 2
                    alt204 = self.dfa204.predict(self.input)
                    if alt204 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:26: ( LT )*
                        while True: #loop202
                            alt202 = 2
                            LA202_0 = self.input.LA(1)

                            if (LA202_0 == LT) :
                                alt202 = 1


                            if alt202 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT395 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2223)
                                if self.failed:
                                    return retval


                            else:
                                break #loop202


                        set396 = self.input.LT(1)
                        if (96 <= self.input.LA(1) <= 98):
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
                                self.input, mse, self.FOLLOW_set_in_shiftExpression2227
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:53: ( LT )*
                        while True: #loop203
                            alt203 = 2
                            LA203_0 = self.input.LA(1)

                            if (LA203_0 == LT) :
                                alt203 = 1


                            if alt203 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT397 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2239)
                                if self.failed:
                                    return retval


                            else:
                                break #loop203


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2243)
                        additiveExpression398 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression398.tree)


                    else:
                        break #loop204





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
    def additiveExpression(self, ):

        retval = self.additiveExpression_return()
        retval.start = self.input.LT(1)
        additiveExpression_StartIndex = self.input.index()
        root_0 = None

        LT400 = None
        set401 = None
        LT402 = None
        multiplicativeExpression399 = None

        multiplicativeExpression403 = None


        LT400_tree = None
        set401_tree = None
        LT402_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2256)
                multiplicativeExpression399 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression399.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop207
                    alt207 = 2
                    LA207_0 = self.input.LA(1)

                    if (LA207_0 == LT) :
                        LA207_1 = self.input.LA(2)

                        if (self.synpred260()) :
                            alt207 = 1


                    elif ((99 <= LA207_0 <= 100)) :
                        alt207 = 1


                    if alt207 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:32: ( LT )*
                        while True: #loop205
                            alt205 = 2
                            LA205_0 = self.input.LA(1)

                            if (LA205_0 == LT) :
                                alt205 = 1


                            if alt205 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT400 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2259)
                                if self.failed:
                                    return retval


                            else:
                                break #loop205


                        set401 = self.input.LT(1)
                        if (99 <= self.input.LA(1) <= 100):
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
                                self.input, mse, self.FOLLOW_set_in_additiveExpression2263
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:49: ( LT )*
                        while True: #loop206
                            alt206 = 2
                            LA206_0 = self.input.LA(1)

                            if (LA206_0 == LT) :
                                alt206 = 1


                            if alt206 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT402 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2271)
                                if self.failed:
                                    return retval


                            else:
                                break #loop206


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2275)
                        multiplicativeExpression403 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression403.tree)


                    else:
                        break #loop207





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
    def multiplicativeExpression(self, ):

        retval = self.multiplicativeExpression_return()
        retval.start = self.input.LT(1)
        multiplicativeExpression_StartIndex = self.input.index()
        root_0 = None

        LT405 = None
        set406 = None
        LT407 = None
        unaryExpression404 = None

        unaryExpression408 = None


        LT405_tree = None
        set406_tree = None
        LT407_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2288)
                unaryExpression404 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression404.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop210
                    alt210 = 2
                    alt210 = self.dfa210.predict(self.input)
                    if alt210 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:23: ( LT )*
                        while True: #loop208
                            alt208 = 2
                            LA208_0 = self.input.LA(1)

                            if (LA208_0 == LT) :
                                alt208 = 1


                            if alt208 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT405 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2291)
                                if self.failed:
                                    return retval


                            else:
                                break #loop208


                        set406 = self.input.LT(1)
                        if (101 <= self.input.LA(1) <= 103):
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
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression2295
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:46: ( LT )*
                        while True: #loop209
                            alt209 = 2
                            LA209_0 = self.input.LA(1)

                            if (LA209_0 == LT) :
                                alt209 = 1


                            if alt209 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT407 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2307)
                                if self.failed:
                                    return retval


                            else:
                                break #loop209


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2311)
                        unaryExpression408 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression408.tree)


                    else:
                        break #loop210





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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
    def unaryExpression(self, ):

        retval = self.unaryExpression_return()
        retval.start = self.input.LT(1)
        unaryExpression_StartIndex = self.input.index()
        root_0 = None

        set410 = None
        postfixExpression409 = None

        unaryExpression411 = None


        set410_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt211 = 2
                LA211_0 = self.input.LA(1)

                if ((StringLiteral <= LA211_0 <= Identifier) or (37 <= LA211_0 <= 38) or LA211_0 == 41 or LA211_0 == 52 or (66 <= LA211_0 <= 67) or (111 <= LA211_0 <= 116)) :
                    alt211 = 1
                elif ((99 <= LA211_0 <= 100) or (104 <= LA211_0 <= 110)) :
                    alt211 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("346:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 211, 0, self.input)

                    raise nvae

                if alt211 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression2324)
                    postfixExpression409 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression409.tree)


                elif alt211 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:348:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set410 = self.input.LT(1)
                    if (99 <= self.input.LA(1) <= 100) or (104 <= self.input.LA(1) <= 110):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set410))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_unaryExpression2329
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression2365)
                    unaryExpression411 = self.unaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, unaryExpression411.tree)


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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
    def postfixExpression(self, ):

        retval = self.postfixExpression_return()
        retval.start = self.input.LT(1)
        postfixExpression_StartIndex = self.input.index()
        root_0 = None

        set413 = None
        leftHandSideExpression412 = None


        set413_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:352:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:352:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression2377)
                leftHandSideExpression412 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression412.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:352:27: ( '++' | '--' )?
                alt212 = 2
                LA212_0 = self.input.LA(1)

                if ((107 <= LA212_0 <= 108)) :
                    alt212 = 1
                if alt212 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set413 = self.input.LT(1)
                    if (107 <= self.input.LA(1) <= 108):
                        self.input.consume();
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set413))
                        self.errorRecovery = False
                        self.failed = False

                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        mse = MismatchedSetException(None, self.input)
                        self.recoverFromMismatchedSet(
                            self.input, mse, self.FOLLOW_set_in_postfixExpression2379
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
    def primaryExpression(self, ):

        retval = self.primaryExpression_return()
        retval.start = self.input.LT(1)
        primaryExpression_StartIndex = self.input.index()
        root_0 = None

        string_literal414 = None
        char_literal419 = None
        LT420 = None
        LT422 = None
        char_literal423 = None
        identifier415 = None

        literal416 = None

        arrayLiteral417 = None

        objectLiteral418 = None

        expression421 = None


        string_literal414_tree = None
        char_literal419_tree = None
        LT420_tree = None
        LT422_tree = None
        char_literal423_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:356:2: ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt215 = 6
                LA215 = self.input.LA(1)
                if LA215 == 111:
                    alt215 = 1
                elif LA215 == Identifier or LA215 == 52 or LA215 == 112 or LA215 == 113:
                    alt215 = 2
                elif LA215 == StringLiteral or LA215 == NumericLiteral or LA215 == RegularExpressionLiteral or LA215 == 114 or LA215 == 115 or LA215 == 116:
                    alt215 = 3
                elif LA215 == 67:
                    alt215 = 4
                elif LA215 == 41:
                    alt215 = 5
                elif LA215 == 38:
                    alt215 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("355:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 215, 0, self.input)

                    raise nvae

                if alt215 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:356:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal414 = self.input.LT(1)
                    self.match(self.input, 111, self.FOLLOW_111_in_primaryExpression2397)
                    if self.failed:
                        return retval

                    string_literal414_tree = self.adaptor.createWithPayload(string_literal414)
                    self.adaptor.addChild(root_0, string_literal414_tree)



                elif alt215 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:357:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_primaryExpression2402)
                    identifier415 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier415.tree)


                elif alt215 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression2407)
                    literal416 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal416.tree)


                elif alt215 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression2412)
                    arrayLiteral417 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral417.tree)


                elif alt215 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:360:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression2417)
                    objectLiteral418 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral418.tree)


                elif alt215 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:361:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal419 = self.input.LT(1)
                    self.match(self.input, 38, self.FOLLOW_38_in_primaryExpression2422)
                    if self.failed:
                        return retval

                    char_literal419_tree = self.adaptor.createWithPayload(char_literal419)
                    self.adaptor.addChild(root_0, char_literal419_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:361:10: ( LT )*
                    while True: #loop213
                        alt213 = 2
                        LA213_0 = self.input.LA(1)

                        if (LA213_0 == LT) :
                            alt213 = 1


                        if alt213 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT420 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2424)
                            if self.failed:
                                return retval


                        else:
                            break #loop213


                    self.following.append(self.FOLLOW_expression_in_primaryExpression2428)
                    expression421 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression421.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:361:26: ( LT )*
                    while True: #loop214
                        alt214 = 2
                        LA214_0 = self.input.LA(1)

                        if (LA214_0 == LT) :
                            alt214 = 1


                        if alt214 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT422 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2430)
                            if self.failed:
                                return retval


                        else:
                            break #loop214


                    char_literal423 = self.input.LT(1)
                    self.match(self.input, 40, self.FOLLOW_40_in_primaryExpression2434)
                    if self.failed:
                        return retval

                    char_literal423_tree = self.adaptor.createWithPayload(char_literal423)
                    self.adaptor.addChild(root_0, char_literal423_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:365:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' ;
    def arrayLiteral(self, ):

        retval = self.arrayLiteral_return()
        retval.start = self.input.LT(1)
        arrayLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal424 = None
        LT425 = None
        LT427 = None
        char_literal428 = None
        LT429 = None
        LT431 = None
        char_literal432 = None
        assignmentExpression426 = None

        assignmentExpression430 = None


        char_literal424_tree = None
        LT425_tree = None
        LT427_tree = None
        char_literal428_tree = None
        LT429_tree = None
        LT431_tree = None
        char_literal432_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']'
                root_0 = self.adaptor.nil()

                char_literal424 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_arrayLiteral2447)
                if self.failed:
                    return retval

                char_literal424_tree = self.adaptor.createWithPayload(char_literal424)
                self.adaptor.addChild(root_0, char_literal424_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:10: ( LT )*
                while True: #loop216
                    alt216 = 2
                    LA216_0 = self.input.LA(1)

                    if (LA216_0 == LT) :
                        LA216_2 = self.input.LA(2)

                        if (self.synpred284()) :
                            alt216 = 1




                    if alt216 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT425 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2449)
                        if self.failed:
                            return retval


                    else:
                        break #loop216


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:13: ( assignmentExpression )?
                alt217 = 2
                LA217_0 = self.input.LA(1)

                if ((StringLiteral <= LA217_0 <= Identifier) or (37 <= LA217_0 <= 38) or LA217_0 == 41 or LA217_0 == 52 or (66 <= LA217_0 <= 67) or (99 <= LA217_0 <= 100) or (104 <= LA217_0 <= 116)) :
                    alt217 = 1
                if alt217 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2453)
                    assignmentExpression426 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression426.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop221
                    alt221 = 2
                    alt221 = self.dfa221.predict(self.input)
                    if alt221 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:36: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:38: ( LT )*
                        while True: #loop218
                            alt218 = 2
                            LA218_0 = self.input.LA(1)

                            if (LA218_0 == LT) :
                                alt218 = 1


                            if alt218 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT427 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2457)
                                if self.failed:
                                    return retval


                            else:
                                break #loop218


                        char_literal428 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_arrayLiteral2461)
                        if self.failed:
                            return retval

                        char_literal428_tree = self.adaptor.createWithPayload(char_literal428)
                        self.adaptor.addChild(root_0, char_literal428_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:45: ( ( LT )* assignmentExpression )?
                        alt220 = 2
                        alt220 = self.dfa220.predict(self.input)
                        if alt220 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:46: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:48: ( LT )*
                            while True: #loop219
                                alt219 = 2
                                LA219_0 = self.input.LA(1)

                                if (LA219_0 == LT) :
                                    alt219 = 1


                                if alt219 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT429 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2464)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop219


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2468)
                            assignmentExpression430 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression430.tree)





                    else:
                        break #loop221


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:78: ( LT )*
                while True: #loop222
                    alt222 = 2
                    LA222_0 = self.input.LA(1)

                    if (LA222_0 == LT) :
                        alt222 = 1


                    if alt222 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT431 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2474)
                        if self.failed:
                            return retval


                    else:
                        break #loop222


                char_literal432 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_arrayLiteral2478)
                if self.failed:
                    return retval

                char_literal432_tree = self.adaptor.createWithPayload(char_literal432)
                self.adaptor.addChild(root_0, char_literal432_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:370:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
    def objectLiteral(self, ):

        retval = self.objectLiteral_return()
        retval.start = self.input.LT(1)
        objectLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal433 = None
        LT434 = None
        LT436 = None
        char_literal437 = None
        LT438 = None
        LT440 = None
        char_literal441 = None
        propertyNameAndValue435 = None

        propertyNameAndValue439 = None


        char_literal433_tree = None
        LT434_tree = None
        LT436_tree = None
        char_literal437_tree = None
        LT438_tree = None
        LT440_tree = None
        char_literal441_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_41 = RewriteRuleTokenStream(self.adaptor, "token 41")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_39 = RewriteRuleTokenStream(self.adaptor, "token 39")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}'
                char_literal433 = self.input.LT(1)
                self.match(self.input, 41, self.FOLLOW_41_in_objectLiteral2497)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_41.add(char_literal433)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:8: ( LT )*
                while True: #loop223
                    alt223 = 2
                    LA223_0 = self.input.LA(1)

                    if (LA223_0 == LT) :
                        LA223_2 = self.input.LA(2)

                        if (self.synpred291()) :
                            alt223 = 1




                    if alt223 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT434 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2499)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT434)


                    else:
                        break #loop223


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:12: ( propertyNameAndValue )?
                alt224 = 2
                LA224_0 = self.input.LA(1)

                if ((StringLiteral <= LA224_0 <= NumericLiteral) or LA224_0 == Identifier or LA224_0 == 52 or (112 <= LA224_0 <= 113)) :
                    alt224 = 1
                if alt224 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2502)
                    propertyNameAndValue435 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue435.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop227
                    alt227 = 2
                    alt227 = self.dfa227.predict(self.input)
                    if alt227 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:35: ( LT )*
                        while True: #loop225
                            alt225 = 2
                            LA225_0 = self.input.LA(1)

                            if (LA225_0 == LT) :
                                alt225 = 1


                            if alt225 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT436 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2506)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT436)


                            else:
                                break #loop225


                        char_literal437 = self.input.LT(1)
                        self.match(self.input, 39, self.FOLLOW_39_in_objectLiteral2509)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_39.add(char_literal437)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:43: ( LT )*
                        while True: #loop226
                            alt226 = 2
                            LA226_0 = self.input.LA(1)

                            if (LA226_0 == LT) :
                                alt226 = 1


                            if alt226 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT438 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2511)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT438)


                            else:
                                break #loop226


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2514)
                        propertyNameAndValue439 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue439.tree)


                    else:
                        break #loop227


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:70: ( LT )*
                while True: #loop228
                    alt228 = 2
                    LA228_0 = self.input.LA(1)

                    if (LA228_0 == LT) :
                        alt228 = 1


                    if alt228 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT440 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2518)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT440)


                    else:
                        break #loop228


                char_literal441 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_objectLiteral2521)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_42.add(char_literal441)
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
                    # 372:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:372:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:372:12: ( propertyNameAndValue )*
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:375:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName assignmentExpression ) | ( 'get' | 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP identifier ^( FUNC identifier formalParameterList functionBody ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        LT443 = None
        char_literal444 = None
        LT445 = None
        string_literal447 = None
        string_literal448 = None
        LT449 = None
        LT451 = None
        LT453 = None
        propertyName442 = None

        assignmentExpression446 = None

        identifier450 = None

        formalParameterList452 = None

        functionBody454 = None


        LT443_tree = None
        char_literal444_tree = None
        LT445_tree = None
        string_literal447_tree = None
        string_literal448_tree = None
        LT449_tree = None
        LT451_tree = None
        LT453_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_112 = RewriteRuleTokenStream(self.adaptor, "token 112")
        stream_58 = RewriteRuleTokenStream(self.adaptor, "token 58")
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:376:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName assignmentExpression ) | ( 'get' | 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody -> ^( PROP identifier ^( FUNC identifier formalParameterList functionBody ) ) )
                alt235 = 2
                alt235 = self.dfa235.predict(self.input)
                if alt235 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:376:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue2545)
                    propertyName442 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName442.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:376:17: ( LT )*
                    while True: #loop229
                        alt229 = 2
                        LA229_0 = self.input.LA(1)

                        if (LA229_0 == LT) :
                            alt229 = 1


                        if alt229 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT443 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2547)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT443)


                        else:
                            break #loop229


                    char_literal444 = self.input.LT(1)
                    self.match(self.input, 58, self.FOLLOW_58_in_propertyNameAndValue2550)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_58.add(char_literal444)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:376:25: ( LT )*
                    while True: #loop230
                        alt230 = 2
                        LA230_0 = self.input.LA(1)

                        if (LA230_0 == LT) :
                            alt230 = 1


                        if alt230 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT445 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2552)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT445)


                        else:
                            break #loop230


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue2555)
                    assignmentExpression446 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression446.tree)
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
                        # 377:3: -> ^( PROP propertyName assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:377:6: ^( PROP propertyName assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt235 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:4: ( 'get' | 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* functionBody
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:4: ( 'get' | 'set' )
                    alt231 = 2
                    LA231_0 = self.input.LA(1)

                    if (LA231_0 == 112) :
                        alt231 = 1
                    elif (LA231_0 == 113) :
                        alt231 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("378:4: ( 'get' | 'set' )", 231, 0, self.input)

                        raise nvae

                    if alt231 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:5: 'get'
                        string_literal447 = self.input.LT(1)
                        self.match(self.input, 112, self.FOLLOW_112_in_propertyNameAndValue2573)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_112.add(string_literal447)


                    elif alt231 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:11: 'set'
                        string_literal448 = self.input.LT(1)
                        self.match(self.input, 113, self.FOLLOW_113_in_propertyNameAndValue2575)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_113.add(string_literal448)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:18: ( LT )*
                    while True: #loop232
                        alt232 = 2
                        LA232_0 = self.input.LA(1)

                        if (LA232_0 == LT) :
                            alt232 = 1


                        if alt232 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT449 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2578)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT449)


                        else:
                            break #loop232


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2581)
                    identifier450 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier450.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:33: ( LT )*
                    while True: #loop233
                        alt233 = 2
                        LA233_0 = self.input.LA(1)

                        if (LA233_0 == LT) :
                            alt233 = 1


                        if alt233 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT451 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2583)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT451)


                        else:
                            break #loop233


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue2586)
                    formalParameterList452 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList452.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:57: ( LT )*
                    while True: #loop234
                        alt234 = 2
                        LA234_0 = self.input.LA(1)

                        if (LA234_0 == LT) :
                            alt234 = 1


                        if alt234 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT453 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2588)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT453)


                        else:
                            break #loop234


                    self.following.append(self.FOLLOW_functionBody_in_propertyNameAndValue2591)
                    functionBody454 = self.functionBody()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_functionBody.add(functionBody454.tree)
                    # AST Rewrite
                    # elements: identifier, formalParameterList, functionBody, identifier
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
                        # 379:3: -> ^( PROP identifier ^( FUNC identifier formalParameterList functionBody ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:6: ^( PROP identifier ^( FUNC identifier formalParameterList functionBody ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:379:24: ^( FUNC identifier formalParameterList functionBody )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_identifier.next())
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral456 = None
        NumericLiteral457 = None
        identifier455 = None


        StringLiteral456_tree = None
        NumericLiteral457_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:2: ( identifier | StringLiteral | NumericLiteral )
                alt236 = 3
                LA236 = self.input.LA(1)
                if LA236 == Identifier or LA236 == 52 or LA236 == 112 or LA236 == 113:
                    alt236 = 1
                elif LA236 == StringLiteral:
                    alt236 = 2
                elif LA236 == NumericLiteral:
                    alt236 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("382:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 236, 0, self.input)

                    raise nvae

                if alt236 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName2622)
                    identifier455 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier455.tree)


                elif alt236 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral456 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName2627)
                    if self.failed:
                        return retval

                    StringLiteral456_tree = self.adaptor.createWithPayload(StringLiteral456)
                    self.adaptor.addChild(root_0, StringLiteral456_tree)



                elif alt236 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:385:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral457 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName2632)
                    if self.failed:
                        return retval

                    NumericLiteral457_tree = self.adaptor.createWithPayload(NumericLiteral457)
                    self.adaptor.addChild(root_0, NumericLiteral457_tree)



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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | RegularExpressionLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        set458 = None

        set458_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:2: ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | RegularExpressionLiteral )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set458 = self.input.LT(1)
                if (StringLiteral <= self.input.LA(1) <= RegularExpressionLiteral) or (114 <= self.input.LA(1) <= 116):
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:1: regularExpressionLiteral : '/' RegularExpressionLiteral '/' Identifier ;
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal459 = None
        RegularExpressionLiteral460 = None
        char_literal461 = None
        Identifier462 = None

        char_literal459_tree = None
        RegularExpressionLiteral460_tree = None
        char_literal461_tree = None
        Identifier462_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:399:2: ( '/' RegularExpressionLiteral '/' Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:399:4: '/' RegularExpressionLiteral '/' Identifier
                root_0 = self.adaptor.nil()

                char_literal459 = self.input.LT(1)
                self.match(self.input, 102, self.FOLLOW_102_in_regularExpressionLiteral2680)
                if self.failed:
                    return retval

                char_literal459_tree = self.adaptor.createWithPayload(char_literal459)
                self.adaptor.addChild(root_0, char_literal459_tree)

                RegularExpressionLiteral460 = self.input.LT(1)
                self.match(self.input, RegularExpressionLiteral, self.FOLLOW_RegularExpressionLiteral_in_regularExpressionLiteral2682)
                if self.failed:
                    return retval

                RegularExpressionLiteral460_tree = self.adaptor.createWithPayload(RegularExpressionLiteral460)
                self.adaptor.addChild(root_0, RegularExpressionLiteral460_tree)

                char_literal461 = self.input.LT(1)
                self.match(self.input, 102, self.FOLLOW_102_in_regularExpressionLiteral2684)
                if self.failed:
                    return retval

                char_literal461_tree = self.adaptor.createWithPayload(char_literal461)
                self.adaptor.addChild(root_0, char_literal461_tree)

                Identifier462 = self.input.LT(1)
                self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral2686)
                if self.failed:
                    return retval

                Identifier462_tree = self.adaptor.createWithPayload(Identifier462)
                self.adaptor.addChild(root_0, Identifier462_tree)




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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:1: identifier : ( 'get' | 'set' | 'each' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set463 = None

        set463_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:405:2: ( 'get' | 'set' | 'each' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set463 = self.input.LT(1)
                if self.input.LA(1) == Identifier or self.input.LA(1) == 52 or (112 <= self.input.LA(1) <= 113):
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
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:19: ( ( LT )* sourceElement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:19: ( LT )* sourceElement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:28:21: ( LT )*
        while True: #loop237
            alt237 = 2
            LA237_0 = self.input.LA(1)

            if (LA237_0 == LT) :
                alt237 = 1


            if alt237 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred486)
                if self.failed:
                    return 


            else:
                break #loop237


        self.following.append(self.FOLLOW_sourceElement_in_synpred490)
        self.sourceElement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred4



    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:4: ( functionDeclaration )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:32:4: functionDeclaration
        self.following.append(self.FOLLOW_functionDeclaration_in_synpred5104)
        self.functionDeclaration()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred9
    def synpred9_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:15: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:15: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred9165)
        if self.failed:
            return 


    # $ANTLR end synpred9



    # $ANTLR start synpred19
    def synpred19_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred19249)
        if self.failed:
            return 


    # $ANTLR end synpred19



    # $ANTLR start synpred22
    def synpred22_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:57:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred22272)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred22



    # $ANTLR start synpred25
    def synpred25_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred25287)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred25



    # $ANTLR start synpred32
    def synpred32_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred32322)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred32



    # $ANTLR start synpred35
    def synpred35_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred35351)
        if self.failed:
            return 


    # $ANTLR end synpred35



    # $ANTLR start synpred62
    def synpred62_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:61: ( LT )*
        while True: #loop251
            alt251 = 2
            LA251_0 = self.input.LA(1)

            if (LA251_0 == LT) :
                alt251 = 1


            if alt251 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred62617)
                if self.failed:
                    return 


            else:
                break #loop251


        self.match(self.input, 48, self.FOLLOW_48_in_synpred62621)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:73: ( LT )*
        while True: #loop252
            alt252 = 2
            LA252_0 = self.input.LA(1)

            if (LA252_0 == LT) :
                alt252 = 1


            if alt252 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred62623)
                if self.failed:
                    return 


            else:
                break #loop252


        self.following.append(self.FOLLOW_statement_in_synpred62627)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred62



    # $ANTLR start synpred65
    def synpred65_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:124:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:124:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred65651)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred65



    # $ANTLR start synpred87
    def synpred87_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred87841)
        if self.failed:
            return 


    # $ANTLR end synpred87



    # $ANTLR start synpred122
    def synpred122_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1221139)
        if self.failed:
            return 


    # $ANTLR end synpred122



    # $ANTLR start synpred125
    def synpred125_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1251164)
        if self.failed:
            return 


    # $ANTLR end synpred125



    # $ANTLR start synpred144
    def synpred144_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:4: ( conditionalExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:4: conditionalExpression
        self.following.append(self.FOLLOW_conditionalExpression_in_synpred1441356)
        self.conditionalExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred144



    # $ANTLR start synpred147
    def synpred147_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: ( conditionalExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: conditionalExpressionNoIn
        self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_synpred1471385)
        self.conditionalExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred147



    # $ANTLR start synpred150
    def synpred150_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred1501414)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred150



    # $ANTLR start synpred151
    def synpred151_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred1511431)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred151



    # $ANTLR start synpred158
    def synpred158_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:91: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:91: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:93: ( LT )*
        while True: #loop266
            alt266 = 2
            LA266_0 = self.input.LA(1)

            if (LA266_0 == LT) :
                alt266 = 1


            if alt266 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1581479)
                if self.failed:
                    return 


            else:
                break #loop266


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1581483)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred158



    # $ANTLR start synpred162
    def synpred162_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:37: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:37: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:39: ( LT )*
        while True: #loop267
            alt267 = 2
            LA267_0 = self.input.LA(1)

            if (LA267_0 == LT) :
                alt267 = 1


            if alt267 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1621522)
                if self.failed:
                    return 


            else:
                break #loop267


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred1621526)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred162



    # $ANTLR start synpred260
    def synpred260_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:32: ( LT )*
        while True: #loop312
            alt312 = 2
            LA312_0 = self.input.LA(1)

            if (LA312_0 == LT) :
                alt312 = 1


            if alt312 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2602259)
                if self.failed:
                    return 


            else:
                break #loop312


        if (99 <= self.input.LA(1) <= 100):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2602263
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:49: ( LT )*
        while True: #loop313
            alt313 = 2
            LA313_0 = self.input.LA(1)

            if (LA313_0 == LT) :
                alt313 = 1


            if alt313 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2602271)
                if self.failed:
                    return 


            else:
                break #loop313


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred2602275)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred260



    # $ANTLR start synpred284
    def synpred284_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:366:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2842449)
        if self.failed:
            return 


    # $ANTLR end synpred284



    # $ANTLR start synpred291
    def synpred291_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2912499)
        if self.failed:
            return 


    # $ANTLR end synpred291



    def synpred25(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred25_fragment()
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

    def synpred260(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred260_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred162(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred162_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred151(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred151_fragment()
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

    def synpred22(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred22_fragment()
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

    def synpred62(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred62_fragment()
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

    def synpred87(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred87_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred9(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred9_fragment()
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

    def synpred35(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred35_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred291(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred291_fragment()
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

    def synpred19(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred19_fragment()
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

    def synpred158(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred158_fragment()
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

    def synpred144(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred144_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred125(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred125_fragment()
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
        u"\1\10\1\7\1\uffff\12\7\1\0\2\7\1\0\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\164\1\161\1\uffff\1\161\2\46\2\161\1\50\1\51\1\50\1\161\1\51"
        u"\1\0\1\161\1\50\1\0\2\uffff"
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
    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\2\161\2\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA17_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA17_transition = [
        DFA.unpack(u"\1\1\3\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\3\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
        u"\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    DFA17 = DFA
    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\2\50\2\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA16_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA16_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    DFA16 = DFA
    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA27_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\3\uffff\15\3"),
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #27

    DFA27 = DFA
    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\2"
        )

    DFA31_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA31_max = DFA.unpack(
        u"\1\55\1\164\2\uffff\1\164"
        )

    DFA31_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA31_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA31_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #31

    DFA31 = DFA
    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA34_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    DFA34 = DFA
    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA36_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA36_max = DFA.unpack(
        u"\1\56\1\164\2\uffff\1\164"
        )

    DFA36_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA36_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA36_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2"),
        DFA.unpack(u"\1\4\4\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\3\uffff\15\3")
    ]

    # class definition for DFA #36

    DFA36 = DFA
    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\2\65\2\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA38_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA38_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #38

    DFA38 = DFA
    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA58_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA58_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA58_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA58_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #58

    DFA58 = DFA
    # lookup tables for DFA #61

    DFA61_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA61_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA61_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA61_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA61_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA61_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA61_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #61

    DFA61 = DFA
    # lookup tables for DFA #64

    DFA64_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA64_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA64_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA64_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA64_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA64_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA64_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #64

    DFA64 = DFA
    # lookup tables for DFA #93

    DFA93_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA93_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA93_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA93_max = DFA.unpack(
        u"\2\75\2\uffff"
        )

    DFA93_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA93_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA93_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #93

    DFA93 = DFA
    # lookup tables for DFA #97

    DFA97_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA97_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA97_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA97_max = DFA.unpack(
        u"\2\75\2\uffff"
        )

    DFA97_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA97_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA97_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u"\1\1\42\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #97

    DFA97 = DFA
    # lookup tables for DFA #96

    DFA96_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA96_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA96_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA96_max = DFA.unpack(
        u"\2\74\2\uffff"
        )

    DFA96_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA96_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA96_transition = [
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u"\1\1\42\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #96

    DFA96 = DFA
    # lookup tables for DFA #109

    DFA109_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA109_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA109_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA109_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA109_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA109_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA109_transition = [
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u"\1\1\4\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #109

    DFA109 = DFA
    # lookup tables for DFA #118

    DFA118_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA118_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA118_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA118_max = DFA.unpack(
        u"\1\104\1\164\2\uffff\1\164"
        )

    DFA118_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA118_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA118_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2\4\uffff\1\2\14\uffff\1\2\11\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #118

    DFA118 = DFA
    # lookup tables for DFA #121

    DFA121_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA121_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA121_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA121_max = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA121_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA121_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA121_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #121

    DFA121 = DFA
    # lookup tables for DFA #145

    DFA145_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA145_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA145_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA145_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA145_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\3\uffff\15\2"),
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
        u"\2\7\2\uffff"
        )

    DFA144_max = DFA.unpack(
        u"\2\50\2\uffff"
        )

    DFA144_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA144_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA144_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #144

    DFA144 = DFA
    # lookup tables for DFA #154

    DFA154_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA154_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA154_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA154_max = DFA.unpack(
        u"\1\121\1\164\2\uffff\1\164"
        )

    DFA154_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA154_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA154_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\3\1\uffff\1\3\2\uffff\1\3\14\uffff\1"
        u"\3\11\uffff\1\3\14\uffff\1\2"),
        DFA.unpack(u"\1\4\4\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\3\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\3\uffff\15\3")
    ]

    # class definition for DFA #154

    DFA154 = DFA
    # lookup tables for DFA #159

    DFA159_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA159_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA159_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA159_max = DFA.unpack(
        u"\2\121\2\uffff"
        )

    DFA159_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA159_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA159_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #159

    DFA159 = DFA
    # lookup tables for DFA #162

    DFA162_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA162_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA162_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA162_max = DFA.unpack(
        u"\1\122\1\164\2\uffff\1\164"
        )

    DFA162_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA162_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA162_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\1\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #162

    DFA162 = DFA
    # lookup tables for DFA #165

    DFA165_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA165_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA165_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA165_max = DFA.unpack(
        u"\2\122\2\uffff"
        )

    DFA165_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA165_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA165_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #165

    DFA165 = DFA
    # lookup tables for DFA #168

    DFA168_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA168_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA168_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA168_max = DFA.unpack(
        u"\1\123\1\164\2\uffff\1\164"
        )

    DFA168_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA168_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA168_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\2\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #168

    DFA168 = DFA
    # lookup tables for DFA #171

    DFA171_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA171_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA171_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA171_max = DFA.unpack(
        u"\2\123\2\uffff"
        )

    DFA171_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA171_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA171_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #171

    DFA171 = DFA
    # lookup tables for DFA #174

    DFA174_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA174_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA174_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA174_max = DFA.unpack(
        u"\1\124\1\164\2\uffff\1\164"
        )

    DFA174_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA174_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA174_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\3\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #174

    DFA174 = DFA
    # lookup tables for DFA #177

    DFA177_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA177_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA177_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA177_max = DFA.unpack(
        u"\2\124\2\uffff"
        )

    DFA177_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA177_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA177_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #177

    DFA177 = DFA
    # lookup tables for DFA #180

    DFA180_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA180_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA180_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA180_max = DFA.unpack(
        u"\1\125\1\164\2\uffff\1\164"
        )

    DFA180_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA180_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA180_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\4\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #180

    DFA180 = DFA
    # lookup tables for DFA #183

    DFA183_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA183_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA183_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA183_max = DFA.unpack(
        u"\2\125\2\uffff"
        )

    DFA183_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA183_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA183_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #183

    DFA183 = DFA
    # lookup tables for DFA #186

    DFA186_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA186_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA186_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA186_max = DFA.unpack(
        u"\1\126\1\164\2\uffff\1\164"
        )

    DFA186_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA186_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA186_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\5\2\1\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #186

    DFA186 = DFA
    # lookup tables for DFA #189

    DFA189_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA189_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA189_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA189_max = DFA.unpack(
        u"\2\126\2\uffff"
        )

    DFA189_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA189_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA189_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #189

    DFA189 = DFA
    # lookup tables for DFA #192

    DFA192_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA192_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA192_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA192_max = DFA.unpack(
        u"\1\132\1\164\2\uffff\1\164"
        )

    DFA192_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA192_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA192_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\6\2\4\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #192

    DFA192 = DFA
    # lookup tables for DFA #195

    DFA195_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA195_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA195_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA195_max = DFA.unpack(
        u"\2\132\2\uffff"
        )

    DFA195_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA195_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA195_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #195

    DFA195 = DFA
    # lookup tables for DFA #198

    DFA198_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA198_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA198_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA198_max = DFA.unpack(
        u"\1\137\1\164\2\uffff\1\164"
        )

    DFA198_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA198_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA198_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\3\4\uffff\1\2\11\uffff\1\2\14\uffff\12\2\5\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #198

    DFA198 = DFA
    # lookup tables for DFA #201

    DFA201_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA201_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA201_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA201_max = DFA.unpack(
        u"\2\137\2\uffff"
        )

    DFA201_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA201_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA201_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
        DFA.unpack(u"\1\1\37\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #201

    DFA201 = DFA
    # lookup tables for DFA #204

    DFA204_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA204_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA204_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA204_max = DFA.unpack(
        u"\1\142\1\164\2\uffff\1\164"
        )

    DFA204_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA204_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA204_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\4\uffff\1\2\11\uffff\1\2\14\uffff\17\2\3\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\3\uffff\15\2")
    ]

    # class definition for DFA #204

    DFA204 = DFA
    # lookup tables for DFA #210

    DFA210_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA210_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA210_min = DFA.unpack(
        u"\2\7\2\uffff\1\7"
        )

    DFA210_max = DFA.unpack(
        u"\1\147\1\164\2\uffff\1\164"
        )

    DFA210_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA210_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA210_transition = [
        DFA.unpack(u"\1\1\37\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\4\uffff\1\2\11\uffff\1\2\14\uffff\24\2\3\3"),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\24\2\3\3\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\4\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\24\2\3\3\15\2")
    ]

    # class definition for DFA #210

    DFA210 = DFA
    # lookup tables for DFA #221

    DFA221_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA221_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA221_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA221_max = DFA.unpack(
        u"\2\104\2\uffff"
        )

    DFA221_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA221_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA221_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #221

    DFA221 = DFA
    # lookup tables for DFA #220

    DFA220_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA220_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA220_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA220_max = DFA.unpack(
        u"\2\164\2\uffff"
        )

    DFA220_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA220_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA220_transition = [
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u"\1\1\4\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\3\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #220

    DFA220 = DFA
    # lookup tables for DFA #227

    DFA227_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA227_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA227_min = DFA.unpack(
        u"\2\7\2\uffff"
        )

    DFA227_max = DFA.unpack(
        u"\2\52\2\uffff"
        )

    DFA227_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA227_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA227_transition = [
        DFA.unpack(u"\1\1\37\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\37\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #227

    DFA227 = DFA
    # lookup tables for DFA #235

    DFA235_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA235_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA235_min = DFA.unpack(
        u"\1\10\1\7\1\uffff\2\7\1\uffff"
        )

    DFA235_max = DFA.unpack(
        u"\2\161\1\uffff\2\161\1\uffff"
        )

    DFA235_accept = DFA.unpack(
        u"\2\uffff\1\1\2\uffff\1\2"
        )

    DFA235_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA235_transition = [
        DFA.unpack(u"\2\2\1\uffff\1\2\50\uffff\1\2\73\uffff\1\1\1\3"),
        DFA.unpack(u"\1\4\3\uffff\1\5\50\uffff\1\5\5\uffff\1\2\65\uffff\2"
        u"\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\uffff\1\5\50\uffff\1\5\5\uffff\1\2\65\uffff\2"
        u"\5"),
        DFA.unpack(u"\1\4\3\uffff\1\5\50\uffff\1\5\5\uffff\1\2\65\uffff\2"
        u"\5"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #235

    DFA235 = DFA
 

    FOLLOW_LT_in_program60 = frozenset([1])
    FOLLOW_sourceElements_in_program64 = frozenset([7])
    FOLLOW_LT_in_program66 = frozenset([1])
    FOLLOW_EOF_in_program70 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements83 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_sourceElements86 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_sourceElement_in_sourceElements90 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_functionDeclaration_in_sourceElement104 = frozenset([1])
    FOLLOW_statement_in_sourceElement109 = frozenset([1])
    FOLLOW_37_in_functionDeclaration122 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_functionDeclaration124 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_identifier_in_functionDeclaration127 = frozenset([7, 38])
    FOLLOW_LT_in_functionDeclaration129 = frozenset([7, 38])
    FOLLOW_formalParameterList_in_functionDeclaration132 = frozenset([7, 41])
    FOLLOW_LT_in_functionDeclaration134 = frozenset([7, 41])
    FOLLOW_functionBody_in_functionDeclaration137 = frozenset([1])
    FOLLOW_37_in_functionExpression163 = frozenset([7, 11, 38, 52, 112, 113])
    FOLLOW_LT_in_functionExpression165 = frozenset([7, 11, 38, 52, 112, 113])
    FOLLOW_identifier_in_functionExpression168 = frozenset([7, 38])
    FOLLOW_LT_in_functionExpression171 = frozenset([7, 38])
    FOLLOW_formalParameterList_in_functionExpression174 = frozenset([7, 41])
    FOLLOW_LT_in_functionExpression176 = frozenset([7, 41])
    FOLLOW_functionBody_in_functionExpression179 = frozenset([1])
    FOLLOW_38_in_formalParameterList206 = frozenset([7, 11, 40, 52, 112, 113])
    FOLLOW_LT_in_formalParameterList209 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_identifier_in_formalParameterList213 = frozenset([7, 39, 40])
    FOLLOW_LT_in_formalParameterList216 = frozenset([7, 39])
    FOLLOW_39_in_formalParameterList220 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_formalParameterList222 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_identifier_in_formalParameterList226 = frozenset([7, 39, 40])
    FOLLOW_LT_in_formalParameterList232 = frozenset([1])
    FOLLOW_40_in_formalParameterList236 = frozenset([1])
    FOLLOW_41_in_functionBody247 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_functionBody249 = frozenset([1])
    FOLLOW_sourceElements_in_functionBody253 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_functionBody256 = frozenset([1])
    FOLLOW_42_in_functionBody260 = frozenset([1])
    FOLLOW_statementBlock_in_statement272 = frozenset([1])
    FOLLOW_variableStatement_in_statement277 = frozenset([1])
    FOLLOW_emptyStatement_in_statement282 = frozenset([1])
    FOLLOW_expressionStatement_in_statement287 = frozenset([1])
    FOLLOW_ifStatement_in_statement292 = frozenset([1])
    FOLLOW_iterationStatement_in_statement297 = frozenset([1])
    FOLLOW_continueStatement_in_statement302 = frozenset([1])
    FOLLOW_breakStatement_in_statement307 = frozenset([1])
    FOLLOW_returnStatement_in_statement312 = frozenset([1])
    FOLLOW_withStatement_in_statement317 = frozenset([1])
    FOLLOW_labelledStatement_in_statement322 = frozenset([1])
    FOLLOW_switchStatement_in_statement327 = frozenset([1])
    FOLLOW_throwStatement_in_statement332 = frozenset([1])
    FOLLOW_tryStatement_in_statement337 = frozenset([1])
    FOLLOW_41_in_statementBlock349 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_statementBlock351 = frozenset([1])
    FOLLOW_statementList_in_statementBlock355 = frozenset([7, 42])
    FOLLOW_LT_in_statementBlock358 = frozenset([1])
    FOLLOW_42_in_statementBlock362 = frozenset([1])
    FOLLOW_statement_in_statementList374 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_statementList377 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_statement_in_statementList381 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_set_in_variableStatement395 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_variableStatement401 = frozenset([1])
    FOLLOW_variableDeclarationList_in_variableStatement405 = frozenset([7, 45])
    FOLLOW_set_in_variableStatement407 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList425 = frozenset([1, 7, 39])
    FOLLOW_LT_in_variableDeclarationList428 = frozenset([7, 39])
    FOLLOW_39_in_variableDeclarationList432 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_variableDeclarationList434 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_variableDeclaration_in_variableDeclarationList438 = frozenset([1, 7, 39])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn452 = frozenset([1, 7, 39])
    FOLLOW_LT_in_variableDeclarationListNoIn455 = frozenset([7, 39])
    FOLLOW_39_in_variableDeclarationListNoIn459 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_variableDeclarationListNoIn461 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn465 = frozenset([1, 7, 39])
    FOLLOW_identifier_in_variableDeclaration479 = frozenset([1, 7, 46])
    FOLLOW_LT_in_variableDeclaration482 = frozenset([7, 46])
    FOLLOW_initialiser_in_variableDeclaration486 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn500 = frozenset([1, 7, 46])
    FOLLOW_LT_in_variableDeclarationNoIn503 = frozenset([7, 46])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn507 = frozenset([1])
    FOLLOW_46_in_initialiser521 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_initialiser523 = frozenset([1])
    FOLLOW_assignmentExpression_in_initialiser527 = frozenset([1])
    FOLLOW_46_in_initialiserNoIn539 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_initialiserNoIn541 = frozenset([1])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn545 = frozenset([1])
    FOLLOW_45_in_emptyStatement557 = frozenset([1])
    FOLLOW_expression_in_expressionStatement569 = frozenset([7, 45])
    FOLLOW_set_in_expressionStatement571 = frozenset([1])
    FOLLOW_47_in_ifStatement590 = frozenset([7, 38])
    FOLLOW_LT_in_ifStatement592 = frozenset([1])
    FOLLOW_38_in_ifStatement596 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_ifStatement598 = frozenset([1])
    FOLLOW_expression_in_ifStatement602 = frozenset([7, 40])
    FOLLOW_LT_in_ifStatement604 = frozenset([1])
    FOLLOW_40_in_ifStatement608 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_ifStatement610 = frozenset([1])
    FOLLOW_statement_in_ifStatement614 = frozenset([1, 7, 48])
    FOLLOW_LT_in_ifStatement617 = frozenset([7, 48])
    FOLLOW_48_in_ifStatement621 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_ifStatement623 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_statement_in_ifStatement627 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement641 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement646 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement651 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement656 = frozenset([1])
    FOLLOW_49_in_doWhileStatement668 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_doWhileStatement670 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement674 = frozenset([7, 50])
    FOLLOW_LT_in_doWhileStatement676 = frozenset([1])
    FOLLOW_50_in_doWhileStatement680 = frozenset([7, 38])
    FOLLOW_LT_in_doWhileStatement682 = frozenset([1])
    FOLLOW_38_in_doWhileStatement686 = frozenset([8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_expression_in_doWhileStatement688 = frozenset([40])
    FOLLOW_40_in_doWhileStatement690 = frozenset([7, 45])
    FOLLOW_set_in_doWhileStatement692 = frozenset([1])
    FOLLOW_50_in_whileStatement711 = frozenset([7, 38])
    FOLLOW_LT_in_whileStatement713 = frozenset([1])
    FOLLOW_38_in_whileStatement717 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_whileStatement719 = frozenset([1])
    FOLLOW_expression_in_whileStatement723 = frozenset([7, 40])
    FOLLOW_LT_in_whileStatement725 = frozenset([1])
    FOLLOW_40_in_whileStatement729 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_whileStatement731 = frozenset([1])
    FOLLOW_statement_in_whileStatement735 = frozenset([1])
    FOLLOW_51_in_forStatement747 = frozenset([7, 38])
    FOLLOW_LT_in_forStatement749 = frozenset([1])
    FOLLOW_38_in_forStatement753 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 45, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forStatement756 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_forStatementInitialiserPart_in_forStatement760 = frozenset([7, 45])
    FOLLOW_LT_in_forStatement764 = frozenset([1])
    FOLLOW_45_in_forStatement768 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 45, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forStatement771 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_expression_in_forStatement775 = frozenset([7, 45])
    FOLLOW_LT_in_forStatement779 = frozenset([1])
    FOLLOW_45_in_forStatement783 = frozenset([7, 8, 9, 10, 11, 37, 38, 40, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forStatement786 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_expression_in_forStatement790 = frozenset([7, 40])
    FOLLOW_LT_in_forStatement794 = frozenset([1])
    FOLLOW_40_in_forStatement798 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forStatement800 = frozenset([1])
    FOLLOW_statement_in_forStatement804 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart816 = frozenset([1])
    FOLLOW_43_in_forStatementInitialiserPart821 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_forStatementInitialiserPart823 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart827 = frozenset([1])
    FOLLOW_51_in_forInStatement839 = frozenset([7, 38, 52])
    FOLLOW_LT_in_forInStatement841 = frozenset([1])
    FOLLOW_52_in_forInStatement845 = frozenset([7, 38])
    FOLLOW_LT_in_forInStatement848 = frozenset([1])
    FOLLOW_38_in_forInStatement852 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 52, 66, 67, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forInStatement854 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement858 = frozenset([7, 53])
    FOLLOW_LT_in_forInStatement860 = frozenset([1])
    FOLLOW_53_in_forInStatement864 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forInStatement866 = frozenset([1])
    FOLLOW_expression_in_forInStatement870 = frozenset([7, 40])
    FOLLOW_LT_in_forInStatement872 = frozenset([1])
    FOLLOW_40_in_forInStatement876 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_forInStatement878 = frozenset([1])
    FOLLOW_statement_in_forInStatement882 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart894 = frozenset([1])
    FOLLOW_43_in_forInStatementInitialiserPart899 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_forInStatementInitialiserPart901 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart905 = frozenset([1])
    FOLLOW_54_in_continueStatement916 = frozenset([7, 11, 45, 52, 112, 113])
    FOLLOW_identifier_in_continueStatement918 = frozenset([7, 45])
    FOLLOW_set_in_continueStatement921 = frozenset([1])
    FOLLOW_55_in_breakStatement939 = frozenset([7, 11, 45, 52, 112, 113])
    FOLLOW_identifier_in_breakStatement941 = frozenset([7, 45])
    FOLLOW_set_in_breakStatement944 = frozenset([1])
    FOLLOW_56_in_returnStatement962 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 45, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_expression_in_returnStatement964 = frozenset([7, 45])
    FOLLOW_set_in_returnStatement967 = frozenset([1])
    FOLLOW_57_in_withStatement986 = frozenset([7, 38])
    FOLLOW_LT_in_withStatement988 = frozenset([1])
    FOLLOW_38_in_withStatement992 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_withStatement994 = frozenset([1])
    FOLLOW_expression_in_withStatement998 = frozenset([7, 40])
    FOLLOW_LT_in_withStatement1000 = frozenset([1])
    FOLLOW_40_in_withStatement1004 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_withStatement1006 = frozenset([1])
    FOLLOW_statement_in_withStatement1010 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1021 = frozenset([7, 58])
    FOLLOW_LT_in_labelledStatement1023 = frozenset([1])
    FOLLOW_58_in_labelledStatement1027 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_labelledStatement1029 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1033 = frozenset([1])
    FOLLOW_59_in_switchStatement1045 = frozenset([7, 38])
    FOLLOW_LT_in_switchStatement1047 = frozenset([1])
    FOLLOW_38_in_switchStatement1051 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_switchStatement1053 = frozenset([1])
    FOLLOW_expression_in_switchStatement1057 = frozenset([7, 40])
    FOLLOW_LT_in_switchStatement1059 = frozenset([1])
    FOLLOW_40_in_switchStatement1063 = frozenset([7, 41])
    FOLLOW_LT_in_switchStatement1065 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1069 = frozenset([1])
    FOLLOW_41_in_caseBlock1081 = frozenset([7, 42, 60, 61])
    FOLLOW_LT_in_caseBlock1084 = frozenset([7, 60])
    FOLLOW_caseClause_in_caseBlock1088 = frozenset([7, 42, 60, 61])
    FOLLOW_LT_in_caseBlock1093 = frozenset([7, 61])
    FOLLOW_defaultClause_in_caseBlock1097 = frozenset([7, 42, 60])
    FOLLOW_LT_in_caseBlock1100 = frozenset([7, 60])
    FOLLOW_caseClause_in_caseBlock1104 = frozenset([7, 42, 60])
    FOLLOW_LT_in_caseBlock1110 = frozenset([1])
    FOLLOW_42_in_caseBlock1114 = frozenset([1])
    FOLLOW_60_in_caseClause1125 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_caseClause1127 = frozenset([1])
    FOLLOW_expression_in_caseClause1131 = frozenset([7, 58])
    FOLLOW_LT_in_caseClause1133 = frozenset([1])
    FOLLOW_58_in_caseClause1137 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_caseClause1139 = frozenset([1])
    FOLLOW_statementList_in_caseClause1143 = frozenset([1])
    FOLLOW_61_in_defaultClause1156 = frozenset([7, 58])
    FOLLOW_LT_in_defaultClause1158 = frozenset([1])
    FOLLOW_58_in_defaultClause1162 = frozenset([1, 7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_defaultClause1164 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1168 = frozenset([1])
    FOLLOW_62_in_throwStatement1181 = frozenset([8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_expression_in_throwStatement1183 = frozenset([7, 45])
    FOLLOW_set_in_throwStatement1185 = frozenset([1])
    FOLLOW_63_in_tryStatement1203 = frozenset([7, 41])
    FOLLOW_LT_in_tryStatement1205 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1209 = frozenset([7, 64, 65])
    FOLLOW_LT_in_tryStatement1211 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1216 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1220 = frozenset([1, 7, 65])
    FOLLOW_LT_in_tryStatement1223 = frozenset([7, 65])
    FOLLOW_finallyClause_in_tryStatement1227 = frozenset([1])
    FOLLOW_64_in_catchClause1248 = frozenset([7, 38])
    FOLLOW_LT_in_catchClause1250 = frozenset([1])
    FOLLOW_38_in_catchClause1254 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_catchClause1256 = frozenset([1])
    FOLLOW_identifier_in_catchClause1260 = frozenset([7, 40])
    FOLLOW_LT_in_catchClause1262 = frozenset([1])
    FOLLOW_40_in_catchClause1266 = frozenset([7, 41])
    FOLLOW_LT_in_catchClause1268 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1272 = frozenset([1])
    FOLLOW_65_in_finallyClause1284 = frozenset([7, 41])
    FOLLOW_LT_in_finallyClause1286 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause1290 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1302 = frozenset([1, 7, 39])
    FOLLOW_LT_in_expression1305 = frozenset([7, 39])
    FOLLOW_39_in_expression1309 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_expression1311 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_expression1315 = frozenset([1, 7, 39])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1329 = frozenset([1, 7, 39])
    FOLLOW_LT_in_expressionNoIn1332 = frozenset([7, 39])
    FOLLOW_39_in_expressionNoIn1336 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_expressionNoIn1338 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1342 = frozenset([1, 7, 39])
    FOLLOW_conditionalExpression_in_assignmentExpression1356 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1361 = frozenset([7, 46, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_LT_in_assignmentExpression1363 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpression1367 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_assignmentExpression1369 = frozenset([1])
    FOLLOW_assignmentExpression_in_assignmentExpression1373 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1385 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1390 = frozenset([7, 46, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
    FOLLOW_LT_in_assignmentExpressionNoIn1392 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1396 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_assignmentExpressionNoIn1398 = frozenset([1])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1402 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression1414 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression1419 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1431 = frozenset([1])
    FOLLOW_66_in_newExpression1436 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_newExpression1438 = frozenset([1])
    FOLLOW_newExpression_in_newExpression1442 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1455 = frozenset([1, 7, 67, 69])
    FOLLOW_functionExpression_in_memberExpression1459 = frozenset([1, 7, 67, 69])
    FOLLOW_66_in_memberExpression1463 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_memberExpression1465 = frozenset([1])
    FOLLOW_memberExpression_in_memberExpression1469 = frozenset([7, 38])
    FOLLOW_LT_in_memberExpression1471 = frozenset([1])
    FOLLOW_arguments_in_memberExpression1475 = frozenset([1, 7, 67, 69])
    FOLLOW_LT_in_memberExpression1479 = frozenset([7, 67, 69])
    FOLLOW_memberExpressionSuffix_in_memberExpression1483 = frozenset([1, 7, 67, 69])
    FOLLOW_indexSuffix_in_memberExpressionSuffix1497 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1502 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression1513 = frozenset([7, 38])
    FOLLOW_LT_in_callExpression1515 = frozenset([1])
    FOLLOW_arguments_in_callExpression1519 = frozenset([1, 7, 38, 67, 69])
    FOLLOW_LT_in_callExpression1522 = frozenset([7, 38, 67, 69])
    FOLLOW_callExpressionSuffix_in_callExpression1526 = frozenset([1, 7, 38, 67, 69])
    FOLLOW_arguments_in_callExpressionSuffix1540 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix1545 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1550 = frozenset([1])
    FOLLOW_38_in_arguments1561 = frozenset([7, 8, 9, 10, 11, 37, 38, 40, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_arguments1564 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_arguments1568 = frozenset([7, 39, 40])
    FOLLOW_LT_in_arguments1571 = frozenset([7, 39])
    FOLLOW_39_in_arguments1575 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_arguments1577 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_arguments1581 = frozenset([7, 39, 40])
    FOLLOW_LT_in_arguments1587 = frozenset([1])
    FOLLOW_40_in_arguments1591 = frozenset([1])
    FOLLOW_67_in_indexSuffix1603 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_indexSuffix1605 = frozenset([1])
    FOLLOW_expression_in_indexSuffix1609 = frozenset([7, 68])
    FOLLOW_LT_in_indexSuffix1611 = frozenset([1])
    FOLLOW_68_in_indexSuffix1615 = frozenset([1])
    FOLLOW_69_in_propertyReferenceSuffix1628 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_propertyReferenceSuffix1630 = frozenset([1])
    FOLLOW_identifier_in_propertyReferenceSuffix1634 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression1701 = frozenset([1, 7, 81])
    FOLLOW_LT_in_conditionalExpression1704 = frozenset([7, 81])
    FOLLOW_81_in_conditionalExpression1708 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_conditionalExpression1710 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_conditionalExpression1714 = frozenset([7, 58])
    FOLLOW_LT_in_conditionalExpression1716 = frozenset([7, 58])
    FOLLOW_58_in_conditionalExpression1720 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_conditionalExpression1722 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_conditionalExpression1726 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1739 = frozenset([1, 7, 81])
    FOLLOW_LT_in_conditionalExpressionNoIn1742 = frozenset([7, 81])
    FOLLOW_81_in_conditionalExpressionNoIn1746 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_conditionalExpressionNoIn1748 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1752 = frozenset([7, 58])
    FOLLOW_LT_in_conditionalExpressionNoIn1754 = frozenset([7, 58])
    FOLLOW_58_in_conditionalExpressionNoIn1758 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_conditionalExpressionNoIn1760 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1764 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression1777 = frozenset([1, 7, 82])
    FOLLOW_LT_in_logicalORExpression1780 = frozenset([7, 82])
    FOLLOW_82_in_logicalORExpression1784 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_logicalORExpression1786 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_logicalANDExpression_in_logicalORExpression1790 = frozenset([1, 7, 82])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1804 = frozenset([1, 7, 82])
    FOLLOW_LT_in_logicalORExpressionNoIn1807 = frozenset([7, 82])
    FOLLOW_82_in_logicalORExpressionNoIn1811 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_logicalORExpressionNoIn1813 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1817 = frozenset([1, 7, 82])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1831 = frozenset([1, 7, 83])
    FOLLOW_LT_in_logicalANDExpression1834 = frozenset([7, 83])
    FOLLOW_83_in_logicalANDExpression1838 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_logicalANDExpression1840 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1844 = frozenset([1, 7, 83])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1858 = frozenset([1, 7, 83])
    FOLLOW_LT_in_logicalANDExpressionNoIn1861 = frozenset([7, 83])
    FOLLOW_83_in_logicalANDExpressionNoIn1865 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_logicalANDExpressionNoIn1867 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1871 = frozenset([1, 7, 83])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1885 = frozenset([1, 7, 84])
    FOLLOW_LT_in_bitwiseORExpression1888 = frozenset([7, 84])
    FOLLOW_84_in_bitwiseORExpression1892 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseORExpression1894 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1898 = frozenset([1, 7, 84])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1912 = frozenset([1, 7, 84])
    FOLLOW_LT_in_bitwiseORExpressionNoIn1915 = frozenset([7, 84])
    FOLLOW_84_in_bitwiseORExpressionNoIn1919 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseORExpressionNoIn1921 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn1925 = frozenset([1, 7, 84])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1939 = frozenset([1, 7, 85])
    FOLLOW_LT_in_bitwiseXORExpression1942 = frozenset([7, 85])
    FOLLOW_85_in_bitwiseXORExpression1946 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseXORExpression1948 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression1952 = frozenset([1, 7, 85])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1966 = frozenset([1, 7, 85])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn1969 = frozenset([7, 85])
    FOLLOW_85_in_bitwiseXORExpressionNoIn1973 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn1975 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn1979 = frozenset([1, 7, 85])
    FOLLOW_equalityExpression_in_bitwiseANDExpression1993 = frozenset([1, 7, 86])
    FOLLOW_LT_in_bitwiseANDExpression1996 = frozenset([7, 86])
    FOLLOW_86_in_bitwiseANDExpression2000 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseANDExpression2002 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2006 = frozenset([1, 7, 86])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2020 = frozenset([1, 7, 86])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2023 = frozenset([7, 86])
    FOLLOW_86_in_bitwiseANDExpressionNoIn2027 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2029 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2033 = frozenset([1, 7, 86])
    FOLLOW_relationalExpression_in_equalityExpression2047 = frozenset([1, 7, 87, 88, 89, 90])
    FOLLOW_LT_in_equalityExpression2050 = frozenset([7, 87, 88, 89, 90])
    FOLLOW_set_in_equalityExpression2054 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_equalityExpression2070 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_relationalExpression_in_equalityExpression2074 = frozenset([1, 7, 87, 88, 89, 90])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2087 = frozenset([1, 7, 87, 88, 89, 90])
    FOLLOW_LT_in_equalityExpressionNoIn2090 = frozenset([7, 87, 88, 89, 90])
    FOLLOW_set_in_equalityExpressionNoIn2094 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_equalityExpressionNoIn2110 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2114 = frozenset([1, 7, 87, 88, 89, 90])
    FOLLOW_shiftExpression_in_relationalExpression2128 = frozenset([1, 7, 53, 91, 92, 93, 94, 95])
    FOLLOW_LT_in_relationalExpression2131 = frozenset([7, 53, 91, 92, 93, 94, 95])
    FOLLOW_set_in_relationalExpression2135 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_relationalExpression2159 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_shiftExpression_in_relationalExpression2163 = frozenset([1, 7, 53, 91, 92, 93, 94, 95])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2176 = frozenset([1, 7, 91, 92, 93, 94, 95])
    FOLLOW_LT_in_relationalExpressionNoIn2179 = frozenset([7, 91, 92, 93, 94, 95])
    FOLLOW_set_in_relationalExpressionNoIn2183 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_relationalExpressionNoIn2203 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2207 = frozenset([1, 7, 91, 92, 93, 94, 95])
    FOLLOW_additiveExpression_in_shiftExpression2220 = frozenset([1, 7, 96, 97, 98])
    FOLLOW_LT_in_shiftExpression2223 = frozenset([7, 96, 97, 98])
    FOLLOW_set_in_shiftExpression2227 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_shiftExpression2239 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_additiveExpression_in_shiftExpression2243 = frozenset([1, 7, 96, 97, 98])
    FOLLOW_multiplicativeExpression_in_additiveExpression2256 = frozenset([1, 7, 99, 100])
    FOLLOW_LT_in_additiveExpression2259 = frozenset([7, 99, 100])
    FOLLOW_set_in_additiveExpression2263 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_additiveExpression2271 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_multiplicativeExpression_in_additiveExpression2275 = frozenset([1, 7, 99, 100])
    FOLLOW_unaryExpression_in_multiplicativeExpression2288 = frozenset([1, 7, 101, 102, 103])
    FOLLOW_LT_in_multiplicativeExpression2291 = frozenset([7, 101, 102, 103])
    FOLLOW_set_in_multiplicativeExpression2295 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_multiplicativeExpression2307 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_unaryExpression_in_multiplicativeExpression2311 = frozenset([1, 7, 101, 102, 103])
    FOLLOW_postfixExpression_in_unaryExpression2324 = frozenset([1])
    FOLLOW_set_in_unaryExpression2329 = frozenset([8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_unaryExpression_in_unaryExpression2365 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression2377 = frozenset([1, 107, 108])
    FOLLOW_set_in_postfixExpression2379 = frozenset([1])
    FOLLOW_111_in_primaryExpression2397 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression2402 = frozenset([1])
    FOLLOW_literal_in_primaryExpression2407 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression2412 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression2417 = frozenset([1])
    FOLLOW_38_in_primaryExpression2422 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_primaryExpression2424 = frozenset([1])
    FOLLOW_expression_in_primaryExpression2428 = frozenset([7, 40])
    FOLLOW_LT_in_primaryExpression2430 = frozenset([1])
    FOLLOW_40_in_primaryExpression2434 = frozenset([1])
    FOLLOW_67_in_arrayLiteral2447 = frozenset([7, 8, 9, 10, 11, 37, 38, 39, 41, 52, 66, 67, 68, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_arrayLiteral2449 = frozenset([1])
    FOLLOW_assignmentExpression_in_arrayLiteral2453 = frozenset([7, 39, 68])
    FOLLOW_LT_in_arrayLiteral2457 = frozenset([7, 39])
    FOLLOW_39_in_arrayLiteral2461 = frozenset([7, 8, 9, 10, 11, 37, 38, 39, 41, 52, 66, 67, 68, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_arrayLiteral2464 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_arrayLiteral2468 = frozenset([7, 39, 68])
    FOLLOW_LT_in_arrayLiteral2474 = frozenset([1])
    FOLLOW_68_in_arrayLiteral2478 = frozenset([1])
    FOLLOW_41_in_objectLiteral2497 = frozenset([7, 8, 9, 11, 39, 42, 52, 112, 113])
    FOLLOW_LT_in_objectLiteral2499 = frozenset([7, 8, 9, 11, 39, 42, 52, 112, 113])
    FOLLOW_propertyNameAndValue_in_objectLiteral2502 = frozenset([7, 39, 42])
    FOLLOW_LT_in_objectLiteral2506 = frozenset([7, 39])
    FOLLOW_39_in_objectLiteral2509 = frozenset([7, 8, 9, 11, 52, 112, 113])
    FOLLOW_LT_in_objectLiteral2511 = frozenset([7, 8, 9, 11, 52, 112, 113])
    FOLLOW_propertyNameAndValue_in_objectLiteral2514 = frozenset([7, 39, 42])
    FOLLOW_LT_in_objectLiteral2518 = frozenset([7, 42])
    FOLLOW_42_in_objectLiteral2521 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue2545 = frozenset([7, 58])
    FOLLOW_LT_in_propertyNameAndValue2547 = frozenset([7, 58])
    FOLLOW_58_in_propertyNameAndValue2550 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_propertyNameAndValue2552 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_assignmentExpression_in_propertyNameAndValue2555 = frozenset([1])
    FOLLOW_112_in_propertyNameAndValue2573 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_113_in_propertyNameAndValue2575 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_LT_in_propertyNameAndValue2578 = frozenset([7, 11, 52, 112, 113])
    FOLLOW_identifier_in_propertyNameAndValue2581 = frozenset([7, 38])
    FOLLOW_LT_in_propertyNameAndValue2583 = frozenset([7, 38])
    FOLLOW_formalParameterList_in_propertyNameAndValue2586 = frozenset([7, 41])
    FOLLOW_LT_in_propertyNameAndValue2588 = frozenset([7, 41])
    FOLLOW_functionBody_in_propertyNameAndValue2591 = frozenset([1])
    FOLLOW_identifier_in_propertyName2622 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName2627 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName2632 = frozenset([1])
    FOLLOW_set_in_literal0 = frozenset([1])
    FOLLOW_102_in_regularExpressionLiteral2680 = frozenset([10])
    FOLLOW_RegularExpressionLiteral_in_regularExpressionLiteral2682 = frozenset([102])
    FOLLOW_102_in_regularExpressionLiteral2684 = frozenset([11])
    FOLLOW_Identifier_in_regularExpressionLiteral2686 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_LT_in_synpred486 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_sourceElement_in_synpred490 = frozenset([1])
    FOLLOW_functionDeclaration_in_synpred5104 = frozenset([1])
    FOLLOW_LT_in_synpred9165 = frozenset([1])
    FOLLOW_LT_in_synpred19249 = frozenset([1])
    FOLLOW_statementBlock_in_synpred22272 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred25287 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred32322 = frozenset([1])
    FOLLOW_LT_in_synpred35351 = frozenset([1])
    FOLLOW_LT_in_synpred62617 = frozenset([7, 48])
    FOLLOW_48_in_synpred62621 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_synpred62623 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 59, 62, 63, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_statement_in_synpred62627 = frozenset([1])
    FOLLOW_forStatement_in_synpred65651 = frozenset([1])
    FOLLOW_LT_in_synpred87841 = frozenset([1])
    FOLLOW_LT_in_synpred1221139 = frozenset([1])
    FOLLOW_LT_in_synpred1251164 = frozenset([1])
    FOLLOW_conditionalExpression_in_synpred1441356 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_synpred1471385 = frozenset([1])
    FOLLOW_callExpression_in_synpred1501414 = frozenset([1])
    FOLLOW_memberExpression_in_synpred1511431 = frozenset([1])
    FOLLOW_LT_in_synpred1581479 = frozenset([7, 67, 69])
    FOLLOW_memberExpressionSuffix_in_synpred1581483 = frozenset([1])
    FOLLOW_LT_in_synpred1621522 = frozenset([7, 38, 67, 69])
    FOLLOW_callExpressionSuffix_in_synpred1621526 = frozenset([1])
    FOLLOW_LT_in_synpred2602259 = frozenset([7, 99, 100])
    FOLLOW_set_in_synpred2602263 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_LT_in_synpred2602271 = frozenset([7, 8, 9, 10, 11, 37, 38, 41, 52, 66, 67, 99, 100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    FOLLOW_multiplicativeExpression_in_synpred2602275 = frozenset([1])
    FOLLOW_LT_in_synpred2842449 = frozenset([1])
    FOLLOW_LT_in_synpred2912499 = frozenset([1])

