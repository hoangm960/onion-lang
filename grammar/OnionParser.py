# Generated from .//grammar//Onion.g4 by ANTLR 4.13.2
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
        4,1,32,271,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,63,8,2,11,2,12,2,64,1,2,1,2,3,2,69,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,105,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,
        5,148,8,5,1,6,1,6,1,6,1,6,1,6,5,6,155,8,6,10,6,12,6,158,9,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,170,8,7,1,7,1,7,1,8,1,8,
        1,8,1,8,5,8,178,8,8,10,8,12,8,181,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,5,11,207,8,11,10,11,12,11,210,9,11,3,11,212,
        8,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,222,8,12,10,12,
        12,12,225,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        4,14,237,8,14,11,14,12,14,238,1,14,1,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,250,8,15,10,15,12,15,253,9,15,3,15,255,8,15,1,15,
        1,15,1,15,1,15,1,16,1,16,4,16,263,8,16,11,16,12,16,264,1,16,1,16,
        1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,0,1,1,0,27,29,286,0,37,1,0,0,0,2,47,1,0,0,0,4,68,1,0,0,0,6,
        78,1,0,0,0,8,104,1,0,0,0,10,147,1,0,0,0,12,149,1,0,0,0,14,162,1,
        0,0,0,16,173,1,0,0,0,18,184,1,0,0,0,20,189,1,0,0,0,22,199,1,0,0,
        0,24,217,1,0,0,0,26,228,1,0,0,0,28,234,1,0,0,0,30,242,1,0,0,0,32,
        260,1,0,0,0,34,268,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,
        0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,0,41,48,3,4,2,0,42,48,
        3,6,3,0,43,48,3,18,9,0,44,48,3,22,11,0,45,48,3,26,13,0,46,48,3,20,
        10,0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,
        45,1,0,0,0,47,46,1,0,0,0,48,3,1,0,0,0,49,50,5,1,0,0,50,51,5,2,0,
        0,51,52,5,26,0,0,52,53,3,6,3,0,53,54,5,3,0,0,54,69,1,0,0,0,55,56,
        5,1,0,0,56,62,5,2,0,0,57,58,5,1,0,0,58,59,5,26,0,0,59,60,3,6,3,0,
        60,61,5,3,0,0,61,63,1,0,0,0,62,57,1,0,0,0,63,64,1,0,0,0,64,62,1,
        0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,3,0,0,67,69,1,0,0,0,68,
        49,1,0,0,0,68,55,1,0,0,0,69,5,1,0,0,0,70,79,3,34,17,0,71,79,5,26,
        0,0,72,79,3,8,4,0,73,79,3,10,5,0,74,79,3,12,6,0,75,79,3,16,8,0,76,
        79,3,14,7,0,77,79,3,24,12,0,78,70,1,0,0,0,78,71,1,0,0,0,78,72,1,
        0,0,0,78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,
        77,1,0,0,0,79,7,1,0,0,0,80,81,5,1,0,0,81,82,5,4,0,0,82,83,3,6,3,
        0,83,84,3,6,3,0,84,85,5,3,0,0,85,105,1,0,0,0,86,87,5,1,0,0,87,88,
        5,5,0,0,88,89,3,6,3,0,89,90,3,6,3,0,90,91,5,3,0,0,91,105,1,0,0,0,
        92,93,5,1,0,0,93,94,5,6,0,0,94,95,3,6,3,0,95,96,3,6,3,0,96,97,5,
        3,0,0,97,105,1,0,0,0,98,99,5,1,0,0,99,100,5,7,0,0,100,101,3,6,3,
        0,101,102,3,6,3,0,102,103,5,3,0,0,103,105,1,0,0,0,104,80,1,0,0,0,
        104,86,1,0,0,0,104,92,1,0,0,0,104,98,1,0,0,0,105,9,1,0,0,0,106,107,
        5,1,0,0,107,108,5,8,0,0,108,109,3,6,3,0,109,110,3,6,3,0,110,111,
        5,3,0,0,111,148,1,0,0,0,112,113,5,1,0,0,113,114,5,9,0,0,114,115,
        3,6,3,0,115,116,3,6,3,0,116,117,5,3,0,0,117,148,1,0,0,0,118,119,
        5,1,0,0,119,120,5,10,0,0,120,121,3,6,3,0,121,122,3,6,3,0,122,123,
        5,3,0,0,123,148,1,0,0,0,124,125,5,1,0,0,125,126,5,11,0,0,126,127,
        3,6,3,0,127,128,3,6,3,0,128,129,5,3,0,0,129,148,1,0,0,0,130,131,
        5,1,0,0,131,132,5,12,0,0,132,133,3,6,3,0,133,134,3,6,3,0,134,135,
        5,3,0,0,135,148,1,0,0,0,136,137,5,1,0,0,137,138,5,13,0,0,138,139,
        3,6,3,0,139,140,3,6,3,0,140,141,5,3,0,0,141,148,1,0,0,0,142,143,
        5,1,0,0,143,144,5,14,0,0,144,145,3,6,3,0,145,146,5,3,0,0,146,148,
        1,0,0,0,147,106,1,0,0,0,147,112,1,0,0,0,147,118,1,0,0,0,147,124,
        1,0,0,0,147,130,1,0,0,0,147,136,1,0,0,0,147,142,1,0,0,0,148,11,1,
        0,0,0,149,150,5,1,0,0,150,151,5,15,0,0,151,156,3,6,3,0,152,153,5,
        16,0,0,153,155,3,6,3,0,154,152,1,0,0,0,155,158,1,0,0,0,156,154,1,
        0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,160,5,
        17,0,0,160,161,5,3,0,0,161,13,1,0,0,0,162,163,5,1,0,0,163,164,5,
        18,0,0,164,165,3,6,3,0,165,166,5,19,0,0,166,169,3,2,1,0,167,168,
        5,20,0,0,168,170,3,2,1,0,169,167,1,0,0,0,169,170,1,0,0,0,170,171,
        1,0,0,0,171,172,5,3,0,0,172,15,1,0,0,0,173,174,5,1,0,0,174,175,5,
        26,0,0,175,179,3,6,3,0,176,178,3,6,3,0,177,176,1,0,0,0,178,181,1,
        0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,179,1,
        0,0,0,182,183,5,3,0,0,183,17,1,0,0,0,184,185,5,1,0,0,185,186,5,21,
        0,0,186,187,3,6,3,0,187,188,5,3,0,0,188,19,1,0,0,0,189,190,5,1,0,
        0,190,191,5,22,0,0,191,192,5,1,0,0,192,193,5,26,0,0,193,194,3,6,
        3,0,194,195,3,6,3,0,195,196,5,3,0,0,196,197,3,2,1,0,197,198,5,3,
        0,0,198,21,1,0,0,0,199,200,5,1,0,0,200,201,5,23,0,0,201,202,5,26,
        0,0,202,211,5,1,0,0,203,208,5,26,0,0,204,205,5,16,0,0,205,207,5,
        26,0,0,206,204,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,
        0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,211,203,1,0,0,0,211,212,1,
        0,0,0,212,213,1,0,0,0,213,214,5,3,0,0,214,215,3,32,16,0,215,216,
        5,3,0,0,216,23,1,0,0,0,217,218,5,1,0,0,218,219,5,26,0,0,219,223,
        3,6,3,0,220,222,3,6,3,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,
        1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,223,1,0,0,0,226,227,
        5,3,0,0,227,25,1,0,0,0,228,229,5,1,0,0,229,230,5,24,0,0,230,231,
        5,26,0,0,231,232,3,28,14,0,232,233,5,3,0,0,233,27,1,0,0,0,234,236,
        5,1,0,0,235,237,3,30,15,0,236,235,1,0,0,0,237,238,1,0,0,0,238,236,
        1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,3,0,0,241,29,1,
        0,0,0,242,243,5,1,0,0,243,244,5,25,0,0,244,245,5,26,0,0,245,254,
        5,1,0,0,246,251,5,26,0,0,247,248,5,16,0,0,248,250,5,26,0,0,249,247,
        1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,255,
        1,0,0,0,253,251,1,0,0,0,254,246,1,0,0,0,254,255,1,0,0,0,255,256,
        1,0,0,0,256,257,5,3,0,0,257,258,3,32,16,0,258,259,5,3,0,0,259,31,
        1,0,0,0,260,262,5,1,0,0,261,263,3,2,1,0,262,261,1,0,0,0,263,264,
        1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,266,1,0,0,0,266,267,
        5,3,0,0,267,33,1,0,0,0,268,269,7,0,0,0,269,35,1,0,0,0,17,39,47,64,
        68,78,104,147,156,169,179,208,211,223,238,251,254,264
    ]

