// Generated from c:/Users/Tomáš/Documents/VSB/PJP/projekt/MyLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MyLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, BOOL=3, STRING=4, FILE=5, TYPE=6, IF=7, ELSE=8, WHILE=9, 
		READ=10, WRITE=11, COMMENT=12, WS=13, ASSIGN=14, PLUS=15, MINUS=16, MUL=17, 
		DIV=18, MOD=19, DOT=20, AND=21, OR=22, NOT=23, EQ=24, NEQ=25, LT=26, GT=27, 
		SEMI=28, COMMA=29, LPAREN=30, RPAREN=31, LBRACE=32, RBRACE=33, BITLEFT=34, 
		ID=35;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"INT", "FLOAT", "BOOL", "STRING", "FILE", "TYPE", "IF", "ELSE", "WHILE", 
			"READ", "WRITE", "COMMENT", "WS", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
			"MOD", "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", "SEMI", "COMMA", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "BITLEFT", "ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'if'", "'else'", "'while'", 
			"'read'", "'write'", null, null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
			"'.'", "'&&'", "'||'", "'!'", "'=='", "'!='", "'<'", "'>'", "';'", "','", 
			"'('", "')'", "'{'", "'}'", "'<<'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INT", "FLOAT", "BOOL", "STRING", "FILE", "TYPE", "IF", "ELSE", 
			"WHILE", "READ", "WRITE", "COMMENT", "WS", "ASSIGN", "PLUS", "MINUS", 
			"MUL", "DIV", "MOD", "DOT", "AND", "OR", "NOT", "EQ", "NEQ", "LT", "GT", 
			"SEMI", "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "BITLEFT", "ID"
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


	public MyLangLexer(CharStream input) {
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
		"\u0004\u0000#\u00e6\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0001\u0000\u0004\u0000I\b\u0000\u000b\u0000\f\u0000"+
		"J\u0001\u0001\u0004\u0001N\b\u0001\u000b\u0001\f\u0001O\u0001\u0001\u0001"+
		"\u0001\u0004\u0001T\b\u0001\u000b\u0001\f\u0001U\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002a\b\u0002\u0001\u0003\u0001\u0003\u0005\u0003"+
		"e\b\u0003\n\u0003\f\u0003h\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"\u0084\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0005\u000b\u00a3\b\u000b\n\u000b\f\u000b\u00a6\t\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0004\f\u00ab\b\f\u000b\f\f\f\u00ac\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a"+
		"\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001 \u0001"+
		" \u0001!\u0001!\u0001!\u0001\"\u0001\"\u0005\"\u00e2\b\"\n\"\f\"\u00e5"+
		"\t\"\u0001f\u0000#\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015"+
		"+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f"+
		"? A!C\"E#\u0001\u0000\u0005\u0001\u000009\u0002\u0000\n\n\r\r\u0003\u0000"+
		"\t\n\r\r  \u0002\u0000AZaz\u0003\u000009AZaz\u00f1\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u0000"+
		"1\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001"+
		"\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000"+
		"\u0000\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000"+
		"?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C\u0001"+
		"\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0001H\u0001\u0000\u0000"+
		"\u0000\u0003M\u0001\u0000\u0000\u0000\u0005`\u0001\u0000\u0000\u0000\u0007"+
		"b\u0001\u0000\u0000\u0000\tk\u0001\u0000\u0000\u0000\u000b\u0083\u0001"+
		"\u0000\u0000\u0000\r\u0085\u0001\u0000\u0000\u0000\u000f\u0088\u0001\u0000"+
		"\u0000\u0000\u0011\u008d\u0001\u0000\u0000\u0000\u0013\u0093\u0001\u0000"+
		"\u0000\u0000\u0015\u0098\u0001\u0000\u0000\u0000\u0017\u009e\u0001\u0000"+
		"\u0000\u0000\u0019\u00aa\u0001\u0000\u0000\u0000\u001b\u00b0\u0001\u0000"+
		"\u0000\u0000\u001d\u00b2\u0001\u0000\u0000\u0000\u001f\u00b4\u0001\u0000"+
		"\u0000\u0000!\u00b6\u0001\u0000\u0000\u0000#\u00b8\u0001\u0000\u0000\u0000"+
		"%\u00ba\u0001\u0000\u0000\u0000\'\u00bc\u0001\u0000\u0000\u0000)\u00be"+
		"\u0001\u0000\u0000\u0000+\u00c1\u0001\u0000\u0000\u0000-\u00c4\u0001\u0000"+
		"\u0000\u0000/\u00c6\u0001\u0000\u0000\u00001\u00c9\u0001\u0000\u0000\u0000"+
		"3\u00cc\u0001\u0000\u0000\u00005\u00ce\u0001\u0000\u0000\u00007\u00d0"+
		"\u0001\u0000\u0000\u00009\u00d2\u0001\u0000\u0000\u0000;\u00d4\u0001\u0000"+
		"\u0000\u0000=\u00d6\u0001\u0000\u0000\u0000?\u00d8\u0001\u0000\u0000\u0000"+
		"A\u00da\u0001\u0000\u0000\u0000C\u00dc\u0001\u0000\u0000\u0000E\u00df"+
		"\u0001\u0000\u0000\u0000GI\u0007\u0000\u0000\u0000HG\u0001\u0000\u0000"+
		"\u0000IJ\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000"+
		"\u0000\u0000K\u0002\u0001\u0000\u0000\u0000LN\u0007\u0000\u0000\u0000"+
		"ML\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000"+
		"\u0000OP\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QS\u0005.\u0000"+
		"\u0000RT\u0007\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000TU\u0001\u0000"+
		"\u0000\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000V\u0004"+
		"\u0001\u0000\u0000\u0000WX\u0005t\u0000\u0000XY\u0005r\u0000\u0000YZ\u0005"+
		"u\u0000\u0000Za\u0005e\u0000\u0000[\\\u0005f\u0000\u0000\\]\u0005a\u0000"+
		"\u0000]^\u0005l\u0000\u0000^_\u0005s\u0000\u0000_a\u0005e\u0000\u0000"+
		"`W\u0001\u0000\u0000\u0000`[\u0001\u0000\u0000\u0000a\u0006\u0001\u0000"+
		"\u0000\u0000bf\u0005\"\u0000\u0000ce\t\u0000\u0000\u0000dc\u0001\u0000"+
		"\u0000\u0000eh\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000fd\u0001"+
		"\u0000\u0000\u0000gi\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000"+
		"ij\u0005\"\u0000\u0000j\b\u0001\u0000\u0000\u0000kl\u0003\u0007\u0003"+
		"\u0000l\n\u0001\u0000\u0000\u0000mn\u0005i\u0000\u0000no\u0005n\u0000"+
		"\u0000o\u0084\u0005t\u0000\u0000pq\u0005f\u0000\u0000qr\u0005l\u0000\u0000"+
		"rs\u0005o\u0000\u0000st\u0005a\u0000\u0000t\u0084\u0005t\u0000\u0000u"+
		"v\u0005b\u0000\u0000vw\u0005o\u0000\u0000wx\u0005o\u0000\u0000x\u0084"+
		"\u0005l\u0000\u0000yz\u0005s\u0000\u0000z{\u0005t\u0000\u0000{|\u0005"+
		"r\u0000\u0000|}\u0005i\u0000\u0000}~\u0005n\u0000\u0000~\u0084\u0005g"+
		"\u0000\u0000\u007f\u0080\u0005F\u0000\u0000\u0080\u0081\u0005I\u0000\u0000"+
		"\u0081\u0082\u0005L\u0000\u0000\u0082\u0084\u0005E\u0000\u0000\u0083m"+
		"\u0001\u0000\u0000\u0000\u0083p\u0001\u0000\u0000\u0000\u0083u\u0001\u0000"+
		"\u0000\u0000\u0083y\u0001\u0000\u0000\u0000\u0083\u007f\u0001\u0000\u0000"+
		"\u0000\u0084\f\u0001\u0000\u0000\u0000\u0085\u0086\u0005i\u0000\u0000"+
		"\u0086\u0087\u0005f\u0000\u0000\u0087\u000e\u0001\u0000\u0000\u0000\u0088"+
		"\u0089\u0005e\u0000\u0000\u0089\u008a\u0005l\u0000\u0000\u008a\u008b\u0005"+
		"s\u0000\u0000\u008b\u008c\u0005e\u0000\u0000\u008c\u0010\u0001\u0000\u0000"+
		"\u0000\u008d\u008e\u0005w\u0000\u0000\u008e\u008f\u0005h\u0000\u0000\u008f"+
		"\u0090\u0005i\u0000\u0000\u0090\u0091\u0005l\u0000\u0000\u0091\u0092\u0005"+
		"e\u0000\u0000\u0092\u0012\u0001\u0000\u0000\u0000\u0093\u0094\u0005r\u0000"+
		"\u0000\u0094\u0095\u0005e\u0000\u0000\u0095\u0096\u0005a\u0000\u0000\u0096"+
		"\u0097\u0005d\u0000\u0000\u0097\u0014\u0001\u0000\u0000\u0000\u0098\u0099"+
		"\u0005w\u0000\u0000\u0099\u009a\u0005r\u0000\u0000\u009a\u009b\u0005i"+
		"\u0000\u0000\u009b\u009c\u0005t\u0000\u0000\u009c\u009d\u0005e\u0000\u0000"+
		"\u009d\u0016\u0001\u0000\u0000\u0000\u009e\u009f\u0005/\u0000\u0000\u009f"+
		"\u00a0\u0005/\u0000\u0000\u00a0\u00a4\u0001\u0000\u0000\u0000\u00a1\u00a3"+
		"\b\u0001\u0000\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000\u00a3\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a7\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0006\u000b\u0000\u0000\u00a8\u0018\u0001"+
		"\u0000\u0000\u0000\u00a9\u00ab\u0007\u0002\u0000\u0000\u00aa\u00a9\u0001"+
		"\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001"+
		"\u0000\u0000\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001"+
		"\u0000\u0000\u0000\u00ae\u00af\u0006\f\u0000\u0000\u00af\u001a\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b1\u0005=\u0000\u0000\u00b1\u001c\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b3\u0005+\u0000\u0000\u00b3\u001e\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b5\u0005-\u0000\u0000\u00b5 \u0001\u0000\u0000\u0000\u00b6\u00b7"+
		"\u0005*\u0000\u0000\u00b7\"\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005"+
		"/\u0000\u0000\u00b9$\u0001\u0000\u0000\u0000\u00ba\u00bb\u0005%\u0000"+
		"\u0000\u00bb&\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005.\u0000\u0000\u00bd"+
		"(\u0001\u0000\u0000\u0000\u00be\u00bf\u0005&\u0000\u0000\u00bf\u00c0\u0005"+
		"&\u0000\u0000\u00c0*\u0001\u0000\u0000\u0000\u00c1\u00c2\u0005|\u0000"+
		"\u0000\u00c2\u00c3\u0005|\u0000\u0000\u00c3,\u0001\u0000\u0000\u0000\u00c4"+
		"\u00c5\u0005!\u0000\u0000\u00c5.\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005"+
		"=\u0000\u0000\u00c7\u00c8\u0005=\u0000\u0000\u00c80\u0001\u0000\u0000"+
		"\u0000\u00c9\u00ca\u0005!\u0000\u0000\u00ca\u00cb\u0005=\u0000\u0000\u00cb"+
		"2\u0001\u0000\u0000\u0000\u00cc\u00cd\u0005<\u0000\u0000\u00cd4\u0001"+
		"\u0000\u0000\u0000\u00ce\u00cf\u0005>\u0000\u0000\u00cf6\u0001\u0000\u0000"+
		"\u0000\u00d0\u00d1\u0005;\u0000\u0000\u00d18\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d3\u0005,\u0000\u0000\u00d3:\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005"+
		"(\u0000\u0000\u00d5<\u0001\u0000\u0000\u0000\u00d6\u00d7\u0005)\u0000"+
		"\u0000\u00d7>\u0001\u0000\u0000\u0000\u00d8\u00d9\u0005{\u0000\u0000\u00d9"+
		"@\u0001\u0000\u0000\u0000\u00da\u00db\u0005}\u0000\u0000\u00dbB\u0001"+
		"\u0000\u0000\u0000\u00dc\u00dd\u0005<\u0000\u0000\u00dd\u00de\u0005<\u0000"+
		"\u0000\u00deD\u0001\u0000\u0000\u0000\u00df\u00e3\u0007\u0003\u0000\u0000"+
		"\u00e0\u00e2\u0007\u0004\u0000\u0000\u00e1\u00e0\u0001\u0000\u0000\u0000"+
		"\u00e2\u00e5\u0001\u0000\u0000\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e4\u0001\u0000\u0000\u0000\u00e4F\u0001\u0000\u0000\u0000\u00e5"+
		"\u00e3\u0001\u0000\u0000\u0000\n\u0000JOU`f\u0083\u00a4\u00ac\u00e3\u0001"+
		"\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}