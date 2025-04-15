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
        4,1,36,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,
        1,41,9,1,1,1,1,1,1,1,1,1,1,1,5,1,48,8,1,10,1,12,1,51,9,1,1,1,1,1,
        1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,70,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,78,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        114,8,2,10,2,12,2,117,9,2,1,3,1,3,1,4,1,4,1,4,0,1,4,5,0,2,4,6,8,
        0,6,1,0,23,24,1,0,25,26,2,0,17,18,30,30,1,0,19,21,1,0,6,9,1,0,10,
        13,141,0,13,1,0,0,0,2,77,1,0,0,0,4,90,1,0,0,0,6,118,1,0,0,0,8,120,
        1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,
        13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,
        0,0,18,78,5,35,0,0,19,20,3,6,3,0,20,25,5,14,0,0,21,22,5,36,0,0,22,
        24,5,14,0,0,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,
        0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,35,0,0,29,78,1,0,0,0,30,
        31,3,4,2,0,31,32,5,35,0,0,32,78,1,0,0,0,33,34,5,1,0,0,34,39,5,14,
        0,0,35,36,5,36,0,0,36,38,5,14,0,0,37,35,1,0,0,0,38,41,1,0,0,0,39,
        37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,78,5,35,
        0,0,43,44,5,2,0,0,44,49,3,4,2,0,45,46,5,36,0,0,46,48,3,4,2,0,47,
        45,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,
        0,51,49,1,0,0,0,52,53,5,35,0,0,53,78,1,0,0,0,54,58,5,33,0,0,55,57,
        3,2,1,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,
        59,61,1,0,0,0,60,58,1,0,0,0,61,78,5,34,0,0,62,63,5,3,0,0,63,64,5,
        31,0,0,64,65,3,4,2,0,65,66,5,32,0,0,66,69,3,2,1,0,67,68,5,4,0,0,
        68,70,3,2,1,0,69,67,1,0,0,0,69,70,1,0,0,0,70,78,1,0,0,0,71,72,5,
        5,0,0,72,73,5,31,0,0,73,74,3,4,2,0,74,75,5,32,0,0,75,76,3,2,1,0,
        76,78,1,0,0,0,77,18,1,0,0,0,77,19,1,0,0,0,77,30,1,0,0,0,77,33,1,
        0,0,0,77,43,1,0,0,0,77,54,1,0,0,0,77,62,1,0,0,0,77,71,1,0,0,0,78,
        3,1,0,0,0,79,80,6,2,-1,0,80,81,5,29,0,0,81,91,3,4,2,5,82,83,5,18,
        0,0,83,91,3,4,2,4,84,85,5,31,0,0,85,86,3,4,2,0,86,87,5,32,0,0,87,
        91,1,0,0,0,88,91,3,8,4,0,89,91,5,14,0,0,90,79,1,0,0,0,90,82,1,0,
        0,0,90,84,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,115,1,0,0,0,92,
        93,10,12,0,0,93,94,5,22,0,0,94,114,3,4,2,12,95,96,10,11,0,0,96,97,
        5,28,0,0,97,114,3,4,2,12,98,99,10,10,0,0,99,100,5,27,0,0,100,114,
        3,4,2,11,101,102,10,9,0,0,102,103,7,0,0,0,103,114,3,4,2,10,104,105,
        10,8,0,0,105,106,7,1,0,0,106,114,3,4,2,9,107,108,10,7,0,0,108,109,
        7,2,0,0,109,114,3,4,2,8,110,111,10,6,0,0,111,112,7,3,0,0,112,114,
        3,4,2,7,113,92,1,0,0,0,113,95,1,0,0,0,113,98,1,0,0,0,113,101,1,0,
        0,0,113,104,1,0,0,0,113,107,1,0,0,0,113,110,1,0,0,0,114,117,1,0,
        0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,5,1,0,0,0,117,115,1,0,0,
        0,118,119,7,4,0,0,119,7,1,0,0,0,120,121,7,5,0,0,121,9,1,0,0,0,10,
        13,25,39,49,58,69,77,90,113,115
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'write'", "'if'", "'else'", 
                     "'while'", "'int'", "'float'", "'bool'", "'string'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'='", "'=='", "'!='", "'<'", 
                     "'>'", "'&&'", "'||'", "'!'", "'.'", "'('", "')'", 
                     "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "INT", "FLOAT", 
                      "STRING", "ID", "WS", "LINE_COMMENT", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "ASSIGN", "EQ", "NEQ", "LT", 
                      "GT", "AND", "OR", "NOT", "DOT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMI", "COMMA" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_type = 3
    RULE_literal = 4

    ruleNames =  [ "program", "statement", "expression", "type", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    BOOL=10
    INT=11
    FLOAT=12
    STRING=13
    ID=14
    WS=15
    LINE_COMMENT=16
    PLUS=17
    MINUS=18
    MUL=19
    DIV=20
    MOD=21
    ASSIGN=22
    EQ=23
    NEQ=24
    LT=25
    GT=26
    AND=27
    OR=28
    NOT=29
    DOT=30
    LPAREN=31
    RPAREN=32
    LBRACE=33
    RBRACE=34
    SEMI=35
    COMMA=36

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

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 45634322414) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(MyLangParser.EOF)
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


        def getRuleIndex(self):
            return MyLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(MyLangParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                localctx = MyLangParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(MyLangParser.SEMI)
                pass
            elif token in [6, 7, 8, 9]:
                localctx = MyLangParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.type_()
                self.state = 20
                self.match(MyLangParser.ID)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 21
                    self.match(MyLangParser.COMMA)
                    self.state = 22
                    self.match(MyLangParser.ID)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(MyLangParser.SEMI)
                pass
            elif token in [10, 11, 12, 13, 14, 18, 29, 31]:
                localctx = MyLangParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.expression(0)
                self.state = 31
                self.match(MyLangParser.SEMI)
                pass
            elif token in [1]:
                localctx = MyLangParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.match(MyLangParser.T__0)
                self.state = 34
                self.match(MyLangParser.ID)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 35
                    self.match(MyLangParser.COMMA)
                    self.state = 36
                    self.match(MyLangParser.ID)
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(MyLangParser.SEMI)
                pass
            elif token in [2]:
                localctx = MyLangParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(MyLangParser.T__1)
                self.state = 44
                self.expression(0)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 45
                    self.match(MyLangParser.COMMA)
                    self.state = 46
                    self.expression(0)
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 52
                self.match(MyLangParser.SEMI)
                pass
            elif token in [33]:
                localctx = MyLangParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.match(MyLangParser.LBRACE)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 45634322414) != 0):
                    self.state = 55
                    self.statement()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 61
                self.match(MyLangParser.RBRACE)
                pass
            elif token in [3]:
                localctx = MyLangParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.match(MyLangParser.T__2)
                self.state = 63
                self.match(MyLangParser.LPAREN)
                self.state = 64
                self.expression(0)
                self.state = 65
                self.match(MyLangParser.RPAREN)
                self.state = 66
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.match(MyLangParser.T__3)
                    self.state = 68
                    self.statement()


                pass
            elif token in [5]:
                localctx = MyLangParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.match(MyLangParser.T__4)
                self.state = 72
                self.match(MyLangParser.LPAREN)
                self.state = 73
                self.expression(0)
                self.state = 74
                self.match(MyLangParser.RPAREN)
                self.state = 75
                self.statement()
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(MyLangParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(MyLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MyLangParser.DIV, 0)
        def MOD(self):
            return self.getToken(MyLangParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(MyLangParser.LT, 0)
        def GT(self):
            return self.getToken(MyLangParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(MyLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MyLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(MyLangParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)
        def DOT(self):
            return self.getToken(MyLangParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MyLangParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(MyLangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = MyLangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(MyLangParser.NOT)
                self.state = 81
                self.expression(5)
                pass
            elif token in [18]:
                localctx = MyLangParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(MyLangParser.MINUS)
                self.state = 83
                self.expression(4)
                pass
            elif token in [31]:
                localctx = MyLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(MyLangParser.LPAREN)
                self.state = 85
                self.expression(0)
                self.state = 86
                self.match(MyLangParser.RPAREN)
                pass
            elif token in [10, 11, 12, 13]:
                localctx = MyLangParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.literal()
                pass
            elif token in [14]:
                localctx = MyLangParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(MyLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 113
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.AssignExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 93
                        self.match(MyLangParser.ASSIGN)
                        self.state = 94
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.OrExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 96
                        self.match(MyLangParser.OR)
                        self.state = 97
                        self.expression(12)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.AndExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 99
                        self.match(MyLangParser.AND)
                        self.state = 100
                        self.expression(11)
                        pass

                    elif la_ == 4:
                        localctx = MyLangParser.EqExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 102
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        self.expression(10)
                        pass

                    elif la_ == 5:
                        localctx = MyLangParser.RelExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 105
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expression(9)
                        pass

                    elif la_ == 6:
                        localctx = MyLangParser.AddExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 108
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1074135040) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expression(8)
                        pass

                    elif la_ == 7:
                        localctx = MyLangParser.MulExprContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expression(7)
                        pass

             
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MyLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyLangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def BOOL(self):
            return self.getToken(MyLangParser.BOOL, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MyLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         




