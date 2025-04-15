# Generated from grammar/Onion.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OnionParser import OnionParser
else:
    from OnionParser import OnionParser

# This class defines a complete generic visitor for a parse tree produced by OnionParser.

class OnionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OnionParser#program.
    def visitProgram(self, ctx:OnionParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#statement.
    def visitStatement(self, ctx:OnionParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#incDecStmt.
    def visitIncDecStmt(self, ctx:OnionParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#assignment.
    def visitAssignment(self, ctx:OnionParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#expression.
    def visitExpression(self, ctx:OnionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#arithmeticExpr.
    def visitArithmeticExpr(self, ctx:OnionParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#booleanExpr.
    def visitBooleanExpr(self, ctx:OnionParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#listExpr.
    def visitListExpr(self, ctx:OnionParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#ifExpr.
    def visitIfExpr(self, ctx:OnionParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#branchExpr.
    def visitBranchExpr(self, ctx:OnionParser.BranchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#functionDef.
    def visitFunctionDef(self, ctx:OnionParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#returnStmt.
    def visitReturnStmt(self, ctx:OnionParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#functionCall.
    def visitFunctionCall(self, ctx:OnionParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#printStatement.
    def visitPrintStatement(self, ctx:OnionParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#loopStatement.
    def visitLoopStatement(self, ctx:OnionParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#macroDef.
    def visitMacroDef(self, ctx:OnionParser.MacroDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#macroCall.
    def visitMacroCall(self, ctx:OnionParser.MacroCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#classDef.
    def visitClassDef(self, ctx:OnionParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#classBody.
    def visitClassBody(self, ctx:OnionParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#methodDef.
    def visitMethodDef(self, ctx:OnionParser.MethodDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#block.
    def visitBlock(self, ctx:OnionParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OnionParser#literal.
    def visitLiteral(self, ctx:OnionParser.LiteralContext):
        return self.visitChildren(ctx)



del OnionParser