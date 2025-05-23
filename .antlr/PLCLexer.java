// Generated from d:/VSB/PJP/projekt/MyLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PLCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, BOOL=3, STRING=4, TYPE=5, IF=6, ELSE=7, WHILE=8, READ=9, 
		WRITE=10, COMMENT=11, WS=12, ASSIGN=13, PLUS=14, MINUS=15, MUL=16, DIV=17, 
		MOD=18, DOT=19, AND=20, OR=21, NOT=22, EQ=23, NEQ=24, LT=25, GT=26, SEMI=27, 
		COMMA=28, LPAREN=29, RPAREN=30, LBRACE=31, RBRACE=32, ID=33;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"INT", "FLOAT", "BOOL", "STRING", "TYPE", "IF", "ELSE", "WHILE", "READ", 
			"WRITE", "COMMENT", "WS", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
			"DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", "SEMI", "COMMA", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'if'", "'else'", "'while'", "'read'", 
			"'write'", null, null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'.'", 
			"'&&'", "'||'", "'!'", "'=='", "'!='", "'<'", "'>'", "';'", "','", "'('", 
			"')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INT", "FLOAT", "BOOL", "STRING", "TYPE", "IF", "ELSE", "WHILE", 
			"READ", "WRITE", "COMMENT", "WS", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
			"MOD", "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", "SEMI", "COMMA", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "ID"
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


	public PLCLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000!\u00d9\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0001\u0000\u0004"+
		"\u0000E\b\u0000\u000b\u0000\f\u0000F\u0001\u0001\u0004\u0001J\b\u0001"+
		"\u000b\u0001\f\u0001K\u0001\u0001\u0001\u0001\u0004\u0001P\b\u0001\u000b"+
		"\u0001\f\u0001Q\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002]\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0005\u0003a\b\u0003\n\u0003\f\u0003d\t"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004z\b\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0005\n\u0099"+
		"\b\n\n\n\f\n\u009c\t\n\u0001\n\u0001\n\u0001\u000b\u0004\u000b\u00a1\b"+
		"\u000b\u000b\u000b\f\u000b\u00a2\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001"+
		" \u0001 \u0005 \u00d5\b \n \f \u00d8\t \u0001b\u0000!\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010"+
		"!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a"+
		"5\u001b7\u001c9\u001d;\u001e=\u001f? A!\u0001\u0000\u0005\u0001\u0000"+
		"09\u0002\u0000\n\n\r\r\u0003\u0000\t\n\r\r  \u0002\u0000AZaz\u0003\u0000"+
		"09AZaz\u00e3\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000"+
		"A\u0001\u0000\u0000\u0000\u0001D\u0001\u0000\u0000\u0000\u0003I\u0001"+
		"\u0000\u0000\u0000\u0005\\\u0001\u0000\u0000\u0000\u0007^\u0001\u0000"+
		"\u0000\u0000\ty\u0001\u0000\u0000\u0000\u000b{\u0001\u0000\u0000\u0000"+
		"\r~\u0001\u0000\u0000\u0000\u000f\u0083\u0001\u0000\u0000\u0000\u0011"+
		"\u0089\u0001\u0000\u0000\u0000\u0013\u008e\u0001\u0000\u0000\u0000\u0015"+
		"\u0094\u0001\u0000\u0000\u0000\u0017\u00a0\u0001\u0000\u0000\u0000\u0019"+
		"\u00a6\u0001\u0000\u0000\u0000\u001b\u00a8\u0001\u0000\u0000\u0000\u001d"+
		"\u00aa\u0001\u0000\u0000\u0000\u001f\u00ac\u0001\u0000\u0000\u0000!\u00ae"+
		"\u0001\u0000\u0000\u0000#\u00b0\u0001\u0000\u0000\u0000%\u00b2\u0001\u0000"+
		"\u0000\u0000\'\u00b4\u0001\u0000\u0000\u0000)\u00b7\u0001\u0000\u0000"+
		"\u0000+\u00ba\u0001\u0000\u0000\u0000-\u00bc\u0001\u0000\u0000\u0000/"+
		"\u00bf\u0001\u0000\u0000\u00001\u00c2\u0001\u0000\u0000\u00003\u00c4\u0001"+
		"\u0000\u0000\u00005\u00c6\u0001\u0000\u0000\u00007\u00c8\u0001\u0000\u0000"+
		"\u00009\u00ca\u0001\u0000\u0000\u0000;\u00cc\u0001\u0000\u0000\u0000="+
		"\u00ce\u0001\u0000\u0000\u0000?\u00d0\u0001\u0000\u0000\u0000A\u00d2\u0001"+
		"\u0000\u0000\u0000CE\u0007\u0000\u0000\u0000DC\u0001\u0000\u0000\u0000"+
		"EF\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000"+
		"\u0000G\u0002\u0001\u0000\u0000\u0000HJ\u0007\u0000\u0000\u0000IH\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000"+
		"KL\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MO\u0005.\u0000\u0000"+
		"NP\u0007\u0000\u0000\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000R\u0004\u0001"+
		"\u0000\u0000\u0000ST\u0005t\u0000\u0000TU\u0005r\u0000\u0000UV\u0005u"+
		"\u0000\u0000V]\u0005e\u0000\u0000WX\u0005f\u0000\u0000XY\u0005a\u0000"+
		"\u0000YZ\u0005l\u0000\u0000Z[\u0005s\u0000\u0000[]\u0005e\u0000\u0000"+
		"\\S\u0001\u0000\u0000\u0000\\W\u0001\u0000\u0000\u0000]\u0006\u0001\u0000"+
		"\u0000\u0000^b\u0005\"\u0000\u0000_a\t\u0000\u0000\u0000`_\u0001\u0000"+
		"\u0000\u0000ad\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000b`\u0001"+
		"\u0000\u0000\u0000ce\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"ef\u0005\"\u0000\u0000f\b\u0001\u0000\u0000\u0000gh\u0005i\u0000\u0000"+
		"hi\u0005n\u0000\u0000iz\u0005t\u0000\u0000jk\u0005f\u0000\u0000kl\u0005"+
		"l\u0000\u0000lm\u0005o\u0000\u0000mn\u0005a\u0000\u0000nz\u0005t\u0000"+
		"\u0000op\u0005b\u0000\u0000pq\u0005o\u0000\u0000qr\u0005o\u0000\u0000"+
		"rz\u0005l\u0000\u0000st\u0005s\u0000\u0000tu\u0005t\u0000\u0000uv\u0005"+
		"r\u0000\u0000vw\u0005i\u0000\u0000wx\u0005n\u0000\u0000xz\u0005g\u0000"+
		"\u0000yg\u0001\u0000\u0000\u0000yj\u0001\u0000\u0000\u0000yo\u0001\u0000"+
		"\u0000\u0000ys\u0001\u0000\u0000\u0000z\n\u0001\u0000\u0000\u0000{|\u0005"+
		"i\u0000\u0000|}\u0005f\u0000\u0000}\f\u0001\u0000\u0000\u0000~\u007f\u0005"+
		"e\u0000\u0000\u007f\u0080\u0005l\u0000\u0000\u0080\u0081\u0005s\u0000"+
		"\u0000\u0081\u0082\u0005e\u0000\u0000\u0082\u000e\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0005w\u0000\u0000\u0084\u0085\u0005h\u0000\u0000\u0085\u0086"+
		"\u0005i\u0000\u0000\u0086\u0087\u0005l\u0000\u0000\u0087\u0088\u0005e"+
		"\u0000\u0000\u0088\u0010\u0001\u0000\u0000\u0000\u0089\u008a\u0005r\u0000"+
		"\u0000\u008a\u008b\u0005e\u0000\u0000\u008b\u008c\u0005a\u0000\u0000\u008c"+
		"\u008d\u0005d\u0000\u0000\u008d\u0012\u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0005w\u0000\u0000\u008f\u0090\u0005r\u0000\u0000\u0090\u0091\u0005i"+
		"\u0000\u0000\u0091\u0092\u0005t\u0000\u0000\u0092\u0093\u0005e\u0000\u0000"+
		"\u0093\u0014\u0001\u0000\u0000\u0000\u0094\u0095\u0005/\u0000\u0000\u0095"+
		"\u0096\u0005/\u0000\u0000\u0096\u009a\u0001\u0000\u0000\u0000\u0097\u0099"+
		"\b\u0001\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0099\u009c\u0001"+
		"\u0000\u0000\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009a\u009b\u0001"+
		"\u0000\u0000\u0000\u009b\u009d\u0001\u0000\u0000\u0000\u009c\u009a\u0001"+
		"\u0000\u0000\u0000\u009d\u009e\u0006\n\u0000\u0000\u009e\u0016\u0001\u0000"+
		"\u0000\u0000\u009f\u00a1\u0007\u0002\u0000\u0000\u00a0\u009f\u0001\u0000"+
		"\u0000\u0000\u00a1\u00a2\u0001\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000"+
		"\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a5\u0006\u000b\u0000\u0000\u00a5\u0018\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a7\u0005=\u0000\u0000\u00a7\u001a\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a9\u0005+\u0000\u0000\u00a9\u001c\u0001\u0000\u0000\u0000"+
		"\u00aa\u00ab\u0005-\u0000\u0000\u00ab\u001e\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ad\u0005*\u0000\u0000\u00ad \u0001\u0000\u0000\u0000\u00ae\u00af\u0005"+
		"/\u0000\u0000\u00af\"\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005%\u0000"+
		"\u0000\u00b1$\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005.\u0000\u0000\u00b3"+
		"&\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005&\u0000\u0000\u00b5\u00b6\u0005"+
		"&\u0000\u0000\u00b6(\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005|\u0000"+
		"\u0000\u00b8\u00b9\u0005|\u0000\u0000\u00b9*\u0001\u0000\u0000\u0000\u00ba"+
		"\u00bb\u0005!\u0000\u0000\u00bb,\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005"+
		"=\u0000\u0000\u00bd\u00be\u0005=\u0000\u0000\u00be.\u0001\u0000\u0000"+
		"\u0000\u00bf\u00c0\u0005!\u0000\u0000\u00c0\u00c1\u0005=\u0000\u0000\u00c1"+
		"0\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005<\u0000\u0000\u00c32\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0005>\u0000\u0000\u00c54\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c7\u0005;\u0000\u0000\u00c76\u0001\u0000\u0000\u0000\u00c8"+
		"\u00c9\u0005,\u0000\u0000\u00c98\u0001\u0000\u0000\u0000\u00ca\u00cb\u0005"+
		"(\u0000\u0000\u00cb:\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005)\u0000"+
		"\u0000\u00cd<\u0001\u0000\u0000\u0000\u00ce\u00cf\u0005{\u0000\u0000\u00cf"+
		">\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005}\u0000\u0000\u00d1@\u0001"+
		"\u0000\u0000\u0000\u00d2\u00d6\u0007\u0003\u0000\u0000\u00d3\u00d5\u0007"+
		"\u0004\u0000\u0000\u00d4\u00d3\u0001\u0000\u0000\u0000\u00d5\u00d8\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001"+
		"\u0000\u0000\u0000\u00d7B\u0001\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000"+
		"\u0000\u0000\n\u0000FKQ\\by\u009a\u00a2\u00d6\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}