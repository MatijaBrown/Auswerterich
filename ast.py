import tokenizer as tk

class Node():
    pass


class Value(Node):

    def __init__(self, value):
        self.value = value
        self.isNumber = value.type == tk.NUMBER

    def as_number(self):
        return self.value.get_as_number()

    def __str__(self):
        return "Value({v})".format(
            v = self.value.litteral,
        )

    def __repr__(self):
        return self.__str__()


class Operation(Node):

    def __init__(self, left, op, pri, right):
        self.left = left
        self.op = op
        self.pri = pri
        self.right = right

    def __str__(self):
        return "Operator({l} {op} {r} p={pri})".format(
            l = self.left,
            op = self.op,
            r = self.right,
            pri = self.pri
        )

    def __repr__(self):
        return self.__str__()


class Tree():
    
    root = None
    isIllegal = False

    def empty(self):
        return self.root == None

    def __str__(self):
        return "Tree({rt})".format(
            rt = self.root
        )

    def __repr__(self):
        return self.__str__()


tree = Tree()

PRI_PLUS = 1
PRI_MINUS = -PRI_PLUS
PRI_TIMES = 2
PRI_DIVIDE = -PRI_TIMES
PRI_POWER = PRI_MAX = 3
PRI_ROOT = PRI_MIN = -PRI_POWER
PRI_NONE = 0

def priority(op):
    if op.type == tk.PLUS:
        return PRI_PLUS
    elif op.type == tk.MINUS:
        return PRI_MINUS
    elif op.type == tk.TIMES:
        return PRI_TIMES
    elif op.type == tk.DIVIDE:
        return PRI_DIVIDE
    elif op.type == tk.POWER:
        return PRI_POWER
    elif op.type == tk.ROOT:
        return PRI_ROOT
    else:
        return PRI_NONE


def create_node(token):
    if token.category == tk.VALUE:
        node = Value(token)
    elif token.category == tk.OPERATION:
        pri = abs(priority(token)) + depthInBraces * PRI_MAX

        rootPriority = 0
        if isinstance(tree.root, Operation):
            rootPriority = abs(tree.root.pri)

        if (pri <= rootPriority) or (rootPriority == PRI_NONE):
            # Insert Above
            node = Operation(tree.root, token, pri, None)
            tree.root = None
        else:
            # Insert Below
            currentNode = tree.root
            while (currentNode.right != None) and (not(isinstance(currentNode.right, Value))):
                currentNode = currentNode.right
            node = Operation(currentNode.right, token, pri, None)
    
    if tree.empty():
        tree.root = node
    else:
        currentNode = tree.root
        while (currentNode.right != None) and (not(isinstance(currentNode.right, Value))):
            currentNode = currentNode.right
        currentNode.right = node


def error(message):
    print(message)
    exit(-1)


def create_tree(tokens):
    global depthInBraces
    depthInBraces = 0
    for i in range(len(tokens)):
        token = tokens[i]

        if ((i == 0) or (tokens[i - 1].category == tk.OPERATION) or (tokens[i - 1].type == tk.OPEN_BRACES)) and (token.category == tk.OPERATION):
            if (token.type != tk.MINUS) and (token.category == tk.OPERATION):
                error("Illegal expression!")
            elif token.category == tk.OPERATION:
                if i == len(tokens) - 1:
                    error("Illegal expression!")
                depthInBraces += 1
                create_node(tk.Token("0", tk.NUMBER, tk.VALUE))
                create_node(tk.Token("-", tk.MINUS, tk.OPERATION))
                depthInBraces -= 1
        elif token.category == tk.BRACES:
            if token.type == tk.OPEN_BRACES:
                depthInBraces += 1
            else:
                depthInBraces -= 1
            if depthInBraces < 0:
                error("More ')' than '('!")
        else:
            create_node(token)

    if depthInBraces > 1:
        error("More '(' than ')'!")
    return tree