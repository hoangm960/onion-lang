grammar Onion;

// Top-level rules

program: statement+ ;

statement
    : assignment
    | expression
    | printStatement
    | macroDef
    | classDef
    | loopStatement
    | incDecStmt
    | functionDef   
    ;

incDecStmt
    : '(' 'inc' IDENTIFIER ')'  // Increment: (inc x)
    | '(' 'dec' IDENTIFIER ')'  // Decrement: (dec x)
    ;

assignment
    : '(' 'let' IDENTIFIER expression ')'
    | '(' 'let' ( '(' IDENTIFIER expression ')' )+ ')';

expression
    : literal
    | IDENTIFIER
    | arithmeticExpr
    | booleanExpr
    | listExpr
    | functionCall
    | ifExpr
    | macroCall
    ;

arithmeticExpr
    : '(' '+' expression+ ')'
    | '(' '-' expression expression+ ')'   // at least 2
    | '(' '*' expression+ ')'
    | '(' '/' expression expression+ ')'   // at least 2
    ;


booleanExpr
    : '(' '==' expression expression ')'
    | '(' '!=' expression expression ')'
    | '(' '<' expression expression ')'
    | '(' '>' expression expression ')'
    | '(' '<=' expression expression ')'
    | '(' '>=' expression expression ')'
    | '(' 'not' expression ')'
    ;

listExpr: '(' 'list' expression (expression)* ')'; //example: (list 1 "abc" Person) 

ifExpr
    : '(' 'if' '(' expression ')' statement ')'
      ('(' 'elif' '(' expression ')' statement)*
      ('(' 'else' statement ')')? 
    ')';
branchExpr
    : '(' 'cond' 
        ('(' expression statement ')')+
        ('(' 't' statement ')')?
    ')';

functionDef
    : '(' 'def' IDENTIFIER 
        '(' (IDENTIFIER (IDENTIFIER)*)? ')' 
        block 
    ')';

functionCall: '(' IDENTIFIER expression (expression)* ')';

printStatement: '(' 'print' expression ')';

loopStatement 
    : '(' 'repeat' expression statement ')'                                           // (repeat 5 statement)
    | '(' 'loop' IDENTIFIER 'range' '(' expression ',' expression (',' expression)? ')' statement ')'  // (for i in range(0, 10, 2) statement)
    | '(' 'while' '(' expression ')' statement ')'                                   // (while (< x 10) statement)
    ;

macroDef: '(' 'macro' IDENTIFIER '(' (IDENTIFIER (',' IDENTIFIER)*)? ')' block ')';

macroCall: '(' IDENTIFIER expression (expression)* ')';

classDef: '(' 'class' IDENTIFIER classBody ')';

classBody
    : '(' methodDef+ ')'
    ;

methodDef: '(' 'def' IDENTIFIER '(' (IDENTIFIER (',' IDENTIFIER)*)? ')' block ')';

block: '(' statement+ ')';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

literal
    : INT
    | FLOAT
    | BOOL
    | STRING
    ;

INT: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n])* '"';

// Skip whitespace and comments

WS: [ \t\r\n]+ -> skip;

COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
