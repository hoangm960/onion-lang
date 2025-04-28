# src/statement_analyzer.py

from generated.OnionParser import OnionParser
from antlr4 import TerminalNode
from src.exceptions import (
    OnionRuntimeError,
    OnionNameError,
    OnionArgumentError,
    OnionTypeError,
    OnionPrintError
)
# Needs SymbolTable if doing assignments/definitions directly, 
# but better to use interpreter's env
# from src.symbol_table import SymbolTable 

# Forward declaration for type hinting
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.interpreter import Interpreter

class ReturnValue:
    """ 
    Wrapper class for values explicitly returned using the 'return' statement.
    Used to differentiate between implicit block results and explicit returns,
    allowing loops and function calls to terminate early.
    """
    def __init__(self, value):
        self.value = value

class StatementAnalyzer:
    """
    Handles the analysis and execution of statement nodes in the Onion AST.
    Collaborates with the main Interpreter instance.
    """
    def __init__(self, interpreter: 'Interpreter'):
        """
        Initializes the StatementAnalyzer.

        Args:
            interpreter: The main Interpreter instance.
        """
        self.interpreter = interpreter
        # Assign ReturnValue to the interpreter instance for access by ExpressionAnalyzer
        self.interpreter.ReturnValue = ReturnValue 

    # --- Core Statement Visitors ---

    def visitProgram(self, ctx: OnionParser.ProgramContext):
        """Visits the root Program node, executing statements sequentially."""
        result = None
        # Iterate through all statement nodes in the program.
        for stmt_ctx in ctx.statement():
            # Delegate execution of each statement to the interpreter's visit method.
            result = self.interpreter.visit(stmt_ctx)
            # Check if a statement resulted in an explicit return (e.g., top-level return).
            # Depending on language semantics, a top-level return might stop execution.
            if isinstance(result, ReturnValue):
                # Return the wrapped value from the top-level return.
                return result.value # Or maybe just `break`?
        # Return the result of the last executed statement (or None if empty/no return).
        # If the last statement was a ReturnValue, we already returned its value.
        return result

    def visitStatement(self, ctx: OnionParser.StatementContext):
        """
        Visits a general Statement node, which wraps a specific statement type.
        Grammar: statement: LPAREN [SIFE]? statementType RPAREN
        It delegates to visiting the nested statementType, ignoring SIFE for now.
        """
        # Check for SIFE token (optional second child after LPAREN)
        has_sife = isinstance(ctx.getChild(1), TerminalNode) and ctx.getChild(1).symbol.type == OnionParser.SIFE
        
        # Get the statementType node (either 2nd or 3rd child)
        stmt_type_index = 2 if has_sife else 1
        stmt_type_node = ctx.getChild(stmt_type_index)

        if isinstance(stmt_type_node, OnionParser.StatementTypeContext):
            # TODO: Decide if SIFE should modify behavior - passed to visit?
            return self.interpreter.visit(stmt_type_node)
        else:
            raise OnionRuntimeError("Internal error: StatementContext parsed without a statementType child where expected.")

    def visitStatementType(self, ctx: OnionParser.StatementTypeContext):
        """
        Visits a StatementType node, which groups various specific statement kinds.
        Delegates to the actual statement node present (e.g., print, assignment).
        """
        # Check each possible child representing a specific statement type.
        if ctx.printStatement():
            return self.interpreter.visit(ctx.printStatement())
        elif ctx.assignment():
            return self.interpreter.visit(ctx.assignment())
        elif ctx.loopStatement():
            return self.interpreter.visit(ctx.loopStatement())
        elif ctx.functionDef():
            return self.interpreter.visit(ctx.functionDef())
        elif ctx.macroDef():
            return self.interpreter.visit(ctx.macroDef())
        elif ctx.returnStmt():
            return self.interpreter.visit(ctx.returnStmt())
        elif ctx.appendStmt():
            return self.interpreter.visit(ctx.appendStmt())
        elif ctx.augmentedAssignment():
             return self.interpreter.visit(ctx.augmentedAssignment())
        elif ctx.block(): # If block can be directly under statementType
            return self.interpreter.visit(ctx.block())
        elif ctx.ifStmt():
            return self.interpreter.visit(ctx.ifStmt())    
            
        # If none match, might be an empty statement or error.
        return None

    # --- Specific Statement Visitors ---

    def visitPrintStatement(self, ctx: OnionParser.PrintStatementContext):
        """Executes a print statement: (PRINT expr)."""
        # Check for PRINT token (optional, for robustness)
        if ctx.getChild(0).symbol.type != OnionParser.PRINT:
             raise OnionRuntimeError("Internal error: Expected PRINT token in print statement")
             
        try:
            # Evaluate the expression to be printed (second child).
            value = self.interpreter.visit(ctx.expression())
            # Use Python's print function for output.
            # TODO: Consider redirecting output or using a custom print function.
            print(value)
            # Print statements typically don't return a value in the language itself.
            return None
        except Exception as e:
            # Wrap potential evaluation errors in a specific print error.
            raise OnionPrintError(f"Error during print statement: {e}") from e

    def visitAssignment(self, ctx: OnionParser.AssignmentContext):
        """
        Executes an assignment statement: (LET name expr) or (LET (name1 val1) ...).
        Defines variables in the current environment scope.
        """
        # Check for LET token
        if ctx.getChild(0).symbol.type != OnionParser.LET:
             raise OnionRuntimeError("Internal error: Expected LET token in assignment statement")
             
        # Use getChild(1) to determine assignment type based on grammar structure.
        second_child = ctx.getChild(1)

        # Case 1: Multi-variable assignment (LET (name1 val1) (name2 val2) ...)
        # Detect by checking if the second child is an opening parenthesis '('.
        if isinstance(second_child, TerminalNode) and second_child.getText() == '(':
            last_assigned_value = None
            i = 1 # Start index after 'LET'
            while i < ctx.getChildCount():
                # Expecting an opening parenthesis for a pair.
                if isinstance(ctx.getChild(i), TerminalNode) and ctx.getChild(i).getText() == '(':
                    # Pair structure: '(', IDENTIFIER, expression, ')'
                    # Indices relative to the pair's '(': 0= (, 1=ID, 2=expr, 3= )
                    if i + 3 < ctx.getChildCount():
                        name_node = ctx.getChild(i + 1)
                        expr_node = ctx.getChild(i + 2)
                        close_paren = ctx.getChild(i + 3)

                        # Validate the structure of the pair.
                        # Check name is IDENTIFIER, expr is ExpressionContext, close is ')'.
                        # Note: Accessing parser.ruleNames is less robust than instanceof checks.
                        is_valid_pair = (
                            isinstance(name_node, TerminalNode) and 
                            name_node.symbol.type == OnionParser.IDENTIFIER and
                            isinstance(expr_node, OnionParser.ExpressionContext) and # Or other valid expr types?
                            isinstance(close_paren, TerminalNode) and 
                            close_paren.getText() == ')'
                        )

                        if is_valid_pair:
                            var_name = name_node.getText()
                            # Evaluate the expression for the value.
                            var_value = self.interpreter.visit(expr_node)
                            # Define the variable in the *current* scope using interpreter's env.
                            self.interpreter.env.define(var_name, var_value)
                            last_assigned_value = var_value # Track last value for return.
                            i += 4 # Move index past the processed pair ' ( id expr ) '
                        else:
                            raise OnionRuntimeError(f"Malformed variable assignment pair near: '...' {ctx.getText()[ctx.start.start:ctx.stop.stop]}")
                    else:
                        raise OnionRuntimeError(f"Incomplete variable assignment pair near: '...' {ctx.getText()[ctx.start.start:ctx.stop.stop]}")
                else:
                    # Move to the next token if it wasn't an opening parenthesis.
                    # This handles spaces or other tokens between pairs if grammar allows.
                    i += 1
            # Multi-assignment statement returns the value of the *last* assignment.
            return last_assigned_value

        # Case 2: Single variable assignment (LET name expr)
        # Detect by checking if the second child is an IDENTIFIER.
        elif isinstance(second_child, TerminalNode) and second_child.symbol.type == OnionParser.IDENTIFIER:
            var_name = second_child.getText()
            # Expect exactly one expression for the value.
            expressions = ctx.expression()
            if len(expressions) == 1:
                value = self.interpreter.visit(expressions[0])
                # Define in the current scope.
                self.interpreter.env.define(var_name, value)
                # Single assignment returns the assigned value.
                return value
            else:
                # Should be caught by parser if grammar is correct.
                raise OnionRuntimeError(f"Assignment for '{var_name}' expects 1 value expression, found {len(expressions)}")
        
        # Case 3: Error - Unrecognized assignment structure.
        else:
            raise OnionRuntimeError("Unrecognized assignment statement structure")

    def visitBlock(self, ctx: OnionParser.BlockContext):
        """
        Executes a block of statements. Usually introduces a new scope.
        Returns the value of the last statement executed, or ReturnValue if encountered.
        """
        # Delegate block execution to the interpreter's helper method,
        # which handles scoping and result propagation.
        return self.interpreter.execute_block(ctx)


    def visitReturnStmt(self, ctx: OnionParser.ReturnStmtContext):
        """
        Handles a return statement: (RETURN [expr]).
        Wraps the evaluated expression (or None) in a ReturnValue object.
        """
        # Check for RETURN token
        if ctx.getChild(0).symbol.type != OnionParser.RETURN:
            raise OnionRuntimeError("Internal error: Expected RETURN token in return statement")
            
        value = None
        # Expression is the second child (index 1)
        if ctx.expression():
            # Evaluate the expression to be returned.
            value = self.interpreter.visit(ctx.expression())
        # Wrap the result (or None) in ReturnValue to signal an explicit return.
        return ReturnValue(value)

    def visitAppendStmt(self, ctx: OnionParser.AppendStmtContext):
        """
        Executes an append statement: (APPEND list_var element_expr).
        Modifies the list in-place.
        """
        # Check for APPEND token
        if ctx.getChild(0).symbol.type != OnionParser.APPEND:
             raise OnionRuntimeError("Internal error: Expected APPEND token in append statement")
             
        var_name = ctx.IDENTIFIER().getText()
        element_expr = ctx.expression()

        # Look up the list variable in the environment.
        lst = self.interpreter.env.lookup(var_name)

        if lst is None:
            raise OnionNameError(f"Cannot append: list variable '{var_name}' is not defined")
        if not isinstance(lst, list):
            raise OnionTypeError(f"Variable '{var_name}' must be a list to append, but it is {type(lst).__name__}")

        # Evaluate the element to be appended.
        element = self.interpreter.visit(element_expr)

        # Perform the append operation (modifies the list object).
        lst.append(element)

        # Append statements typically don't return a value.
        return None

    def visitIfStmt(self, ctx: OnionParser.IfStmtContext):
        """
        Visits an 'if' statement: (if condition_expr then_block [(elif cond_expr block)]* [else block]).
        Evaluates conditions sequentially and executes the corresponding block.
        Uses generated accessor methods (e.g., ctx.expression(), ctx.block()).
        Statements typically return None, unless the executed block contains a 'return'.
        """
        # 1. Check the main 'if' condition
        if_condition_ctx = ctx.expression(0) # First expression is the main condition
        if not if_condition_ctx:
            raise OnionRuntimeError("Missing condition for 'if' statement") 
            
        if_condition = self.interpreter.visit(if_condition_ctx)
        # Need to access _assert_bool, let's assume it's available via interpreter or moved here.
        # Simplest: access via expression_analyzer held by interpreter.
        self.interpreter.expression_analyzer._assert_bool(if_condition, "if statement condition")

        if if_condition:
            # If condition is true, execute the 'then' block (first block)
            then_block_ctx = ctx.block(0)
            if then_block_ctx:
                return self.interpreter.visit(then_block_ctx) # Execute block
            else:
                raise OnionRuntimeError("Missing block for 'if' statement")

        # 2. Check 'elif' conditions (if any)
        elif_conditions = ctx.expression()[1:] # Skip the first (main if) condition
        all_blocks = ctx.block() # Get all blocks
        then_block = all_blocks[0]
        elif_else_blocks = all_blocks[1:] # Blocks for elif/else

        num_elifs = 0
        for i in range(len(elif_conditions)):
            # Ensure there's a corresponding block for this elif condition
            if i < len(elif_else_blocks):
                num_elifs += 1
                elif_cond_ctx = elif_conditions[i]
                elif_block_ctx = elif_else_blocks[i]

                condition = self.interpreter.visit(elif_cond_ctx)
                self.interpreter.expression_analyzer._assert_bool(condition, f"elif statement condition {i+1}")

                if condition:
                    # Execute the corresponding elif block and return its result
                    return self.interpreter.visit(elif_block_ctx)
            else:
                # This indicates a potential mismatch if loop continues
                break 

        # 3. Check for 'else' block
        # The else block is the last block if it exists beyond the elif blocks
        if len(elif_else_blocks) > num_elifs:
            # Need to check the 'else' keyword inside the parenthesis
            # Find the start index of the potential else block structure
            potential_else_paren_idx = -1
            last_elif_end_idx = ctx.expression(num_elifs).stop.tokenIndex if num_elifs > 0 else ctx.expression(0).stop.tokenIndex
            # Search for '(' after the last elif expression (or the if expression)
            for k in range(len(ctx.children)):
                 if isinstance(ctx.children[k], TerminalNode) and ctx.children[k].symbol.tokenIndex > last_elif_end_idx:
                      if ctx.children[k].symbol.type == OnionParser.LPAREN:
                           potential_else_paren_idx = k
                           break
                           
            if potential_else_paren_idx != -1 and \
               potential_else_paren_idx + 1 < len(ctx.children) and \
               isinstance(ctx.children[potential_else_paren_idx + 1], TerminalNode) and \
               ctx.children[potential_else_paren_idx + 1].symbol.type == OnionParser.ELSE:
                
                else_block_ctx = elif_else_blocks[num_elifs] # The block after the last elif
                return self.interpreter.visit(else_block_ctx)

        # 4. No condition met, no else block executed
        return None # If statement itself doesn't return a value

    # --- Loop Statements ---

    def visitLoopStatement(self, ctx: OnionParser.LoopStatementContext):
        """
        Visits a loop statement node, delegating to specific loop types.
        Handles 'repeat', 'loop' (for), and 'while'.
        """
        # Determine the loop type from the first child token.
        loop_type_token = ctx.getChild(0).symbol.type
        handlers = {
            OnionParser.REPEAT: self._handle_repeat,
            OnionParser.LOOP: self._handle_for_loop,
            OnionParser.WHILE: self._handle_while,
        }
        if loop_type_token in handlers:
            # Call the appropriate handler method.
            return handlers[loop_type_token](ctx)
        else:
            loop_text = ctx.getChild(0).getText()
            raise OnionNameError(f"Internal error: Unknown loop type '{loop_text}'")

    def _handle_repeat(self, ctx):
        """
        Executes a 'repeat' loop: (repeat count_expr block).
        Executes the block a fixed number of times.
        """
        # Evaluate the repeat count expression.
        count = self.interpreter.visit(ctx.expression(0))
        if not isinstance(count, int):
            raise OnionTypeError(f"Repeat loop count must be an integer, got {type(count).__name__}")
        if count < 0:
            raise OnionRuntimeError("Repeat loop count cannot be negative")

        # Get the block to execute.
        # Assuming block is the last child after 'repeat' and count expression.
        block_node = ctx.block()
        if not block_node:
             raise OnionRuntimeError("Repeat loop requires a block to execute")

        # Execute the block 'count' times.
        last_result = None
        for _ in range(count):
            # Visit the block for each iteration.
            result = self.interpreter.visit(block_node)
            # Check for early exit via 'return'.
            if isinstance(result, ReturnValue):
                return result # Propagate the return value immediately.
            last_result = result # Keep track of the last non-return result.
            
        # Return the result of the last iteration (or None if count was 0).
        return last_result

    def _handle_for_loop(self, ctx):
        """
        Executes a 'loop' (for-style) loop: (loop var start end [step] block).
        Iterates over a range, assigning the value to 'var' in each iteration.
        """
        var_name = ctx.IDENTIFIER().getText()
        expressions = ctx.expression() # range arguments
        num_args = len(expressions)
        block_node = ctx.block()

        if not block_node:
             raise OnionRuntimeError("For loop requires a block to execute")

        # Determine range parameters based on the number of expression arguments.
        start, end, step = 0, 0, 1 # Defaults
        try:
            if num_args == 1:
                end = self.interpreter.visit(expressions[0])
            elif num_args == 2:
                start = self.interpreter.visit(expressions[0])
                end = self.interpreter.visit(expressions[1])
            elif num_args == 3:
                start = self.interpreter.visit(expressions[0])
                end = self.interpreter.visit(expressions[1])
                step = self.interpreter.visit(expressions[2])
            else:
                raise OnionArgumentError(f"For loop ('loop') range expects 1, 2, or 3 arguments, got {num_args}")
        except Exception as e:
             raise OnionRuntimeError(f"Error evaluating loop range arguments: {e}") from e

        # Validate types of range parameters.
        if not all(isinstance(v, int) for v in [start, end, step]):
            raise OnionTypeError("Loop range arguments (start, end, step) must be integers")
        if step == 0:
            raise OnionRuntimeError("Loop step cannot be zero")

        # --- Loop Execution --- 
        last_result = None
        # Create the range iterator.
        loop_range = range(start, end, step)
        
        # Introduce a scope for the loop variable? Optional, depends on language rules.
        # If var should be local to the loop, push/pop scope here.
        # self.interpreter.env.push_scope() 
        try:
            for i in loop_range:
                # Define/update the loop variable in the current scope for this iteration.
                self.interpreter.env.define(var_name, i)
                # Execute the loop body.
                result = self.interpreter.visit(block_node)
                # Check for early exit via 'return'.
                if isinstance(result, ReturnValue):
                    return result # Propagate return immediately.
                last_result = result # Track last non-return result.
        finally:
            # If scope was pushed, pop it here.
            # self.interpreter.env.pop_scope()
            pass # No scope push/pop in this version

        # Return the result of the last iteration (or None if range was empty).
        return last_result

    def _handle_while(self, ctx):
        """
        Executes a 'while' loop: (while condition_expr block).
        Repeatedly executes the block as long as the condition is true.
        """
        cond_expr = ctx.expression(0)
        block_node = ctx.block()

        if not block_node:
             raise OnionRuntimeError("While loop requires a block to execute")

        last_result = None
        while True:
            # Evaluate the condition expression in each iteration.
            condition = self.interpreter.visit(cond_expr)
            if not isinstance(condition, bool):
                raise OnionTypeError(f"While loop condition must evaluate to a boolean, got {type(condition).__name__}")

            # Exit loop if condition is false.
            if not condition:
                break

            # Execute the loop body.
            result = self.interpreter.visit(block_node)
            # Check for early exit via 'return'.
            if isinstance(result, ReturnValue):
                return result # Propagate return immediately.
            last_result = result # Track last non-return result.

        # Return the result of the last iteration (or None if loop never ran).
        return last_result

    # --- Function and Macro Definitions ---

    def visitFunctionDef(self, ctx: OnionParser.FunctionDefContext):
        """
        Handles a function definition: (def name (param1 param2...) block).
        Stores the function definition in the interpreter's function registry.
        """
        # Check for DEF token
        if ctx.getChild(0).symbol.type != OnionParser.DEF:
             raise OnionRuntimeError("Internal error: Expected DEF token in function definition")
             
        identifiers = ctx.IDENTIFIER() # Get all IDENTIFIER nodes.
        if not identifiers:
             # Should be caught by parser if grammar requires a name.
             raise OnionRuntimeError("Function definition requires at least a name")

        # First IDENTIFIER is the function name.
        name = identifiers[0].getText()
        # Subsequent IDENTIFIERs are parameter names.
        params = [ident.getText() for ident in identifiers[1:]]
        # The function body is the BlockContext node.
        body = ctx.block()

        if not body:
             raise OnionRuntimeError(f"Function definition '{name}' requires a body block")

        # Store the function details (parameters and body AST node) 
        # in the interpreter's function storage.
        self.interpreter.functions[name] = {
            "params": params,
            "body": body # Store the actual context node
        }
        # Function definitions typically don't return a value themselves.
        return None

    def visitMacroDef(self, ctx: OnionParser.MacroDefContext):
        """
        Handles a macro definition: (macro name (param1 param2...) block).
        Stores the macro definition in the interpreter's macro registry.
        """
        # Check for MACRO token
        if ctx.getChild(0).symbol.type != OnionParser.MACRO:
             raise OnionRuntimeError("Internal error: Expected MACRO token in macro definition")
             
        identifiers = ctx.IDENTIFIER()
        if not identifiers:
             raise OnionRuntimeError("Macro definition requires at least a name")

        name = identifiers[0].getText()
        params = [ident.getText() for ident in identifiers[1:]]
        body = ctx.block()

        if not body:
             raise OnionRuntimeError(f"Macro definition '{name}' requires a body block")

        # Store macro details in the interpreter's macro storage.
        self.interpreter.macros[name] = {
            "params": params,
            "body": body
        }
        # Macro definitions typically don't return a value.
        return None

    def visitAugmentedAssignment(self, ctx: OnionParser.AugmentedAssignmentContext):
        """Executes augmented assignment (+=, -=, *=, /=)."""
        op_type = ctx.getChild(0).symbol.type
        var_name = ctx.IDENTIFIER().getText()
        expr_ctx = ctx.expression() or ctx.ternaryExpr() # Get the expression

        if not expr_ctx:
             raise OnionRuntimeError("Missing expression in augmented assignment")

        # 1. Look up current value
        current_value = self.interpreter.env.lookup(var_name)
        if current_value is None:
            raise OnionNameError(f"Variable '{var_name}' used in augmented assignment is not defined")

        # 2. Evaluate the right-hand side expression
        rhs_value = self.interpreter.visit(expr_ctx)

        # 3. Perform the operation
        new_value = None
        op_map = { 
            OnionParser.PLUS_EQUALS: lambda a, b: a + b,
            OnionParser.MINUS_EQUALS: lambda a, b: a - b,
            OnionParser.MULT_EQUALS: lambda a, b: a * b,
            OnionParser.DIV_EQUALS: lambda a, b: a / b, # Consider ZeroDivisionError
        }

        if op_type in op_map:
            try:
                # Special handling for division by zero
                if op_type == OnionParser.DIV_EQUALS and rhs_value == 0:
                     raise OnionRuntimeError("Division by zero in augmented assignment (/=)")
                new_value = op_map[op_type](current_value, rhs_value)
            except TypeError as e:
                 raise OnionTypeError(f"Type error during augmented assignment for '{var_name}': {e}") from e
            except Exception as e:
                 raise OnionRuntimeError(f"Error during augmented assignment for '{var_name}': {e}") from e
        else:
            raise OnionRuntimeError(f"Internal error: Unknown augmented assignment operator type")

        # 4. Update the variable in the environment
        # Use assign method if available for potentially updating existing scope
        if not self.interpreter.env.lookup(var_name):
             # If assign fails (e.g., var doesn't exist), raise error
             # This differs from `define` which always puts in current scope
             raise OnionNameError(f"Failed to assign to '{var_name}' in augmented assignment (was it defined?)")
        self.interpreter.env.define(var_name, new_value)
        # Augmented assignments typically return None (or maybe the new value? Choose semantics)
        return None

    # --- Block Execution Helper (used by interpreter) ---
    # This method lives here conceptually, but might be called by the main interpreter.

    def execute_block_scoped(self, block_ctx: OnionParser.BlockContext):
        """
        Executes a block of statements within a new scope.
        Pushes a scope before execution and pops it after.
        Returns the result of the last statement or a ReturnValue if encountered.
        
        Args:
            block_ctx: The BlockContext node to execute.
            
        Returns:
            The result of the block execution (value of last statement or ReturnValue).
        """
        if not block_ctx: # Handle empty or non-existent blocks gracefully.
             return None
             
        self.interpreter.env.push_scope() # Create a new scope for the block.
        last_result = None
        try:
            # Iterate through all statements within the block.
            for i in range(block_ctx.getChildCount()):
                stmt_ctx = block_ctx.getChild(i)
                # Delegate execution of each statement back to the interpreter.
                result = self.interpreter.visit(stmt_ctx)
                
                # Check for explicit return.
                if isinstance(result, ReturnValue):
                    # If return encountered, stop block execution and return the ReturnValue wrapper.
                    return result 
                    
                # Keep track of the result of the last executed statement (for implicit return).
                # Filter out None results unless it's the only result? Depends on language rules.
                # Simple approach: always store the last result.
                last_result = result
        finally:
            self.interpreter.env.pop_scope() # Ensure scope is popped even if errors occur.
            
        # Return the result of the last statement executed in the block.
        return last_result
        
    # --- Other statement-related helpers can go here --- 