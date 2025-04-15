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


    # Enter a parse tree produced by MyLangParser#statement.
    def enterStatement(self, ctx:MyLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#statement.
    def exitStatement(self, ctx:MyLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#declaration.
    def enterDeclaration(self, ctx:MyLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MyLangParser#declaration.
    def exitDeclaration(self, ctx:MyLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MyLangParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MyLangParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MyLangParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#readStatement.
    def enterReadStatement(self, ctx:MyLangParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#readStatement.
    def exitReadStatement(self, ctx:MyLangParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#writeStatement.
    def enterWriteStatement(self, ctx:MyLangParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#writeStatement.
    def exitWriteStatement(self, ctx:MyLangParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#block.
    def enterBlock(self, ctx:MyLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MyLangParser#block.
    def exitBlock(self, ctx:MyLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MyLangParser#ifStatement.
    def enterIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#ifStatement.
    def exitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#whileStatement.
    def enterWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MyLangParser#whileStatement.
    def exitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MyLangParser#expression.
    def enterExpression(self, ctx:MyLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyLangParser#expression.
    def exitExpression(self, ctx:MyLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyLangParser#assignment.
    def enterAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyLangParser#assignment.
    def exitAssignment(self, ctx:MyLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyLangParser#logic_or.
    def enterLogic_or(self, ctx:MyLangParser.Logic_orContext):
        pass

    # Exit a parse tree produced by MyLangParser#logic_or.
    def exitLogic_or(self, ctx:MyLangParser.Logic_orContext):
        pass


    # Enter a parse tree produced by MyLangParser#logic_and.
    def enterLogic_and(self, ctx:MyLangParser.Logic_andContext):
        pass

    # Exit a parse tree produced by MyLangParser#logic_and.
    def exitLogic_and(self, ctx:MyLangParser.Logic_andContext):
        pass


    # Enter a parse tree produced by MyLangParser#equality.
    def enterEquality(self, ctx:MyLangParser.EqualityContext):
        pass

    # Exit a parse tree produced by MyLangParser#equality.
    def exitEquality(self, ctx:MyLangParser.EqualityContext):
        pass


    # Enter a parse tree produced by MyLangParser#comparison.
    def enterComparison(self, ctx:MyLangParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MyLangParser#comparison.
    def exitComparison(self, ctx:MyLangParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MyLangParser#addition.
    def enterAddition(self, ctx:MyLangParser.AdditionContext):
        pass

    # Exit a parse tree produced by MyLangParser#addition.
    def exitAddition(self, ctx:MyLangParser.AdditionContext):
        pass


    # Enter a parse tree produced by MyLangParser#multiplication.
    def enterMultiplication(self, ctx:MyLangParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by MyLangParser#multiplication.
    def exitMultiplication(self, ctx:MyLangParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by MyLangParser#unary.
    def enterUnary(self, ctx:MyLangParser.UnaryContext):
        pass

    # Exit a parse tree produced by MyLangParser#unary.
    def exitUnary(self, ctx:MyLangParser.UnaryContext):
        pass


    # Enter a parse tree produced by MyLangParser#primary.
    def enterPrimary(self, ctx:MyLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MyLangParser#primary.
    def exitPrimary(self, ctx:MyLangParser.PrimaryContext):
        pass



del MyLangParser