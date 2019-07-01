# Simple Test Driver for BST

from BST import BST
import sys

# Create a list of some ints
L = [3,4,1,100,-33]

# Create an instance of BST
b = BST()

# Insert into b the ints in L. All these inserts are unique so they
# should all return True
for i in range(len(L)):
    if not b.insert(L[i]):
        print("Incorrect bool return value when inserting " + str(L[i]))
        sys.exit()
print("Insert Int OK.")

# Test Duplicate Insertion. Should return false.
if b.insert(L[0]):
    print("Incorrect bool return value when inserting " + str(L[0]))
    sys.exit()
print("Duplicate Insert Int OK.")

# Test size
print("Size is: " + str(b.size))
if b.size != len(L):
    print("... which is incorrect.")
    sys.exit()

# Test height
print("Height is: " + str(b.height))
if b.height != 2:
    print("... which is incorrect.")
    sys.exit()

# Test find return value for all ints in the BST
for i in range(len(L)):
    if (b.find(L[i])).getVal() != L[i]:
        print("Incorrect return value when finding " + str(L[i]))
        sys.exit()
print("Find Int OK.")

# Test find return value for int not in BST.
if b.find(2) != b.end():
    print("Incorrect return value when finding " + str(2))
    sys.exit()
print("Does Not Find Int OK.")

# Sort the list, to compare with inorder iteration on the BST
L.sort()

# Test BST iterator; should iterate inorder
print("traversal using iterator:")
en = b.end()
it = b.begin()
for i in range(len(L)):
    if it.getVal() != L[i]:
        print(str(it.getVal()) + "," + str(L[i]) + ": Incorrect inorder iteration of BST")
        sys.exit()
    next(it)
print("Traversal Int OK.")

# Test inorder traverse function
print("traversal using traverse:")
b.traverse()

