import os
import sys
import time
import re

from antlr4 import TerminalNode

from generated.OnionParser import OnionParser
from generated.OnionVisitor import OnionVisitor
from src.builtins import BuiltInFunctions
from src.exceptions import (OnionArgumentError, OnionAssignmentError, OnionDivisionByZeroError,
                           OnionEmptyListError, OnionIndexError, OnionInterpolationError, 
                           OnionLoopRangeError, OnionNameError, OnionOperationError, 
                           OnionPrintError, OnionRecursionError, OnionRuntimeError, 
                           OnionTimeoutError, OnionTypeError)
from src.symbol_table import SymbolTable

#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TypeChecker:
    """Handles type checking based on type declarations in the language."""
    
    @staticmethod
    def get_type_from_typedec(type_dec_node):
        """Extract the type name from a TypeDecContext."""
        if type_dec_node is None:
            return None
            
        # Type declaration format: ':' type
        # The type name is the second child after the colon
        if type_dec_node.getChildCount() >= 2:
            type_node = type_dec_node.getChild(1)
            return type_node.getText()
        return None
        
    @staticmethod
    def get_python_type(type_name):
        """Convert an Onion type name to a Python type."""
        if type_name is None:
            return None
        
        # Handle generic type for lists, e.g., 'list:int'
        if ":" in type_name:
            base_type, element_type = type_name.split(":", 1)
            if base_type.lower() == 'list':
                return list  # Return list type; element type checked separately
            
        # Basic types    
        type_map = {
            'int': int,
            'float': float, 
            'string': str,
            'bool': bool,
            'list': list,
            'void': type(None)
        }
        
        return type_map.get(type_name.lower())
    
    @staticmethod
    def get_element_type(type_name):
        """Extract element type for generic collections."""
        if type_name is None or ":" not in type_name:
            return None
            
        base_type, element_type = type_name.split(":", 1)
        if base_type.lower() == 'list':
            return element_type
            
        return None
        
    @staticmethod
    def check_type(value, expected_type_name):
        """Check if a value matches the expected type."""
        if expected_type_name is None:
            return True  # No type constraint
            
        # Handle generic types (e.g., 'list:int')
        if ":" in expected_type_name:
            base_type, element_type = expected_type_name.split(":", 1)
            
            # List with typed elements
            if base_type.lower() == 'list':
                # Check if value is a list
                if not isinstance(value, list):
                    return False
                
                # Check every element in the list
                for item in value:
                    if not TypeChecker.check_type(item, element_type):
                        return False
                return True
        
        # Normal type checking for basic types
        expected_type = TypeChecker.get_python_type(expected_type_name)
        if expected_type is None:
            # Unknown type, cannot check
            return True
            
        # Special case for None value with void type
        if value is None and expected_type is type(None):
            return True
            
        # Handle numeric type compatibility (int can be assigned to float)
        if expected_type is float and isinstance(value, int):
            return True
            
        return isinstance(value, expected_type)
        
    @staticmethod
    def type_error_message(value, expected_type_name):
        """Generate a type error message."""
        actual_type = type(value).__name__
        
        # For collections, include more specific information
        if isinstance(value, list) and value and ":" in expected_type_name:
            base_type, element_type = expected_type_name.split(":", 1)
            element_types = set(type(item).__name__ for item in value)
            actual_type = f"list of [{', '.join(element_types)}]"
            
        return f"Type error: Expected '{expected_type_name}', got '{actual_type}'"


class ReturnValue:
    """Lớp bọc giá trị trả về bởi lệnh return."""

    def __init__(self, value):
        super().__init__()
        self.value = value


class Lambda:
    """Represents a lambda function with captured environment."""
    
    def __init__(self, params, body_expr, capturing_interpreter):
        self.params = params
        self.body_expr = body_expr
        # Don't store the full interpreter, just capture the environment
        self.env = capturing_interpreter.env.clone()  # Capture the current environment

    def __call__(self, args, calling_interpreter=None):
        """Makes Lambda instances callable like regular functions."""
        if len(args) != len(self.params):
            raise OnionArgumentError(f"Lambda expected {len(self.params)} arguments, got {len(args)}")

        # Must use the calling interpreter, as we no longer store the capturing_interpreter
        if not calling_interpreter:
            raise OnionRuntimeError("Lambda requires a calling interpreter")
        
        interpreter = calling_interpreter
        
        # Save the current environment
        original_env = interpreter.env
        
        # Create a new environment based on the captured environment
        new_env = self.env.clone()
        new_env.push_scope()  # Add a new scope for parameters
        
        # Define parameters in the new scope
        for param, arg in zip(self.params, args):
            new_env.define(param, arg)
        
        try:
            # Set the interpreter's environment to our new environment
            interpreter.env = new_env
            
            # Evaluate the body expression
            return interpreter.visit(self.body_expr)
        finally:
            # Restore the original environment
            interpreter.env = original_env
    
    # Make Lambda pickle-friendly
    def __getstate__(self):
        """Return state values to be pickled."""
        return {
            'params': self.params,
            'body_expr': self.body_expr,
            'env': self.env
        }
    
    def __setstate__(self, state):
        """Restore state from the unpickled values."""
        self.params = state['params']
        self.body_expr = state['body_expr']
        self.env = state['env']
            
    def __str__(self):
        param_str = " ".join(self.params)
        return f"<lambda ({param_str})>"


