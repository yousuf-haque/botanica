from parsely.lexer.lexer import Lexer
from parsely.parser.parser import Parser

if __name__ == '__main__':
    source = "40 + 1 + 1"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    print(f"tokens:\n{tokens}")
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"ast:\n{ast}")
