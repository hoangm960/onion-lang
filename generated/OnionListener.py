# Generated from grammar/Onion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OnionParser import OnionParser
else:
    from OnionParser import OnionParser

# This class defines a complete listener for a parse tree produced by OnionParser.
class OnionListener(ParseTreeListener):

    # Enter a parse tree produced by OnionParser#program.
    def enterProgram(self, ctx:OnionParser.ProgramContext):
        pass

    # Exit a parse tree produced by OnionParser#program.
    def exitProgram(self, ctx:OnionParser.ProgramContext):
        pass


    # Enter a parse tree produced by OnionParser#statement.
    def enterStatement(self, ctx:OnionParser.StatementContext):
        pass

    # Exit a parse tree produced by OnionParser#statement.
    def exitStatement(self, ctx:OnionParser.StatementContext):
        pass


    # Enter a parse tree produced by OnionParser#statementType.
    def enterStatementType(self, ctx:OnionParser.StatementTypeContext):
        pass

    # Exit a parse tree produced by OnionParser#statementType.
    def exitStatementType(self, ctx:OnionParser.StatementTypeContext):
        pass


    # Enter a parse tree produced by OnionParser#incDecStmt.
    def enterIncDecStmt(self, ctx:OnionParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by OnionParser#incDecStmt.
    def exitIncDecStmt(self, ctx:OnionParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by OnionParser#assignment.
    def enterAssignment(self, ctx:OnionParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OnionParser#assignment.
    def exitAssignment(self, ctx:OnionParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OnionParser#expression.
    def enterExpression(self, ctx:OnionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OnionParser#expression.
    def exitExpression(self, ctx:OnionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OnionParser#compoundExpr.
    def enterCompoundExpr(self, ctx:OnionParser.CompoundExprContext):
        pass

    # Exit a parse tree produced by OnionParser#compoundExpr.
    def exitCompoundExpr(self, ctx:OnionParser.CompoundExprContext):
        pass


    # Enter a parse tree produced by OnionParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:OnionParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by OnionParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:OnionParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by OnionParser#booleanExpr.
    def enterBooleanExpr(self, ctx:OnionParser.BooleanExprContext):
        pass

    # Exit a parse tree produced by OnionParser#booleanExpr.
    def exitBooleanExpr(self, ctx:OnionParser.BooleanExprContext):
        pass


    # Enter a parse tree produced by OnionParser#listExpr.
    def enterListExpr(self, ctx:OnionParser.ListExprContext):
        pass

    # Exit a parse tree produced by OnionParser#listExpr.
    def exitListExpr(self, ctx:OnionParser.ListExprContext):
        pass


    # Enter a parse tree produced by OnionParser#ifExpr.
    def enterIfExpr(self, ctx:OnionParser.IfExprContext):
        pass

    # Exit a parse tree produced by OnionParser#ifExpr.
    def exitIfExpr(self, ctx:OnionParser.IfExprContext):
        pass


    # Enter a parse tree produced by OnionParser#branchExpr.
    def enterBranchExpr(self, ctx:OnionParser.BranchExprContext):
        pass

    # Exit a parse tree produced by OnionParser#branchExpr.
    def exitBranchExpr(self, ctx:OnionParser.BranchExprContext):
        pass


    # Enter a parse tree produced by OnionParser#functionDef.
    def enterFunctionDef(self, ctx:OnionParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by OnionParser#functionDef.
    def exitFunctionDef(self, ctx:OnionParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by OnionParser#returnStmt.
    def enterReturnStmt(self, ctx:OnionParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by OnionParser#returnStmt.
    def exitReturnStmt(self, ctx:OnionParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by OnionParser#functionCall.
    def enterFunctionCall(self, ctx:OnionParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by OnionParser#functionCall.
    def exitFunctionCall(self, ctx:OnionParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by OnionParser#printStatement.
    def enterPrintStatement(self, ctx:OnionParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by OnionParser#printStatement.
    def exitPrintStatement(self, ctx:OnionParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by OnionParser#loopStatement.
    def enterLoopStatement(self, ctx:OnionParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by OnionParser#loopStatement.
    def exitLoopStatement(self, ctx:OnionParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by OnionParser#listOpExpr.
    def enterListOpExpr(self, ctx:OnionParser.ListOpExprContext):
        pass

    # Exit a parse tree produced by OnionParser#listOpExpr.
    def exitListOpExpr(self, ctx:OnionParser.ListOpExprContext):
        pass


    # Enter a parse tree produced by OnionParser#macroDef.
    def enterMacroDef(self, ctx:OnionParser.MacroDefContext):
        pass

    # Exit a parse tree produced by OnionParser#macroDef.
    def exitMacroDef(self, ctx:OnionParser.MacroDefContext):
        pass


    # Enter a parse tree produced by OnionParser#macroCall.
    def enterMacroCall(self, ctx:OnionParser.MacroCallContext):
        pass

    # Exit a parse tree produced by OnionParser#macroCall.
    def exitMacroCall(self, ctx:OnionParser.MacroCallContext):
        pass


    # Enter a parse tree produced by OnionParser#classDef.
    def enterClassDef(self, ctx:OnionParser.ClassDefContext):
        pass

    # Exit a parse tree produced by OnionParser#classDef.
    def exitClassDef(self, ctx:OnionParser.ClassDefContext):
        pass


    # Enter a parse tree produced by OnionParser#classBody.
    def enterClassBody(self, ctx:OnionParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by OnionParser#classBody.
    def exitClassBody(self, ctx:OnionParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by OnionParser#methodDef.
    def enterMethodDef(self, ctx:OnionParser.MethodDefContext):
        pass

    # Exit a parse tree produced by OnionParser#methodDef.
    def exitMethodDef(self, ctx:OnionParser.MethodDefContext):
        pass


    # Enter a parse tree produced by OnionParser#block.
    def enterBlock(self, ctx:OnionParser.BlockContext):
        pass

    # Exit a parse tree produced by OnionParser#block.
    def exitBlock(self, ctx:OnionParser.BlockContext):
        pass


    # Enter a parse tree produced by OnionParser#literal.
    def enterLiteral(self, ctx:OnionParser.LiteralContext):
        pass

    # Exit a parse tree produced by OnionParser#literal.
    def exitLiteral(self, ctx:OnionParser.LiteralContext):
        pass



del OnionParser