class BaseInterpreter(OnionVisitor):
    def __init__(self):
        self.env = SymbolTable()
        self.functions = {}  # Lưu trữ các định nghĩa hàm
        self.start_time = time.time()  # Time when execution started
        self.max_execution_time = 300.0  # Default timeout: 5 minutes
        self.last_timeout_check = time.time()  # Track when we last checked timeout

    def check_timeout(self):
        """Check if execution has exceeded maximum time"""
        # Only check every 0.1 seconds to avoid excessive time.time() calls
        current_time = time.time()
        if current_time - self.last_timeout_check < 0.1:
            return  # Skip checking if less than 0.1 seconds passed since last check
            
        self.last_timeout_check = current_time
        if current_time - self.start_time > self.max_execution_time:
            raise OnionTimeoutError(f"Execution exceeded maximum time limit of {self.max_execution_time} seconds")

    def visitProgram(self, ctx):
        self.start_time = time.time()  # Reset timer at start of program
        result = None
        for stmt in ctx.statement():
            self.check_timeout()  # Check timeout before each statement
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
            
            # Determine if it's print or println based on the first child (token)
            op = ctx.getChild(0).getText()
            
            if op == "println":
                # println: print with trailing newline (default Python print behavior)
                print(value)
            else:
                # print: print without trailing newline
                print(value, end='', flush=True)
                if self.is_repl_mode:
                    print()  # Add a newline if in REPL mode
                
            return None
        except OnionRuntimeError as e:
            # Pass through Onion errors directly rather than wrapping them
            raise e
        except Exception as e:
            # Only wrap unexpected non-Onion errors
            raise OnionPrintError(f"Error in print statement: {str(e)}")

    def visitSetStmt(self, ctx: OnionParser.SetStmtContext):
        """Handles the \'set\' statement: (set IDENTIFIER expression)"""
        var_name = ctx.IDENTIFIER().getText()
        
        # Check if variable exists
        if self.env.lookup(var_name) is None:
            raise OnionNameError(f"Cannot set variable \'{var_name}\' because it has not been declared with \'let\'.")

        # Get the original type if declared (this is a simplification, full type tracking is complex)
        # For now, we rely on the TypeChecker within the assignment logic of SymbolTable or direct type checks.
        # A more robust solution would store type info in SymbolTable upon \'let\' declaration.
        original_value = self.env.lookup(var_name)
        original_type_name = None
        if isinstance(original_value, int): original_type_name = "int"
        elif isinstance(original_value, float): original_type_name = "float"
        elif isinstance(original_value, str): original_type_name = "string"
        elif isinstance(original_value, bool): original_type_name = "bool"
        elif isinstance(original_value, list): original_type_name = "list"
        # Not perfectly tracking \'void\' or complex list types here, but good for basic reassignment.

        new_value = self.visit(ctx.getChild(2)) # child(0)=\'set\', child(1)=IDENTIFIER, child(2)=expression or ternaryExpr

        # Type check if original type was inferred/known
        if original_type_name:
            if not TypeChecker.check_type(new_value, original_type_name):
                # Allow int to float promotion implicitly
                if original_type_name == "float" and isinstance(new_value, int):
                    pass # This is fine
                else:
                    raise OnionTypeError(
                        f"Cannot set \'{var_name}\': " +
                        TypeChecker.type_error_message(new_value, original_type_name)
                    )
        
        # Update the variable in the current or an outer scope
        # The SymbolTable.define method should handle finding and updating the variable.
        # If SymbolTable.define only adds to the current scope, we need SymbolTable.update or similar.
        # Assuming SymbolTable.define can update existing variables in outer scopes if found.
        self.env.define(var_name, new_value) # SymbolTable.define should overwrite if var_name exists
        return None # \'set\' is a statement, returns nothing

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
                        
                        # Handle type declaration if present
                        type_node = None
                        expr_node = None
                        closing_paren_idx = None
                        
                        next_idx = i + 2
                        if next_idx < ctx.getChildCount() and isinstance(ctx.getChild(next_idx), OnionParser.TypeDecContext):
                            type_node = ctx.getChild(next_idx)
                            next_idx += 1
                        
                        if next_idx < ctx.getChildCount():
                            expr_node = ctx.getChild(next_idx)
                            closing_paren_idx = next_idx + 1
                        
                        # Basic structural check for '(' IDENTIFIER (typeDec)? (expression | ternaryExpr) ')'
                        if isinstance(var_name_node, TerminalNode) and var_name_node.symbol.type == OnionParser.IDENTIFIER and \
                           (isinstance(expr_node, OnionParser.ExpressionContext) or isinstance(expr_node, OnionParser.TernaryExprContext)) and \
                           closing_paren_idx < ctx.getChildCount() and isinstance(ctx.getChild(closing_paren_idx), TerminalNode) and ctx.getChild(closing_paren_idx).getText() == ')':

                            var_name = var_name_node.getText()
                            var_value = self.visit(expr_node)
                            
                            # Check for redeclaration in the current scope
                            if self.env.lookup_current_scope(var_name) is not None:
                                raise OnionNameError(f"Variable '{var_name}' has already been declared in the current scope.")

                            # Type checking if type declaration present
                            if type_node is not None:
                                expected_type = TypeChecker.get_type_from_typedec(type_node)
                                if not TypeChecker.check_type(var_value, expected_type):
                                    raise OnionTypeError(TypeChecker.type_error_message(var_value, expected_type))
                                    
                            self.env.define(var_name, var_value)
                            result = var_value # Keep track of the last assigned value
                            i = closing_paren_idx # Move index past the processed pair ')'
                        else:
                             raise OnionAssignmentError(f"Malformed multi-assignment pair starting near index {i}")
                    else:
                        raise OnionAssignmentError(f"Incomplete multi-assignment pair starting near index {i}")
                
                i += 1 # Move to the next child, checking if it starts a pair
            return result # Return the value of the last assignment in the multi-let

        # Case 2: Single or Conditional assignment: 'let' IDENTIFIER ...
        # The second child is an IDENTIFIER
        elif isinstance(second_child, TerminalNode) and second_child.symbol.type == OnionParser.IDENTIFIER:
            identifier = second_child.getText() # Get identifier text
            
            # Check for typeDec
            type_dec = None
            next_index = 2
            if next_index < ctx.getChildCount() and isinstance(ctx.getChild(next_index), OnionParser.TypeDecContext):
                type_dec = ctx.getChild(next_index)
                next_index += 1
                
            # Get expression
            expr = ctx.getChild(next_index)
            if isinstance(expr, OnionParser.ExpressionContext) or isinstance(expr, OnionParser.TernaryExprContext):
                value = self.visit(expr)
                
                # Check for redeclaration in the current scope
                if self.env.lookup_current_scope(identifier) is not None:
                    raise OnionNameError(f"Variable '{identifier}' has already been declared in the current scope.")

                # Type checking if type declaration present
                if type_dec is not None:
                    expected_type = TypeChecker.get_type_from_typedec(type_dec)
                    if not TypeChecker.check_type(value, expected_type):
                        raise OnionTypeError(TypeChecker.type_error_message(value, expected_type))
                
                self.env.define(identifier, value)
                return value
            else:
                raise OnionAssignmentError(f"Expected expression after identifier '{identifier}'")
        else:
            # This case should theoretically not be reachable if the grammar is correct
            # and the input parses successfully.
            raise OnionAssignmentError("Unrecognized assignment structure")

    def visitAugmentedAssignment(self, ctx):
        """Handles augmented assignment operators (+=, -=, *=, /=)"""
        # Get operator type
        op = ctx.getChild(0).getText()
        # Get variable name
        var_name = ctx.IDENTIFIER().getText()
        # Get expression value
        expr_value = self.visit(ctx.expression())

        # Lookup current value
        current_value = self.env.lookup(var_name)
        if current_value is None:
            raise OnionNameError(f"Variable '{var_name}' is not defined")

        # Get the variable's type information if it exists
        var_type = None
        # We would need access to the original declaration to know the variable's type
        # For now, we'll infer based on the current value
        if isinstance(current_value, int):
            var_type = 'int'
        elif isinstance(current_value, float):
            var_type = 'float'
        elif isinstance(current_value, str):
            var_type = 'string'
        elif isinstance(current_value, bool):
            var_type = 'bool'
        elif isinstance(current_value, list):
            var_type = 'list'
            
        # Calculate new value based on operator
        if op == "+=":
            # Handle addition (works for numbers and strings)
            if isinstance(current_value, (int, float)) and isinstance(expr_value, (int, float)):
                new_value = current_value + expr_value
                
                # Preserve integer type if both are integers
                if var_type == 'int' and isinstance(expr_value, int):
                    new_value = int(new_value)
            elif isinstance(current_value, str) and isinstance(expr_value, str):
                new_value = current_value + expr_value
            else:
                raise OnionTypeError(f"Cannot apply '+=' with types {type(current_value).__name__} and {type(expr_value).__name__}")
        elif op == "-=":
            # Only numeric types
            if isinstance(current_value, (int, float)) and isinstance(expr_value, (int, float)):
                new_value = current_value - expr_value
                
                # Preserve integer type if both are integers
                if var_type == 'int' and isinstance(expr_value, int):
                    new_value = int(new_value)
            else:
                raise OnionTypeError(f"Cannot apply '-=' with types {type(current_value).__name__} and {type(expr_value).__name__}")
        elif op == "*=":
            # Handle multiplication (works for numbers and string*int)
            if isinstance(current_value, (int, float)) and isinstance(expr_value, (int, float)):
                new_value = current_value * expr_value
                
                # Preserve integer type if both are integers
                if var_type == 'int' and isinstance(expr_value, int):
                    new_value = int(new_value)
            elif isinstance(current_value, str) and isinstance(expr_value, int):
                new_value = current_value * expr_value
            else:
                raise OnionTypeError(f"Cannot apply '*=' with types {type(current_value).__name__} and {type(expr_value).__name__}")
        elif op == "/=":
            # Only numeric types
            if isinstance(current_value, (int, float)) and isinstance(expr_value, (int, float)):
                if expr_value == 0:
                    raise OnionDivisionByZeroError("Division by zero")
                new_value = current_value / expr_value
                
                # Preserve integer type for integer division if requested
                if var_type == 'int' and isinstance(expr_value, int):
                    new_value = int(new_value)
            else:
                raise OnionTypeError(f"Cannot apply '/=' with types {type(current_value).__name__} and {type(expr_value).__name__}")
        else:
            raise OnionRuntimeError(f"Unknown augmented assignment operator: {op}")
            
        # Ensure the resulting type is compatible with the variable's original type
        if var_type is not None:
            if not TypeChecker.check_type(new_value, var_type):
                raise OnionTypeError(f"Augmented assignment result: " + 
                                  TypeChecker.type_error_message(new_value, var_type))
        
        # Update the variable value
        self.env.define(var_name, new_value)
        
        # Return None instead of the new value to avoid unintentionally
        # returning values from functions with void return type
        return None

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
            # Get and execute then statements (after condition)
            then_statements = []
            condition_idx = -1
            
            # Find the index of the condition expression
            for i in range(ctx.getChildCount()):
                if isinstance(ctx.getChild(i), OnionParser.ExpressionContext):
                    condition_idx = i
                    break
            
            # Collect all statements after the condition until else or end
            i = condition_idx + 1
            while i < ctx.getChildCount():
                child = ctx.getChild(i)
                if isinstance(child, TerminalNode) and child.getText() == 'else':
                    break
                if isinstance(child, OnionParser.StatementContext):
                    then_statements.append(child)
                i += 1
                
            # Execute then statements
                result = None
            for stmt in then_statements:
                result = self.visit(stmt)
                if isinstance(result, ReturnValue):
                    break
            return result
        else:
            # Find and execute else statements if they exist
            else_statements = []
            else_idx = -1
            
            # Find the else token
            for i in range(ctx.getChildCount()):
                if isinstance(ctx.getChild(i), TerminalNode) and ctx.getChild(i).getText() == 'else':
                    else_idx = i
                    break
                    
            if else_idx != -1:
                # Collect statements after else
                for i in range(else_idx + 1, ctx.getChildCount()):
                    child = ctx.getChild(i)
                    if isinstance(child, OnionParser.StatementContext):
                        else_statements.append(child)
                
                # Execute else statements
                result = None
                for stmt in else_statements:
                    result = self.visit(stmt)
                    if isinstance(result, ReturnValue):
                        break
                return result
            else:
                return None

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

        # We should only have one expression (the element to append)
        if element_expr:
            element = self.visit(element_expr)
            lst.append(element)
                # Return None instead of the list to make append a void operation
            return None
        else:
            raise OnionArgumentError("append requires an element to append")


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
        if ctx.lambdaExpr():
            return self.visit(ctx.lambdaExpr())
        if ctx.filterExpr():
            return self.visit(ctx.filterExpr())
        if ctx.reduceExpr():
            return self.visit(ctx.reduceExpr())
        if ctx.mapExpr():
            return self.visit(ctx.mapExpr())
        return None

    def visitLiteral(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        if ctx.STRING():
            text = ctx.STRING().getText()
            # Regular string - just remove the quotes
            return text[1:-1]
        if ctx.FSTRING():
            text = ctx.FSTRING().getText()
            # Remove the 'f"' prefix and the ending quote
            text = text[2:-1]
            try:
                return self._interpolate_string(text)
            except Exception as e:
                raise OnionInterpolationError(f"String interpolation failed: {str(e)}")
        if ctx.BOOL():
            token = ctx.BOOL().getText()
            return token == "true"
        return None

    def _interpolate_string(self, text):
        """
        Interpolate variables in a string using (var) syntax.
        Similar to Python's f-strings but with parentheses instead of curly braces.
        """
        def replace_var(match):
            expr = match.group(1).strip()
            
            # Check for special cases like len
            if expr.startswith('len '):
                # Handle len function
                var_name = expr[4:].strip()  # Get the argument after 'len'
                value = self.env.lookup(var_name)
                if value is None:
                    raise OnionNameError(f"Variable '{var_name}' not found in string interpolation")
                if not isinstance(value, (list, str)):
                    raise OnionTypeError(f"Expected a list or string but got {type(value).__name__}")
                return str(len(value))
            
            # Handle nested expressions by checking if it contains spaces
            if ' ' in expr:
                # It's likely an expression, not just a variable name
                raise OnionInterpolationError(f"Complex expressions in string interpolation not supported: '{expr}'")
                
            # Look up the variable in the environment
            value = self.env.lookup(expr)
            if value is None:
                raise OnionNameError(f"Variable '{expr}' not found in string interpolation")
                
            # Convert the value to string
            return str(value)
            
        # Use regex to find and replace all (var) patterns
        pattern = r'\(([^)]+)\)'
        result = re.sub(pattern, replace_var, text)
        return result

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

    def visitLambdaExpr(self, ctx):
        """Handle lambda expressions: (lambda params body_expr)"""
        # Get parameter identifiers
        params = []
        for i in range(ctx.getChildCount()):
            if i > 0:  # Skip 'lambda' token
                child = ctx.getChild(i)
                if isinstance(child, OnionParser.ExpressionContext):
                    # Found the body expression
                    break
                elif hasattr(child, 'symbol') and child.symbol.type == OnionParser.IDENTIFIER:
                    params.append(child.getText())
        
        # Get the body expression
        body_expr = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, OnionParser.ExpressionContext):
                body_expr = child
                break
        
        if not body_expr:
            raise OnionRuntimeError("Lambda expression must have a body")
            
        # Create lambda function with current environment
        return Lambda(params, body_expr, self)


