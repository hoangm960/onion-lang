import os
from src.parser import parse_input
from src.utils import beautify_parse_tree


TEST_DIR_INPUTS = "./examples"
TEST_DIR_OUTPUTS = "./tests/output/parsers"


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

        tree = parse_input(case)
        beautify_tree = beautify_parse_tree(tree)
        with open(output_file_path, "w") as f:
            f.write(beautify_tree)
        print(beautify_tree)


def run_all_test_files():
    filenames = next(os.walk(TEST_DIR_INPUTS), (None, None, []))[2]
    for filename in filenames:
        run_test_file(filename)


def main():
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
    main()