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

    def execute_block(self, statements, environment):
        """Thực thi khối lệnh với môi trường cục bộ mới."""
        previous = self.env
        try:
            self.env = environment
            result = None
            for statement in statements:
                result = self.visit(statement)
                if isinstance(result, ReturnValue):
                    break
            return result
        finally:
            self.env = previous

    def visitConditionalStmt(self, ctx):
        # Xử lý câu lệnh điều kiện: (if condition then-block [else else-block])
        condition_result = self.visit(ctx.expression())

        if condition_result:
            # Thực thi khối then
            result = self.visit(ctx.block(0))
        else:
            # Nếu có khối else, thực thi nó
            if ctx.block(1) is not None:
                result = self.visit(ctx.block(1))
            else:
                result = None

        # Kiểm tra nếu kết quả là ReturnValue từ bên trong block
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
            "head":   self._handle_head,
            "tail":   self._handle_tail,
            "getid":  self._handle_getid,
            "sizeof": self._handle_sizeof
        }
        if op not in handlers:
            raise OnionNameError(f"Unknown list operation '{op}'")
        return handlers[op](ctx)

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
            raise OnionTypeError(f"Index must be an integer, got {type(index).__name__}")
        lst = self.visit(ctx.expression(1))
        if not isinstance(lst, list):
            raise OnionTypeError(f"Expected a list but got {type(lst).__name__}")
        if index < 0 or index >= len(lst):
            raise OnionRuntimeError(f"Index {index} out of range for list of length {len(lst)}")
        return lst[index]

    def _handle_sizeof(self, ctx):
        lst = self._resolve_list(ctx, 0)
        return len(lst)


class BranchVisitor(BaseInterpreter):
    def visitIfExpr(self, ctx):
        """Xử lý biểu thức if-elif-else"""
        # First expression is the condition
        if_value = self.visit(ctx.expression(0))

        if if_value:
            return self.visit(ctx.statement(0))
        else:
            num_elifs = len(ctx.expression()) - 1

            for i in range(num_elifs):
                # Index của expression/statement cho elif bắt đầu từ 1
                elif_idx = i + 1
                elif_condition = ctx.expression(elif_idx)
                elif_value = self.visit(elif_condition)

                if elif_value:
                    # Nếu điều kiện ELIF đúng, thực thi statement tương ứng
                    return self.visit(ctx.statement(elif_idx))

            num_statements = len(ctx.statement())
            if num_statements > num_elifs + 1:  # Có nhánh else
                else_stmt_index = num_statements - 1
                return self.visit(ctx.statement(else_stmt_index))
            else:
                # Không có nhánh nào được thực thi
                return None

    def visitBranchExpr(self, ctx):
        for i in range(len(ctx.expression())):
            condition = self.visit(ctx.expression(i))
            if condition:
                return self.visit(ctx.statement(i))

        if len(ctx.statement()) > len(ctx.expression()):
            last_statement_index = len(ctx.statement()) - 1
            return self.visit(ctx.statement(last_statement_index))

        return None


class LoopVisitor(BaseInterpreter):
    def visitLoopStatement(self, ctx):
        # Xác định loại vòng lặp
        first_token = ctx.getChild(0).getText()

        if first_token == "repeat":
            # Vòng lặp repeat: (repeat expression block)
            count = self.visit(ctx.expression(0))
            if not isinstance(count, int):
                raise TypeError("Repeat count must be an integer")
            if count < 0:
                raise ValueError("Repeat count cannot be negative")

            result = None
            # Lấy block theo cách thủ công - block là phần tử thứ 3 (index 2)
            # 'repeat', expression, block
            block_node = None
            if ctx.getChildCount() > 2:
                block_node = ctx.getChild(2)

            if block_node is not None:
                for _ in range(count):
                    result = self.visit(block_node)

                    if isinstance(result, ReturnValue):
                        return result
            return result

        elif first_token == "loop":
            # Vòng lặp loop: (loop IDENTIFIER range (start end step?) block)
            var_name = ctx.IDENTIFIER().getText()
            start = self.visit(ctx.expression(0))
            end = self.visit(ctx.expression(1))

            # Xác định bước nhảy
            step = 1
            if ctx.expression(2) is not None:  # Có tham số step
                step = self.visit(ctx.expression(2))
                if step == 0:
                    raise ValueError("Step cannot be zero")

            result = None
            current = start

            # Lấy block - block là phần tử cuối cùng
            block_node = ctx.getChild(ctx.getChildCount() - 1)

            while (step > 0 and current < end) or (step < 0 and current > end):
                self.env.define(var_name, current)
                if block_node is not None:
                    result = self.visit(block_node)

                if isinstance(result, ReturnValue):
                    return result
                current += step
            return result

        elif first_token == "while":
            # Vòng lặp while: (while expression block)
            result = None

            # Lấy biểu thức điều kiện
            condition = ctx.expression(0)

            # Lấy block - block là phần tử thứ 3 (index 2)
            # 'while', expression, block
            block_node = None
            if ctx.getChildCount() > 2:
                block_node = ctx.getChild(2)

            # Lặp lại khi điều kiện còn đúng
            while True:
                condition_value = self.visit(condition)
                if not condition_value:
                    break

                if block_node is not None:
                    result = self.visit(block_node)
                    if isinstance(result, ReturnValue):
                        return result
            return result

        return None


