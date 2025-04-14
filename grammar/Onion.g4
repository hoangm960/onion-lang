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
    ;

assignment
    : '(' 'let' IDENTIFIER expression ')'
    | '(' 'let' ( '(' IDENTIFIER expression ')' )+ ')';

expression
    : literal
    | IDENTIFIER
    | arithmeticExpr
    | booleanExpr
    | arrayExpr
    | functionCall
    | ifExpr
    | macroCall
    ;

arithmeticExpr
    : '(' '+' expression expression ')'
    | '(' '-' expression expression ')'
    | '(' '*' expression expression ')'
    | '(' '/' expression expression ')'
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

arrayExpr: '(' '[' expression (',' expression)* ']' ')';

ifExpr: '(' 'if' expression 'then' statement ('else' statement)? ')';

functionCall: '(' IDENTIFIER expression (expression)* ')';

printStatement: '(' 'print' expression ')';

loopStatement 
    : '(' 'for' '(' IDENTIFIER expression expression ')' statement ')'
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
    | BOOL
    | STRING
    ;

INT: [0-9]+;
BOOL: 'true' | 'false';
STRING: '"' (~["\r\n])* '"';

// Skip whitespace and comments

WS: [ \t\r\n]+ -> skip;

COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
