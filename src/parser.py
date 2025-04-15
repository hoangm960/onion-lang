from antlr4 import CommonTokenStream, InputStream
from generated import OnionLexer, OnionParser


def parse_input(input_text):
    try:
        lexer = OnionLexer(InputStream(input_text))
        tokens = CommonTokenStream(lexer)
        parser = OnionParser(tokens)

        tree = parser.program()
        return tree.toStringTree(recog=parser)
    except Exception as e:
        print(f"Parse error: {e}")