class ArithmeticVisitor(ExpressionVisitor):
    def visitArithmeticExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "+": self._handle_addition,
            "-": self._handle_subtraction,
            "*": self._handle_multiplication,
            "/": self._handle_division,
            "//": self._handle_integer_division,
            "%": self._handle_modulo,
        }
        return handlers[op](ctx)

    def _handle_addition(self, ctx):
        # Addition and string concatenation
        result = self.visit(ctx.getChild(1))
        for i in range(2, ctx.getChildCount()):
            value = self.visit(ctx.getChild(i))
            
            # String concatenation with any type
            if isinstance(result, str):
                # Convert any value to string for concatenation
                result = result + str(value)
            elif isinstance(value, str):
                # If the second operand is a string, convert the first to string too
                result = str(result) + value
            # Numeric addition
            elif isinstance(result, (int, float)) and isinstance(value, (int, float)):
                result = result + value
            else:
                raise OnionOperationError(
                    f"Cannot add values of type {type(result).__name__} and {type(value).__name__}"
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
        if ctx.getChildCount() < 2:
            raise ValueError("Multiplication requires at least one operand")
            
        # Get the first value
        result = self.visit(ctx.getChild(1))
        if result is None:
            raise ValueError("Cannot evaluate first multiplication operand")
            
        # If there's only one operand, just return it
        if ctx.getChildCount() == 2:
            return result
            
        # Process remaining operands
        for i in range(2, ctx.getChildCount()):
            value = self.visit(ctx.getChild(i))
            if value is None:
                raise ValueError(f"Cannot evaluate expression at position {i}")
                
            # Handle special case: string * number
            if isinstance(result, str) and isinstance(value, int):
                result = result * value
            # Handle special case: number * string
            elif isinstance(result, int) and isinstance(value, str):
                result = value * result
            # Regular numeric multiplication
            elif isinstance(result, (int, float)) and isinstance(value, (int, float)):
                result = result * value
            else:
                raise OnionOperationError(
                    f"Cannot multiply values of type {type(result).__name__} and {type(value).__name__}"
                )
                
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
            raise OnionDivisionByZeroError("Division by zero")
        return left / right

    def _handle_integer_division(self, ctx):
        if ctx.getChildCount() != 3:
            raise SyntaxError("Integer division requires exactly 2 operands")
        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        if left is None or right is None:
            raise ValueError("Cannot evaluate integer division operands")
        if right == 0:
            raise OnionDivisionByZeroError("Integer division by zero")
        return left // right

    def _handle_modulo(self, ctx):
        """Handle modulo operation: (% expr1 expr2)"""
        if ctx.getChildCount() != 3:
            raise SyntaxError("Modulo requires exactly 2 operands")
        left = self.visit(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        if left is None or right is None:
            raise ValueError("Cannot evaluate modulo operands")
        if right == 0:
            raise OnionDivisionByZeroError("Modulo by zero")
        
        # Ensure integer operands
        if not isinstance(left, int) or not isinstance(right, int):
            raise OnionTypeError(f"Modulo requires integer operands, got {type(left).__name__} and {type(right).__name__}")
        
        return left % right


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
        # Create an empty list
        result = []

        # Start from index 1 to skip the 'list' keyword
        start_idx = 1
        
        # Check for optional type declaration
        element_type = None
        if start_idx < ctx.getChildCount() and isinstance(ctx.getChild(start_idx), OnionParser.TypeDecContext):
            type_dec = ctx.getChild(start_idx)
            list_type = TypeChecker.get_type_from_typedec(type_dec)
            
            # Check if it's a generic list type (e.g., list:int)
            element_type = TypeChecker.get_element_type(list_type)
            
            # If no element type specified, it's just a basic list
            if element_type is None and list_type == 'list':
                element_type = None  # Any type allowed
                
            start_idx += 1
        
        # Process all expressions and add to list
        for i in range(start_idx, ctx.getChildCount()):
            child = ctx.getChild(i)
            child_value = self.visit(child)

            if child_value is None:
                raise ValueError(f"Cannot evaluate list element at position {i-start_idx}")
                
            # Type check list elements if a type was specified
            if element_type is not None:
                if not TypeChecker.check_type(child_value, element_type):
                    raise OnionTypeError(f"List element at position {i-start_idx}: " + 
                                        TypeChecker.type_error_message(child_value, element_type))

            result.append(child_value)
        return result

    def visitListOpExpr(self, ctx):
        op = ctx.getChild(0).getText()
        handlers = {
            "head": self._handle_head,
            "tail": self._handle_tail,
            "id": self._handle_getid,
            "len": self._handle_sizeof,
        }
        if op not in handlers:
            raise OnionNameError(f"Unknown list operation '{op}'")
        return handlers[op](ctx)

    def _handle_head(self, ctx):
        value = self._resolve_list_or_string(ctx, 0)
        self._validate_non_empty(value, "head")
        return value[0]

    def _handle_tail(self, ctx):
        value = self._resolve_list_or_string(ctx, 0)
        self._validate_non_empty(value, "tail")
        return value[1:]

    def _handle_getid(self, ctx):
        if len(ctx.expression()) < 2:
            raise OnionArgumentError("Requires an index and a list or string")
        index = self.visit(ctx.expression(0))
        if not isinstance(index, int):
            raise OnionTypeError(
                f"Index must be an integer, got {type(index).__name__}"
            )
        value = self.visit(ctx.expression(1))
        if not isinstance(value, (list, str)):
            raise OnionTypeError(f"Expected a list or string but got {type(value).__name__}")
        if index < 0 or index >= len(value):
            # Format a clear error message for out of bounds
            if len(value) == 0:
                raise OnionIndexError(f"Cannot access index {index} in an empty {type(value).__name__}")
            elif index < 0:
                raise OnionIndexError(f"Negative index {index} not allowed. Valid indices are 0 to {len(value)-1}")
            else:
                raise OnionIndexError(f"Index {index} out of range. Valid indices are 0 to {len(value)-1}")
        return value[index]

    def _handle_sizeof(self, ctx):
        value = self._resolve_list_or_string(ctx, 0)
        return len(value)
        
    def _resolve_list_or_string(self, ctx, expr_index):
        # Prefer explicit expression argument
        if len(ctx.expression()) > expr_index:
            value = self.visit(ctx.expression(expr_index))
        else:
            # Fallback: next token after op is an identifier
            var_name = ctx.getChild(expr_index + 1).getText()
            try:
                value = self.env.resolve(var_name)
            except NameError:
                raise OnionNameError(f"Variable '{var_name}' is not defined")
                
        # Check if it's a list or string
        if not isinstance(value, (list, str)):
            raise OnionTypeError(f"Expected a list or string but got {type(value).__name__}")
            
        return value

    def _validate_non_empty(self, value, op):
        if not value:
            value_type = "list" if isinstance(value, list) else "string"
            raise OnionEmptyListError(f"Cannot perform '{op}' on empty {value_type}")

    def visitFilterExpr(self, ctx):
        """Handle filter expression: (filter predicate_expr list_expr)"""
        expressions = ctx.expression()
        
        if len(expressions) != 2:
            raise OnionArgumentError("Filter requires exactly 2 expressions: predicate and list")
            
        # Get the predicate and list expressions
        pred_expr = expressions[0]
        list_expr = expressions[1]
        
        # Evaluate the list expression
        lst = self.visit(list_expr)
        
        if not isinstance(lst, list):
            raise OnionTypeError(f"Second argument of filter must be a list, got {type(lst).__name__}")
        
        # Handle direct lambda expression
        if isinstance(pred_expr, OnionParser.ExpressionContext) and pred_expr.compoundExpr() and \
           pred_expr.compoundExpr().lambdaExpr():
            # This is a lambda expression directly in the filter call
            lambda_expr = pred_expr.compoundExpr().lambdaExpr()
            result = []
            
            # Get lambda parameters
            params = []
            for i in range(lambda_expr.getChildCount()):
                if i > 0:  # Skip 'lambda' token
                    child = lambda_expr.getChild(i)
                    if isinstance(child, OnionParser.ExpressionContext):
                        break
                    elif hasattr(child, 'symbol') and child.symbol.type == OnionParser.IDENTIFIER:
                        params.append(child.getText())
            
            # Get the lambda body expression
            body_expr = None
            for i in range(lambda_expr.getChildCount()):
                child = lambda_expr.getChild(i)
                if isinstance(child, OnionParser.ExpressionContext):
                    body_expr = child
                    break
            
            if not body_expr or not params:
                raise OnionRuntimeError("Invalid lambda expression in filter")
            
            # Process each list item with the lambda
            for item in lst:
                # Push a new scope for this lambda execution
                self.env.push_scope()
                try:
                    # Define the parameter with the current list item
                    self.env.define(params[0], item)
                    
                    # Evaluate the lambda body in this scope to get boolean result
                    predicate_result = self.visit(body_expr)
                    if predicate_result:  # Filter in only items that evaluate to true
                        result.append(item)
                finally:
                    # Pop scope after processing this item
                    self.env.pop_scope()
            
            return result
        else:
            # Regular function reference
            predicate = self.visit(pred_expr)
            
            # Check if predicate is a Lambda
            if isinstance(predicate, Lambda):
                # Apply predicate to each list element
                result = []
                for item in lst:
                    # Call the lambda with the current interpreter
                    if predicate([item], self):
                        result.append(item)
                return result
            else:
                raise OnionTypeError("Filter predicate must be a lambda expression")
    
    def visitReduceExpr(self, ctx):
        """Handle reduce expression: (reduce op list)"""
        # Get the operator
        op_text = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if hasattr(child, 'getText') and child.getText() in ['+', '-', '*', '//']:
                op_text = child.getText()
                break
                
        if op_text is None:
            raise OnionRuntimeError("Reduce requires an operator (+, -, *, //)")
            
        # Get the list expression
        list_expr = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, OnionParser.ExpressionContext):
                list_expr = child
                break
                
        if list_expr is None:
            raise OnionRuntimeError("Reduce requires a list expression")
            
        # Get the list value
        lst = self.visit(list_expr)
        
        if not isinstance(lst, list):
            raise OnionTypeError(f"Reduce requires a list, got {type(lst).__name__}")
            
        if not lst:
            raise OnionRuntimeError("Cannot reduce an empty list")
            
        # Apply the operation cumulatively
        result = lst[0]
        for item in lst[1:]:
            if op_text == '+':
                result = result + item
            elif op_text == '-':
                result = result - item
            elif op_text == '*':
                result = result * item
            elif op_text == '//':
                if item == 0:
                    raise OnionDivisionByZeroError("Division by zero in reduce operation")
                result = result // item
                
        return result
        
    def visitMapExpr(self, ctx):
        """Handle map expression: (map function list)"""
        expressions = ctx.expression()
        
        if len(expressions) != 2:
            raise OnionArgumentError("Map requires exactly 2 expressions: function and list")
        
        # Get the function expression and list expression
        func_expr = expressions[0]
        list_expr = expressions[1]
        
        # Evaluate the list expression
        lst = self.visit(list_expr)
        
        if not isinstance(lst, list):
            raise OnionTypeError(f"Second argument of map must be a list, got {type(lst).__name__}")
        
        # Handle direct lambda expression
        if isinstance(func_expr, OnionParser.ExpressionContext) and func_expr.compoundExpr() and \
           func_expr.compoundExpr().lambdaExpr():
            # This is a lambda expression directly in the map call
            lambda_expr = func_expr.compoundExpr().lambdaExpr()
            result = []
            
            # Get lambda parameters (we need them for each list item)
            params = []
            for i in range(lambda_expr.getChildCount()):
                if i > 0:  # Skip 'lambda' token
                    child = lambda_expr.getChild(i)
                    if isinstance(child, OnionParser.ExpressionContext):
                        break
                    elif hasattr(child, 'symbol') and child.symbol.type == OnionParser.IDENTIFIER:
                        params.append(child.getText())
            
            # Get the lambda body expression
            body_expr = None
            for i in range(lambda_expr.getChildCount()):
                child = lambda_expr.getChild(i)
                if isinstance(child, OnionParser.ExpressionContext):
                    body_expr = child
                    break
            
            if not body_expr or not params:
                raise OnionRuntimeError("Invalid lambda expression in map")
            
            # Process each list item with the lambda
            for item in lst:
                # Push a new scope for this lambda execution
                self.env.push_scope()
                try:
                    # Define the parameter with the current list item
                    self.env.define(params[0], item)
                    
                    # Evaluate the lambda body in this scope
                    mapped_val = self.visit(body_expr)
                    result.append(mapped_val)
                finally:
                    # Pop scope after processing this item
                    self.env.pop_scope()
            
            return result
        else:
            # Regular function reference
            func = self.visit(func_expr)
            
            # Check if func is a Lambda
            if isinstance(func, Lambda):
                # Apply function to each list element
                result = []
                for item in lst:
                    # Call the lambda with the current interpreter
                    mapped_val = func([item], self)
                    result.append(mapped_val)
                return result
            else:
                raise OnionTypeError("Map function must be a lambda expression")


class ConditionalVisitor(BaseInterpreter):
    def visitIfExpr(self, ctx: OnionParser.IfExprContext):
        if_condition_expr = ctx.expression(0)
        if_condition_value = self.visit(if_condition_expr)
        self._assert_bool(if_condition_value, "if")

        current_child_index = 0
        for i in range(ctx.getChildCount()):
            if ctx.getChild(i) == if_condition_expr:
                current_child_index = i + 1
                break
        
        if_statements = []
        temp_idx_for_if_stmts = current_child_index
        while temp_idx_for_if_stmts < ctx.getChildCount():
            child = ctx.getChild(temp_idx_for_if_stmts)
            if isinstance(child, OnionParser.StatementContext):
                if_statements.append(child)
            elif isinstance(child, TerminalNode) and child.getText() == '(':
                break 
            temp_idx_for_if_stmts += 1
        current_child_index = temp_idx_for_if_stmts

        if if_condition_value:
            result = None
            for stmt_ctx in if_statements:
                result = self.visit(stmt_ctx)
                if isinstance(result, ReturnValue):
                    return result
            return result

        elif_expression_index_offset = 1
        
        processed_elif_or_else = False
        while current_child_index < ctx.getChildCount():
            child = ctx.getChild(current_child_index)
            if isinstance(child, TerminalNode) and child.getText() == '(':
                next_node_idx = current_child_index + 1
                if next_node_idx < ctx.getChildCount():
                    next_node_terminal = ctx.getChild(next_node_idx)
                    if isinstance(next_node_terminal, TerminalNode):
                        # Check for ELIF
                        if next_node_terminal.getText() == 'elif':
                            elif_condition_expr = ctx.expression(elif_expression_index_offset)
                            elif_condition_value = self.visit(elif_condition_expr)
                            self._assert_bool(elif_condition_value, "elif")
                            
                            elif_statements = []
                            temp_idx = current_child_index + 3 
                            while temp_idx < ctx.getChildCount():
                                inner_child = ctx.getChild(temp_idx)
                                if isinstance(inner_child, OnionParser.StatementContext):
                                    elif_statements.append(inner_child)
                                elif isinstance(inner_child, TerminalNode) and inner_child.getText() == ')':
                                    break
                                temp_idx += 1
                            
                            if elif_condition_value:
                                result = None
                                for stmt_ctx in elif_statements:
                                    result = self.visit(stmt_ctx)
                                    if isinstance(result, ReturnValue):
                                        return result
                                return result
                               
                            current_child_index = temp_idx + 1 
                            elif_expression_index_offset += 1
                            processed_elif_or_else = True
                            continue 

                        # Check for ELSE
                        elif next_node_terminal.getText() == 'else':
                            else_statements = []
                            temp_idx = current_child_index + 2 
                            while temp_idx < ctx.getChildCount():
                                inner_child = ctx.getChild(temp_idx)
                                if isinstance(inner_child, OnionParser.StatementContext):
                                    else_statements.append(inner_child)
                                elif isinstance(inner_child, TerminalNode) and inner_child.getText() == ')':
                                    break
                                temp_idx += 1
                            
                            result = None
                            for stmt_ctx in else_statements:
                                result = self.visit(stmt_ctx)
                                if isinstance(result, ReturnValue):
                                    return result
                            current_child_index = temp_idx + 1 
                            processed_elif_or_else = True
                            return result 
                    break 
            else:
                current_child_index += 1
        
        return None

    def visitBranchExpr(self, ctx: OnionParser.BranchExprContext):
        # For cond, each (condition statement) pair is evaluated
        # cond (expr stmt) (expr stmt) ... (t stmt)?
        num_pairs = (ctx.getChildCount() -1) // 3 # roughly, for ( expr stmt )
        
        current_child_idx = 1 # Skip initial 'cond' or '('
        
        while current_child_idx < ctx.getChildCount():
            node = ctx.getChild(current_child_idx)
            if isinstance(node, TerminalNode) and node.getText() == '(':
                # Start of a pair or the 't' clause
                next_node = ctx.getChild(current_child_idx + 1)
                if isinstance(next_node, TerminalNode) and next_node.getText() == 't':
                    # This is the default 't' clause
                    # ( t statement )
                    if current_child_idx + 2 < ctx.getChildCount() and isinstance(ctx.getChild(current_child_idx+2), OnionParser.StatementContext):
                        return self.visit(ctx.getChild(current_child_idx + 2))
                    else:
                        break # Malformed 't' clause
                elif isinstance(next_node, OnionParser.ExpressionContext):
                    # This is a (condition statement) pair
                    condition_expr = next_node
                    statement_node = ctx.getChild(current_child_idx + 2) if current_child_idx + 2 < ctx.getChildCount() else None
                    
                    if isinstance(statement_node, OnionParser.StatementContext):
                        cond_value = self.visit(condition_expr)
                        self._assert_bool(cond_value, "cond")
                        if cond_value:
                            return self.visit(statement_node)
                        # Move to the end of this pair: ( expr stmt )
                        current_child_idx += 4 
                    else:
                        break # Malformed pair
                else:
                    break # Unexpected structure inside 'cond'
            else:
                break # Top level of cond should be pairs or 't' clause
        return None

    def _assert_bool(self, value, construct):
        if not isinstance(value, bool):
            raise OnionTypeError(f"{construct} condition must be boolean, got {type(value).__name__}")


class LoopVisitor(BaseInterpreter):
    def visitLoopStatement(self, ctx):
        loop_type = ctx.getChild(0).getText()
        handlers = {
            "repeat": self._handle_repeat,
            "for": self._handle_for_loop,
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

        statements = self._get_loop_statements(ctx)
        
        result = None
        for _ in range(count):
            self.check_timeout() # Check timeout at the start of each iteration

            vars_in_scope_before_body = set(self.env.scopes[-1].keys())
            returned_from_iteration = False
            iteration_body_result = None

            try:
                for stmt in statements:
                    stmt_result = self.visit(stmt)
                    if isinstance(stmt_result, ReturnValue):
                        returned_from_iteration = True
                        result = stmt_result # Store ReturnValue to be propagated
                        break # Exit statements loop for this iteration
                    iteration_body_result = stmt_result
                
                if not returned_from_iteration:
                    result = iteration_body_result # Update overall loop result if iteration completed normally
            finally:
                # Clean up variables declared during this iteration
                vars_in_scope_after_body = set(self.env.scopes[-1].keys())
                newly_declared_in_body = vars_in_scope_after_body - vars_in_scope_before_body
                for var_to_remove in newly_declared_in_body:
                    if var_to_remove in self.env.scopes[-1]: # Ensure key exists before deleting
                        del self.env.scopes[-1][var_to_remove]
            
            if returned_from_iteration:
                return result # Propagate ReturnValue immediately

        return result

    def _handle_for_loop(self, ctx):
        # Get variable name or underscore (for anonymous iterator)
        var_node = ctx.getChild(2)
        if isinstance(var_node, TerminalNode):
            var_name = var_node.getText()
            if var_name == "_":
                # Anonymous iterator - we'll still need a variable name in the environment
                var_name = "_for_loop_anonymous_" + str(id(ctx))
        else:
            # This should be caught by the parser, but just in case
            raise OnionRuntimeError("Expected identifier or underscore in for loop")
        
        # Get expressions
        expressions = ctx.expression()
        
        # Handle the different cases of the for loop syntax
        # for (id/_ start:end step)
        if len(expressions) == 3:
            # All arguments provided: start, end, step
            start = self.visit(expressions[0])
            end = self.visit(expressions[1])
            step = self.visit(expressions[2])
        elif len(expressions) == 2:
            # Start and end provided, default step=1
            start = self.visit(expressions[0])
            end = self.visit(expressions[1])
            step = 1
        elif len(expressions) == 1:
            # Only end provided, default start=0, step=1
            start = 0
            end = self.visit(expressions[0])
            step = 1
        else:
            # This should be caught by the parser, but just in case
            raise OnionArgumentError(f"For loop expects 1-3 expressions, got {len(expressions)}")

        # Validate numeric arguments
        for val, name in ((start, "start"), (end, "end"), (step, "step")):
            if not isinstance(val, int):
                raise OnionTypeError(f"Loop {name} must be an integer")
        
        if step == 0:
            raise OnionLoopRangeError("Loop step cannot be zero")
            
        # Check for invalid range parameters
        if (step > 0 and start > end) or (step < 0 and start < end):
            raise OnionLoopRangeError(f"Loop will never execute with range({start}, {end}, {step})")

        # Get statements to execute in loop body
        statements = self._get_loop_statements(ctx)
        seq = range(start, end, step)

        # Safety check for very large ranges
        if len(seq) > 100000:
            raise OnionLoopRangeError(f"Range too large: {len(seq)} iterations")
                
        # Execute the loop
        result = None
        iteration_count = 0
        for current in seq:
            # Check timeout periodically
            iteration_count += 1
            if iteration_count % 1000 == 0: # Existing check
                    self.check_timeout()
                    
            self.env.define(var_name, current) # Define/update loop variable

            vars_in_scope_before_body = set(self.env.scopes[-1].keys())
            returned_from_iteration = False
            iteration_body_result = None

            try:
                for stmt in statements:
                    stmt_result = self.visit(stmt)
                    if isinstance(stmt_result, ReturnValue):
                        returned_from_iteration = True
                        result = stmt_result # Store ReturnValue
                        break # Exit statements loop
                    iteration_body_result = stmt_result
                
                if not returned_from_iteration:
                    result = iteration_body_result # Update loop's overall result
            finally:
                # Clean up variables declared during this iteration's body
                vars_in_scope_after_body = set(self.env.scopes[-1].keys())
                newly_declared_in_body = vars_in_scope_after_body - vars_in_scope_before_body
                for var_to_remove in newly_declared_in_body:
                    # The loop variable 'var_name' will be in vars_in_scope_before_body,
                    # so it won't be removed unless re-declared with 'let' inside the body.
                    if var_to_remove in self.env.scopes[-1]:
                        del self.env.scopes[-1][var_to_remove]

            if returned_from_iteration:
                return result # Propagate ReturnValue immediately
        
        return result

    def _handle_while(self, ctx):
        # Get condition expression
        cond_ctx = ctx.expression(0)

        # Get statements to execute in loop body
        statements = self._get_loop_statements(ctx)
        
        result = None 
        iterations = 0
        while True:
            self.check_timeout() 
                
            iterations += 1
            if iterations % 1000 == 0: 
                    self.check_timeout()
                    
            cond = self.visit(cond_ctx)
            if not isinstance(cond, bool):
                raise OnionTypeError("While condition must be boolean")
            if not cond:
                break
            
            vars_in_scope_before_iteration = set(self.env.scopes[-1].keys())
            _current_iteration_block_result = None 
            returned_from_iteration = False

            try:
                for stmt_node in statements: 
                    _val_from_stmt = self.visit(stmt_node) 
                    
                    if isinstance(_val_from_stmt, ReturnValue):
                        returned_from_iteration = True
                        result = _val_from_stmt # Store ReturnValue
                        break # Exit statements loop for this iteration
                    
                    _current_iteration_block_result = _val_from_stmt
                
                if not returned_from_iteration:
                    result = _current_iteration_block_result # Update loop's overall result
            finally:
                # Clean up variables declared during this iteration
                vars_in_scope_after_iteration = set(self.env.scopes[-1].keys())
                newly_declared_vars = vars_in_scope_after_iteration - vars_in_scope_before_iteration
                for var_name_to_remove in newly_declared_vars:
                    if var_name_to_remove in self.env.scopes[-1]:
                        del self.env.scopes[-1][var_name_to_remove]
            
            if returned_from_iteration:
                return result # Propagate ReturnValue immediately
        
        return result

    def _get_loop_statements(self, ctx):
        """Helper method to extract statements from a loop construct."""
        statements = []
        
        # Find the first expression node (condition/count)
        condition_idx = -1
        for i in range(ctx.getChildCount()):
            if isinstance(ctx.getChild(i), OnionParser.ExpressionContext):
                condition_idx = i
                break
                
        # Collect all statement nodes that come after the expressions
        expression_count = len(ctx.expression())
        start_idx = condition_idx + expression_count
        
        for i in range(start_idx, ctx.getChildCount()):
            if isinstance(ctx.getChild(i), OnionParser.StatementContext):
                statements.append(ctx.getChild(i))
                
        return statements


class FunctionVisitor(BaseInterpreter):
    def __init__(self):
        super().__init__()
        self.call_stack = []
        self.max_recursion_depth = 1000  # Set a reasonable default max recursion depth
    
    def visitFunctionDef(self, ctx):
        identifiers = ctx.IDENTIFIER()
        if not identifiers:
            return None

        name = identifiers[0].getText()
        
        # Extract parameter names and types
        params = []
        param_types = {}  # Store parameter types for type checking
        
        # Find parameter definitions
        i = 0
        while i < ctx.getChildCount():
            child = ctx.getChild(i)
            
            # Look for open parenthesis
            if isinstance(child, TerminalNode) and child.getText() == '(':
                # Process parameters inside parentheses
                j = i + 1
                while j < ctx.getChildCount():
                    param_child = ctx.getChild(j)
                    
                    # Check if we reached the closing parenthesis
                    if isinstance(param_child, TerminalNode) and param_child.getText() == ')':
                        i = j  # Skip to the closing parenthesis
                        break
                        
                    # Process parameter identifier
                    if isinstance(param_child, TerminalNode) and param_child.symbol.type == OnionParser.IDENTIFIER:
                        param_name = param_child.getText()
                        params.append(param_name)
                        
                        # Check for type declaration after parameter
                        if j + 1 < ctx.getChildCount() and isinstance(ctx.getChild(j + 1), OnionParser.TypeDecContext):
                            type_dec = ctx.getChild(j + 1)
                            param_type = TypeChecker.get_type_from_typedec(type_dec)
                            param_types[param_name] = param_type
                            j += 1  # Skip the type declaration
                    j += 1
            i += 1
        
        # Check for return type declaration
        # This would be after the parameter list and before the function body
        return_type = None  # Store return type
        
        # Look for return type after closing parenthesis
        for i in range(ctx.getChildCount()):
            if isinstance(ctx.getChild(i), TerminalNode) and ctx.getChild(i).getText() == ')':
                if i + 1 < ctx.getChildCount() and isinstance(ctx.getChild(i + 1), OnionParser.TypeDecContext):
                    type_dec = ctx.getChild(i + 1)
                    return_type = TypeChecker.get_type_from_typedec(type_dec)
                break
        
        # Get the body statements
        # The body consists of all statements after the function signature
        statements = []
        for i in range(ctx.getChildCount()):
            if isinstance(ctx.getChild(i), OnionParser.StatementContext):
                statements.append(ctx.getChild(i))
        
        # Store function definition with params, types, and body
        self.functions[name] = {
            "params": params,
            "param_types": param_types,
            "return_type": return_type,
            "body": statements  # Store statements directly instead of a block
        }
        return None

    def visitCallExpr(self, ctx):
        name = ctx.IDENTIFIER().getText()

        # Evaluate all arguments
        args = self._evaluate_arguments(ctx)

        if name in BuiltInFunctions.registry:
            return BuiltInFunctions.execute(name, self, args)

        elif name == "typeof":
            return self._handle_typeof(args)

        if name in self.functions:
            return self._handle_function_call(ctx, name, args)
            
        # Check if the identifier refers to a Lambda stored in a variable
        value = self.env.lookup(name)
        if isinstance(value, Lambda):
            return value(args, self)  # Call the lambda with the current interpreter

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
        # Check timeout before function execution
        self.check_timeout()
        
        # Check recursion depth
        if name in self.call_stack:
            # Count how many times this function appears in the call stack
            recursion_depth = sum(1 for func in self.call_stack if func == name)
            if recursion_depth >= self.max_recursion_depth:
                raise OnionRecursionError(f"Maximum recursion depth ({self.max_recursion_depth}) exceeded for function '{name}'")
        
        # Add function to call stack
        self.call_stack.append(name)
        
        try:
            function_def = self.functions[name]
            params = function_def["params"]
            statements = function_def["body"]  # Now it's a list of statements
            param_types = function_def.get("param_types", {})
            return_type = function_def.get("return_type")

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
                # Type check parameter value if type is defined
                if param in param_types:
                    expected_type = param_types[param]
                    if not TypeChecker.check_type(args[i], expected_type):
                        raise OnionTypeError(f"Parameter '{param}': " + 
                                           TypeChecker.type_error_message(args[i], expected_type))
                
                current_scope[param] = args[i]

            final_return_value = None
            # Execute each statement in the function body
            for stmt in statements:
                self.check_timeout()  # Check timeout during function execution
                stmt_result = self.visit(stmt)  # This might return a ReturnValue object
                
                if isinstance(stmt_result, ReturnValue):
                    final_return_value = stmt_result.value  # Extract the actual value
                    # Type check return value if return type is defined
                    if return_type:
                        if not TypeChecker.check_type(final_return_value, return_type):
                            raise OnionTypeError(f"Function '{name}' return value: " + 
                                              TypeChecker.type_error_message(final_return_value, return_type))
                    break  # Exit the loop immediately upon return
                elif stmt_result is not None:
                    # If no explicit return, the value of the last statement is used (like Lisp)
                    final_return_value = stmt_result

            # Pop scope before type checking final implicit return value
            self.env.pop_scope()

            # Check type of implicit return (if not already checked by explicit return)
            if return_type and not isinstance(final_return_value, ReturnValue):
                if not TypeChecker.check_type(final_return_value, return_type):
                    raise OnionTypeError(f"Function '{name}' return value: " + 
                                      TypeChecker.type_error_message(final_return_value, return_type))

            return final_return_value  # Return the determined value
        finally:
            # Remove function from call stack even if an exception occurs
            self.call_stack.pop()

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

    def visitReturnStmt(self, ctx):
        """Handle return statement and type checking for return values"""
        if ctx.getChildCount() > 1:
            expr = ctx.getChild(1)  # Phần tử thứ 2 (index 1) sau 'return'
            value = self.visit(expr)  # Triggers lookup if expr is identifier
            
            # Note: Type checking for return values is done in _handle_function_call
            # because that's where we have access to the function's return type
            return ReturnValue(value)
        return ReturnValue(None)

class Interpreter(
    # BaseInterpreter is inherited via other visitors
    ArithmeticVisitor,  # Inherits ExpressionVisitor -> BaseInterpreter
    BooleanVisitor,     # Inherits ExpressionVisitor -> BaseInterpreter
    ListVisitor,        # Inherits BaseInterpreter
    ConditionalVisitor, # Inherits BaseInterpreter
    LoopVisitor,        # Inherits BaseInterpreter
    FunctionVisitor     # Inherits BaseInterpreter
):
    def __init__(self, max_execution_time=300.0, max_recursion_depth=1000, is_repl_mode=True):
        # Ensure super().__init__() calls the correct chain
        super().__init__()
        # Initialize environment and built-ins specifically for Interpreter instance
        self.env = SymbolTable()
        self.call_stack = []  # Initialize call stack for recursion tracking
        self.max_recursion_depth = max_recursion_depth  # Set configurable max recursion depth
        self.max_execution_time = max_execution_time  # Set configurable execution time limit (300 seconds = 5 minutes)
        self.start_time = time.time()  # Reset timer at initialization
        self.visit_count = 0  # Counter to avoid checking timeout too frequently
        self.is_repl_mode = is_repl_mode  # Flag to indicate if we're running in REPL mode
        BuiltInFunctions.register_defaults()
        
    def visit(self, tree):
        """Override visit with error handling"""
        try:
            # Only check timeout occasionally to avoid performance impact
            self.visit_count += 1
            if self.visit_count % 1000 == 0:  # Only check every 1000 visits
                self.check_timeout()
                
            # The super().visit() will correctly traverse the MRO
            return super().visit(tree)
        except OnionRuntimeError as e:
            raise e
        except Exception as e:
            raise OnionRuntimeError(f"Runtime error: {str(e)}") from e