import os
from antlr4 import *
from OnionLexer import OnionLexer
from OnionParser import OnionParser
import sys

# Define the global variable for test file directory
dir_name = "./tests"  # Set your test directory here (relative or absolute path)

def parse_input(input_text):
    lexer = OnionLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    parser = OnionParser(tokens)

    try:
        tree = parser.program()  # Replace with your actual entry rule
        print(tree.toStringTree(recog=parser))
    except Exception as e:
        print(f"Parse error: {e}")

def run_test_file(filename):
    # Use the global dir_name to form the full path
    test_file_path = os.path.join(dir_name, filename)

    if not os.path.exists(test_file_path):
        print(f"❌ File '{test_file_path}' not found.")
        return

    print(f"📄 Running test cases from '{test_file_path}':")
    with open(test_file_path, 'r') as f:
        test_code = f.read()

    # Each test block is separated by blank lines
    cases = [case.strip() for case in test_code.split("\n\n") if case.strip()]
    for i, case in enumerate(cases, start=1):
        print(f"\n[Test {i}]")
        print(f"Code:\n{case}")
        parse_input(case)

def repl():
    print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
    while True:
        try:
            line = input(">>> ").strip()
            if line.lower() in ('exit', 'quit'):
                break
            elif line.startswith("RUN_TEST"):
                parts = line.split()
                if len(parts) == 2:
                    run_test_file(parts[1])
                else:
                    print("Usage: RUN_TEST filename.txt")
            elif line == "":
                continue
            else:
                parse_input(line)
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    repl()
