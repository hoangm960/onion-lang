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
├── README.md       
├── requirements.txt          
├── grammar/          
│   └── Onion.g4 
├── generated/             # Generated parser files from ANTLR4
│   ├── __init__.py
│   ├── ...
│   ├── OnionLexer.py
│   ├── OnionParser.py
│   └── OnionVisitor.py
├── src/                   # Main source code
│   ├── __init__.py
│   ├── parser.py          # Module to load parser
│   ├── interpreter.py     # Module for interpreter
│   ├── repl.py            # Read-Evaluate-Print Loop
│   └── utils.py
└── tests/
    └── parsers/    
        ├── input/
        │   ├── input1.onion  
        │   └── input2.onion
        └── output/
            ├── output1.onion
            └── output2.onion
```
## Grammar
### Test grammar
Input your test file in *tests/inputs/*
```bash
python main.py
```
To test 1 test file:
```bash
>>> run [filename].txt
```
To test all test files:
```bash
>>> runall
```
Outputs of the test cases will be displays at the terminal and saved to *tests/outputs/* 
### Fix grammar
The grammar file located at: *grammar/Onion.g4*. After fixing, run:
```bash
antlr4 -Dlanguage=Python3 Onion.g4 -visitor -o onion_parser
```