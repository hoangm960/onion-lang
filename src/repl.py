from src.interpreter import Interpreter
from src.parser import Parser
from generated.OnionParser import OnionParser
import os
import sys

class OnionREPL:
    """
    A REPL (Read-Evaluate-Print-Loop) for the Onion programming language.
    This REPL supports interactive evaluation of expressions and statements.
    """
    
    def __init__(self):
        self.interpreter = Interpreter(is_repl_mode=True)
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_help(self):
        """Display REPL usage help"""
        help_text = """
ONION REPL COMMANDS:
-------------------
- help              : Show this help message
- clear             : Clear the terminal screen
- reset             : Reset the interpreter (clear all variables)
- env               : Show current environment (variables)
- run <filename>    : Run an Onion program file
- exit, quit        : Exit the REPL

EXPRESSION EXAMPLES:
-----------------
- Arithmetic:       (+ 1 2 3), (- 10 5), (* 2 3 4), (/ 10 2)
- Variables:        (let x 5), (let y:int 10)
- Print:            (print "Hello"), (println x)
- Function calls:   (func arg1 arg2)
- String operations:(+ "Hello " "World"), (* "Hi" 3)
- List operations:  (head (list 1 2 3)), (len mylist)
- Conditionals:     (if (> x 10) "big" : "small")
"""
        print(help_text)
        
    def show_environment(self):
        """Display current variables in the environment"""
        # Get the top-level scope from the interpreter
        if not self.interpreter.env.scopes:
            print("Environment is empty.")
            return
            
        # Get the global scope (first scope in the stack)
        global_scope = self.interpreter.env.scopes[0]
        
        if not global_scope:
            print("No variables defined.")
            return
            
        print("Current variables:")
        print("------------------")
        for name, value in sorted(global_scope.items()):
            # Format the value based on its type
            if isinstance(value, str):
                formatted_value = f'"{value}"'
            elif isinstance(value, list):
                formatted_value = f"[{', '.join(map(str, value))}]"
            else:
                formatted_value = str(value)
                
            print(f"{name} = {formatted_value}")
    
    def run_file(self, filename):
        """Run an Onion program file"""
        try:
            # Add .onion extension if missing
            if not filename.endswith('.onion'):
                filename = filename + '.onion'
                
            # Support relative paths from tests/input directory
            if not os.path.isabs(filename) and not os.path.exists(filename):
                test_path = os.path.join('tests', 'input', filename)
                if os.path.exists(test_path):
                    filename = test_path
            
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' not found")
                return
                
            # Read the file content
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                
            # Parse the file
            parser = Parser()
            tree = parser.parse_input(content)
            
            if not tree:
                print(f"Error: Failed to parse '{filename}'")
                return
                
            # Execute the program in the current interpreter
            result = self.interpreter.visit(tree)
            if result is not None:
                print(f"Result: {result}")
                
        except Exception as e:
            print(f"Error executing '{filename}': {str(e)}")
        
    def parse_input(self, input_text):
        """
        Parse the input text, trying different strategies to make it user-friendly.
        1. Try parsing it as a full program (with statements)
        2. If that fails, try parsing as an expression
        3. If that fails too, try wrapping it in parentheses for a statement
        """
        parser = Parser()
        
        # First try to parse as a full program
        try:
            tree = parser.parse_input(input_text)
            if tree:
                return tree
        except Exception:
            pass  # Silently continue to next strategy
            
        # Next try to parse as an expression
        try:
            tree = parser.parse_expression(input_text)
            if tree:
                return tree
        except Exception:
            pass  # Silently continue to next strategy
            
        # Finally, try wrapping in parentheses if it's not already
        if not (input_text.startswith('(') and input_text.endswith(')')):
            try:
                wrapped_input = f"({input_text})"
                return parser.parse_input(wrapped_input)
            except Exception:
                pass  # Silently fail
                
        # All parsing strategies failed
        return None
        
    def start(self):
        """Start the Onion REPL"""
        print("🧅 Onion REPL - type 'exit' or Ctrl+C to quit")
        print("Type 'help' for available commands")
        
        while True:
            try:
                # Read input from user
                user_input = input("onion> ").strip()
                
                # Handle special commands
                if user_input.lower() in ('exit', 'quit'):
                    print("Goodbye!")
                    break
                elif user_input == "":
                    continue
                elif user_input.lower() == "help":
                    self.show_help()
                elif user_input.lower() == "clear":
                    self.clear_screen()
                elif user_input.lower() == "reset":
                    self.interpreter = Interpreter(is_repl_mode=True)
                    print("Interpreter state has been reset.")
                elif user_input.lower() == "env":
                    self.show_environment()
                elif user_input.lower().startswith("run "):
                    # Extract filename and run it
                    filename = user_input[4:].strip()
                    self.run_file(filename)
                else:
                    # Parse and evaluate the input
                    tree = self.parse_input(user_input)
                    
                    if tree:
                        try:
                            result = self.interpreter.visit(tree)
                            if result is not None:
                                print(result)
                        except Exception as e:
                            print(f"Error: {str(e)}")
                    else:
                        print("Error: Failed to parse input")
            
            except KeyboardInterrupt:
                print("\nBye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                
def main():
    repl = OnionREPL()
    repl.start()
    
if __name__ == "__main__":
    main()