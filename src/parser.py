from antlr4 import CommonTokenStream, InputStream
from generated import OnionLexer, OnionParser

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import traceback

class ParserError(Exception):
    """Custom exception for parser errors with detailed information"""
    def __init__(self, message, error_type=None, line=None, column=None, original_exception=None):
        self.message = message
        self.error_type = error_type
        self.line = line
        self.column = column
        self.original_exception = original_exception
        super().__init__(message)
        
    def __str__(self):
        if self.line and self.column:
            return f"{self.error_type} at line {self.line}, column {self.column}: {self.message}"
        return f"{self.error_type}: {self.message}"

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParserError(msg, error_type="Syntax error", line=line, column=column, original_exception=e)

class Parser():
    def __init__(self):
        self.parser = None
        self.tree = None
        self.last_error = None

    def parse_input(self, input_text):
        """Parse input as an Onion program"""
        try:
            lexer = OnionLexer(InputStream(input_text))
            tokens = CommonTokenStream(lexer)
            self.parser = OnionParser(tokens)

            self.parser.removeErrorListeners()
            self.parser.addErrorListener(CustomErrorListener())

            self.tree = self.parser.program()
            self.last_error = None
            return self.tree
        except ParserError as e:
            self.last_error = e
            return None
        except Exception as e:
            self.last_error = ParserError(str(e), error_type="Parser exception", original_exception=e)
            return None
            
    def parse_expression(self, input_text):
        """Parse input as an Onion expression (not a full program)"""
        try:
            # Create lexer and token stream
            lexer = OnionLexer(InputStream(input_text))
            tokens = CommonTokenStream(lexer)
            
            # Create parser with custom error listener
            self.parser = OnionParser(tokens)
            self.parser.removeErrorListeners()
            self.parser.addErrorListener(CustomErrorListener())
            
            # Parse as expression instead of program
            self.tree = self.parser.expression()
            self.last_error = None
            return self.tree
        except ParserError as e:
            self.last_error = e
            return None
        except Exception as e:
            self.last_error = ParserError(str(e), error_type="Parser exception", original_exception=e)
            return None

    def get_str_tree(self):
        return self.tree.toStringTree(recog=self.parser)
        
    def get_last_error(self):
        """Return the last error that occurred during parsing"""
        return self.last_error
