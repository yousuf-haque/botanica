from typing import List
from parsely.lexer.sage_token import SageToken, number_token


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.current_position = 0
        self.current_char = self.source[self.current_position] if self.source else None

    def _advance(self):
        self.current_position = self.current_position + 1
        self.current_char = self.source[self.current_position] if self.current_position < len(self.source) else None

    def tokenize(self) -> List[SageToken]:
        tokens = []

        while self.current_char:
            if self.current_char.isdigit():
                tokens.append(self._number())
        return tokens

    def _number(self) -> SageToken:
        value = int(self.current_char)
        self._advance()

        while self.current_char and self.current_char.isdigit():
            value = value*10 + int(self.current_char)
            self._advance()

        return number_token(value)

