from generated.OnionVisitor import OnionVisitor
from generated.OnionParser import OnionParser
import sys
import os
from src.symbol_table import SymbolTable
from src.exceptions import (
    OnionRuntimeError,
    OnionNameError,
    OnionArgumentError,
    OnionTypeError,
)
from src.builtins import BuiltInFunctions

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ReturnValue:
    """Lớp bọc giá trị trả về bởi lệnh return."""

    def __init__(self, value):
        self.value = value


class BaseInterpreter(OnionVisitor):
    def __init__(self):
        self.env = SymbolTable()
        self.functions = {}  # Lưu trữ các định nghĩa hàm
        self.macros = {}  # Lưu trữ các định nghĩa hàm

    def visitProgram(self, ctx):
        result = None
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if isinstance(result, ReturnValue):
                break

        return result

    def visitStatement(self, ctx):
        # Xử lý câu lệnh trong ngoặc đơn: '(' statementType ')'
        if ctx.getChildCount() >= 3 and ctx.statementType() is not None:
            # Gọi visit cho statementType
            result = self.visit(ctx.statementType())
            # Trả về kết quả mà không cần xử lý thêm
            return result
        # Trường hợp không có statementType, truy cập trực tiếp các nút con
        for i in range(ctx.getChildCount()):
            if i != 0 and i != ctx.getChildCount() - 1:  # Bỏ qua dấu ngoặc đơn
                child = ctx.getChild(i)
                if child is not None:
                    return self.visit(child)
        return None

    def visitStatementType(self, ctx):
        # Truy cập loại câu lệnh cụ thể (assignment, expression, v.v.)
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child is not None:
                result = self.visit(child)
                if result is not None:
                    return result
        return None

    def visitPrintStatement(self, ctx):
        try:
            value = self.visit(ctx.expression())
            print(value)
            return None
        except Exception as e:
            # Xử lý các lỗi khác
            print(f"Print error: {e}")
            return None

    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:  # 'let' IDENTIFIER expression
            # Dạng đơn giản: let a 2
            identifier = ctx.getChild(1).getText()
            value = self.visit(ctx.getChild(2))
            # print(f"Debug: {value}")
            self.env.define(identifier, value)
            return value
        else:
            # Dạng nhiều biến: let (a 1) (b 2)
            result = None
            # Bắt đầu từ vị trí 1 (sau 'let')
            i = 1
            while i < ctx.getChildCount():
                if ctx.getChild(i).getText() == "(":
                    # Mỗi cặp biến-giá trị có dạng '(' IDENTIFIER expression ')'
                    pair = ctx.getChild(i)
                    if pair.getChildCount() == 4:  # '(', IDENTIFIER, expression, ')'
                        var_name = pair.getChild(1).getText()
                        var_value = self.visit(pair.getChild(2))
                        self.env.define(var_name, var_value)
                        result = var_value
                i += 1
            return result

    def visitChildren(self, ctx):
        # Phương thức này đảm bảo mọi nút con đều được ghé thăm, hữu ích cho các quy tắc chưa có phương thức visit cụ thể
        result = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child:
                child_result = self.visit(child)
                if child_result is not None:
                    result = child_result
        return result

    def visitBlock(self, ctx):
        """Xử lý block các câu lệnh"""
        result = None

        # Duyệt qua tất cả các statement trong block
        for i in range(ctx.getChildCount()):
            stmt = ctx.getChild(i)
            result = self.visit(stmt)

            # Kiểm tra nếu kết quả là ReturnValue
            if isinstance(result, ReturnValue):
                # Gặp lệnh return, dừng việc xử lý block và trả về đối tượng ReturnValue
                return result

        return result

    def visitIncDecStmt(self, ctx):
        """Xử lý tăng/giảm biến"""
        op = ctx.getChild(0).getText()
        var_name = ctx.IDENTIFIER().getText()

        # Lấy giá trị hiện tại
        current_value = self.env.resolve(var_name)

        if not isinstance(current_value, (int, float)):
            raise TypeError(
                f"Cannot increment/decrement non-numeric value: {current_value}"
            )

        if op == "inc":
            # Tăng biến lên 1: (inc x)
            new_value = current_value + 1
        elif op == "dec":
            # Giảm biến đi 1: (dec x)
            new_value = current_value - 1

        # Cập nhật giá trị mới
        if not self.env.assign(var_name, new_value):
            raise NameError(f"Variable '{var_name}' is not defined")

        return new_value

    def visitReturnStmt(self, ctx):
        """Xử lý lệnh return trong hàm"""
        # Lấy trực tiếp biểu thức sau từ khóa 'return'
        if ctx.getChildCount() > 1:
            expr = ctx.getChild(1)  # Phần tử thứ 2 (index 1) sau 'return'

            value = self.visit(expr)

            # Đánh dấu đây là giá trị return
            return_value = ReturnValue(value)
            return return_value

        # Nếu không có biểu thức, trả về None
        return ReturnValue(None)

    def _execute_block(self, body):
        result = None
        for i in range(body.getChildCount()):
            stmt_result = self.visit(body.getChild(i))
            if isinstance(stmt_result, ReturnValue):
                result = stmt_result.value
                break
            elif stmt_result is not None:
                result = stmt_result
        return result

