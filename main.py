import sys
from antlr4 import *
from PLCLexer import PLCLexer
from PLCParser import PLCParser
from TypeCheckerVisitor import TypeCheckerVisitor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input-file>")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as f:
        input_stream = InputStream(f.read())

    lexer = PLCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PLCParser(token_stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() == 0:
        print("✅ Program parsed successfully.")
        type_checker = TypeCheckerVisitor()
        type_checker.visit(tree)
    else:
        print("❌ Syntax error(s) detected.")

if __name__ == "__main__":
    main()
