# $ANTLR 3.0.1 /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g 2008-04-09 00:13:18

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
UnicodeDigit=36
LT=13
NumericLiteral=15
HexEscapeSequence=23
RegularExpressionChars=19
UnicodeEscapeSequence=24
IdentifierStart=33
LineComment=40
DoubleStringCharacter=20
DecimalDigit=28
DecimalLiteral=30
EOF=-1
PROP=9
HexDigit=29
Identifier=16
SingleStringCharacter=21
StringLiteral=14
RegularExpressionFirstChar=18
Comment=39
OBJ=8
HexIntegerLiteral=31
FUNC=6
SingleEscapeCharacter=25
NonEscapeCharacter=26
PROPREF=10
UnicodeLetter=35
ExponentPart=32
EscapeCharacter=27
WhiteSpace=41
CALL=5
CharacterEscapeSequence=22
VARDEF=11
VARDEFS=12
EscapeSequence=17
IdentifierPart=34
INDEXREF=7
UnicodeConnectorPunctuation=37
ANONYMOUS=4
UnicodeCombiningMark=38

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ANONYMOUS", "CALL", "FUNC", "INDEXREF", "OBJ", "PROP", "PROPREF", "VARDEF", 
    "VARDEFS", "LT", "StringLiteral", "NumericLiteral", "Identifier", "EscapeSequence", 
    "RegularExpressionFirstChar", "RegularExpressionChars", "DoubleStringCharacter", 
    "SingleStringCharacter", "CharacterEscapeSequence", "HexEscapeSequence", 
    "UnicodeEscapeSequence", "SingleEscapeCharacter", "NonEscapeCharacter", 
    "EscapeCharacter", "DecimalDigit", "HexDigit", "DecimalLiteral", "HexIntegerLiteral", 
    "ExponentPart", "IdentifierStart", "IdentifierPart", "UnicodeLetter", 
    "UnicodeDigit", "UnicodeConnectorPunctuation", "UnicodeCombiningMark", 
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
    "'set'", "'null'", "'true'", "'false'", "'#'"
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
        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
            )
        self.dfa37 = self.DFA37(
            self, 37,
            eot = self.DFA37_eot,
            eof = self.DFA37_eof,
            min = self.DFA37_min,
            max = self.DFA37_max,
            accept = self.DFA37_accept,
            special = self.DFA37_special,
            transition = self.DFA37_transition
            )
        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )
        self.dfa59 = self.DFA59(
            self, 59,
            eot = self.DFA59_eot,
            eof = self.DFA59_eof,
            min = self.DFA59_min,
            max = self.DFA59_max,
            accept = self.DFA59_accept,
            special = self.DFA59_special,
            transition = self.DFA59_transition
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
        self.dfa65 = self.DFA65(
            self, 65,
            eot = self.DFA65_eot,
            eof = self.DFA65_eof,
            min = self.DFA65_min,
            max = self.DFA65_max,
            accept = self.DFA65_accept,
            special = self.DFA65_special,
            transition = self.DFA65_transition
            )
        self.dfa94 = self.DFA94(
            self, 94,
            eot = self.DFA94_eot,
            eof = self.DFA94_eof,
            min = self.DFA94_min,
            max = self.DFA94_max,
            accept = self.DFA94_accept,
            special = self.DFA94_special,
            transition = self.DFA94_transition
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
        self.dfa110 = self.DFA110(
            self, 110,
            eot = self.DFA110_eot,
            eof = self.DFA110_eof,
            min = self.DFA110_min,
            max = self.DFA110_max,
            accept = self.DFA110_accept,
            special = self.DFA110_special,
            transition = self.DFA110_transition
            )
        self.dfa119 = self.DFA119(
            self, 119,
            eot = self.DFA119_eot,
            eof = self.DFA119_eof,
            min = self.DFA119_min,
            max = self.DFA119_max,
            accept = self.DFA119_accept,
            special = self.DFA119_special,
            transition = self.DFA119_transition
            )
        self.dfa122 = self.DFA122(
            self, 122,
            eot = self.DFA122_eot,
            eof = self.DFA122_eof,
            min = self.DFA122_min,
            max = self.DFA122_max,
            accept = self.DFA122_accept,
            special = self.DFA122_special,
            transition = self.DFA122_transition
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
        self.dfa155 = self.DFA155(
            self, 155,
            eot = self.DFA155_eot,
            eof = self.DFA155_eof,
            min = self.DFA155_min,
            max = self.DFA155_max,
            accept = self.DFA155_accept,
            special = self.DFA155_special,
            transition = self.DFA155_transition
            )
        self.dfa160 = self.DFA160(
            self, 160,
            eot = self.DFA160_eot,
            eof = self.DFA160_eof,
            min = self.DFA160_min,
            max = self.DFA160_max,
            accept = self.DFA160_accept,
            special = self.DFA160_special,
            transition = self.DFA160_transition
            )
        self.dfa163 = self.DFA163(
            self, 163,
            eot = self.DFA163_eot,
            eof = self.DFA163_eof,
            min = self.DFA163_min,
            max = self.DFA163_max,
            accept = self.DFA163_accept,
            special = self.DFA163_special,
            transition = self.DFA163_transition
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
        self.dfa172 = self.DFA172(
            self, 172,
            eot = self.DFA172_eot,
            eof = self.DFA172_eof,
            min = self.DFA172_min,
            max = self.DFA172_max,
            accept = self.DFA172_accept,
            special = self.DFA172_special,
            transition = self.DFA172_transition
            )
        self.dfa175 = self.DFA175(
            self, 175,
            eot = self.DFA175_eot,
            eof = self.DFA175_eof,
            min = self.DFA175_min,
            max = self.DFA175_max,
            accept = self.DFA175_accept,
            special = self.DFA175_special,
            transition = self.DFA175_transition
            )
        self.dfa178 = self.DFA178(
            self, 178,
            eot = self.DFA178_eot,
            eof = self.DFA178_eof,
            min = self.DFA178_min,
            max = self.DFA178_max,
            accept = self.DFA178_accept,
            special = self.DFA178_special,
            transition = self.DFA178_transition
            )
        self.dfa181 = self.DFA181(
            self, 181,
            eot = self.DFA181_eot,
            eof = self.DFA181_eof,
            min = self.DFA181_min,
            max = self.DFA181_max,
            accept = self.DFA181_accept,
            special = self.DFA181_special,
            transition = self.DFA181_transition
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
        self.dfa228 = self.DFA228(
            self, 228,
            eot = self.DFA228_eot,
            eof = self.DFA228_eof,
            min = self.DFA228_min,
            max = self.DFA228_max,
            accept = self.DFA228_accept,
            special = self.DFA228_special,
            transition = self.DFA228_transition
            )
        self.dfa240 = self.DFA240(
            self, 240,
            eot = self.DFA240_eot,
            eof = self.DFA240_eof,
            min = self.DFA240_min,
            max = self.DFA240_max,
            accept = self.DFA240_accept,
            special = self.DFA240_special,
            transition = self.DFA240_transition
            )




                
        self.adaptor = CommonTreeAdaptor()




    class program_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start program
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:29:1: program : ( LT )* sourceElements ( LT )* EOF ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:30:2: ( ( LT )* sourceElements ( LT )* EOF )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:30:4: ( LT )* sourceElements ( LT )* EOF
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:30:6: ( LT )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == LT) :
                        alt1 = 1


                    if alt1 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT1 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program84)
                        if self.failed:
                            return retval


                    else:
                        break #loop1


                self.following.append(self.FOLLOW_sourceElements_in_program88)
                sourceElements2 = self.sourceElements()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElements2.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:30:26: ( LT )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == LT) :
                        alt2 = 1


                    if alt2 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT3 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_program90)
                        if self.failed:
                            return retval


                    else:
                        break #loop2


                EOF4 = self.input.LT(1)
                self.match(self.input, EOF, self.FOLLOW_EOF_in_program94)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:33:1: sourceElements : sourceElement ( ( LT )* sourceElement )* ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:2: ( sourceElement ( ( LT )* sourceElement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:4: sourceElement ( ( LT )* sourceElement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_sourceElement_in_sourceElements107)
                sourceElement5 = self.sourceElement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, sourceElement5.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:18: ( ( LT )* sourceElement )*
                while True: #loop4
                    alt4 = 2
                    alt4 = self.dfa4.predict(self.input)
                    if alt4 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:19: ( LT )* sourceElement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:34:21: ( LT )*
                        while True: #loop3
                            alt3 = 2
                            LA3_0 = self.input.LA(1)

                            if (LA3_0 == LT) :
                                alt3 = 1


                            if alt3 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT6 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_sourceElements110)
                                if self.failed:
                                    return retval


                            else:
                                break #loop3


                        self.following.append(self.FOLLOW_sourceElement_in_sourceElements114)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:37:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:2: ( ( functionDeclaration )=> functionDeclaration | statement )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 42) :
                    LA5_1 = self.input.LA(2)

                    if (self.synpred5()) :
                        alt5 = 1
                    elif (True) :
                        alt5 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("37:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 1, self.input)

                        raise nvae

                elif ((StringLiteral <= LA5_0 <= Identifier) or LA5_0 == 43 or LA5_0 == 46 or (48 <= LA5_0 <= 50) or LA5_0 == 52 or (54 <= LA5_0 <= 57) or (59 <= LA5_0 <= 62) or LA5_0 == 64 or (67 <= LA5_0 <= 68) or (71 <= LA5_0 <= 72) or (104 <= LA5_0 <= 105) or LA5_0 == 107 or (109 <= LA5_0 <= 121)) :
                    alt5 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("37:1: sourceElement : ( ( functionDeclaration )=> functionDeclaration | statement );", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:4: ( functionDeclaration )=> functionDeclaration
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_functionDeclaration_in_sourceElement133)
                    functionDeclaration8 = self.functionDeclaration()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionDeclaration8.tree)


                elif alt5 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:39:4: statement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statement_in_sourceElement138)
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:43:1: functionDeclaration : 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) ;
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

        statementBlock16 = None


        string_literal10_tree = None
        LT11_tree = None
        LT13_tree = None
        LT15_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 4):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                string_literal10 = self.input.LT(1)
                self.match(self.input, 42, self.FOLLOW_42_in_functionDeclaration151)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_42.add(string_literal10)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:15: ( LT )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LT) :
                        alt6 = 1


                    if alt6 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT11 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration153)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT11)


                    else:
                        break #loop6


                self.following.append(self.FOLLOW_identifier_in_functionDeclaration156)
                identifier12 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier12.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:30: ( LT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == LT) :
                        alt7 = 1


                    if alt7 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT13 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration158)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT13)


                    else:
                        break #loop7


                self.following.append(self.FOLLOW_formalParameterList_in_functionDeclaration161)
                formalParameterList14 = self.formalParameterList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_formalParameterList.add(formalParameterList14.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:44:54: ( LT )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == LT) :
                        alt8 = 1


                    if alt8 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT15 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_functionDeclaration163)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT15)


                    else:
                        break #loop8


                self.following.append(self.FOLLOW_statementBlock_in_functionDeclaration166)
                statementBlock16 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_statementBlock.add(statementBlock16.tree)
                # AST Rewrite
                # elements: identifier, formalParameterList, statementBlock
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
                    # 45:3: -> ^( FUNC identifier formalParameterList statementBlock )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:45:6: ^( FUNC identifier formalParameterList statementBlock )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:48:1: functionExpression : ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS formalParameterList statementBlock ) );
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

        statementBlock23 = None

        formalParameterList26 = None

        statementBlock28 = None


        string_literal17_tree = None
        LT18_tree = None
        LT20_tree = None
        LT22_tree = None
        string_literal24_tree = None
        LT25_tree = None
        LT27_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_42 = RewriteRuleTokenStream(self.adaptor, "token 42")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 5):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:2: ( 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC identifier formalParameterList statementBlock ) | 'function' ( LT )* formalParameterList ( LT )* statementBlock -> ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                alt14 = 2
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:4: 'function' ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                    string_literal17 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_functionExpression192)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_42.add(string_literal17)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:15: ( LT )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == LT) :
                            alt9 = 1


                        if alt9 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT18 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression194)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT18)


                        else:
                            break #loop9


                    self.following.append(self.FOLLOW_identifier_in_functionExpression197)
                    identifier19 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier19.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:30: ( LT )*
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == LT) :
                            alt10 = 1


                        if alt10 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT20 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression199)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT20)


                        else:
                            break #loop10


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression202)
                    formalParameterList21 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList21.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:49:54: ( LT )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == LT) :
                            alt11 = 1


                        if alt11 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT22 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression204)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT22)


                        else:
                            break #loop11


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression207)
                    statementBlock23 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock23.tree)
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
                        # 50:3: -> ^( FUNC identifier formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:50:6: ^( FUNC identifier formalParameterList statementBlock )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_formalParameterList.next())
                        self.adaptor.addChild(root_1, stream_statementBlock.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt14 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:4: 'function' ( LT )* formalParameterList ( LT )* statementBlock
                    string_literal24 = self.input.LT(1)
                    self.match(self.input, 42, self.FOLLOW_42_in_functionExpression226)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_42.add(string_literal24)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:15: ( LT )*
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == LT) :
                            alt12 = 1


                        if alt12 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT25 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression228)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT25)


                        else:
                            break #loop12


                    self.following.append(self.FOLLOW_formalParameterList_in_functionExpression231)
                    formalParameterList26 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList26.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:51:39: ( LT )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == LT) :
                            alt13 = 1


                        if alt13 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT27 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_functionExpression233)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT27)


                        else:
                            break #loop13


                    self.following.append(self.FOLLOW_statementBlock_in_functionExpression236)
                    statementBlock28 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock28.tree)
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
                        # 52:3: -> ^( FUNC ANONYMOUS formalParameterList statementBlock )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:52:6: ^( FUNC ANONYMOUS formalParameterList statementBlock )
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
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:55:1: formalParameterList : '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' ;
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

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:2: ( '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:4: '(' ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal29 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_formalParameterList262)
                if self.failed:
                    return retval

                char_literal29_tree = self.adaptor.createWithPayload(char_literal29)
                self.adaptor.addChild(root_0, char_literal29_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:8: ( ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )* )?
                alt19 = 2
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:9: ( LT )* identifier ( ( LT )* ',' ( LT )* identifier )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:11: ( LT )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == LT) :
                            alt15 = 1


                        if alt15 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT30 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList265)
                            if self.failed:
                                return retval


                        else:
                            break #loop15


                    self.following.append(self.FOLLOW_identifier_in_formalParameterList269)
                    identifier31 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier31.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:25: ( ( LT )* ',' ( LT )* identifier )*
                    while True: #loop18
                        alt18 = 2
                        alt18 = self.dfa18.predict(self.input)
                        if alt18 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:26: ( LT )* ',' ( LT )* identifier
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:28: ( LT )*
                            while True: #loop16
                                alt16 = 2
                                LA16_0 = self.input.LA(1)

                                if (LA16_0 == LT) :
                                    alt16 = 1


                                if alt16 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT32 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList272)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop16


                            char_literal33 = self.input.LT(1)
                            self.match(self.input, 44, self.FOLLOW_44_in_formalParameterList276)
                            if self.failed:
                                return retval

                            char_literal33_tree = self.adaptor.createWithPayload(char_literal33)
                            self.adaptor.addChild(root_0, char_literal33_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:37: ( LT )*
                            while True: #loop17
                                alt17 = 2
                                LA17_0 = self.input.LA(1)

                                if (LA17_0 == LT) :
                                    alt17 = 1


                                if alt17 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT34 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList278)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop17


                            self.following.append(self.FOLLOW_identifier_in_formalParameterList282)
                            identifier35 = self.identifier()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, identifier35.tree)


                        else:
                            break #loop18





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:56:57: ( LT )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == LT) :
                        alt20 = 1


                    if alt20 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT36 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_formalParameterList288)
                        if self.failed:
                            return retval


                    else:
                        break #loop20


                char_literal37 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_formalParameterList292)
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

    class statement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:60:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 7):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:2: ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement )
                alt21 = 14
                LA21 = self.input.LA(1)
                if LA21 == 46:
                    LA21_1 = self.input.LA(2)

                    if (self.synpred21()) :
                        alt21 = 1
                    elif (self.synpred24()) :
                        alt21 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("60:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 21, 1, self.input)

                        raise nvae

                elif LA21 == 48 or LA21 == 49:
                    alt21 = 2
                elif LA21 == 50:
                    alt21 = 3
                elif LA21 == StringLiteral or LA21 == NumericLiteral or LA21 == 42 or LA21 == 43 or LA21 == 71 or LA21 == 72 or LA21 == 104 or LA21 == 105 or LA21 == 107 or LA21 == 109 or LA21 == 110 or LA21 == 111 or LA21 == 112 or LA21 == 113 or LA21 == 114 or LA21 == 115 or LA21 == 116 or LA21 == 119 or LA21 == 120 or LA21 == 121:
                    alt21 = 4
                elif LA21 == Identifier or LA21 == 57 or LA21 == 117 or LA21 == 118:
                    LA21_6 = self.input.LA(2)

                    if (self.synpred24()) :
                        alt21 = 4
                    elif (self.synpred31()) :
                        alt21 = 11
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("60:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 21, 6, self.input)

                        raise nvae

                elif LA21 == 52:
                    alt21 = 5
                elif LA21 == 54 or LA21 == 55 or LA21 == 56:
                    alt21 = 6
                elif LA21 == 59:
                    alt21 = 7
                elif LA21 == 60:
                    alt21 = 8
                elif LA21 == 61:
                    alt21 = 9
                elif LA21 == 62:
                    alt21 = 10
                elif LA21 == 64:
                    alt21 = 12
                elif LA21 == 67:
                    alt21 = 13
                elif LA21 == 68:
                    alt21 = 14
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("60:1: statement : ( statementBlock | variableStatement | emptyStatement | expressionStatement | ifStatement | iterationStatement | continueStatement | breakStatement | returnStatement | withStatement | labelledStatement | switchStatement | throwStatement | tryStatement );", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:4: statementBlock
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_statementBlock_in_statement304)
                    statementBlock38 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementBlock38.tree)


                elif alt21 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:62:4: variableStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_variableStatement_in_statement309)
                    variableStatement39 = self.variableStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, variableStatement39.tree)


                elif alt21 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:63:4: emptyStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_emptyStatement_in_statement314)
                    emptyStatement40 = self.emptyStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, emptyStatement40.tree)


                elif alt21 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: expressionStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionStatement_in_statement319)
                    expressionStatement41 = self.expressionStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionStatement41.tree)


                elif alt21 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:65:4: ifStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_ifStatement_in_statement324)
                    ifStatement42 = self.ifStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, ifStatement42.tree)


                elif alt21 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:66:4: iterationStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_iterationStatement_in_statement329)
                    iterationStatement43 = self.iterationStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, iterationStatement43.tree)


                elif alt21 == 7:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:67:4: continueStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_continueStatement_in_statement334)
                    continueStatement44 = self.continueStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, continueStatement44.tree)


                elif alt21 == 8:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:68:4: breakStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_breakStatement_in_statement339)
                    breakStatement45 = self.breakStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, breakStatement45.tree)


                elif alt21 == 9:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:69:4: returnStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_returnStatement_in_statement344)
                    returnStatement46 = self.returnStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, returnStatement46.tree)


                elif alt21 == 10:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:70:4: withStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_withStatement_in_statement349)
                    withStatement47 = self.withStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, withStatement47.tree)


                elif alt21 == 11:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:71:4: labelledStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_labelledStatement_in_statement354)
                    labelledStatement48 = self.labelledStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, labelledStatement48.tree)


                elif alt21 == 12:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:72:4: switchStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_switchStatement_in_statement359)
                    switchStatement49 = self.switchStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, switchStatement49.tree)


                elif alt21 == 13:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:73:4: throwStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_throwStatement_in_statement364)
                    throwStatement50 = self.throwStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, throwStatement50.tree)


                elif alt21 == 14:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:74:4: tryStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_tryStatement_in_statement369)
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
                self.memoize(self.input, 7, statement_StartIndex)

            pass

        return retval

    # $ANTLR end statement

    class statementBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:77:1: statementBlock : '{' ( LT )* ( statementList )? ( LT )* '}' ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 8):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:2: ( '{' ( LT )* ( statementList )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:4: '{' ( LT )* ( statementList )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal52 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_statementBlock381)
                if self.failed:
                    return retval

                char_literal52_tree = self.adaptor.createWithPayload(char_literal52)
                self.adaptor.addChild(root_0, char_literal52_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:10: ( LT )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == LT) :
                        LA22_2 = self.input.LA(2)

                        if (self.synpred34()) :
                            alt22 = 1




                    if alt22 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT53 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock383)
                        if self.failed:
                            return retval


                    else:
                        break #loop22


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:13: ( statementList )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((StringLiteral <= LA23_0 <= Identifier) or (42 <= LA23_0 <= 43) or LA23_0 == 46 or (48 <= LA23_0 <= 50) or LA23_0 == 52 or (54 <= LA23_0 <= 57) or (59 <= LA23_0 <= 62) or LA23_0 == 64 or (67 <= LA23_0 <= 68) or (71 <= LA23_0 <= 72) or (104 <= LA23_0 <= 105) or LA23_0 == 107 or (109 <= LA23_0 <= 121)) :
                    alt23 = 1
                if alt23 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_statementBlock387)
                    statementList54 = self.statementList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, statementList54.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:30: ( LT )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == LT) :
                        alt24 = 1


                    if alt24 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT55 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_statementBlock390)
                        if self.failed:
                            return retval


                    else:
                        break #loop24


                char_literal56 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_statementBlock394)
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
                self.memoize(self.input, 8, statementBlock_StartIndex)

            pass

        return retval

    # $ANTLR end statementBlock

    class statementList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start statementList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:81:1: statementList : statement ( ( LT )* statement )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 9):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:2: ( statement ( ( LT )* statement )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:4: statement ( ( LT )* statement )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_statement_in_statementList406)
                statement57 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement57.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:14: ( ( LT )* statement )*
                while True: #loop26
                    alt26 = 2
                    alt26 = self.dfa26.predict(self.input)
                    if alt26 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:15: ( LT )* statement
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:82:17: ( LT )*
                        while True: #loop25
                            alt25 = 2
                            LA25_0 = self.input.LA(1)

                            if (LA25_0 == LT) :
                                alt25 = 1


                            if alt25 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT58 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_statementList409)
                                if self.failed:
                                    return retval


                            else:
                                break #loop25


                        self.following.append(self.FOLLOW_statement_in_statementList413)
                        statement59 = self.statement()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, statement59.tree)


                    else:
                        break #loop26





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 9, statementList_StartIndex)

            pass

        return retval

    # $ANTLR end statementList

    class variableStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:85:1: variableStatement : (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) ;
    def variableStatement(self, ):

        retval = self.variableStatement_return()
        retval.start = self.input.LT(1)
        variableStatement_StartIndex = self.input.index()
        root_0 = None

        mod = None
        LT60 = None
        LT62 = None
        char_literal63 = None
        variableDeclarationList61 = None


        mod_tree = None
        LT60_tree = None
        LT62_tree = None
        char_literal63_tree = None
        stream_49 = RewriteRuleTokenStream(self.adaptor, "token 49")
        stream_48 = RewriteRuleTokenStream(self.adaptor, "token 48")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_50 = RewriteRuleTokenStream(self.adaptor, "token 50")
        stream_variableDeclarationList = RewriteRuleSubtreeStream(self.adaptor, "rule variableDeclarationList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 10):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:2: ( (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' ) -> ^( VARDEFS $mod variableDeclarationList ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:4: (mod= 'var' | mod= 'const' ) ( LT )* variableDeclarationList ( LT | ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:4: (mod= 'var' | mod= 'const' )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == 48) :
                    alt27 = 1
                elif (LA27_0 == 49) :
                    alt27 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("86:4: (mod= 'var' | mod= 'const' )", 27, 0, self.input)

                    raise nvae

                if alt27 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:5: mod= 'var'
                    mod = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_variableStatement430)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_48.add(mod)


                elif alt27 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:15: mod= 'const'
                    mod = self.input.LT(1)
                    self.match(self.input, 49, self.FOLLOW_49_in_variableStatement434)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_49.add(mod)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:28: ( LT )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == LT) :
                        alt28 = 1


                    if alt28 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT60 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement437)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT60)


                    else:
                        break #loop28


                self.following.append(self.FOLLOW_variableDeclarationList_in_variableStatement440)
                variableDeclarationList61 = self.variableDeclarationList()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_variableDeclarationList.add(variableDeclarationList61.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:56: ( LT | ';' )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == LT) :
                    alt29 = 1
                elif (LA29_0 == 50) :
                    alt29 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("86:56: ( LT | ';' )", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:57: LT
                    LT62 = self.input.LT(1)
                    self.match(self.input, LT, self.FOLLOW_LT_in_variableStatement443)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_LT.add(LT62)


                elif alt29 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:86:62: ';'
                    char_literal63 = self.input.LT(1)
                    self.match(self.input, 50, self.FOLLOW_50_in_variableStatement447)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_50.add(char_literal63)



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
                    # 87:3: -> ^( VARDEFS $mod variableDeclarationList )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:87:6: ^( VARDEFS $mod variableDeclarationList )
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
                self.memoize(self.input, 10, variableStatement_StartIndex)

            pass

        return retval

    # $ANTLR end variableStatement

    class variableDeclarationList_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationList
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:90:1: variableDeclarationList : variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 11):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:2: ( variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:4: variableDeclaration ( ( LT )* ',' ( LT )* variableDeclaration )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList472)
                variableDeclaration64 = self.variableDeclaration()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclaration64.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:24: ( ( LT )* ',' ( LT )* variableDeclaration )*
                while True: #loop32
                    alt32 = 2
                    alt32 = self.dfa32.predict(self.input)
                    if alt32 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:25: ( LT )* ',' ( LT )* variableDeclaration
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:27: ( LT )*
                        while True: #loop30
                            alt30 = 2
                            LA30_0 = self.input.LA(1)

                            if (LA30_0 == LT) :
                                alt30 = 1


                            if alt30 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT65 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList475)
                                if self.failed:
                                    return retval


                            else:
                                break #loop30


                        char_literal66 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_variableDeclarationList479)
                        if self.failed:
                            return retval

                        char_literal66_tree = self.adaptor.createWithPayload(char_literal66)
                        self.adaptor.addChild(root_0, char_literal66_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:91:36: ( LT )*
                        while True: #loop31
                            alt31 = 2
                            LA31_0 = self.input.LA(1)

                            if (LA31_0 == LT) :
                                alt31 = 1


                            if alt31 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT67 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationList481)
                                if self.failed:
                                    return retval


                            else:
                                break #loop31


                        self.following.append(self.FOLLOW_variableDeclaration_in_variableDeclarationList485)
                        variableDeclaration68 = self.variableDeclaration()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclaration68.tree)


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
            if self.backtracking > 0:
                self.memoize(self.input, 11, variableDeclarationList_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationList

    class variableDeclarationListNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationListNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:94:1: variableDeclarationListNoIn : variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 12):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:2: ( variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:4: variableDeclarationNoIn ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn499)
                variableDeclarationNoIn69 = self.variableDeclarationNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, variableDeclarationNoIn69.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:28: ( ( LT )* ',' ( LT )* variableDeclarationNoIn )*
                while True: #loop35
                    alt35 = 2
                    alt35 = self.dfa35.predict(self.input)
                    if alt35 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:29: ( LT )* ',' ( LT )* variableDeclarationNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:31: ( LT )*
                        while True: #loop33
                            alt33 = 2
                            LA33_0 = self.input.LA(1)

                            if (LA33_0 == LT) :
                                alt33 = 1


                            if alt33 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT70 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn502)
                                if self.failed:
                                    return retval


                            else:
                                break #loop33


                        char_literal71 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_variableDeclarationListNoIn506)
                        if self.failed:
                            return retval

                        char_literal71_tree = self.adaptor.createWithPayload(char_literal71)
                        self.adaptor.addChild(root_0, char_literal71_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:95:40: ( LT )*
                        while True: #loop34
                            alt34 = 2
                            LA34_0 = self.input.LA(1)

                            if (LA34_0 == LT) :
                                alt34 = 1


                            if alt34 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT72 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationListNoIn508)
                                if self.failed:
                                    return retval


                            else:
                                break #loop34


                        self.following.append(self.FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn512)
                        variableDeclarationNoIn73 = self.variableDeclarationNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, variableDeclarationNoIn73.tree)


                    else:
                        break #loop35





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 12, variableDeclarationListNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationListNoIn

    class variableDeclaration_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclaration
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:98:1: variableDeclaration : identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) ;
    def variableDeclaration(self, ):

        retval = self.variableDeclaration_return()
        retval.start = self.input.LT(1)
        variableDeclaration_StartIndex = self.input.index()
        root_0 = None

        LT75 = None
        identifier74 = None

        initialiser76 = None


        LT75_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiser = RewriteRuleSubtreeStream(self.adaptor, "rule initialiser")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 13):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:2: ( identifier ( ( LT )* initialiser )? -> ^( VARDEF identifier ( initialiser )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:4: identifier ( ( LT )* initialiser )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclaration526)
                identifier74 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier74.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:15: ( ( LT )* initialiser )?
                alt37 = 2
                alt37 = self.dfa37.predict(self.input)
                if alt37 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:16: ( LT )* initialiser
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:99:16: ( LT )*
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == LT) :
                            alt36 = 1


                        if alt36 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT75 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclaration529)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT75)


                        else:
                            break #loop36


                    self.following.append(self.FOLLOW_initialiser_in_variableDeclaration532)
                    initialiser76 = self.initialiser()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiser.add(initialiser76.tree)



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
                    # 100:3: -> ^( VARDEF identifier ( initialiser )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:100:6: ^( VARDEF identifier ( initialiser )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:100:26: ( initialiser )?
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
                self.memoize(self.input, 13, variableDeclaration_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclaration

    class variableDeclarationNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start variableDeclarationNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:103:1: variableDeclarationNoIn : identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) ;
    def variableDeclarationNoIn(self, ):

        retval = self.variableDeclarationNoIn_return()
        retval.start = self.input.LT(1)
        variableDeclarationNoIn_StartIndex = self.input.index()
        root_0 = None

        LT78 = None
        identifier77 = None

        initialiserNoIn79 = None


        LT78_tree = None
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_initialiserNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule initialiserNoIn")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 14):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:2: ( identifier ( ( LT )* initialiserNoIn )? -> ^( VARDEF identifier ( initialiserNoIn )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:4: identifier ( ( LT )* initialiserNoIn )?
                self.following.append(self.FOLLOW_identifier_in_variableDeclarationNoIn559)
                identifier77 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier77.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:15: ( ( LT )* initialiserNoIn )?
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:16: ( LT )* initialiserNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:104:16: ( LT )*
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == LT) :
                            alt38 = 1


                        if alt38 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT78 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_variableDeclarationNoIn562)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT78)


                        else:
                            break #loop38


                    self.following.append(self.FOLLOW_initialiserNoIn_in_variableDeclarationNoIn565)
                    initialiserNoIn79 = self.initialiserNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_initialiserNoIn.add(initialiserNoIn79.tree)



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
                    # 105:3: -> ^( VARDEF identifier ( initialiserNoIn )? )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:6: ^( VARDEF identifier ( initialiserNoIn )? )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(VARDEF, "VARDEF"), root_1)

                    self.adaptor.addChild(root_1, stream_identifier.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:105:26: ( initialiserNoIn )?
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
                self.memoize(self.input, 14, variableDeclarationNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end variableDeclarationNoIn

    class initialiser_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiser
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:108:1: initialiser : '=' ( LT )* assignmentExpression -> assignmentExpression ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 15):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:2: ( '=' ( LT )* assignmentExpression -> assignmentExpression )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:4: '=' ( LT )* assignmentExpression
                char_literal80 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_initialiser592)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal80)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:109:8: ( LT )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == LT) :
                        alt40 = 1


                    if alt40 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT81 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiser594)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT81)


                    else:
                        break #loop40


                self.following.append(self.FOLLOW_assignmentExpression_in_initialiser597)
                assignmentExpression82 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpression.add(assignmentExpression82.tree)
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
                    # 110:3: -> assignmentExpression
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
                self.memoize(self.input, 15, initialiser_StartIndex)

            pass

        return retval

    # $ANTLR end initialiser

    class initialiserNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start initialiserNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:113:1: initialiserNoIn : '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_51 = RewriteRuleTokenStream(self.adaptor, "token 51")
        stream_assignmentExpressionNoIn = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpressionNoIn")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 16):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:114:2: ( '=' ( LT )* assignmentExpressionNoIn -> assignmentExpressionNoIn )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:114:4: '=' ( LT )* assignmentExpressionNoIn
                char_literal83 = self.input.LT(1)
                self.match(self.input, 51, self.FOLLOW_51_in_initialiserNoIn615)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_51.add(char_literal83)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:114:8: ( LT )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == LT) :
                        alt41 = 1


                    if alt41 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT84 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_initialiserNoIn617)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT84)


                    else:
                        break #loop41


                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn620)
                assignmentExpressionNoIn85 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_assignmentExpressionNoIn.add(assignmentExpressionNoIn85.tree)
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
                    # 115:3: -> assignmentExpressionNoIn
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
                self.memoize(self.input, 16, initialiserNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end initialiserNoIn

    class emptyStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start emptyStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:118:1: emptyStatement : ';' ;
    def emptyStatement(self, ):

        retval = self.emptyStatement_return()
        retval.start = self.input.LT(1)
        emptyStatement_StartIndex = self.input.index()
        root_0 = None

        char_literal86 = None

        char_literal86_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 17):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:119:2: ( ';' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:119:4: ';'
                root_0 = self.adaptor.nil()

                char_literal86 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_emptyStatement638)
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
                self.memoize(self.input, 17, emptyStatement_StartIndex)

            pass

        return retval

    # $ANTLR end emptyStatement

    class expressionStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:122:1: expressionStatement : expression ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 18):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:2: ( expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:123:4: expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_expression_in_expressionStatement650)
                expression87 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression87.tree)
                set88 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_expressionStatement652
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
                self.memoize(self.input, 18, expressionStatement_StartIndex)

            pass

        return retval

    # $ANTLR end expressionStatement

    class ifStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start ifStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:126:1: ifStatement : 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 19):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:2: ( 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:4: 'if' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ( ( LT )* 'else' ( LT )* statement )?
                root_0 = self.adaptor.nil()

                string_literal89 = self.input.LT(1)
                self.match(self.input, 52, self.FOLLOW_52_in_ifStatement671)
                if self.failed:
                    return retval

                string_literal89_tree = self.adaptor.createWithPayload(string_literal89)
                self.adaptor.addChild(root_0, string_literal89_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:11: ( LT )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == LT) :
                        alt42 = 1


                    if alt42 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT90 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement673)
                        if self.failed:
                            return retval


                    else:
                        break #loop42


                char_literal91 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_ifStatement677)
                if self.failed:
                    return retval

                char_literal91_tree = self.adaptor.createWithPayload(char_literal91)
                self.adaptor.addChild(root_0, char_literal91_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:20: ( LT )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == LT) :
                        alt43 = 1


                    if alt43 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT92 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement679)
                        if self.failed:
                            return retval


                    else:
                        break #loop43


                self.following.append(self.FOLLOW_expression_in_ifStatement683)
                expression93 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression93.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:36: ( LT )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == LT) :
                        alt44 = 1


                    if alt44 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT94 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement685)
                        if self.failed:
                            return retval


                    else:
                        break #loop44


                char_literal95 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_ifStatement689)
                if self.failed:
                    return retval

                char_literal95_tree = self.adaptor.createWithPayload(char_literal95)
                self.adaptor.addChild(root_0, char_literal95_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:45: ( LT )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT96 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement691)
                        if self.failed:
                            return retval


                    else:
                        break #loop45


                self.following.append(self.FOLLOW_statement_in_ifStatement695)
                statement97 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement97.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:58: ( ( LT )* 'else' ( LT )* statement )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == LT) :
                    LA48_1 = self.input.LA(2)

                    if (self.synpred61()) :
                        alt48 = 1
                elif (LA48_0 == 53) :
                    LA48_2 = self.input.LA(2)

                    if (self.synpred61()) :
                        alt48 = 1
                if alt48 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:59: ( LT )* 'else' ( LT )* statement
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:61: ( LT )*
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == LT) :
                            alt46 = 1


                        if alt46 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT98 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement698)
                            if self.failed:
                                return retval


                        else:
                            break #loop46


                    string_literal99 = self.input.LT(1)
                    self.match(self.input, 53, self.FOLLOW_53_in_ifStatement702)
                    if self.failed:
                        return retval

                    string_literal99_tree = self.adaptor.createWithPayload(string_literal99)
                    self.adaptor.addChild(root_0, string_literal99_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:73: ( LT )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == LT) :
                            alt47 = 1


                        if alt47 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT100 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_ifStatement704)
                            if self.failed:
                                return retval


                        else:
                            break #loop47


                    self.following.append(self.FOLLOW_statement_in_ifStatement708)
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
                self.memoize(self.input, 19, ifStatement_StartIndex)

            pass

        return retval

    # $ANTLR end ifStatement

    class iterationStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start iterationStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:130:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 20):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:2: ( doWhileStatement | whileStatement | forStatement | forInStatement )
                alt49 = 4
                LA49 = self.input.LA(1)
                if LA49 == 54:
                    alt49 = 1
                elif LA49 == 55:
                    alt49 = 2
                elif LA49 == 56:
                    LA49_3 = self.input.LA(2)

                    if (self.synpred64()) :
                        alt49 = 3
                    elif (True) :
                        alt49 = 4
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("130:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 49, 3, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("130:1: iterationStatement : ( doWhileStatement | whileStatement | forStatement | forInStatement );", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:131:4: doWhileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_doWhileStatement_in_iterationStatement722)
                    doWhileStatement102 = self.doWhileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, doWhileStatement102.tree)


                elif alt49 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:132:4: whileStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_whileStatement_in_iterationStatement727)
                    whileStatement103 = self.whileStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, whileStatement103.tree)


                elif alt49 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:4: forStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forStatement_in_iterationStatement732)
                    forStatement104 = self.forStatement()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatement104.tree)


                elif alt49 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:134:4: forInStatement
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_forInStatement_in_iterationStatement737)
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
                self.memoize(self.input, 20, iterationStatement_StartIndex)

            pass

        return retval

    # $ANTLR end iterationStatement

    class doWhileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start doWhileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:137:1: doWhileStatement : 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 21):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:2: ( 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:4: 'do' ( LT )* statement ( LT )* 'while' ( LT )* '(' expression ')' ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal106 = self.input.LT(1)
                self.match(self.input, 54, self.FOLLOW_54_in_doWhileStatement749)
                if self.failed:
                    return retval

                string_literal106_tree = self.adaptor.createWithPayload(string_literal106)
                self.adaptor.addChild(root_0, string_literal106_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:11: ( LT )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == LT) :
                        alt50 = 1


                    if alt50 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT107 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement751)
                        if self.failed:
                            return retval


                    else:
                        break #loop50


                self.following.append(self.FOLLOW_statement_in_doWhileStatement755)
                statement108 = self.statement()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statement108.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:26: ( LT )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == LT) :
                        alt51 = 1


                    if alt51 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT109 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement757)
                        if self.failed:
                            return retval


                    else:
                        break #loop51


                string_literal110 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_doWhileStatement761)
                if self.failed:
                    return retval

                string_literal110_tree = self.adaptor.createWithPayload(string_literal110)
                self.adaptor.addChild(root_0, string_literal110_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:138:39: ( LT )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == LT) :
                        alt52 = 1


                    if alt52 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT111 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_doWhileStatement763)
                        if self.failed:
                            return retval


                    else:
                        break #loop52


                char_literal112 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_doWhileStatement767)
                if self.failed:
                    return retval

                char_literal112_tree = self.adaptor.createWithPayload(char_literal112)
                self.adaptor.addChild(root_0, char_literal112_tree)

                self.following.append(self.FOLLOW_expression_in_doWhileStatement769)
                expression113 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression113.tree)
                char_literal114 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_doWhileStatement771)
                if self.failed:
                    return retval

                char_literal114_tree = self.adaptor.createWithPayload(char_literal114)
                self.adaptor.addChild(root_0, char_literal114_tree)

                set115 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_doWhileStatement773
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
                self.memoize(self.input, 21, doWhileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end doWhileStatement

    class whileStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start whileStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:141:1: whileStatement : 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 22):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:2: ( 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:4: 'while' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal116 = self.input.LT(1)
                self.match(self.input, 55, self.FOLLOW_55_in_whileStatement792)
                if self.failed:
                    return retval

                string_literal116_tree = self.adaptor.createWithPayload(string_literal116)
                self.adaptor.addChild(root_0, string_literal116_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:14: ( LT )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == LT) :
                        alt53 = 1


                    if alt53 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT117 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement794)
                        if self.failed:
                            return retval


                    else:
                        break #loop53


                char_literal118 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_whileStatement798)
                if self.failed:
                    return retval

                char_literal118_tree = self.adaptor.createWithPayload(char_literal118)
                self.adaptor.addChild(root_0, char_literal118_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:23: ( LT )*
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == LT) :
                        alt54 = 1


                    if alt54 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT119 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement800)
                        if self.failed:
                            return retval


                    else:
                        break #loop54


                self.following.append(self.FOLLOW_expression_in_whileStatement804)
                expression120 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression120.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:39: ( LT )*
                while True: #loop55
                    alt55 = 2
                    LA55_0 = self.input.LA(1)

                    if (LA55_0 == LT) :
                        alt55 = 1


                    if alt55 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT121 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement806)
                        if self.failed:
                            return retval


                    else:
                        break #loop55


                char_literal122 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_whileStatement810)
                if self.failed:
                    return retval

                char_literal122_tree = self.adaptor.createWithPayload(char_literal122)
                self.adaptor.addChild(root_0, char_literal122_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:142:48: ( LT )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == LT) :
                        alt56 = 1


                    if alt56 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT123 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_whileStatement812)
                        if self.failed:
                            return retval


                    else:
                        break #loop56


                self.following.append(self.FOLLOW_statement_in_whileStatement816)
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
                self.memoize(self.input, 22, whileStatement_StartIndex)

            pass

        return retval

    # $ANTLR end whileStatement

    class forStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:145:1: forStatement : 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 23):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:2: ( 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:4: 'for' ( LT )* '(' ( ( LT )* forStatementInitialiserPart )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ';' ( ( LT )* expression )? ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal125 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_forStatement828)
                if self.failed:
                    return retval

                string_literal125_tree = self.adaptor.createWithPayload(string_literal125)
                self.adaptor.addChild(root_0, string_literal125_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:12: ( LT )*
                while True: #loop57
                    alt57 = 2
                    LA57_0 = self.input.LA(1)

                    if (LA57_0 == LT) :
                        alt57 = 1


                    if alt57 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT126 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement830)
                        if self.failed:
                            return retval


                    else:
                        break #loop57


                char_literal127 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_forStatement834)
                if self.failed:
                    return retval

                char_literal127_tree = self.adaptor.createWithPayload(char_literal127)
                self.adaptor.addChild(root_0, char_literal127_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:19: ( ( LT )* forStatementInitialiserPart )?
                alt59 = 2
                alt59 = self.dfa59.predict(self.input)
                if alt59 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:20: ( LT )* forStatementInitialiserPart
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:22: ( LT )*
                    while True: #loop58
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if (LA58_0 == LT) :
                            alt58 = 1


                        if alt58 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT128 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement837)
                            if self.failed:
                                return retval


                        else:
                            break #loop58


                    self.following.append(self.FOLLOW_forStatementInitialiserPart_in_forStatement841)
                    forStatementInitialiserPart129 = self.forStatementInitialiserPart()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, forStatementInitialiserPart129.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:57: ( LT )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == LT) :
                        alt60 = 1


                    if alt60 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT130 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement845)
                        if self.failed:
                            return retval


                    else:
                        break #loop60


                char_literal131 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_forStatement849)
                if self.failed:
                    return retval

                char_literal131_tree = self.adaptor.createWithPayload(char_literal131)
                self.adaptor.addChild(root_0, char_literal131_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:64: ( ( LT )* expression )?
                alt62 = 2
                alt62 = self.dfa62.predict(self.input)
                if alt62 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:65: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:67: ( LT )*
                    while True: #loop61
                        alt61 = 2
                        LA61_0 = self.input.LA(1)

                        if (LA61_0 == LT) :
                            alt61 = 1


                        if alt61 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT132 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement852)
                            if self.failed:
                                return retval


                        else:
                            break #loop61


                    self.following.append(self.FOLLOW_expression_in_forStatement856)
                    expression133 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression133.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:85: ( LT )*
                while True: #loop63
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if (LA63_0 == LT) :
                        alt63 = 1


                    if alt63 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT134 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement860)
                        if self.failed:
                            return retval


                    else:
                        break #loop63


                char_literal135 = self.input.LT(1)
                self.match(self.input, 50, self.FOLLOW_50_in_forStatement864)
                if self.failed:
                    return retval

                char_literal135_tree = self.adaptor.createWithPayload(char_literal135)
                self.adaptor.addChild(root_0, char_literal135_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:92: ( ( LT )* expression )?
                alt65 = 2
                alt65 = self.dfa65.predict(self.input)
                if alt65 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:93: ( LT )* expression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:95: ( LT )*
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == LT) :
                            alt64 = 1


                        if alt64 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT136 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatement867)
                            if self.failed:
                                return retval


                        else:
                            break #loop64


                    self.following.append(self.FOLLOW_expression_in_forStatement871)
                    expression137 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression137.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:113: ( LT )*
                while True: #loop66
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == LT) :
                        alt66 = 1


                    if alt66 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT138 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement875)
                        if self.failed:
                            return retval


                    else:
                        break #loop66


                char_literal139 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_forStatement879)
                if self.failed:
                    return retval

                char_literal139_tree = self.adaptor.createWithPayload(char_literal139)
                self.adaptor.addChild(root_0, char_literal139_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:146:122: ( LT )*
                while True: #loop67
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == LT) :
                        alt67 = 1


                    if alt67 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT140 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forStatement881)
                        if self.failed:
                            return retval


                    else:
                        break #loop67


                self.following.append(self.FOLLOW_statement_in_forStatement885)
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
                self.memoize(self.input, 23, forStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forStatement

    class forStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:149:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 24):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:2: ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn )
                alt69 = 2
                LA69_0 = self.input.LA(1)

                if ((StringLiteral <= LA69_0 <= Identifier) or (42 <= LA69_0 <= 43) or LA69_0 == 46 or LA69_0 == 57 or (71 <= LA69_0 <= 72) or (104 <= LA69_0 <= 105) or LA69_0 == 107 or (109 <= LA69_0 <= 121)) :
                    alt69 = 1
                elif (LA69_0 == 48) :
                    alt69 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("149:1: forStatementInitialiserPart : ( expressionNoIn | 'var' ( LT )* variableDeclarationListNoIn );", 69, 0, self.input)

                    raise nvae

                if alt69 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:150:4: expressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_expressionNoIn_in_forStatementInitialiserPart897)
                    expressionNoIn142 = self.expressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expressionNoIn142.tree)


                elif alt69 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:4: 'var' ( LT )* variableDeclarationListNoIn
                    root_0 = self.adaptor.nil()

                    string_literal143 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_forStatementInitialiserPart902)
                    if self.failed:
                        return retval

                    string_literal143_tree = self.adaptor.createWithPayload(string_literal143)
                    self.adaptor.addChild(root_0, string_literal143_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:151:12: ( LT )*
                    while True: #loop68
                        alt68 = 2
                        LA68_0 = self.input.LA(1)

                        if (LA68_0 == LT) :
                            alt68 = 1


                        if alt68 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT144 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forStatementInitialiserPart904)
                            if self.failed:
                                return retval


                        else:
                            break #loop68


                    self.following.append(self.FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart908)
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
                self.memoize(self.input, 24, forStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forStatementInitialiserPart

    class forInStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:154:1: forInStatement : 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 25):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:2: ( 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:4: 'for' ( LT )* ( 'each' )? ( LT )* '(' ( LT )* forInStatementInitialiserPart ( LT )* 'in' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal146 = self.input.LT(1)
                self.match(self.input, 56, self.FOLLOW_56_in_forInStatement920)
                if self.failed:
                    return retval

                string_literal146_tree = self.adaptor.createWithPayload(string_literal146)
                self.adaptor.addChild(root_0, string_literal146_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:12: ( LT )*
                while True: #loop70
                    alt70 = 2
                    LA70_0 = self.input.LA(1)

                    if (LA70_0 == LT) :
                        LA70_2 = self.input.LA(2)

                        if (self.synpred86()) :
                            alt70 = 1




                    if alt70 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT147 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement922)
                        if self.failed:
                            return retval


                    else:
                        break #loop70


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:15: ( 'each' )?
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if (LA71_0 == 57) :
                    alt71 = 1
                if alt71 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: 'each'
                    string_literal148 = self.input.LT(1)
                    self.match(self.input, 57, self.FOLLOW_57_in_forInStatement926)
                    if self.failed:
                        return retval

                    string_literal148_tree = self.adaptor.createWithPayload(string_literal148)
                    self.adaptor.addChild(root_0, string_literal148_tree)




                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:25: ( LT )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == LT) :
                        alt72 = 1


                    if alt72 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT149 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement929)
                        if self.failed:
                            return retval


                    else:
                        break #loop72


                char_literal150 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_forInStatement933)
                if self.failed:
                    return retval

                char_literal150_tree = self.adaptor.createWithPayload(char_literal150)
                self.adaptor.addChild(root_0, char_literal150_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:34: ( LT )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == LT) :
                        alt73 = 1


                    if alt73 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT151 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement935)
                        if self.failed:
                            return retval


                    else:
                        break #loop73


                self.following.append(self.FOLLOW_forInStatementInitialiserPart_in_forInStatement939)
                forInStatementInitialiserPart152 = self.forInStatementInitialiserPart()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, forInStatementInitialiserPart152.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:69: ( LT )*
                while True: #loop74
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == LT) :
                        alt74 = 1


                    if alt74 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT153 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement941)
                        if self.failed:
                            return retval


                    else:
                        break #loop74


                string_literal154 = self.input.LT(1)
                self.match(self.input, 58, self.FOLLOW_58_in_forInStatement945)
                if self.failed:
                    return retval

                string_literal154_tree = self.adaptor.createWithPayload(string_literal154)
                self.adaptor.addChild(root_0, string_literal154_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:79: ( LT )*
                while True: #loop75
                    alt75 = 2
                    LA75_0 = self.input.LA(1)

                    if (LA75_0 == LT) :
                        alt75 = 1


                    if alt75 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT155 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement947)
                        if self.failed:
                            return retval


                    else:
                        break #loop75


                self.following.append(self.FOLLOW_expression_in_forInStatement951)
                expression156 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression156.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:95: ( LT )*
                while True: #loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == LT) :
                        alt76 = 1


                    if alt76 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT157 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement953)
                        if self.failed:
                            return retval


                    else:
                        break #loop76


                char_literal158 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_forInStatement957)
                if self.failed:
                    return retval

                char_literal158_tree = self.adaptor.createWithPayload(char_literal158)
                self.adaptor.addChild(root_0, char_literal158_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:104: ( LT )*
                while True: #loop77
                    alt77 = 2
                    LA77_0 = self.input.LA(1)

                    if (LA77_0 == LT) :
                        alt77 = 1


                    if alt77 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT159 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_forInStatement959)
                        if self.failed:
                            return retval


                    else:
                        break #loop77


                self.following.append(self.FOLLOW_statement_in_forInStatement963)
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
                self.memoize(self.input, 25, forInStatement_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatement

    class forInStatementInitialiserPart_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start forInStatementInitialiserPart
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:158:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 26):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:2: ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn )
                alt79 = 2
                LA79_0 = self.input.LA(1)

                if ((StringLiteral <= LA79_0 <= Identifier) or (42 <= LA79_0 <= 43) or LA79_0 == 46 or LA79_0 == 57 or (71 <= LA79_0 <= 72) or LA79_0 == 107 or (116 <= LA79_0 <= 121)) :
                    alt79 = 1
                elif (LA79_0 == 48) :
                    alt79 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("158:1: forInStatementInitialiserPart : ( leftHandSideExpression | 'var' ( LT )* variableDeclarationNoIn );", 79, 0, self.input)

                    raise nvae

                if alt79 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:159:4: leftHandSideExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart975)
                    leftHandSideExpression161 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression161.tree)


                elif alt79 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:4: 'var' ( LT )* variableDeclarationNoIn
                    root_0 = self.adaptor.nil()

                    string_literal162 = self.input.LT(1)
                    self.match(self.input, 48, self.FOLLOW_48_in_forInStatementInitialiserPart980)
                    if self.failed:
                        return retval

                    string_literal162_tree = self.adaptor.createWithPayload(string_literal162)
                    self.adaptor.addChild(root_0, string_literal162_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:160:12: ( LT )*
                    while True: #loop78
                        alt78 = 2
                        LA78_0 = self.input.LA(1)

                        if (LA78_0 == LT) :
                            alt78 = 1


                        if alt78 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT163 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_forInStatementInitialiserPart982)
                            if self.failed:
                                return retval


                        else:
                            break #loop78


                    self.following.append(self.FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart986)
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
                self.memoize(self.input, 26, forInStatementInitialiserPart_StartIndex)

            pass

        return retval

    # $ANTLR end forInStatementInitialiserPart

    class continueStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start continueStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:163:1: continueStatement : 'continue' ( identifier )? ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 27):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:2: ( 'continue' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:4: 'continue' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal165 = self.input.LT(1)
                self.match(self.input, 59, self.FOLLOW_59_in_continueStatement997)
                if self.failed:
                    return retval

                string_literal165_tree = self.adaptor.createWithPayload(string_literal165)
                self.adaptor.addChild(root_0, string_literal165_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:164:15: ( identifier )?
                alt80 = 2
                LA80_0 = self.input.LA(1)

                if (LA80_0 == Identifier or LA80_0 == 57 or (117 <= LA80_0 <= 118)) :
                    alt80 = 1
                if alt80 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_continueStatement999)
                    identifier166 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier166.tree)



                set167 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_continueStatement1002
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
                self.memoize(self.input, 27, continueStatement_StartIndex)

            pass

        return retval

    # $ANTLR end continueStatement

    class breakStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start breakStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:167:1: breakStatement : 'break' ( identifier )? ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 28):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:2: ( 'break' ( identifier )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:4: 'break' ( identifier )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal168 = self.input.LT(1)
                self.match(self.input, 60, self.FOLLOW_60_in_breakStatement1020)
                if self.failed:
                    return retval

                string_literal168_tree = self.adaptor.createWithPayload(string_literal168)
                self.adaptor.addChild(root_0, string_literal168_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:168:12: ( identifier )?
                alt81 = 2
                LA81_0 = self.input.LA(1)

                if (LA81_0 == Identifier or LA81_0 == 57 or (117 <= LA81_0 <= 118)) :
                    alt81 = 1
                if alt81 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: identifier
                    self.following.append(self.FOLLOW_identifier_in_breakStatement1022)
                    identifier169 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier169.tree)



                set170 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_breakStatement1025
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
                self.memoize(self.input, 28, breakStatement_StartIndex)

            pass

        return retval

    # $ANTLR end breakStatement

    class returnStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start returnStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:171:1: returnStatement : 'return' ( expression )? ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 29):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:2: ( 'return' ( expression )? ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:4: 'return' ( expression )? ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal171 = self.input.LT(1)
                self.match(self.input, 61, self.FOLLOW_61_in_returnStatement1043)
                if self.failed:
                    return retval

                string_literal171_tree = self.adaptor.createWithPayload(string_literal171)
                self.adaptor.addChild(root_0, string_literal171_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:172:13: ( expression )?
                alt82 = 2
                LA82_0 = self.input.LA(1)

                if ((StringLiteral <= LA82_0 <= Identifier) or (42 <= LA82_0 <= 43) or LA82_0 == 46 or LA82_0 == 57 or (71 <= LA82_0 <= 72) or (104 <= LA82_0 <= 105) or LA82_0 == 107 or (109 <= LA82_0 <= 121)) :
                    alt82 = 1
                if alt82 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: expression
                    self.following.append(self.FOLLOW_expression_in_returnStatement1045)
                    expression172 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression172.tree)



                set173 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_returnStatement1048
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
                self.memoize(self.input, 29, returnStatement_StartIndex)

            pass

        return retval

    # $ANTLR end returnStatement

    class withStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start withStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:175:1: withStatement : 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 30):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:2: ( 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:4: 'with' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* statement
                root_0 = self.adaptor.nil()

                string_literal174 = self.input.LT(1)
                self.match(self.input, 62, self.FOLLOW_62_in_withStatement1067)
                if self.failed:
                    return retval

                string_literal174_tree = self.adaptor.createWithPayload(string_literal174)
                self.adaptor.addChild(root_0, string_literal174_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:13: ( LT )*
                while True: #loop83
                    alt83 = 2
                    LA83_0 = self.input.LA(1)

                    if (LA83_0 == LT) :
                        alt83 = 1


                    if alt83 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT175 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1069)
                        if self.failed:
                            return retval


                    else:
                        break #loop83


                char_literal176 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_withStatement1073)
                if self.failed:
                    return retval

                char_literal176_tree = self.adaptor.createWithPayload(char_literal176)
                self.adaptor.addChild(root_0, char_literal176_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:22: ( LT )*
                while True: #loop84
                    alt84 = 2
                    LA84_0 = self.input.LA(1)

                    if (LA84_0 == LT) :
                        alt84 = 1


                    if alt84 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT177 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1075)
                        if self.failed:
                            return retval


                    else:
                        break #loop84


                self.following.append(self.FOLLOW_expression_in_withStatement1079)
                expression178 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression178.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:38: ( LT )*
                while True: #loop85
                    alt85 = 2
                    LA85_0 = self.input.LA(1)

                    if (LA85_0 == LT) :
                        alt85 = 1


                    if alt85 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT179 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1081)
                        if self.failed:
                            return retval


                    else:
                        break #loop85


                char_literal180 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_withStatement1085)
                if self.failed:
                    return retval

                char_literal180_tree = self.adaptor.createWithPayload(char_literal180)
                self.adaptor.addChild(root_0, char_literal180_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:176:47: ( LT )*
                while True: #loop86
                    alt86 = 2
                    LA86_0 = self.input.LA(1)

                    if (LA86_0 == LT) :
                        alt86 = 1


                    if alt86 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT181 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_withStatement1087)
                        if self.failed:
                            return retval


                    else:
                        break #loop86


                self.following.append(self.FOLLOW_statement_in_withStatement1091)
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
                self.memoize(self.input, 30, withStatement_StartIndex)

            pass

        return retval

    # $ANTLR end withStatement

    class labelledStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start labelledStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:179:1: labelledStatement : identifier ( LT )* ':' ( LT )* statement ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 31):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:180:2: ( identifier ( LT )* ':' ( LT )* statement )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:180:4: identifier ( LT )* ':' ( LT )* statement
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_identifier_in_labelledStatement1102)
                identifier183 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier183.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:180:17: ( LT )*
                while True: #loop87
                    alt87 = 2
                    LA87_0 = self.input.LA(1)

                    if (LA87_0 == LT) :
                        alt87 = 1


                    if alt87 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT184 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1104)
                        if self.failed:
                            return retval


                    else:
                        break #loop87


                char_literal185 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_labelledStatement1108)
                if self.failed:
                    return retval

                char_literal185_tree = self.adaptor.createWithPayload(char_literal185)
                self.adaptor.addChild(root_0, char_literal185_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:180:26: ( LT )*
                while True: #loop88
                    alt88 = 2
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == LT) :
                        alt88 = 1


                    if alt88 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT186 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_labelledStatement1110)
                        if self.failed:
                            return retval


                    else:
                        break #loop88


                self.following.append(self.FOLLOW_statement_in_labelledStatement1114)
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
                self.memoize(self.input, 31, labelledStatement_StartIndex)

            pass

        return retval

    # $ANTLR end labelledStatement

    class switchStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start switchStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:183:1: switchStatement : 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 32):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:2: ( 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:4: 'switch' ( LT )* '(' ( LT )* expression ( LT )* ')' ( LT )* caseBlock
                root_0 = self.adaptor.nil()

                string_literal188 = self.input.LT(1)
                self.match(self.input, 64, self.FOLLOW_64_in_switchStatement1126)
                if self.failed:
                    return retval

                string_literal188_tree = self.adaptor.createWithPayload(string_literal188)
                self.adaptor.addChild(root_0, string_literal188_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:15: ( LT )*
                while True: #loop89
                    alt89 = 2
                    LA89_0 = self.input.LA(1)

                    if (LA89_0 == LT) :
                        alt89 = 1


                    if alt89 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT189 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1128)
                        if self.failed:
                            return retval


                    else:
                        break #loop89


                char_literal190 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_switchStatement1132)
                if self.failed:
                    return retval

                char_literal190_tree = self.adaptor.createWithPayload(char_literal190)
                self.adaptor.addChild(root_0, char_literal190_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:24: ( LT )*
                while True: #loop90
                    alt90 = 2
                    LA90_0 = self.input.LA(1)

                    if (LA90_0 == LT) :
                        alt90 = 1


                    if alt90 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT191 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1134)
                        if self.failed:
                            return retval


                    else:
                        break #loop90


                self.following.append(self.FOLLOW_expression_in_switchStatement1138)
                expression192 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression192.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:40: ( LT )*
                while True: #loop91
                    alt91 = 2
                    LA91_0 = self.input.LA(1)

                    if (LA91_0 == LT) :
                        alt91 = 1


                    if alt91 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT193 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1140)
                        if self.failed:
                            return retval


                    else:
                        break #loop91


                char_literal194 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_switchStatement1144)
                if self.failed:
                    return retval

                char_literal194_tree = self.adaptor.createWithPayload(char_literal194)
                self.adaptor.addChild(root_0, char_literal194_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:184:49: ( LT )*
                while True: #loop92
                    alt92 = 2
                    LA92_0 = self.input.LA(1)

                    if (LA92_0 == LT) :
                        alt92 = 1


                    if alt92 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT195 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_switchStatement1146)
                        if self.failed:
                            return retval


                    else:
                        break #loop92


                self.following.append(self.FOLLOW_caseBlock_in_switchStatement1150)
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
                self.memoize(self.input, 32, switchStatement_StartIndex)

            pass

        return retval

    # $ANTLR end switchStatement

    class caseBlock_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseBlock
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:187:1: caseBlock : '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 33):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:2: ( '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:4: '{' ( ( LT )* caseClause )* ( ( LT )* defaultClause ( ( LT )* caseClause )* )? ( LT )* '}'
                root_0 = self.adaptor.nil()

                char_literal197 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_caseBlock1162)
                if self.failed:
                    return retval

                char_literal197_tree = self.adaptor.createWithPayload(char_literal197)
                self.adaptor.addChild(root_0, char_literal197_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:8: ( ( LT )* caseClause )*
                while True: #loop94
                    alt94 = 2
                    alt94 = self.dfa94.predict(self.input)
                    if alt94 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:9: ( LT )* caseClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:11: ( LT )*
                        while True: #loop93
                            alt93 = 2
                            LA93_0 = self.input.LA(1)

                            if (LA93_0 == LT) :
                                alt93 = 1


                            if alt93 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT198 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1165)
                                if self.failed:
                                    return retval


                            else:
                                break #loop93


                        self.following.append(self.FOLLOW_caseClause_in_caseBlock1169)
                        caseClause199 = self.caseClause()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, caseClause199.tree)


                    else:
                        break #loop94


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:27: ( ( LT )* defaultClause ( ( LT )* caseClause )* )?
                alt98 = 2
                alt98 = self.dfa98.predict(self.input)
                if alt98 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:28: ( LT )* defaultClause ( ( LT )* caseClause )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:30: ( LT )*
                    while True: #loop95
                        alt95 = 2
                        LA95_0 = self.input.LA(1)

                        if (LA95_0 == LT) :
                            alt95 = 1


                        if alt95 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT200 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1174)
                            if self.failed:
                                return retval


                        else:
                            break #loop95


                    self.following.append(self.FOLLOW_defaultClause_in_caseBlock1178)
                    defaultClause201 = self.defaultClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, defaultClause201.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:47: ( ( LT )* caseClause )*
                    while True: #loop97
                        alt97 = 2
                        alt97 = self.dfa97.predict(self.input)
                        if alt97 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:48: ( LT )* caseClause
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:50: ( LT )*
                            while True: #loop96
                                alt96 = 2
                                LA96_0 = self.input.LA(1)

                                if (LA96_0 == LT) :
                                    alt96 = 1


                                if alt96 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT202 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1181)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop96


                            self.following.append(self.FOLLOW_caseClause_in_caseBlock1185)
                            caseClause203 = self.caseClause()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, caseClause203.tree)


                        else:
                            break #loop97





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:188:70: ( LT )*
                while True: #loop99
                    alt99 = 2
                    LA99_0 = self.input.LA(1)

                    if (LA99_0 == LT) :
                        alt99 = 1


                    if alt99 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT204 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseBlock1191)
                        if self.failed:
                            return retval


                    else:
                        break #loop99


                char_literal205 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_caseBlock1195)
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
                self.memoize(self.input, 33, caseBlock_StartIndex)

            pass

        return retval

    # $ANTLR end caseBlock

    class caseClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start caseClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:191:1: caseClause : 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 34):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:2: ( 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:4: 'case' ( LT )* expression ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal206 = self.input.LT(1)
                self.match(self.input, 65, self.FOLLOW_65_in_caseClause1206)
                if self.failed:
                    return retval

                string_literal206_tree = self.adaptor.createWithPayload(string_literal206)
                self.adaptor.addChild(root_0, string_literal206_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:13: ( LT )*
                while True: #loop100
                    alt100 = 2
                    LA100_0 = self.input.LA(1)

                    if (LA100_0 == LT) :
                        alt100 = 1


                    if alt100 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT207 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1208)
                        if self.failed:
                            return retval


                    else:
                        break #loop100


                self.following.append(self.FOLLOW_expression_in_caseClause1212)
                expression208 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression208.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:29: ( LT )*
                while True: #loop101
                    alt101 = 2
                    LA101_0 = self.input.LA(1)

                    if (LA101_0 == LT) :
                        alt101 = 1


                    if alt101 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT209 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1214)
                        if self.failed:
                            return retval


                    else:
                        break #loop101


                char_literal210 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_caseClause1218)
                if self.failed:
                    return retval

                char_literal210_tree = self.adaptor.createWithPayload(char_literal210)
                self.adaptor.addChild(root_0, char_literal210_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:38: ( LT )*
                while True: #loop102
                    alt102 = 2
                    LA102_0 = self.input.LA(1)

                    if (LA102_0 == LT) :
                        LA102_2 = self.input.LA(2)

                        if (self.synpred121()) :
                            alt102 = 1




                    if alt102 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT211 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_caseClause1220)
                        if self.failed:
                            return retval


                    else:
                        break #loop102


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:41: ( statementList )?
                alt103 = 2
                LA103_0 = self.input.LA(1)

                if ((StringLiteral <= LA103_0 <= Identifier) or (42 <= LA103_0 <= 43) or LA103_0 == 46 or (48 <= LA103_0 <= 50) or LA103_0 == 52 or (54 <= LA103_0 <= 57) or (59 <= LA103_0 <= 62) or LA103_0 == 64 or (67 <= LA103_0 <= 68) or (71 <= LA103_0 <= 72) or (104 <= LA103_0 <= 105) or LA103_0 == 107 or (109 <= LA103_0 <= 121)) :
                    alt103 = 1
                if alt103 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_caseClause1224)
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
                self.memoize(self.input, 34, caseClause_StartIndex)

            pass

        return retval

    # $ANTLR end caseClause

    class defaultClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start defaultClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:195:1: defaultClause : 'default' ( LT )* ':' ( LT )* ( statementList )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 35):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:2: ( 'default' ( LT )* ':' ( LT )* ( statementList )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:4: 'default' ( LT )* ':' ( LT )* ( statementList )?
                root_0 = self.adaptor.nil()

                string_literal213 = self.input.LT(1)
                self.match(self.input, 66, self.FOLLOW_66_in_defaultClause1237)
                if self.failed:
                    return retval

                string_literal213_tree = self.adaptor.createWithPayload(string_literal213)
                self.adaptor.addChild(root_0, string_literal213_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:16: ( LT )*
                while True: #loop104
                    alt104 = 2
                    LA104_0 = self.input.LA(1)

                    if (LA104_0 == LT) :
                        alt104 = 1


                    if alt104 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT214 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1239)
                        if self.failed:
                            return retval


                    else:
                        break #loop104


                char_literal215 = self.input.LT(1)
                self.match(self.input, 63, self.FOLLOW_63_in_defaultClause1243)
                if self.failed:
                    return retval

                char_literal215_tree = self.adaptor.createWithPayload(char_literal215)
                self.adaptor.addChild(root_0, char_literal215_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:25: ( LT )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == LT) :
                        LA105_2 = self.input.LA(2)

                        if (self.synpred124()) :
                            alt105 = 1




                    if alt105 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT216 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_defaultClause1245)
                        if self.failed:
                            return retval


                    else:
                        break #loop105


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:28: ( statementList )?
                alt106 = 2
                LA106_0 = self.input.LA(1)

                if ((StringLiteral <= LA106_0 <= Identifier) or (42 <= LA106_0 <= 43) or LA106_0 == 46 or (48 <= LA106_0 <= 50) or LA106_0 == 52 or (54 <= LA106_0 <= 57) or (59 <= LA106_0 <= 62) or LA106_0 == 64 or (67 <= LA106_0 <= 68) or (71 <= LA106_0 <= 72) or (104 <= LA106_0 <= 105) or LA106_0 == 107 or (109 <= LA106_0 <= 121)) :
                    alt106 = 1
                if alt106 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: statementList
                    self.following.append(self.FOLLOW_statementList_in_defaultClause1249)
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
                self.memoize(self.input, 35, defaultClause_StartIndex)

            pass

        return retval

    # $ANTLR end defaultClause

    class throwStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start throwStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:199:1: throwStatement : 'throw' expression ( LT | ';' ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 36):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:200:2: ( 'throw' expression ( LT | ';' ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:200:4: 'throw' expression ( LT | ';' )
                root_0 = self.adaptor.nil()

                string_literal218 = self.input.LT(1)
                self.match(self.input, 67, self.FOLLOW_67_in_throwStatement1262)
                if self.failed:
                    return retval

                string_literal218_tree = self.adaptor.createWithPayload(string_literal218)
                self.adaptor.addChild(root_0, string_literal218_tree)

                self.following.append(self.FOLLOW_expression_in_throwStatement1264)
                expression219 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, expression219.tree)
                set220 = self.input.LT(1)
                if self.input.LA(1) == LT or self.input.LA(1) == 50:
                    self.input.consume();
                    self.errorRecovery = False
                    self.failed = False

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_throwStatement1266
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
                self.memoize(self.input, 36, throwStatement_StartIndex)

            pass

        return retval

    # $ANTLR end throwStatement

    class tryStatement_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start tryStatement
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:203:1: tryStatement : 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 37):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:2: ( 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:4: 'try' ( LT )* statementBlock ( LT )* ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                root_0 = self.adaptor.nil()

                string_literal221 = self.input.LT(1)
                self.match(self.input, 68, self.FOLLOW_68_in_tryStatement1284)
                if self.failed:
                    return retval

                string_literal221_tree = self.adaptor.createWithPayload(string_literal221)
                self.adaptor.addChild(root_0, string_literal221_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:12: ( LT )*
                while True: #loop107
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if (LA107_0 == LT) :
                        alt107 = 1


                    if alt107 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT222 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1286)
                        if self.failed:
                            return retval


                    else:
                        break #loop107


                self.following.append(self.FOLLOW_statementBlock_in_tryStatement1290)
                statementBlock223 = self.statementBlock()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, statementBlock223.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:32: ( LT )*
                while True: #loop108
                    alt108 = 2
                    LA108_0 = self.input.LA(1)

                    if (LA108_0 == LT) :
                        alt108 = 1


                    if alt108 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT224 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1292)
                        if self.failed:
                            return retval


                    else:
                        break #loop108


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )
                alt111 = 2
                LA111_0 = self.input.LA(1)

                if (LA111_0 == 70) :
                    alt111 = 1
                elif (LA111_0 == 69) :
                    alt111 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("204:35: ( finallyClause | catchClause ( ( LT )* finallyClause )? )", 111, 0, self.input)

                    raise nvae

                if alt111 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:36: finallyClause
                    self.following.append(self.FOLLOW_finallyClause_in_tryStatement1297)
                    finallyClause225 = self.finallyClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, finallyClause225.tree)


                elif alt111 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:52: catchClause ( ( LT )* finallyClause )?
                    self.following.append(self.FOLLOW_catchClause_in_tryStatement1301)
                    catchClause226 = self.catchClause()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, catchClause226.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:64: ( ( LT )* finallyClause )?
                    alt110 = 2
                    alt110 = self.dfa110.predict(self.input)
                    if alt110 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:65: ( LT )* finallyClause
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:204:67: ( LT )*
                        while True: #loop109
                            alt109 = 2
                            LA109_0 = self.input.LA(1)

                            if (LA109_0 == LT) :
                                alt109 = 1


                            if alt109 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT227 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_tryStatement1304)
                                if self.failed:
                                    return retval


                            else:
                                break #loop109


                        self.following.append(self.FOLLOW_finallyClause_in_tryStatement1308)
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
                self.memoize(self.input, 37, tryStatement_StartIndex)

            pass

        return retval

    # $ANTLR end tryStatement

    class catchClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start catchClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:207:1: catchClause : 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 38):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:2: ( 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:4: 'catch' ( LT )* '(' ( LT )* identifier ( LT )* ')' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal229 = self.input.LT(1)
                self.match(self.input, 69, self.FOLLOW_69_in_catchClause1329)
                if self.failed:
                    return retval

                string_literal229_tree = self.adaptor.createWithPayload(string_literal229)
                self.adaptor.addChild(root_0, string_literal229_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:14: ( LT )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == LT) :
                        alt112 = 1


                    if alt112 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT230 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1331)
                        if self.failed:
                            return retval


                    else:
                        break #loop112


                char_literal231 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_catchClause1335)
                if self.failed:
                    return retval

                char_literal231_tree = self.adaptor.createWithPayload(char_literal231)
                self.adaptor.addChild(root_0, char_literal231_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:23: ( LT )*
                while True: #loop113
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if (LA113_0 == LT) :
                        alt113 = 1


                    if alt113 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT232 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1337)
                        if self.failed:
                            return retval


                    else:
                        break #loop113


                self.following.append(self.FOLLOW_identifier_in_catchClause1341)
                identifier233 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, identifier233.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:39: ( LT )*
                while True: #loop114
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if (LA114_0 == LT) :
                        alt114 = 1


                    if alt114 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT234 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1343)
                        if self.failed:
                            return retval


                    else:
                        break #loop114


                char_literal235 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_catchClause1347)
                if self.failed:
                    return retval

                char_literal235_tree = self.adaptor.createWithPayload(char_literal235)
                self.adaptor.addChild(root_0, char_literal235_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:208:48: ( LT )*
                while True: #loop115
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if (LA115_0 == LT) :
                        alt115 = 1


                    if alt115 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT236 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_catchClause1349)
                        if self.failed:
                            return retval


                    else:
                        break #loop115


                self.following.append(self.FOLLOW_statementBlock_in_catchClause1353)
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
                self.memoize(self.input, 38, catchClause_StartIndex)

            pass

        return retval

    # $ANTLR end catchClause

    class finallyClause_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start finallyClause
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:211:1: finallyClause : 'finally' ( LT )* statementBlock ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 39):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:2: ( 'finally' ( LT )* statementBlock )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:4: 'finally' ( LT )* statementBlock
                root_0 = self.adaptor.nil()

                string_literal238 = self.input.LT(1)
                self.match(self.input, 70, self.FOLLOW_70_in_finallyClause1365)
                if self.failed:
                    return retval

                string_literal238_tree = self.adaptor.createWithPayload(string_literal238)
                self.adaptor.addChild(root_0, string_literal238_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:212:16: ( LT )*
                while True: #loop116
                    alt116 = 2
                    LA116_0 = self.input.LA(1)

                    if (LA116_0 == LT) :
                        alt116 = 1


                    if alt116 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT239 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_finallyClause1367)
                        if self.failed:
                            return retval


                    else:
                        break #loop116


                self.following.append(self.FOLLOW_statementBlock_in_finallyClause1371)
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
                self.memoize(self.input, 39, finallyClause_StartIndex)

            pass

        return retval

    # $ANTLR end finallyClause

    class expression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:216:1: expression : assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 40):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:2: ( assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:4: assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpression_in_expression1383)
                assignmentExpression241 = self.assignmentExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpression241.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:25: ( ( LT )* ',' ( LT )* assignmentExpression )*
                while True: #loop119
                    alt119 = 2
                    alt119 = self.dfa119.predict(self.input)
                    if alt119 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:26: ( LT )* ',' ( LT )* assignmentExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:28: ( LT )*
                        while True: #loop117
                            alt117 = 2
                            LA117_0 = self.input.LA(1)

                            if (LA117_0 == LT) :
                                alt117 = 1


                            if alt117 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT242 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1386)
                                if self.failed:
                                    return retval


                            else:
                                break #loop117


                        char_literal243 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_expression1390)
                        if self.failed:
                            return retval

                        char_literal243_tree = self.adaptor.createWithPayload(char_literal243)
                        self.adaptor.addChild(root_0, char_literal243_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:217:37: ( LT )*
                        while True: #loop118
                            alt118 = 2
                            LA118_0 = self.input.LA(1)

                            if (LA118_0 == LT) :
                                alt118 = 1


                            if alt118 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT244 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expression1392)
                                if self.failed:
                                    return retval


                            else:
                                break #loop118


                        self.following.append(self.FOLLOW_assignmentExpression_in_expression1396)
                        assignmentExpression245 = self.assignmentExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpression245.tree)


                    else:
                        break #loop119





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 40, expression_StartIndex)

            pass

        return retval

    # $ANTLR end expression

    class expressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start expressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:220:1: expressionNoIn : assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 41):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:2: ( assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:4: assignmentExpressionNoIn ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1410)
                assignmentExpressionNoIn246 = self.assignmentExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, assignmentExpressionNoIn246.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:29: ( ( LT )* ',' ( LT )* assignmentExpressionNoIn )*
                while True: #loop122
                    alt122 = 2
                    alt122 = self.dfa122.predict(self.input)
                    if alt122 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:30: ( LT )* ',' ( LT )* assignmentExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:32: ( LT )*
                        while True: #loop120
                            alt120 = 2
                            LA120_0 = self.input.LA(1)

                            if (LA120_0 == LT) :
                                alt120 = 1


                            if alt120 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT247 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1413)
                                if self.failed:
                                    return retval


                            else:
                                break #loop120


                        char_literal248 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_expressionNoIn1417)
                        if self.failed:
                            return retval

                        char_literal248_tree = self.adaptor.createWithPayload(char_literal248)
                        self.adaptor.addChild(root_0, char_literal248_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:221:41: ( LT )*
                        while True: #loop121
                            alt121 = 2
                            LA121_0 = self.input.LA(1)

                            if (LA121_0 == LT) :
                                alt121 = 1


                            if alt121 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT249 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_expressionNoIn1419)
                                if self.failed:
                                    return retval


                            else:
                                break #loop121


                        self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1423)
                        assignmentExpressionNoIn250 = self.assignmentExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, assignmentExpressionNoIn250.tree)


                    else:
                        break #loop122





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 41, expressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end expressionNoIn

    class assignmentExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 42):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:2: ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression )
                alt125 = 2
                LA125 = self.input.LA(1)
                if LA125 == 116:
                    LA125_1 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 1, self.input)

                        raise nvae

                elif LA125 == Identifier or LA125 == 57 or LA125 == 117 or LA125 == 118:
                    LA125_2 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 2, self.input)

                        raise nvae

                elif LA125 == 119:
                    LA125_3 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 3, self.input)

                        raise nvae

                elif LA125 == 120:
                    LA125_4 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 4, self.input)

                        raise nvae

                elif LA125 == 121:
                    LA125_5 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 5, self.input)

                        raise nvae

                elif LA125 == StringLiteral:
                    LA125_6 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 6, self.input)

                        raise nvae

                elif LA125 == NumericLiteral:
                    LA125_7 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 7, self.input)

                        raise nvae

                elif LA125 == 107:
                    LA125_8 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 8, self.input)

                        raise nvae

                elif LA125 == 72:
                    LA125_9 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 9, self.input)

                        raise nvae

                elif LA125 == 46:
                    LA125_10 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 10, self.input)

                        raise nvae

                elif LA125 == 43:
                    LA125_11 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 11, self.input)

                        raise nvae

                elif LA125 == 42:
                    LA125_12 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 12, self.input)

                        raise nvae

                elif LA125 == 71:
                    LA125_13 = self.input.LA(2)

                    if (self.synpred143()) :
                        alt125 = 1
                    elif (True) :
                        alt125 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 13, self.input)

                        raise nvae

                elif LA125 == 104 or LA125 == 105 or LA125 == 109 or LA125 == 110 or LA125 == 111 or LA125 == 112 or LA125 == 113 or LA125 == 114 or LA125 == 115:
                    alt125 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("224:1: assignmentExpression : ( conditionalExpression | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression );", 125, 0, self.input)

                    raise nvae

                if alt125 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: conditionalExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpression_in_assignmentExpression1437)
                    conditionalExpression251 = self.conditionalExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpression251.tree)


                elif alt125 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpression1442)
                    leftHandSideExpression252 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression252.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:29: ( LT )*
                    while True: #loop123
                        alt123 = 2
                        LA123_0 = self.input.LA(1)

                        if (LA123_0 == LT) :
                            alt123 = 1


                        if alt123 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT253 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1444)
                            if self.failed:
                                return retval


                        else:
                            break #loop123


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpression1448)
                    assignmentOperator254 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator254.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:226:53: ( LT )*
                    while True: #loop124
                        alt124 = 2
                        LA124_0 = self.input.LA(1)

                        if (LA124_0 == LT) :
                            alt124 = 1


                        if alt124 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT255 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpression1450)
                            if self.failed:
                                return retval


                        else:
                            break #loop124


                    self.following.append(self.FOLLOW_assignmentExpression_in_assignmentExpression1454)
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
                self.memoize(self.input, 42, assignmentExpression_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpression

    class assignmentExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 43):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:2: ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn )
                alt128 = 2
                LA128 = self.input.LA(1)
                if LA128 == 116:
                    LA128_1 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 1, self.input)

                        raise nvae

                elif LA128 == Identifier or LA128 == 57 or LA128 == 117 or LA128 == 118:
                    LA128_2 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 2, self.input)

                        raise nvae

                elif LA128 == 119:
                    LA128_3 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 3, self.input)

                        raise nvae

                elif LA128 == 120:
                    LA128_4 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 4, self.input)

                        raise nvae

                elif LA128 == 121:
                    LA128_5 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 5, self.input)

                        raise nvae

                elif LA128 == StringLiteral:
                    LA128_6 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 6, self.input)

                        raise nvae

                elif LA128 == NumericLiteral:
                    LA128_7 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 7, self.input)

                        raise nvae

                elif LA128 == 107:
                    LA128_8 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 8, self.input)

                        raise nvae

                elif LA128 == 72:
                    LA128_9 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 9, self.input)

                        raise nvae

                elif LA128 == 46:
                    LA128_10 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 10, self.input)

                        raise nvae

                elif LA128 == 43:
                    LA128_11 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 11, self.input)

                        raise nvae

                elif LA128 == 42:
                    LA128_12 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 12, self.input)

                        raise nvae

                elif LA128 == 71:
                    LA128_13 = self.input.LA(2)

                    if (self.synpred146()) :
                        alt128 = 1
                    elif (True) :
                        alt128 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 13, self.input)

                        raise nvae

                elif LA128 == 104 or LA128 == 105 or LA128 == 109 or LA128 == 110 or LA128 == 111 or LA128 == 112 or LA128 == 113 or LA128 == 114 or LA128 == 115:
                    alt128 = 1
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("229:1: assignmentExpressionNoIn : ( conditionalExpressionNoIn | leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn );", 128, 0, self.input)

                    raise nvae

                if alt128 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:4: conditionalExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1466)
                    conditionalExpressionNoIn257 = self.conditionalExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, conditionalExpressionNoIn257.tree)


                elif alt128 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:4: leftHandSideExpression ( LT )* assignmentOperator ( LT )* assignmentExpressionNoIn
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1471)
                    leftHandSideExpression258 = self.leftHandSideExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, leftHandSideExpression258.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:29: ( LT )*
                    while True: #loop126
                        alt126 = 2
                        LA126_0 = self.input.LA(1)

                        if (LA126_0 == LT) :
                            alt126 = 1


                        if alt126 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT259 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1473)
                            if self.failed:
                                return retval


                        else:
                            break #loop126


                    self.following.append(self.FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1477)
                    assignmentOperator260 = self.assignmentOperator()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentOperator260.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:231:53: ( LT )*
                    while True: #loop127
                        alt127 = 2
                        LA127_0 = self.input.LA(1)

                        if (LA127_0 == LT) :
                            alt127 = 1


                        if alt127 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT261 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_assignmentExpressionNoIn1479)
                            if self.failed:
                                return retval


                        else:
                            break #loop127


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1483)
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
                self.memoize(self.input, 43, assignmentExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentExpressionNoIn

    class leftHandSideExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start leftHandSideExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:234:1: leftHandSideExpression : ( callExpression | newExpression );
    def leftHandSideExpression(self, ):

        retval = self.leftHandSideExpression_return()
        retval.start = self.input.LT(1)
        leftHandSideExpression_StartIndex = self.input.index()
        root_0 = None

        callExpression263 = None

        newExpression264 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 44):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:2: ( callExpression | newExpression )
                alt129 = 2
                LA129 = self.input.LA(1)
                if LA129 == 116:
                    LA129_1 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 1, self.input)

                        raise nvae

                elif LA129 == Identifier or LA129 == 57 or LA129 == 117 or LA129 == 118:
                    LA129_2 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 2, self.input)

                        raise nvae

                elif LA129 == 119:
                    LA129_3 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 3, self.input)

                        raise nvae

                elif LA129 == 120:
                    LA129_4 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 4, self.input)

                        raise nvae

                elif LA129 == 121:
                    LA129_5 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 5, self.input)

                        raise nvae

                elif LA129 == StringLiteral:
                    LA129_6 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 6, self.input)

                        raise nvae

                elif LA129 == NumericLiteral:
                    LA129_7 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 7, self.input)

                        raise nvae

                elif LA129 == 107:
                    LA129_8 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 8, self.input)

                        raise nvae

                elif LA129 == 72:
                    LA129_9 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 9, self.input)

                        raise nvae

                elif LA129 == 46:
                    LA129_10 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 10, self.input)

                        raise nvae

                elif LA129 == 43:
                    LA129_11 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 11, self.input)

                        raise nvae

                elif LA129 == 42:
                    LA129_12 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 12, self.input)

                        raise nvae

                elif LA129 == 71:
                    LA129_13 = self.input.LA(2)

                    if (self.synpred149()) :
                        alt129 = 1
                    elif (True) :
                        alt129 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 13, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("234:1: leftHandSideExpression : ( callExpression | newExpression );", 129, 0, self.input)

                    raise nvae

                if alt129 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:4: callExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_callExpression_in_leftHandSideExpression1495)
                    callExpression263 = self.callExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, callExpression263.tree)


                elif alt129 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:236:4: newExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_newExpression_in_leftHandSideExpression1500)
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
                self.memoize(self.input, 44, leftHandSideExpression_StartIndex)

            pass

        return retval

    # $ANTLR end leftHandSideExpression

    class newExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start newExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:239:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 45):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:2: ( memberExpression | 'new' ( LT )* newExpression )
                alt131 = 2
                LA131_0 = self.input.LA(1)

                if ((StringLiteral <= LA131_0 <= Identifier) or (42 <= LA131_0 <= 43) or LA131_0 == 46 or LA131_0 == 57 or LA131_0 == 72 or LA131_0 == 107 or (116 <= LA131_0 <= 121)) :
                    alt131 = 1
                elif (LA131_0 == 71) :
                    LA131_13 = self.input.LA(2)

                    if (self.synpred150()) :
                        alt131 = 1
                    elif (True) :
                        alt131 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("239:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 131, 13, self.input)

                        raise nvae

                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("239:1: newExpression : ( memberExpression | 'new' ( LT )* newExpression );", 131, 0, self.input)

                    raise nvae

                if alt131 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:4: memberExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_memberExpression_in_newExpression1512)
                    memberExpression265 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression265.tree)


                elif alt131 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:241:4: 'new' ( LT )* newExpression
                    root_0 = self.adaptor.nil()

                    string_literal266 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_newExpression1517)
                    if self.failed:
                        return retval

                    string_literal266_tree = self.adaptor.createWithPayload(string_literal266)
                    self.adaptor.addChild(root_0, string_literal266_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:241:12: ( LT )*
                    while True: #loop130
                        alt130 = 2
                        LA130_0 = self.input.LA(1)

                        if (LA130_0 == LT) :
                            alt130 = 1


                        if alt130 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT267 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_newExpression1519)
                            if self.failed:
                                return retval


                        else:
                            break #loop130


                    self.following.append(self.FOLLOW_newExpression_in_newExpression1523)
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
                self.memoize(self.input, 45, newExpression_StartIndex)

            pass

        return retval

    # $ANTLR end newExpression

    class memberExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:244:1: memberExpression : ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 46):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:2: ( ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments ) ( ( LT )* memberExpressionSuffix )*
                root_0 = self.adaptor.nil()

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )
                alt134 = 3
                LA134 = self.input.LA(1)
                if LA134 == StringLiteral or LA134 == NumericLiteral or LA134 == Identifier or LA134 == 43 or LA134 == 46 or LA134 == 57 or LA134 == 72 or LA134 == 107 or LA134 == 116 or LA134 == 117 or LA134 == 118 or LA134 == 119 or LA134 == 120 or LA134 == 121:
                    alt134 = 1
                elif LA134 == 42:
                    alt134 = 2
                elif LA134 == 71:
                    alt134 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("245:4: ( primaryExpression | functionExpression | 'new' ( LT )* memberExpression ( LT )* arguments )", 134, 0, self.input)

                    raise nvae

                if alt134 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:5: primaryExpression
                    self.following.append(self.FOLLOW_primaryExpression_in_memberExpression1536)
                    primaryExpression269 = self.primaryExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, primaryExpression269.tree)


                elif alt134 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:25: functionExpression
                    self.following.append(self.FOLLOW_functionExpression_in_memberExpression1540)
                    functionExpression270 = self.functionExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, functionExpression270.tree)


                elif alt134 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:46: 'new' ( LT )* memberExpression ( LT )* arguments
                    string_literal271 = self.input.LT(1)
                    self.match(self.input, 71, self.FOLLOW_71_in_memberExpression1544)
                    if self.failed:
                        return retval

                    string_literal271_tree = self.adaptor.createWithPayload(string_literal271)
                    self.adaptor.addChild(root_0, string_literal271_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:54: ( LT )*
                    while True: #loop132
                        alt132 = 2
                        LA132_0 = self.input.LA(1)

                        if (LA132_0 == LT) :
                            alt132 = 1


                        if alt132 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT272 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1546)
                            if self.failed:
                                return retval


                        else:
                            break #loop132


                    self.following.append(self.FOLLOW_memberExpression_in_memberExpression1550)
                    memberExpression273 = self.memberExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, memberExpression273.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:76: ( LT )*
                    while True: #loop133
                        alt133 = 2
                        LA133_0 = self.input.LA(1)

                        if (LA133_0 == LT) :
                            alt133 = 1


                        if alt133 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT274 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1552)
                            if self.failed:
                                return retval


                        else:
                            break #loop133


                    self.following.append(self.FOLLOW_arguments_in_memberExpression1556)
                    arguments275 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments275.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:90: ( ( LT )* memberExpressionSuffix )*
                while True: #loop136
                    alt136 = 2
                    LA136_0 = self.input.LA(1)

                    if (LA136_0 == LT) :
                        LA136_1 = self.input.LA(2)

                        if (self.synpred157()) :
                            alt136 = 1


                    elif (LA136_0 == 72 or LA136_0 == 74) :
                        alt136 = 1


                    if alt136 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:91: ( LT )* memberExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:93: ( LT )*
                        while True: #loop135
                            alt135 = 2
                            LA135_0 = self.input.LA(1)

                            if (LA135_0 == LT) :
                                alt135 = 1


                            if alt135 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT276 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_memberExpression1560)
                                if self.failed:
                                    return retval


                            else:
                                break #loop135


                        self.following.append(self.FOLLOW_memberExpressionSuffix_in_memberExpression1564)
                        memberExpressionSuffix277 = self.memberExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, memberExpressionSuffix277.tree)


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
                self.memoize(self.input, 46, memberExpression_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpression

    class memberExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start memberExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:248:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );
    def memberExpressionSuffix(self, ):

        retval = self.memberExpressionSuffix_return()
        retval.start = self.input.LT(1)
        memberExpressionSuffix_StartIndex = self.input.index()
        root_0 = None

        indexSuffix278 = None

        propertyReferenceSuffix279 = None



        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 47):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:2: ( indexSuffix | propertyReferenceSuffix )
                alt137 = 2
                LA137_0 = self.input.LA(1)

                if (LA137_0 == 72) :
                    alt137 = 1
                elif (LA137_0 == 74) :
                    alt137 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("248:1: memberExpressionSuffix : ( indexSuffix | propertyReferenceSuffix );", 137, 0, self.input)

                    raise nvae

                if alt137 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:249:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_memberExpressionSuffix1578)
                    indexSuffix278 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix278.tree)


                elif alt137 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:250:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1583)
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
                self.memoize(self.input, 47, memberExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end memberExpressionSuffix

    class callExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:253:1: callExpression : memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_memberExpression = RewriteRuleSubtreeStream(self.adaptor, "rule memberExpression")
        stream_arguments = RewriteRuleSubtreeStream(self.adaptor, "rule arguments")
        stream_callExpressionSuffix = RewriteRuleSubtreeStream(self.adaptor, "rule callExpressionSuffix")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 48):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:2: ( memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )* -> ^( CALL memberExpression arguments ( callExpressionSuffix )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:4: memberExpression ( LT )* arguments ( ( LT )* callExpressionSuffix )*
                self.following.append(self.FOLLOW_memberExpression_in_callExpression1594)
                memberExpression280 = self.memberExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_memberExpression.add(memberExpression280.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:21: ( LT )*
                while True: #loop138
                    alt138 = 2
                    LA138_0 = self.input.LA(1)

                    if (LA138_0 == LT) :
                        alt138 = 1


                    if alt138 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT281 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1596)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT281)


                    else:
                        break #loop138


                self.following.append(self.FOLLOW_arguments_in_callExpression1599)
                arguments282 = self.arguments()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_arguments.add(arguments282.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:35: ( ( LT )* callExpressionSuffix )*
                while True: #loop140
                    alt140 = 2
                    LA140_0 = self.input.LA(1)

                    if (LA140_0 == LT) :
                        LA140_1 = self.input.LA(2)

                        if (self.synpred161()) :
                            alt140 = 1


                    elif (LA140_0 == 43 or LA140_0 == 72 or LA140_0 == 74) :
                        alt140 = 1


                    if alt140 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:36: ( LT )* callExpressionSuffix
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:36: ( LT )*
                        while True: #loop139
                            alt139 = 2
                            LA139_0 = self.input.LA(1)

                            if (LA139_0 == LT) :
                                alt139 = 1


                            if alt139 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT283 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_callExpression1602)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT283)


                            else:
                                break #loop139


                        self.following.append(self.FOLLOW_callExpressionSuffix_in_callExpression1605)
                        callExpressionSuffix284 = self.callExpressionSuffix()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_callExpressionSuffix.add(callExpressionSuffix284.tree)


                    else:
                        break #loop140


                # AST Rewrite
                # elements: memberExpression, arguments, callExpressionSuffix
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
                    # 255:3: -> ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:6: ^( CALL memberExpression arguments ( callExpressionSuffix )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(CALL, "CALL"), root_1)

                    self.adaptor.addChild(root_1, stream_memberExpression.next())
                    self.adaptor.addChild(root_1, stream_arguments.next())
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:255:40: ( callExpressionSuffix )*
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
                self.memoize(self.input, 48, callExpression_StartIndex)

            pass

        return retval

    # $ANTLR end callExpression

    class callExpressionSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start callExpressionSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:258:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 49):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:2: ( arguments | indexSuffix | propertyReferenceSuffix )
                alt141 = 3
                LA141 = self.input.LA(1)
                if LA141 == 43:
                    alt141 = 1
                elif LA141 == 72:
                    alt141 = 2
                elif LA141 == 74:
                    alt141 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("258:1: callExpressionSuffix : ( arguments | indexSuffix | propertyReferenceSuffix );", 141, 0, self.input)

                    raise nvae

                if alt141 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:259:4: arguments
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arguments_in_callExpressionSuffix1634)
                    arguments285 = self.arguments()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arguments285.tree)


                elif alt141 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:260:4: indexSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_indexSuffix_in_callExpressionSuffix1639)
                    indexSuffix286 = self.indexSuffix()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, indexSuffix286.tree)


                elif alt141 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:261:4: propertyReferenceSuffix
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1644)
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
                self.memoize(self.input, 49, callExpressionSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end callExpressionSuffix

    class arguments_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arguments
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:264:1: arguments : '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 50):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:2: ( '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:4: '(' ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )? ( LT )* ')'
                root_0 = self.adaptor.nil()

                char_literal288 = self.input.LT(1)
                self.match(self.input, 43, self.FOLLOW_43_in_arguments1655)
                if self.failed:
                    return retval

                char_literal288_tree = self.adaptor.createWithPayload(char_literal288)
                self.adaptor.addChild(root_0, char_literal288_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:8: ( ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )* )?
                alt146 = 2
                alt146 = self.dfa146.predict(self.input)
                if alt146 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:9: ( LT )* assignmentExpression ( ( LT )* ',' ( LT )* assignmentExpression )*
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:11: ( LT )*
                    while True: #loop142
                        alt142 = 2
                        LA142_0 = self.input.LA(1)

                        if (LA142_0 == LT) :
                            alt142 = 1


                        if alt142 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT289 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_arguments1658)
                            if self.failed:
                                return retval


                        else:
                            break #loop142


                    self.following.append(self.FOLLOW_assignmentExpression_in_arguments1662)
                    assignmentExpression290 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression290.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:35: ( ( LT )* ',' ( LT )* assignmentExpression )*
                    while True: #loop145
                        alt145 = 2
                        alt145 = self.dfa145.predict(self.input)
                        if alt145 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:36: ( LT )* ',' ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:38: ( LT )*
                            while True: #loop143
                                alt143 = 2
                                LA143_0 = self.input.LA(1)

                                if (LA143_0 == LT) :
                                    alt143 = 1


                                if alt143 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT291 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1665)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop143


                            char_literal292 = self.input.LT(1)
                            self.match(self.input, 44, self.FOLLOW_44_in_arguments1669)
                            if self.failed:
                                return retval

                            char_literal292_tree = self.adaptor.createWithPayload(char_literal292)
                            self.adaptor.addChild(root_0, char_literal292_tree)

                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:47: ( LT )*
                            while True: #loop144
                                alt144 = 2
                                LA144_0 = self.input.LA(1)

                                if (LA144_0 == LT) :
                                    alt144 = 1


                                if alt144 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT293 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arguments1671)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop144


                            self.following.append(self.FOLLOW_assignmentExpression_in_arguments1675)
                            assignmentExpression294 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression294.tree)


                        else:
                            break #loop145





                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:265:77: ( LT )*
                while True: #loop147
                    alt147 = 2
                    LA147_0 = self.input.LA(1)

                    if (LA147_0 == LT) :
                        alt147 = 1


                    if alt147 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT295 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arguments1681)
                        if self.failed:
                            return retval


                    else:
                        break #loop147


                char_literal296 = self.input.LT(1)
                self.match(self.input, 45, self.FOLLOW_45_in_arguments1685)
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
                self.memoize(self.input, 50, arguments_StartIndex)

            pass

        return retval

    # $ANTLR end arguments

    class indexSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start indexSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:268:1: indexSuffix : '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_72 = RewriteRuleTokenStream(self.adaptor, "token 72")
        stream_73 = RewriteRuleTokenStream(self.adaptor, "token 73")
        stream_expression = RewriteRuleSubtreeStream(self.adaptor, "rule expression")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 51):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:2: ( '[' ( LT )* expression ( LT )* ']' -> ^( INDEXREF expression ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:4: '[' ( LT )* expression ( LT )* ']'
                char_literal297 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_indexSuffix1697)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_72.add(char_literal297)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:8: ( LT )*
                while True: #loop148
                    alt148 = 2
                    LA148_0 = self.input.LA(1)

                    if (LA148_0 == LT) :
                        alt148 = 1


                    if alt148 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT298 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1699)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT298)


                    else:
                        break #loop148


                self.following.append(self.FOLLOW_expression_in_indexSuffix1702)
                expression299 = self.expression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_expression.add(expression299.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:269:23: ( LT )*
                while True: #loop149
                    alt149 = 2
                    LA149_0 = self.input.LA(1)

                    if (LA149_0 == LT) :
                        alt149 = 1


                    if alt149 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT300 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_indexSuffix1704)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT300)


                    else:
                        break #loop149


                char_literal301 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_indexSuffix1707)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_73.add(char_literal301)
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
                    # 270:3: -> ^( INDEXREF expression )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:270:6: ^( INDEXREF expression )
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
                self.memoize(self.input, 51, indexSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end indexSuffix

    class propertyReferenceSuffix_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyReferenceSuffix
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:273:1: propertyReferenceSuffix : '.' ( LT )* identifier -> ^( PROPREF identifier ) ;
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
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_74 = RewriteRuleTokenStream(self.adaptor, "token 74")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 52):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:2: ( '.' ( LT )* identifier -> ^( PROPREF identifier ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:4: '.' ( LT )* identifier
                char_literal302 = self.input.LT(1)
                self.match(self.input, 74, self.FOLLOW_74_in_propertyReferenceSuffix1730)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_74.add(char_literal302)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:274:8: ( LT )*
                while True: #loop150
                    alt150 = 2
                    LA150_0 = self.input.LA(1)

                    if (LA150_0 == LT) :
                        alt150 = 1


                    if alt150 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT303 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_propertyReferenceSuffix1732)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT303)


                    else:
                        break #loop150


                self.following.append(self.FOLLOW_identifier_in_propertyReferenceSuffix1735)
                identifier304 = self.identifier()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_identifier.add(identifier304.tree)
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
                    # 275:3: -> ^( PROPREF identifier )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:275:6: ^( PROPREF identifier )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROPREF, "PROPREF"), root_1)

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
                self.memoize(self.input, 52, propertyReferenceSuffix_StartIndex)

            pass

        return retval

    # $ANTLR end propertyReferenceSuffix

    class assignmentOperator_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start assignmentOperator
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:278:1: assignmentOperator : ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' );
    def assignmentOperator(self, ):

        retval = self.assignmentOperator_return()
        retval.start = self.input.LT(1)
        assignmentOperator_StartIndex = self.input.index()
        root_0 = None

        set305 = None

        set305_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 53):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:279:2: ( '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set305 = self.input.LT(1)
                if self.input.LA(1) == 51 or (75 <= self.input.LA(1) <= 85):
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
                self.memoize(self.input, 53, assignmentOperator_StartIndex)

            pass

        return retval

    # $ANTLR end assignmentOperator

    class conditionalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:282:1: conditionalExpression : logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 54):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:2: ( logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:4: logicalORExpression ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpression_in_conditionalExpression1812)
                logicalORExpression306 = self.logicalORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpression306.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:24: ( ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression )?
                alt155 = 2
                alt155 = self.dfa155.predict(self.input)
                if alt155 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:25: ( LT )* '?' ( LT )* assignmentExpression ( LT )* ':' ( LT )* assignmentExpression
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:27: ( LT )*
                    while True: #loop151
                        alt151 = 2
                        LA151_0 = self.input.LA(1)

                        if (LA151_0 == LT) :
                            alt151 = 1


                        if alt151 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT307 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1815)
                            if self.failed:
                                return retval


                        else:
                            break #loop151


                    char_literal308 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_conditionalExpression1819)
                    if self.failed:
                        return retval

                    char_literal308_tree = self.adaptor.createWithPayload(char_literal308)
                    self.adaptor.addChild(root_0, char_literal308_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:36: ( LT )*
                    while True: #loop152
                        alt152 = 2
                        LA152_0 = self.input.LA(1)

                        if (LA152_0 == LT) :
                            alt152 = 1


                        if alt152 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT309 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1821)
                            if self.failed:
                                return retval


                        else:
                            break #loop152


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1825)
                    assignmentExpression310 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression310.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:62: ( LT )*
                    while True: #loop153
                        alt153 = 2
                        LA153_0 = self.input.LA(1)

                        if (LA153_0 == LT) :
                            alt153 = 1


                        if alt153 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT311 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1827)
                            if self.failed:
                                return retval


                        else:
                            break #loop153


                    char_literal312 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpression1831)
                    if self.failed:
                        return retval

                    char_literal312_tree = self.adaptor.createWithPayload(char_literal312)
                    self.adaptor.addChild(root_0, char_literal312_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:283:71: ( LT )*
                    while True: #loop154
                        alt154 = 2
                        LA154_0 = self.input.LA(1)

                        if (LA154_0 == LT) :
                            alt154 = 1


                        if alt154 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT313 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpression1833)
                            if self.failed:
                                return retval


                        else:
                            break #loop154


                    self.following.append(self.FOLLOW_assignmentExpression_in_conditionalExpression1837)
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
                self.memoize(self.input, 54, conditionalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpression

    class conditionalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start conditionalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:286:1: conditionalExpressionNoIn : logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 55):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:2: ( logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:4: logicalORExpressionNoIn ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1850)
                logicalORExpressionNoIn315 = self.logicalORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalORExpressionNoIn315.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:28: ( ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn )?
                alt160 = 2
                alt160 = self.dfa160.predict(self.input)
                if alt160 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:29: ( LT )* '?' ( LT )* assignmentExpressionNoIn ( LT )* ':' ( LT )* assignmentExpressionNoIn
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:31: ( LT )*
                    while True: #loop156
                        alt156 = 2
                        LA156_0 = self.input.LA(1)

                        if (LA156_0 == LT) :
                            alt156 = 1


                        if alt156 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT316 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1853)
                            if self.failed:
                                return retval


                        else:
                            break #loop156


                    char_literal317 = self.input.LT(1)
                    self.match(self.input, 86, self.FOLLOW_86_in_conditionalExpressionNoIn1857)
                    if self.failed:
                        return retval

                    char_literal317_tree = self.adaptor.createWithPayload(char_literal317)
                    self.adaptor.addChild(root_0, char_literal317_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:40: ( LT )*
                    while True: #loop157
                        alt157 = 2
                        LA157_0 = self.input.LA(1)

                        if (LA157_0 == LT) :
                            alt157 = 1


                        if alt157 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT318 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1859)
                            if self.failed:
                                return retval


                        else:
                            break #loop157


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1863)
                    assignmentExpressionNoIn319 = self.assignmentExpressionNoIn()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpressionNoIn319.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:70: ( LT )*
                    while True: #loop158
                        alt158 = 2
                        LA158_0 = self.input.LA(1)

                        if (LA158_0 == LT) :
                            alt158 = 1


                        if alt158 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT320 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1865)
                            if self.failed:
                                return retval


                        else:
                            break #loop158


                    char_literal321 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_conditionalExpressionNoIn1869)
                    if self.failed:
                        return retval

                    char_literal321_tree = self.adaptor.createWithPayload(char_literal321)
                    self.adaptor.addChild(root_0, char_literal321_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:287:79: ( LT )*
                    while True: #loop159
                        alt159 = 2
                        LA159_0 = self.input.LA(1)

                        if (LA159_0 == LT) :
                            alt159 = 1


                        if alt159 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT322 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_conditionalExpressionNoIn1871)
                            if self.failed:
                                return retval


                        else:
                            break #loop159


                    self.following.append(self.FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1875)
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
                self.memoize(self.input, 55, conditionalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end conditionalExpressionNoIn

    class logicalORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:290:1: logicalORExpression : logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 56):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:2: ( logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:4: logicalANDExpression ( ( LT )* '||' ( LT )* logicalANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1888)
                logicalANDExpression324 = self.logicalANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpression324.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:25: ( ( LT )* '||' ( LT )* logicalANDExpression )*
                while True: #loop163
                    alt163 = 2
                    alt163 = self.dfa163.predict(self.input)
                    if alt163 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:26: ( LT )* '||' ( LT )* logicalANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:28: ( LT )*
                        while True: #loop161
                            alt161 = 2
                            LA161_0 = self.input.LA(1)

                            if (LA161_0 == LT) :
                                alt161 = 1


                            if alt161 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT325 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1891)
                                if self.failed:
                                    return retval


                            else:
                                break #loop161


                        string_literal326 = self.input.LT(1)
                        self.match(self.input, 87, self.FOLLOW_87_in_logicalORExpression1895)
                        if self.failed:
                            return retval

                        string_literal326_tree = self.adaptor.createWithPayload(string_literal326)
                        self.adaptor.addChild(root_0, string_literal326_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:291:38: ( LT )*
                        while True: #loop162
                            alt162 = 2
                            LA162_0 = self.input.LA(1)

                            if (LA162_0 == LT) :
                                alt162 = 1


                            if alt162 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT327 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpression1897)
                                if self.failed:
                                    return retval


                            else:
                                break #loop162


                        self.following.append(self.FOLLOW_logicalANDExpression_in_logicalORExpression1901)
                        logicalANDExpression328 = self.logicalANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpression328.tree)


                    else:
                        break #loop163





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 56, logicalORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpression

    class logicalORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:294:1: logicalORExpressionNoIn : logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 57):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:2: ( logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:4: logicalANDExpressionNoIn ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1915)
                logicalANDExpressionNoIn329 = self.logicalANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, logicalANDExpressionNoIn329.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:29: ( ( LT )* '||' ( LT )* logicalANDExpressionNoIn )*
                while True: #loop166
                    alt166 = 2
                    alt166 = self.dfa166.predict(self.input)
                    if alt166 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:30: ( LT )* '||' ( LT )* logicalANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:32: ( LT )*
                        while True: #loop164
                            alt164 = 2
                            LA164_0 = self.input.LA(1)

                            if (LA164_0 == LT) :
                                alt164 = 1


                            if alt164 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT330 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1918)
                                if self.failed:
                                    return retval


                            else:
                                break #loop164


                        string_literal331 = self.input.LT(1)
                        self.match(self.input, 87, self.FOLLOW_87_in_logicalORExpressionNoIn1922)
                        if self.failed:
                            return retval

                        string_literal331_tree = self.adaptor.createWithPayload(string_literal331)
                        self.adaptor.addChild(root_0, string_literal331_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:295:42: ( LT )*
                        while True: #loop165
                            alt165 = 2
                            LA165_0 = self.input.LA(1)

                            if (LA165_0 == LT) :
                                alt165 = 1


                            if alt165 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT332 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalORExpressionNoIn1924)
                                if self.failed:
                                    return retval


                            else:
                                break #loop165


                        self.following.append(self.FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1928)
                        logicalANDExpressionNoIn333 = self.logicalANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, logicalANDExpressionNoIn333.tree)


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
                self.memoize(self.input, 57, logicalORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalORExpressionNoIn

    class logicalANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:298:1: logicalANDExpression : bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 58):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:2: ( bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:4: bitwiseORExpression ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1942)
                bitwiseORExpression334 = self.bitwiseORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpression334.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:24: ( ( LT )* '&&' ( LT )* bitwiseORExpression )*
                while True: #loop169
                    alt169 = 2
                    alt169 = self.dfa169.predict(self.input)
                    if alt169 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:25: ( LT )* '&&' ( LT )* bitwiseORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:27: ( LT )*
                        while True: #loop167
                            alt167 = 2
                            LA167_0 = self.input.LA(1)

                            if (LA167_0 == LT) :
                                alt167 = 1


                            if alt167 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT335 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1945)
                                if self.failed:
                                    return retval


                            else:
                                break #loop167


                        string_literal336 = self.input.LT(1)
                        self.match(self.input, 88, self.FOLLOW_88_in_logicalANDExpression1949)
                        if self.failed:
                            return retval

                        string_literal336_tree = self.adaptor.createWithPayload(string_literal336)
                        self.adaptor.addChild(root_0, string_literal336_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:299:37: ( LT )*
                        while True: #loop168
                            alt168 = 2
                            LA168_0 = self.input.LA(1)

                            if (LA168_0 == LT) :
                                alt168 = 1


                            if alt168 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT337 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpression1951)
                                if self.failed:
                                    return retval


                            else:
                                break #loop168


                        self.following.append(self.FOLLOW_bitwiseORExpression_in_logicalANDExpression1955)
                        bitwiseORExpression338 = self.bitwiseORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpression338.tree)


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
                self.memoize(self.input, 58, logicalANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpression

    class logicalANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start logicalANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:302:1: logicalANDExpressionNoIn : bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 59):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:2: ( bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:4: bitwiseORExpressionNoIn ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1969)
                bitwiseORExpressionNoIn339 = self.bitwiseORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseORExpressionNoIn339.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:28: ( ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn )*
                while True: #loop172
                    alt172 = 2
                    alt172 = self.dfa172.predict(self.input)
                    if alt172 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:29: ( LT )* '&&' ( LT )* bitwiseORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:31: ( LT )*
                        while True: #loop170
                            alt170 = 2
                            LA170_0 = self.input.LA(1)

                            if (LA170_0 == LT) :
                                alt170 = 1


                            if alt170 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT340 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1972)
                                if self.failed:
                                    return retval


                            else:
                                break #loop170


                        string_literal341 = self.input.LT(1)
                        self.match(self.input, 88, self.FOLLOW_88_in_logicalANDExpressionNoIn1976)
                        if self.failed:
                            return retval

                        string_literal341_tree = self.adaptor.createWithPayload(string_literal341)
                        self.adaptor.addChild(root_0, string_literal341_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:303:41: ( LT )*
                        while True: #loop171
                            alt171 = 2
                            LA171_0 = self.input.LA(1)

                            if (LA171_0 == LT) :
                                alt171 = 1


                            if alt171 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT342 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_logicalANDExpressionNoIn1978)
                                if self.failed:
                                    return retval


                            else:
                                break #loop171


                        self.following.append(self.FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1982)
                        bitwiseORExpressionNoIn343 = self.bitwiseORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseORExpressionNoIn343.tree)


                    else:
                        break #loop172





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 59, logicalANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end logicalANDExpressionNoIn

    class bitwiseORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:306:1: bitwiseORExpression : bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 60):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:2: ( bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:4: bitwiseXORExpression ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1996)
                bitwiseXORExpression344 = self.bitwiseXORExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpression344.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:25: ( ( LT )* '|' ( LT )* bitwiseXORExpression )*
                while True: #loop175
                    alt175 = 2
                    alt175 = self.dfa175.predict(self.input)
                    if alt175 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:26: ( LT )* '|' ( LT )* bitwiseXORExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:28: ( LT )*
                        while True: #loop173
                            alt173 = 2
                            LA173_0 = self.input.LA(1)

                            if (LA173_0 == LT) :
                                alt173 = 1


                            if alt173 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT345 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression1999)
                                if self.failed:
                                    return retval


                            else:
                                break #loop173


                        char_literal346 = self.input.LT(1)
                        self.match(self.input, 89, self.FOLLOW_89_in_bitwiseORExpression2003)
                        if self.failed:
                            return retval

                        char_literal346_tree = self.adaptor.createWithPayload(char_literal346)
                        self.adaptor.addChild(root_0, char_literal346_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:307:37: ( LT )*
                        while True: #loop174
                            alt174 = 2
                            LA174_0 = self.input.LA(1)

                            if (LA174_0 == LT) :
                                alt174 = 1


                            if alt174 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT347 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpression2005)
                                if self.failed:
                                    return retval


                            else:
                                break #loop174


                        self.following.append(self.FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2009)
                        bitwiseXORExpression348 = self.bitwiseXORExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpression348.tree)


                    else:
                        break #loop175





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 60, bitwiseORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpression

    class bitwiseORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:310:1: bitwiseORExpressionNoIn : bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 61):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:2: ( bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:4: bitwiseXORExpressionNoIn ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2023)
                bitwiseXORExpressionNoIn349 = self.bitwiseXORExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn349.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:29: ( ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn )*
                while True: #loop178
                    alt178 = 2
                    alt178 = self.dfa178.predict(self.input)
                    if alt178 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:30: ( LT )* '|' ( LT )* bitwiseXORExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:32: ( LT )*
                        while True: #loop176
                            alt176 = 2
                            LA176_0 = self.input.LA(1)

                            if (LA176_0 == LT) :
                                alt176 = 1


                            if alt176 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT350 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2026)
                                if self.failed:
                                    return retval


                            else:
                                break #loop176


                        char_literal351 = self.input.LT(1)
                        self.match(self.input, 89, self.FOLLOW_89_in_bitwiseORExpressionNoIn2030)
                        if self.failed:
                            return retval

                        char_literal351_tree = self.adaptor.createWithPayload(char_literal351)
                        self.adaptor.addChild(root_0, char_literal351_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:311:41: ( LT )*
                        while True: #loop177
                            alt177 = 2
                            LA177_0 = self.input.LA(1)

                            if (LA177_0 == LT) :
                                alt177 = 1


                            if alt177 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT352 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseORExpressionNoIn2032)
                                if self.failed:
                                    return retval


                            else:
                                break #loop177


                        self.following.append(self.FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2036)
                        bitwiseXORExpressionNoIn353 = self.bitwiseXORExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseXORExpressionNoIn353.tree)


                    else:
                        break #loop178





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 61, bitwiseORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseORExpressionNoIn

    class bitwiseXORExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:314:1: bitwiseXORExpression : bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 62):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:2: ( bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:4: bitwiseANDExpression ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2050)
                bitwiseANDExpression354 = self.bitwiseANDExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpression354.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:25: ( ( LT )* '^' ( LT )* bitwiseANDExpression )*
                while True: #loop181
                    alt181 = 2
                    alt181 = self.dfa181.predict(self.input)
                    if alt181 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:26: ( LT )* '^' ( LT )* bitwiseANDExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:28: ( LT )*
                        while True: #loop179
                            alt179 = 2
                            LA179_0 = self.input.LA(1)

                            if (LA179_0 == LT) :
                                alt179 = 1


                            if alt179 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT355 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2053)
                                if self.failed:
                                    return retval


                            else:
                                break #loop179


                        char_literal356 = self.input.LT(1)
                        self.match(self.input, 90, self.FOLLOW_90_in_bitwiseXORExpression2057)
                        if self.failed:
                            return retval

                        char_literal356_tree = self.adaptor.createWithPayload(char_literal356)
                        self.adaptor.addChild(root_0, char_literal356_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:315:37: ( LT )*
                        while True: #loop180
                            alt180 = 2
                            LA180_0 = self.input.LA(1)

                            if (LA180_0 == LT) :
                                alt180 = 1


                            if alt180 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT357 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpression2059)
                                if self.failed:
                                    return retval


                            else:
                                break #loop180


                        self.following.append(self.FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2063)
                        bitwiseANDExpression358 = self.bitwiseANDExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpression358.tree)


                    else:
                        break #loop181





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 62, bitwiseXORExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpression

    class bitwiseXORExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseXORExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:318:1: bitwiseXORExpressionNoIn : bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 63):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:2: ( bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:4: bitwiseANDExpressionNoIn ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2077)
                bitwiseANDExpressionNoIn359 = self.bitwiseANDExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn359.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:29: ( ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn )*
                while True: #loop184
                    alt184 = 2
                    alt184 = self.dfa184.predict(self.input)
                    if alt184 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:30: ( LT )* '^' ( LT )* bitwiseANDExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:32: ( LT )*
                        while True: #loop182
                            alt182 = 2
                            LA182_0 = self.input.LA(1)

                            if (LA182_0 == LT) :
                                alt182 = 1


                            if alt182 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT360 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2080)
                                if self.failed:
                                    return retval


                            else:
                                break #loop182


                        char_literal361 = self.input.LT(1)
                        self.match(self.input, 90, self.FOLLOW_90_in_bitwiseXORExpressionNoIn2084)
                        if self.failed:
                            return retval

                        char_literal361_tree = self.adaptor.createWithPayload(char_literal361)
                        self.adaptor.addChild(root_0, char_literal361_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:319:41: ( LT )*
                        while True: #loop183
                            alt183 = 2
                            LA183_0 = self.input.LA(1)

                            if (LA183_0 == LT) :
                                alt183 = 1


                            if alt183 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT362 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseXORExpressionNoIn2086)
                                if self.failed:
                                    return retval


                            else:
                                break #loop183


                        self.following.append(self.FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2090)
                        bitwiseANDExpressionNoIn363 = self.bitwiseANDExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, bitwiseANDExpressionNoIn363.tree)


                    else:
                        break #loop184





                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 63, bitwiseXORExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseXORExpressionNoIn

    class bitwiseANDExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:322:1: bitwiseANDExpression : equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 64):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:2: ( equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:4: equalityExpression ( ( LT )* '&' ( LT )* equalityExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2104)
                equalityExpression364 = self.equalityExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpression364.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:23: ( ( LT )* '&' ( LT )* equalityExpression )*
                while True: #loop187
                    alt187 = 2
                    alt187 = self.dfa187.predict(self.input)
                    if alt187 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:24: ( LT )* '&' ( LT )* equalityExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:26: ( LT )*
                        while True: #loop185
                            alt185 = 2
                            LA185_0 = self.input.LA(1)

                            if (LA185_0 == LT) :
                                alt185 = 1


                            if alt185 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT365 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2107)
                                if self.failed:
                                    return retval


                            else:
                                break #loop185


                        char_literal366 = self.input.LT(1)
                        self.match(self.input, 91, self.FOLLOW_91_in_bitwiseANDExpression2111)
                        if self.failed:
                            return retval

                        char_literal366_tree = self.adaptor.createWithPayload(char_literal366)
                        self.adaptor.addChild(root_0, char_literal366_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:323:35: ( LT )*
                        while True: #loop186
                            alt186 = 2
                            LA186_0 = self.input.LA(1)

                            if (LA186_0 == LT) :
                                alt186 = 1


                            if alt186 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT367 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpression2113)
                                if self.failed:
                                    return retval


                            else:
                                break #loop186


                        self.following.append(self.FOLLOW_equalityExpression_in_bitwiseANDExpression2117)
                        equalityExpression368 = self.equalityExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpression368.tree)


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
                self.memoize(self.input, 64, bitwiseANDExpression_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpression

    class bitwiseANDExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start bitwiseANDExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:326:1: bitwiseANDExpressionNoIn : equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 65):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:2: ( equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:4: equalityExpressionNoIn ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2131)
                equalityExpressionNoIn369 = self.equalityExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, equalityExpressionNoIn369.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:27: ( ( LT )* '&' ( LT )* equalityExpressionNoIn )*
                while True: #loop190
                    alt190 = 2
                    alt190 = self.dfa190.predict(self.input)
                    if alt190 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:28: ( LT )* '&' ( LT )* equalityExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:30: ( LT )*
                        while True: #loop188
                            alt188 = 2
                            LA188_0 = self.input.LA(1)

                            if (LA188_0 == LT) :
                                alt188 = 1


                            if alt188 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT370 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2134)
                                if self.failed:
                                    return retval


                            else:
                                break #loop188


                        char_literal371 = self.input.LT(1)
                        self.match(self.input, 91, self.FOLLOW_91_in_bitwiseANDExpressionNoIn2138)
                        if self.failed:
                            return retval

                        char_literal371_tree = self.adaptor.createWithPayload(char_literal371)
                        self.adaptor.addChild(root_0, char_literal371_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:327:39: ( LT )*
                        while True: #loop189
                            alt189 = 2
                            LA189_0 = self.input.LA(1)

                            if (LA189_0 == LT) :
                                alt189 = 1


                            if alt189 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT372 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_bitwiseANDExpressionNoIn2140)
                                if self.failed:
                                    return retval


                            else:
                                break #loop189


                        self.following.append(self.FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2144)
                        equalityExpressionNoIn373 = self.equalityExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, equalityExpressionNoIn373.tree)


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
                self.memoize(self.input, 65, bitwiseANDExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end bitwiseANDExpressionNoIn

    class equalityExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:330:1: equalityExpression : relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 66):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:2: ( relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:4: relationalExpression ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2158)
                relationalExpression374 = self.relationalExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpression374.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:25: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression )*
                while True: #loop193
                    alt193 = 2
                    alt193 = self.dfa193.predict(self.input)
                    if alt193 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:26: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:28: ( LT )*
                        while True: #loop191
                            alt191 = 2
                            LA191_0 = self.input.LA(1)

                            if (LA191_0 == LT) :
                                alt191 = 1


                            if alt191 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT375 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2161)
                                if self.failed:
                                    return retval


                            else:
                                break #loop191


                        set376 = self.input.LT(1)
                        if (92 <= self.input.LA(1) <= 95):
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
                                self.input, mse, self.FOLLOW_set_in_equalityExpression2165
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:331:63: ( LT )*
                        while True: #loop192
                            alt192 = 2
                            LA192_0 = self.input.LA(1)

                            if (LA192_0 == LT) :
                                alt192 = 1


                            if alt192 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT377 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpression2181)
                                if self.failed:
                                    return retval


                            else:
                                break #loop192


                        self.following.append(self.FOLLOW_relationalExpression_in_equalityExpression2185)
                        relationalExpression378 = self.relationalExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpression378.tree)


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
                self.memoize(self.input, 66, equalityExpression_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpression

    class equalityExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start equalityExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:334:1: equalityExpressionNoIn : relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 67):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:2: ( relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:4: relationalExpressionNoIn ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2198)
                relationalExpressionNoIn379 = self.relationalExpressionNoIn()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, relationalExpressionNoIn379.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:29: ( ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn )*
                while True: #loop196
                    alt196 = 2
                    alt196 = self.dfa196.predict(self.input)
                    if alt196 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:30: ( LT )* ( '==' | '!=' | '===' | '!==' ) ( LT )* relationalExpressionNoIn
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:32: ( LT )*
                        while True: #loop194
                            alt194 = 2
                            LA194_0 = self.input.LA(1)

                            if (LA194_0 == LT) :
                                alt194 = 1


                            if alt194 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT380 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2201)
                                if self.failed:
                                    return retval


                            else:
                                break #loop194


                        set381 = self.input.LT(1)
                        if (92 <= self.input.LA(1) <= 95):
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
                                self.input, mse, self.FOLLOW_set_in_equalityExpressionNoIn2205
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:335:67: ( LT )*
                        while True: #loop195
                            alt195 = 2
                            LA195_0 = self.input.LA(1)

                            if (LA195_0 == LT) :
                                alt195 = 1


                            if alt195 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT382 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_equalityExpressionNoIn2221)
                                if self.failed:
                                    return retval


                            else:
                                break #loop195


                        self.following.append(self.FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2225)
                        relationalExpressionNoIn383 = self.relationalExpressionNoIn()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, relationalExpressionNoIn383.tree)


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
                self.memoize(self.input, 67, equalityExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end equalityExpressionNoIn

    class relationalExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:338:1: relationalExpression : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 68):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2239)
                shiftExpression384 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression384.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression )*
                while True: #loop199
                    alt199 = 2
                    alt199 = self.dfa199.predict(self.input)
                    if alt199 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' | 'in' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:23: ( LT )*
                        while True: #loop197
                            alt197 = 2
                            LA197_0 = self.input.LA(1)

                            if (LA197_0 == LT) :
                                alt197 = 1


                            if alt197 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT385 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2242)
                                if self.failed:
                                    return retval


                            else:
                                break #loop197


                        set386 = self.input.LT(1)
                        if self.input.LA(1) == 58 or (96 <= self.input.LA(1) <= 100):
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
                                self.input, mse, self.FOLLOW_set_in_relationalExpression2246
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:339:76: ( LT )*
                        while True: #loop198
                            alt198 = 2
                            LA198_0 = self.input.LA(1)

                            if (LA198_0 == LT) :
                                alt198 = 1


                            if alt198 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT387 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpression2270)
                                if self.failed:
                                    return retval


                            else:
                                break #loop198


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpression2274)
                        shiftExpression388 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression388.tree)


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
                self.memoize(self.input, 68, relationalExpression_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpression

    class relationalExpressionNoIn_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start relationalExpressionNoIn
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:342:1: relationalExpressionNoIn : shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 69):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:2: ( shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:4: shiftExpression ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2287)
                shiftExpression389 = self.shiftExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, shiftExpression389.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:20: ( ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression )*
                while True: #loop202
                    alt202 = 2
                    alt202 = self.dfa202.predict(self.input)
                    if alt202 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:21: ( LT )* ( '<' | '>' | '<=' | '>=' | 'instanceof' ) ( LT )* shiftExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:23: ( LT )*
                        while True: #loop200
                            alt200 = 2
                            LA200_0 = self.input.LA(1)

                            if (LA200_0 == LT) :
                                alt200 = 1


                            if alt200 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT390 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2290)
                                if self.failed:
                                    return retval


                            else:
                                break #loop200


                        set391 = self.input.LT(1)
                        if (96 <= self.input.LA(1) <= 100):
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
                                self.input, mse, self.FOLLOW_set_in_relationalExpressionNoIn2294
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:343:69: ( LT )*
                        while True: #loop201
                            alt201 = 2
                            LA201_0 = self.input.LA(1)

                            if (LA201_0 == LT) :
                                alt201 = 1


                            if alt201 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT392 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_relationalExpressionNoIn2314)
                                if self.failed:
                                    return retval


                            else:
                                break #loop201


                        self.following.append(self.FOLLOW_shiftExpression_in_relationalExpressionNoIn2318)
                        shiftExpression393 = self.shiftExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, shiftExpression393.tree)


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
                self.memoize(self.input, 69, relationalExpressionNoIn_StartIndex)

            pass

        return retval

    # $ANTLR end relationalExpressionNoIn

    class shiftExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start shiftExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:346:1: shiftExpression : additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 70):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:2: ( additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:4: additiveExpression ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2331)
                additiveExpression394 = self.additiveExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, additiveExpression394.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:23: ( ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression )*
                while True: #loop205
                    alt205 = 2
                    alt205 = self.dfa205.predict(self.input)
                    if alt205 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:24: ( LT )* ( '<<' | '>>' | '>>>' ) ( LT )* additiveExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:26: ( LT )*
                        while True: #loop203
                            alt203 = 2
                            LA203_0 = self.input.LA(1)

                            if (LA203_0 == LT) :
                                alt203 = 1


                            if alt203 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT395 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2334)
                                if self.failed:
                                    return retval


                            else:
                                break #loop203


                        set396 = self.input.LT(1)
                        if (101 <= self.input.LA(1) <= 103):
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
                                self.input, mse, self.FOLLOW_set_in_shiftExpression2338
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:347:53: ( LT )*
                        while True: #loop204
                            alt204 = 2
                            LA204_0 = self.input.LA(1)

                            if (LA204_0 == LT) :
                                alt204 = 1


                            if alt204 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT397 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_shiftExpression2350)
                                if self.failed:
                                    return retval


                            else:
                                break #loop204


                        self.following.append(self.FOLLOW_additiveExpression_in_shiftExpression2354)
                        additiveExpression398 = self.additiveExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, additiveExpression398.tree)


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
                self.memoize(self.input, 70, shiftExpression_StartIndex)

            pass

        return retval

    # $ANTLR end shiftExpression

    class additiveExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start additiveExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:350:1: additiveExpression : multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 71):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:2: ( multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:4: multiplicativeExpression ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2367)
                multiplicativeExpression399 = self.multiplicativeExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, multiplicativeExpression399.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:29: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )*
                while True: #loop208
                    alt208 = 2
                    LA208_0 = self.input.LA(1)

                    if (LA208_0 == LT) :
                        LA208_1 = self.input.LA(2)

                        if (self.synpred259()) :
                            alt208 = 1


                    elif ((104 <= LA208_0 <= 105)) :
                        alt208 = 1


                    if alt208 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:32: ( LT )*
                        while True: #loop206
                            alt206 = 2
                            LA206_0 = self.input.LA(1)

                            if (LA206_0 == LT) :
                                alt206 = 1


                            if alt206 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT400 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2370)
                                if self.failed:
                                    return retval


                            else:
                                break #loop206


                        set401 = self.input.LT(1)
                        if (104 <= self.input.LA(1) <= 105):
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
                                self.input, mse, self.FOLLOW_set_in_additiveExpression2374
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:49: ( LT )*
                        while True: #loop207
                            alt207 = 2
                            LA207_0 = self.input.LA(1)

                            if (LA207_0 == LT) :
                                alt207 = 1


                            if alt207 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT402 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_additiveExpression2382)
                                if self.failed:
                                    return retval


                            else:
                                break #loop207


                        self.following.append(self.FOLLOW_multiplicativeExpression_in_additiveExpression2386)
                        multiplicativeExpression403 = self.multiplicativeExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, multiplicativeExpression403.tree)


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
                self.memoize(self.input, 71, additiveExpression_StartIndex)

            pass

        return retval

    # $ANTLR end additiveExpression

    class multiplicativeExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start multiplicativeExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:354:1: multiplicativeExpression : unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 72):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:2: ( unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )* )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:4: unaryExpression ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2399)
                unaryExpression404 = self.unaryExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, unaryExpression404.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:20: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )*
                while True: #loop211
                    alt211 = 2
                    LA211_0 = self.input.LA(1)

                    if (LA211_0 == LT) :
                        LA211_1 = self.input.LA(2)

                        if (self.synpred264()) :
                            alt211 = 1


                    elif ((106 <= LA211_0 <= 108)) :
                        alt211 = 1


                    if alt211 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:23: ( LT )*
                        while True: #loop209
                            alt209 = 2
                            LA209_0 = self.input.LA(1)

                            if (LA209_0 == LT) :
                                alt209 = 1


                            if alt209 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT405 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2402)
                                if self.failed:
                                    return retval


                            else:
                                break #loop209


                        set406 = self.input.LT(1)
                        if (106 <= self.input.LA(1) <= 108):
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
                                self.input, mse, self.FOLLOW_set_in_multiplicativeExpression2406
                                )
                            raise mse


                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:46: ( LT )*
                        while True: #loop210
                            alt210 = 2
                            LA210_0 = self.input.LA(1)

                            if (LA210_0 == LT) :
                                alt210 = 1


                            if alt210 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT407 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_multiplicativeExpression2418)
                                if self.failed:
                                    return retval


                            else:
                                break #loop210


                        self.following.append(self.FOLLOW_unaryExpression_in_multiplicativeExpression2422)
                        unaryExpression408 = self.unaryExpression()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, unaryExpression408.tree)


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
                self.memoize(self.input, 72, multiplicativeExpression_StartIndex)

            pass

        return retval

    # $ANTLR end multiplicativeExpression

    class unaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start unaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:358:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 73):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:2: ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression )
                alt212 = 2
                LA212_0 = self.input.LA(1)

                if ((StringLiteral <= LA212_0 <= Identifier) or (42 <= LA212_0 <= 43) or LA212_0 == 46 or LA212_0 == 57 or (71 <= LA212_0 <= 72) or LA212_0 == 107 or (116 <= LA212_0 <= 121)) :
                    alt212 = 1
                elif ((104 <= LA212_0 <= 105) or (109 <= LA212_0 <= 115)) :
                    alt212 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("358:1: unaryExpression : ( postfixExpression | ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression );", 212, 0, self.input)

                    raise nvae

                if alt212 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:359:4: postfixExpression
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_postfixExpression_in_unaryExpression2435)
                    postfixExpression409 = self.postfixExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, postfixExpression409.tree)


                elif alt212 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:360:4: ( 'delete' | 'void' | 'typeof' | '++' | '--' | '+' | '-' | '~' | '!' ) unaryExpression
                    root_0 = self.adaptor.nil()

                    set410 = self.input.LT(1)
                    if (104 <= self.input.LA(1) <= 105) or (109 <= self.input.LA(1) <= 115):
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
                            self.input, mse, self.FOLLOW_set_in_unaryExpression2440
                            )
                        raise mse


                    self.following.append(self.FOLLOW_unaryExpression_in_unaryExpression2476)
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
                self.memoize(self.input, 73, unaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end unaryExpression

    class postfixExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start postfixExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:363:1: postfixExpression : leftHandSideExpression ( '++' | '--' )? ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 74):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:2: ( leftHandSideExpression ( '++' | '--' )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:4: leftHandSideExpression ( '++' | '--' )?
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_leftHandSideExpression_in_postfixExpression2488)
                leftHandSideExpression412 = self.leftHandSideExpression()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, leftHandSideExpression412.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:364:27: ( '++' | '--' )?
                alt213 = 2
                LA213_0 = self.input.LA(1)

                if ((112 <= LA213_0 <= 113)) :
                    alt213 = 1
                if alt213 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                    set413 = self.input.LT(1)
                    if (112 <= self.input.LA(1) <= 113):
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
                            self.input, mse, self.FOLLOW_set_in_postfixExpression2490
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
                self.memoize(self.input, 74, postfixExpression_StartIndex)

            pass

        return retval

    # $ANTLR end postfixExpression

    class primaryExpression_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start primaryExpression
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:367:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 75):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:2: ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' )
                alt216 = 6
                LA216 = self.input.LA(1)
                if LA216 == 116:
                    alt216 = 1
                elif LA216 == Identifier or LA216 == 57 or LA216 == 117 or LA216 == 118:
                    alt216 = 2
                elif LA216 == StringLiteral or LA216 == NumericLiteral or LA216 == 107 or LA216 == 119 or LA216 == 120 or LA216 == 121:
                    alt216 = 3
                elif LA216 == 72:
                    alt216 = 4
                elif LA216 == 46:
                    alt216 = 5
                elif LA216 == 43:
                    alt216 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("367:1: primaryExpression : ( 'this' | identifier | literal | arrayLiteral | objectLiteral | '(' ( LT )* expression ( LT )* ')' );", 216, 0, self.input)

                    raise nvae

                if alt216 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:368:4: 'this'
                    root_0 = self.adaptor.nil()

                    string_literal414 = self.input.LT(1)
                    self.match(self.input, 116, self.FOLLOW_116_in_primaryExpression2508)
                    if self.failed:
                        return retval

                    string_literal414_tree = self.adaptor.createWithPayload(string_literal414)
                    self.adaptor.addChild(root_0, string_literal414_tree)



                elif alt216 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:369:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_primaryExpression2513)
                    identifier415 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier415.tree)


                elif alt216 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:370:4: literal
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_literal_in_primaryExpression2518)
                    literal416 = self.literal()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, literal416.tree)


                elif alt216 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:371:4: arrayLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_arrayLiteral_in_primaryExpression2523)
                    arrayLiteral417 = self.arrayLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, arrayLiteral417.tree)


                elif alt216 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:372:4: objectLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_objectLiteral_in_primaryExpression2528)
                    objectLiteral418 = self.objectLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, objectLiteral418.tree)


                elif alt216 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:4: '(' ( LT )* expression ( LT )* ')'
                    root_0 = self.adaptor.nil()

                    char_literal419 = self.input.LT(1)
                    self.match(self.input, 43, self.FOLLOW_43_in_primaryExpression2533)
                    if self.failed:
                        return retval

                    char_literal419_tree = self.adaptor.createWithPayload(char_literal419)
                    self.adaptor.addChild(root_0, char_literal419_tree)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:10: ( LT )*
                    while True: #loop214
                        alt214 = 2
                        LA214_0 = self.input.LA(1)

                        if (LA214_0 == LT) :
                            alt214 = 1


                        if alt214 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT420 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2535)
                            if self.failed:
                                return retval


                        else:
                            break #loop214


                    self.following.append(self.FOLLOW_expression_in_primaryExpression2539)
                    expression421 = self.expression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, expression421.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:373:26: ( LT )*
                    while True: #loop215
                        alt215 = 2
                        LA215_0 = self.input.LA(1)

                        if (LA215_0 == LT) :
                            alt215 = 1


                        if alt215 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT422 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_primaryExpression2541)
                            if self.failed:
                                return retval


                        else:
                            break #loop215


                    char_literal423 = self.input.LT(1)
                    self.match(self.input, 45, self.FOLLOW_45_in_primaryExpression2545)
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
                self.memoize(self.input, 75, primaryExpression_StartIndex)

            pass

        return retval

    # $ANTLR end primaryExpression

    class arrayLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start arrayLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:377:1: arrayLiteral : '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' ;
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
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 76):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:2: ( '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']' )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:4: '[' ( LT )* ( assignmentExpression )? ( ( LT )* ',' ( ( LT )* assignmentExpression )? )* ( LT )* ']'
                root_0 = self.adaptor.nil()

                char_literal424 = self.input.LT(1)
                self.match(self.input, 72, self.FOLLOW_72_in_arrayLiteral2558)
                if self.failed:
                    return retval

                char_literal424_tree = self.adaptor.createWithPayload(char_literal424)
                self.adaptor.addChild(root_0, char_literal424_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:10: ( LT )*
                while True: #loop217
                    alt217 = 2
                    LA217_0 = self.input.LA(1)

                    if (LA217_0 == LT) :
                        LA217_2 = self.input.LA(2)

                        if (self.synpred283()) :
                            alt217 = 1




                    if alt217 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT425 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2560)
                        if self.failed:
                            return retval


                    else:
                        break #loop217


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:13: ( assignmentExpression )?
                alt218 = 2
                LA218_0 = self.input.LA(1)

                if ((StringLiteral <= LA218_0 <= Identifier) or (42 <= LA218_0 <= 43) or LA218_0 == 46 or LA218_0 == 57 or (71 <= LA218_0 <= 72) or (104 <= LA218_0 <= 105) or LA218_0 == 107 or (109 <= LA218_0 <= 121)) :
                    alt218 = 1
                if alt218 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: assignmentExpression
                    self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2564)
                    assignmentExpression426 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, assignmentExpression426.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:35: ( ( LT )* ',' ( ( LT )* assignmentExpression )? )*
                while True: #loop222
                    alt222 = 2
                    alt222 = self.dfa222.predict(self.input)
                    if alt222 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:36: ( LT )* ',' ( ( LT )* assignmentExpression )?
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:38: ( LT )*
                        while True: #loop219
                            alt219 = 2
                            LA219_0 = self.input.LA(1)

                            if (LA219_0 == LT) :
                                alt219 = 1


                            if alt219 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT427 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2568)
                                if self.failed:
                                    return retval


                            else:
                                break #loop219


                        char_literal428 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_arrayLiteral2572)
                        if self.failed:
                            return retval

                        char_literal428_tree = self.adaptor.createWithPayload(char_literal428)
                        self.adaptor.addChild(root_0, char_literal428_tree)

                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:45: ( ( LT )* assignmentExpression )?
                        alt221 = 2
                        alt221 = self.dfa221.predict(self.input)
                        if alt221 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:46: ( LT )* assignmentExpression
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:48: ( LT )*
                            while True: #loop220
                                alt220 = 2
                                LA220_0 = self.input.LA(1)

                                if (LA220_0 == LT) :
                                    alt220 = 1


                                if alt220 == 1:
                                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                    LT429 = self.input.LT(1)
                                    self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2575)
                                    if self.failed:
                                        return retval


                                else:
                                    break #loop220


                            self.following.append(self.FOLLOW_assignmentExpression_in_arrayLiteral2579)
                            assignmentExpression430 = self.assignmentExpression()
                            self.following.pop()
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                self.adaptor.addChild(root_0, assignmentExpression430.tree)





                    else:
                        break #loop222


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:78: ( LT )*
                while True: #loop223
                    alt223 = 2
                    LA223_0 = self.input.LA(1)

                    if (LA223_0 == LT) :
                        alt223 = 1


                    if alt223 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT431 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_arrayLiteral2585)
                        if self.failed:
                            return retval


                    else:
                        break #loop223


                char_literal432 = self.input.LT(1)
                self.match(self.input, 73, self.FOLLOW_73_in_arrayLiteral2589)
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
                self.memoize(self.input, 76, arrayLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end arrayLiteral

    class objectLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start objectLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:382:1: objectLiteral : '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) ;
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
        stream_44 = RewriteRuleTokenStream(self.adaptor, "token 44")
        stream_47 = RewriteRuleTokenStream(self.adaptor, "token 47")
        stream_46 = RewriteRuleTokenStream(self.adaptor, "token 46")
        stream_propertyNameAndValue = RewriteRuleSubtreeStream(self.adaptor, "rule propertyNameAndValue")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 77):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:2: ( '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}' -> ^( OBJ ( propertyNameAndValue )* ) )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:4: '{' ( LT )* ( propertyNameAndValue )? ( ( LT )* ',' ( LT )* propertyNameAndValue )* ( LT )* '}'
                char_literal433 = self.input.LT(1)
                self.match(self.input, 46, self.FOLLOW_46_in_objectLiteral2608)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_46.add(char_literal433)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:8: ( LT )*
                while True: #loop224
                    alt224 = 2
                    LA224_0 = self.input.LA(1)

                    if (LA224_0 == LT) :
                        LA224_2 = self.input.LA(2)

                        if (self.synpred290()) :
                            alt224 = 1




                    if alt224 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT434 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2610)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT434)


                    else:
                        break #loop224


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:12: ( propertyNameAndValue )?
                alt225 = 2
                LA225_0 = self.input.LA(1)

                if ((StringLiteral <= LA225_0 <= Identifier) or LA225_0 == 57 or (117 <= LA225_0 <= 118)) :
                    alt225 = 1
                if alt225 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: propertyNameAndValue
                    self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2613)
                    propertyNameAndValue435 = self.propertyNameAndValue()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyNameAndValue.add(propertyNameAndValue435.tree)



                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:34: ( ( LT )* ',' ( LT )* propertyNameAndValue )*
                while True: #loop228
                    alt228 = 2
                    alt228 = self.dfa228.predict(self.input)
                    if alt228 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:35: ( LT )* ',' ( LT )* propertyNameAndValue
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:35: ( LT )*
                        while True: #loop226
                            alt226 = 2
                            LA226_0 = self.input.LA(1)

                            if (LA226_0 == LT) :
                                alt226 = 1


                            if alt226 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT436 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2617)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT436)


                            else:
                                break #loop226


                        char_literal437 = self.input.LT(1)
                        self.match(self.input, 44, self.FOLLOW_44_in_objectLiteral2620)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_44.add(char_literal437)
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:43: ( LT )*
                        while True: #loop227
                            alt227 = 2
                            LA227_0 = self.input.LA(1)

                            if (LA227_0 == LT) :
                                alt227 = 1


                            if alt227 == 1:
                                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                                LT438 = self.input.LT(1)
                                self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2622)
                                if self.failed:
                                    return retval
                                if self.backtracking == 0:
                                    stream_LT.add(LT438)


                            else:
                                break #loop227


                        self.following.append(self.FOLLOW_propertyNameAndValue_in_objectLiteral2625)
                        propertyNameAndValue439 = self.propertyNameAndValue()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_propertyNameAndValue.add(propertyNameAndValue439.tree)


                    else:
                        break #loop228


                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:70: ( LT )*
                while True: #loop229
                    alt229 = 2
                    LA229_0 = self.input.LA(1)

                    if (LA229_0 == LT) :
                        alt229 = 1


                    if alt229 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                        LT440 = self.input.LT(1)
                        self.match(self.input, LT, self.FOLLOW_LT_in_objectLiteral2629)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_LT.add(LT440)


                    else:
                        break #loop229


                char_literal441 = self.input.LT(1)
                self.match(self.input, 47, self.FOLLOW_47_in_objectLiteral2632)
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    stream_47.add(char_literal441)
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
                    # 384:3: -> ^( OBJ ( propertyNameAndValue )* )
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:6: ^( OBJ ( propertyNameAndValue )* )
                    root_1 = self.adaptor.nil()
                    root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(OBJ, "OBJ"), root_1)

                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:384:12: ( propertyNameAndValue )*
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
                self.memoize(self.input, 77, objectLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end objectLiteral

    class propertyNameAndValue_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyNameAndValue
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:387:1: propertyNameAndValue : ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) );
    def propertyNameAndValue(self, ):

        retval = self.propertyNameAndValue_return()
        retval.start = self.input.LT(1)
        propertyNameAndValue_StartIndex = self.input.index()
        root_0 = None

        action = None
        LT443 = None
        char_literal444 = None
        LT445 = None
        LT447 = None
        LT448 = None
        LT450 = None
        LT452 = None
        LT454 = None
        LT456 = None
        propname = None

        funcname = None

        propertyName442 = None

        assignmentExpression446 = None

        formalParameterList449 = None

        statementBlock451 = None

        identifier453 = None

        formalParameterList455 = None

        statementBlock457 = None


        action_tree = None
        LT443_tree = None
        char_literal444_tree = None
        LT445_tree = None
        LT447_tree = None
        LT448_tree = None
        LT450_tree = None
        LT452_tree = None
        LT454_tree = None
        LT456_tree = None
        stream_117 = RewriteRuleTokenStream(self.adaptor, "token 117")
        stream_LT = RewriteRuleTokenStream(self.adaptor, "token LT")
        stream_63 = RewriteRuleTokenStream(self.adaptor, "token 63")
        stream_118 = RewriteRuleTokenStream(self.adaptor, "token 118")
        stream_propertyName = RewriteRuleSubtreeStream(self.adaptor, "rule propertyName")
        stream_assignmentExpression = RewriteRuleSubtreeStream(self.adaptor, "rule assignmentExpression")
        stream_statementBlock = RewriteRuleSubtreeStream(self.adaptor, "rule statementBlock")
        stream_identifier = RewriteRuleSubtreeStream(self.adaptor, "rule identifier")
        stream_formalParameterList = RewriteRuleSubtreeStream(self.adaptor, "rule formalParameterList")
        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 78):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:2: ( propertyName ( LT )* ':' ( LT )* assignmentExpression -> ^( PROP propertyName PROP assignmentExpression ) | (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) ) | (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) ) )
                alt240 = 3
                alt240 = self.dfa240.predict(self.input)
                if alt240 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:4: propertyName ( LT )* ':' ( LT )* assignmentExpression
                    self.following.append(self.FOLLOW_propertyName_in_propertyNameAndValue2656)
                    propertyName442 = self.propertyName()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_propertyName.add(propertyName442.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:17: ( LT )*
                    while True: #loop230
                        alt230 = 2
                        LA230_0 = self.input.LA(1)

                        if (LA230_0 == LT) :
                            alt230 = 1


                        if alt230 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT443 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2658)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT443)


                        else:
                            break #loop230


                    char_literal444 = self.input.LT(1)
                    self.match(self.input, 63, self.FOLLOW_63_in_propertyNameAndValue2661)
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_63.add(char_literal444)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:388:25: ( LT )*
                    while True: #loop231
                        alt231 = 2
                        LA231_0 = self.input.LA(1)

                        if (LA231_0 == LT) :
                            alt231 = 1


                        if alt231 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT445 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2663)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT445)


                        else:
                            break #loop231


                    self.following.append(self.FOLLOW_assignmentExpression_in_propertyNameAndValue2666)
                    assignmentExpression446 = self.assignmentExpression()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_assignmentExpression.add(assignmentExpression446.tree)
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
                        # 389:3: -> ^( PROP propertyName PROP assignmentExpression )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:389:6: ^( PROP propertyName PROP assignmentExpression )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propertyName.next())
                        self.adaptor.addChild(root_1, self.adaptor.createFromType(PROP, "PROP"))
                        self.adaptor.addChild(root_1, stream_assignmentExpression.next())

                        self.adaptor.addChild(root_0, root_1)





                elif alt240 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:4: (action= 'get' | action= 'set' ) propname= identifier ( LT )* funcname= identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:4: (action= 'get' | action= 'set' )
                    alt232 = 2
                    LA232_0 = self.input.LA(1)

                    if (LA232_0 == 117) :
                        alt232 = 1
                    elif (LA232_0 == 118) :
                        alt232 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("390:4: (action= 'get' | action= 'set' )", 232, 0, self.input)

                        raise nvae

                    if alt232 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_propertyNameAndValue2688)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_117.add(action)


                    elif alt232 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 118, self.FOLLOW_118_in_propertyNameAndValue2692)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_118.add(action)



                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2697)
                    propname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(propname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:52: ( LT )*
                    while True: #loop233
                        alt233 = 2
                        LA233_0 = self.input.LA(1)

                        if (LA233_0 == LT) :
                            alt233 = 1


                        if alt233 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT447 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2699)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT447)


                        else:
                            break #loop233


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2704)
                    funcname = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(funcname.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:76: ( LT )*
                    while True: #loop234
                        alt234 = 2
                        LA234_0 = self.input.LA(1)

                        if (LA234_0 == LT) :
                            alt234 = 1


                        if alt234 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT448 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2706)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT448)


                        else:
                            break #loop234


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue2709)
                    formalParameterList449 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList449.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:390:100: ( LT )*
                    while True: #loop235
                        alt235 = 2
                        LA235_0 = self.input.LA(1)

                        if (LA235_0 == LT) :
                            alt235 = 1


                        if alt235 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT450 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2711)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT450)


                        else:
                            break #loop235


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue2714)
                    statementBlock451 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock451.tree)
                    # AST Rewrite
                    # elements: formalParameterList, action, statementBlock, funcname, propname
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
                        # 391:3: -> ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:391:6: ^( PROP $propname $action ^( FUNC $funcname formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_propname.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:391:31: ^( FUNC $funcname formalParameterList statementBlock )
                        root_2 = self.adaptor.nil()
                        root_2 = self.adaptor.becomeRoot(self.adaptor.createFromType(FUNC, "FUNC"), root_2)

                        self.adaptor.addChild(root_2, stream_funcname.next())
                        self.adaptor.addChild(root_2, stream_formalParameterList.next())
                        self.adaptor.addChild(root_2, stream_statementBlock.next())

                        self.adaptor.addChild(root_1, root_2)

                        self.adaptor.addChild(root_0, root_1)





                elif alt240 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:4: (action= 'get' | action= 'set' ) ( LT )* identifier ( LT )* formalParameterList ( LT )* statementBlock
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:4: (action= 'get' | action= 'set' )
                    alt236 = 2
                    LA236_0 = self.input.LA(1)

                    if (LA236_0 == 117) :
                        alt236 = 1
                    elif (LA236_0 == 118) :
                        alt236 = 2
                    else:
                        if self.backtracking > 0:
                            self.failed = True
                            return retval

                        nvae = NoViableAltException("392:4: (action= 'get' | action= 'set' )", 236, 0, self.input)

                        raise nvae

                    if alt236 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:5: action= 'get'
                        action = self.input.LT(1)
                        self.match(self.input, 117, self.FOLLOW_117_in_propertyNameAndValue2747)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_117.add(action)


                    elif alt236 == 2:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:18: action= 'set'
                        action = self.input.LT(1)
                        self.match(self.input, 118, self.FOLLOW_118_in_propertyNameAndValue2751)
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            stream_118.add(action)



                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:32: ( LT )*
                    while True: #loop237
                        alt237 = 2
                        LA237_0 = self.input.LA(1)

                        if (LA237_0 == LT) :
                            alt237 = 1


                        if alt237 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT452 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2754)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT452)


                        else:
                            break #loop237


                    self.following.append(self.FOLLOW_identifier_in_propertyNameAndValue2757)
                    identifier453 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_identifier.add(identifier453.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:47: ( LT )*
                    while True: #loop238
                        alt238 = 2
                        LA238_0 = self.input.LA(1)

                        if (LA238_0 == LT) :
                            alt238 = 1


                        if alt238 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT454 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2759)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT454)


                        else:
                            break #loop238


                    self.following.append(self.FOLLOW_formalParameterList_in_propertyNameAndValue2762)
                    formalParameterList455 = self.formalParameterList()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_formalParameterList.add(formalParameterList455.tree)
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:392:71: ( LT )*
                    while True: #loop239
                        alt239 = 2
                        LA239_0 = self.input.LA(1)

                        if (LA239_0 == LT) :
                            alt239 = 1


                        if alt239 == 1:
                            # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                            LT456 = self.input.LT(1)
                            self.match(self.input, LT, self.FOLLOW_LT_in_propertyNameAndValue2764)
                            if self.failed:
                                return retval
                            if self.backtracking == 0:
                                stream_LT.add(LT456)


                        else:
                            break #loop239


                    self.following.append(self.FOLLOW_statementBlock_in_propertyNameAndValue2767)
                    statementBlock457 = self.statementBlock()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        stream_statementBlock.add(statementBlock457.tree)
                    # AST Rewrite
                    # elements: formalParameterList, action, statementBlock, identifier
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
                        # 393:3: -> ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:393:6: ^( PROP identifier $action ^( FUNC ANONYMOUS formalParameterList statementBlock ) )
                        root_1 = self.adaptor.nil()
                        root_1 = self.adaptor.becomeRoot(self.adaptor.createFromType(PROP, "PROP"), root_1)

                        self.adaptor.addChild(root_1, stream_identifier.next())
                        self.adaptor.addChild(root_1, stream_action.next())
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:393:32: ^( FUNC ANONYMOUS formalParameterList statementBlock )
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
                self.memoize(self.input, 78, propertyNameAndValue_StartIndex)

            pass

        return retval

    # $ANTLR end propertyNameAndValue

    class propertyName_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start propertyName
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:396:1: propertyName : ( identifier | StringLiteral | NumericLiteral );
    def propertyName(self, ):

        retval = self.propertyName_return()
        retval.start = self.input.LT(1)
        propertyName_StartIndex = self.input.index()
        root_0 = None

        StringLiteral459 = None
        NumericLiteral460 = None
        identifier458 = None


        StringLiteral459_tree = None
        NumericLiteral460_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 79):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:397:2: ( identifier | StringLiteral | NumericLiteral )
                alt241 = 3
                LA241 = self.input.LA(1)
                if LA241 == Identifier or LA241 == 57 or LA241 == 117 or LA241 == 118:
                    alt241 = 1
                elif LA241 == StringLiteral:
                    alt241 = 2
                elif LA241 == NumericLiteral:
                    alt241 = 3
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("396:1: propertyName : ( identifier | StringLiteral | NumericLiteral );", 241, 0, self.input)

                    raise nvae

                if alt241 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:397:4: identifier
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_identifier_in_propertyName2801)
                    identifier458 = self.identifier()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, identifier458.tree)


                elif alt241 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:398:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral459 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_propertyName2806)
                    if self.failed:
                        return retval

                    StringLiteral459_tree = self.adaptor.createWithPayload(StringLiteral459)
                    self.adaptor.addChild(root_0, StringLiteral459_tree)



                elif alt241 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:399:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral460 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_propertyName2811)
                    if self.failed:
                        return retval

                    NumericLiteral460_tree = self.adaptor.createWithPayload(NumericLiteral460)
                    self.adaptor.addChild(root_0, NumericLiteral460_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 79, propertyName_StartIndex)

            pass

        return retval

    # $ANTLR end propertyName

    class literal_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start literal
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:403:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)
        literal_StartIndex = self.input.index()
        root_0 = None

        string_literal461 = None
        string_literal462 = None
        string_literal463 = None
        StringLiteral464 = None
        NumericLiteral465 = None
        regularExpressionLiteral466 = None


        string_literal461_tree = None
        string_literal462_tree = None
        string_literal463_tree = None
        StringLiteral464_tree = None
        NumericLiteral465_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 80):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:2: ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral )
                alt242 = 6
                LA242 = self.input.LA(1)
                if LA242 == 119:
                    alt242 = 1
                elif LA242 == 120:
                    alt242 = 2
                elif LA242 == 121:
                    alt242 = 3
                elif LA242 == StringLiteral:
                    alt242 = 4
                elif LA242 == NumericLiteral:
                    alt242 = 5
                elif LA242 == 107:
                    alt242 = 6
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("403:1: literal : ( 'null' | 'true' | 'false' | StringLiteral | NumericLiteral | regularExpressionLiteral );", 242, 0, self.input)

                    raise nvae

                if alt242 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:404:4: 'null'
                    root_0 = self.adaptor.nil()

                    string_literal461 = self.input.LT(1)
                    self.match(self.input, 119, self.FOLLOW_119_in_literal2823)
                    if self.failed:
                        return retval

                    string_literal461_tree = self.adaptor.createWithPayload(string_literal461)
                    self.adaptor.addChild(root_0, string_literal461_tree)



                elif alt242 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:405:4: 'true'
                    root_0 = self.adaptor.nil()

                    string_literal462 = self.input.LT(1)
                    self.match(self.input, 120, self.FOLLOW_120_in_literal2828)
                    if self.failed:
                        return retval

                    string_literal462_tree = self.adaptor.createWithPayload(string_literal462)
                    self.adaptor.addChild(root_0, string_literal462_tree)



                elif alt242 == 3:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:406:4: 'false'
                    root_0 = self.adaptor.nil()

                    string_literal463 = self.input.LT(1)
                    self.match(self.input, 121, self.FOLLOW_121_in_literal2833)
                    if self.failed:
                        return retval

                    string_literal463_tree = self.adaptor.createWithPayload(string_literal463)
                    self.adaptor.addChild(root_0, string_literal463_tree)



                elif alt242 == 4:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:407:4: StringLiteral
                    root_0 = self.adaptor.nil()

                    StringLiteral464 = self.input.LT(1)
                    self.match(self.input, StringLiteral, self.FOLLOW_StringLiteral_in_literal2838)
                    if self.failed:
                        return retval

                    StringLiteral464_tree = self.adaptor.createWithPayload(StringLiteral464)
                    self.adaptor.addChild(root_0, StringLiteral464_tree)



                elif alt242 == 5:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:408:4: NumericLiteral
                    root_0 = self.adaptor.nil()

                    NumericLiteral465 = self.input.LT(1)
                    self.match(self.input, NumericLiteral, self.FOLLOW_NumericLiteral_in_literal2843)
                    if self.failed:
                        return retval

                    NumericLiteral465_tree = self.adaptor.createWithPayload(NumericLiteral465)
                    self.adaptor.addChild(root_0, NumericLiteral465_tree)



                elif alt242 == 6:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:409:4: regularExpressionLiteral
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_regularExpressionLiteral_in_literal2848)
                    regularExpressionLiteral466 = self.regularExpressionLiteral()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, regularExpressionLiteral466.tree)


                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 80, literal_StartIndex)

            pass

        return retval

    # $ANTLR end literal

    class reFirstChar_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reFirstChar
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:419:1: reFirstChar : ( ';' | ',' | '.' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'instanceof' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | StringLiteral | NumericLiteral | Identifier );
    def reFirstChar(self, ):

        retval = self.reFirstChar_return()
        retval.start = self.input.LT(1)
        reFirstChar_StartIndex = self.input.index()
        root_0 = None

        set467 = None

        set467_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 81):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:420:2: ( ';' | ',' | '.' | '[' | ']' | '(' | ')' | '{' | '}' | '?' | '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '>>>=' | '&=' | '^=' | '|=' | '<' | '>' | '<=' | '>=' | '<<' | '>>' | '>>>' | '|' | '||' | '&' | '&&' | '!' | '#' | '%' | '^' | '++' | '--' | '+' | '-' | '~' | 'break' | 'case' | 'catch' | 'const' | 'continue' | 'default' | 'delete' | 'do' | 'each' | 'else' | 'false' | 'finally' | 'for' | 'function' | 'get' | 'if' | 'in' | 'instanceof' | 'new' | 'null' | 'return' | 'set' | 'switch' | 'this' | 'throw' | 'true' | 'try' | 'typeof' | 'while' | 'with' | 'var' | 'void' | StringLiteral | NumericLiteral | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set467 = self.input.LT(1)
                if (StringLiteral <= self.input.LA(1) <= Identifier) or (42 <= self.input.LA(1) <= 62) or (64 <= self.input.LA(1) <= 91) or (96 <= self.input.LA(1) <= 105) or (108 <= self.input.LA(1) <= 122):
                    self.input.consume();
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set467))
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
                self.memoize(self.input, 81, reFirstChar_StartIndex)

            pass

        return retval

    # $ANTLR end reFirstChar

    class reChars_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start reChars
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:438:1: reChars : ( reFirstChar | '*' );
    def reChars(self, ):

        retval = self.reChars_return()
        retval.start = self.input.LT(1)
        reChars_StartIndex = self.input.index()
        root_0 = None

        char_literal469 = None
        reFirstChar468 = None


        char_literal469_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 82):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:2: ( reFirstChar | '*' )
                alt243 = 2
                LA243_0 = self.input.LA(1)

                if ((StringLiteral <= LA243_0 <= Identifier) or (42 <= LA243_0 <= 62) or (64 <= LA243_0 <= 91) or (96 <= LA243_0 <= 105) or (108 <= LA243_0 <= 122)) :
                    alt243 = 1
                elif (LA243_0 == 106) :
                    alt243 = 2
                else:
                    if self.backtracking > 0:
                        self.failed = True
                        return retval

                    nvae = NoViableAltException("438:1: reChars : ( reFirstChar | '*' );", 243, 0, self.input)

                    raise nvae

                if alt243 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:439:4: reFirstChar
                    root_0 = self.adaptor.nil()

                    self.following.append(self.FOLLOW_reFirstChar_in_reChars3226)
                    reFirstChar468 = self.reFirstChar()
                    self.following.pop()
                    if self.failed:
                        return retval
                    if self.backtracking == 0:
                        self.adaptor.addChild(root_0, reFirstChar468.tree)


                elif alt243 == 2:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:440:4: '*'
                    root_0 = self.adaptor.nil()

                    char_literal469 = self.input.LT(1)
                    self.match(self.input, 106, self.FOLLOW_106_in_reChars3231)
                    if self.failed:
                        return retval

                    char_literal469_tree = self.adaptor.createWithPayload(char_literal469)
                    self.adaptor.addChild(root_0, char_literal469_tree)



                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 82, reChars_StartIndex)

            pass

        return retval

    # $ANTLR end reChars

    class regularExpressionLiteral_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start regularExpressionLiteral
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:443:1: regularExpressionLiteral : '/' reFirstChar ( reChars )* '/' ( Identifier )? ;
    def regularExpressionLiteral(self, ):

        retval = self.regularExpressionLiteral_return()
        retval.start = self.input.LT(1)
        regularExpressionLiteral_StartIndex = self.input.index()
        root_0 = None

        char_literal470 = None
        char_literal473 = None
        Identifier474 = None
        reFirstChar471 = None

        reChars472 = None


        char_literal470_tree = None
        char_literal473_tree = None
        Identifier474_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 83):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:444:2: ( '/' reFirstChar ( reChars )* '/' ( Identifier )? )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:444:4: '/' reFirstChar ( reChars )* '/' ( Identifier )?
                root_0 = self.adaptor.nil()

                char_literal470 = self.input.LT(1)
                self.match(self.input, 107, self.FOLLOW_107_in_regularExpressionLiteral3242)
                if self.failed:
                    return retval

                char_literal470_tree = self.adaptor.createWithPayload(char_literal470)
                self.adaptor.addChild(root_0, char_literal470_tree)

                self.following.append(self.FOLLOW_reFirstChar_in_regularExpressionLiteral3244)
                reFirstChar471 = self.reFirstChar()
                self.following.pop()
                if self.failed:
                    return retval
                if self.backtracking == 0:
                    self.adaptor.addChild(root_0, reFirstChar471.tree)
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:444:20: ( reChars )*
                while True: #loop244
                    alt244 = 2
                    LA244_0 = self.input.LA(1)

                    if ((StringLiteral <= LA244_0 <= Identifier) or (42 <= LA244_0 <= 62) or (64 <= LA244_0 <= 91) or (96 <= LA244_0 <= 106) or (108 <= LA244_0 <= 122)) :
                        alt244 = 1


                    if alt244 == 1:
                        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: reChars
                        self.following.append(self.FOLLOW_reChars_in_regularExpressionLiteral3246)
                        reChars472 = self.reChars()
                        self.following.pop()
                        if self.failed:
                            return retval
                        if self.backtracking == 0:
                            self.adaptor.addChild(root_0, reChars472.tree)


                    else:
                        break #loop244


                char_literal473 = self.input.LT(1)
                self.match(self.input, 107, self.FOLLOW_107_in_regularExpressionLiteral3249)
                if self.failed:
                    return retval

                char_literal473_tree = self.adaptor.createWithPayload(char_literal473)
                self.adaptor.addChild(root_0, char_literal473_tree)

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:444:33: ( Identifier )?
                alt245 = 2
                LA245_0 = self.input.LA(1)

                if (LA245_0 == Identifier) :
                    alt245 = 1
                if alt245 == 1:
                    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: Identifier
                    Identifier474 = self.input.LT(1)
                    self.match(self.input, Identifier, self.FOLLOW_Identifier_in_regularExpressionLiteral3251)
                    if self.failed:
                        return retval

                    Identifier474_tree = self.adaptor.createWithPayload(Identifier474)
                    self.adaptor.addChild(root_0, Identifier474_tree)







                retval.stop = self.input.LT(-1)

                if self.backtracking == 0:

                    retval.tree = self.adaptor.rulePostProcessing(root_0)
                    self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:
            if self.backtracking > 0:
                self.memoize(self.input, 83, regularExpressionLiteral_StartIndex)

            pass

        return retval

    # $ANTLR end regularExpressionLiteral

    class identifier_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start identifier
    # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:449:1: identifier : ( 'get' | 'set' | 'each' | Identifier );
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)
        identifier_StartIndex = self.input.index()
        root_0 = None

        set475 = None

        set475_tree = None

        try:
            try:
                if self.backtracking > 0 and self.alreadyParsedRule(self.input, 84):
                    return retval

                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:450:2: ( 'get' | 'set' | 'each' | Identifier )
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:
                root_0 = self.adaptor.nil()

                set475 = self.input.LT(1)
                if self.input.LA(1) == Identifier or self.input.LA(1) == 57 or (117 <= self.input.LA(1) <= 118):
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
                self.memoize(self.input, 84, identifier_StartIndex)

            pass

        return retval

    # $ANTLR end identifier

    # $ANTLR start synpred5
    def synpred5_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:4: ( functionDeclaration )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:38:5: functionDeclaration
        self.following.append(self.FOLLOW_functionDeclaration_in_synpred5129)
        self.functionDeclaration()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred5



    # $ANTLR start synpred21
    def synpred21_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:4: ( statementBlock )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:61:4: statementBlock
        self.following.append(self.FOLLOW_statementBlock_in_synpred21304)
        self.statementBlock()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred21



    # $ANTLR start synpred24
    def synpred24_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: ( expressionStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:64:4: expressionStatement
        self.following.append(self.FOLLOW_expressionStatement_in_synpred24319)
        self.expressionStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred24



    # $ANTLR start synpred31
    def synpred31_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:71:4: ( labelledStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:71:4: labelledStatement
        self.following.append(self.FOLLOW_labelledStatement_in_synpred31354)
        self.labelledStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred31



    # $ANTLR start synpred34
    def synpred34_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:78:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred34383)
        if self.failed:
            return 


    # $ANTLR end synpred34



    # $ANTLR start synpred61
    def synpred61_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:59: ( ( LT )* 'else' ( LT )* statement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:59: ( LT )* 'else' ( LT )* statement
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:61: ( LT )*
        while True: #loop263
            alt263 = 2
            LA263_0 = self.input.LA(1)

            if (LA263_0 == LT) :
                alt263 = 1


            if alt263 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred61698)
                if self.failed:
                    return 


            else:
                break #loop263


        self.match(self.input, 53, self.FOLLOW_53_in_synpred61702)
        if self.failed:
            return 
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:127:73: ( LT )*
        while True: #loop264
            alt264 = 2
            LA264_0 = self.input.LA(1)

            if (LA264_0 == LT) :
                alt264 = 1


            if alt264 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred61704)
                if self.failed:
                    return 


            else:
                break #loop264


        self.following.append(self.FOLLOW_statement_in_synpred61708)
        self.statement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred61



    # $ANTLR start synpred64
    def synpred64_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:4: ( forStatement )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:133:4: forStatement
        self.following.append(self.FOLLOW_forStatement_in_synpred64732)
        self.forStatement()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred64



    # $ANTLR start synpred86
    def synpred86_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:10: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:155:10: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred86922)
        if self.failed:
            return 


    # $ANTLR end synpred86



    # $ANTLR start synpred121
    def synpred121_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:36: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:192:36: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1211220)
        if self.failed:
            return 


    # $ANTLR end synpred121



    # $ANTLR start synpred124
    def synpred124_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:23: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:196:23: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred1241245)
        if self.failed:
            return 


    # $ANTLR end synpred124



    # $ANTLR start synpred143
    def synpred143_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: ( conditionalExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:225:4: conditionalExpression
        self.following.append(self.FOLLOW_conditionalExpression_in_synpred1431437)
        self.conditionalExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred143



    # $ANTLR start synpred146
    def synpred146_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:4: ( conditionalExpressionNoIn )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:230:4: conditionalExpressionNoIn
        self.following.append(self.FOLLOW_conditionalExpressionNoIn_in_synpred1461466)
        self.conditionalExpressionNoIn()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred146



    # $ANTLR start synpred149
    def synpred149_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:4: ( callExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:235:4: callExpression
        self.following.append(self.FOLLOW_callExpression_in_synpred1491495)
        self.callExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred149



    # $ANTLR start synpred150
    def synpred150_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:4: ( memberExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:240:4: memberExpression
        self.following.append(self.FOLLOW_memberExpression_in_synpred1501512)
        self.memberExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred150



    # $ANTLR start synpred157
    def synpred157_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:91: ( ( LT )* memberExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:91: ( LT )* memberExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:245:93: ( LT )*
        while True: #loop278
            alt278 = 2
            LA278_0 = self.input.LA(1)

            if (LA278_0 == LT) :
                alt278 = 1


            if alt278 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1571560)
                if self.failed:
                    return 


            else:
                break #loop278


        self.following.append(self.FOLLOW_memberExpressionSuffix_in_synpred1571564)
        self.memberExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred157



    # $ANTLR start synpred161
    def synpred161_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:36: ( ( LT )* callExpressionSuffix )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:36: ( LT )* callExpressionSuffix
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:254:36: ( LT )*
        while True: #loop279
            alt279 = 2
            LA279_0 = self.input.LA(1)

            if (LA279_0 == LT) :
                alt279 = 1


            if alt279 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred1611602)
                if self.failed:
                    return 


            else:
                break #loop279


        self.following.append(self.FOLLOW_callExpressionSuffix_in_synpred1611605)
        self.callExpressionSuffix()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred161



    # $ANTLR start synpred259
    def synpred259_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:30: ( ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:30: ( LT )* ( '+' | '-' ) ( LT )* multiplicativeExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:32: ( LT )*
        while True: #loop324
            alt324 = 2
            LA324_0 = self.input.LA(1)

            if (LA324_0 == LT) :
                alt324 = 1


            if alt324 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2592370)
                if self.failed:
                    return 


            else:
                break #loop324


        if (104 <= self.input.LA(1) <= 105):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2592374
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:351:49: ( LT )*
        while True: #loop325
            alt325 = 2
            LA325_0 = self.input.LA(1)

            if (LA325_0 == LT) :
                alt325 = 1


            if alt325 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2592382)
                if self.failed:
                    return 


            else:
                break #loop325


        self.following.append(self.FOLLOW_multiplicativeExpression_in_synpred2592386)
        self.multiplicativeExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred259



    # $ANTLR start synpred264
    def synpred264_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:21: ( ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:21: ( LT )* ( '*' | '/' | '%' ) ( LT )* unaryExpression
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:23: ( LT )*
        while True: #loop326
            alt326 = 2
            LA326_0 = self.input.LA(1)

            if (LA326_0 == LT) :
                alt326 = 1


            if alt326 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2642402)
                if self.failed:
                    return 


            else:
                break #loop326


        if (106 <= self.input.LA(1) <= 108):
            self.input.consume();
            self.errorRecovery = False
            self.failed = False

        else:
            if self.backtracking > 0:
                self.failed = True
                return 

            mse = MismatchedSetException(None, self.input)
            self.recoverFromMismatchedSet(
                self.input, mse, self.FOLLOW_set_in_synpred2642406
                )
            raise mse


        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:355:46: ( LT )*
        while True: #loop327
            alt327 = 2
            LA327_0 = self.input.LA(1)

            if (LA327_0 == LT) :
                alt327 = 1


            if alt327 == 1:
                # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:0:0: LT
                self.match(self.input, LT, self.FOLLOW_LT_in_synpred2642418)
                if self.failed:
                    return 


            else:
                break #loop327


        self.following.append(self.FOLLOW_unaryExpression_in_synpred2642422)
        self.unaryExpression()
        self.following.pop()
        if self.failed:
            return 


    # $ANTLR end synpred264



    # $ANTLR start synpred283
    def synpred283_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:378:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2832560)
        if self.failed:
            return 


    # $ANTLR end synpred283



    # $ANTLR start synpred290
    def synpred290_fragment(self, ):
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:8: ( LT )
        # /home/visbrero/rev_control/git/java-antlr-grammar/JavaScript.g:383:8: LT
        self.match(self.input, LT, self.FOLLOW_LT_in_synpred2902610)
        if self.failed:
            return 


    # $ANTLR end synpred290



    def synpred34(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred34_fragment()
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

    def synpred149(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred149_fragment()
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

    def synpred86(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred86_fragment()
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

    def synpred5(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred5_fragment()
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

    def synpred283(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred283_fragment()
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

    def synpred121(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred121_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred31(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred31_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred143(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred143_fragment()
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

    def synpred264(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred264_fragment()
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

    def synpred24(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred24_fragment()
        success = not self.failed
        self.input.rewind(start)
        self.backtracking -= 1
        self.failed = False
        return success

    def synpred259(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred259_fragment()
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

    def synpred157(self):
        self.backtracking += 1
        start = self.input.mark()
        self.synpred157_fragment()
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
        u"\2\15\2\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA4_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\1\3\1\uffff\3\3\1\uffff"
        u"\1\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\uffff\2\3\2\uffff\2"
        u"\3\37\uffff\2\3\1\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\1\3\1\uffff\3\3\1\uffff"
        u"\1\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\uffff\2\3\2\uffff\2"
        u"\3\37\uffff\2\3\1\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    DFA4 = DFA
    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\52\2\15\2\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\52\2\166\2\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1"
        )

    DFA14_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\2\uffff\1\4\32\uffff\1\3\15\uffff\1\4\73\uffff"
        u"\2\4"),
        DFA.unpack(u"\1\2\2\uffff\1\4\32\uffff\1\3\15\uffff\1\4\73\uffff"
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
        u"\2\15\2\uffff"
        )

    DFA19_max = DFA.unpack(
        u"\2\166\2\uffff"
        )

    DFA19_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA19_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA19_transition = [
        DFA.unpack(u"\1\1\2\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
        u"\2\2"),
        DFA.unpack(u"\1\1\2\uffff\1\2\34\uffff\1\3\13\uffff\1\2\73\uffff"
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
        u"\2\15\2\uffff"
        )

    DFA18_max = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA18_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA18_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA18_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #18

    DFA18 = DFA
    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA26_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\1\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\1\3\1\2\3\3\1\uffff\1"
        u"\3\1\uffff\4\3\1\uffff\4\3\1\uffff\1\3\2\2\2\3\2\uffff\2\3\37\uffff"
        u"\2\3\1\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    DFA26 = DFA
    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\1\uffff\1\2\2\uffff\1\2"
        )

    DFA32_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA32_max = DFA.unpack(
        u"\1\62\1\171\2\uffff\1\171"
        )

    DFA32_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA32_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\4\3\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\2\2\1\3\1\uffff\5\2\1\uffff\6\2\1"
        u"\uffff\4\2\1\uffff\5\2\2\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff"
        u"\15\2")
    ]

    # class definition for DFA #32

    DFA32 = DFA
    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA35_max = DFA.unpack(
        u"\2\62\2\uffff"
        )

    DFA35_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA35_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA35_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #35

    DFA35 = DFA
    # lookup tables for DFA #37

    DFA37_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA37_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA37_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA37_max = DFA.unpack(
        u"\1\63\1\171\2\uffff\1\171"
        )

    DFA37_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA37_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA37_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\3\1\2"),
        DFA.unpack(u"\1\4\3\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\1\uffff\1\3\1\uffff\15"
        u"\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\3\31\uffff\3\3\1\uffff\5\3\1\2\6\3\1\uffff\4"
        u"\3\1\uffff\5\3\2\uffff\2\3\37\uffff\2\3\1\uffff\1\3\1\uffff\15"
        u"\3")
    ]

    # class definition for DFA #37

    DFA37 = DFA
    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA39_max = DFA.unpack(
        u"\2\72\2\uffff"
        )

    DFA39_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA39_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA39_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\3\1\2\6\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #39

    DFA39 = DFA
    # lookup tables for DFA #59

    DFA59_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA59_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA59_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA59_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA59_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA59_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA59_transition = [
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\uffff"
        u"\1\3\6\uffff\1\2\15\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff"
        u"\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #59

    DFA59 = DFA
    # lookup tables for DFA #62

    DFA62_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA62_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA62_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA62_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA62_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA62_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA62_transition = [
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\2\uffff\1\2\3\uffff\1\3\6\uffff"
        u"\1\2\15\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #62

    DFA62 = DFA
    # lookup tables for DFA #65

    DFA65_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA65_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA65_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA65_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA65_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA65_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA65_transition = [
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #65

    DFA65 = DFA
    # lookup tables for DFA #94

    DFA94_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA94_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA94_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA94_max = DFA.unpack(
        u"\2\102\2\uffff"
        )

    DFA94_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA94_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA94_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\41\uffff\1\2\21\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #94

    DFA94 = DFA
    # lookup tables for DFA #98

    DFA98_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA98_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA98_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA98_max = DFA.unpack(
        u"\2\102\2\uffff"
        )

    DFA98_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA98_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA98_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u"\1\1\41\uffff\1\3\22\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #98

    DFA98 = DFA
    # lookup tables for DFA #97

    DFA97_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA97_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA97_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA97_max = DFA.unpack(
        u"\2\101\2\uffff"
        )

    DFA97_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA97_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA97_transition = [
        DFA.unpack(u"\1\1\41\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u"\1\1\41\uffff\1\2\21\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #97

    DFA97 = DFA
    # lookup tables for DFA #110

    DFA110_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA110_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA110_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA110_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA110_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA110_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA110_transition = [
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\1\uffff\1\3\1\uffff"
        u"\15\3"),
        DFA.unpack(u"\1\1\3\3\31\uffff\2\3\2\uffff\5\3\1\uffff\6\3\1\uffff"
        u"\4\3\1\uffff\5\3\1\uffff\1\2\2\3\37\uffff\2\3\1\uffff\1\3\1\uffff"
        u"\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #110

    DFA110 = DFA
    # lookup tables for DFA #119

    DFA119_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA119_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA119_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA119_max = DFA.unpack(
        u"\1\111\1\171\2\uffff\1\171"
        )

    DFA119_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA119_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA119_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\1\2\4\uffff\1\2\14\uffff\1\2\11\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\4\3\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\2\2\1\3\6\2\1\uffff\6\2\1\uffff\12"
        u"\2\2\uffff\3\2\36\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #119

    DFA119 = DFA
    # lookup tables for DFA #122

    DFA122_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA122_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA122_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA122_max = DFA.unpack(
        u"\2\62\2\uffff"
        )

    DFA122_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA122_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA122_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #122

    DFA122 = DFA
    # lookup tables for DFA #146

    DFA146_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA146_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA146_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA146_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA146_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA146_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA146_transition = [
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\uffff\1\3\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\37\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #146

    DFA146 = DFA
    # lookup tables for DFA #145

    DFA145_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA145_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA145_max = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA145_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA145_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA145_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #145

    DFA145 = DFA
    # lookup tables for DFA #155

    DFA155_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA155_eof = DFA.unpack(
        u"\2\3\2\uffff\1\3"
        )

    DFA155_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA155_max = DFA.unpack(
        u"\1\126\1\171\2\uffff\1\171"
        )

    DFA155_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\uffff"
        )

    DFA155_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA155_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\3\1\uffff\1\3\2\uffff\1\3\14\uffff\1"
        u"\3\11\uffff\1\3\14\uffff\1\2"),
        DFA.unpack(u"\1\4\3\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\1\uffff\1\3\1\uffff\15\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\3\31\uffff\11\3\1\uffff\6\3\1\uffff\12\3\2\uffff"
        u"\3\3\14\uffff\1\2\21\uffff\2\3\1\uffff\1\3\1\uffff\15\3")
    ]

    # class definition for DFA #155

    DFA155 = DFA
    # lookup tables for DFA #160

    DFA160_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA160_eof = DFA.unpack(
        u"\1\3\3\uffff"
        )

    DFA160_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA160_max = DFA.unpack(
        u"\2\126\2\uffff"
        )

    DFA160_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA160_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA160_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\5\uffff\1\3\7\uffff\1\3\4\uffff\1"
        u"\3\26\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #160

    DFA160 = DFA
    # lookup tables for DFA #163

    DFA163_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA163_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA163_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA163_max = DFA.unpack(
        u"\1\127\1\171\2\uffff\1\171"
        )

    DFA163_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA163_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA163_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\1\2\1\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\1\2\1\3\20\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #163

    DFA163 = DFA
    # lookup tables for DFA #166

    DFA166_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA166_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA166_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA166_max = DFA.unpack(
        u"\2\127\2\uffff"
        )

    DFA166_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA166_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA166_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #166

    DFA166 = DFA
    # lookup tables for DFA #169

    DFA169_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA169_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA169_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA169_max = DFA.unpack(
        u"\1\130\1\171\2\uffff\1\171"
        )

    DFA169_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA169_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA169_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\2\2\1\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\2\2\1\3\17\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #169

    DFA169 = DFA
    # lookup tables for DFA #172

    DFA172_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA172_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA172_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA172_max = DFA.unpack(
        u"\2\130\2\uffff"
        )

    DFA172_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA172_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA172_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\2\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #172

    DFA172 = DFA
    # lookup tables for DFA #175

    DFA175_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA175_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA175_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA175_max = DFA.unpack(
        u"\1\131\1\171\2\uffff\1\171"
        )

    DFA175_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA175_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA175_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\3\2\1\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\3\2\1\3\16\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #175

    DFA175 = DFA
    # lookup tables for DFA #178

    DFA178_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA178_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA178_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA178_max = DFA.unpack(
        u"\2\131\2\uffff"
        )

    DFA178_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA178_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA178_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\3\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #178

    DFA178 = DFA
    # lookup tables for DFA #181

    DFA181_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA181_eof = DFA.unpack(
        u"\2\2\2\uffff\1\2"
        )

    DFA181_min = DFA.unpack(
        u"\2\15\2\uffff\1\15"
        )

    DFA181_max = DFA.unpack(
        u"\1\132\1\171\2\uffff\1\171"
        )

    DFA181_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA181_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA181_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\4\2\1\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\4\2\1\3\15\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #181

    DFA181 = DFA
    # lookup tables for DFA #184

    DFA184_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA184_eof = DFA.unpack(
        u"\1\2\3\uffff"
        )

    DFA184_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA184_max = DFA.unpack(
        u"\2\132\2\uffff"
        )

    DFA184_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA184_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA184_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\4\2\1\3"),
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
        u"\2\15\2\uffff\1\15"
        )

    DFA187_max = DFA.unpack(
        u"\1\133\1\171\2\uffff\1\171"
        )

    DFA187_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA187_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA187_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\5\2\1\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\5\2\1\3\14\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
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
        u"\2\15\2\uffff"
        )

    DFA190_max = DFA.unpack(
        u"\2\133\2\uffff"
        )

    DFA190_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA190_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA190_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\5\2\1\3"),
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
        u"\2\15\2\uffff\1\15"
        )

    DFA193_max = DFA.unpack(
        u"\1\137\1\171\2\uffff\1\171"
        )

    DFA193_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA193_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA193_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\14\uffff\1"
        u"\2\11\uffff\1\2\14\uffff\6\2\4\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\uffff\12\2\2\uffff"
        u"\3\2\14\uffff\6\2\4\3\10\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
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
        u"\2\15\2\uffff"
        )

    DFA196_max = DFA.unpack(
        u"\2\137\2\uffff"
        )

    DFA196_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA196_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA196_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\6\2\4\3"),
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
        u"\2\15\2\uffff\1\15"
        )

    DFA199_max = DFA.unpack(
        u"\1\144\1\171\2\uffff\1\171"
        )

    DFA199_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA199_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA199_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\3\4\uffff\1\2\11\uffff\1\2\14\uffff\12\2\5\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\6\2\1\3\12\2\2\uffff"
        u"\3\2\14\uffff\12\2\5\3\3\uffff\2\2\1\uffff\1\2\1\uffff\15\2")
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
        u"\2\15\2\uffff"
        )

    DFA202_max = DFA.unpack(
        u"\2\144\2\uffff"
        )

    DFA202_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA202_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA202_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
        DFA.unpack(u"\1\1\36\uffff\1\2\5\uffff\1\2\7\uffff\1\2\4\uffff\1"
        u"\2\26\uffff\12\2\5\3"),
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
        u"\2\15\2\uffff\1\15"
        )

    DFA205_max = DFA.unpack(
        u"\1\147\1\171\2\uffff\1\171"
        )

    DFA205_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\1\uffff"
        )

    DFA205_special = DFA.unpack(
        u"\5\uffff"
        )

            
    DFA205_transition = [
        DFA.unpack(u"\1\1\36\uffff\2\2\1\uffff\1\2\2\uffff\1\2\7\uffff\1"
        u"\2\4\uffff\1\2\11\uffff\1\2\14\uffff\17\2\3\3"),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\3\2\31\uffff\11\2\1\uffff\21\2\2\uffff\3\2\14\uffff"
        u"\17\2\3\3\2\2\1\uffff\1\2\1\uffff\15\2")
    ]

    # class definition for DFA #205

    DFA205 = DFA
    # lookup tables for DFA #222

    DFA222_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA222_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA222_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA222_max = DFA.unpack(
        u"\2\111\2\uffff"
        )

    DFA222_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA222_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA222_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\34\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #222

    DFA222 = DFA
    # lookup tables for DFA #221

    DFA221_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA221_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA221_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA221_max = DFA.unpack(
        u"\2\171\2\uffff"
        )

    DFA221_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA221_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA221_transition = [
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u"\1\1\3\2\31\uffff\2\2\1\3\1\uffff\1\2\12\uffff\1\2\15"
        u"\uffff\2\2\1\3\36\uffff\2\2\1\uffff\1\2\1\uffff\15\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #221

    DFA221 = DFA
    # lookup tables for DFA #228

    DFA228_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA228_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA228_min = DFA.unpack(
        u"\2\15\2\uffff"
        )

    DFA228_max = DFA.unpack(
        u"\2\57\2\uffff"
        )

    DFA228_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA228_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA228_transition = [
        DFA.unpack(u"\1\1\36\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u"\1\1\36\uffff\1\3\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #228

    DFA228 = DFA
    # lookup tables for DFA #240

    DFA240_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA240_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA240_min = DFA.unpack(
        u"\1\16\1\15\1\uffff\3\15\1\uffff\1\15\1\uffff"
        )

    DFA240_max = DFA.unpack(
        u"\2\166\1\uffff\3\166\1\uffff\1\166\1\uffff"
        )

    DFA240_accept = DFA.unpack(
        u"\2\uffff\1\1\3\uffff\1\3\1\uffff\1\2"
        )

    DFA240_special = DFA.unpack(
        u"\11\uffff"
        )

            
    DFA240_transition = [
        DFA.unpack(u"\3\2\50\uffff\1\2\73\uffff\1\1\1\3"),
        DFA.unpack(u"\1\4\2\uffff\1\5\50\uffff\1\5\5\uffff\1\2\65\uffff\2"
        u"\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\1\5\50\uffff\1\5\5\uffff\1\2\65\uffff\2"
        u"\5"),
        DFA.unpack(u"\1\4\2\uffff\1\6\50\uffff\1\6\5\uffff\1\2\65\uffff\2"
        u"\6"),
        DFA.unpack(u"\1\7\2\uffff\1\10\32\uffff\1\6\15\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\2\uffff\1\10\32\uffff\1\6\15\uffff\1\10\73\uffff"
        u"\2\10"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #240

    DFA240 = DFA
 

    FOLLOW_LT_in_program84 = frozenset([1])
    FOLLOW_sourceElements_in_program88 = frozenset([13])
    FOLLOW_LT_in_program90 = frozenset([1])
    FOLLOW_EOF_in_program94 = frozenset([1])
    FOLLOW_sourceElement_in_sourceElements107 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_sourceElements110 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_sourceElement_in_sourceElements114 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_functionDeclaration_in_sourceElement133 = frozenset([1])
    FOLLOW_statement_in_sourceElement138 = frozenset([1])
    FOLLOW_42_in_functionDeclaration151 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_functionDeclaration153 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_functionDeclaration156 = frozenset([13, 43])
    FOLLOW_LT_in_functionDeclaration158 = frozenset([13, 43])
    FOLLOW_formalParameterList_in_functionDeclaration161 = frozenset([13, 46])
    FOLLOW_LT_in_functionDeclaration163 = frozenset([13, 46])
    FOLLOW_statementBlock_in_functionDeclaration166 = frozenset([1])
    FOLLOW_42_in_functionExpression192 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_functionExpression194 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_functionExpression197 = frozenset([13, 43])
    FOLLOW_LT_in_functionExpression199 = frozenset([13, 43])
    FOLLOW_formalParameterList_in_functionExpression202 = frozenset([13, 46])
    FOLLOW_LT_in_functionExpression204 = frozenset([13, 46])
    FOLLOW_statementBlock_in_functionExpression207 = frozenset([1])
    FOLLOW_42_in_functionExpression226 = frozenset([13, 43])
    FOLLOW_LT_in_functionExpression228 = frozenset([13, 43])
    FOLLOW_formalParameterList_in_functionExpression231 = frozenset([13, 46])
    FOLLOW_LT_in_functionExpression233 = frozenset([13, 46])
    FOLLOW_statementBlock_in_functionExpression236 = frozenset([1])
    FOLLOW_43_in_formalParameterList262 = frozenset([13, 16, 45, 57, 117, 118])
    FOLLOW_LT_in_formalParameterList265 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_formalParameterList269 = frozenset([13, 44, 45])
    FOLLOW_LT_in_formalParameterList272 = frozenset([13, 44])
    FOLLOW_44_in_formalParameterList276 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_formalParameterList278 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_formalParameterList282 = frozenset([13, 44, 45])
    FOLLOW_LT_in_formalParameterList288 = frozenset([1])
    FOLLOW_45_in_formalParameterList292 = frozenset([1])
    FOLLOW_statementBlock_in_statement304 = frozenset([1])
    FOLLOW_variableStatement_in_statement309 = frozenset([1])
    FOLLOW_emptyStatement_in_statement314 = frozenset([1])
    FOLLOW_expressionStatement_in_statement319 = frozenset([1])
    FOLLOW_ifStatement_in_statement324 = frozenset([1])
    FOLLOW_iterationStatement_in_statement329 = frozenset([1])
    FOLLOW_continueStatement_in_statement334 = frozenset([1])
    FOLLOW_breakStatement_in_statement339 = frozenset([1])
    FOLLOW_returnStatement_in_statement344 = frozenset([1])
    FOLLOW_withStatement_in_statement349 = frozenset([1])
    FOLLOW_labelledStatement_in_statement354 = frozenset([1])
    FOLLOW_switchStatement_in_statement359 = frozenset([1])
    FOLLOW_throwStatement_in_statement364 = frozenset([1])
    FOLLOW_tryStatement_in_statement369 = frozenset([1])
    FOLLOW_46_in_statementBlock381 = frozenset([13, 14, 15, 16, 42, 43, 46, 47, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_statementBlock383 = frozenset([1])
    FOLLOW_statementList_in_statementBlock387 = frozenset([13, 47])
    FOLLOW_LT_in_statementBlock390 = frozenset([1])
    FOLLOW_47_in_statementBlock394 = frozenset([1])
    FOLLOW_statement_in_statementList406 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_statementList409 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_statement_in_statementList413 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_48_in_variableStatement430 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_49_in_variableStatement434 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_variableStatement437 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_variableDeclarationList_in_variableStatement440 = frozenset([13, 50])
    FOLLOW_LT_in_variableStatement443 = frozenset([1])
    FOLLOW_50_in_variableStatement447 = frozenset([1])
    FOLLOW_variableDeclaration_in_variableDeclarationList472 = frozenset([1, 13, 44])
    FOLLOW_LT_in_variableDeclarationList475 = frozenset([13, 44])
    FOLLOW_44_in_variableDeclarationList479 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_variableDeclarationList481 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_variableDeclaration_in_variableDeclarationList485 = frozenset([1, 13, 44])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn499 = frozenset([1, 13, 44])
    FOLLOW_LT_in_variableDeclarationListNoIn502 = frozenset([13, 44])
    FOLLOW_44_in_variableDeclarationListNoIn506 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_variableDeclarationListNoIn508 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_variableDeclarationNoIn_in_variableDeclarationListNoIn512 = frozenset([1, 13, 44])
    FOLLOW_identifier_in_variableDeclaration526 = frozenset([1, 13, 51])
    FOLLOW_LT_in_variableDeclaration529 = frozenset([13, 51])
    FOLLOW_initialiser_in_variableDeclaration532 = frozenset([1])
    FOLLOW_identifier_in_variableDeclarationNoIn559 = frozenset([1, 13, 51])
    FOLLOW_LT_in_variableDeclarationNoIn562 = frozenset([13, 51])
    FOLLOW_initialiserNoIn_in_variableDeclarationNoIn565 = frozenset([1])
    FOLLOW_51_in_initialiser592 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_initialiser594 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_initialiser597 = frozenset([1])
    FOLLOW_51_in_initialiserNoIn615 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_initialiserNoIn617 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpressionNoIn_in_initialiserNoIn620 = frozenset([1])
    FOLLOW_50_in_emptyStatement638 = frozenset([1])
    FOLLOW_expression_in_expressionStatement650 = frozenset([13, 50])
    FOLLOW_set_in_expressionStatement652 = frozenset([1])
    FOLLOW_52_in_ifStatement671 = frozenset([13, 43])
    FOLLOW_LT_in_ifStatement673 = frozenset([1])
    FOLLOW_43_in_ifStatement677 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_ifStatement679 = frozenset([1])
    FOLLOW_expression_in_ifStatement683 = frozenset([13, 45])
    FOLLOW_LT_in_ifStatement685 = frozenset([1])
    FOLLOW_45_in_ifStatement689 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_ifStatement691 = frozenset([1])
    FOLLOW_statement_in_ifStatement695 = frozenset([1, 13, 53])
    FOLLOW_LT_in_ifStatement698 = frozenset([13, 53])
    FOLLOW_53_in_ifStatement702 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_ifStatement704 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_statement_in_ifStatement708 = frozenset([1])
    FOLLOW_doWhileStatement_in_iterationStatement722 = frozenset([1])
    FOLLOW_whileStatement_in_iterationStatement727 = frozenset([1])
    FOLLOW_forStatement_in_iterationStatement732 = frozenset([1])
    FOLLOW_forInStatement_in_iterationStatement737 = frozenset([1])
    FOLLOW_54_in_doWhileStatement749 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_doWhileStatement751 = frozenset([1])
    FOLLOW_statement_in_doWhileStatement755 = frozenset([13, 55])
    FOLLOW_LT_in_doWhileStatement757 = frozenset([1])
    FOLLOW_55_in_doWhileStatement761 = frozenset([13, 43])
    FOLLOW_LT_in_doWhileStatement763 = frozenset([1])
    FOLLOW_43_in_doWhileStatement767 = frozenset([14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_doWhileStatement769 = frozenset([45])
    FOLLOW_45_in_doWhileStatement771 = frozenset([13, 50])
    FOLLOW_set_in_doWhileStatement773 = frozenset([1])
    FOLLOW_55_in_whileStatement792 = frozenset([13, 43])
    FOLLOW_LT_in_whileStatement794 = frozenset([1])
    FOLLOW_43_in_whileStatement798 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_whileStatement800 = frozenset([1])
    FOLLOW_expression_in_whileStatement804 = frozenset([13, 45])
    FOLLOW_LT_in_whileStatement806 = frozenset([1])
    FOLLOW_45_in_whileStatement810 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_whileStatement812 = frozenset([1])
    FOLLOW_statement_in_whileStatement816 = frozenset([1])
    FOLLOW_56_in_forStatement828 = frozenset([13, 43])
    FOLLOW_LT_in_forStatement830 = frozenset([1])
    FOLLOW_43_in_forStatement834 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 50, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forStatement837 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_forStatementInitialiserPart_in_forStatement841 = frozenset([13, 50])
    FOLLOW_LT_in_forStatement845 = frozenset([1])
    FOLLOW_50_in_forStatement849 = frozenset([13, 14, 15, 16, 42, 43, 46, 50, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forStatement852 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_forStatement856 = frozenset([13, 50])
    FOLLOW_LT_in_forStatement860 = frozenset([1])
    FOLLOW_50_in_forStatement864 = frozenset([13, 14, 15, 16, 42, 43, 45, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forStatement867 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_forStatement871 = frozenset([13, 45])
    FOLLOW_LT_in_forStatement875 = frozenset([1])
    FOLLOW_45_in_forStatement879 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forStatement881 = frozenset([1])
    FOLLOW_statement_in_forStatement885 = frozenset([1])
    FOLLOW_expressionNoIn_in_forStatementInitialiserPart897 = frozenset([1])
    FOLLOW_48_in_forStatementInitialiserPart902 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_forStatementInitialiserPart904 = frozenset([1])
    FOLLOW_variableDeclarationListNoIn_in_forStatementInitialiserPart908 = frozenset([1])
    FOLLOW_56_in_forInStatement920 = frozenset([13, 43, 57])
    FOLLOW_LT_in_forInStatement922 = frozenset([1])
    FOLLOW_57_in_forInStatement926 = frozenset([13, 43])
    FOLLOW_LT_in_forInStatement929 = frozenset([1])
    FOLLOW_43_in_forInStatement933 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 57, 71, 72, 107, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forInStatement935 = frozenset([1])
    FOLLOW_forInStatementInitialiserPart_in_forInStatement939 = frozenset([13, 58])
    FOLLOW_LT_in_forInStatement941 = frozenset([1])
    FOLLOW_58_in_forInStatement945 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forInStatement947 = frozenset([1])
    FOLLOW_expression_in_forInStatement951 = frozenset([13, 45])
    FOLLOW_LT_in_forInStatement953 = frozenset([1])
    FOLLOW_45_in_forInStatement957 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_forInStatement959 = frozenset([1])
    FOLLOW_statement_in_forInStatement963 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_forInStatementInitialiserPart975 = frozenset([1])
    FOLLOW_48_in_forInStatementInitialiserPart980 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_forInStatementInitialiserPart982 = frozenset([1])
    FOLLOW_variableDeclarationNoIn_in_forInStatementInitialiserPart986 = frozenset([1])
    FOLLOW_59_in_continueStatement997 = frozenset([13, 16, 50, 57, 117, 118])
    FOLLOW_identifier_in_continueStatement999 = frozenset([13, 50])
    FOLLOW_set_in_continueStatement1002 = frozenset([1])
    FOLLOW_60_in_breakStatement1020 = frozenset([13, 16, 50, 57, 117, 118])
    FOLLOW_identifier_in_breakStatement1022 = frozenset([13, 50])
    FOLLOW_set_in_breakStatement1025 = frozenset([1])
    FOLLOW_61_in_returnStatement1043 = frozenset([13, 14, 15, 16, 42, 43, 46, 50, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_returnStatement1045 = frozenset([13, 50])
    FOLLOW_set_in_returnStatement1048 = frozenset([1])
    FOLLOW_62_in_withStatement1067 = frozenset([13, 43])
    FOLLOW_LT_in_withStatement1069 = frozenset([1])
    FOLLOW_43_in_withStatement1073 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_withStatement1075 = frozenset([1])
    FOLLOW_expression_in_withStatement1079 = frozenset([13, 45])
    FOLLOW_LT_in_withStatement1081 = frozenset([1])
    FOLLOW_45_in_withStatement1085 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_withStatement1087 = frozenset([1])
    FOLLOW_statement_in_withStatement1091 = frozenset([1])
    FOLLOW_identifier_in_labelledStatement1102 = frozenset([13, 63])
    FOLLOW_LT_in_labelledStatement1104 = frozenset([1])
    FOLLOW_63_in_labelledStatement1108 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_labelledStatement1110 = frozenset([1])
    FOLLOW_statement_in_labelledStatement1114 = frozenset([1])
    FOLLOW_64_in_switchStatement1126 = frozenset([13, 43])
    FOLLOW_LT_in_switchStatement1128 = frozenset([1])
    FOLLOW_43_in_switchStatement1132 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_switchStatement1134 = frozenset([1])
    FOLLOW_expression_in_switchStatement1138 = frozenset([13, 45])
    FOLLOW_LT_in_switchStatement1140 = frozenset([1])
    FOLLOW_45_in_switchStatement1144 = frozenset([13, 46])
    FOLLOW_LT_in_switchStatement1146 = frozenset([1])
    FOLLOW_caseBlock_in_switchStatement1150 = frozenset([1])
    FOLLOW_46_in_caseBlock1162 = frozenset([13, 47, 65, 66])
    FOLLOW_LT_in_caseBlock1165 = frozenset([13, 65])
    FOLLOW_caseClause_in_caseBlock1169 = frozenset([13, 47, 65, 66])
    FOLLOW_LT_in_caseBlock1174 = frozenset([13, 66])
    FOLLOW_defaultClause_in_caseBlock1178 = frozenset([13, 47, 65])
    FOLLOW_LT_in_caseBlock1181 = frozenset([13, 65])
    FOLLOW_caseClause_in_caseBlock1185 = frozenset([13, 47, 65])
    FOLLOW_LT_in_caseBlock1191 = frozenset([1])
    FOLLOW_47_in_caseBlock1195 = frozenset([1])
    FOLLOW_65_in_caseClause1206 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_caseClause1208 = frozenset([1])
    FOLLOW_expression_in_caseClause1212 = frozenset([13, 63])
    FOLLOW_LT_in_caseClause1214 = frozenset([1])
    FOLLOW_63_in_caseClause1218 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_caseClause1220 = frozenset([1])
    FOLLOW_statementList_in_caseClause1224 = frozenset([1])
    FOLLOW_66_in_defaultClause1237 = frozenset([13, 63])
    FOLLOW_LT_in_defaultClause1239 = frozenset([1])
    FOLLOW_63_in_defaultClause1243 = frozenset([1, 13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_defaultClause1245 = frozenset([1])
    FOLLOW_statementList_in_defaultClause1249 = frozenset([1])
    FOLLOW_67_in_throwStatement1262 = frozenset([14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_throwStatement1264 = frozenset([13, 50])
    FOLLOW_set_in_throwStatement1266 = frozenset([1])
    FOLLOW_68_in_tryStatement1284 = frozenset([13, 46])
    FOLLOW_LT_in_tryStatement1286 = frozenset([1])
    FOLLOW_statementBlock_in_tryStatement1290 = frozenset([13, 69, 70])
    FOLLOW_LT_in_tryStatement1292 = frozenset([1])
    FOLLOW_finallyClause_in_tryStatement1297 = frozenset([1])
    FOLLOW_catchClause_in_tryStatement1301 = frozenset([1, 13, 70])
    FOLLOW_LT_in_tryStatement1304 = frozenset([13, 70])
    FOLLOW_finallyClause_in_tryStatement1308 = frozenset([1])
    FOLLOW_69_in_catchClause1329 = frozenset([13, 43])
    FOLLOW_LT_in_catchClause1331 = frozenset([1])
    FOLLOW_43_in_catchClause1335 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_catchClause1337 = frozenset([1])
    FOLLOW_identifier_in_catchClause1341 = frozenset([13, 45])
    FOLLOW_LT_in_catchClause1343 = frozenset([1])
    FOLLOW_45_in_catchClause1347 = frozenset([13, 46])
    FOLLOW_LT_in_catchClause1349 = frozenset([1])
    FOLLOW_statementBlock_in_catchClause1353 = frozenset([1])
    FOLLOW_70_in_finallyClause1365 = frozenset([13, 46])
    FOLLOW_LT_in_finallyClause1367 = frozenset([1])
    FOLLOW_statementBlock_in_finallyClause1371 = frozenset([1])
    FOLLOW_assignmentExpression_in_expression1383 = frozenset([1, 13, 44])
    FOLLOW_LT_in_expression1386 = frozenset([13, 44])
    FOLLOW_44_in_expression1390 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_expression1392 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_expression1396 = frozenset([1, 13, 44])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1410 = frozenset([1, 13, 44])
    FOLLOW_LT_in_expressionNoIn1413 = frozenset([13, 44])
    FOLLOW_44_in_expressionNoIn1417 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_expressionNoIn1419 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpressionNoIn_in_expressionNoIn1423 = frozenset([1, 13, 44])
    FOLLOW_conditionalExpression_in_assignmentExpression1437 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpression1442 = frozenset([13, 51, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])
    FOLLOW_LT_in_assignmentExpression1444 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpression1448 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_assignmentExpression1450 = frozenset([1])
    FOLLOW_assignmentExpression_in_assignmentExpression1454 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_assignmentExpressionNoIn1466 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_assignmentExpressionNoIn1471 = frozenset([13, 51, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85])
    FOLLOW_LT_in_assignmentExpressionNoIn1473 = frozenset([1])
    FOLLOW_assignmentOperator_in_assignmentExpressionNoIn1477 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_assignmentExpressionNoIn1479 = frozenset([1])
    FOLLOW_assignmentExpressionNoIn_in_assignmentExpressionNoIn1483 = frozenset([1])
    FOLLOW_callExpression_in_leftHandSideExpression1495 = frozenset([1])
    FOLLOW_newExpression_in_leftHandSideExpression1500 = frozenset([1])
    FOLLOW_memberExpression_in_newExpression1512 = frozenset([1])
    FOLLOW_71_in_newExpression1517 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 107, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_newExpression1519 = frozenset([1])
    FOLLOW_newExpression_in_newExpression1523 = frozenset([1])
    FOLLOW_primaryExpression_in_memberExpression1536 = frozenset([1, 13, 72, 74])
    FOLLOW_functionExpression_in_memberExpression1540 = frozenset([1, 13, 72, 74])
    FOLLOW_71_in_memberExpression1544 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 107, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_memberExpression1546 = frozenset([1])
    FOLLOW_memberExpression_in_memberExpression1550 = frozenset([13, 43])
    FOLLOW_LT_in_memberExpression1552 = frozenset([1])
    FOLLOW_arguments_in_memberExpression1556 = frozenset([1, 13, 72, 74])
    FOLLOW_LT_in_memberExpression1560 = frozenset([13, 72, 74])
    FOLLOW_memberExpressionSuffix_in_memberExpression1564 = frozenset([1, 13, 72, 74])
    FOLLOW_indexSuffix_in_memberExpressionSuffix1578 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_memberExpressionSuffix1583 = frozenset([1])
    FOLLOW_memberExpression_in_callExpression1594 = frozenset([13, 43])
    FOLLOW_LT_in_callExpression1596 = frozenset([13, 43])
    FOLLOW_arguments_in_callExpression1599 = frozenset([1, 13, 43, 72, 74])
    FOLLOW_LT_in_callExpression1602 = frozenset([13, 43, 72, 74])
    FOLLOW_callExpressionSuffix_in_callExpression1605 = frozenset([1, 13, 43, 72, 74])
    FOLLOW_arguments_in_callExpressionSuffix1634 = frozenset([1])
    FOLLOW_indexSuffix_in_callExpressionSuffix1639 = frozenset([1])
    FOLLOW_propertyReferenceSuffix_in_callExpressionSuffix1644 = frozenset([1])
    FOLLOW_43_in_arguments1655 = frozenset([13, 14, 15, 16, 42, 43, 45, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_arguments1658 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_arguments1662 = frozenset([13, 44, 45])
    FOLLOW_LT_in_arguments1665 = frozenset([13, 44])
    FOLLOW_44_in_arguments1669 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_arguments1671 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_arguments1675 = frozenset([13, 44, 45])
    FOLLOW_LT_in_arguments1681 = frozenset([1])
    FOLLOW_45_in_arguments1685 = frozenset([1])
    FOLLOW_72_in_indexSuffix1697 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_indexSuffix1699 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_expression_in_indexSuffix1702 = frozenset([13, 73])
    FOLLOW_LT_in_indexSuffix1704 = frozenset([13, 73])
    FOLLOW_73_in_indexSuffix1707 = frozenset([1])
    FOLLOW_74_in_propertyReferenceSuffix1730 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_propertyReferenceSuffix1732 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_propertyReferenceSuffix1735 = frozenset([1])
    FOLLOW_set_in_assignmentOperator0 = frozenset([1])
    FOLLOW_logicalORExpression_in_conditionalExpression1812 = frozenset([1, 13, 86])
    FOLLOW_LT_in_conditionalExpression1815 = frozenset([13, 86])
    FOLLOW_86_in_conditionalExpression1819 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_conditionalExpression1821 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_conditionalExpression1825 = frozenset([13, 63])
    FOLLOW_LT_in_conditionalExpression1827 = frozenset([13, 63])
    FOLLOW_63_in_conditionalExpression1831 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_conditionalExpression1833 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_conditionalExpression1837 = frozenset([1])
    FOLLOW_logicalORExpressionNoIn_in_conditionalExpressionNoIn1850 = frozenset([1, 13, 86])
    FOLLOW_LT_in_conditionalExpressionNoIn1853 = frozenset([13, 86])
    FOLLOW_86_in_conditionalExpressionNoIn1857 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_conditionalExpressionNoIn1859 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1863 = frozenset([13, 63])
    FOLLOW_LT_in_conditionalExpressionNoIn1865 = frozenset([13, 63])
    FOLLOW_63_in_conditionalExpressionNoIn1869 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_conditionalExpressionNoIn1871 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpressionNoIn_in_conditionalExpressionNoIn1875 = frozenset([1])
    FOLLOW_logicalANDExpression_in_logicalORExpression1888 = frozenset([1, 13, 87])
    FOLLOW_LT_in_logicalORExpression1891 = frozenset([13, 87])
    FOLLOW_87_in_logicalORExpression1895 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_logicalORExpression1897 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_logicalANDExpression_in_logicalORExpression1901 = frozenset([1, 13, 87])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1915 = frozenset([1, 13, 87])
    FOLLOW_LT_in_logicalORExpressionNoIn1918 = frozenset([13, 87])
    FOLLOW_87_in_logicalORExpressionNoIn1922 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_logicalORExpressionNoIn1924 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_logicalANDExpressionNoIn_in_logicalORExpressionNoIn1928 = frozenset([1, 13, 87])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1942 = frozenset([1, 13, 88])
    FOLLOW_LT_in_logicalANDExpression1945 = frozenset([13, 88])
    FOLLOW_88_in_logicalANDExpression1949 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_logicalANDExpression1951 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseORExpression_in_logicalANDExpression1955 = frozenset([1, 13, 88])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1969 = frozenset([1, 13, 88])
    FOLLOW_LT_in_logicalANDExpressionNoIn1972 = frozenset([13, 88])
    FOLLOW_88_in_logicalANDExpressionNoIn1976 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_logicalANDExpressionNoIn1978 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseORExpressionNoIn_in_logicalANDExpressionNoIn1982 = frozenset([1, 13, 88])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression1996 = frozenset([1, 13, 89])
    FOLLOW_LT_in_bitwiseORExpression1999 = frozenset([13, 89])
    FOLLOW_89_in_bitwiseORExpression2003 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseORExpression2005 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseXORExpression_in_bitwiseORExpression2009 = frozenset([1, 13, 89])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2023 = frozenset([1, 13, 89])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2026 = frozenset([13, 89])
    FOLLOW_89_in_bitwiseORExpressionNoIn2030 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseORExpressionNoIn2032 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseXORExpressionNoIn_in_bitwiseORExpressionNoIn2036 = frozenset([1, 13, 89])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2050 = frozenset([1, 13, 90])
    FOLLOW_LT_in_bitwiseXORExpression2053 = frozenset([13, 90])
    FOLLOW_90_in_bitwiseXORExpression2057 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseXORExpression2059 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseANDExpression_in_bitwiseXORExpression2063 = frozenset([1, 13, 90])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2077 = frozenset([1, 13, 90])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2080 = frozenset([13, 90])
    FOLLOW_90_in_bitwiseXORExpressionNoIn2084 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseXORExpressionNoIn2086 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_bitwiseANDExpressionNoIn_in_bitwiseXORExpressionNoIn2090 = frozenset([1, 13, 90])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2104 = frozenset([1, 13, 91])
    FOLLOW_LT_in_bitwiseANDExpression2107 = frozenset([13, 91])
    FOLLOW_91_in_bitwiseANDExpression2111 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseANDExpression2113 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_equalityExpression_in_bitwiseANDExpression2117 = frozenset([1, 13, 91])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2131 = frozenset([1, 13, 91])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2134 = frozenset([13, 91])
    FOLLOW_91_in_bitwiseANDExpressionNoIn2138 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_bitwiseANDExpressionNoIn2140 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_equalityExpressionNoIn_in_bitwiseANDExpressionNoIn2144 = frozenset([1, 13, 91])
    FOLLOW_relationalExpression_in_equalityExpression2158 = frozenset([1, 13, 92, 93, 94, 95])
    FOLLOW_LT_in_equalityExpression2161 = frozenset([13, 92, 93, 94, 95])
    FOLLOW_set_in_equalityExpression2165 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpression2181 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_relationalExpression_in_equalityExpression2185 = frozenset([1, 13, 92, 93, 94, 95])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2198 = frozenset([1, 13, 92, 93, 94, 95])
    FOLLOW_LT_in_equalityExpressionNoIn2201 = frozenset([13, 92, 93, 94, 95])
    FOLLOW_set_in_equalityExpressionNoIn2205 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_equalityExpressionNoIn2221 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_relationalExpressionNoIn_in_equalityExpressionNoIn2225 = frozenset([1, 13, 92, 93, 94, 95])
    FOLLOW_shiftExpression_in_relationalExpression2239 = frozenset([1, 13, 58, 96, 97, 98, 99, 100])
    FOLLOW_LT_in_relationalExpression2242 = frozenset([13, 58, 96, 97, 98, 99, 100])
    FOLLOW_set_in_relationalExpression2246 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_relationalExpression2270 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_shiftExpression_in_relationalExpression2274 = frozenset([1, 13, 58, 96, 97, 98, 99, 100])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2287 = frozenset([1, 13, 96, 97, 98, 99, 100])
    FOLLOW_LT_in_relationalExpressionNoIn2290 = frozenset([13, 96, 97, 98, 99, 100])
    FOLLOW_set_in_relationalExpressionNoIn2294 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_relationalExpressionNoIn2314 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_shiftExpression_in_relationalExpressionNoIn2318 = frozenset([1, 13, 96, 97, 98, 99, 100])
    FOLLOW_additiveExpression_in_shiftExpression2331 = frozenset([1, 13, 101, 102, 103])
    FOLLOW_LT_in_shiftExpression2334 = frozenset([13, 101, 102, 103])
    FOLLOW_set_in_shiftExpression2338 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_shiftExpression2350 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_additiveExpression_in_shiftExpression2354 = frozenset([1, 13, 101, 102, 103])
    FOLLOW_multiplicativeExpression_in_additiveExpression2367 = frozenset([1, 13, 104, 105])
    FOLLOW_LT_in_additiveExpression2370 = frozenset([13, 104, 105])
    FOLLOW_set_in_additiveExpression2374 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_additiveExpression2382 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_multiplicativeExpression_in_additiveExpression2386 = frozenset([1, 13, 104, 105])
    FOLLOW_unaryExpression_in_multiplicativeExpression2399 = frozenset([1, 13, 106, 107, 108])
    FOLLOW_LT_in_multiplicativeExpression2402 = frozenset([13, 106, 107, 108])
    FOLLOW_set_in_multiplicativeExpression2406 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_multiplicativeExpression2418 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_unaryExpression_in_multiplicativeExpression2422 = frozenset([1, 13, 106, 107, 108])
    FOLLOW_postfixExpression_in_unaryExpression2435 = frozenset([1])
    FOLLOW_set_in_unaryExpression2440 = frozenset([14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_unaryExpression_in_unaryExpression2476 = frozenset([1])
    FOLLOW_leftHandSideExpression_in_postfixExpression2488 = frozenset([1, 112, 113])
    FOLLOW_set_in_postfixExpression2490 = frozenset([1])
    FOLLOW_116_in_primaryExpression2508 = frozenset([1])
    FOLLOW_identifier_in_primaryExpression2513 = frozenset([1])
    FOLLOW_literal_in_primaryExpression2518 = frozenset([1])
    FOLLOW_arrayLiteral_in_primaryExpression2523 = frozenset([1])
    FOLLOW_objectLiteral_in_primaryExpression2528 = frozenset([1])
    FOLLOW_43_in_primaryExpression2533 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_primaryExpression2535 = frozenset([1])
    FOLLOW_expression_in_primaryExpression2539 = frozenset([13, 45])
    FOLLOW_LT_in_primaryExpression2541 = frozenset([1])
    FOLLOW_45_in_primaryExpression2545 = frozenset([1])
    FOLLOW_72_in_arrayLiteral2558 = frozenset([13, 14, 15, 16, 42, 43, 44, 46, 57, 71, 72, 73, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_arrayLiteral2560 = frozenset([1])
    FOLLOW_assignmentExpression_in_arrayLiteral2564 = frozenset([13, 44, 73])
    FOLLOW_LT_in_arrayLiteral2568 = frozenset([13, 44])
    FOLLOW_44_in_arrayLiteral2572 = frozenset([13, 14, 15, 16, 42, 43, 44, 46, 57, 71, 72, 73, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_arrayLiteral2575 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_arrayLiteral2579 = frozenset([13, 44, 73])
    FOLLOW_LT_in_arrayLiteral2585 = frozenset([1])
    FOLLOW_73_in_arrayLiteral2589 = frozenset([1])
    FOLLOW_46_in_objectLiteral2608 = frozenset([13, 14, 15, 16, 44, 47, 57, 117, 118])
    FOLLOW_LT_in_objectLiteral2610 = frozenset([13, 14, 15, 16, 44, 47, 57, 117, 118])
    FOLLOW_propertyNameAndValue_in_objectLiteral2613 = frozenset([13, 44, 47])
    FOLLOW_LT_in_objectLiteral2617 = frozenset([13, 44])
    FOLLOW_44_in_objectLiteral2620 = frozenset([13, 14, 15, 16, 57, 117, 118])
    FOLLOW_LT_in_objectLiteral2622 = frozenset([13, 14, 15, 16, 57, 117, 118])
    FOLLOW_propertyNameAndValue_in_objectLiteral2625 = frozenset([13, 44, 47])
    FOLLOW_LT_in_objectLiteral2629 = frozenset([13, 47])
    FOLLOW_47_in_objectLiteral2632 = frozenset([1])
    FOLLOW_propertyName_in_propertyNameAndValue2656 = frozenset([13, 63])
    FOLLOW_LT_in_propertyNameAndValue2658 = frozenset([13, 63])
    FOLLOW_63_in_propertyNameAndValue2661 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_propertyNameAndValue2663 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_assignmentExpression_in_propertyNameAndValue2666 = frozenset([1])
    FOLLOW_117_in_propertyNameAndValue2688 = frozenset([16, 57, 117, 118])
    FOLLOW_118_in_propertyNameAndValue2692 = frozenset([16, 57, 117, 118])
    FOLLOW_identifier_in_propertyNameAndValue2697 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_propertyNameAndValue2699 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_propertyNameAndValue2704 = frozenset([13, 43])
    FOLLOW_LT_in_propertyNameAndValue2706 = frozenset([13, 43])
    FOLLOW_formalParameterList_in_propertyNameAndValue2709 = frozenset([13, 46])
    FOLLOW_LT_in_propertyNameAndValue2711 = frozenset([13, 46])
    FOLLOW_statementBlock_in_propertyNameAndValue2714 = frozenset([1])
    FOLLOW_117_in_propertyNameAndValue2747 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_118_in_propertyNameAndValue2751 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_LT_in_propertyNameAndValue2754 = frozenset([13, 16, 57, 117, 118])
    FOLLOW_identifier_in_propertyNameAndValue2757 = frozenset([13, 43])
    FOLLOW_LT_in_propertyNameAndValue2759 = frozenset([13, 43])
    FOLLOW_formalParameterList_in_propertyNameAndValue2762 = frozenset([13, 46])
    FOLLOW_LT_in_propertyNameAndValue2764 = frozenset([13, 46])
    FOLLOW_statementBlock_in_propertyNameAndValue2767 = frozenset([1])
    FOLLOW_identifier_in_propertyName2801 = frozenset([1])
    FOLLOW_StringLiteral_in_propertyName2806 = frozenset([1])
    FOLLOW_NumericLiteral_in_propertyName2811 = frozenset([1])
    FOLLOW_119_in_literal2823 = frozenset([1])
    FOLLOW_120_in_literal2828 = frozenset([1])
    FOLLOW_121_in_literal2833 = frozenset([1])
    FOLLOW_StringLiteral_in_literal2838 = frozenset([1])
    FOLLOW_NumericLiteral_in_literal2843 = frozenset([1])
    FOLLOW_regularExpressionLiteral_in_literal2848 = frozenset([1])
    FOLLOW_set_in_reFirstChar0 = frozenset([1])
    FOLLOW_reFirstChar_in_reChars3226 = frozenset([1])
    FOLLOW_106_in_reChars3231 = frozenset([1])
    FOLLOW_107_in_regularExpressionLiteral3242 = frozenset([14, 15, 16, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122])
    FOLLOW_reFirstChar_in_regularExpressionLiteral3244 = frozenset([14, 15, 16, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122])
    FOLLOW_reChars_in_regularExpressionLiteral3246 = frozenset([14, 15, 16, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122])
    FOLLOW_107_in_regularExpressionLiteral3249 = frozenset([1, 16])
    FOLLOW_Identifier_in_regularExpressionLiteral3251 = frozenset([1])
    FOLLOW_set_in_identifier0 = frozenset([1])
    FOLLOW_functionDeclaration_in_synpred5129 = frozenset([1])
    FOLLOW_statementBlock_in_synpred21304 = frozenset([1])
    FOLLOW_expressionStatement_in_synpred24319 = frozenset([1])
    FOLLOW_labelledStatement_in_synpred31354 = frozenset([1])
    FOLLOW_LT_in_synpred34383 = frozenset([1])
    FOLLOW_LT_in_synpred61698 = frozenset([13, 53])
    FOLLOW_53_in_synpred61702 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_synpred61704 = frozenset([13, 14, 15, 16, 42, 43, 46, 48, 49, 50, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 67, 68, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_statement_in_synpred61708 = frozenset([1])
    FOLLOW_forStatement_in_synpred64732 = frozenset([1])
    FOLLOW_LT_in_synpred86922 = frozenset([1])
    FOLLOW_LT_in_synpred1211220 = frozenset([1])
    FOLLOW_LT_in_synpred1241245 = frozenset([1])
    FOLLOW_conditionalExpression_in_synpred1431437 = frozenset([1])
    FOLLOW_conditionalExpressionNoIn_in_synpred1461466 = frozenset([1])
    FOLLOW_callExpression_in_synpred1491495 = frozenset([1])
    FOLLOW_memberExpression_in_synpred1501512 = frozenset([1])
    FOLLOW_LT_in_synpred1571560 = frozenset([13, 72, 74])
    FOLLOW_memberExpressionSuffix_in_synpred1571564 = frozenset([1])
    FOLLOW_LT_in_synpred1611602 = frozenset([13, 43, 72, 74])
    FOLLOW_callExpressionSuffix_in_synpred1611605 = frozenset([1])
    FOLLOW_LT_in_synpred2592370 = frozenset([13, 104, 105])
    FOLLOW_set_in_synpred2592374 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_synpred2592382 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_multiplicativeExpression_in_synpred2592386 = frozenset([1])
    FOLLOW_LT_in_synpred2642402 = frozenset([13, 106, 107, 108])
    FOLLOW_set_in_synpred2642406 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_LT_in_synpred2642418 = frozenset([13, 14, 15, 16, 42, 43, 46, 57, 71, 72, 104, 105, 107, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121])
    FOLLOW_unaryExpression_in_synpred2642422 = frozenset([1])
    FOLLOW_LT_in_synpred2832560 = frozenset([1])
    FOLLOW_LT_in_synpred2902610 = frozenset([1])