class ExpressionVisitor(BaseInterpreter):
    def _resolve_identifier(self, ctx):
        """Resolve variable identifier with error handling"""
        var_name = ctx.IDENTIFIER().getText()
        try:
            return self.env.resolve(var_name)
        except NameError as e:
            if var_name in BuiltInFunctions.registry:
                return BuiltInFunctions.execute(var_name, self, [])
            raise OnionNameError(f"Undefined variable '{var_name}'") from e

    def visitExpression(self, ctx):
        if ctx.literal():
            result = self.visit(ctx.literal())
            return result
        elif ctx.IDENTIFIER():
            return self._resolve_identifier(ctx)
        elif ctx.compoundExpr():
            return self.visit(ctx.compoundExpr())
        return None

    def visitCompoundExpr(self, ctx):
        if ctx.arithmeticExpr():
            return self.visit(ctx.arithmeticExpr())
        if ctx.booleanExpr():
            return self.visit(ctx.booleanExpr())
        if ctx.listExpr():
            return self.visit(ctx.listExpr())
        if ctx.callExpr():
            return self.visit(ctx.callExpr())
        if ctx.ifExpr():
            return self.visit(ctx.ifExpr())
        if ctx.branchExpr():
            return self.visit(ctx.branchExpr())
        if ctx.listOpExpr():
            return self.visit(ctx.listOpExpr())
        return None

    def visitLiteral(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        if ctx.STRING():
            text = ctx.STRING().getText()
            return text[1:-1]
        if ctx.BOOL():
            token = ctx.BOOL().getText()
            return token == "true"
        return None


class ArithmeticVisitor(ExpressionVisitor):
    def visitArithmeticExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "+": self._handle_addition,
            "-": self._handle_subtraction,
            "*": self._handle_multiplication,
            "/": self._handle_division,
            "//": self._handle_integer_division,
        }
        return handlers[op](ctx)

    def _handle_addition(self, ctx):
        # Addition and string concatenation
        result = self.visit(ctx.getChild(1))
        for i in range(2, ctx.getChildCount()):
            value = self.visit(ctx.getChild(i))
            # If string then concat
            if isinstance(result, str) and isinstance(value, str):
                result = result + value
            # Else if number then add (can be int or float)
            elif isinstance(result, (int, float)) and isinstance(value, (int, float)):
                result = result + value
            else:
                raise TypeError(
                    f"Cannot add values of type {type(result)} and {type(value)}"
                )
        return result

    def _handle_subtraction(self, ctx):
        # Subtraction: only 2 operands
        if ctx.getChildCount() != 3:
            raise SyntaxError("Subtraction requires exactly 2 operands")
        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        if left is None or right is None:
            raise ValueError("Cannot evaluate subtraction operands")
        return left - right

    def _handle_multiplication(self, ctx):
        # Multiplication: multiply all child expressions
        result = 1
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            value = self.visit(child)
            if value is None:
                raise ValueError(f"Cannot evaluate expression at position {i}")
            result *= value
        return result

    def _handle_division(self, ctx):
        # Division: only 2 operands
        if ctx.getChildCount() != 3:
            raise SyntaxError("Division requires exactly 2 operands")
        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        if left is None or right is None:
            raise ValueError("Cannot evaluate division operands")
        if right == 0:
            raise ZeroDivisionError("Division by zero")
        return left / right

    def _handle_integer_division(self, ctx):
        if ctx.getChildCount() != 3:
            raise SyntaxError("Integer division requires exactly 2 operands")
        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        if left is None or right is None:
            raise ValueError("Cannot evaluate integer division operands")
        if right == 0:
            raise ZeroDivisionError("Division by zero")
        return left // right


