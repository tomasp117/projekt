// Generated from c:/Users/Tomáš/Documents/VSB/PJP/projekt/PLC.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PLCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, BOOL=3, STRING=4, TYPE=5, IF=6, ELSE=7, WHILE=8, FOR=9, 
		READ=10, WRITE=11, COMMENT=12, WS=13, ASSIGN=14, PLUS=15, MINUS=16, MUL=17, 
		DIV=18, MOD=19, DOT=20, AND=21, OR=22, NOT=23, EQ=24, NEQ=25, LT=26, GT=27, 
		SEMI=28, COMMA=29, LPAREN=30, RPAREN=31, LBRACE=32, RBRACE=33, ID=34;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_declaration = 2, RULE_expressionStatement = 3, 
		RULE_readStatement = 4, RULE_writeStatement = 5, RULE_block = 6, RULE_ifStatement = 7, 
		RULE_whileStatement = 8, RULE_forStatement = 9, RULE_expression = 10, 
		RULE_assignment = 11, RULE_logic_or = 12, RULE_logic_and = 13, RULE_equality = 14, 
		RULE_comparison = 15, RULE_addition = 16, RULE_multiplication = 17, RULE_unary = 18, 
		RULE_primary = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "declaration", "expressionStatement", "readStatement", 
			"writeStatement", "block", "ifStatement", "whileStatement", "forStatement", 
			"expression", "assignment", "logic_or", "logic_and", "equality", "comparison", 
			"addition", "multiplication", "unary", "primary"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'if'", "'else'", "'while'", "'for'", 
			"'read'", "'write'", null, null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'.'", "'&&'", "'||'", "'!'", "'=='", "'!='", "'<'", "'>'", "';'", "','", 
			"'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INT", "FLOAT", "BOOL", "STRING", "TYPE", "IF", "ELSE", "WHILE", 
			"FOR", "READ", "WRITE", "COMMENT", "WS", "ASSIGN", "PLUS", "MINUS", "MUL", 
			"DIV", "MOD", "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", "SEMI", 
			"COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "ID"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PLC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PLCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 22825471870L) != 0)) {
				{
				{
				setState(40);
				statement();
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public ReadStatementContext readStatement() {
			return getRuleContext(ReadStatementContext.class,0);
		}
		public WriteStatementContext writeStatement() {
			return getRuleContext(WriteStatementContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public WhileStatementContext whileStatement() {
			return getRuleContext(WhileStatementContext.class,0);
		}
		public ForStatementContext forStatement() {
			return getRuleContext(ForStatementContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PLCParser.SEMI, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				declaration();
				}
				break;
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
			case MINUS:
			case NOT:
			case LPAREN:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				expressionStatement();
				}
				break;
			case READ:
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				readStatement();
				}
				break;
			case WRITE:
				enterOuterAlt(_localctx, 4);
				{
				setState(49);
				writeStatement();
				}
				break;
			case LBRACE:
				enterOuterAlt(_localctx, 5);
				{
				setState(50);
				block();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 6);
				{
				setState(51);
				ifStatement();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 7);
				{
				setState(52);
				whileStatement();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 8);
				{
				setState(53);
				forStatement();
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 9);
				{
				setState(54);
				match(SEMI);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(PLCParser.TYPE, 0); }
		public List<TerminalNode> ID() { return getTokens(PLCParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLCParser.ID, i);
		}
		public TerminalNode SEMI() { return getToken(PLCParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PLCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PLCParser.COMMA, i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(TYPE);
			setState(58);
			match(ID);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(59);
				match(COMMA);
				setState(60);
				match(ID);
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(PLCParser.SEMI, 0); }
		public ExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStatement; }
	}

	public final ExpressionStatementContext expressionStatement() throws RecognitionException {
		ExpressionStatementContext _localctx = new ExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expressionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			expression();
			setState(69);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadStatementContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(PLCParser.READ, 0); }
		public List<TerminalNode> ID() { return getTokens(PLCParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLCParser.ID, i);
		}
		public TerminalNode SEMI() { return getToken(PLCParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PLCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PLCParser.COMMA, i);
		}
		public ReadStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_readStatement; }
	}

	public final ReadStatementContext readStatement() throws RecognitionException {
		ReadStatementContext _localctx = new ReadStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_readStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(READ);
			setState(72);
			match(ID);
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(73);
				match(COMMA);
				setState(74);
				match(ID);
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(80);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteStatementContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(PLCParser.WRITE, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(PLCParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(PLCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PLCParser.COMMA, i);
		}
		public WriteStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_writeStatement; }
	}

	public final WriteStatementContext writeStatement() throws RecognitionException {
		WriteStatementContext _localctx = new WriteStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_writeStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(WRITE);
			setState(83);
			expression();
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(84);
				match(COMMA);
				setState(85);
				expression();
				}
				}
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(91);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(PLCParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(PLCParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(LBRACE);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 22825471870L) != 0)) {
				{
				{
				setState(94);
				statement();
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(100);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(PLCParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(PLCParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PLCParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(PLCParser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IF);
			setState(103);
			match(LPAREN);
			setState(104);
			expression();
			setState(105);
			match(RPAREN);
			setState(106);
			statement();
			setState(109);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(107);
				match(ELSE);
				setState(108);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(PLCParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(PLCParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PLCParser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatement; }
	}

	public final WhileStatementContext whileStatement() throws RecognitionException {
		WhileStatementContext _localctx = new WhileStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(WHILE);
			setState(112);
			match(LPAREN);
			setState(113);
			expression();
			setState(114);
			match(RPAREN);
			setState(115);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForStatementContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(PLCParser.FOR, 0); }
		public TerminalNode LPAREN() { return getToken(PLCParser.LPAREN, 0); }
		public TerminalNode TYPE() { return getToken(PLCParser.TYPE, 0); }
		public TerminalNode ID() { return getToken(PLCParser.ID, 0); }
		public List<TerminalNode> SEMI() { return getTokens(PLCParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(PLCParser.SEMI, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(PLCParser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ForStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStatement; }
	}

	public final ForStatementContext forStatement() throws RecognitionException {
		ForStatementContext _localctx = new ForStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_forStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(FOR);
			setState(118);
			match(LPAREN);
			setState(119);
			match(TYPE);
			setState(120);
			match(ID);
			setState(121);
			match(SEMI);
			setState(122);
			expression();
			setState(123);
			match(SEMI);
			setState(124);
			expression();
			setState(125);
			match(RPAREN);
			setState(126);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public Logic_orContext logic_or() {
			return getRuleContext(Logic_orContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(PLCParser.ASSIGN, 0); }
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			logic_or();
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(131);
				match(ASSIGN);
				setState(132);
				assignment();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logic_orContext extends ParserRuleContext {
		public List<Logic_andContext> logic_and() {
			return getRuleContexts(Logic_andContext.class);
		}
		public Logic_andContext logic_and(int i) {
			return getRuleContext(Logic_andContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(PLCParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(PLCParser.OR, i);
		}
		public Logic_orContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_or; }
	}

	public final Logic_orContext logic_or() throws RecognitionException {
		Logic_orContext _localctx = new Logic_orContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_logic_or);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			logic_and();
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(136);
				match(OR);
				setState(137);
				logic_and();
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logic_andContext extends ParserRuleContext {
		public List<EqualityContext> equality() {
			return getRuleContexts(EqualityContext.class);
		}
		public EqualityContext equality(int i) {
			return getRuleContext(EqualityContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(PLCParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(PLCParser.AND, i);
		}
		public Logic_andContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_and; }
	}

	public final Logic_andContext logic_and() throws RecognitionException {
		Logic_andContext _localctx = new Logic_andContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_logic_and);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			equality();
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(144);
				match(AND);
				setState(145);
				equality();
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityContext extends ParserRuleContext {
		public List<ComparisonContext> comparison() {
			return getRuleContexts(ComparisonContext.class);
		}
		public ComparisonContext comparison(int i) {
			return getRuleContext(ComparisonContext.class,i);
		}
		public List<TerminalNode> EQ() { return getTokens(PLCParser.EQ); }
		public TerminalNode EQ(int i) {
			return getToken(PLCParser.EQ, i);
		}
		public List<TerminalNode> NEQ() { return getTokens(PLCParser.NEQ); }
		public TerminalNode NEQ(int i) {
			return getToken(PLCParser.NEQ, i);
		}
		public EqualityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality; }
	}

	public final EqualityContext equality() throws RecognitionException {
		EqualityContext _localctx = new EqualityContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_equality);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			comparison();
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==EQ || _la==NEQ) {
				{
				{
				setState(152);
				_la = _input.LA(1);
				if ( !(_la==EQ || _la==NEQ) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(153);
				comparison();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ParserRuleContext {
		public List<AdditionContext> addition() {
			return getRuleContexts(AdditionContext.class);
		}
		public AdditionContext addition(int i) {
			return getRuleContext(AdditionContext.class,i);
		}
		public List<TerminalNode> LT() { return getTokens(PLCParser.LT); }
		public TerminalNode LT(int i) {
			return getToken(PLCParser.LT, i);
		}
		public List<TerminalNode> GT() { return getTokens(PLCParser.GT); }
		public TerminalNode GT(int i) {
			return getToken(PLCParser.GT, i);
		}
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			addition();
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LT || _la==GT) {
				{
				{
				setState(160);
				_la = _input.LA(1);
				if ( !(_la==LT || _la==GT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(161);
				addition();
				}
				}
				setState(166);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditionContext extends ParserRuleContext {
		public List<MultiplicationContext> multiplication() {
			return getRuleContexts(MultiplicationContext.class);
		}
		public MultiplicationContext multiplication(int i) {
			return getRuleContext(MultiplicationContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(PLCParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(PLCParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(PLCParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(PLCParser.MINUS, i);
		}
		public List<TerminalNode> DOT() { return getTokens(PLCParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(PLCParser.DOT, i);
		}
		public AdditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addition; }
	}

	public final AdditionContext addition() throws RecognitionException {
		AdditionContext _localctx = new AdditionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_addition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			multiplication();
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1146880L) != 0)) {
				{
				{
				setState(168);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1146880L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(169);
				multiplication();
				}
				}
				setState(174);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicationContext extends ParserRuleContext {
		public List<UnaryContext> unary() {
			return getRuleContexts(UnaryContext.class);
		}
		public UnaryContext unary(int i) {
			return getRuleContext(UnaryContext.class,i);
		}
		public List<TerminalNode> MUL() { return getTokens(PLCParser.MUL); }
		public TerminalNode MUL(int i) {
			return getToken(PLCParser.MUL, i);
		}
		public List<TerminalNode> DIV() { return getTokens(PLCParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(PLCParser.DIV, i);
		}
		public List<TerminalNode> MOD() { return getTokens(PLCParser.MOD); }
		public TerminalNode MOD(int i) {
			return getToken(PLCParser.MOD, i);
		}
		public MultiplicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplication; }
	}

	public final MultiplicationContext multiplication() throws RecognitionException {
		MultiplicationContext _localctx = new MultiplicationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_multiplication);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			unary();
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 917504L) != 0)) {
				{
				{
				setState(176);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 917504L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(177);
				unary();
				}
				}
				setState(182);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryContext extends ParserRuleContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode NOT() { return getToken(PLCParser.NOT, 0); }
		public TerminalNode MINUS() { return getToken(PLCParser.MINUS, 0); }
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_unary);
		int _la;
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				_la = _input.LA(1);
				if ( !(_la==MINUS || _la==NOT) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(184);
				unary();
				}
				break;
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
			case LPAREN:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(185);
				primary();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PLCParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(PLCParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(PLCParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(PLCParser.STRING, 0); }
		public TerminalNode ID() { return getToken(PLCParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(PLCParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(PLCParser.RPAREN, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_primary);
		try {
			setState(197);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(188);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				match(FLOAT);
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(190);
				match(BOOL);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(191);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(192);
				match(ID);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 6);
				{
				setState(193);
				match(LPAREN);
				setState(194);
				expression();
				setState(195);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\"\u00c8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0005\u0000*\b\u0000\n\u0000\f\u0000"+
		"-\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u00018\b\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002>\b\u0002"+
		"\n\u0002\f\u0002A\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"L\b\u0004\n\u0004\f\u0004O\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005W\b\u0005\n\u0005\f\u0005"+
		"Z\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0005\u0006"+
		"`\b\u0006\n\u0006\f\u0006c\t\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0003\u0007n\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u0086\b\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u008b\b\f\n"+
		"\f\f\f\u008e\t\f\u0001\r\u0001\r\u0001\r\u0005\r\u0093\b\r\n\r\f\r\u0096"+
		"\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u009b\b\u000e\n\u000e"+
		"\f\u000e\u009e\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f"+
		"\u00a3\b\u000f\n\u000f\f\u000f\u00a6\t\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0005\u0010\u00ab\b\u0010\n\u0010\f\u0010\u00ae\t\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0005\u0011\u00b3\b\u0011\n\u0011\f\u0011\u00b6"+
		"\t\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00bb\b\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0003\u0013\u00c6\b\u0013\u0001\u0013"+
		"\u0000\u0000\u0014\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&\u0000\u0005\u0001\u0000\u0018\u0019"+
		"\u0001\u0000\u001a\u001b\u0002\u0000\u000f\u0010\u0014\u0014\u0001\u0000"+
		"\u0011\u0013\u0002\u0000\u0010\u0010\u0017\u0017\u00ce\u0000+\u0001\u0000"+
		"\u0000\u0000\u00027\u0001\u0000\u0000\u0000\u00049\u0001\u0000\u0000\u0000"+
		"\u0006D\u0001\u0000\u0000\u0000\bG\u0001\u0000\u0000\u0000\nR\u0001\u0000"+
		"\u0000\u0000\f]\u0001\u0000\u0000\u0000\u000ef\u0001\u0000\u0000\u0000"+
		"\u0010o\u0001\u0000\u0000\u0000\u0012u\u0001\u0000\u0000\u0000\u0014\u0080"+
		"\u0001\u0000\u0000\u0000\u0016\u0082\u0001\u0000\u0000\u0000\u0018\u0087"+
		"\u0001\u0000\u0000\u0000\u001a\u008f\u0001\u0000\u0000\u0000\u001c\u0097"+
		"\u0001\u0000\u0000\u0000\u001e\u009f\u0001\u0000\u0000\u0000 \u00a7\u0001"+
		"\u0000\u0000\u0000\"\u00af\u0001\u0000\u0000\u0000$\u00ba\u0001\u0000"+
		"\u0000\u0000&\u00c5\u0001\u0000\u0000\u0000(*\u0003\u0002\u0001\u0000"+
		")(\u0001\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000"+
		"\u0000+,\u0001\u0000\u0000\u0000,\u0001\u0001\u0000\u0000\u0000-+\u0001"+
		"\u0000\u0000\u0000.8\u0003\u0004\u0002\u0000/8\u0003\u0006\u0003\u0000"+
		"08\u0003\b\u0004\u000018\u0003\n\u0005\u000028\u0003\f\u0006\u000038\u0003"+
		"\u000e\u0007\u000048\u0003\u0010\b\u000058\u0003\u0012\t\u000068\u0005"+
		"\u001c\u0000\u00007.\u0001\u0000\u0000\u00007/\u0001\u0000\u0000\u0000"+
		"70\u0001\u0000\u0000\u000071\u0001\u0000\u0000\u000072\u0001\u0000\u0000"+
		"\u000073\u0001\u0000\u0000\u000074\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u000076\u0001\u0000\u0000\u00008\u0003\u0001\u0000\u0000\u0000"+
		"9:\u0005\u0005\u0000\u0000:?\u0005\"\u0000\u0000;<\u0005\u001d\u0000\u0000"+
		"<>\u0005\"\u0000\u0000=;\u0001\u0000\u0000\u0000>A\u0001\u0000\u0000\u0000"+
		"?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@B\u0001\u0000\u0000"+
		"\u0000A?\u0001\u0000\u0000\u0000BC\u0005\u001c\u0000\u0000C\u0005\u0001"+
		"\u0000\u0000\u0000DE\u0003\u0014\n\u0000EF\u0005\u001c\u0000\u0000F\u0007"+
		"\u0001\u0000\u0000\u0000GH\u0005\n\u0000\u0000HM\u0005\"\u0000\u0000I"+
		"J\u0005\u001d\u0000\u0000JL\u0005\"\u0000\u0000KI\u0001\u0000\u0000\u0000"+
		"LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NP\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0005\u001c"+
		"\u0000\u0000Q\t\u0001\u0000\u0000\u0000RS\u0005\u000b\u0000\u0000SX\u0003"+
		"\u0014\n\u0000TU\u0005\u001d\u0000\u0000UW\u0003\u0014\n\u0000VT\u0001"+
		"\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000"+
		"XY\u0001\u0000\u0000\u0000Y[\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000"+
		"\u0000[\\\u0005\u001c\u0000\u0000\\\u000b\u0001\u0000\u0000\u0000]a\u0005"+
		" \u0000\u0000^`\u0003\u0002\u0001\u0000_^\u0001\u0000\u0000\u0000`c\u0001"+
		"\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000"+
		"bd\u0001\u0000\u0000\u0000ca\u0001\u0000\u0000\u0000de\u0005!\u0000\u0000"+
		"e\r\u0001\u0000\u0000\u0000fg\u0005\u0006\u0000\u0000gh\u0005\u001e\u0000"+
		"\u0000hi\u0003\u0014\n\u0000ij\u0005\u001f\u0000\u0000jm\u0003\u0002\u0001"+
		"\u0000kl\u0005\u0007\u0000\u0000ln\u0003\u0002\u0001\u0000mk\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000n\u000f\u0001\u0000\u0000\u0000"+
		"op\u0005\b\u0000\u0000pq\u0005\u001e\u0000\u0000qr\u0003\u0014\n\u0000"+
		"rs\u0005\u001f\u0000\u0000st\u0003\u0002\u0001\u0000t\u0011\u0001\u0000"+
		"\u0000\u0000uv\u0005\t\u0000\u0000vw\u0005\u001e\u0000\u0000wx\u0005\u0005"+
		"\u0000\u0000xy\u0005\"\u0000\u0000yz\u0005\u001c\u0000\u0000z{\u0003\u0014"+
		"\n\u0000{|\u0005\u001c\u0000\u0000|}\u0003\u0014\n\u0000}~\u0005\u001f"+
		"\u0000\u0000~\u007f\u0003\u0002\u0001\u0000\u007f\u0013\u0001\u0000\u0000"+
		"\u0000\u0080\u0081\u0003\u0016\u000b\u0000\u0081\u0015\u0001\u0000\u0000"+
		"\u0000\u0082\u0085\u0003\u0018\f\u0000\u0083\u0084\u0005\u000e\u0000\u0000"+
		"\u0084\u0086\u0003\u0016\u000b\u0000\u0085\u0083\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u0017\u0001\u0000\u0000\u0000"+
		"\u0087\u008c\u0003\u001a\r\u0000\u0088\u0089\u0005\u0016\u0000\u0000\u0089"+
		"\u008b\u0003\u001a\r\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008b\u008e"+
		"\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008c\u008d"+
		"\u0001\u0000\u0000\u0000\u008d\u0019\u0001\u0000\u0000\u0000\u008e\u008c"+
		"\u0001\u0000\u0000\u0000\u008f\u0094\u0003\u001c\u000e\u0000\u0090\u0091"+
		"\u0005\u0015\u0000\u0000\u0091\u0093\u0003\u001c\u000e\u0000\u0092\u0090"+
		"\u0001\u0000\u0000\u0000\u0093\u0096\u0001\u0000\u0000\u0000\u0094\u0092"+
		"\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u001b"+
		"\u0001\u0000\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0097\u009c"+
		"\u0003\u001e\u000f\u0000\u0098\u0099\u0007\u0000\u0000\u0000\u0099\u009b"+
		"\u0003\u001e\u000f\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009e"+
		"\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d"+
		"\u0001\u0000\u0000\u0000\u009d\u001d\u0001\u0000\u0000\u0000\u009e\u009c"+
		"\u0001\u0000\u0000\u0000\u009f\u00a4\u0003 \u0010\u0000\u00a0\u00a1\u0007"+
		"\u0001\u0000\u0000\u00a1\u00a3\u0003 \u0010\u0000\u00a2\u00a0\u0001\u0000"+
		"\u0000\u0000\u00a3\u00a6\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u001f\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000\u0000\u00a7\u00ac\u0003\"\u0011"+
		"\u0000\u00a8\u00a9\u0007\u0002\u0000\u0000\u00a9\u00ab\u0003\"\u0011\u0000"+
		"\u00aa\u00a8\u0001\u0000\u0000\u0000\u00ab\u00ae\u0001\u0000\u0000\u0000"+
		"\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000"+
		"\u00ad!\u0001\u0000\u0000\u0000\u00ae\u00ac\u0001\u0000\u0000\u0000\u00af"+
		"\u00b4\u0003$\u0012\u0000\u00b0\u00b1\u0007\u0003\u0000\u0000\u00b1\u00b3"+
		"\u0003$\u0012\u0000\u00b2\u00b0\u0001\u0000\u0000\u0000\u00b3\u00b6\u0001"+
		"\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b4\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b5#\u0001\u0000\u0000\u0000\u00b6\u00b4\u0001\u0000"+
		"\u0000\u0000\u00b7\u00b8\u0007\u0004\u0000\u0000\u00b8\u00bb\u0003$\u0012"+
		"\u0000\u00b9\u00bb\u0003&\u0013\u0000\u00ba\u00b7\u0001\u0000\u0000\u0000"+
		"\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb%\u0001\u0000\u0000\u0000\u00bc"+
		"\u00c6\u0005\u0001\u0000\u0000\u00bd\u00c6\u0005\u0002\u0000\u0000\u00be"+
		"\u00c6\u0005\u0003\u0000\u0000\u00bf\u00c6\u0005\u0004\u0000\u0000\u00c0"+
		"\u00c6\u0005\"\u0000\u0000\u00c1\u00c2\u0005\u001e\u0000\u0000\u00c2\u00c3"+
		"\u0003\u0014\n\u0000\u00c3\u00c4\u0005\u001f\u0000\u0000\u00c4\u00c6\u0001"+
		"\u0000\u0000\u0000\u00c5\u00bc\u0001\u0000\u0000\u0000\u00c5\u00bd\u0001"+
		"\u0000\u0000\u0000\u00c5\u00be\u0001\u0000\u0000\u0000\u00c5\u00bf\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c0\u0001\u0000\u0000\u0000\u00c5\u00c1\u0001"+
		"\u0000\u0000\u0000\u00c6\'\u0001\u0000\u0000\u0000\u0010+7?MXam\u0085"+
		"\u008c\u0094\u009c\u00a4\u00ac\u00b4\u00ba\u00c5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}