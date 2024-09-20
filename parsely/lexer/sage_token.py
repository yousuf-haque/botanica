from dataclasses import dataclass


@dataclass
class SageToken:
        type: str
        value: str

def number_token(value) -> SageToken:
        return SageToken('NUMBER', value)

def plus_token() -> SageToken:
        return SageToken('PLUS', '+')
