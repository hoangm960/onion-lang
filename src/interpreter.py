import os
import sys

from antlr4 import ErrorNode, TerminalNode

from generated.OnionParser import OnionParser
from generated.OnionVisitor import OnionVisitor
from src.builtins import BuiltInFunctions
from src.exceptions import (OnionArgumentError, OnionNameError,
                            OnionPrintError, OnionRuntimeError, OnionTypeError)
from src.symbol_table import SymbolTable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ReturnValue:
    """Lớp bọc giá trị trả về bởi lệnh return."""

    def __init__(self, value):
        super().__init__()
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
            raise OnionPrintError from e

    def visitAssignment(self, ctx):
        # Check the second child to distinguish assignment types
        second_child = ctx.getChild(1)

        # Case 1: Multi-assignment like 'let (a 1) (b 2)'
        # The second child is '('
        if isinstance(second_child, TerminalNode) and second_child.getText() == '(':
            # Dạng nhiều biến: let (a 1) (b 2)
            result = None
            # Start from index 1 (the first '(')
            i = 1
            while i < ctx.getChildCount():
                 # Check if the current child is an opening parenthesis indicating a pair
                if isinstance(ctx.getChild(i), TerminalNode) and ctx.getChild(i).getText() == "(":
                    # A pair starts at index i, id is at i+1, expr is at i+2, ) is at i+3
                    if i + 3 < ctx.getChildCount():
                        var_name_node = ctx.getChild(i+1)
                        expr_node = ctx.getChild(i+2)
                        closing_paren = ctx.getChild(i+3)

                        # Basic structural check for '(' IDENTIFIER (expression | ternaryExpr) ')'
                        if isinstance(var_name_node, TerminalNode) and ctx.parser.ruleNames[var_name_node.symbol.type -1] == 'IDENTIFIER' and \
                           (isinstance(expr_node, OnionParser.ExpressionContext) or isinstance(expr_node, OnionParser.TernaryExprContext)) and \
                           isinstance(closing_paren, TerminalNode) and closing_paren.getText() == ')':

                            var_name = var_name_node.getText()
                            var_value = self.visit(expr_node)
                            self.env.define(var_name, var_value)
                            result = var_value # Keep track of the last assigned value
                            i += 3 # Move index past the processed pair ')'
                        else:
                             raise OnionRuntimeError(f"Malformed multi-assignment pair starting near index {i}")
                    else:
                        raise OnionRuntimeError(f"Incomplete multi-assignment pair starting near index {i}")
                
                i += 1 # Move to the next child, checking if it starts a pair
            return result # Return the value of the last assignment in the multi-let

        # Case 2: Single or Conditional assignment: 'let' IDENTIFIER ...
        # The second child is an IDENTIFIER
        elif isinstance(second_child, TerminalNode) and second_child.symbol.type == OnionParser.IDENTIFIER:
             identifier = second_child.getText() # Get identifier text
             expressions = ctx.expression() # Get all expression nodes

             if len(expressions) == 1: # Simple assignment: let x expr
                 value = self.visit(expressions[0])
                 self.env.define(identifier, value)
                 return value
             else:
                 # Should not happen based on the grammar if single/conditional
                 raise OnionRuntimeError(f"Unexpected number of expressions ({len(expressions)}) in single/conditional assignment for '{identifier}'")
        else:
            # This case should theoretically not be reachable if the grammar is correct
            # and the input parses successfully.
            raise OnionRuntimeError("Unrecognized assignment structure")

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
        current_value = self.env.lookup(var_name)
        if current_value is None:
            raise OnionNameError(f"Variable '{var_name}' is not defined")

        if not isinstance(current_value, (int, float)):
            raise OnionTypeError(
                f"Cannot increment/decrement non-numeric value: {current_value}"
            )

        # Calculate new value
        if op == "inc":
            new_value = current_value + 1
        elif op == "dec":
            new_value = current_value - 1
        else:
            raise OnionRuntimeError(f"Unknown operation: {op}")

        # Update value in environment
        self.env.define(var_name, new_value)
        return new_value

    def visitReturnStmt(self, ctx):
        """Xử lý lệnh return trong hàm"""
        if ctx.getChildCount() > 1:
            expr = ctx.getChild(1)  # Phần tử thứ 2 (index 1) sau 'return'
            value = self.visit(expr) # Triggers lookup if expr is identifier
            return ReturnValue(value)
        return ReturnValue(None)

    def execute_block(self, statements, environment=None):
        """Thực thi khối lệnh với môi trường cục bộ mới."""
        if environment:
            self.env = environment
        else:
            self.env.push_scope()
            
        try:
            result = None
            for statement in statements:
                result = self.visit(statement)
                if isinstance(result, ReturnValue):
                    break
            return result
        finally:
            if not environment:
                self.env.pop_scope()

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

        return result
    
    def visitAppendStmt(self, ctx):
        """Visit the append statement: (append list_var element_expr)"""
        var_name = ctx.IDENTIFIER().getText()
        element_expr = ctx.expression()

        # Look up the list variable in the environment
        lst = self.env.lookup(var_name)

        if lst is None:
            raise OnionNameError(f"List variable '{var_name}' is not defined")
        if not isinstance(lst, list):
            raise OnionTypeError(f"Variable '{var_name}' must be a list to append, got {type(lst).__name__}")

        # Evaluate the element to append
        element = self.visit(element_expr)

        # Perform the append (modifies the list in place)
        lst.append(element)

        # Statements typically return None unless they are return statements
        return None


