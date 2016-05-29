import __future__

class Node(object):

    def __init__(self, data = None, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node

    def print_node(self):
        if (self.data):
            print("self", self.data, ", next:", self.next_node.data, ", prev:", self.prev_node.data)
        else:
            print("Empty Node")


class linked_list(object):

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insertleft(self, data):
        new_head = Node(data, self.head)
        if self.head:
            self.head.prev_node = new_head
        else:
            self.tail = new_head
        self.head = new_head
            
            

    def search(self, data):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                prev = current
                current = current.next_node
        if current:
            return current, prev
        else:
            return None

    def print_node(self, data):
        node, _ = self.search(data)

        if node:
            node.print_node()
        else:
            print ("Node does not Exist")



    def remove(self, data):
        node, prev = self.search(data)

        # Node not found.
        if not node:
            return
        nxt = node.next_node

        # Node is a middle link with a previous and next
        if prev and nxt:
            prev.next_node = nxt
            nxt.prev_node = prev

        #  Node is tail node. No next node.
        elif prev and not nxt:
            prev.next_node = None
            self.tail = node.prev_node

        #  Node is head node. No previous node.
        elif nxt and not prev:
            nxt.prev_node = None
            self.head = node.next_node

        #  Node is both head and tail, leaving empty list.
        else:
            self.head = None
            self.tail = None

        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node



if __name__ == "__main__":
    l = linked_list()

    for i in xrange(10):
        l.insertleft(i)

    l.remove(4)
    l.print_list()

    l.print_node(3)
