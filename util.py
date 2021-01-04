import tokenizer as tk

def swap_plus_minus(tokens):
    lastToken = None
    for token in tokens:
        if (lastToken == None) or isinstance(lastToken, list) or (lastToken.category == tk.OPERATION):
            lastToken = token
            continue

        if token.type == tk.PLUS:
            token.type = tk.MINUS
            token.litteral = "-"
        elif token.type == tk.MINUS:
            token.type = tk.PLUS
            token.litteral = "+"

        lastToken = token
    return tokens


def swap_times_divide(tokens):
    lastToken = None
    for token in tokens:
        if (lastToken == None) or isinstance(lastToken, list) or (lastToken.category == tk.OPERATION):
            lastToken = token
            continue

        if token.type == tk.TIMES:
            token.type = tk.DIVIDE
            token.litteral = "/"
        elif token.type == tk.DIVIDE:
            token.type = tk.TIMES
            token.litteral = "*"

        lastToken = token
    return tokens