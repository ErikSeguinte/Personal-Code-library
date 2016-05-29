import __future__

class Node(object):

    def __init__(self, data = None, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class linked_list(object):

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insert(self, data):
        new_head = Node(data, self.head)
        if self.head:
            self.head.prev_node = new_head
        else:
            self.tail = new_head
        self.head = new_head
            
            

    def search(self, data):
        current = self.head
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next_node

        return current



    def remove(self, data):
        pass

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node



l = linked_list()

for i in xrange(10):
    l.insert(i)

l.print_list()
print(l.head.data)
