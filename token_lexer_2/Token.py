from enum import Enum, auto


class TokenType(Enum):
    DATATYPE = auto()
    VARIABLE = auto()
    EQUAL = auto()
    NUMBER = auto()
    SEMICOLON = auto()
    POINTER = auto()
    REFERENCE = auto()


class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f'({self.type_}) {self.value}'

    def __repr__(self):
        return str(self)
