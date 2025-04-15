from src.interpreter import Interpreter
from src.parser import Parser


def main():
    interpreter = Interpreter()
    print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
    while True:
        try:
            line = input(">>> ").strip()
            tokens = line.split()
            if line.strip().lower() in ('exit', 'quit'):
                break
            elif line == "":
                continue
            else:
                parser = Parser()
                tree = parser.parse_input(line)
                interpreter.visit(tree)
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")
