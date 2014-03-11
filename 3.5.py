"""
__author__ = 'anyu'

3.5 Implement a MyQueue class which implements a queue using two stacks.
We can use our second stack to reverse the order of the elements (by popping s i

We can implement a"lazy"approach where we let the elements sit
in s2 until we absolutely must reverse the elements.

During your actual interview, you may find that you forget the exact API calls.
Don't stress too much if that happens to you. Most interviewers are okay with
your asking for them to refresh your memory on little details.
They're much more concerned with your big picture understanding.

"""

# this is cumbersome, implement a real queue class which take a linkedlist parameter
# then implement a linkedlist with two stacks,bingo!
# take array or linkedlist as parameter, or inherit, or use Queue class's object, good idea

class myqueueforfun(object):
    def __init__(self):
        self.stk1=[]
        self.stk2=[]
        self.qfrond=0
        self.qend=0
        self.size = 10

    def enqueue(self,value):
        if self.isfull():
            print "queue full"
        elif self.stk1 == [] and self.stk2 !=[] :
            while self.stk2 != []:
                self.stk1.append(self.stk2.pop())
            self.stk1.append(value)
            self.qfrond += 1
        else:
            self.stk1.append(value)
            self.qfrond += 1
        return

    def dequeue(self):
        if self.isempty():
            print "queue empty!"
            return
        else:
            if len(self.stk2)>len(self.stk1):
                v = self.stk2.pop()
            else:
                v = self.stk1.pop()
            self.qfrond -= 1
            return v


    def isempty(self):
        return self.stk1==[] and self.stk2 == []

    def isfull(self):
        return self.qfrond == 10



q1 = myqueueforfun()

q2 = myqueueforfun()

#testing
from random import randrange
for step in xrange(20):
	operation = randrange(10)
	if operation < 7:
		q1.enqueue(operation)
		q2.enqueue(operation)
		print "push", operation
	elif not q2.isempty():
		print "pop", q1.dequeue(), q2.enqueue(operation)
