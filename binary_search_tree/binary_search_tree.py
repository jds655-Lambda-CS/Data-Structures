"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from jds_queue import Queue



class BSTNode:

    queue: Queue()

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # class BinarySearchTree:
    #     def __init__(self, value):
    #         self.root = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node is not None:
            if target == node.value:
                return True
            elif target > node.value:
                node = node.right
            elif target <= node.value:
                node = node.left
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        result = self.value
        node = self.right
        while node is not None:
            result = node.value
            node = node.right
        return result

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        node = self
        fn(node.value)
        if node.right is not None:
            node.right.for_each(fn)
        if node.left is not None:
            node.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        currentNode = self
        if currentNode.left is None and currentNode.right is None:
            print(currentNode.value)
            return
        if currentNode.left is not None:
            currentNode.left.in_order_print()

        print(currentNode.value)

        if currentNode.right is not None:
            currentNode.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        currentNode = self
        print(currentNode.value)
        if currentNode.left is None and currentNode.right is None:
            # print(currentNode.value)
            return
        if currentNode.left is not None:
            currentNode.left.pre_order_dft()
        if currentNode.right is not None:
            currentNode.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        currentNode = self
        if currentNode.left is None and currentNode.right is None:
            print(currentNode.value)
            return
        if currentNode.left is not None:
            currentNode.left.post_order_dft()
        if currentNode.right is not None:
            currentNode.right.post_order_dft()
        print(currentNode.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(25)

bst.insert(15)
bst.insert(10)
bst.insert(4)
bst.insert(12)
bst.insert(22)
bst.insert(18)
bst.insert(24)
bst.insert(50)
bst.insert(35)
bst.insert(31)
bst.insert(44)
bst.insert(70)
bst.insert(66)
bst.insert(90)

print("In Order:\n")
bst.in_order_print()
print("\n\nPre Order:\n")
bst.pre_order_dft()
print("\n\nPost Order:\n")
bst.post_order_dft()


#
# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
