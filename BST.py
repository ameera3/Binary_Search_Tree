from BSTIterator import BSTIterator
from BSTNode import BSTNode

# Class name: BST
# Instance Variables: root (the root of the BST)
#                     isize (number of elements in BST)
#                     iheight (height of BST)
# Description: Implements a BST
# Methods: init, insert, find, begin, first, end, traverse, traverseHelper

class BST:

    # Default constructor.
    # Initialize an empty BST.

    def __init__(self):

        # root of BST
        self.root = None

        # Number of data items in this BST
        self.size = 0

        # Height of BST
        self.height = 0

    # Given a reference to a Data item, insert a copy of it in this BST.
    # Return true if the item was added to this BST as a result of this
    # call to insert.
    # Return false if an item equal to this one was already in this BST.

    def insert(self, Data):

        # Working or current node
        working = self.root

        # Parent of working node
        parent = None

        # How far we went down in the BST to insert
        localHeight = 0

        # While working node is not null, if item is less than data of
        # working node, go to left, and increment local height. If data
        # in working node is greater than item, go to right, and increment
        # local height. Otherwise, data in working node equals item;
        # return false to prevent duplicate insert.

        while(working != None):
            parent = working
            if(Data < working.val):
                working = working.left
                localHeight+=1
            elif(working.val < Data):
                working = working.right
                localHeight+=1
            else:
                return False

        # If insertion should happen, compare local height to height of
        # tree. Update height of tree if local height > height
        if(localHeight > self.height):
            self.height = localHeight

        # Create a new BST node whose data is item and whose parent is
        # the parent of the working node.  Insert it into the tree. Update
        # size of tree and return true

        working = BSTNode(Data)
        working.parent = parent
        if self.root == None:
            self.root = working
        else:
            if Data < parent.val:
                parent.left = working
            else:
                parent.right = working
        self.size+=1
        return True

    # Find a Data item in the BST.
    # Return an iterator pointing to the item, or pointing past
    # the last node in the BST if not found.

    def find(self, Data):

        # working or current node
        working = self.root

        # While working is not null, if item is less than data in working
        # node, go left. If data in working node is less than item, go
        # right. Otherwise, data in working node equals item, so return
        # iterator pointing to item.

        while(working != None):
            if Data < working.val:
                working = working.left
            elif working.val < Data:
                working = working.right
            else:
                return BSTIterator(working)

        # If item is not found, return iterator pointing past the last
        # node in the BST

        return BSTIterator(None)

    # Traverse the BST in order

    def traverse(self):

        # Call traverseHelper function taking root as a parameter
        self.traverseHelper(self.root)

    # Recursive inorder traversal 'helper' function

    def traverseHelper(self, working):

        # If current node is not null
        # Recursively traverse left subtree
        # Print current node data
        # Recursively traverse right subtree

        if working != None:
            self.traverseHelper(working.left)
            print(repr(working))
            self.traverseHelper(working.right)

    # Return an iterator pointing to the first item in the BST
    # (not the root).

    def begin(self):
        return BSTIterator(self.first())


    # Find the first element of the BST

    def first(self):

        # working or current node
        working = self.root

        # parent of working node
        parent = None

        # keep going left until you can't
        while working != None:
            parent = working
            working = working.left
        return parent

    # Return an iterator pointing past the last item in the BST.

    def end(self):
        return BSTIterator(None)


