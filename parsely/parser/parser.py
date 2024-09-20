from typing import List

from parsely.parser.ast_node import *


class Parser:
    def __init__(self, tokens: List[SageToken]):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position] if self.tokens else None

    def _eat(self, token_type: str):
        if self.current_token.type == token_type:
            self._advance()
        else:
            raise Exception(f'Unexpected token: {self.current_token.type}, expected: {token_type}')

    def _advance(self):
        self.position += 1
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None

    def parse(self):
        return self._expr()

    def _expr(self):
        left = self._term()
        while self.current_token is not None and self.current_token.type == 'PLUS':
            op = self.current_token
            self._eat('PLUS')
            right = self._term()
            left = BinOp(left, op, right)
        return left

    def _term(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self._eat('NUMBER')
            return Num(token)
        else:
            raise Exception(f"Unexpected token in term: {token.type}")
