from antlr4 import CommonTokenStream, InputStream
from generated import OnionLexer, OnionParser

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Syntax error at line {line}, column {column}: {msg}")

class Parser():
    def __init__(self):
        self.parser = None
        self.tree = None

    def parse_input(self, input_text):
        try:
            lexer = OnionLexer(InputStream(input_text))
            tokens = CommonTokenStream(lexer)
            self.parser = OnionParser(tokens)

            self.parser.removeErrorListeners()
            self.parser.addErrorListener(CustomErrorListener())

            self.tree = self.parser.program()
            return self.tree
        except SyntaxError as e:
            print(e)
        except Exception as e:
            print(f"Parse error: {e}")

    def get_str_tree(self):
        return self.tree.toStringTree(recog=self.parser)
