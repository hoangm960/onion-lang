import os
from src.interpreter import Interpreter
from src.parser import Parser
from src.utils import beautify_parse_tree

TEST_DIR_INPUTS = "./tests/parsers/input"
TEST_DIR_OUTPUTS = "./tests/parsers/output"


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
    parser = Parser()
    for i, case in enumerate(cases, start=1):
        print(f"\n[Test {i}]")
        print(f"Code:\n{case}")
        print(f"Output:")

        parser.parse_input(case)
        beautify_tree = beautify_parse_tree(parser.get_str_tree())
        with open(output_file_path, "w") as f:
            f.write(beautify_tree)
        print(beautify_tree)


def run_all_test_files():
    filenames = next(os.walk(TEST_DIR_INPUTS), (None, None, []))[2]
    for filename in filenames:
        run_test_file(filename)

if __name__ == "__main__":
    while True:
        try:
            user_input = input(">>> ")
            tokens = user_input.strip().split()
            command = tokens.pop()
            if command in ["quit", "exit"]:
                break
            if command == "run":
                if tokens:
                    test_file = tokens.pop()
                    run_test_file(test_file)
                else:
                    print("Usage: run [filename].txt")
            elif command == "runall":
                run_all_test_files()
            else:
                print(f"Command '{command}' is not recognized!")
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"Error: {e}")