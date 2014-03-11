"""__author__ = 'anyu'

4.3 Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

One way to implement this is to use a simple root.insertNode(int v) method
This will indeed construct a tree with minimal height but it will not do so very efficiently.
Each insertion will require traversing the tree, giving a total costofO(N log N) to the tree.
Alternatively, we can cut out the extra traversals by recursivelyusing the createMin-
imalBST method. This method is passed just a subsection of the array and returns the


Although this code does not seem especially complex, it can be very easy to make little off-by-one errors.
 Besure to test these parts of the codevery thoroughly  (But I DID NOT! ONE TIME FINISHED MASTERPIECE:) )

discuss that it automatically maintain a binary SEARCH tree here
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return "( " + str(self.data) + " ( " + str(self.left) + " | " + str(self.right) + "))"

def creat_bst(sorted_array):
    if len(sorted_array) == 0: return "nul array"
    if len(sorted_array) == 1:
        bst=Node(sorted_array[0])
        return bst
    else:
        mid = len(sorted_array)//2
        bst = Node(sorted_array[mid])
        bst.left=creat_bst(sorted_array[:mid])
        bst.right=creat_bst(sorted_array[mid+1:])
        return bst

intarray1=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515]
print str(creat_bst(intarray1))
