class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add(self, value, tail=True):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if tail:
                self.tail.nextnode = newnode
                self.tail = newnode
            else:
                oldheadnode = self.head
                self.head = newnode
                self.head.nextnode = oldheadnode

    def add_to_tail(self, value):
        self.add(value)

    def add_to_head(self,value):
        self.add(value, False)

    def remove(self, tail=True):
        if tail:
            if self.tail is None:
                return None
            elif self.head == self.tail:
                value = self.tail.get_value()
                self.head = None
                self.tail = None
                return value
            else:
                node = self.head
                value = None
                while node is not None:
                    if node.nextnode == self.tail:
                        value = self.tail.value
                        self.tail = node
                    node = node.nextnode
                return value
        else:
            if self.head is None:
                return None
            # list with 1 node
            elif self.head == self.tail:
                value = self.head.get_value()
                self.head = None
                self.tail = None
                return value
            # LL with 2 or more nodes
            else:
                value = self.head.get_value()
                self.head = self.head.get_next()
                return value

    def remove_head(self):
        return self.remove(False)

    def contains(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            else:
                node = node.nextnode
        return False

    def get_max(self):
        if self.head is None:
            return None
        else:
            node = self.head
            max = node.value
            while node is not None:
                if node.value > max:
                    max = node.value
                node = node.nextnode
            return max


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.nextnode = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.nextnode