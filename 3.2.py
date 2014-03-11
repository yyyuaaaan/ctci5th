"""

__author__ = 'anyu'

How would you design a stack which, in addition to push and pop,
also has a function min which returns the minimum element? Push,
pop and min should all operate in O(1) time.


solution 1: priority queue, no, push is ok, when we pop, looking for the next min will take more than O(1)
solution 2 change stack item to (iter,min) tuper, costly
solution 3. Use an additional python list to keep track of mins (Save space)

"""
class Stack(object):
    def __init__(self,size=100):
        self.stacksize= size
        self.stackbottom=[None]*size
        self.sp = 0 # fix later-1

    def isempty(self):
        return self.sp == 0
    def isfull(self):
        return self.sp == self.stacksize - 1
    def push(self,value):
        if self.isfull: return "stack full"
        self.stackbottom[self.sp+1] = value
        self.sp = self.sp +1

    def pop(self):
        if  self.isempty: return "empty"
        temp = self.stackbottom[self.sp]
        self.stackbottom[self.sp] = None
        self.sp = self.sp - 1
        return temp

    def peek(self):
        if self.isempty(): return "empty"
        return self.stackbottom[self.sp]


class Stackwithmin(Stack):
    """
    more concise, only need to change the pop push, and add a trivial getmin
    do not forget goddam self!
    """
    def __init__(self,size=100, minlist=[]):
        self.stacksize= size
        self.stackbottom=[None]*size
        self.sp = 0 # fix later-1
        self.minlist=minlist

    def push(self,value):
        if self.isfull: return "stack full"
        self.stackbottom[self.sp+1] = value

        if self.isempty(): self.minlist.append(value)
        if value < self.minlist[-1]: self.minlist.append(value)
        else: self.minlist.append(self.minlist[-1])

        self.sp = self.sp +1

    def pop(self):
        if  self.isempty: return "empty"
        temp = self.stackbottom[self.sp]
        self.stackbottom[self.sp] = None

        self.minlist.pop()

        self.sp = self.sp - 1
        return temp

    def getmin(self):
        return self.minlist[self.sp]
