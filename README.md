# Onion

🧅 Welcome to Onion! 🧅

Onion is a delightful little programming language designed to be both powerful and fun to use. It draws inspiration from the elegance of Lisp (you'll notice the parentheses! 😉) but aims for a syntax that feels as approachable and easy to learn as Python. Whether you're a seasoned Lisp enthusiast or new to functional programming concepts, Onion offers a fresh and engaging experience. Dive in and explore its features! 🚀

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
.
├── .git/
├── .github/
├── .gitignore
├── build/
├── dist/
│   └── Onion.exe        # Executable for Windows
├── generated/           # Generated parser files from ANTLR4
│   ├── __init__.py
│   ├── OnionLexer.py
│   ├── OnionParser.py
│   └── OnionVisitor.py
├── grammar/
│   └── Onion.g4
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
│   └── output/          # Generated ASTs are saved here
├── main.py              # Main script to run REPL or files
├── README.md
├── requirements.txt
└── test.py              # (Assuming this is a test runner or utility)
```
### Running Tests
The test files should be placed in the `tests/input/` directory.

To run a specific test file (e.g., `my_test.onion`):
```bash
# Using the executable (if dist is in PATH)
Onion.exe run tests/input/my_test.onion

# Or using Python
python main.py run tests/input/my_test.onion
```
The `run` command in `main.py` can also accept an `--ast` flag to save the AST for each file to `tests/output/`.

```bash
python main.py run tests/input/my_test.onion --ast
```
## Regenerating the Parser
The grammar file is located at: `grammar/Onion.g4`. After making changes, regenerate the parser files (located in `generated/`):
```bash
antlr4 -Dlanguage=Python3 grammar/Onion.g4 -visitor -o generated
```
## Packaging
To package the application run:
```bash
pyinstaller --onefile main.py -n onion
```
## Running Onion

There are two main ways to run Onion programs or the REPL:

1.  **Using the Executable (Windows):**
    The `dist/` folder contains `Onion.exe`. You can run this directly:
    ```bash
    dist/Onion.exe repl          # To start the REPL
    dist/Onion.exe run your_file.onion # To run a file
    ```
    For convenience, you can add the `dist` directory to your system's PATH environment variable. Then, you can simply type `Onion repl` or `Onion run ...` from any directory.

2.  **Using Python:**
    If you have Python installed, you can run Onion using `main.py`:
    ```bash
    python main.py repl          # To start the REPL
    python main.py run your_file.onion # To run a file
    ```

## Onion Language Features

Here are some of the key features of the Onion language with examples:

### 1. Variables and Assignment
Variables are declared using `let`. Type declarations are optional.
```onion
(let x 10)
(let name "Onion")
(let count:int 100) # With type
(let (a 1) (b "hello")) # Multiple
(set x 20) # Re-assign
```

### 2. Conditional Statements (if/elif/else)
Onion supports `if`, `elif`, and `else`.
```onion
(let score 75)
(if (>= score 90)
    (print "Grade: A")
    (elif (>= score 80)
        (print "Grade: B"))
    (else
        (print "Grade: C or lower"))
)
```

### 3. Lists
Lists are ordered collections. Type declarations for list elements are optional.
```onion
# Creating lists
(let numbers (list 1 2 3))
(let typed_list (list:int (list 10 20))) # Typed list

# Get list length
(let my_list (list "a" "b" "c"))
(print (len my_list)) # Output: 3

# Get element by index (0-based)
(print (id 1 my_list)) # Output: "b"

# Append element (modifies in-place)
(append my_list "d")
(print my_list) # Output: (list "a" "b" "c" "d")
```

#### List Operations: `map`, `lambda`, `reduce`, `filter`
```onion
(let data (list 1 2 3 4))

# Lambda: (lambda (params) body_expr)
(let double (lambda (x) (* x x)))
(print (double 3)) # Output: 9

# Map: (map fn list)
(let doubled_data (map double data))
(print doubled_data) # Output: (list 1 4 9 16)

# Filter: (filter predicate_lambda list)
(let evens (filter (lambda (n) (== (% n 2) 0)) data))
(print evens) # Output: (list 2 4)

# Reduce: (reduce operator list)
(let sum_val (reduce + data))
(print sum_val) # Output: 10
```

### 4. Loops

#### `for` loop
`(for (var start:end step) statements+)`
```onion
(for (i 0:3 1) (print i)) # Prints 0, 1, 2
```

#### `while` loop
```onion
(let counter 0)
(while (< counter 2)
    (print counter)
    (set counter (+ counter 1)) # Prints 0, 1
)
```

#### `repeat` loop
```onion
(repeat 2 (println "Hi")) # Prints "Hi" twice
```

### 5. Functions
Defined with `def`. Types are optional.
```onion
# Simple function with return
(def add (a b) (return (+ a b)))
(print (add 5 3)) # Output: 8

# Typed function
(def multiply (x:int y:int) :int (return (* x y)))
(print (multiply 6 7)) # Output: 42

# Recursive Fibonacci (compact)
(def fib (n:int) :int
    (if (<= n 1) (return n) (return (+ (fib (- n 1)) (fib (- n 2)))))
)
(print (fib 5)) # Output: 5
```

### 6. Printing
`print` and `println` (with newline).
```onion
(print "One ") (println "Two") # Output: One Two (newline)
```

## Using the REPL (Read-Evaluate-Print Loop)

The REPL is an interactive environment for executing Onion code. To start the REPL:

```bash
# Using the executable (if dist is in PATH)
Onion.exe repl

# Or using Python
python main.py repl
```

The REPL prompt is `onion>`.

### REPL Commands:

- `help`: Display usage instructions.
- `run <filename_or_path>`: Execute an Onion file.
  - If only a filename (e.g., `my_test`) is provided, it looks for `tests/input/my_test.onion`.
  - You can provide a full or relative path (e.g., `run path/to/file.onion`).
- `clear`: Clear the terminal screen.
- `exit` or `quit`: Exit the REPL.

### Old Onion Code Examples (To be reviewed/updated/merged with above)
```onion
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
```