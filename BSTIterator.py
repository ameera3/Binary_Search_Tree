from BSTNode import BSTNode

# Class name: BSTIterator
# Instance Variables: curr (the current node)
# Description: Implements a BST Iterator
# Methods: constructor, iter, next, getVal, equality

class BSTIterator:

    # Constructor.  Use the argument to initialize the current BSTNode
    # in this BSTIterator.

    def __init__(self, current : BSTNode):
        self.curr = current

    # Returns an iterator
    def __iter__(self):
        return self

    # Returns the next item in the iterator
    def __next__(self):
        self.curr = (self.curr).successor()
        return self

    # Returns the data stored by the iterator's current node
    def getVal(self):
        return (self.curr).val

    # equality operator for iterators
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.curr == other.curr
        else:
            return False