class BooleanVisitor(ExpressionVisitor):
    def visitBooleanExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "==": self._handle_equal,
            "!=": self._handle_not_equal,
            "<": self._handle_less,
            ">": self._handle_greater,
            "<=": self._handle_less_equal,
            ">=": self._handle_greater_equal,
            "not": self._handle_not,
        }
        return handlers[op](ctx)

    def _handle_equal(self, ctx):
        # So sánh bằng: (== expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left == right

    def _handle_not_equal(self, ctx):
        # So sánh khác: (!= expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left != right

    def _handle_less(self, ctx):
        # So sánh nhỏ hơn: (< expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left < right

    def _handle_greater(self, ctx):
        # So sánh lớn hơn: (> expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left > right

    def _handle_less_equal(self, ctx):
        # So sánh nhỏ hơn hoặc bằng: (<= expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left <= right

    def _handle_greater_equal(self, ctx):
        # So sánh lớn hơn hoặc bằng: (>= expr1 expr2)
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left >= right

    def _handle_not(self, ctx):
        # Phủ định: (not expr)
        value = self.visit(ctx.expression(0))
        return not value


class ListVisitor(BaseInterpreter):
    def visitListExpr(self, ctx):
        # First child is 'list' keyword, skip it
        result = []

        # Start from index 1 to skip the 'list' keyword
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            child_value = self.visit(child)

            if child_value is None:
                raise ValueError(f"Cannot evaluate list element at position {i}")

            result.append(child_value)
        return result

    def visitListOpExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "head": self._handle_head,
            "tail": self._handle_tail,
            "getid": self._handle_getid,
            "sizeof": self._handle_sizeof,
        }
        if op not in handlers:
            raise OnionNameError(f"Unknown list operation '{op}'")
        return handlers[op](ctx)

    def _handle_head(self, ctx):
        lst = self._resolve_list(ctx, 0)
        self._validate_non_empty(lst, "head")
        return lst[0]

    def _handle_tail(self, ctx):
        lst = self._resolve_list(ctx, 0)
        self._validate_non_empty(lst, "tail")
        return lst[1:]

    def _handle_getid(self, ctx):
        if len(ctx.expression()) < 2:
            raise OnionArgumentError("getid requires an index and a list")
        index = self.visit(ctx.expression(0))
        if not isinstance(index, int):
            raise OnionTypeError(
                f"Index must be an integer, got {type(index).__name__}"
            )
        lst = self.visit(ctx.expression(1))
        if not isinstance(lst, list):
            raise OnionTypeError(f"Expected a list but got {type(lst).__name__}")
        if index < 0 or index >= len(lst):
            raise OnionRuntimeError(
                f"Index {index} out of range for list of length {len(lst)}"
            )
        return lst[index]

    def _handle_sizeof(self, ctx):
        lst = self._resolve_list(ctx, 0)
        return len(lst)

    def _resolve_list(self, ctx, expr_index):
        # Prefer explicit expression argument
        if len(ctx.expression()) > expr_index:
            lst = self.visit(ctx.expression(expr_index))
        else:
            # Fallback: next token after op is an identifier
            var_name = ctx.getChild(expr_index + 1).getText()
            try:
                lst = self.env.resolve(var_name)
            except NameError:
                raise OnionNameError(f"Variable '{var_name}' is not defined")
        if not isinstance(lst, list):
            raise OnionTypeError(f"Expected a list but got {type(lst).__name__}")
        return lst

    def _validate_non_empty(self, lst, op):
        if not lst:
            raise OnionRuntimeError(f"Cannot perform '{op}' on empty list")


class ConditionalVisitor(BaseInterpreter):
    def visitIfExpr(self, ctx):
        return self._handle_conditional(
            ctx.expression(), ctx.statement(), construct="if"
        )

    def visitBranchExpr(self, ctx):
        return self._handle_conditional(
            ctx.expression(), ctx.statement(), construct="branch"
        )

    def _handle_conditional(self, expr_list, stmt_list, construct):
        num_conds = len(expr_list)
        num_stmts = len(stmt_list)

        # Evaluate each condition in order
        for i, expr_ctx in enumerate(expr_list):
            cond_value = self.visit(expr_ctx)
            self._assert_bool(cond_value, construct)
            if cond_value:
                return self.visit(stmt_list[i])

        # No condition matched; check for default statement
        if num_stmts > num_conds:
            # Default is the last statement
            return self.visit(stmt_list[-1])

        # No branch taken
        return None

    def _assert_bool(self, value, construct):
        if not isinstance(value, bool):
            raise OnionTypeError(
                f"Condition in '{construct}' must be boolean, got {type(value).__name__}"
            )


