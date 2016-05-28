import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Bst:
    """ Implements a binary search tree.
    """

    def __init__(self, values):
        self.root = Node(None)

        self.insert_list(values)

    def insert(self, value):
        if self.root.value:
            self._add(value, self.root)
        else:
            self.root = Node(value)

    def _add(self, value, node):
        if value > node.value:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)

        else:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)

    def __repr__(self):
        return self._repr(self.root)

    def _repr(self, node, indent=0):
        string = ('\t' * indent) + str(node.value) + '\n'

        if node.left:
            string += ('\t' * (indent + 1)) + 'Left:\n'
            string += self._repr(node.left, indent + 1)

        if node.right:
            string += ('\t' * (indent + 1)) + 'Right:\n'
            string += self._repr(node.right, indent + 1)

        return string

    def insert_list(self, bunnies):
        for bunny in bunnies:
            self.insert(bunny)


def count(tree):
    """ Counts the number of nodes, including the root.
    """

    return 1 + count(tree.left) + count(tree.right) if tree else 0


def interleave(left_size, right_size):
    """ Finds the number of possible ways to interleave the left and right sub tree

    We are interested only in the combinations with fixed ordering, giving the formula:
    (left_size + Right_size)! / (left_size! * right_size)
    """

    return math.factorial(left_size + right_size) / (math.factorial(left_size) * math.factorial(right_size))


def calculate(tree):
    """ Returns the number of combinations.

    For a leaf, the number is 1. For a non-leaf node with one child, the
    number equals to the number of topological orderings for the child. For a
    non-leaf node with two children with subtree sizes |L| and |R|, both having
    l and r orderings, resp., the number equals to (l * r * INT(|L|, |R|)),
    where INT is the possible number of interleavings of |L| and |R|
    """

    if not tree:
        # Empty sub tree.
        return 1

    left_size = count(tree.left)
    right_size = count(tree.right)

    left_orderings = calculate(tree.left)
    right_orderings = calculate(tree.right)

    return left_orderings * right_orderings * interleave(left_size, right_size)


def answer(seq):
    tree = Bst(seq)
    return str(calculate(tree.root))


print(answer([5, 9, 8, 2, 1]))
