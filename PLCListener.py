# Generated from PLC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PLCParser import PLCParser
else:
    from PLCParser import PLCParser

# This class defines a complete listener for a parse tree produced by PLCParser.
class PLCListener(ParseTreeListener):

    # Enter a parse tree produced by PLCParser#program.
    def enterProgram(self, ctx:PLCParser.ProgramContext):
        pass

    # Exit a parse tree produced by PLCParser#program.
    def exitProgram(self, ctx:PLCParser.ProgramContext):
        pass


    # Enter a parse tree produced by PLCParser#statement.
    def enterStatement(self, ctx:PLCParser.StatementContext):
        pass

    # Exit a parse tree produced by PLCParser#statement.
    def exitStatement(self, ctx:PLCParser.StatementContext):
        pass


    # Enter a parse tree produced by PLCParser#declaration.
    def enterDeclaration(self, ctx:PLCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLCParser#declaration.
    def exitDeclaration(self, ctx:PLCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:PLCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#readStatement.
    def enterReadStatement(self, ctx:PLCParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#readStatement.
    def exitReadStatement(self, ctx:PLCParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#writeStatement.
    def enterWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#writeStatement.
    def exitWriteStatement(self, ctx:PLCParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#block.
    def enterBlock(self, ctx:PLCParser.BlockContext):
        pass

    # Exit a parse tree produced by PLCParser#block.
    def exitBlock(self, ctx:PLCParser.BlockContext):
        pass


    # Enter a parse tree produced by PLCParser#ifStatement.
    def enterIfStatement(self, ctx:PLCParser.IfStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#ifStatement.
    def exitIfStatement(self, ctx:PLCParser.IfStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#whileStatement.
    def enterWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#whileStatement.
    def exitWhileStatement(self, ctx:PLCParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#forStatement.
    def enterForStatement(self, ctx:PLCParser.ForStatementContext):
        pass

    # Exit a parse tree produced by PLCParser#forStatement.
    def exitForStatement(self, ctx:PLCParser.ForStatementContext):
        pass


    # Enter a parse tree produced by PLCParser#expression.
    def enterExpression(self, ctx:PLCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLCParser#expression.
    def exitExpression(self, ctx:PLCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLCParser#assignment.
    def enterAssignment(self, ctx:PLCParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PLCParser#assignment.
    def exitAssignment(self, ctx:PLCParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PLCParser#logic_or.
    def enterLogic_or(self, ctx:PLCParser.Logic_orContext):
        pass

    # Exit a parse tree produced by PLCParser#logic_or.
    def exitLogic_or(self, ctx:PLCParser.Logic_orContext):
        pass


    # Enter a parse tree produced by PLCParser#logic_and.
    def enterLogic_and(self, ctx:PLCParser.Logic_andContext):
        pass

    # Exit a parse tree produced by PLCParser#logic_and.
    def exitLogic_and(self, ctx:PLCParser.Logic_andContext):
        pass


    # Enter a parse tree produced by PLCParser#equality.
    def enterEquality(self, ctx:PLCParser.EqualityContext):
        pass

    # Exit a parse tree produced by PLCParser#equality.
    def exitEquality(self, ctx:PLCParser.EqualityContext):
        pass


    # Enter a parse tree produced by PLCParser#comparison.
    def enterComparison(self, ctx:PLCParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PLCParser#comparison.
    def exitComparison(self, ctx:PLCParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PLCParser#addition.
    def enterAddition(self, ctx:PLCParser.AdditionContext):
        pass

    # Exit a parse tree produced by PLCParser#addition.
    def exitAddition(self, ctx:PLCParser.AdditionContext):
        pass


    # Enter a parse tree produced by PLCParser#multiplication.
    def enterMultiplication(self, ctx:PLCParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by PLCParser#multiplication.
    def exitMultiplication(self, ctx:PLCParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by PLCParser#unary.
    def enterUnary(self, ctx:PLCParser.UnaryContext):
        pass

    # Exit a parse tree produced by PLCParser#unary.
    def exitUnary(self, ctx:PLCParser.UnaryContext):
        pass


    # Enter a parse tree produced by PLCParser#primary.
    def enterPrimary(self, ctx:PLCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PLCParser#primary.
    def exitPrimary(self, ctx:PLCParser.PrimaryContext):
        pass



del PLCParser