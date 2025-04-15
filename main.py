import sys
from antlr4 import *
from parser.MyLangLexer import MyLangLexer
from parser.MyLangParser import MyLangParser
from TypeCheckerVisitor import TypeCheckerVisitor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input-file> [--tree] [--debug]")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as f:
        input_stream = InputStream(f.read())

    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"{parser.getNumberOfSyntaxErrors()} syntax error(s) detected.")
        return

    print("Program parsed successfully.")

    if "--debug" in sys.argv:
        token_stream.fill()
        print("Tokens:")
        for token in token_stream.tokens:
            print(token)

    if "--tree" in sys.argv:
        print("Parse Tree:")
        print(tree.toStringTree(recog=parser))

    type_checker = TypeCheckerVisitor()
    type_checker.visit(tree)

if __name__ == "__main__":
    main()
