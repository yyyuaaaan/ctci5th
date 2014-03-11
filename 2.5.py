"""

__author__ = 'anyu'

You have two numbers represented by a linked list, where each node contains a
singledigit.The digits are stored in reverse order,such that the 1'sdigitisat thehead
of the list. Write a function that adds the two numbers and returns the sum as a
linked list.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
"""

def addlistforwardorder(l1,l2):
    # using stacks, pretend not list, but linkedlist

    l1tempstack=[]
    l2tempstack=[]
    if len(l1)>len(l2): l2tempstack+=[0]*(len(l1)-len(l2))
    if len(l2)>len(l1): l1tempstack+=[0]*(len(l2)-len(l1))

    for x in l1: l1tempstack.append(x)
    for x in l2: l2tempstack.append(x)

    ltemp = []
    while l1tempstack != []:
        ltemp.append(l1tempstack.pop()+l2tempstack.pop())

    for p1 in range(len(ltemp)):
        if ltemp[p1]>9:
            ltemp[p1] -= 10
            ltemp[p1+1] +=1   # do  maintain carry implicitly

    return ltemp



print addlist([1,2,3,4],[1,2,9])
print addlistforwardorder([4,3,2,1],[9,2,1])

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def addlist(l1,l2): # suppose two linked list
    p1 = l1
    p2 = l2
    finalresult=Node()
    presult=finalresult
    while p1 is not None and p2 is not None:
        # border condition
        if p1 is None:
            presult.next = p2
        if p2 is None:
            presult.next = p1

        #do sth
        temp = p1.data + p2.data
        if temp < 10:
            presult.data = temp
        else:
            presult.data = temp - 10
            presult.next = Node(1) # carry




