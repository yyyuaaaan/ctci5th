"""

__author__ = 'anyu'

Implement an algorithm to delete a node in the middle
 of a singly linked list, given only access to that node.
 p1 is that node to be deleted
 p2 = p1.next
 p1.data = p2.data
 p1,next = p2.next
 del(p2)

 Note that this problem cannot be solved if the node to be deleted
 is the last node in the linked list. That's ok—your interviewer wants
 you to point that out, and to discuss how to handle this case. You could,
for example, consider marking the node as dummy.

"""
def delnode(indexaspointer, llist):
    llist[indexaspointer] = llist[indexaspointer+1]
    del(llist[indexaspointer+1])

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def delnode2(indexaspointer, llist):
    if llist is None: return "null list"
    if indexaspointer.next is None:
        pass # do something later      if the given node is the last one, ,use to p, q, traverse, or just require last list node is None.
    indexaspointer.data = indexaspointer.next.data
    indexaspointer.next = indexaspointer.next.next


