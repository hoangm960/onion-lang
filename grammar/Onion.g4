// --- START OF FILE Onion.g4 ---

grammar Onion;

// Top-level rules

program: statement+ EOF; // Added EOF for completeness

statement
    : assignment
    | expression
    | printStatement
    | macroDef
    | classDef
    | loopStatement
    | incDecStmt
    | functionDef
    | returnStmt
    | block
    ;

incDecStmt
    : '(' 'inc' IDENTIFIER ')'  // Increment: (inc x)
    | '(' 'dec' IDENTIFIER ')'  // Decrement: (dec x)
    ;

assignment
    : '(' 'let' IDENTIFIER expression ')'
    | '(' 'let' ( '(' IDENTIFIER expression ')' )+ ')'
    ;

expression
    : literal
    | IDENTIFIER
    | arithmeticExpr
    | booleanExpr
    | listExpr
    | functionCall
    | ifExpr
    | branchExpr // Added branchExpr here as it seems intended to be an expression form
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

listExpr: '(' 'list' expression* ')'; // Changed to * to allow empty lists (list)

ifExpr
    : '(' 'if' expression statement                      
      ( '(' 'elif' expression statement ')' )*           
      ( '(' 'else' statement ')' )?                     
    ')'                                                 
    ;

branchExpr
    : '(' 'cond'
        ( '(' expression statement ')' )+
        ( '(' 't' statement ')' )? // 't' often means true/otherwise in cond
    ')';

functionDef
    : '(' 'def' IDENTIFIER
        '(' IDENTIFIER* ')' // Simplified parameter list - allows zero params
        block
    ')';

returnStmt
    : '(' 'return' (IDENTIFIER | literal) ')' // Single return value
    | '(' 'return' '(' (IDENTIFIER | literal)+ ')' ')'; // Multiple return values - added closing paren and +

functionCall: '(' IDENTIFIER expression* ')'; // Simplified argument list - allows zero args

printStatement: '(' 'print' expression ')';

loopStatement
    : '(' 'repeat' expression statement ')'                                           
    | '(' 'loop' IDENTIFIER 'range' '(' expression expression (expression)? ')' statement+ ')'  
    | '(' 'while' expression statement+  ')'                               
    ;

// Macros look syntactically similar to functions - ensure distinct handling in visitor/listener
macroDef: '(' 'macro' IDENTIFIER '(' IDENTIFIER* ')' block ')'; // Simplified params

macroCall: '(' IDENTIFIER expression* ')'; // Simplified args

classDef: '(' 'class' IDENTIFIER classBody ')';

classBody
    : '(' methodDef+ ')' // Assuming at least one method needed?
    ;

methodDef: '(' 'def' IDENTIFIER '(' IDENTIFIER* ')' block ')'; // Simplified params

block: '(' statement+ ')';

literal
    : INT
    | FLOAT
    | BOOL      
    | STRING
    ;

// Keywords as Tokens (matched before IDENTIFIER)
BOOL:       'true' | 'false';

// Literals
INT:        [0-9]+;
FLOAT:      [0-9]* '.' [0-9]+;
STRING:     '"' (~["\r\n])*? '"' ; // *** Corrected: Added semicolon ***

// Identifier (comes AFTER specific keywords like BOOL)
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip whitespace and comments
WS:         [ \t\r\n]+ -> skip;
COMMENT:    '/*' .*? '*/' -> skip; // Non-greedy match
LINE_COMMENT: '//' ~[\r\n]* -> skip;
