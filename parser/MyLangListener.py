# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete listener for a parse tree produced by MyLangParser.
class MyLangListener(ParseTreeListener):

    # Enter a parse tree produced by MyLangParser#program.
    def enterProgram(self, ctx:MyLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLangParser#program.
    def exitProgram(self, ctx:MyLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLangParser#EmptyStmt.
    def enterEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#EmptyStmt.
    def exitEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#VarDecl.
    def enterVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MyLangParser#VarDecl.
    def exitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MyLangParser#ExprStmt.
    def enterExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ExprStmt.
    def exitExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#ReadStmt.
    def enterReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#ReadStmt.
    def exitReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#WriteStmt.
    def enterWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#WriteStmt.
    def exitWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#BlockStmt.
    def enterBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#BlockStmt.
    def exitBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#IfStmt.
    def enterIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#IfStmt.
    def exitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#WhileStmt.
    def enterWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MyLangParser#WhileStmt.
    def exitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MyLangParser#AndExpr.
    def enterAndExpr(self, ctx:MyLangParser.AndExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AndExpr.
    def exitAndExpr(self, ctx:MyLangParser.AndExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#MulExpr.
    def enterMulExpr(self, ctx:MyLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#MulExpr.
    def exitMulExpr(self, ctx:MyLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#RelExpr.
    def enterRelExpr(self, ctx:MyLangParser.RelExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#RelExpr.
    def exitRelExpr(self, ctx:MyLangParser.RelExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#EqExpr.
    def enterEqExpr(self, ctx:MyLangParser.EqExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#EqExpr.
    def exitEqExpr(self, ctx:MyLangParser.EqExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#NegExpr.
    def enterNegExpr(self, ctx:MyLangParser.NegExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#NegExpr.
    def exitNegExpr(self, ctx:MyLangParser.NegExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#ParensExpr.
    def enterParensExpr(self, ctx:MyLangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#ParensExpr.
    def exitParensExpr(self, ctx:MyLangParser.ParensExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#VarExpr.
    def enterVarExpr(self, ctx:MyLangParser.VarExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#VarExpr.
    def exitVarExpr(self, ctx:MyLangParser.VarExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#AddExpr.
    def enterAddExpr(self, ctx:MyLangParser.AddExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AddExpr.
    def exitAddExpr(self, ctx:MyLangParser.AddExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#NotExpr.
    def enterNotExpr(self, ctx:MyLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#NotExpr.
    def exitNotExpr(self, ctx:MyLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#OrExpr.
    def enterOrExpr(self, ctx:MyLangParser.OrExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#OrExpr.
    def exitOrExpr(self, ctx:MyLangParser.OrExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#AssignExpr.
    def enterAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        pass

    # Exit a parse tree produced by MyLangParser#AssignExpr.
    def exitAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        pass


    # Enter a parse tree produced by MyLangParser#type.
    def enterType(self, ctx:MyLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLangParser#type.
    def exitType(self, ctx:MyLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLangParser#literal.
    def enterLiteral(self, ctx:MyLangParser.LiteralContext):
        pass

    # Exit a parse tree produced by MyLangParser#literal.
    def exitLiteral(self, ctx:MyLangParser.LiteralContext):
        pass



del MyLangParser