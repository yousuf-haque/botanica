from parsely.lexer.lexer import Lexer
if __name__ == '__main__':
    source = "40"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    print(tokens)
