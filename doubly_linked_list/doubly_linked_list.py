"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.head.next.prev = None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.tail.prev.next = None
        value = self.tail.value
        self.tail = self.tail.prev
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node: ListNode):
        if node is not None:
            if node.prev is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = self.head
                self.head.prev = node
                self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is not None:
            if node != self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                self.tail = node


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node: ListNode):
        #check for valid arg
        if node is not None:
            #check list is not empty
            if not (self.head is None and self.tail is None)
                #Check if only item in the list
                if self.head == node and self.tail == node:
                    self.head = None
                    self.tail = None
                #More than one item
                else:
                    #Are we deleting the head
                    if self.head == node:
                        node.next.prev = None
                        self.head = node.next
                    else:
                        node.next.prev = node.prev
                    #Are we deleting the tail?
                    if self.tail == node:
                        node.prev.next = None
                        self.tail = node.prev
                    else:
                        node.prev.next = node.next
            self.length -= 1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max = 0
        while current_node is not None:
            if max < current_node.value:
                max = current_node.value
            current_node = current_node.next
        return max
