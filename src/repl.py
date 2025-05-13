from src.interpreter import Interpreter
from src.parser import Parser
from generated.OnionParser import OnionParser
from src.utils import beautify_parse_tree
import os
import sys

def get_ast_as_string(tree, parser):
    """Generate a string representation of the AST for a given parse tree"""
    if tree:
        raw_tree = parser.get_str_tree()
        # Beautify the parse tree for better readability
        return beautify_parse_tree(raw_tree)
    return "No AST generated - parsing failed"

def run_onion_file(filename, interpreter, save_ast=False):
    """Execute an Onion file and optionally save its AST"""
    try:
        # Default to tests/input directory if only filename is provided
        if not os.path.isabs(filename) and os.path.dirname(filename) == '':
            default_dir = os.path.join('tests', 'input')
            filename = os.path.join(default_dir, filename)

        # Add .onion extension if missing
        if not filename.endswith('.onion'):
            filename = filename + '.onion'

        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found")
            return None

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        parser = Parser()
        tree = parser.parse_input(content)

        if tree:
            # Create AST output if requested
            if save_ast:
                # Create output directory if it doesn't exist
                output_dir = os.path.join('tests', 'output')
                os.makedirs(output_dir, exist_ok=True)

                # Create output filename
                base_filename = os.path.basename(filename)
                output_filename = os.path.join(output_dir,
                                              os.path.splitext(base_filename)[0] + '.ast.txt')

                # Save beautified AST to file
                ast_str = get_ast_as_string(tree, parser)
                with open(output_filename, 'w', encoding='utf-8') as out_file:
                    out_file.write(f"# AST for {base_filename}\n\n")
                    out_file.write(ast_str)

                print(f"Beautified AST saved to: {output_filename}")

            try:
                # Execute the code
                result = interpreter.visit(tree)

                # Print the result if it's meaningful
                if result is not None:
                    print(f"Result: {result}")

                return result
            except Exception as e:
                # Show a cleaner error message
                error_message = str(e)
                if error_message:
                    print(f"Error: {error_message}")
                else:
                    print(f"Error: {e.__class__.__name__}")
                
                # Uncomment for debugging
                # import traceback
                # traceback.print_exc()
                return None
        else:
            print("Failed to parse the file")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        # Uncomment for debugging
        # import traceback
        # traceback.print_exc()
        return None

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    """Display REPL usage help"""
    help_text = """
ONION REPL COMMANDS:
-------------------
- run <filename>       : Run a file from tests/input directory
                        (if only filename provided) or from custom path
                        Example: run binary_search_test

- clear                : Clear the terminal screen

- reset                : Reset the interpreter state (clear memory)

- help                 : Show this help message

- exit, quit           : Exit the REPL

CODE EXAMPLES:
------------
- Variable assignment  : (let x 5)
- Arithmetic           : (+ x 3)
- Print                : (print x)
- List                 : (list 1 2 3)
- Logical operations   : (& true false), (| true false)
"""
    print(help_text)

def main():
    interpreter = Interpreter()

    # Check if a file was specified as command line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        run_onion_file(filename, interpreter)
        return

    # Interactive mode
    print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
    print("Type 'help' for available commands")

    while True:
        try:
            line = input(">>> ").strip()
            tokens = line.split()

            if line.strip().lower() in ('exit', 'quit'):
                break
            elif line == "":
                continue
            elif line.lower() == "help":
                show_help()
            elif line.lower() == "clear":
                clear_screen()
            elif line.lower() == "reset":
                interpreter = Interpreter() # Re-initialize the interpreter
                print("Interpreter state has been reset.")
            elif line.lower().startswith("run "):
                # Extract filename from command
                filename = line[4:].strip()
                run_onion_file(filename, interpreter)
            else:
                # Try to parse and evaluate the line as Onion code
                parser = Parser()
                tree = parser.parse_input(line)
                if tree:
                    try:
                        result = interpreter.visit(tree)
                        if result is not None:
                            print(f"Result: {result}")
                    except Exception as e:
                        # Get the original error message without traceback
                        error_message = str(e)
                        if error_message:
                            print(f"Error: {error_message}")
                        else:
                            # If error message is empty, get the error class
                            print(f"Error: {e.__class__.__name__}")
                            
                        # Uncomment for debugging
                        # import traceback
                        # traceback.print_exc()
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            # Get the original error message without traceback
            error_message = str(e)
            if error_message:
                print(f"Error: {error_message}")
            else:
                # If error message is empty, get the error class
                print(f"Error: {e.__class__.__name__}")
                
            # Uncomment for debugging
            # import traceback
            # traceback.print_exc()

if __name__ == "__main__":
    main()
