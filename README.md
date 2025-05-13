# Onion
## Objective
- Document writing
- Language features
    - Variables (including arrays)
    - Expressions
    - Condition statements
    - Loop statements
    - Printing variable
    - Error handling: Type mismatch (including if/for condition), divide-by-zero, index out of bound.
## Folder Structure
```bash
onion-lang/
├── grammar/
│   └── Onion.g4
├── generated/           # Generated parser files from ANTLR4
│   ├── __init__.py
│   ├── OnionLexer.py
│   ├── OnionParser.py
│   └── OnionVisitor.py
├── src/                 # Main source code
│   ├── __init__.py
│   ├── parser.py        # Module to load parser
│   ├── interpreter.py   # Module for interpreter
│   ├── symbol_table.py  # Symbol table implementation 
│   ├── exceptions.py    # Custom exceptions
│   ├── builtins.py      # Built-in functions
│   └── repl.py          # Read-Evaluate-Print Loop
├── tests/
│   ├── input/           # Test files go here
│   │   ├── function_test.onion
│   │   ├── binary_search_test.onion
│   │   └── logical_test.onion
│   └── output/          # Generated ASTs are saved here
│       ├── function_test.ast.txt
│       └── binary_search_test.ast.txt
├── main.py              # Main file to run repl
├── README.md
└── requirements.txt
```
## Grammar
### Running Tests
The test files should be placed in the `tests/input/` directory. You can run them directly from the REPL:

```bash
python main.py
```

To test a specific file:
```bash
>>> run binary_search_test
```

This will automatically:
1. Look for the file in `tests/input/` folder
2. Add the `.onion` extension if you didn't specify it
3. Run the file
4. Generate an AST (Abstract Syntax Tree) representation in `tests/output/`

You can also run a file directly from the command line:
```bash
python main.py binary_search_test
```

### Regenerating the Parser
The grammar file is located at: `grammar/Onion.g4`. After making changes, regenerate the parser:
```bash
antlr4 -Dlanguage=Python3 grammar/Onion.g4 -visitor -o generated
```
## Packaging
To package the application run:
```bash
pyinstaller --onefile main.py
```

## Using the REPL (Read-Evaluate-Print Loop)

The REPL is an interactive environment for executing Onion code. To start the REPL, run:

```bash
python main.py
```

### REPL Commands:

- `help`: Display usage instructions and code examples
- `run <filename>`: Execute an Onion file
  - If only a filename is provided, it looks in `tests/input/` directory
  - Example: `run binary_search_test` runs `tests/input/binary_search_test.onion`
  - You can also provide a full path: `run /path/to/your/file.onion`
- `clear`: Clear the terminal screen
- `exit` or `quit`: Exit the REPL

### Onion Code Examples:
```
# Variable assignment
(let x 5)

# Arithmetic
(+ x 10)
(* 2 3 4)
(- 10 5)
(/ 10 2)
(// 10 3)  # Integer division

# Boolean operations
(== 5 5)
(< 3 6)
(& true false)  # Logical AND
(| false true)  # Logical OR
(! true)        # Logical NOT

# Conditionals
(if (> x 0) (print "Positive") (else (print "Non-positive")))

# Functions
(def add (a b)
    (return (+ a b)))
(print (add 3 4))

# Lists
(let mylist (list 1 2 3 4 5))
(print (getid 2 mylist))  # Get element at index 2
