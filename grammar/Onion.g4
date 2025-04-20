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
	| functionCall
	| ifExpr // allow if as a top-level statement
	| branchExpr ; // allow cond as a top-level statement

incDecStmt:
	'inc' IDENTIFIER // Increment: (inc x)
	| 'dec' IDENTIFIER ; // Decrement: (dec x)

assignment:
	'let' IDENTIFIER expression
	| 'let' ( '(' IDENTIFIER expression ')')+;

expression: literal | IDENTIFIER | '(' compoundExpr ')';

compoundExpr:
	arithmeticExpr
	| booleanExpr
	| listExpr
	| functionCall
	| ifExpr
	| branchExpr
	| macroCall
	| listOpExpr;

arithmeticExpr:
	'+' expression+
	| '-' expression expression
	| '*' expression+
	| '/' expression expression;

booleanExpr:
	'==' expression expression
	| '!=' expression expression
	| '<' expression expression
	| '>' expression expression
	| '<=' expression expression
	| '>=' expression expression
	| 'not' expression;

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

functionCall:
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
	| 'getid' expression expression
	| 'sizeof' expression;

// Macros look syntactically similar to functions - ensure distinct handling in visitor/listener
macroDef:
	'macro' IDENTIFIER '(' IDENTIFIER* ')' block; // Simplified params

macroCall: IDENTIFIER expression*; // Simplified args

classDef: 'class' IDENTIFIER classBody;

classBody: '(' methodDef+ ')';

methodDef:
	'def' IDENTIFIER '(' IDENTIFIER* ')' block; // Simplified params

block: statement+;

literal: INT | FLOAT | BOOL | STRING;

// Keywords as Tokens (matched before IDENTIFIER)
BOOL: 'true' | 'false';

// Literals
INT: [0-9]+;
FLOAT: [0-9]* '.' [0-9]+;
STRING: '"' (~["\r\n])*? '"';

// Identifier (comes AFTER specific keywords like BOOL)
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip; // Non-greedy match
LINE_COMMENT: '//' ~[\r\n]* -> skip;