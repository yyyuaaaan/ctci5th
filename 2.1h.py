"""

__author__ = 'anyu'

Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
import itertools

def remove_dup(linkedlist):
    """
    use list as linkedlist in python
    use dict as hash table
    """

    listtemp=list()
    for x in linkedlist:
        if (x in listtemp) == False:    # "x in listtemp == False:" is not ok. pay attention to expression priority
            listtemp.append(x)

    linkedlist = listtemp
    return linkedlist

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def remove_dup2(linkedlist):
    """
    no extra buffer
    if make yourself a python linked list, it will be very cumbersome.
    trade off between time and space, and also readability, maintainability

    assume linkedlist is a list() in python
    assume current and rider are pointers of linkedlist
    if define a new Node class, new space, less efficient than official python

    This code runs in 0(1) space, but 0(N2) time.
    """

    if linkedlist.next is None or linkedlist is None:
        return linkedlist
    current = linkedlist, rider = linkedlist.next
    while current.next is not None:
        while rider.next is not None: # p.next = q.next tricky, this is not right,use helper function maybe
            if rider.data == current.data:
                rider.next.data = rider.data # det rider
                rider.next = rider.next.next
            rider = rider.next
        if current.data == rider.data: # del rider if last is none
            current.next = None
        current =current.next






print remove_dup([1,2,3,4,4,'sfd',5,5,5,7])

print remove_dup2([1,2,3,4,4,5,5,5,7])
