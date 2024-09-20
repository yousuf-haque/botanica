from parsely.compiler.compiler import Compiler
from parsely.lexer.lexer import Lexer
from parsely.parser.parser import Parser
from rosemary.virtual_machine import VirtualMachine

if __name__ == '__main__':
    source = "40 + 1 + 1"

    lexer = Lexer(source)
    tokens = lexer.tokenize()
    print(f"tokens:\n{tokens}")

    parser = Parser(tokens)
    ast = parser.parse()
    print(f"ast:\n{ast}")

    compiler = Compiler(ast)
    bytecode = compiler.compile()
    print(bytecode)

    vm = VirtualMachine(bytecode)
    vm.run()
    print(f"stack value: {vm.get_tail()}")
