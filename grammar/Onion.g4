grammar Onion;

// Top-level rules
program: statement+ EOF;

statement: 
    LPAREN statementType RPAREN
    | LPAREN SIFE statementType RPAREN
    ;

statementType:
    assignment
    | augmentedAssignment
    | expression
    | printStatement
    | macroDef
    | classDef
    | loopStatement
    | functionDef
    | returnStmt
    | block
    | ifStmt
    | appendStmt;

assignment:
    LET IDENTIFIER (expression | ternaryExpr)
    | LET (LPAREN IDENTIFIER (expression | ternaryExpr) RPAREN)+;

augmentedAssignment:
    PLUS_EQUALS IDENTIFIER (expression | ternaryExpr)
    | MINUS_EQUALS IDENTIFIER (expression | ternaryExpr)
    | MULT_EQUALS IDENTIFIER (expression | ternaryExpr)
    | DIV_EQUALS IDENTIFIER (expression | ternaryExpr)
    ;

expression: literal | IDENTIFIER | LPAREN compoundExpr RPAREN;

compoundExpr:
    arithmeticExpr
    | booleanExpr
    | logicalExpr
    | listExpr
    | callExpr
    | branchExpr
    | listOpExpr
    | ternaryExpr;

arithmeticExpr:
    PLUS expression+
    | MINUS expression expression
    | MULT expression+
    | DIV expression expression
    | FLOOR_DIV expression expression;

booleanExpr:
    EQ expression expression
    | NEQ expression expression
    | LT expression expression
    | GT expression expression
    | LTE expression expression
    | GTE expression expression
    | NOT expression;

logicalExpr:
    AND expression expression
    | OR expression expression
    | NOT expression;

listExpr: LIST expression*;

ifStmt:
    IF expression block (
        LPAREN ELIF expression block RPAREN
    )* (LPAREN ELSE block RPAREN)?;

branchExpr:
    COND (LPAREN expression statement RPAREN)+ (
        LPAREN T statement RPAREN
    )?;

functionDef:
    DEF IDENTIFIER LPAREN (IDENTIFIER)* RPAREN
    block;

returnStmt: RETURN expression;

callExpr:
    IDENTIFIER expression*;

printStatement: PRINT expression;

loopStatement:
    REPEAT expression block
    | LOOP IDENTIFIER RANGE LPAREN expression (expression)? (expression)? RPAREN block
    | WHILE expression block;

listOpExpr:
    HEAD expression
    | TAIL expression
    | GETID expression expression
    | SIZEOF expression;

macroDef:
    MACRO IDENTIFIER LPAREN (IDENTIFIER)* RPAREN block;

classDef: CLASS IDENTIFIER classBody;

classBody: LPAREN methodDef+ RPAREN;

methodDef:
    DEF IDENTIFIER LPAREN IDENTIFIER* RPAREN block;

block: 
    statement+;

appendStmt: APPEND IDENTIFIER expression;

literal: INT | FLOAT | BOOL | STRING;

// Keywords as Tokens (matched before IDENTIFIER)
BOOL: 'true' | 'false';
LET: 'let';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
PRINT: 'print';
REPEAT: 'repeat';
LOOP: 'loop';
RANGE: 'range';
WHILE: 'while';
DEF: 'def';
RETURN: 'return';
MACRO: 'macro';
CLASS: 'class';
COND: 'cond';
T: 't';
LIST: 'list';
HEAD: 'head';
TAIL: 'tail';
GETID: 'getid';
SIZEOF: 'sizeof';
APPEND: 'append';

// Operators as tokens
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
FLOOR_DIV: '//';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NOT: 'not';
AND: '&';
OR: '|';
PLUS_EQUALS: '+=';
MINUS_EQUALS: '-=';
MULT_EQUALS: '*=';
DIV_EQUALS: '/=';

// Punctuation tokens
LPAREN: '(';
RPAREN: ')';
COLON: ':';
SIFE: '$';

// Literals
INT: '-'? [0-9]+;
FLOAT: '-'? [0-9]* '.' [0-9]+;
STRING: '"' (~["\r\n])*? '"';

// Identifier (comes AFTER specific keywords)
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '#' ~[\r\n]* -> skip;

ternaryExpr:
    IF expression expression COLON expression;