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
## Grammar
### Test grammar
Input your test file in *tests/inputs/*
```cmd
cd grammar
python main.py
```
```
>>> run [filename].txt
```
Outputs of the test cases will be displays at the terminal and saved to *tests/outputs/* 
### Fix grammar
The grammar file located at: *grammar/Onion.g4*. After fixing, run:
```cmd
antlr4 -Dlanguage=Python3 Onion.g4
```