# Generated from grammar/Onion.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,72,8,2,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,4,4,89,8,4,11,4,12,4,90,3,4,93,8,4,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,101,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,111,
        8,6,1,7,1,7,4,7,115,8,7,11,7,12,7,116,1,7,1,7,1,7,1,7,1,7,1,7,4,
        7,125,8,7,11,7,12,7,126,1,7,1,7,1,7,1,7,3,7,133,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,161,8,8,1,9,1,9,5,9,165,8,9,10,9,
        12,9,168,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,179,
        8,10,10,10,12,10,182,9,10,1,10,1,10,1,10,1,10,1,10,3,10,189,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,4,11,197,8,11,11,11,12,11,198,1,11,
        1,11,1,11,1,11,1,11,3,11,206,8,11,1,12,1,12,1,12,1,12,5,12,212,8,
        12,10,12,12,12,215,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,
        5,14,225,8,14,10,14,12,14,228,9,14,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,244,8,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,253,8,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,265,8,17,1,18,1,18,1,18,1,18,5,18,
        271,8,18,10,18,12,18,274,9,18,1,18,1,18,1,18,1,19,1,19,5,19,281,
        8,19,10,19,12,19,284,9,19,1,20,1,20,1,20,1,20,1,21,1,21,4,21,292,
        8,21,11,21,12,21,293,1,21,1,21,1,22,1,22,1,22,1,22,5,22,302,8,22,
        10,22,12,22,305,9,22,1,22,1,22,1,22,1,23,4,23,311,8,23,11,23,12,
        23,312,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,36,39,342,0,51,1,0,0,0,
        2,57,1,0,0,0,4,71,1,0,0,0,6,77,1,0,0,0,8,92,1,0,0,0,10,100,1,0,0,
        0,12,110,1,0,0,0,14,132,1,0,0,0,16,160,1,0,0,0,18,162,1,0,0,0,20,
        169,1,0,0,0,22,190,1,0,0,0,24,207,1,0,0,0,26,219,1,0,0,0,28,222,
        1,0,0,0,30,229,1,0,0,0,32,252,1,0,0,0,34,264,1,0,0,0,36,266,1,0,
        0,0,38,278,1,0,0,0,40,285,1,0,0,0,42,289,1,0,0,0,44,297,1,0,0,0,
        46,310,1,0,0,0,48,314,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,53,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,5,0,0,1,
        56,1,1,0,0,0,57,58,5,1,0,0,58,59,3,4,2,0,59,60,5,2,0,0,60,3,1,0,
        0,0,61,72,3,8,4,0,62,72,3,10,5,0,63,72,3,30,15,0,64,72,3,36,18,0,
        65,72,3,40,20,0,66,72,3,32,16,0,67,72,3,6,3,0,68,72,3,24,12,0,69,
        72,3,26,13,0,70,72,3,46,23,0,71,61,1,0,0,0,71,62,1,0,0,0,71,63,1,
        0,0,0,71,64,1,0,0,0,71,65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,
        68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,5,1,0,0,0,73,74,5,3,0,
        0,74,78,5,40,0,0,75,76,5,4,0,0,76,78,5,40,0,0,77,73,1,0,0,0,77,75,
        1,0,0,0,78,7,1,0,0,0,79,80,5,5,0,0,80,81,5,40,0,0,81,93,3,10,5,0,
        82,88,5,5,0,0,83,84,5,1,0,0,84,85,5,40,0,0,85,86,3,10,5,0,86,87,
        5,2,0,0,87,89,1,0,0,0,88,83,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,
        90,91,1,0,0,0,91,93,1,0,0,0,92,79,1,0,0,0,92,82,1,0,0,0,93,9,1,0,
        0,0,94,101,3,48,24,0,95,101,5,40,0,0,96,97,5,1,0,0,97,98,3,12,6,
        0,98,99,5,2,0,0,99,101,1,0,0,0,100,94,1,0,0,0,100,95,1,0,0,0,100,
        96,1,0,0,0,101,11,1,0,0,0,102,111,3,14,7,0,103,111,3,16,8,0,104,
        111,3,18,9,0,105,111,3,28,14,0,106,111,3,20,10,0,107,111,3,22,11,
        0,108,111,3,38,19,0,109,111,3,34,17,0,110,102,1,0,0,0,110,103,1,
        0,0,0,110,104,1,0,0,0,110,105,1,0,0,0,110,106,1,0,0,0,110,107,1,
        0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,13,1,0,0,0,112,114,5,6,
        0,0,113,115,3,10,5,0,114,113,1,0,0,0,115,116,1,0,0,0,116,114,1,0,
        0,0,116,117,1,0,0,0,117,133,1,0,0,0,118,119,5,7,0,0,119,120,3,10,
        5,0,120,121,3,10,5,0,121,133,1,0,0,0,122,124,5,8,0,0,123,125,3,10,
        5,0,124,123,1,0,0,0,125,126,1,0,0,0,126,124,1,0,0,0,126,127,1,0,
        0,0,127,133,1,0,0,0,128,129,5,9,0,0,129,130,3,10,5,0,130,131,3,10,
        5,0,131,133,1,0,0,0,132,112,1,0,0,0,132,118,1,0,0,0,132,122,1,0,
        0,0,132,128,1,0,0,0,133,15,1,0,0,0,134,135,5,10,0,0,135,136,3,10,
        5,0,136,137,3,10,5,0,137,161,1,0,0,0,138,139,5,11,0,0,139,140,3,
        10,5,0,140,141,3,10,5,0,141,161,1,0,0,0,142,143,5,12,0,0,143,144,
        3,10,5,0,144,145,3,10,5,0,145,161,1,0,0,0,146,147,5,13,0,0,147,148,
        3,10,5,0,148,149,3,10,5,0,149,161,1,0,0,0,150,151,5,14,0,0,151,152,
        3,10,5,0,152,153,3,10,5,0,153,161,1,0,0,0,154,155,5,15,0,0,155,156,
        3,10,5,0,156,157,3,10,5,0,157,161,1,0,0,0,158,159,5,16,0,0,159,161,
        3,10,5,0,160,134,1,0,0,0,160,138,1,0,0,0,160,142,1,0,0,0,160,146,
        1,0,0,0,160,150,1,0,0,0,160,154,1,0,0,0,160,158,1,0,0,0,161,17,1,
        0,0,0,162,166,5,17,0,0,163,165,3,10,5,0,164,163,1,0,0,0,165,168,
        1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,19,1,0,0,0,168,166,1,
        0,0,0,169,170,5,18,0,0,170,171,3,10,5,0,171,180,3,2,1,0,172,173,
        5,1,0,0,173,174,5,19,0,0,174,175,3,10,5,0,175,176,3,2,1,0,176,177,
        5,2,0,0,177,179,1,0,0,0,178,172,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,188,1,0,0,0,182,180,1,0,0,0,183,184,
        5,1,0,0,184,185,5,20,0,0,185,186,3,2,1,0,186,187,5,2,0,0,187,189,
        1,0,0,0,188,183,1,0,0,0,188,189,1,0,0,0,189,21,1,0,0,0,190,196,5,
        21,0,0,191,192,5,1,0,0,192,193,3,10,5,0,193,194,3,2,1,0,194,195,
        5,2,0,0,195,197,1,0,0,0,196,191,1,0,0,0,197,198,1,0,0,0,198,196,
        1,0,0,0,198,199,1,0,0,0,199,205,1,0,0,0,200,201,5,1,0,0,201,202,
        5,22,0,0,202,203,3,2,1,0,203,204,5,2,0,0,204,206,1,0,0,0,205,200,
        1,0,0,0,205,206,1,0,0,0,206,23,1,0,0,0,207,208,5,23,0,0,208,209,
        5,40,0,0,209,213,5,1,0,0,210,212,5,40,0,0,211,210,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,
        1,0,0,0,216,217,5,2,0,0,217,218,3,46,23,0,218,25,1,0,0,0,219,220,
        5,24,0,0,220,221,3,10,5,0,221,27,1,0,0,0,222,226,5,40,0,0,223,225,
        3,10,5,0,224,223,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,29,1,0,0,0,228,226,1,0,0,0,229,230,5,25,0,0,230,231,
        3,10,5,0,231,31,1,0,0,0,232,233,5,26,0,0,233,234,3,10,5,0,234,235,
        3,46,23,0,235,253,1,0,0,0,236,237,5,27,0,0,237,238,5,40,0,0,238,
        239,5,28,0,0,239,240,5,1,0,0,240,241,3,10,5,0,241,243,3,10,5,0,242,
        244,3,10,5,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,
        246,5,2,0,0,246,247,3,46,23,0,247,253,1,0,0,0,248,249,5,29,0,0,249,
        250,3,10,5,0,250,251,3,46,23,0,251,253,1,0,0,0,252,232,1,0,0,0,252,
        236,1,0,0,0,252,248,1,0,0,0,253,33,1,0,0,0,254,255,5,30,0,0,255,
        265,3,10,5,0,256,257,5,31,0,0,257,265,3,10,5,0,258,259,5,32,0,0,
        259,260,3,10,5,0,260,261,3,10,5,0,261,265,1,0,0,0,262,263,5,33,0,
        0,263,265,3,10,5,0,264,254,1,0,0,0,264,256,1,0,0,0,264,258,1,0,0,
        0,264,262,1,0,0,0,265,35,1,0,0,0,266,267,5,34,0,0,267,268,5,40,0,
        0,268,272,5,1,0,0,269,271,5,40,0,0,270,269,1,0,0,0,271,274,1,0,0,
        0,272,270,1,0,0,0,272,273,1,0,0,0,273,275,1,0,0,0,274,272,1,0,0,
        0,275,276,5,2,0,0,276,277,3,46,23,0,277,37,1,0,0,0,278,282,5,40,
        0,0,279,281,3,10,5,0,280,279,1,0,0,0,281,284,1,0,0,0,282,280,1,0,
        0,0,282,283,1,0,0,0,283,39,1,0,0,0,284,282,1,0,0,0,285,286,5,35,
        0,0,286,287,5,40,0,0,287,288,3,42,21,0,288,41,1,0,0,0,289,291,5,
        1,0,0,290,292,3,44,22,0,291,290,1,0,0,0,292,293,1,0,0,0,293,291,
        1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,0,295,296,5,2,0,0,296,43,1,
        0,0,0,297,298,5,23,0,0,298,299,5,40,0,0,299,303,5,1,0,0,300,302,
        5,40,0,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,307,5,2,0,0,307,308,
        3,46,23,0,308,45,1,0,0,0,309,311,3,2,1,0,310,309,1,0,0,0,311,312,
        1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,47,1,0,0,0,314,315,7,
        0,0,0,315,49,1,0,0,0,26,53,71,77,90,92,100,110,116,126,132,160,166,
        180,188,198,205,213,226,243,252,264,272,282,293,303,312
    ]