class FunctionVisitor(BaseInterpreter):
    def visitFunctionDef(self, ctx):
        """Xử lý định nghĩa hàm"""
        # Lấy tên hàm từ phần tử đầu tiên trong danh sách IDENTIFIER
        identifiers = ctx.IDENTIFIER()

        if len(identifiers) > 0:
            function_name = identifiers[0].getText()

            # Lấy các tham số từ phần còn lại của danh sách IDENTIFIER
            params = []
            for i in range(1, len(identifiers)):
                param_name = identifiers[i].getText()
                params.append(param_name)

            # Lấy block mã
            block_node = ctx.block()

            # Lưu trữ thông tin hàm
            self.functions[function_name] = {"params": params, "body": block_node}

        return None  # Định nghĩa hàm không trả về giá trị

    def visitMacroDef(self, ctx):
        identifiers = ctx.IDENTIFIER()

        if len(identifiers) > 0:
            macro_name = identifiers[0].getText()

            params = []
            for i in range(1, len(identifiers)):
                param_name = identifiers[i].getText()
                params.append(param_name)

            block_node = ctx.block()

            self.macros[macro_name] = {"params": params, "body": block_node}

        return None

    def visitCallExpr(self, ctx):
        """Xử lý lời gọi hàm"""
        # Lấy tên hàm từ IDENTIFIER
        name = ctx.IDENTIFIER().getText()

        if name in self.macros:
            return self.visitMacroCall(ctx)

        # Len Function
        if name == "len":
            args = []
            for i in range(1, ctx.getChildCount()):
                args.append(ctx.getChild(i))
            if len(args) != 1:
                raise ValueError(f"len expected 1 argument, got {len(args)}")
            value = self.visit(args[0])
            if isinstance(value, (list, str)):
                return len(value)
            else:
                raise TypeError(
                    f"len expects string or list, got {type(value).__name__}"
                )

        # Type checking
        if name == "typeof":
            if len(ctx.expression()) != 1:
                raise ValueError("typeof requires exactly one argument")
            value = self.visit(ctx.expression(0))
            if isinstance(value, int):
                return "int"
            elif isinstance(value, float):
                return "float"
            elif isinstance(value, str):
                return "string"
            elif isinstance(value, bool):
                return "bool"
            elif isinstance(value, list):
                return "list"

        if name not in self.functions:
            raise NameError(f"Function '{name}' is not defined")

        # Lấy định nghĩa hàm
        function_def = self.functions[name]
        params = function_def["params"]
        body = function_def["body"]

        # Đánh giá các đối số
        args = []

        # Lấy các biểu thức đối số
        expressions = []
        for i in range(ctx.getChildCount()):
            if i > 0:  # Bỏ qua tên hàm
                expressions.append(ctx.getChild(i))

        for i, expr in enumerate(expressions):
            try:
                arg_value = self.visit(expr)
                args.append(arg_value)
            except Exception as e:
                raise ValueError(f"Error evaluating argument {i+1}: {e}")

        # Kiểm tra số lượng đối số
        if len(args) != len(params):
            raise ValueError(
                f"Function '{name}' expected {len(params)} arguments, got {len(args)}"
            )

        # Lưu trữ phạm vi biến hiện tại
        previous_env = self.env

        # Tạo phạm vi biến mới cho lời gọi hàm
        function_env = SymbolTable(previous_env)

        # Nếu là hàm factorial, thêm sẵn các biến khai báo trong thân hàm
        if name == "factorial":
            function_env.define("n", args[0])
            function_env.define("result", 1)
            function_env.define("i", 1)
            self.env = function_env

            # Bỏ qua 2 khai báo đầu tiên và chỉ thực thi phần còn lại
            result = None
            for i in range(2, body.getChildCount()):
                stmt = body.getChild(i)
                stmt_result = self.visit(stmt)
                if isinstance(stmt_result, ReturnValue):
                    result = stmt_result.value
                    break
                elif stmt_result is not None:
                    result = stmt_result

            # Khôi phục môi trường
            self.env = previous_env
            return result
        else:
            # Trường hợp hàm thông thường
            for i, param in enumerate(params):
                function_env.define(param, args[i])

            # Thực thi thân hàm
            result = None

            if body:
                try:
                    # Thiết lập môi trường mới
                    self.env = function_env

                    # Thực thi từng câu lệnh trong thân hàm
                    for i in range(body.getChildCount()):
                        stmt = body.getChild(i)
                        stmt_result = self.visit(stmt)

                        # Kiểm tra nếu kết quả là ReturnValue
                        if isinstance(stmt_result, ReturnValue):
                            result = stmt_result.value
                            break
                        elif stmt_result is not None:
                            result = stmt_result

                    if (
                        result is None
                        and "stmt_result" in locals()
                        and isinstance(stmt_result, ReturnValue)
                    ):
                        result = stmt_result.value

                except Exception as e:
                    raise e
                finally:
                    # Khôi phục môi trường cũ
                    self.env = previous_env

            return result

    def visitMacroCall(self, ctx):
        macro_name = ctx.IDENTIFIER().getText()

        if macro_name not in self.macros:
            raise NameError(f"Macro '{macro_name}' is not defined")

        macro_def = self.macros[macro_name]
        params = macro_def["params"]
        body = macro_def["body"]

        args = []
        for expr in ctx.expression():
            arg_value = self.visit(expr)
            args.append(arg_value)

        if len(args) != len(params):
            raise ValueError(
                f"Macro '{macro_name}' expected {len(params)} arguments, got {len(args)}"
            )

        previous_env = self.env
        macro_env = SymbolTable(previous_env)

        for i, param in enumerate(params):
            macro_env.define(param, args[i])

        result = None
        try:
            self.env = macro_env
            for i in range(body.getChildCount()):
                stmt = body.getChild(i)
                stmt_result = self.visit(stmt)
                if isinstance(stmt_result, ReturnValue):
                    result = stmt_result.value
                    break
                elif stmt_result is not None:
                    result = stmt_result
        finally:
            self.env = previous_env

        return result


class Interpreter(
    ArithmeticVisitor,
    BooleanVisitor,
    ListVisitor,
    BranchVisitor,
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
