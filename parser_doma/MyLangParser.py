# Generated from MyLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,1,2,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,4,1,4,1,5,1,5,1,5,1,5,
        5,5,84,8,5,10,5,12,5,87,9,5,1,5,1,5,1,6,1,6,5,6,93,8,6,10,6,12,6,
        96,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,107,8,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,3,10,120,8,10,1,11,1,11,1,11,
        5,11,125,8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,5,12,133,8,12,
        10,12,12,12,136,9,12,1,13,1,13,1,13,5,13,141,8,13,10,13,12,13,144,
        9,13,1,14,1,14,1,14,5,14,149,8,14,10,14,12,14,152,9,14,1,15,1,15,
        1,15,5,15,157,8,15,10,15,12,15,160,9,15,1,16,1,16,1,16,5,16,165,
        8,16,10,16,12,16,168,9,16,1,17,1,17,1,17,3,17,173,8,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,184,8,18,1,18,0,0,19,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,5,1,0,23,24,1,
        0,25,26,2,0,14,15,19,19,1,0,16,18,2,0,15,15,22,22,192,0,41,1,0,0,
        0,2,52,1,0,0,0,4,54,1,0,0,0,6,65,1,0,0,0,8,68,1,0,0,0,10,79,1,0,
        0,0,12,90,1,0,0,0,14,99,1,0,0,0,16,108,1,0,0,0,18,114,1,0,0,0,20,
        116,1,0,0,0,22,121,1,0,0,0,24,129,1,0,0,0,26,137,1,0,0,0,28,145,
        1,0,0,0,30,153,1,0,0,0,32,161,1,0,0,0,34,172,1,0,0,0,36,183,1,0,
        0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,53,3,4,2,0,45,53,3,6,3,0,46,
        53,3,8,4,0,47,53,3,10,5,0,48,53,3,12,6,0,49,53,3,14,7,0,50,53,3,
        16,8,0,51,53,5,27,0,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,1,0,0,0,
        52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,
        0,0,0,53,3,1,0,0,0,54,55,5,5,0,0,55,60,5,33,0,0,56,57,5,28,0,0,57,
        59,5,33,0,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,
        0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,64,5,27,0,0,64,5,1,0,0,0,65,66,
        3,18,9,0,66,67,5,27,0,0,67,7,1,0,0,0,68,69,5,9,0,0,69,74,5,33,0,
        0,70,71,5,28,0,0,71,73,5,33,0,0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,27,0,0,
        78,9,1,0,0,0,79,80,5,10,0,0,80,85,3,18,9,0,81,82,5,28,0,0,82,84,
        3,18,9,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,27,0,0,89,11,1,0,0,0,90,94,5,
        31,0,0,91,93,3,2,1,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,
        95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,32,0,0,98,13,1,0,
        0,0,99,100,5,6,0,0,100,101,5,29,0,0,101,102,3,18,9,0,102,103,5,30,
        0,0,103,106,3,2,1,0,104,105,5,7,0,0,105,107,3,2,1,0,106,104,1,0,
        0,0,106,107,1,0,0,0,107,15,1,0,0,0,108,109,5,8,0,0,109,110,5,29,
        0,0,110,111,3,18,9,0,111,112,5,30,0,0,112,113,3,2,1,0,113,17,1,0,
        0,0,114,115,3,20,10,0,115,19,1,0,0,0,116,119,3,22,11,0,117,118,5,
        13,0,0,118,120,3,20,10,0,119,117,1,0,0,0,119,120,1,0,0,0,120,21,
        1,0,0,0,121,126,3,24,12,0,122,123,5,21,0,0,123,125,3,24,12,0,124,
        122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,
        23,1,0,0,0,128,126,1,0,0,0,129,134,3,26,13,0,130,131,5,20,0,0,131,
        133,3,26,13,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,25,1,0,0,0,136,134,1,0,0,0,137,142,3,28,14,0,138,
        139,7,0,0,0,139,141,3,28,14,0,140,138,1,0,0,0,141,144,1,0,0,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,27,1,0,0,0,144,142,1,0,0,0,145,150,
        3,30,15,0,146,147,7,1,0,0,147,149,3,30,15,0,148,146,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,29,1,0,0,0,152,150,
        1,0,0,0,153,158,3,32,16,0,154,155,7,2,0,0,155,157,3,32,16,0,156,
        154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        31,1,0,0,0,160,158,1,0,0,0,161,166,3,34,17,0,162,163,7,3,0,0,163,
        165,3,34,17,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,33,1,0,0,0,168,166,1,0,0,0,169,170,7,4,0,0,170,173,
        3,34,17,0,171,173,3,36,18,0,172,169,1,0,0,0,172,171,1,0,0,0,173,
        35,1,0,0,0,174,184,5,1,0,0,175,184,5,2,0,0,176,184,5,3,0,0,177,184,
        5,4,0,0,178,184,5,33,0,0,179,180,5,29,0,0,180,181,3,18,9,0,181,182,
        5,30,0,0,182,184,1,0,0,0,183,174,1,0,0,0,183,175,1,0,0,0,183,176,
        1,0,0,0,183,177,1,0,0,0,183,178,1,0,0,0,183,179,1,0,0,0,184,37,1,
        0,0,0,16,41,52,60,74,85,94,106,119,126,134,142,150,158,166,172,183
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'if'", "'else'", "'while'", 
                     "'read'", "'write'", "<INVALID>", "<INVALID>", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'.'", "'&&'", "'||'", 
                     "'!'", "'=='", "'!='", "'<'", "'>'", "';'", "','", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "BOOL", "STRING", "TYPE", 
                      "IF", "ELSE", "WHILE", "READ", "WRITE", "COMMENT", 
                      "WS", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", 
                      "SEMI", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_expressionStatement = 3
    RULE_readStatement = 4
    RULE_writeStatement = 5
    RULE_block = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_expression = 9
    RULE_assignment = 10
    RULE_logic_or = 11
    RULE_logic_and = 12
    RULE_equality = 13
    RULE_comparison = 14
    RULE_addition = 15
    RULE_multiplication = 16
    RULE_unary = 17
    RULE_primary = 18

    ruleNames =  [ "program", "statement", "declaration", "expressionStatement", 
                   "readStatement", "writeStatement", "block", "ifStatement", 
                   "whileStatement", "expression", "assignment", "logic_or", 
                   "logic_and", "equality", "comparison", "addition", "multiplication", 
                   "unary", "primary" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    BOOL=3
    STRING=4
    TYPE=5
    IF=6
    ELSE=7
    WHILE=8
    READ=9
    WRITE=10
    COMMENT=11
    WS=12
    ASSIGN=13
    PLUS=14
    MINUS=15
    MUL=16
    DIV=17
    MOD=18
    DOT=19
    AND=20
    OR=21
    NOT=22
    EQ=23
    NEQ=24
    LT=25
    GT=26
    SEMI=27
    COMMA=28
    LPAREN=29
    RPAREN=30
    LBRACE=31
    RBRACE=32
    ID=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11412735870) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MyLangParser.DeclarationContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionStatementContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(MyLangParser.ReadStatementContext,0)


        def writeStatement(self):
            return self.getTypedRuleContext(MyLangParser.WriteStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.declaration()
                pass
            elif token in [1, 2, 3, 4, 15, 22, 29, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.expressionStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.readStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.writeStatement()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.block()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.ifStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.whileStatement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 8)
                self.state = 51
                self.match(MyLangParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MyLangParser.TYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MyLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MyLangParser.TYPE)
            self.state = 55
            self.match(MyLangParser.ID)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 56
                self.match(MyLangParser.COMMA)
                self.state = 57
                self.match(MyLangParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MyLangParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.expression()
            self.state = 66
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(MyLangParser.READ, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.ID)
            else:
                return self.getToken(MyLangParser.ID, i)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_readStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)




    def readStatement(self):

        localctx = MyLangParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MyLangParser.READ)
            self.state = 69
            self.match(MyLangParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 70
                self.match(MyLangParser.COMMA)
                self.state = 71
                self.match(MyLangParser.ID)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(MyLangParser.WRITE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_writeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)




    def writeStatement(self):

        localctx = MyLangParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_writeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MyLangParser.WRITE)
            self.state = 80
            self.expression()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 81
                self.match(MyLangParser.COMMA)
                self.state = 82
                self.expression()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MyLangParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 11412735870) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MyLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(MyLangParser.IF)
            self.state = 100
            self.match(MyLangParser.LPAREN)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(MyLangParser.RPAREN)
            self.state = 103
            self.statement()
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(MyLangParser.ELSE)
                self.state = 105
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MyLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MyLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MyLangParser.WHILE)
            self.state = 109
            self.match(MyLangParser.LPAREN)
            self.state = 110
            self.expression()
            self.state = 111
            self.match(MyLangParser.RPAREN)
            self.state = 112
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MyLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_or(self):
            return self.getTypedRuleContext(MyLangParser.Logic_orContext,0)


        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.logic_or()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 117
                self.match(MyLangParser.ASSIGN)
                self.state = 118
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.Logic_andContext)
            else:
                return self.getTypedRuleContext(MyLangParser.Logic_andContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.OR)
            else:
                return self.getToken(MyLangParser.OR, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_logic_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_or" ):
                listener.enterLogic_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_or" ):
                listener.exitLogic_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_or" ):
                return visitor.visitLogic_or(self)
            else:
                return visitor.visitChildren(self)




    def logic_or(self):

        localctx = MyLangParser.Logic_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logic_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.logic_and()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 122
                self.match(MyLangParser.OR)
                self.state = 123
                self.logic_and()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.EqualityContext)
            else:
                return self.getTypedRuleContext(MyLangParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.AND)
            else:
                return self.getToken(MyLangParser.AND, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_logic_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_and" ):
                listener.enterLogic_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_and" ):
                listener.exitLogic_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_and" ):
                return visitor.visitLogic_and(self)
            else:
                return visitor.visitChildren(self)




    def logic_and(self):

        localctx = MyLangParser.Logic_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_logic_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.equality()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 130
                self.match(MyLangParser.AND)
                self.state = 131
                self.equality()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ComparisonContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.EQ)
            else:
                return self.getToken(MyLangParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.NEQ)
            else:
                return self.getToken(MyLangParser.NEQ, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = MyLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.comparison()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.comparison()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.AdditionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.AdditionContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.LT)
            else:
                return self.getToken(MyLangParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.GT)
            else:
                return self.getToken(MyLangParser.GT, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = MyLangParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.addition()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.addition()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.MultiplicationContext)
            else:
                return self.getTypedRuleContext(MyLangParser.MultiplicationContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.PLUS)
            else:
                return self.getToken(MyLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.MINUS)
            else:
                return self.getToken(MyLangParser.MINUS, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.DOT)
            else:
                return self.getToken(MyLangParser.DOT, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)




    def addition(self):

        localctx = MyLangParser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.multiplication()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 573440) != 0):
                self.state = 154
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 573440) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.multiplication()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.UnaryContext)
            else:
                return self.getTypedRuleContext(MyLangParser.UnaryContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.MUL)
            else:
                return self.getToken(MyLangParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.DIV)
            else:
                return self.getToken(MyLangParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.MOD)
            else:
                return self.getToken(MyLangParser.MOD, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_multiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)




    def multiplication(self):

        localctx = MyLangParser.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.unary()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0):
                self.state = 162
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.unary()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MyLangParser.UnaryContext,0)


        def NOT(self):
            return self.getToken(MyLangParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(MyLangParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MyLangParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==15 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self.unary()
                pass
            elif token in [1, 2, 3, 4, 29, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(MyLangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MyLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primary)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(MyLangParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(MyLangParser.FLOAT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(MyLangParser.BOOL)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(MyLangParser.STRING)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.match(MyLangParser.ID)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(MyLangParser.LPAREN)
                self.state = 180
                self.expression()
                self.state = 181
                self.match(MyLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





