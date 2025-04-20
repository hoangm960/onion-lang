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
        4,1,43,320,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,4,0,52,8,0,11,0,
        12,0,53,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,75,8,2,1,3,1,3,1,3,1,3,3,3,81,8,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,92,8,4,11,4,12,4,93,3,4,96,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,104,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,114,8,6,1,7,1,7,4,7,118,8,7,11,7,12,7,119,1,7,1,7,1,7,1,
        7,1,7,1,7,4,7,128,8,7,11,7,12,7,129,1,7,1,7,1,7,1,7,3,7,136,8,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,164,8,8,1,9,1,9,5,9,
        168,8,9,10,9,12,9,171,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,182,8,10,10,10,12,10,185,9,10,1,10,1,10,1,10,1,10,1,10,
        3,10,192,8,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,200,8,11,11,11,
        12,11,201,1,11,1,11,1,11,1,11,1,11,3,11,209,8,11,1,12,1,12,1,12,
        1,12,5,12,215,8,12,10,12,12,12,218,9,12,1,12,1,12,1,12,1,13,1,13,
        1,13,1,14,1,14,5,14,228,8,14,10,14,12,14,231,9,14,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,247,
        8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,256,8,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,268,8,17,1,18,1,18,
        1,18,1,18,5,18,274,8,18,10,18,12,18,277,9,18,1,18,1,18,1,18,1,19,
        1,19,5,19,284,8,19,10,19,12,19,287,9,19,1,20,1,20,1,20,1,20,1,21,
        1,21,4,21,295,8,21,11,21,12,21,296,1,21,1,21,1,22,1,22,1,22,1,22,
        5,22,305,8,22,10,22,12,22,308,9,22,1,22,1,22,1,22,1,23,4,23,314,
        8,23,11,23,12,23,315,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,36,39,348,
        0,51,1,0,0,0,2,57,1,0,0,0,4,74,1,0,0,0,6,80,1,0,0,0,8,95,1,0,0,0,
        10,103,1,0,0,0,12,113,1,0,0,0,14,135,1,0,0,0,16,163,1,0,0,0,18,165,
        1,0,0,0,20,172,1,0,0,0,22,193,1,0,0,0,24,210,1,0,0,0,26,222,1,0,
        0,0,28,225,1,0,0,0,30,232,1,0,0,0,32,255,1,0,0,0,34,267,1,0,0,0,
        36,269,1,0,0,0,38,281,1,0,0,0,40,288,1,0,0,0,42,292,1,0,0,0,44,300,
        1,0,0,0,46,313,1,0,0,0,48,317,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,
        0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,
        5,0,0,1,56,1,1,0,0,0,57,58,5,1,0,0,58,59,3,4,2,0,59,60,5,2,0,0,60,
        3,1,0,0,0,61,75,3,8,4,0,62,75,3,10,5,0,63,75,3,30,15,0,64,75,3,36,
        18,0,65,75,3,40,20,0,66,75,3,32,16,0,67,75,3,6,3,0,68,75,3,24,12,
        0,69,75,3,26,13,0,70,75,3,46,23,0,71,75,3,28,14,0,72,75,3,20,10,
        0,73,75,3,22,11,0,74,61,1,0,0,0,74,62,1,0,0,0,74,63,1,0,0,0,74,64,
        1,0,0,0,74,65,1,0,0,0,74,66,1,0,0,0,74,67,1,0,0,0,74,68,1,0,0,0,
        74,69,1,0,0,0,74,70,1,0,0,0,74,71,1,0,0,0,74,72,1,0,0,0,74,73,1,
        0,0,0,75,5,1,0,0,0,76,77,5,3,0,0,77,81,5,40,0,0,78,79,5,4,0,0,79,
        81,5,40,0,0,80,76,1,0,0,0,80,78,1,0,0,0,81,7,1,0,0,0,82,83,5,5,0,
        0,83,84,5,40,0,0,84,96,3,10,5,0,85,91,5,5,0,0,86,87,5,1,0,0,87,88,
        5,40,0,0,88,89,3,10,5,0,89,90,5,2,0,0,90,92,1,0,0,0,91,86,1,0,0,
        0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,82,
        1,0,0,0,95,85,1,0,0,0,96,9,1,0,0,0,97,104,3,48,24,0,98,104,5,40,
        0,0,99,100,5,1,0,0,100,101,3,12,6,0,101,102,5,2,0,0,102,104,1,0,
        0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,99,1,0,0,0,104,11,1,0,0,0,
        105,114,3,14,7,0,106,114,3,16,8,0,107,114,3,18,9,0,108,114,3,28,
        14,0,109,114,3,20,10,0,110,114,3,22,11,0,111,114,3,38,19,0,112,114,
        3,34,17,0,113,105,1,0,0,0,113,106,1,0,0,0,113,107,1,0,0,0,113,108,
        1,0,0,0,113,109,1,0,0,0,113,110,1,0,0,0,113,111,1,0,0,0,113,112,
        1,0,0,0,114,13,1,0,0,0,115,117,5,6,0,0,116,118,3,10,5,0,117,116,
        1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,136,
        1,0,0,0,121,122,5,7,0,0,122,123,3,10,5,0,123,124,3,10,5,0,124,136,
        1,0,0,0,125,127,5,8,0,0,126,128,3,10,5,0,127,126,1,0,0,0,128,129,
        1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,136,1,0,0,0,131,132,
        5,9,0,0,132,133,3,10,5,0,133,134,3,10,5,0,134,136,1,0,0,0,135,115,
        1,0,0,0,135,121,1,0,0,0,135,125,1,0,0,0,135,131,1,0,0,0,136,15,1,
        0,0,0,137,138,5,10,0,0,138,139,3,10,5,0,139,140,3,10,5,0,140,164,
        1,0,0,0,141,142,5,11,0,0,142,143,3,10,5,0,143,144,3,10,5,0,144,164,
        1,0,0,0,145,146,5,12,0,0,146,147,3,10,5,0,147,148,3,10,5,0,148,164,
        1,0,0,0,149,150,5,13,0,0,150,151,3,10,5,0,151,152,3,10,5,0,152,164,
        1,0,0,0,153,154,5,14,0,0,154,155,3,10,5,0,155,156,3,10,5,0,156,164,
        1,0,0,0,157,158,5,15,0,0,158,159,3,10,5,0,159,160,3,10,5,0,160,164,
        1,0,0,0,161,162,5,16,0,0,162,164,3,10,5,0,163,137,1,0,0,0,163,141,
        1,0,0,0,163,145,1,0,0,0,163,149,1,0,0,0,163,153,1,0,0,0,163,157,
        1,0,0,0,163,161,1,0,0,0,164,17,1,0,0,0,165,169,5,17,0,0,166,168,
        3,10,5,0,167,166,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,
        1,0,0,0,170,19,1,0,0,0,171,169,1,0,0,0,172,173,5,18,0,0,173,174,
        3,10,5,0,174,183,3,2,1,0,175,176,5,1,0,0,176,177,5,19,0,0,177,178,
        3,10,5,0,178,179,3,2,1,0,179,180,5,2,0,0,180,182,1,0,0,0,181,175,
        1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,191,
        1,0,0,0,185,183,1,0,0,0,186,187,5,1,0,0,187,188,5,20,0,0,188,189,
        3,2,1,0,189,190,5,2,0,0,190,192,1,0,0,0,191,186,1,0,0,0,191,192,
        1,0,0,0,192,21,1,0,0,0,193,199,5,21,0,0,194,195,5,1,0,0,195,196,
        3,10,5,0,196,197,3,2,1,0,197,198,5,2,0,0,198,200,1,0,0,0,199,194,
        1,0,0,0,200,201,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,208,
        1,0,0,0,203,204,5,1,0,0,204,205,5,22,0,0,205,206,3,2,1,0,206,207,
        5,2,0,0,207,209,1,0,0,0,208,203,1,0,0,0,208,209,1,0,0,0,209,23,1,
        0,0,0,210,211,5,23,0,0,211,212,5,40,0,0,212,216,5,1,0,0,213,215,
        5,40,0,0,214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,
        1,0,0,0,217,219,1,0,0,0,218,216,1,0,0,0,219,220,5,2,0,0,220,221,
        3,46,23,0,221,25,1,0,0,0,222,223,5,24,0,0,223,224,3,10,5,0,224,27,
        1,0,0,0,225,229,5,40,0,0,226,228,3,10,5,0,227,226,1,0,0,0,228,231,
        1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,29,1,0,0,0,231,229,1,
        0,0,0,232,233,5,25,0,0,233,234,3,10,5,0,234,31,1,0,0,0,235,236,5,
        26,0,0,236,237,3,10,5,0,237,238,3,46,23,0,238,256,1,0,0,0,239,240,
        5,27,0,0,240,241,5,40,0,0,241,242,5,28,0,0,242,243,5,1,0,0,243,244,
        3,10,5,0,244,246,3,10,5,0,245,247,3,10,5,0,246,245,1,0,0,0,246,247,
        1,0,0,0,247,248,1,0,0,0,248,249,5,2,0,0,249,250,3,46,23,0,250,256,
        1,0,0,0,251,252,5,29,0,0,252,253,3,10,5,0,253,254,3,46,23,0,254,
        256,1,0,0,0,255,235,1,0,0,0,255,239,1,0,0,0,255,251,1,0,0,0,256,
        33,1,0,0,0,257,258,5,30,0,0,258,268,3,10,5,0,259,260,5,31,0,0,260,
        268,3,10,5,0,261,262,5,32,0,0,262,263,3,10,5,0,263,264,3,10,5,0,
        264,268,1,0,0,0,265,266,5,33,0,0,266,268,3,10,5,0,267,257,1,0,0,
        0,267,259,1,0,0,0,267,261,1,0,0,0,267,265,1,0,0,0,268,35,1,0,0,0,
        269,270,5,34,0,0,270,271,5,40,0,0,271,275,5,1,0,0,272,274,5,40,0,
        0,273,272,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,
        0,276,278,1,0,0,0,277,275,1,0,0,0,278,279,5,2,0,0,279,280,3,46,23,
        0,280,37,1,0,0,0,281,285,5,40,0,0,282,284,3,10,5,0,283,282,1,0,0,
        0,284,287,1,0,0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,39,1,0,0,0,
        287,285,1,0,0,0,288,289,5,35,0,0,289,290,5,40,0,0,290,291,3,42,21,
        0,291,41,1,0,0,0,292,294,5,1,0,0,293,295,3,44,22,0,294,293,1,0,0,
        0,295,296,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,
        0,298,299,5,2,0,0,299,43,1,0,0,0,300,301,5,23,0,0,301,302,5,40,0,
        0,302,306,5,1,0,0,303,305,5,40,0,0,304,303,1,0,0,0,305,308,1,0,0,
        0,306,304,1,0,0,0,306,307,1,0,0,0,307,309,1,0,0,0,308,306,1,0,0,
        0,309,310,5,2,0,0,310,311,3,46,23,0,311,45,1,0,0,0,312,314,3,2,1,
        0,313,312,1,0,0,0,314,315,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,
        0,316,47,1,0,0,0,317,318,7,0,0,0,318,49,1,0,0,0,26,53,74,80,93,95,
        103,113,119,129,135,163,169,183,191,201,208,216,229,246,255,267,
        275,285,296,306,315
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


        def functionCall(self):
            return self.getTypedRuleContext(OnionParser.FunctionCallContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(OnionParser.IfExprContext,0)


        def branchExpr(self):
            return self.getTypedRuleContext(OnionParser.BranchExprContext,0)


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
            self.state = 74
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

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 71
                self.functionCall()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 72
                self.ifExpr()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 73
                self.branchExpr()
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
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(OnionParser.T__2)
                self.state = 77
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(OnionParser.T__3)
                self.state = 79
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(OnionParser.T__4)
                self.state = 83
                self.match(OnionParser.IDENTIFIER)
                self.state = 84
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(OnionParser.T__4)
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 86
                    self.match(OnionParser.T__0)
                    self.state = 87
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 88
                    self.expression()
                    self.state = 89
                    self.match(OnionParser.T__1)
                    self.state = 93 
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
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(OnionParser.IDENTIFIER)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(OnionParser.T__0)
                self.state = 100
                self.compoundExpr()
                self.state = 101
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.arithmeticExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.booleanExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.listExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.ifExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.branchExpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.macroCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 112
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
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(OnionParser.T__5)
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 116
                    self.expression()
                    self.state = 119 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(OnionParser.T__6)
                self.state = 122
                self.expression()
                self.state = 123
                self.expression()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(OnionParser.T__7)
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 126
                    self.expression()
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0)):
                        break

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.match(OnionParser.T__8)
                self.state = 132
                self.expression()
                self.state = 133
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
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(OnionParser.T__9)
                self.state = 138
                self.expression()
                self.state = 139
                self.expression()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(OnionParser.T__10)
                self.state = 142
                self.expression()
                self.state = 143
                self.expression()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(OnionParser.T__11)
                self.state = 146
                self.expression()
                self.state = 147
                self.expression()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.match(OnionParser.T__12)
                self.state = 150
                self.expression()
                self.state = 151
                self.expression()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.match(OnionParser.T__13)
                self.state = 154
                self.expression()
                self.state = 155
                self.expression()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
                self.match(OnionParser.T__14)
                self.state = 158
                self.expression()
                self.state = 159
                self.expression()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.match(OnionParser.T__15)
                self.state = 162
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
            self.state = 165
            self.match(OnionParser.T__16)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 166
                self.expression()
                self.state = 171
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
            self.state = 172
            self.match(OnionParser.T__17)
            self.state = 173
            self.expression()
            self.state = 174
            self.statement()
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.match(OnionParser.T__0)
                    self.state = 176
                    self.match(OnionParser.T__18)
                    self.state = 177
                    self.expression()
                    self.state = 178
                    self.statement()
                    self.state = 179
                    self.match(OnionParser.T__1) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 186
                self.match(OnionParser.T__0)
                self.state = 187
                self.match(OnionParser.T__19)
                self.state = 188
                self.statement()
                self.state = 189
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
            self.state = 193
            self.match(OnionParser.T__20)
            self.state = 199 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 194
                    self.match(OnionParser.T__0)
                    self.state = 195
                    self.expression()
                    self.state = 196
                    self.statement()
                    self.state = 197
                    self.match(OnionParser.T__1)

                else:
                    raise NoViableAltException(self)
                self.state = 201 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 203
                self.match(OnionParser.T__0)
                self.state = 204
                self.match(OnionParser.T__21)
                self.state = 205
                self.statement()
                self.state = 206
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
            self.state = 210
            self.match(OnionParser.T__22)
            self.state = 211
            self.match(OnionParser.IDENTIFIER)
            self.state = 212
            self.match(OnionParser.T__0)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 213
                self.match(OnionParser.IDENTIFIER)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(OnionParser.T__1)
            self.state = 220
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
            self.state = 222
            self.match(OnionParser.T__23)
            self.state = 223
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
            self.state = 225
            self.match(OnionParser.IDENTIFIER)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 226
                self.expression()
                self.state = 231
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
            self.state = 232
            self.match(OnionParser.T__24)
            self.state = 233
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
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(OnionParser.T__25)
                self.state = 236
                self.expression()
                self.state = 237
                self.block()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(OnionParser.T__26)
                self.state = 240
                self.match(OnionParser.IDENTIFIER)
                self.state = 241
                self.match(OnionParser.T__27)
                self.state = 242
                self.match(OnionParser.T__0)
                self.state = 243
                self.expression()
                self.state = 244
                self.expression()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                    self.state = 245
                    self.expression()


                self.state = 248
                self.match(OnionParser.T__1)
                self.state = 249
                self.block()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.match(OnionParser.T__28)
                self.state = 252
                self.expression()
                self.state = 253
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
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(OnionParser.T__29)
                self.state = 258
                self.expression()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(OnionParser.T__30)
                self.state = 260
                self.expression()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.match(OnionParser.T__31)
                self.state = 262
                self.expression()
                self.state = 263
                self.expression()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.match(OnionParser.T__32)
                self.state = 266
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
            self.state = 269
            self.match(OnionParser.T__33)
            self.state = 270
            self.match(OnionParser.IDENTIFIER)
            self.state = 271
            self.match(OnionParser.T__0)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 272
                self.match(OnionParser.IDENTIFIER)
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 278
            self.match(OnionParser.T__1)
            self.state = 279
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
            self.state = 281
            self.match(OnionParser.IDENTIFIER)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778818) != 0):
                self.state = 282
                self.expression()
                self.state = 287
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
            self.state = 288
            self.match(OnionParser.T__34)
            self.state = 289
            self.match(OnionParser.IDENTIFIER)
            self.state = 290
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
            self.state = 292
            self.match(OnionParser.T__0)
            self.state = 294 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 293
                self.methodDef()
                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

            self.state = 298
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
            self.state = 300
            self.match(OnionParser.T__22)
            self.state = 301
            self.match(OnionParser.IDENTIFIER)
            self.state = 302
            self.match(OnionParser.T__0)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 303
                self.match(OnionParser.IDENTIFIER)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 309
            self.match(OnionParser.T__1)
            self.state = 310
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
            self.state = 313 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 312
                self.statement()
                self.state = 315 
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
            self.state = 317
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





