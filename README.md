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

## Onion Language Features

Here are some of the key features of the Onion language with examples:

### 1. Variables and Assignment
Variables are declared using `let`. Type declarations are optional.
```onion
# Basic assignment
(let x 10)
(let name "Onion")

# Assignment with optional type declaration
(let count:int 100)
(let pi:float 3.14159)
(let items:list (list 1 2 3))

# Multiple assignments in one statement
(let (a 1) (b "hello") (c:bool true))

# Re-assigning an existing variable (must be declared with 'let' first)
(set x 20) 
```

### 2. Conditional Statements (if/elif/else)
Onion supports `if`, `elif`, and `else` for conditional logic.
```onion
(let score 85)

(if (>= score 90)
    (print "Grade: A")
    (elif (>= score 80)
        (print "Grade: B"))
    (elif (>= score 70)
        (print "Grade: C"))
    (else
        (print "Grade: D or F"))
)

# Conditional without else
(if (< score 0)
    (print "Invalid score!")
)
```

### 3. Lists
Lists are ordered collections of items. Type declarations for list elements are optional.

```onion
# Creating lists
(let empty_list (list))
(let numbers (list 1 2 3 4 5))
(let mixed_list (list 1 "two" true 3.0))
(let typed_list (list:int (list 10 20 30))) # A list specifically of integers

# Get list length
(let my_list (list "a" "b" "c"))
(print (len my_list)) # Output: 3

# Get element by index (0-based)
(print (id 0 my_list)) # Output: "a"
(print (id 2 my_list)) # Output: "c"

# Append element to a list (modifies the list in-place)
(append my_list "d")
(print my_list) # Output: (list "a" "b" "c" "d")
```

#### List Operations: `map`, `lambda`, `reduce`, `filter`

```onion
(let data (list 1 2 3 4 5))

# Lambda functions (anonymous functions)
# (lambda (parameters) body_expression)
(let square (lambda (x) (* x x)))
(print (square 5)) # Output: 25

# Map: Apply a function to each element of a list
# (map function_or_lambda list)
(let squared_data (map (lambda (n) (* n n)) data))
(print squared_data) # Output: (list 1 4 9 16 25)

(let add_ten (lambda (x) (+ x 10)))
(let mapped_data (map add_ten data))
(print mapped_data) # Output: (list 11 12 13 14 15)

# Filter: Create a new list with elements that satisfy a condition
# (filter predicate_lambda list)
(let even_numbers (filter (lambda (n) (== (% n 2) 0)) data))
(print even_numbers) # Output: (list 2 4)

# Reduce: Apply a function cumulatively to the items of a list
# (reduce operator list) where operator is '+', '-', '*', '/'
(let sum_of_data (reduce + data))
(print sum_of_data) # Output: 15

(let product_of_data (reduce * data))
(print product_of_data) # Output: 120
```

### 4. Loops

#### `for` loop
Iterates over a range with a specified step.
`_` can be used if the loop variable is not needed.
```onion
# (for (variable start_inclusive:end_exclusive step) statements+)
(for (i 0:5 1) 
    (print i)
)

(for (x 10:0 -2)
    (print x)
)
```

#### `while` loop
Executes statements as long as a condition is true.
```onion
(let counter 0)
(while (< counter 3)
    (print counter)
    (set counter (+ counter 1)) 
    # Prints 0, 1, 2
)
```

#### `repeat` loop
Executes statements a fixed number of times.
```onion
(repeat 3 
    (println "Hello from repeat!") 
    # Prints "Hello from repeat!" 3 times
)
```

### 5. Functions
Functions are defined using `def`. Parameter and return type declarations are optional.

```onion
# Simple function
(def greet (name)
    (println (+ "Hello, " name "!"))
)
(greet "World")

# Function with a return value
(def add (a b)
    (return (+ a b))
)
(let result (add 5 3))
(print result) # Output: 8

# Function with type declarations (optional)
(def multiply (x:int y:int) :int
    (return (* x y))
)
(print (multiply 6 7)) # Output: 42

# Fibonacci sequence example
(def fib (n:int) :int
    (if (<= n 1)
        (return n)
        (return (+ (fib (- n 1)) (fib (- n 2))))
    )
)

(println "Fibonacci sequence:")
(for (i 0:10 1)
    (print "fib(") (print i) (print "): ") (println (fib i))
)

### 6. Printing
`print` outputs its argument. `println` outputs its argument followed by a newline.
```onion
(print "Hello, ")
(println "Onion!") 
# Output: 
Hello, 
Onion! (newline after Onion!)

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