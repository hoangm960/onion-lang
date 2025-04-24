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
│   ├── repl.py          # Read-Evaluate-Print Loop
│   └── utils.py
├── tests/
│   └── parsers/
│       ├── input/
│       │   ├── input1.onion
│       │   └── input2.onion
│       └── output/
│           ├── output1.onion
│           └── output2.onion
├── main.py              # Main file to run repl
├── test.py              # Unittest
├── README.md
└── requirements.txt
```
## Grammar
### Test grammar
Input your test file in *tests/parsers/inputs/*
```bash
python test_parser.py
```
To test 1 test file:
```bash
>>> run [filename].txt
```
To test all test files:
```bash
>>> runall
```
Outputs of the test cases will be displayed at the terminal and saved to *tests/parsers/outputs/* 
### Fix grammar
The grammar file located at: *grammar/Onion.g4*. After fixing, run:
```bash
antlr4 -Dlanguage=Python3 grammar/Onion.g4 -visitor -o generated
```

## Using the REPL (Read-Evaluate-Print Loop)

The REPL is an interactive environment for executing Onion code. To start the REPL, run:

```bash
python main.py
```

### REPL Commands:

- `help`: Display usage instructions and code examples
- `run <filename>`: Execute a specific Onion file (can be a relative or absolute path)
  - Example: `run arithmetic.onion` or `run tests/parsers/input/arithmetic.onion`
- `run <filename> -s` or `run <filename> --save`: Run a file and save the results to the tests/parsers/output/ directory
- `runall`: Run all .onion files in the tests/parsers/input directory and save results to the tests/parsers/output/ directory
- `clear`: Clear the terminal screen
- `exit` or `quit`: Exit the REPL

### Onion Code Examples: