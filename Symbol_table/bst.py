import __future__
import st, frequencyCounter

class Node(object):

    def __init__(self, key, value, N=1, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.N = N

class BST(st.ST):

    def __init__(self):

        self.root = None

    def put(self, key, value):

        self.root = self.insert(self.root, key, value)

    def insert(self, node, key, value):

        if node is None:
            return Node(key, value)

        if key > node.key:
            node.right = self.insert(node.right, key, value)
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.value = value

        node.N = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def get(self, key):
        return self.get_node(self.root, key)

    def get_node(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif node.key > key:
            return self.get_node(node.left, key)
        elif node.key < key:
            return self.get_node(node.right, key)

    def size(self):
        return self.node_size(self.root)

    def node_size(self, node):
        if node is None:
            return 0
        else:
            return node.N


    def keys(self):
        stack = []

        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right


frequencyCounter.main(BST)
#
# bst = BST()
# bst.put('A', 1)
# bst.put("A", bst.get("A") + 1)
# bst.put("A", bst.get("A") + 1)
# bst.put("A", bst.get("A") + 1)
# bst.put("B", 1)
# print("B" > "A")
# bst.put("B", bst.get("B") + 1)
# print(bst.contains("B"))
# print(bst.get("A"))
# print(bst.get("B"))
