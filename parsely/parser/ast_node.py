from dataclasses import dataclass

from parsely.lexer.sage_token import SageToken


@dataclass
class ASTNode:
    pass

@dataclass
class BinOp(ASTNode):
    left: ASTNode
    op: SageToken
    right: ASTNode

@dataclass(init=False)
class Num(ASTNode):
    token: SageToken
    value: int
    def __init__(self, token):
        self.value = int(token.value)
        self.token = token
