// --- START OF FILE Onion.g4 ---

grammar Onion;

// Top-level rules

program: statement+ EOF; // Added EOF for completeness

statement: '(' statementType ')';

statementType:
	assignment
	| expression
	| printStatement
	| loopStatement
	| augmentedAssignment
	| functionDef
	| returnStmt
	| ifExpr
	| branchExpr
	| appendStmt
	| setStmt;

augmentedAssignment:
	'+=' IDENTIFIER expression
	|'-=' IDENTIFIER expression
	|'*=' IDENTIFIER expression
	|'/=' IDENTIFIER expression
	;

assignment:
	'let' IDENTIFIER (typeDec)? (expression | ternaryExpr)
	| 'let' ( '(' IDENTIFIER (typeDec)? (expression | ternaryExpr) ')')+ //Multi assignment
	;

setStmt:
	'set' IDENTIFIER (expression | ternaryExpr);

expression: literal | IDENTIFIER | '(' compoundExpr ')';

type: 
	'int'
	| 'char'
	| 'string'
	| 'bool'
	| 'float'
	| 'list'
	| 'void'
	;

typeDec: ':' type;

compoundExpr:
    arithmeticExpr # Arithmetic
  | booleanExpr # Boolean
  | logicalExpr # Logical
  | listExpr # List
  | callExpr # Call
  | ifExpr # If
  | branchExpr # Branch
  | ternaryExpr # Ternary
  | listOpExpr # ListOp
  | lambdaExpr # Lambda
  | filterExpr # Filter
  | reduceExpr # Reduce
  | mapExpr # Map
;

arithmeticExpr:
	'+' expression+
	| '-' expression expression
	| '*' expression+
	| '/' expression expression
	| '//' expression expression
	| '%' expression expression;

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

listExpr: 'list' (typeDec)? expression*; // Allow empty lists (list)

lambdaExpr: 'lambda' (IDENTIFIER)+ expression; // (lambda x (*x 2))

filterExpr: 'filter' expression expression; //(filter (even x) list)

reduceExpr: 'reduce' ('+' | '-' | '*' | '//') expression; //('reduce' + list)

ifExpr:
	'if' expression (statement)+ (
		'(' 'elif' expression (statement)+ ')'
	)* ('(' 'else' (statement)+ ')')?;

branchExpr:
	'cond' ('(' expression statement ')')+ (
		'(' 't' statement ')'
	)?;

functionDef:
	'def' IDENTIFIER '(' (IDENTIFIER (typeDec)?)* ')' (typeDec)?
	(statement)+;

returnStmt: 'return' expression;

callExpr:
	IDENTIFIER expression*; // Simplified argument list - allows zero args

printStatement: 
	'print' expression
	|'println' expression;

loopStatement:
	'repeat' expression (statement)+
	| 'for' '(' (IDENTIFIER | '_') (expression)':'(expression) (expression)?')' (statement)+ //for (id start:end step)
	| 'while' expression (statement)+;

listOpExpr:
	'head' expression
	| 'tail' expression
	| 'id' expression expression //getid index list
	| 'len' expression;


appendStmt: 'append' IDENTIFIER expression;

mapExpr: 'map' expression expression; // (map (lambda x (*x 2)) list)

literal: INT | FLOAT | BOOL | STRING | FSTRING;

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
FSTRING: 'f"' (~["\r\n])*? '"';

// Identifier (comes AFTER specific keywords like BOOL)
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Skip whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip; // Non-greedy match
LINE_COMMENT: '#' ~[\r\n]* -> skip;

ternaryExpr:
	'if' expression expression COLON expression;
