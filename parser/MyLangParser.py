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
        4,1,35,202,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,56,8,1,1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,1,2,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,76,8,4,10,4,12,4,79,9,4,1,4,1,4,1,
        5,1,5,1,5,1,5,5,5,87,8,5,10,5,12,5,90,9,5,1,5,1,5,1,6,1,6,5,6,96,
        8,6,10,6,12,6,99,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,110,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,123,8,9,10,9,
        12,9,126,9,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,3,11,135,8,11,1,12,
        1,12,1,12,5,12,140,8,12,10,12,12,12,143,9,12,1,13,1,13,1,13,5,13,
        148,8,13,10,13,12,13,151,9,13,1,14,1,14,1,14,5,14,156,8,14,10,14,
        12,14,159,9,14,1,15,1,15,1,15,5,15,164,8,15,10,15,12,15,167,9,15,
        1,16,1,16,1,16,5,16,172,8,16,10,16,12,16,175,9,16,1,17,1,17,1,17,
        5,17,180,8,17,10,17,12,17,183,9,17,1,18,1,18,1,18,3,18,188,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,200,8,19,
        1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,0,5,1,0,24,25,1,0,26,27,2,0,15,16,20,20,1,0,17,19,2,0,16,16,23,
        23,210,0,43,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,68,1,0,0,0,8,71,
        1,0,0,0,10,82,1,0,0,0,12,93,1,0,0,0,14,102,1,0,0,0,16,111,1,0,0,
        0,18,117,1,0,0,0,20,129,1,0,0,0,22,131,1,0,0,0,24,136,1,0,0,0,26,
        144,1,0,0,0,28,152,1,0,0,0,30,160,1,0,0,0,32,168,1,0,0,0,34,176,
        1,0,0,0,36,187,1,0,0,0,38,199,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,
        0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,1,1,0,0,0,45,43,1,
        0,0,0,46,56,3,4,2,0,47,56,3,6,3,0,48,56,3,8,4,0,49,56,3,10,5,0,50,
        56,3,12,6,0,51,56,3,14,7,0,52,56,3,16,8,0,53,56,3,18,9,0,54,56,5,
        28,0,0,55,46,1,0,0,0,55,47,1,0,0,0,55,48,1,0,0,0,55,49,1,0,0,0,55,
        50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,
        0,56,3,1,0,0,0,57,58,5,6,0,0,58,63,5,35,0,0,59,60,5,29,0,0,60,62,
        5,35,0,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,28,0,0,67,5,1,0,0,0,68,69,3,
        20,10,0,69,70,5,28,0,0,70,7,1,0,0,0,71,72,5,10,0,0,72,77,5,35,0,
        0,73,74,5,29,0,0,74,76,5,35,0,0,75,73,1,0,0,0,76,79,1,0,0,0,77,75,
        1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,28,0,0,
        81,9,1,0,0,0,82,83,5,11,0,0,83,88,3,20,10,0,84,85,5,29,0,0,85,87,
        3,20,10,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,
        0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,5,28,0,0,92,11,1,0,0,0,93,97,
        5,32,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,
        97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,5,33,0,0,101,
        13,1,0,0,0,102,103,5,7,0,0,103,104,5,30,0,0,104,105,3,20,10,0,105,
        106,5,31,0,0,106,109,3,2,1,0,107,108,5,8,0,0,108,110,3,2,1,0,109,
        107,1,0,0,0,109,110,1,0,0,0,110,15,1,0,0,0,111,112,5,9,0,0,112,113,
        5,30,0,0,113,114,3,20,10,0,114,115,5,31,0,0,115,116,3,2,1,0,116,
        17,1,0,0,0,117,118,5,35,0,0,118,119,5,34,0,0,119,124,3,20,10,0,120,
        121,5,34,0,0,121,123,3,20,10,0,122,120,1,0,0,0,123,126,1,0,0,0,124,
        122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,
        128,5,28,0,0,128,19,1,0,0,0,129,130,3,22,11,0,130,21,1,0,0,0,131,
        134,3,24,12,0,132,133,5,14,0,0,133,135,3,22,11,0,134,132,1,0,0,0,
        134,135,1,0,0,0,135,23,1,0,0,0,136,141,3,26,13,0,137,138,5,22,0,
        0,138,140,3,26,13,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,
        0,0,141,142,1,0,0,0,142,25,1,0,0,0,143,141,1,0,0,0,144,149,3,28,
        14,0,145,146,5,21,0,0,146,148,3,28,14,0,147,145,1,0,0,0,148,151,
        1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,27,1,0,0,0,151,149,1,
        0,0,0,152,157,3,30,15,0,153,154,7,0,0,0,154,156,3,30,15,0,155,153,
        1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,29,1,
        0,0,0,159,157,1,0,0,0,160,165,3,32,16,0,161,162,7,1,0,0,162,164,
        3,32,16,0,163,161,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,31,1,0,0,0,167,165,1,0,0,0,168,173,3,34,17,0,169,170,
        7,2,0,0,170,172,3,34,17,0,171,169,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,33,1,0,0,0,175,173,1,0,0,0,176,181,3,
        36,18,0,177,178,7,3,0,0,178,180,3,36,18,0,179,177,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,35,1,0,0,0,183,181,1,
        0,0,0,184,185,7,4,0,0,185,188,3,36,18,0,186,188,3,38,19,0,187,184,
        1,0,0,0,187,186,1,0,0,0,188,37,1,0,0,0,189,200,5,1,0,0,190,200,5,
        2,0,0,191,200,5,3,0,0,192,200,5,4,0,0,193,200,5,5,0,0,194,200,5,
        35,0,0,195,196,5,30,0,0,196,197,3,20,10,0,197,198,5,31,0,0,198,200,
        1,0,0,0,199,189,1,0,0,0,199,190,1,0,0,0,199,191,1,0,0,0,199,192,
        1,0,0,0,199,193,1,0,0,0,199,194,1,0,0,0,199,195,1,0,0,0,200,39,1,
        0,0,0,17,43,55,63,77,88,97,109,124,134,141,149,157,165,173,181,187,
        199
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'while'", "'read'", "'write'", "<INVALID>", "<INVALID>", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'.'", "'&&'", 
                     "'||'", "'!'", "'=='", "'!='", "'<'", "'>'", "';'", 
                     "','", "'('", "')'", "'{'", "'}'", "'<<'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "BOOL", "STRING", "FILE", 
                      "TYPE", "IF", "ELSE", "WHILE", "READ", "WRITE", "COMMENT", 
                      "WS", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", 
                      "SEMI", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "BITLEFT", "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_expressionStatement = 3
    RULE_readStatement = 4
    RULE_writeStatement = 5
    RULE_block = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_writeFileStatement = 9
    RULE_expression = 10
    RULE_assignment = 11
    RULE_logic_or = 12
    RULE_logic_and = 13
    RULE_equality = 14
    RULE_comparison = 15
    RULE_addition = 16
    RULE_multiplication = 17
    RULE_unary = 18
    RULE_primary = 19

    ruleNames =  [ "program", "statement", "declaration", "expressionStatement", 
                   "readStatement", "writeStatement", "block", "ifStatement", 
                   "whileStatement", "writeFileStatement", "expression", 
                   "assignment", "logic_or", "logic_and", "equality", "comparison", 
                   "addition", "multiplication", "unary", "primary" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    BOOL=3
    STRING=4
    FILE=5
    TYPE=6
    IF=7
    ELSE=8
    WHILE=9
    READ=10
    WRITE=11
    COMMENT=12
    WS=13
    ASSIGN=14
    PLUS=15
    MINUS=16
    MUL=17
    DIV=18
    MOD=19
    DOT=20
    AND=21
    OR=22
    NOT=23
    EQ=24
    NEQ=25
    LT=26
    GT=27
    SEMI=28
    COMMA=29
    LPAREN=30
    RPAREN=31
    LBRACE=32
    RBRACE=33
    BITLEFT=34
    ID=35

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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 40005340926) != 0):
                self.state = 40
                self.statement()
                self.state = 45
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


        def writeFileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WriteFileStatementContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.expressionStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.readStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.writeStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.writeFileStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.match(MyLangParser.SEMI)
                pass


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
            self.state = 57
            self.match(MyLangParser.TYPE)
            self.state = 58
            self.match(MyLangParser.ID)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 59
                self.match(MyLangParser.COMMA)
                self.state = 60
                self.match(MyLangParser.ID)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 68
            self.expression()
            self.state = 69
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
            self.state = 71
            self.match(MyLangParser.READ)
            self.state = 72
            self.match(MyLangParser.ID)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 73
                self.match(MyLangParser.COMMA)
                self.state = 74
                self.match(MyLangParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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
            self.state = 82
            self.match(MyLangParser.WRITE)
            self.state = 83
            self.expression()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 84
                self.match(MyLangParser.COMMA)
                self.state = 85
                self.expression()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
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
            self.state = 93
            self.match(MyLangParser.LBRACE)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 40005340926) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
            self.state = 102
            self.match(MyLangParser.IF)
            self.state = 103
            self.match(MyLangParser.LPAREN)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(MyLangParser.RPAREN)
            self.state = 106
            self.statement()
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(MyLangParser.ELSE)
                self.state = 108
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
            self.state = 111
            self.match(MyLangParser.WHILE)
            self.state = 112
            self.match(MyLangParser.LPAREN)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(MyLangParser.RPAREN)
            self.state = 115
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteFileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def BITLEFT(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.BITLEFT)
            else:
                return self.getToken(MyLangParser.BITLEFT, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_writeFileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteFileStatement" ):
                listener.enterWriteFileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteFileStatement" ):
                listener.exitWriteFileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteFileStatement" ):
                return visitor.visitWriteFileStatement(self)
            else:
                return visitor.visitChildren(self)




    def writeFileStatement(self):

        localctx = MyLangParser.WriteFileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_writeFileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MyLangParser.ID)
            self.state = 118
            self.match(MyLangParser.BITLEFT)
            self.state = 119
            self.expression()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 120
                self.match(MyLangParser.BITLEFT)
                self.state = 121
                self.expression()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(MyLangParser.SEMI)
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
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 22, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.logic_or()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 132
                self.match(MyLangParser.ASSIGN)
                self.state = 133
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
        self.enterRule(localctx, 24, self.RULE_logic_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.logic_and()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 137
                self.match(MyLangParser.OR)
                self.state = 138
                self.logic_and()
                self.state = 143
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
        self.enterRule(localctx, 26, self.RULE_logic_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.equality()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 145
                self.match(MyLangParser.AND)
                self.state = 146
                self.equality()
                self.state = 151
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
        self.enterRule(localctx, 28, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.comparison()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 153
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.comparison()
                self.state = 159
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
        self.enterRule(localctx, 30, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.addition()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.addition()
                self.state = 167
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
        self.enterRule(localctx, 32, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.multiplication()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1146880) != 0):
                self.state = 169
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1146880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self.multiplication()
                self.state = 175
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
        self.enterRule(localctx, 34, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.unary()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0):
                self.state = 177
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.unary()
                self.state = 183
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
        self.enterRule(localctx, 36, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                _la = self._input.LA(1)
                if not(_la==16 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.unary()
                pass
            elif token in [1, 2, 3, 4, 5, 30, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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

        def FILE(self):
            return self.getToken(MyLangParser.FILE, 0)

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
        self.enterRule(localctx, 38, self.RULE_primary)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(MyLangParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(MyLangParser.FLOAT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.match(MyLangParser.BOOL)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(MyLangParser.STRING)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
                self.match(MyLangParser.FILE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                self.match(MyLangParser.ID)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 7)
                self.state = 195
                self.match(MyLangParser.LPAREN)
                self.state = 196
                self.expression()
                self.state = 197
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





