import tokenizer as tk
import calculator as calc
import ast

inputString = input("Enter your term here: ")

tokens = tk.tokenize(inputString)

ast = ast.build(tokens)



print(calc.calculate(ast))