import re
import os
from antlr4 import *
from OnionLexer import OnionLexer
from OnionParser import OnionParser

# Define the global variable for test file directory
# Set your test directory here (relative or absolute path)
TEST_DIR_INPUTS = "./tests/inputs"
TEST_DIR_OUTPUTS = "./tests/outputs"


def beautify_parse_tree(tree_str):
    tokens = re.findall(r'\(|\)|[^\s()]+', tree_str)

    def parse(tokens, depth=0):
        output = ""
        while tokens:
            token = tokens.pop(0)

            if token == '(':
                # Check for empty node and skip if found
                if tokens and tokens[0] == ')':
                    tokens.pop(0)
                    continue
                node = tokens.pop(0)
                output += " " * depth + f"{node}:\n"
                output += parse(tokens, depth + 1)
            elif token == ')':
                return output
            else:
                output += " " * depth + f"{token}{'' if tokens and tokens[0] == ')' else ':'}\n"
        return output

    return parse(tokens)

def parse_input(input_text):
    lexer = OnionLexer(InputStream(input_text))
    tokens = CommonTokenStream(lexer)
    parser = OnionParser(tokens)

    try:
        tree = parser.program()  # Replace with your actual entry rule
        str_tree = beautify_parse_tree(tree.toStringTree(recog=parser))
        return str_tree
    except Exception as e:
        print(f"Parse error: {e}")


def run_test_file(filename):
    # Use the global dir_name to form the full path
    input_file_path = os.path.join(TEST_DIR_INPUTS, filename)
    output_file_path = os.path.join(TEST_DIR_OUTPUTS, filename)

    if not os.path.exists(input_file_path):
        print(f"❌ File '{input_file_path}' not found.")
        return

    print(f"📄 Running test cases from '{input_file_path}':")
    with open(input_file_path, 'r') as f:
        test_code = f.read()

    # Each test block is separated by blank lines
    cases = [case.strip() for case in test_code.split("\n\n") if case.strip()]
    for i, case in enumerate(cases, start=1):
        print(f"\n[Test {i}]")
        print(f"Code:\n{case}")
        print(f"Output:")

        str_tree = parse_input(case)
        with open(output_file_path, "w") as f:
            f.write(str_tree)
        print(str_tree)

def run_all_test_files():
    filenames = next(os.walk(TEST_DIR_INPUTS), (None, None, []))[2]
    for filename in filenames:
        run_test_file(filename)

def repl():
    print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
    while True:
        try:
            line = input(">>> ").strip()
            tokens = line.split()
            command = tokens.pop()
            if command.lower() in ('exit', 'quit'):
                break
            elif command == "run":
                if tokens:
                    run_test_file(tokens.pop())
                else:
                    print("Usage: run filename.txt")
            elif command == "runall":
                run_all_test_files()
            elif command == "":
                continue
            else:
                result = parse_input(line)
                if result:  
                    print(result)
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    repl()
