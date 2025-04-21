// Generated from c:/Users/Tomáš/Documents/VSB/PJP/projekt/MyLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyLangParser}.
 */
public interface MyLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MyLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MyLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MyLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MyLangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MyLangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(MyLangParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(MyLangParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(MyLangParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(MyLangParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(MyLangParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#readStatement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(MyLangParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void enterWriteStatement(MyLangParser.WriteStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#writeStatement}.
	 * @param ctx the parse tree
	 */
	void exitWriteStatement(MyLangParser.WriteStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MyLangParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MyLangParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(MyLangParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(MyLangParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(MyLangParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(MyLangParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(MyLangParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(MyLangParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(MyLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(MyLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#logic_or}.
	 * @param ctx the parse tree
	 */
	void enterLogic_or(MyLangParser.Logic_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#logic_or}.
	 * @param ctx the parse tree
	 */
	void exitLogic_or(MyLangParser.Logic_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#logic_and}.
	 * @param ctx the parse tree
	 */
	void enterLogic_and(MyLangParser.Logic_andContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#logic_and}.
	 * @param ctx the parse tree
	 */
	void exitLogic_and(MyLangParser.Logic_andContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterEquality(MyLangParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitEquality(MyLangParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#comparison}.
	 * @param ctx the parse tree
	 */
	void enterComparison(MyLangParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#comparison}.
	 * @param ctx the parse tree
	 */
	void exitComparison(MyLangParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#addition}.
	 * @param ctx the parse tree
	 */
	void enterAddition(MyLangParser.AdditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#addition}.
	 * @param ctx the parse tree
	 */
	void exitAddition(MyLangParser.AdditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void enterMultiplication(MyLangParser.MultiplicationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#multiplication}.
	 * @param ctx the parse tree
	 */
	void exitMultiplication(MyLangParser.MultiplicationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterUnary(MyLangParser.UnaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitUnary(MyLangParser.UnaryContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLangParser#primary}.
	 * @param ctx the parse tree
	 */
	void enterPrimary(MyLangParser.PrimaryContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLangParser#primary}.
	 * @param ctx the parse tree
	 */
	void exitPrimary(MyLangParser.PrimaryContext ctx);
}