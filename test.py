import tokenizer as tk
import ast
import calculator as calc
import testData as td

def evaluate(inputString):
    tokens = tk.tokenize(inputString)

    tree = ast.create_tree(tokens)

    return calc.calculate(tree)

def test():
    for i in range(len(td.testInput)):
        testIn = td.testInput[i]
        testResult = evaluate(testIn)
        testOut = td.testOutput[i]
        print(testIn, " =", testResult, end=' ')
        if testResult == testOut:
            print("| Succeeded")
        else:
            print("| Correct result:", testOut)

        ast.tree = ast.Tree()
