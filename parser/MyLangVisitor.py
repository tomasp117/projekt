# Generated from MyLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLangParser import MyLangParser
else:
    from MyLangParser import MyLangParser

# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#EmptyStmt.
    def visitEmptyStmt(self, ctx:MyLangParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#VarDecl.
    def visitVarDecl(self, ctx:MyLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprStmt.
    def visitExprStmt(self, ctx:MyLangParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ReadStmt.
    def visitReadStmt(self, ctx:MyLangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#WriteStmt.
    def visitWriteStmt(self, ctx:MyLangParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#BlockStmt.
    def visitBlockStmt(self, ctx:MyLangParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#IfStmt.
    def visitIfStmt(self, ctx:MyLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#WhileStmt.
    def visitWhileStmt(self, ctx:MyLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AndExpr.
    def visitAndExpr(self, ctx:MyLangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#MulExpr.
    def visitMulExpr(self, ctx:MyLangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#RelExpr.
    def visitRelExpr(self, ctx:MyLangParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#EqExpr.
    def visitEqExpr(self, ctx:MyLangParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#NegExpr.
    def visitNegExpr(self, ctx:MyLangParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ParensExpr.
    def visitParensExpr(self, ctx:MyLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:MyLangParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#VarExpr.
    def visitVarExpr(self, ctx:MyLangParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AddExpr.
    def visitAddExpr(self, ctx:MyLangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#NotExpr.
    def visitNotExpr(self, ctx:MyLangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#OrExpr.
    def visitOrExpr(self, ctx:MyLangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#AssignExpr.
    def visitAssignExpr(self, ctx:MyLangParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#type.
    def visitType(self, ctx:MyLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#literal.
    def visitLiteral(self, ctx:MyLangParser.LiteralContext):
        return self.visitChildren(ctx)



del MyLangParser