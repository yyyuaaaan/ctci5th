"""
__author__ = 'anyu'

An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they
can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures to maintain
this system and implement operations such as enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the builtin LinkedList data structure.

single linkedlist, dequeue complex
two linkedlist, have to maintain a timestamp

"""

class aqueue(object):

    def __init__(self):
        listqueue = LinkedList()

    def enqueue(self,value):
        listqueue.append(value)


    def dequeueAny(self):
        if not isEmpty:
           value = listqueue[0]
           del(listqueue[0])
           return value

    def dequeueDog(self):
        if 'dog' in listqueue:
            temp = listqueue[listqueue.index('dog')]
            del(listqueue[listqueue.index('dog')])
            return temp

    def dequeueCat(self):
        pass

    def isEmpty(self):
        return listqueue ==[]