class OnionParser ( Parser ):

    grammarFileName = "Onion.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "'let'", "')'", "'+'", "'-'", "'*'", 
                     "'/'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'not'", "'['", "','", "']'", "'if'", "'then'", "'else'", 
                     "'print'", "'for'", "'macro'", "'class'", "'def'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "INT", "BOOL", 
                      "STRING", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_arithmeticExpr = 4
    RULE_booleanExpr = 5
    RULE_arrayExpr = 6
    RULE_ifExpr = 7
    RULE_functionCall = 8
    RULE_printStatement = 9
    RULE_loopStatement = 10
    RULE_macroDef = 11
    RULE_macroCall = 12
    RULE_classDef = 13
    RULE_classBody = 14
    RULE_methodDef = 15
    RULE_block = 16
    RULE_literal = 17

    ruleNames =  [ "program", "statement", "assignment", "expression", "arithmeticExpr", 
                   "booleanExpr", "arrayExpr", "ifExpr", "functionCall", 
                   "printStatement", "loopStatement", "macroDef", "macroCall", 
                   "classDef", "classBody", "methodDef", "block", "literal" ]

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
    IDENTIFIER=26
    INT=27
    BOOL=28
    STRING=29
    WS=30
    COMMENT=31
    LINE_COMMENT=32

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632962) != 0)):
                    break

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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.printStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.macroDef()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.classDef()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.loopStatement()
                pass


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
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(OnionParser.T__0)
                self.state = 50
                self.match(OnionParser.T__1)
                self.state = 51
                self.match(OnionParser.IDENTIFIER)
                self.state = 52
                self.expression()
                self.state = 53
                self.match(OnionParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(OnionParser.T__0)
                self.state = 56
                self.match(OnionParser.T__1)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    self.match(OnionParser.T__0)
                    self.state = 58
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 59
                    self.expression()
                    self.state = 60
                    self.match(OnionParser.T__2)
                    self.state = 64 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 66
                self.match(OnionParser.T__2)
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

        def arithmeticExpr(self):
            return self.getTypedRuleContext(OnionParser.ArithmeticExprContext,0)


        def booleanExpr(self):
            return self.getTypedRuleContext(OnionParser.BooleanExprContext,0)


        def arrayExpr(self):
            return self.getTypedRuleContext(OnionParser.ArrayExprContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(OnionParser.FunctionCallContext,0)


        def ifExpr(self):
            return self.getTypedRuleContext(OnionParser.IfExprContext,0)


        def macroCall(self):
            return self.getTypedRuleContext(OnionParser.MacroCallContext,0)


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
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(OnionParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.arithmeticExpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.booleanExpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.arrayExpr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.functionCall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.ifExpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 77
                self.macroCall()
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
        self.enterRule(localctx, 8, self.RULE_arithmeticExpr)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(OnionParser.T__0)
                self.state = 81
                self.match(OnionParser.T__3)
                self.state = 82
                self.expression()
                self.state = 83
                self.expression()
                self.state = 84
                self.match(OnionParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(OnionParser.T__0)
                self.state = 87
                self.match(OnionParser.T__4)
                self.state = 88
                self.expression()
                self.state = 89
                self.expression()
                self.state = 90
                self.match(OnionParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(OnionParser.T__0)
                self.state = 93
                self.match(OnionParser.T__5)
                self.state = 94
                self.expression()
                self.state = 95
                self.expression()
                self.state = 96
                self.match(OnionParser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(OnionParser.T__0)
                self.state = 99
                self.match(OnionParser.T__6)
                self.state = 100
                self.expression()
                self.state = 101
                self.expression()
                self.state = 102
                self.match(OnionParser.T__2)
                pass


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
        self.enterRule(localctx, 10, self.RULE_booleanExpr)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(OnionParser.T__0)
                self.state = 107
                self.match(OnionParser.T__7)
                self.state = 108
                self.expression()
                self.state = 109
                self.expression()
                self.state = 110
                self.match(OnionParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(OnionParser.T__0)
                self.state = 113
                self.match(OnionParser.T__8)
                self.state = 114
                self.expression()
                self.state = 115
                self.expression()
                self.state = 116
                self.match(OnionParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(OnionParser.T__0)
                self.state = 119
                self.match(OnionParser.T__9)
                self.state = 120
                self.expression()
                self.state = 121
                self.expression()
                self.state = 122
                self.match(OnionParser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.match(OnionParser.T__0)
                self.state = 125
                self.match(OnionParser.T__10)
                self.state = 126
                self.expression()
                self.state = 127
                self.expression()
                self.state = 128
                self.match(OnionParser.T__2)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.match(OnionParser.T__0)
                self.state = 131
                self.match(OnionParser.T__11)
                self.state = 132
                self.expression()
                self.state = 133
                self.expression()
                self.state = 134
                self.match(OnionParser.T__2)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.match(OnionParser.T__0)
                self.state = 137
                self.match(OnionParser.T__12)
                self.state = 138
                self.expression()
                self.state = 139
                self.expression()
                self.state = 140
                self.match(OnionParser.T__2)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.match(OnionParser.T__0)
                self.state = 143
                self.match(OnionParser.T__13)
                self.state = 144
                self.expression()
                self.state = 145
                self.match(OnionParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayExprContext(ParserRuleContext):
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
            return OnionParser.RULE_arrayExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)




    def arrayExpr(self):

        localctx = OnionParser.ArrayExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(OnionParser.T__0)
            self.state = 150
            self.match(OnionParser.T__14)
            self.state = 151
            self.expression()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 152
                self.match(OnionParser.T__15)
                self.state = 153
                self.expression()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(OnionParser.T__16)
            self.state = 160
            self.match(OnionParser.T__2)
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

        def expression(self):
            return self.getTypedRuleContext(OnionParser.ExpressionContext,0)


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
        self.enterRule(localctx, 14, self.RULE_ifExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(OnionParser.T__0)
            self.state = 163
            self.match(OnionParser.T__17)
            self.state = 164
            self.expression()
            self.state = 165
            self.match(OnionParser.T__18)
            self.state = 166
            self.statement()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 167
                self.match(OnionParser.T__19)
                self.state = 168
                self.statement()


            self.state = 171
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(OnionParser.T__0)
            self.state = 174
            self.match(OnionParser.IDENTIFIER)
            self.state = 175
            self.expression()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632962) != 0):
                self.state = 176
                self.expression()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(OnionParser.T__0)
            self.state = 185
            self.match(OnionParser.T__20)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(OnionParser.T__2)
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

        def IDENTIFIER(self):
            return self.getToken(OnionParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OnionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(OnionParser.ExpressionContext,i)


        def statement(self):
            return self.getTypedRuleContext(OnionParser.StatementContext,0)


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
        self.enterRule(localctx, 20, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(OnionParser.T__0)
            self.state = 190
            self.match(OnionParser.T__21)
            self.state = 191
            self.match(OnionParser.T__0)
            self.state = 192
            self.match(OnionParser.IDENTIFIER)
            self.state = 193
            self.expression()
            self.state = 194
            self.expression()
            self.state = 195
            self.match(OnionParser.T__2)
            self.state = 196
            self.statement()
            self.state = 197
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 22, self.RULE_macroDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(OnionParser.T__0)
            self.state = 200
            self.match(OnionParser.T__22)
            self.state = 201
            self.match(OnionParser.IDENTIFIER)
            self.state = 202
            self.match(OnionParser.T__0)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 203
                self.match(OnionParser.IDENTIFIER)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 204
                    self.match(OnionParser.T__15)
                    self.state = 205
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 213
            self.match(OnionParser.T__2)
            self.state = 214
            self.block()
            self.state = 215
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 24, self.RULE_macroCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(OnionParser.T__0)
            self.state = 218
            self.match(OnionParser.IDENTIFIER)
            self.state = 219
            self.expression()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632962) != 0):
                self.state = 220
                self.expression()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 26, self.RULE_classDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(OnionParser.T__0)
            self.state = 229
            self.match(OnionParser.T__23)
            self.state = 230
            self.match(OnionParser.IDENTIFIER)
            self.state = 231
            self.classBody()
            self.state = 232
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 28, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(OnionParser.T__0)
            self.state = 236 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 235
                self.methodDef()
                self.state = 238 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 240
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 30, self.RULE_methodDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(OnionParser.T__0)
            self.state = 243
            self.match(OnionParser.T__24)
            self.state = 244
            self.match(OnionParser.IDENTIFIER)
            self.state = 245
            self.match(OnionParser.T__0)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 246
                self.match(OnionParser.IDENTIFIER)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==16:
                    self.state = 247
                    self.match(OnionParser.T__15)
                    self.state = 248
                    self.match(OnionParser.IDENTIFIER)
                    self.state = 253
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 256
            self.match(OnionParser.T__2)
            self.state = 257
            self.block()
            self.state = 258
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 32, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(OnionParser.T__0)
            self.state = 262 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 261
                self.statement()
                self.state = 264 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632962) != 0)):
                    break

            self.state = 266
            self.match(OnionParser.T__2)
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
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
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