class ExpressionVisitor(BaseInterpreter):
    def _resolve_identifier(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.env.lookup(var_name)

        if value is not None:
            # Variable found in the environment
            return value
        else:
            # Variable not found in environment scopes.
            # Built-in functions are handled by visitCallExpr.
            # If it's not in the environment, it's undefined in this context.
            raise OnionNameError(f"Undefined variable '{var_name}'")

    def _resolve_variable(self, name):
        """Resolve a variable from the environment"""
        value = self.env.lookup(name)
        if value is None:
            raise NameError(f"Variable '{name}' is not defined")
        return value
        
    def _assign_variable(self, name, value):
        """Assign a value to a variable in the environment"""
        # Search for the variable in existing scopes
        found = False
        for scope in reversed(self.env.scopes):
            if name in scope:
                scope[name] = value
                found = True
                break
                
        return found

    def visitExpression(self, ctx):
        if ctx.literal():
            result = self.visit(ctx.literal())
            return result
        elif ctx.IDENTIFIER():
            return self._resolve_identifier(ctx)
        elif ctx.compoundExpr():
            return self.visit(ctx.compoundExpr())
        elif ctx.incDecExpr():
            return self.visit(ctx.incDecExpr())
        return None

    def visitCompoundExpr(self, ctx):
        if ctx.arithmeticExpr():
            return self.visit(ctx.arithmeticExpr())
        if ctx.booleanExpr():
            return self.visit(ctx.booleanExpr())
        if ctx.logicalExpr():
            return self.visit(ctx.logicalExpr())
        if ctx.listExpr():
            return self.visit(ctx.listExpr())
        if ctx.callExpr():
            return self.visit(ctx.callExpr())
        if ctx.ifExpr():
            return self.visit(ctx.ifExpr())
        if ctx.branchExpr():
            return self.visit(ctx.branchExpr())
        if ctx.ternaryExpr():
            return self.visit(ctx.ternaryExpr())
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

    def visitIncDecExpr(self, ctx):
        """Handle increment/decrement expressions"""
        op = ctx.getChild(0).getText()
        var_name = ctx.IDENTIFIER().getText()

        # Get current value
        current_value = self.env.lookup(var_name)
        if current_value is None:
            raise OnionNameError(f"Variable '{var_name}' is not defined")

        if not isinstance(current_value, (int, float)):
            raise OnionTypeError(f"Cannot increment/decrement non-numeric value: {current_value}")

        if op == "inc":
            # Increment: (inc x)
            new_value = current_value + 1
        elif op == "dec":
            # Decrement: (dec x)
            new_value = current_value - 1
        else:
            raise OnionRuntimeError(f"Unknown operation: {op}")

        # Update value and return new value
        self.env.define(var_name, new_value)
        return new_value


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
    
    def visitLogicalExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "&": self._handle_and,
            "|": self._handle_or,
            "!": self._handle_not_logical
        }
        return handlers[op](ctx)

    def _handle_and(self, ctx):
        # Logical AND: (& expr1 expr2)
        left = self.visit(ctx.expression(0))
        # Short-circuit evaluation - if left is falsy, don't evaluate right
        if not left:
            return False
        right = self.visit(ctx.expression(1))
        return bool(left and right)
        
    def _handle_or(self, ctx):
        # Logical OR: (| expr1 expr2)
        left = self.visit(ctx.expression(0))
        # Short-circuit evaluation - if left is truthy, don't evaluate right
        if left:
            return True
        right = self.visit(ctx.expression(1))
        return bool(left or right)
        
    def _handle_not_logical(self, ctx):
        # Logical NOT: (! expr) - equivalent to (not expr) but keeping both for compatibility
        value = self.visit(ctx.expression(0))
        return not bool(value)

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

    def visitTernaryExpr(self, ctx):
        """Handle ternary expression: (if condition true_expr : false_expr)"""
        # Children: 'if', condition_expr, true_expr, ':', false_expr
        condition = self.visit(ctx.expression(0))

        if not isinstance(condition, bool):
            raise OnionTypeError(f"Ternary expression requires a boolean condition, got {type(condition).__name__}")

        if condition:
            return self.visit(ctx.expression(1)) # Evaluate true expression
        else:
            return self.visit(ctx.expression(2)) # Evaluate false expression


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

        # Handle different numbers of arguments for range()
        expressions = ctx.expression()
        num_args = len(expressions)

        if num_args == 1:
            # range(end)
            start = 0
            end = self.visit(expressions[0])
            step = 1
        elif num_args == 2:
            # range(start, end)
            start = self.visit(expressions[0])
            end = self.visit(expressions[1])
            step = 1
        elif num_args == 3:
            # range(start, end, step)
            start = self.visit(expressions[0])
            end = self.visit(expressions[1])
            step = self.visit(expressions[2])
        else:
            # This case should ideally be caught by the parser based on the grammar
            raise OnionArgumentError(f"range() expects 1, 2, or 3 arguments, got {num_args}")

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
        
        # Evaluate all arguments
        args = self._evaluate_arguments(ctx)
        if name in self.macros:
            return self._handle_macro_call(ctx, name, args)
            
        if name in BuiltInFunctions.registry:
            return BuiltInFunctions.execute(name, self, args)
        
        elif name == "typeof":
            return self._handle_typeof(args)
            
        if name in self.functions:
            return self._handle_function_call(ctx, name, args)
            
        # Function not found
        raise OnionNameError(f"Function '{name}' is not defined")
            
    def _handle_typeof(self, args):
        """Handle the built-in typeof function"""
        if len(args) != 1:
            raise OnionArgumentError("typeof requires exactly one argument")
        value = args[0]
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
        else:
            return "unknown"
    
    def _handle_function_call(self, ctx, name, args=None):
        function_def = self.functions[name]
        params = function_def["params"]
        body = function_def["body"]

        if args is None:
            args = self._evaluate_arguments(ctx)

        if len(args) != len(params):
            raise OnionArgumentError(
                f"Function '{name}' expected {len(params)} arguments, got {len(args)}"
            )

        self.env.push_scope()
        
        current_scope = self.env.current_scope()
        # Define parameters directly in the new scope
        for i, param in enumerate(params):
            current_scope[param] = args[i]

        final_return_value = None
        # Execute the function body statement by statement
        for i in range(body.getChildCount()):
            stmt = body.getChild(i)
            stmt_result = self.visit(stmt) # This might return a ReturnValue object
            
            if isinstance(stmt_result, ReturnValue):
                final_return_value = stmt_result.value # Extract the actual value
                break # Exit the loop immediately upon return
            elif stmt_result is not None:
                # If no explicit return, the value of the last statement is used (like Lisp)
                final_return_value = stmt_result

        # The scope is still present here, after body execution / return detection
        self.env.pop_scope()

        return final_return_value # Return the determined value

    def _handle_macro_call(self, ctx, macro_name=None, args=None):
        """Handle execution of a macro"""
        if macro_name is None:
            macro_name = ctx.IDENTIFIER().getText()
            
        macro_def = self.macros[macro_name]
        params = macro_def["params"]
        body = macro_def["body"]

        # Use provided args or evaluate them if not provided
        if args is None:
            args = self._evaluate_arguments(ctx)

        # Validate argument count
        if len(args) != len(params):
            raise OnionArgumentError(
                f"Macro '{macro_name}' expected {len(params)} arguments, got {len(args)}"
            )

        # Create a new scope for macro execution
        self.env.push_scope()
        
        try:
            # Define parameters in the new scope
            for i, param in enumerate(params):
                self.env.define(param, args[i])

            # Execute the macro body
            result = None
            for i in range(body.getChildCount()):
                stmt = body.getChild(i)
                stmt_result = self.visit(stmt)
                
                if isinstance(stmt_result, ReturnValue):
                    result = stmt_result.value
                    break
                elif stmt_result is not None:
                    result = stmt_result
                    
            return result
        finally:
            # Restore previous scope
            self.env.pop_scope()
            
    def _evaluate_arguments(self, ctx):
        """Evaluate function call arguments"""
        args = []
        for expr in ctx.expression():
            try:
                arg_value = self.visit(expr)
                args.append(arg_value)
            except Exception as e:
                raise OnionRuntimeError(f"Error evaluating argument: {e}")
        return args

class Interpreter(
    # BaseInterpreter is inherited via other visitors
    ArithmeticVisitor,  # Inherits ExpressionVisitor -> BaseInterpreter
    BooleanVisitor,     # Inherits ExpressionVisitor -> BaseInterpreter
    ListVisitor,        # Inherits BaseInterpreter
    ConditionalVisitor, # Inherits BaseInterpreter
    LoopVisitor,        # Inherits BaseInterpreter
    FunctionVisitor     # Inherits BaseInterpreter
):
    def __init__(self):
        # Ensure super().__init__() calls the correct chain
        super().__init__()
        # Initialize environment and built-ins specifically for Interpreter instance
        self.env = SymbolTable()
        BuiltInFunctions.register_defaults()

    def visit(self, tree):
        """Override visit with error handling"""
        try:
            # The super().visit() will correctly traverse the MRO
            return super().visit(tree)
        except OnionRuntimeError as e:
            raise e
        except Exception as e:
            raise OnionRuntimeError(f"Runtime error: {str(e)}") from e