class LoopVisitor(BaseInterpreter):
    def visitLoopStatement(self, ctx):
        loop_type = ctx.getChild(0).getText()
        handlers = {
            "repeat": self._handle_repeat,
            "loop": self._handle_for_loop,
            "while": self._handle_while,
        }
        if loop_type not in handlers:
            raise OnionNameError(f"Unknown loop type '{loop_type}'")
        return handlers[loop_type](ctx)

    def _handle_repeat(self, ctx):
        count = self.visit(ctx.expression(0))
        if not isinstance(count, int):
            raise OnionTypeError("Repeat count must be an integer")
        if count < 0:
            raise OnionRuntimeError("Repeat count cannot be negative")

        block_node = ctx.getChild(2) if ctx.getChildCount() > 2 else None
        return self._iterate_block(block_node, range(count))

    def _handle_for_loop(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        step = self.visit(ctx.expression(2)) if len(ctx.expression()) > 2 else 1

        for val, name in ((start, "start"), (end, "end"), (step, "step")):
            if not isinstance(val, int):
                raise OnionTypeError(f"Loop {name} must be an integer")
        if step == 0:
            raise OnionRuntimeError("Step cannot be zero")

        block_node = ctx.getChild(ctx.getChildCount() - 1)
        seq = range(start, end, step)

        def body():
            for current in seq:
                self.env.define(var_name, current)
                yield self.visit(block_node)

        return self._collect_loop_result(body())

    def _handle_while(self, ctx):
        cond_ctx = ctx.expression(0)
        block_node = ctx.getChild(2) if ctx.getChildCount() > 2 else None

        def body():
            while True:
                cond = self.visit(cond_ctx)
                if not isinstance(cond, bool):
                    raise OnionTypeError("While condition must be boolean")
                if not cond:
                    break
                yield self.visit(block_node)

        return self._collect_loop_result(body())

    def _iterate_block(self, block_node, iterator):
        result = None
        for _ in iterator:
            result = self.visit(block_node)
            if isinstance(result, ReturnValue):
                return result
        return result

    def _collect_loop_result(self, results):
        last = None
        for res in results:
            if isinstance(res, ReturnValue):
                return res
            last = res
        return last


class FunctionVisitor(BaseInterpreter):
    def visitFunctionDef(self, ctx):
        identifiers = ctx.IDENTIFIER()
        if not identifiers:
            return None

        name = identifiers[0].getText()
        params = [ident.getText() for ident in identifiers[1:]]
        self.functions[name] = {
            "params": params,
            "body": ctx.block()
        }
        return None

    def visitMacroDef(self, ctx):
        identifiers = ctx.IDENTIFIER()
        if not identifiers:
            return None

        name = identifiers[0].getText()
        params = [ident.getText() for ident in identifiers[1:]]
        self.macros[name] = {
            "params": params,
            "body": ctx.block()
        }
        return None

    def visitCallExpr(self, ctx):
        name = ctx.IDENTIFIER().getText()
        # Macro calls
        if name in self.macros:
            return self._call_callable(self.macros[name],
                                       [self.visit(e) for e in ctx.expression()],
                                       is_macro=True)

        # Built-in functions
        if name in BuiltInFunctions.registry:
            args = [self.visit(e) for e in ctx.expression()]
            return BuiltInFunctions.execute(name, self, args)

        # User-defined functions
        if name not in self.functions:
            raise OnionNameError(f"Function '{name}' is not defined")

        args = [self.visit(e) for e in ctx.expression()]
        return self._call_callable(self.functions[name], args)

    def _call_callable(self, callable_def, args, is_macro=False):
        params = callable_def["params"]
        if len(args) != len(params):
            kind = "Macro" if is_macro else "Function"
            raise OnionArgumentError(
                f"{kind} expected {len(params)} arguments, got {len(args)}"
            )
        return self._execute_callable(callable_def, args, is_macro=is_macro)

    def _execute_callable(self, callable_def, args, is_macro=False):
        params = callable_def["params"]
        body = callable_def["body"]
        
        if len(args) != len(params):
            error_type = "Macro" if is_macro else "Function"
            raise OnionArgumentError(
                f"{error_type} expected {len(params)} arguments, got {len(args)}"
            )
        
        previous_env = self.env
        new_env = SymbolTable(previous_env if not is_macro else None)
        
        for i, param in enumerate(params):
            new_env.define(param, args[i])
        
        try:
            self.env = new_env
            return self._execute_block(body)
        finally:
            self.env = previous_env

class Interpreter(
    ArithmeticVisitor,
    BooleanVisitor,
    ListVisitor,
    ConditionalVisitor,
    LoopVisitor,
    FunctionVisitor,
):
    def __init__(self):
        super().__init__()
        self.env = SymbolTable()
        BuiltInFunctions.register_defaults()

    def visit(self, tree):
        """Override visit with error handling"""
        try:
            return super().visit(tree)
        except OnionRuntimeError as e:
            raise e
        except Exception as e:
            raise OnionRuntimeError(f"Runtime error: {str(e)}") from e
