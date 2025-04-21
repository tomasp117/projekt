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


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#declaration.
    def visitDeclaration(self, ctx:MyLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MyLangParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#readStatement.
    def visitReadStatement(self, ctx:MyLangParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#writeStatement.
    def visitWriteStatement(self, ctx:MyLangParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifStatement.
    def visitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#writeFileStatement.
    def visitWriteFileStatement(self, ctx:MyLangParser.WriteFileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expression.
    def visitExpression(self, ctx:MyLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignment.
    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#logic_or.
    def visitLogic_or(self, ctx:MyLangParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#logic_and.
    def visitLogic_and(self, ctx:MyLangParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#equality.
    def visitEquality(self, ctx:MyLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#comparison.
    def visitComparison(self, ctx:MyLangParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#addition.
    def visitAddition(self, ctx:MyLangParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#multiplication.
    def visitMultiplication(self, ctx:MyLangParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#unary.
    def visitUnary(self, ctx:MyLangParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#primary.
    def visitPrimary(self, ctx:MyLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del MyLangParser