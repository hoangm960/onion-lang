from antlr4 import CommonTokenStream, InputStream
from generated import OnionLexer, OnionParser


class Parser():
    def __init__(self):
        self.parser = None
        self.tree = None

    def parse_input(self, input_text):
        try:
            lexer = OnionLexer(InputStream(input_text))
            tokens = CommonTokenStream(lexer)
            self.parser = OnionParser(tokens)

            self.tree = self.parser.program()
            return self.tree
        except Exception as e:
            print(f"Parse error: {e}")

    def get_str_tree(self):
        return self.tree.toStringTree(recog=self.parser)
