"""

__author__ = 'anyu'

Write code to partition a linked list around a value x,
such that all nodes less than x come before alt nodes
 greater than or equal to x.

 If this were an array, we would need to be careful about how
  we shifted elements. Array shifts are very expensive.
However, in a linked list, the situation is much easier. Rather than shifting
and swapping elements, we can actually create two different linked lists:
one for elements less than x, and one for elements greater than or equal to x.
We iterate through the linked list, inserting elements into our before
list or our after list. Once we reach the end of the linked list and
have completed this splitting, we merge the two lists.

filter: we trade less efficiency to less bugs and debugging time

"""
def partitioned(value,llist):
    ltvalue=filter(lambda x:x<= value, llist)
    gtvalue=filter(lambda x:x> value, llist)
    llist = ltvalue+gtvalue
    return llist

def partitioned2(value,llist):
    templist=[]
    for p1 in range(len(llist)):
            if llist[p1]>=value:
                templist.append(llist[p1])
            else:
                templist.insert(0,llist[p1])
    return  templist

print partitioned(3,[1,2,5,6,7,1,2,3,4,5,6,])
print partitioned2(3,[1,2,5,6,7,1,2,3,4,5,6,])


class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def partitioned(value,llist):
    """
    if use one list, can be cumbersome, creat two list
    """
    lesslist=[]
    greaterlist=[]
    p = llist
    while p is not None:
        if p.data >+ value: greaterlist.append(p.data)
        else:
            lesslist.append(p.data)
        p = p.next
    return  lesslist + greaterlist


