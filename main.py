import tokenizer as tk
import calculator as calc
import ast

inputString = input("Enter your term here: ")

tokens = tk.tokenize(inputString)

tree = ast.create_tree(tokens)

print(calc.calculate(tree))