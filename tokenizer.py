# Types
NUMBER = "NUMBER"
VARIABLE = "VARIABLE"
PLUS = "PLUS"
MINUS = "MINUS"
TIMES = "TIMES"
DIVIDE = "DIVIDE"
POWER = "POWER"
ROOT = "ROOT"
OPEN_BRACES = "OPEN_BRACES"
CLOSE_BRACES = "CLOSE_BRACES"

# Categories
VALUE = "VALUE"
OPERATION = "OPERATION"
BRACES = "BRACES"

class Token():

    def __init__(self, litteral, tokenType, category):
        self.litteral = litteral
        self.type = tokenType
        self.category = category

    def get_as_number(self):
        if self.type != NUMBER:
            Exception("Cannot cast a non number!")
        return float(self.litteral)

    def __str__(self):
        return "Token({litteral}, {tokenType}, {category})".format(
            litteral = self.litteral,
            tokenType = repr(self.type),
            category = repr(self.category)
        )

    def __repr__(self):
        return self.__str__()


def get_type(char):
    if char.isnumeric() or char == "," or char == ".":
        return NUMBER
    elif char == "+":
        return PLUS
    elif char == "-":
        return MINUS
    elif char == "*":
        return TIMES
    elif char == "/":
        return DIVIDE
    elif char == "^":
        return POWER
    elif char == "°":
        return ROOT
    elif char == "(":
        return OPEN_BRACES
    elif char == ")":
        return CLOSE_BRACES
    else:
        return VARIABLE


def get_category(tokenType):
    if (tokenType == NUMBER) or (tokenType == VARIABLE):
        return VALUE
    elif (tokenType == PLUS) or (tokenType == MINUS) or (tokenType == TIMES) or (tokenType == DIVIDE) or (tokenType == POWER) or (tokenType == ROOT):
        return OPERATION
    elif (tokenType == OPEN_BRACES) or (tokenType == CLOSE_BRACES):
        return BRACES


def tokenize(inputString):
    tokens = []
    
    currentToken = inputString[0]
    currentTokenType = get_type(currentToken)
    
    for char in inputString[1:]:
        currentType = get_type(char)
        if (currentType != currentTokenType) or (get_category(currentType) is OPERATION) or (get_category(currentType) is BRACES):
            tokens.append(Token(currentToken, currentTokenType, get_category(currentTokenType)))
            currentToken = char
            currentTokenType = currentType
        else:
            currentToken += char

    tokens.append(Token(currentToken, currentTokenType, get_category(currentTokenType)))

    return tokens