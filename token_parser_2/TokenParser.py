from token_parser_2 import TokenType, Token


class TokenParserException(Exception):
    pass


class TokenParser:

    def __init__(self):
        self.token_list = []

    def parse(self, expression):
        datatypes = ['int']
        is_reference = False
        string_value = ''
        numeral_value = ''

        for i in range(len(expression)):
            char = expression[i]
            if char == ' ':
                continue
            if char.isalpha():
                string_value += char
                if not expression[i+1].isalpha():
                    if string_value in datatypes:
                        self.token_list.append(Token(TokenType.DATATYPE, string_value))
                    else:
                        if is_reference:
                            self.token_list.append(Token(TokenType.REFERENCE, string_value))
                        else:
                            self.token_list.append(Token(TokenType.VARIABLE, string_value))
                    string_value = ''
                continue
            if char.isdigit():
                numeral_value += char
                if not expression[i + 1].isdigit():
                    self.token_list.append(Token(TokenType.NUMBER, numeral_value))
                    numeral_value = ''
            if char == '=':
                self.token_list.append(Token(TokenType.EQUAL, char))
                continue
            if char == ';':
                self.token_list.append(Token(TokenType.SEMICOLON, char))
                continue
            if char == '*':
                self.token_list.append(Token(TokenType.POINTER, char))
                continue
            if char == '&':
                is_reference = True
                string_value += char
                continue

    def __str__(self):
        out = f"Tokens: \n"
        for token in self.token_list:
            out += token.__str__()
            if token.type_ == TokenType.SEMICOLON:
                out += '\n'
            else:
                out += ' | '
        return out


if __name__ == '__main__':
    # FOR TESTS
    parser = TokenParser()
    parser.parse('int value = 10;'
                 'int* ptr = &value;')
    print(parser)






