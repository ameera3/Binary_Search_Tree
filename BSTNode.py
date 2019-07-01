# Class name: BSTNode
# Instance Variables: left (left child of node)
#                     right (right child of node)
#                     parent (parent of node)
#                     Date (data stored in node)
# Description: Implements a BST Node
# Methods: constructor, successor, minValue(), northWest()

class BSTNode:

    # Constructor. Initialize a BSTNode with the given Data item,
    # no parent, and no children.

    def __init__(self, key):

        # left child of node
        self.left = None

        # right child of node
        self.right = None

        # parent of node
        self.parent = None

        # data stored in node
        self.val = key

    # Return the successor of this BSTNode in a BST, or None if none.
    # PRECONDITION: this BSTNode is a node in a BST.
    # POSTCONDITION:  the BST is unchanged.
    # RETURNS: the BSTNode that is the successor of this BSTNode,
    # or None if there is none.

    def successor(self):

        # If right child is present, find the minimum value of
        # the right subtree
        if self.right != None:
            return (self.right).minValue()

        # If no parent, return None
        elif self.parent == None:
            return None

        # If node is the left child of its parent, return parent
        elif self == (self.parent).left:
            return self.parent

        # If node is right child of its parent and has no right
        # child of its own, the successor is an ancestor of the
        # node. We travel up the tree through the right children
        # until we can go no further.
        else:
            return (self.parent).northWest()

    # Return the BSTNode with minimum value in a binary search tree
    # PRECONDITION: this BSTNode is a node in a BST
    # POSTCONDITION: the BST is unchanged
    # RETURNS: The BSTNode that has minimum value in a BST

    def minValue(self):
        if self.left != None:
            return (self.left).minValue()

        else:
            return self

    # Go northwest until you can't. Go north if you can,
    # otherwise return 0.
    # PRECONDITION: this BSTNode is a node in a BST.
    # POSTCONDITION: the BST is unchanged.
    # RETURNS: the BSTNode that is an ancestral successor of node or 0

    def northWest(self):
        if self.parent == None:
            return None

        elif self == (self.parent).right:
            return (self.parent).northWest()

        else:
            return self.parent

    # Print Node's value, parent, left child, right child
    def __repr__(self):
        valString = str(self.val) if self != None else "None"
        parentString = str((self.parent).val) if self.parent != None else "None"
        leftString = str((self.left).val) if self.left != None else "None"
        rightString = str((self.right).val) if self.right != None else "None"
        return ("value: " + valString + " parent: " + parentString + " left: " +
        leftString + " right: " + rightString)
