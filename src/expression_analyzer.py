# src/expression_analyzer.py

from generated.OnionParser import OnionParser
from antlr4 import TerminalNode
from src.exceptions import (
    OnionRuntimeError,
    OnionNameError,
    OnionArgumentError,
    OnionTypeError
)
from src.builtins import BuiltInFunctions
# Assuming ReturnValue will be accessible via interpreter instance
# from src.statement_analyzer import ReturnValue 

# Forward declaration for type hinting is good practice
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.interpreter import Interpreter, ReturnValue # Import ReturnValue for type hinting

class ExpressionAnalyzer:
    """
    Handles the analysis and evaluation of expression nodes in the Onion AST.
    It collaborates with the main Interpreter instance.
    """
    def __init__(self, interpreter: 'Interpreter'):
        """
        Initializes the ExpressionAnalyzer.

        Args:
            interpreter: The main Interpreter instance.
        """
        self.interpreter = interpreter

    # --- Core Expression Visitors ---

    def visitExpression(self, ctx: OnionParser.ExpressionContext):
        """Visits a general expression node."""
        if ctx.literal():
            # Delegate visiting literals back to the main interpreter's visit
            # which will then call the appropriate method in this analyzer.
            return self.interpreter.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            # Resolve identifiers directly using a helper method.
            return self._resolve_identifier(ctx)
        elif ctx.compoundExpr():
            # Delegate visiting compound expressions back to the interpreter.
            return self.interpreter.visit(ctx.compoundExpr())
        elif ctx.incDecExpr():
            # Delegate visiting increment/decrement expressions.
            return self.interpreter.visit(ctx.incDecExpr())
        # If none of the above, it might be an error or an unhandled case.
        # Returning None might be acceptable depending on language semantics.
        return None

    def visitCompoundExpr(self, ctx: OnionParser.CompoundExprContext):
        """Visits a compound expression node, delegating to specific types."""
        # Check each possible type of compound expression and delegate.
        if ctx.arithmeticExpr():
            return self.interpreter.visit(ctx.arithmeticExpr())
        if ctx.booleanExpr():
            return self.interpreter.visit(ctx.booleanExpr())
        if ctx.logicalExpr():
            return self.interpreter.visit(ctx.logicalExpr())
        if ctx.listExpr():
            return self.interpreter.visit(ctx.listExpr())
        if ctx.callExpr():
            return self.interpreter.visit(ctx.callExpr())
        if ctx.branchExpr():
            return self.interpreter.visit(ctx.branchExpr())
        if ctx.ternaryExpr():
            return self.interpreter.visit(ctx.ternaryExpr())
        if ctx.listOpExpr():
            return self.interpreter.visit(ctx.listOpExpr())

        return None

    def visitLiteral(self, ctx: OnionParser.LiteralContext):
        """Visits a literal node and returns its Python value."""
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        if ctx.STRING():
            text = ctx.STRING().getText()
            # Remove the surrounding quotes from the string literal.
            return text[1:-1]
        if ctx.BOOL():
            token = ctx.BOOL().getText()
            # Convert "true" or "false" string to Python boolean.
            return token == "true"
        # Should not happen if grammar requires a literal type.
        return None

    # --- Arithmetic Operations ---

    def visitArithmeticExpr(self, ctx: OnionParser.ArithmeticExprContext):
        """Visits an arithmetic expression node (+, -, *, /, //)."""
        op_type = ctx.getChild(0).symbol.type # Check token type
        # Map operator token types to their handler methods.
        handlers = {
            OnionParser.PLUS: self._handle_addition,
            OnionParser.MINUS: self._handle_subtraction,
            OnionParser.MULT: self._handle_multiplication,
            OnionParser.DIV: self._handle_division,
            OnionParser.FLOOR_DIV: self._handle_integer_division, # Use FLOOR_DIV token
        }
        if op_type in handlers:
             return handlers[op_type](ctx)
        else:
             op_text = ctx.getChild(0).getText() # For error message
             raise OnionRuntimeError(f"Internal error: Unknown arithmetic operator type '{op_text}'")

    def _handle_addition(self, ctx):
        """Handles addition (+) supporting numbers and string concatenation."""
        # Visit the first operand (index 1, after the '+').
        result = self.interpreter.visit(ctx.getChild(1))
        # Iterate through the remaining operands (index 2 onwards).
        for i in range(2, ctx.getChildCount()):
            value = self.interpreter.visit(ctx.getChild(i))
            # Check types for valid addition/concatenation.
            if isinstance(result, str) and isinstance(value, str):
                result += value  # String concatenation
            elif isinstance(result, (int, float)) and isinstance(value, (int, float)):
                result += value  # Numeric addition
            else:
                # Raise error for incompatible types.
                raise OnionTypeError(
                    f"Cannot add values of incompatible types: {type(result).__name__} and {type(value).__name__}"
                )
        return result

    def _handle_subtraction(self, ctx):
        """Handles subtraction (-), requires exactly two numeric operands."""
        # Operator '-' is at index 0. Operands at 1 and 2.
        if ctx.getChildCount() != 3:
             raise OnionArgumentError(f"Subtraction operator '-' requires exactly 2 operands, got {ctx.getChildCount()-1}")
        left = self.interpreter.visit(ctx.getChild(1))
        right = self.interpreter.visit(ctx.getChild(2))
        # Ensure both operands are numeric.
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
             raise OnionTypeError(f"Subtraction requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
        return left - right

    def _handle_multiplication(self, ctx):
        """Handles multiplication (*), supports multiple numeric operands."""
        result = 1  # Initialize result for multiplication.
        # Iterate through operands (index 1 onwards).
        for i in range(1, ctx.getChildCount()):
            value = self.interpreter.visit(ctx.getChild(i))
            # Ensure each operand is numeric.
            if not isinstance(value, (int, float)):
                 raise OnionTypeError(f"Multiplication requires numeric operands, got {type(value).__name__} at position {i}")
            result *= value
        return result

    def _handle_division(self, ctx):
        """Handles float division (/), requires exactly two numeric operands."""
        if ctx.getChildCount() != 3:
            raise OnionArgumentError(f"Division operator '/' requires exactly 2 operands, got {ctx.getChildCount()-1}")
        left = self.interpreter.visit(ctx.getChild(1))
        right = self.interpreter.visit(ctx.getChild(2))
        # Ensure operands are numeric.
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise OnionTypeError(f"Division requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
        # Prevent division by zero.
        if right == 0:
            raise OnionRuntimeError("Division by zero")
        return left / right

    def _handle_integer_division(self, ctx):
        """Handles integer division (//), requires exactly two numeric operands."""
        if ctx.getChildCount() != 3:
             raise OnionArgumentError(f"Integer division operator '//' requires exactly 2 operands, got {ctx.getChildCount()-1}")
        left = self.interpreter.visit(ctx.getChild(1))
        right = self.interpreter.visit(ctx.getChild(2))
        # Ensure operands are numeric.
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
             raise OnionTypeError(f"Integer division requires numeric operands, got {type(left).__name__} and {type(right).__name__}")
        # Prevent division by zero.
        if right == 0:
             raise OnionRuntimeError("Integer division by zero")
        # Perform floor division and ensure the result is an integer.
        return int(left // right)

    # --- Boolean and Logical Operations ---

    def visitBooleanExpr(self, ctx: OnionParser.BooleanExprContext):
        """Visits boolean comparison expressions (==, !=, <, >, <=, >=, not)."""
        op_type = ctx.getChild(0).symbol.type # Check token type
        num_expressions = len(ctx.expression())

        # Handle unary 'not' separately.
        if op_type == OnionParser.NOT:
            if num_expressions != 1:
                 raise OnionArgumentError(f"Operator 'not' requires 1 operand, got {num_expressions}")
            return self._handle_not(ctx)
        # All other boolean operators are binary.
        elif num_expressions != 2:
             op_text = ctx.getChild(0).getText()
             raise OnionArgumentError(f"Boolean comparison operator '{op_text}' requires 2 operands, got {num_expressions}")

        # Map binary operators to handlers.
        handlers = {
            OnionParser.EQ: self._handle_equal,
            OnionParser.NEQ: self._handle_not_equal,
            OnionParser.LT: self._handle_less,
            OnionParser.GT: self._handle_greater,
            OnionParser.LTE: self._handle_less_equal,
            OnionParser.GTE: self._handle_greater_equal,
        }
        if op_type in handlers:
            return handlers[op_type](ctx)
        else:
            op_text = ctx.getChild(0).getText()
            raise OnionRuntimeError(f"Internal error: Unknown boolean operator type '{op_text}'")

    def visitLogicalExpr(self, ctx: OnionParser.LogicalExprContext):
        """Visits logical expressions (&, |, !)."""
        op_type = ctx.getChild(0).symbol.type # Check token type
        num_expressions = len(ctx.expression())

        # Handle unary logical '!'. Note: Grammar uses NOT token for both cases.
        if op_type == OnionParser.NOT:
            if num_expressions != 1:
                 raise OnionArgumentError(f"Logical operator '!' (NOT) requires 1 operand, got {num_expressions}")
            return self._handle_not_logical(ctx)
        # Handle binary logical '&' and '|'.
        elif num_expressions != 2:
             op_text = ctx.getChild(0).getText()
             raise OnionArgumentError(f"Logical operator '{op_text}' requires 2 operands, got {num_expressions}")

        handlers = {
            OnionParser.AND: self._handle_and,
            OnionParser.OR: self._handle_or,
        }
        if op_type in handlers:
            return handlers[op_type](ctx)
        else:
            op_text = ctx.getChild(0).getText()
            raise OnionRuntimeError(f"Internal error: Unknown logical operator type '{op_text}'")

    def _handle_and(self, ctx):
        """Handles logical AND (&) with short-circuiting."""
        # Evaluate left operand.
        left = self.interpreter.visit(ctx.expression(0))
        # Short-circuit if left is falsy.
        if not bool(left):
            return False
        # Only evaluate right if left is truthy.
        right = self.interpreter.visit(ctx.expression(1))
        # Result is the boolean value of the right operand.
        return bool(right)

    def _handle_or(self, ctx):
        """Handles logical OR (|) with short-circuiting."""
        # Evaluate left operand.
        left = self.interpreter.visit(ctx.expression(0))
        # Short-circuit if left is truthy.
        if bool(left):
            return True
        # Only evaluate right if left is falsy.
        right = self.interpreter.visit(ctx.expression(1))
        # Result is the boolean value of the right operand.
        return bool(right)

    def _handle_not_logical(self, ctx):
        """Handles logical NOT (!)."""
        value = self.interpreter.visit(ctx.expression(0))
        # Return the boolean negation of the operand's truthiness.
        return not bool(value)

    def _handle_equal(self, ctx):
        """Handles equality comparison (==)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        return left == right

    def _handle_not_equal(self, ctx):
        """Handles inequality comparison (!=)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        return left != right

    def _handle_less(self, ctx):
        """Handles less than comparison (<)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        # Use try-except to catch potential TypeError for incomparable types.
        try:
            return left < right
        except TypeError:
             raise OnionTypeError(f"Cannot compare types '{type(left).__name__}' and '{type(right).__name__}' with '<'")

    def _handle_greater(self, ctx):
        """Handles greater than comparison (>)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        try:
            return left > right
        except TypeError:
             raise OnionTypeError(f"Cannot compare types '{type(left).__name__}' and '{type(right).__name__}' with '>'")

    def _handle_less_equal(self, ctx):
        """Handles less than or equal comparison (<=)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        try:
            return left <= right
        except TypeError:
             raise OnionTypeError(f"Cannot compare types '{type(left).__name__}' and '{type(right).__name__}' with '<='")

    def _handle_greater_equal(self, ctx):
        """Handles greater than or equal comparison (>=)."""
        left = self.interpreter.visit(ctx.expression(0))
        right = self.interpreter.visit(ctx.expression(1))
        try:
            return left >= right
        except TypeError:
             raise OnionTypeError(f"Cannot compare types '{type(left).__name__}' and '{type(right).__name__}' with '>='")

    def _handle_not(self, ctx):
        """Handles boolean NOT (not)."""
        # Note: This is distinct from logical NOT (!).
        value = self.interpreter.visit(ctx.expression(0))
        # Return the boolean negation.
        return not bool(value)

    # --- List Expressions and Operations ---

    def visitListExpr(self, ctx: OnionParser.ListExprContext):
        """Visits a list literal expression (list e1 e2 ...)."""
        # First child should be the LIST token
        if not ctx.getChild(0) or ctx.getChild(0).symbol.type != OnionParser.LIST:
            raise OnionRuntimeError("Internal error: Expected 'list' keyword at start of list expression")
            
        elements = []
        # Iterate through children starting from index 1 (skipping 'list' keyword).
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            # Assume children are expressions representing list elements.
            element_value = self.interpreter.visit(child)
            elements.append(element_value)
        # Return the constructed Python list.
        return elements

    def visitListOpExpr(self, ctx: OnionParser.ListOpExprContext):
        """Visits list operation expressions (head, tail, getid, sizeof)."""
        op_type = ctx.getChild(0).symbol.type # Check token type
        handlers = {
            OnionParser.HEAD: self._handle_head,
            OnionParser.TAIL: self._handle_tail,
            OnionParser.GETID: self._handle_getid,
            OnionParser.SIZEOF: self._handle_sizeof,
        }
        if op_type in handlers:
            return handlers[op_type](ctx)
        else:
            op_text = ctx.getChild(0).getText()
            raise OnionNameError(f"Unknown list operation: '{op_text}'")

    def _handle_head(self, ctx):
        """Handles the 'head' list operation."""
        # Expects one expression argument after 'head'.
        if len(ctx.expression()) != 1:
             raise OnionArgumentError("Operation 'head' requires exactly one list argument")
        # Evaluate the argument, which should be a list.
        lst = self.interpreter.visit(ctx.expression(0))
        # Validate that it's a non-empty list.
        self._validate_list(lst, "head")
        self._validate_non_empty(lst, "head")
        # Return the first element.
        return lst[0]

    def _handle_tail(self, ctx):
        """Handles the 'tail' list operation."""
        if len(ctx.expression()) != 1:
             raise OnionArgumentError("Operation 'tail' requires exactly one list argument")
        lst = self.interpreter.visit(ctx.expression(0))
        self._validate_list(lst, "tail")
        self._validate_non_empty(lst, "tail")
        # Return a *new* list containing all elements except the first.
        return lst[1:]

    def _handle_getid(self, ctx):
        """Handles the 'getid' list operation (get element by index)."""
        # Expects two expression arguments: index and list.
        if len(ctx.expression()) != 2:
            raise OnionArgumentError("Operation 'getid' requires an index and a list argument")
        # Evaluate the index and the list.
        index_val = self.interpreter.visit(ctx.expression(0))
        lst = self.interpreter.visit(ctx.expression(1))

        # Validate index type and list type.
        if not isinstance(index_val, int):
            raise OnionTypeError(f"Index for 'getid' must be an integer, got {type(index_val).__name__}")
        self._validate_list(lst, "getid")

        # Perform bounds checking for the index.
        list_len = len(lst)
        if not (0 <= index_val < list_len):
             # Check for negative index maybe? Or stick to positive indices.
             # Assuming non-negative indices for now.
             raise OnionRuntimeError(f"Index {index_val} out of range for list of size {list_len}")

        # Return the element at the specified index.
        return lst[index_val]

    def _handle_sizeof(self, ctx):
        """Handles the 'sizeof' list operation (get list length)."""
        if len(ctx.expression()) != 1:
             raise OnionArgumentError("Operation 'sizeof' requires exactly one list argument")
        lst = self.interpreter.visit(ctx.expression(0))
        self._validate_list(lst, "sizeof")
        # Return the number of elements in the list.
        return len(lst)

    # --- List Helper Methods ---

    def _validate_list(self, value, op_name):
        """Ensures a value is a list for a given list operation."""
        if not isinstance(value, list):
            raise OnionTypeError(f"Operation '{op_name}' requires a list argument, got {type(value).__name__}")

    def _validate_non_empty(self, lst, op_name):
        """Ensures a list is not empty for operations like 'head' or 'tail'."""
        if not lst: # Check if the list is empty
            raise OnionRuntimeError(f"Cannot perform operation '{op_name}' on an empty list")

    def visitBranchExpr(self, ctx: OnionParser.BranchExprContext):
        """
        Visits a 'branch' expression: (branch (cond1 stmt1) (cond2 stmt2) ... [default_stmt]).
        Evaluates conditions sequentially and returns the result of the first matching statement.
        """
        num_conditions = len(ctx.expression())
        num_branches = len(ctx.statement())

        # Iterate through condition-statement pairs.
        for i in range(num_conditions):
            cond_ctx = ctx.expression(i)
            branch_ctx = ctx.statement(i) # Corresponding statement/branch.

            # Evaluate the condition.
            cond_value = self.interpreter.visit(cond_ctx)
            self._assert_bool(cond_value, f"branch expression condition {i+1}")

            # If condition is true, execute the corresponding statement and return its result.
            if cond_value:
                return self.interpreter.visit(branch_ctx)

        # If no condition matched, check for a default branch.
        # The default branch is the last statement if there are more statements than conditions.
        if num_branches > num_conditions:
            default_ctx = ctx.statement(num_branches - 1)
            return self.interpreter.visit(default_ctx)

        # No condition matched, and no default branch. Expression evaluates to None.
        return None

    def visitTernaryExpr(self, ctx: OnionParser.TernaryExprContext):
        """
        Visits a ternary expression: (if condition true_expr : false_expr).
        Evaluates the condition and returns the value of either true_expr or false_expr.
        Note: The grammar uses 'expression' here, implying value evaluation.
        """
        # Structure: IF expr[0] expr[1] COLON expr[2]
        # Check tokens IF and COLON
        if ctx.getChild(0).symbol.type != OnionParser.IF or \
           ctx.getChild(3).symbol.type != OnionParser.COLON:
             raise OnionRuntimeError("Internal error: Invalid ternary expression structure (missing IF or COLON)")
             
        if len(ctx.expression()) != 3:
             raise OnionRuntimeError("Internal error: Invalid ternary expression structure (incorrect number of expressions)")

        # Evaluate the condition (expression at index 0).
        condition = self.interpreter.visit(ctx.expression(0))
        self._assert_bool(condition, "ternary expression")

        # Return the value of the appropriate expression based on the condition.
        if condition:
            return self.interpreter.visit(ctx.expression(1)) # True expression
        else:
            return self.interpreter.visit(ctx.expression(2)) # False expression

    def _assert_bool(self, value, construct_name):
        """Helper to ensure a condition evaluates to a boolean type."""
        if not isinstance(value, bool):
            raise OnionTypeError(
                f"Condition in {construct_name} must evaluate to a boolean, but got type {type(value).__name__}"
            )

    # --- Function and Macro Call Expressions ---

    def visitCallExpr(self, ctx: OnionParser.CallExprContext):
        """
        Visits a function or macro call expression: (name arg1 arg2 ...).
        Resolves the name and executes the appropriate call.
        """
        # Get the function/macro name (IDENTIFIER).
        name = ctx.IDENTIFIER().getText()
        # Evaluate all argument expressions *before* determining the call type.
        args = self._evaluate_arguments(ctx)

        # Determine call type and execute:
        # 1. Macro? (Macros might have special evaluation rules, handled first).
        if name in self.interpreter.macros:
            return self._handle_macro_call(ctx, name, args)

        # 2. Built-in function? (Like 'typeof' or registered functions).
        if name == "typeof":
            # Handle 'typeof' directly as a special case.
            return self._handle_typeof(args)
        elif name in BuiltInFunctions.registry:
            # Delegate to the central BuiltInFunctions registry.
            # Pass the interpreter instance for context (e.g., accessing env).
            return BuiltInFunctions.execute(name, self.interpreter, args)

        # 3. User-defined function?
        elif name in self.interpreter.functions:
            return self._handle_function_call(ctx, name, args)

        # 4. Name not found.
        else:
            raise OnionNameError(f"Attempted to call undefined function, macro, or built-in: '{name}'")

    def _evaluate_arguments(self, ctx: OnionParser.CallExprContext):
        """Evaluates all argument expressions in a call expression."""
        args = []
        # Arguments are the expression nodes following the function name IDENTIFIER.
        for expr_ctx in ctx.expression():
            try:
                arg_value = self.interpreter.visit(expr_ctx)
                args.append(arg_value)
            except Exception as e:
                # Add context to the error message.
                func_name = ctx.IDENTIFIER().getText()
                # It might be helpful to know *which* argument failed, if possible.
                raise OnionRuntimeError(f"Error evaluating argument for call to '{func_name}': {e}") from e
        return args

    def _handle_typeof(self, args):
        """Handles the 'typeof' built-in operation."""
        if len(args) != 1:
            raise OnionArgumentError("'typeof' requires exactly one argument")
        value = args[0]
        # Return the type name as a lowercase string.
        if isinstance(value, int): return "int"
        if isinstance(value, float): return "float"
        if isinstance(value, str): return "string"
        if isinstance(value, bool): return "bool"
        if isinstance(value, list): return "list"
        # Consider adding 'function', 'macro', 'null'/'none' if applicable.
        return "unknown" # Fallback for other types.

    def _handle_function_call(self, ctx, name, args):
        """Executes a user-defined function call within a single new scope."""
        function_def = self.interpreter.functions[name]
        params = function_def["params"]
        body_block_ctx = function_def["body"] # The BlockContext AST node

        if len(args) != len(params):
            raise OnionArgumentError(
                f"Function '{name}' expects {len(params)} arguments, but received {len(args)}"
            )

        # --- Function Execution Scoping ---
        self.interpreter.env.push_scope() # Create ONE scope for the function call
        final_return_value = None
        try:
            # Bind arguments to parameters in the new scope.
            current_scope = self.interpreter.env.current_scope()
            for param_name, arg_value in zip(params, args):
                current_scope[param_name] = arg_value

            # --- Execute Function Body Directly --- 
            # Iterate through statements in the body block and execute them in the current scope.
            ReturnValue = self.interpreter.ReturnValue # Get the ReturnValue class
            
            # Check if body_block_ctx is actually a BlockContext and has children
            if not isinstance(body_block_ctx, OnionParser.BlockContext):
                 raise OnionRuntimeError(f"Internal error: Function '{name}' body is not a valid block.")
                 
            last_stmt_result = None # Track result for implicit return
            for i in range(body_block_ctx.getChildCount()):
                stmt = body_block_ctx.getChild(i)
                # Visit each statement within the function's scope
                stmt_result = self.interpreter.visit(stmt)
                last_stmt_result = stmt_result # Update last result

                # Check for explicit return
                if isinstance(stmt_result, ReturnValue):
                    final_return_value = stmt_result.value # Extract value from wrapper
                    break # Exit the loop immediately upon return
            else:
                # Loop finished without explicit return
                # The value of the last statement is the implicit return value
                final_return_value = last_stmt_result

        finally:
            # --- Scope Cleanup ---
            self.interpreter.env.pop_scope() # Always pop the function's scope

        # Return the determined value (explicit or implicit)
        return final_return_value

    def _handle_macro_call(self, ctx, macro_name, args):
        """
        Executes a user-defined macro call.
        NOTE: This is a simplified implementation treating macros like functions.
        True macros often involve unevaluated arguments or AST manipulation,
        which would require a more complex approach (e.g., passing AST nodes
        for arguments instead of evaluated values).
        """
        # Retrieve macro definition.
        macro_def = self.interpreter.macros[macro_name]
        params = macro_def["params"]
        body = macro_def["body"] # BlockContext

        # Validate argument count.
        if len(args) != len(params):
             raise OnionArgumentError(
                 f"Macro '{macro_name}' expects {len(params)} arguments, but received {len(args)}"
             )

        # --- Macro Scoping ---
        # Decide whether macros execute in caller's scope or a new scope.
        # Assuming a new scope for simplicity, similar to functions here.
        self.interpreter.env.push_scope()
        try:
            # Bind arguments to parameters in the new scope.
            current_scope = self.interpreter.env.current_scope()
            for param_name, arg_value in zip(params, args):
                 current_scope[param_name] = arg_value

            # --- Execute Macro Body ---
            # Delegate execution to the interpreter's block execution logic.
            ReturnValue = self.interpreter.ReturnValue # Access via interpreter
            block_result = self.interpreter.execute_block(body)

            # Determine macro result (similar to functions for now).
            if isinstance(block_result, ReturnValue):
                result = block_result.value
            else:
                result = block_result # Implicit return value

            return result
        finally:
             # Clean up the macro's scope.
             self.interpreter.env.pop_scope()

    # --- Identifier Resolution ---

    def _resolve_identifier(self, ctx: OnionParser.ExpressionContext):
        """
        Resolves an IDENTIFIER used within an expression context.
        Looks up the identifier in the interpreter's environment.
        """
        var_name = ctx.IDENTIFIER().getText()
        # Use the interpreter's environment lookup mechanism.
        value = self.interpreter.env.lookup(var_name)

        if value is not None:
            # Variable found in the current or enclosing scopes.
            return value
        else:
            # Identifier is not defined as a variable in the accessible scopes.
            # In an expression context, this usually means an undefined variable.
            # (Function/macro names are typically only resolved in call expressions).
            raise OnionNameError(f"Undefined variable '{var_name}' referenced")

    # --- Other expression-related helpers can go here --- 