class OnionParser ( Parser ):

    grammarFileName = "Onion.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'inc'", "'dec'", "'let'", 
                     "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'not'", "'list'", "'if'", "'elif'", 
                     "'else'", "'cond'", "'t'", "'def'", "'return'", "'print'", 
                     "'repeat'", "'loop'", "'range'", "'while'", "'head'", 
                     "'tail'", "'getid'", "'sizeof'", "'macro'", "'class'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "INT", "FLOAT", "STRING", "IDENTIFIER", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_statementType = 2
    RULE_incDecStmt = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_compoundExpr = 6
    RULE_arithmeticExpr = 7
    RULE_booleanExpr = 8
    RULE_listExpr = 9
    RULE_ifExpr = 10
    RULE_branchExpr = 11
    RULE_functionDef = 12
    RULE_returnStmt = 13
    RULE_functionCall = 14
    RULE_printStatement = 15
    RULE_loopStatement = 16
    RULE_listOpExpr = 17
    RULE_macroDef = 18
    RULE_macroCall = 19
    RULE_classDef = 20
    RULE_classBody = 21
    RULE_methodDef = 22
    RULE_block = 23
    RULE_literal = 24

    ruleNames =  [ "program", "statement", "statementType", "incDecStmt", 
                   "assignment", "expression", "compoundExpr", "arithmeticExpr", 
                   "booleanExpr", "listExpr", "ifExpr", "branchExpr", "functionDef", 
                   "returnStmt", "functionCall", "printStatement", "loopStatement", 
                   "listOpExpr", "macroDef", "macroCall", "classDef", "classBody", 
                   "methodDef", "block", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    BOOL=36
    INT=37
    FLOAT=38
    STRING=39
    IDENTIFIER=40
    WS=41
    COMMENT=42
    LINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(OnionParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OnionParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.statement()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 55
            self.match(OnionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementType(self):
            return self.getTypedRuleContext(OnionParser.StatementTypeContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = OnionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(OnionParser.T__0)
            self.state = 58
            self.statementType()
            self.state = 59
            self.match(OnionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(OnionParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(OnionParser.PrintStatementContext,0)


        def macroDef(self):
            return self.getTypedRuleContext(OnionParser.MacroDefContext,0)


        def classDef(self):
            return self.getTypedRuleContext(OnionParser.ClassDefContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(OnionParser.LoopStatementContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(OnionParser.IncDecStmtContext,0)


        def functionDef(self):
            return self.getTypedRuleContext(OnionParser.FunctionDefContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(OnionParser.ReturnStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_statementType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementType" ):
                listener.enterStatementType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementType" ):
                listener.exitStatementType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementType" ):
                return visitor.visitStatementType(self)
            else:
                return visitor.visitChildren(self)




    def statementType(self):

        localctx = OnionParser.StatementTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementType)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.printStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.macroDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.classDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.loopStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.incDecStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.functionDef()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.returnStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 70
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecStmt" ):
                return visitor.visitIncDecStmt(self)
            else:
                return visitor.visitChildren(self)




    def incDecStmt(self):

        localctx = OnionParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_incDecStmt)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(OnionParser.T__2)
                self.state = 74
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(OnionParser.T__3)
                self.state = 76
                self.match(OnionParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = OnionParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(OnionParser.T__4)
                self.state = 80
                self.match(OnionParser.IDENTIFIER)
                self.state = 81
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(OnionParser.T__4)
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 83
                    self.match(OnionParser.T__0)
                    self.state = 84
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 85
                    self.expression()
                    self.state = 86
                    self.match(OnionParser.T__1)
                    self.state = 90 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(OnionParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def compoundExpr(self):
            return self.getTypedRuleContext(OnionParser.CompoundExprContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = OnionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(OnionParser.T__0)
                self.state = 97
                self.compoundExpr()
                self.state = 98
                self.match(OnionParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmeticExpr(self):
            return self.getTypedRuleContext(OnionParser.ArithmeticExprContext,0)


        def booleanExpr(self):
            return self.getTypedRuleContext(OnionParser.BooleanExprContext,0)


        def listExpr(self):
            return self.getTypedRuleContext(OnionParser.ListExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(OnionParser.FunctionCallContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(OnionParser.IfExprContext,0)


        def branchExpr(self):
            return self.getTypedRuleContext(OnionParser.BranchExprContext,0)


        def macroCall(self):
            return self.getTypedRuleContext(OnionParser.MacroCallContext,0)


        def listOpExpr(self):
            return self.getTypedRuleContext(OnionParser.ListOpExprContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_compoundExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundExpr" ):
                listener.enterCompoundExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundExpr" ):
                listener.exitCompoundExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundExpr" ):
                return visitor.visitCompoundExpr(self)
            else:
                return visitor.visitChildren(self)




    def compoundExpr(self):

        localctx = OnionParser.CompoundExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compoundExpr)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.arithmeticExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.booleanExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.listExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.ifExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.branchExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.macroCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.listOpExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_arithmeticExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticExpr(self):

        localctx = OnionParser.ArithmeticExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arithmeticExpr)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(OnionParser.T__5)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 113
                    self.expression()
                    self.state = 116 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(OnionParser.T__6)
                self.state = 119
                self.expression()
                self.state = 120
                self.expression()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(OnionParser.T__7)
                self.state = 124 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 123
                    self.expression()
                    self.state = 126 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.match(OnionParser.T__8)
                self.state = 129
                self.expression()
                self.state = 130
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_booleanExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpr" ):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpr" ):
                listener.exitBooleanExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpr" ):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpr(self):

        localctx = OnionParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_booleanExpr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(OnionParser.T__9)
                self.state = 135
                self.expression()
                self.state = 136
                self.expression()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(OnionParser.T__10)
                self.state = 139
                self.expression()
                self.state = 140
                self.expression()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(OnionParser.T__11)
                self.state = 143
                self.expression()
                self.state = 144
                self.expression()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(OnionParser.T__12)
                self.state = 147
                self.expression()
                self.state = 148
                self.expression()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.match(OnionParser.T__13)
                self.state = 151
                self.expression()
                self.state = 152
                self.expression()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 154
                self.match(OnionParser.T__14)
                self.state = 155
                self.expression()
                self.state = 156
                self.expression()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 158
                self.match(OnionParser.T__15)
                self.state = 159
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_listExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpr" ):
                return visitor.visitListExpr(self)
            else:
                return visitor.visitChildren(self)




    def listExpr(self):

        localctx = OnionParser.ListExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(OnionParser.T__16)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 163
                self.expression()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = OnionParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(OnionParser.T__17)
            self.state = 170
            self.expression()
            self.state = 171
            self.statement()
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.match(OnionParser.T__0)
                    self.state = 173
                    self.match(OnionParser.T__18)
                    self.state = 174
                    self.expression()
                    self.state = 175
                    self.statement()
                    self.state = 176
                    self.match(OnionParser.T__1) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 183
                self.match(OnionParser.T__0)
                self.state = 184
                self.match(OnionParser.T__19)
                self.state = 185
                self.statement()
                self.state = 186
                self.match(OnionParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BranchExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_branchExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranchExpr" ):
                listener.enterBranchExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranchExpr" ):
                listener.exitBranchExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranchExpr" ):
                return visitor.visitBranchExpr(self)
            else:
                return visitor.visitChildren(self)




    def branchExpr(self):

        localctx = OnionParser.BranchExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_branchExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(OnionParser.T__20)
            self.state = 196 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 191
                    self.match(OnionParser.T__0)
                    self.state = 192
                    self.expression()
                    self.state = 193
                    self.statement()
                    self.state = 194
                    self.match(OnionParser.T__1)

                else:
                    raise NoViableAltException(self)
                self.state = 198 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 200
                self.match(OnionParser.T__0)
                self.state = 201
                self.match(OnionParser.T__21)
                self.state = 202
                self.statement()
                self.state = 203
                self.match(OnionParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = OnionParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(OnionParser.T__22)
            self.state = 208
            self.match(OnionParser.IDENTIFIER)
            self.state = 209
            self.match(OnionParser.T__0)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 210
                self.match(OnionParser.IDENTIFIER)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(OnionParser.T__1)
            self.state = 217
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = OnionParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(OnionParser.T__23)
            self.state = 220
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = OnionParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(OnionParser.IDENTIFIER)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 223
                self.expression()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = OnionParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(OnionParser.T__24)
            self.state = 230
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = OnionParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(OnionParser.T__25)
                self.state = 233
                self.expression()
                self.state = 234
                self.block()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(OnionParser.T__26)
                self.state = 237
                self.match(OnionParser.IDENTIFIER)
                self.state = 238
                self.match(OnionParser.T__27)
                self.state = 239
                self.match(OnionParser.T__0)
                self.state = 240
                self.expression()
                self.state = 241
                self.expression()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                    self.state = 242
                    self.expression()


                self.state = 245
                self.match(OnionParser.T__1)
                self.state = 246
                self.block()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(OnionParser.T__28)
                self.state = 249
                self.expression()
                self.state = 250
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_listOpExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListOpExpr" ):
                listener.enterListOpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListOpExpr" ):
                listener.exitListOpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOpExpr" ):
                return visitor.visitListOpExpr(self)
            else:
                return visitor.visitChildren(self)




    def listOpExpr(self):

        localctx = OnionParser.ListOpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_listOpExpr)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(OnionParser.T__29)
                self.state = 255
                self.expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(OnionParser.T__30)
                self.state = 257
                self.expression()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(OnionParser.T__31)
                self.state = 259
                self.expression()
                self.state = 260
                self.expression()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.match(OnionParser.T__32)
                self.state = 263
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_macroDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroDef" ):
                listener.enterMacroDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroDef" ):
                listener.exitMacroDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroDef" ):
                return visitor.visitMacroDef(self)
            else:
                return visitor.visitChildren(self)




    def macroDef(self):

        localctx = OnionParser.MacroDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_macroDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(OnionParser.T__33)
            self.state = 267
            self.match(OnionParser.IDENTIFIER)
            self.state = 268
            self.match(OnionParser.T__0)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 269
                self.match(OnionParser.IDENTIFIER)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
            self.match(OnionParser.T__1)
            self.state = 276
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_macroCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacroCall" ):
                listener.enterMacroCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacroCall" ):
                listener.exitMacroCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroCall" ):
                return visitor.visitMacroCall(self)
            else:
                return visitor.visitChildren(self)




    def macroCall(self):

        localctx = OnionParser.MacroCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macroCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(OnionParser.IDENTIFIER)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 279
                self.expression()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def classBody(self):
            return self.getTypedRuleContext(OnionParser.ClassBodyContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_classDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDef" ):
                listener.enterClassDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDef" ):
                listener.exitClassDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDef" ):
                return visitor.visitClassDef(self)
            else:
                return visitor.visitChildren(self)




    def classDef(self):

        localctx = OnionParser.ClassDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_classDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(OnionParser.T__34)
            self.state = 286
            self.match(OnionParser.IDENTIFIER)
            self.state = 287
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.MethodDefContext)
            else:
                return self.getTypedRuleContext(OnionParser.MethodDefContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = OnionParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(OnionParser.T__0)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 290
                self.methodDef()
                self.state = 293 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

            self.state = 295
            self.match(OnionParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(OnionParser.IDENTIFIER)
            else:
                return self.getToken(OnionParser.IDENTIFIER, i)

        def block(self):
            return self.getTypedRuleContext(OnionParser.BlockContext,0)


        def getRuleIndex(self):
            return OnionParser.RULE_methodDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDef" ):
                listener.enterMethodDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDef" ):
                listener.exitMethodDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDef" ):
                return visitor.visitMethodDef(self)
            else:
                return visitor.visitChildren(self)




    def methodDef(self):

        localctx = OnionParser.MethodDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_methodDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(OnionParser.T__22)
            self.state = 298
            self.match(OnionParser.IDENTIFIER)
            self.state = 299
            self.match(OnionParser.T__0)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 300
                self.match(OnionParser.IDENTIFIER)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.match(OnionParser.T__1)
            self.state = 307
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.StatementContext)
            else:
                return self.getTypedRuleContext(OnionParser.StatementContext,i)


        def getRuleIndex(self):
            return OnionParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = OnionParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 309
                self.statement()
                self.state = 312 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(OnionParser.INT, 0)

        def FLOAT(self):
            return self.getToken(OnionParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(OnionParser.BOOL, 0)

        def STRING(self):
            return self.getToken(OnionParser.STRING, 0)

        def getRuleIndex(self):
            return OnionParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = OnionParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1030792151040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





