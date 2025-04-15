grammar MyLang;

// parser rules

program: statement* EOF;

statement:
	';'														# EmptyStmt
	| type ID (',' ID)* ';'									# VarDecl
	| expression ';'										# ExprStmt
	| 'read' ID (',' ID)* ';'								# ReadStmt
	| 'write' expression (',' expression)* ';'				# WriteStmt
	| '{' statement* '}'									# BlockStmt
	| 'if' '(' expression ')' statement ('else' statement)?	# IfStmt
	| 'while' '(' expression ')' statement					# WhileStmt;

expression:
	<assoc = right> expression '=' expression	# AssignExpr
	| expression '||' expression				# OrExpr
	| expression '&&' expression				# AndExpr
	| expression ('==' | '!=') expression		# EqExpr
	| expression ('<' | '>') expression			# RelExpr
	| expression ('+' | '-' | '.') expression	# AddExpr
	| expression ('*' | '/' | '%') expression	# MulExpr
	| '!' expression							# NotExpr
	| '-' expression							# NegExpr
	| '(' expression ')'						# ParensExpr
	| literal									# LiteralExpr
	| ID										# VarExpr;

// ------------------------ Types ------------------------

type: 'int' | 'float' | 'bool' | 'string';

// ------------------------ Literals ------------------------

literal: INT | FLOAT | STRING | BOOL;

// ------------------------ Lexer Rules ------------------------

BOOL: 'true' | 'false';

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';

ID: [a-zA-Z] [a-zA-Z0-9]*;

WS: [ \t\r\n]+ -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Operators and delimiters
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
AND: '&&';
OR: '||';
NOT: '!';
DOT: '.';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
COMMA: ',';