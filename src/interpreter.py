from generated.OnionVisitor import OnionVisitor
from generated.OnionParser import OnionParser

class Interpreter(OnionVisitor):
    def visitProgram(self, ctx: OnionParser.ProgramContext):
        result = None
        for stmt in ctx.statement():
            result = self.visit(stmt)
        return result

    def visitExpression(self, ctx: OnionParser.ExpressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.arithmeticExpr():
            return self.visit(ctx.arithmeticExpr())
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.env:
                return self.env[var_name]
            else:
                raise NameError(f"Variable '{var_name}' is not defined")
        return None
