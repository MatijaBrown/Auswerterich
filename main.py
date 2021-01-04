import tokenizer as tk
import calculator as calc
import ast
import test

def evaluate(inputString):
    tokens = tk.tokenize(inputString)

    tree = ast.create_tree(tokens)

    return calc.calculate(tree)

inputString = input("Enter your term here: ")

if len(inputString) > 0:      
    print(evaluate(inputString))
else:
    test.test()