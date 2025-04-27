// --- START OF FILE Onion.g4 ---

grammar Onion;

// Top-level rules

program: statement+ EOF; // Added EOF for completeness

statement: '(' statementType ')';

statementType:
	assignment
	| expression
	| printStatement
	| macroDef
	| classDef
	| loopStatement
	| incDecStmt
	| functionDef
	| returnStmt
	| block
	| ifExpr
	| branchExpr;

incDecStmt:
	'inc' IDENTIFIER // Increment: (inc x)
	| 'dec' IDENTIFIER; // Decrement: (dec x)

assignment:
	'let' IDENTIFIER (expression | ternaryExpr)
	| 'let' ( '(' IDENTIFIER (expression | ternaryExpr) ')')+;

expression: literal | IDENTIFIER | '(' compoundExpr ')' | '(' incDecExpr ')';

compoundExpr:
	arithmeticExpr
	| booleanExpr
	| logicalExpr
	| listExpr
	| callExpr
	| ifExpr
	| branchExpr
	| listOpExpr
	| ternaryExpr;

// Allow inc/dec to be used in expressions
incDecExpr:
	'inc' IDENTIFIER 
	| 'dec' IDENTIFIER;

arithmeticExpr:
	'+' expression+
	| '-' expression expression
	| '*' expression+
	| '/' expression expression
	| '//' expression expression;

booleanExpr:
	'==' expression expression
	| '!=' expression expression
	| '<' expression expression
	| '>' expression expression
	| '<=' expression expression
	| '>=' expression expression
	| 'not' expression;

logicalExpr:
	'&' expression expression   // Logical AND
	| '|' expression expression  // Logical OR
	| '!' expression;            // Logical NOT

listExpr: 'list' expression*; // Allow empty lists (list)

ifExpr:
	'if' expression statement (
		'(' 'elif' expression statement ')'
	)* ('(' 'else' statement ')')?;

branchExpr:
	'cond' ('(' expression statement ')')+ (
		'(' 't' statement ')'
	)?;

functionDef:
	'def' IDENTIFIER '(' (IDENTIFIER)* ')' // Simplified parameter list - allows zero params
	block;

returnStmt: 'return' expression;

callExpr:
	IDENTIFIER expression*; // Simplified argument list - allows zero args

printStatement: 'print' expression;

loopStatement:
	'repeat' expression block
	| 'loop' IDENTIFIER 'range' '(' expression expression (
		expression
	)? ')' block
	| 'while' expression block;

listOpExpr:
	'head' expression
	| 'tail' expression
	| 'getid' expression expression //getid index list
	| 'sizeof' expression;

// Macros look syntactically similar to functions - ensure distinct handling in visitor/listener
macroDef:
	'macro' IDENTIFIER '(' (IDENTIFIER)* ')' block; // Simplified params

classDef: 'class' IDENTIFIER classBody;

classBody: '(' methodDef+ ')';

methodDef:
	'def' IDENTIFIER '(' IDENTIFIER* ')' block; // Simplified params

block: statement+;

literal: INT | FLOAT | BOOL | STRING;

// Keywords as Tokens (matched before IDENTIFIER)
BOOL: 'true' | 'false';

// Logical operators as tokens
AND: '&';
OR: '|';
NOT: '!';

// Explicit Colon Token
COLON: ':';

// Literals
INT: '-'? [0-9]+;
FLOAT: '-'? [0-9]* '.' [0-9]+;
STRING: '"' (~["\r\n])*? '"';

// Identifier (comes AFTER specific keywords like BOOL)
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip; // Non-greedy match
LINE_COMMENT: '#' ~[\r\n]* -> skip;

ternaryExpr:
	'if' expression expression COLON expression;
