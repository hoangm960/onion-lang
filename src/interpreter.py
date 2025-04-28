import sys
from antlr4 import TerminalNode, ErrorNode, ParserRuleContext, FileStream, CommonTokenStream
from generated.OnionVisitor import OnionVisitor
from generated.OnionParser import OnionParser
from generated.OnionLexer import OnionLexer

# Import Analyzers and ReturnValue (now in statement_analyzer)
from src.expression_analyzer import ExpressionAnalyzer
from src.statement_analyzer import StatementAnalyzer, ReturnValue

from src.symbol_table import SymbolTable
from src.exceptions import (
    OnionRuntimeError,
    OnionNameError,
    OnionArgumentError,
    OnionTypeError,
    OnionPrintError
)
from src.builtins import BuiltInFunctions
import argparse
import traceback


class Interpreter(OnionVisitor):
    """
    Main Onion language interpreter.
    Delegates expression and statement analysis/execution to dedicated analyzer classes.
    Manages the environment, function/macro definitions, and overall execution flow.
    """
    def __init__(self):
        """Initializes the interpreter, environment, and analyzers."""
        super().__init__() # Initialize the base ANTLR visitor

        self.env = SymbolTable()
        self.functions = {}  # Stores user-defined function definitions
        self.macros = {}     # Stores user-defined macro definitions

        # Make ReturnValue class accessible via the instance
        self.ReturnValue = ReturnValue

        # Create analyzer instances, passing the interpreter instance itself
        self.expression_analyzer = ExpressionAnalyzer(self)
        self.statement_analyzer = StatementAnalyzer(self)

        # Register built-in functions
        BuiltInFunctions.register_defaults()

    def visit(self, tree):
        """
        Overrides the default visitor dispatch mechanism.
        Determines if the node is an expression or statement and delegates
        to the appropriate analyzer's specific visit method.

        Args:
            tree: The ANTLR ParseTree node to visit.

        Returns:
            The result of visiting the node.
        """
        if tree is None:
            return None

        # Get the specific visit method name based on the node type
        # e.g., for ArithmeticExprContext, method_name becomes 'visitArithmeticExpr'
        method_name = 'visit' + type(tree).__name__.replace('Context', '')
        visitor = None
        
        # Determine which analyzer handles this type of node
        # (Using isinstance checks based on analyzers' responsibilities)
        if isinstance(tree, (
            OnionParser.ExpressionContext,
            OnionParser.CompoundExprContext,
            OnionParser.LiteralContext,
            OnionParser.ArithmeticExprContext,
            OnionParser.BooleanExprContext,
            OnionParser.LogicalExprContext,
            OnionParser.ListExprContext,
            OnionParser.ListOpExprContext,
            OnionParser.CallExprContext,
            OnionParser.BranchExprContext, 
            OnionParser.TernaryExprContext 
        )):
            visitor = self.expression_analyzer
        elif isinstance(tree, (
            OnionParser.ProgramContext,
            OnionParser.StatementContext,
            OnionParser.StatementTypeContext,
            OnionParser.PrintStatementContext,
            OnionParser.AssignmentContext,
            OnionParser.BlockContext,
            OnionParser.ReturnStmtContext,
            OnionParser.AppendStmtContext,
            OnionParser.LoopStatementContext,
            OnionParser.FunctionDefContext,
            OnionParser.MacroDefContext,
            OnionParser.IfStmtContext,
            OnionParser.AugmentedAssignmentContext
        )):
            visitor = self.statement_analyzer
        elif isinstance(tree, TerminalNode):
            return None # Terminals usually don't need explicit visit actions
        elif isinstance(tree, ErrorNode):
            print(f"Interpreter encountered error node: {tree.getText()}", file=sys.stderr)
            raise OnionRuntimeError(f"Syntax Error near: {tree.getText()}")

        # If we identified an analyzer, try to call its specific visit method
        if visitor:
            visitor_method = getattr(visitor, method_name, None)
            if visitor_method:
                try:
                    return visitor_method(tree)
                except OnionRuntimeError as e:
                    raise e # Re-raise specific errors
                except (AttributeError, TypeError, ValueError, ZeroDivisionError, IndexError) as e:
                     # Catch common Python errors and wrap them
                     raise OnionRuntimeError(f"Runtime error in {type(tree).__name__}: {e}") from e
                except Exception as e:
                     # Catch any other unexpected errors
                     raise OnionRuntimeError(f"Unexpected runtime error visiting {type(tree).__name__}: {e}") from e
            else:
                 # Method not found on the designated analyzer - fallback or error?
                 # print(f"Warning: No specific visit method '{method_name}' found on {type(visitor).__name__} for {type(tree).__name__}. Using default visitChildren.")
                 return super().visitChildren(tree)
        else:
            # Node type not matched to any analyzer, use default ANTLR behavior
            # print(f"Warning: Unknown node type {type(tree).__name__}, using default visitChildren.")
            return super().visitChildren(tree)

    def execute_block(self, block_ctx: OnionParser.BlockContext):
        """
        Executes a block of statements, ensuring proper scoping.
        Delegates the actual scoped execution to the StatementAnalyzer.
        """
        # Call the scoped execution method on the statement analyzer instance.
        return self.statement_analyzer.execute_block_scoped(block_ctx)

