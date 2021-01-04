import tokenizer as tk
import ast

def do_operations(tree):
    left = calculate(tree.left)
    right = calculate(tree.right)
    return do_tree_operations(left, tree.value, right)

def do_tree_operations(left, op, right):
    if op == tk.PLUS:
        return left + right
    elif op == tk.MINUS:
        return left - right
    elif op == tk.TIMES:
        return left * right
    elif op == tk.DIVIDE:
        return left / right
    elif op == tk.POWER:
        return pow(left, right)
    elif op == tk.ROOT:
        return pow(left, 1/right)


def calc(node):
    if isinstance(node, ast.Value):
        return node.as_number()

    left = calc(node.left)
    right = calc(node.right)
    return do_tree_operations(left, node.op.type, right)


def calculate(tree):
    tn = tree.root
    return calc(tn)
