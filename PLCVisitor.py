# Generated from PLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLCParser import PLCParser
else:
    from PLCParser import PLCParser

# This class defines a complete generic visitor for a parse tree produced by PLCParser.

class PLCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLCParser#program.
    def visitProgram(self, ctx:PLCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#statement.
    def visitStatement(self, ctx:PLCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#declaration.
    def visitDeclaration(self, ctx:PLCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#expressionStatement.
    def visitExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#readStatement.
    def visitReadStatement(self, ctx:PLCParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#writeStatement.
    def visitWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#block.
    def visitBlock(self, ctx:PLCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#ifStatement.
    def visitIfStatement(self, ctx:PLCParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#whileStatement.
    def visitWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#forStatement.
    def visitForStatement(self, ctx:PLCParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#expression.
    def visitExpression(self, ctx:PLCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#assignment.
    def visitAssignment(self, ctx:PLCParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#logic_or.
    def visitLogic_or(self, ctx:PLCParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#logic_and.
    def visitLogic_and(self, ctx:PLCParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#equality.
    def visitEquality(self, ctx:PLCParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#comparison.
    def visitComparison(self, ctx:PLCParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#addition.
    def visitAddition(self, ctx:PLCParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#multiplication.
    def visitMultiplication(self, ctx:PLCParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#unary.
    def visitUnary(self, ctx:PLCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLCParser#primary.
    def visitPrimary(self, ctx:PLCParser.PrimaryContext):
        return self.visitChildren(ctx)



del PLCParser