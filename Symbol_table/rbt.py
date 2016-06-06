import __future__
from collections import deque
import st, frequencyCounter

class Node(object):

    def __init__(self, key, value, N=1, color = True, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.color = color
        self.N = N

    def color_black(self):
        self.color = False

    def color_red(self):
        self.color = True

    def filp_color(self):
        self.color_red()
        self.left.color_black()
        self.right.color_black()


class BST(st.ST):

    def __init__(self):

        self.root = None

    def put(self, key, value=None):
        if value is None:
            value = key
        self.root = self.insert(self.root, key, value)
        self.root.color_black

    def is_red(self, node):
        if node is None:
            return False
        else:
            return node.color

    def insert(self, node, key, value):

        if node is None:
            return Node(key, value)

        if key > node.key:
            node.right = self.insert(node.right, key, value)
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.value = value
            
        if self.is_red(node.right) and not self.is_red(node.left):
            # Right leaning red link. Rotate to the left.
            node =self.rotate_left(node)
        if self.is_red(node.left) and (node.left and self.is_red(node.left.left)):
            # 2 red links. Rotate to the right
            node =self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            # both children linked red. Pass red up the tree.
            node.filp_color()

        node.N = self.node_size(node.left) + self.node_size(node.right) + 1
        return node


    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color_red()
        x.N = h.N
        h.N = self.node_size(h.left) + self.node_size(h.right) + 1
        return x

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color_red()
        x.N = h.N
        h.N = self.node_size(h.left) + self.node_size(h.right) + 1
        return x

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


    def range_root(self, low, high, queue = deque()):
        node = self.root
        left = []
        middle = []
        right = []
        
        stack = deque()
        queue = deque()

        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                if node.key >= low:
                    node = node.left
                else:
                    node = None
            else:
                node = stack.pop()
                if low <= node.key <= high:
                    yield node
                if node.key <= high:
                    node = node.right
                else:
                    node = None


    def keys(self):
        stack = []

        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right

    def del_min(self, node = None):
        if node is None:
            node = self.root

        self.root = self.del_min_node(node)

    def del_min_node(self, node):
        
        if node.left:
            node.left = self.del_min_node(node.left)
        else:
            return node.right

        node.N = self.node_size(node.left) + self.node_size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            # Delete this node.

            if node.left is None and node.right is None:
                # No children. Simply delete node
                return None
            elif (node.left and node.right is None):
                return node.left
            elif node.left is None:
                return node.right
            else:
                # 2 children
                temp = node
                node = self.min_node(node)
                node.left = temp.left
                node.right = self.del_min_node(temp.right)
        return node

    def min_root(self):
        return self.min_node(self.root)

    def min_node(self, node):
        if node.left is None:
            return node
        else:
            return self.min_node(node.left)



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

bst = BST()
bst.put('s',0)
bst.put('e',1)
bst.put('a',2)
bst.put('r',3)
bst.put('c',4)
bst.put('h',5)
bst.put('e',6)
bst.put('x',7)
bst.put('a',8)
bst.put('m',9)
bst.put('p',10)
bst.put('l',11)
bst.put('e',12)

for node in bst.keys():
    print(node.key)
