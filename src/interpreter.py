from generated.OnionVisitor import OnionVisitor
from generated.OnionParser import OnionParser

class Interpreter(OnionVisitor):
    def __init__(self):
        self.env = {}

    def visitProgram(self, ctx: OnionParser.ProgramContext):
        result = None
        for stmt in ctx.statement():
            result = self.visit(stmt)
        return result

    def visitPrintStatement(self, ctx: OnionParser.PrintStatementContext):
        value = self.visit(ctx.expression())
        print(value)
        return value

    def visitAssignment(self, ctx: OnionParser.AssignmentContext):
        identifier = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.env[identifier] = value
        return value

    def visitArithmeticExpr(self, ctx: OnionParser.ArithmeticExprContext):
        op = ctx.getChild(1).getText()
        if op == '+':
            # Addition: Sum all child expressions.
            result = 0
            for expr_ctx in ctx.expression():
                result += self.visit(expr_ctx)
            return result
        elif op == '-':
            # Subtraction: subtract subsequent expressions from the first.
            result = self.visit(ctx.expression(0))
            for expr_ctx in ctx.expression()[1:]:
                result -= self.visit(expr_ctx)
            return result
        elif op == '*':
            result = 1
            for expr_ctx in ctx.expression():
                result *= self.visit(expr_ctx)
            return result
        elif op == '/':
            result = self.visit(ctx.expression(0))
            for expr_ctx in ctx.expression()[1:]:
                divisor = self.visit(expr_ctx)
                if divisor == 0:
                    raise ZeroDivisionError("Division by zero")
                result /= divisor
            return result
        else:
            return None

    def visitLiteral(self, ctx: OnionParser.LiteralContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]
        elif ctx.BOOL():
            token = ctx.BOOL().getText()
            return token == 'true'
        return None

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
