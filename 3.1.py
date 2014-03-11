"""

__author__ = 'anyu'

3.1 Describe how you could use a single array to implement three stacks.
可以以数组的头和尾作为栈底分别维护两个栈，然后第三个栈以数组中间位置作为栈底，
左右交替入栈，当有栈顶碰撞时作为溢出处理。可能比较非主流的想法。。但实现麻烦, flexible in size!!!
Alternatively, we can be flexible in our space allocation,
but this significantly increases the complexity of the problem
 Fixed Division
int stackSize = 100;

below is cumbersome:
class SingleArrayStacks(object):

    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def push(self, stacknum, value):
        if self.pointer[stacknum] + 1 >= self.stacksize:
            print "Out of space"
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = value

    def pop(self, stacknum):
        if self.pointer[stacknum] < 0:
            return "Trying to pop an empty stack."
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data

    def peek(self, stacknum):
        if self.pointer[stacknum] < 0:
            print "Empty stack"
        else:
            return self.array[self.stacktop(stacknum)]

    def isEmpty(self, stacknum):
        return self.pointer[stacknum] == -1

    def stacktop(self, stacknum):
        return self.stacksize * stacknum + self.pointer[stacknum]

easy way：
array[]0 n/3, 2n/3
stacknum 1 2 3
stackbottom[1] = array[0]
stackbottom[2]= array[n/3]
stackbottom[3]= array[2n/3]
stack pointer, stackbottom

push
pop
isempty
isfull
getitme # without delete item



!!!!
array[100], just put array[0...30] as a parameter into the stack class, and created the stack

class SingleStack(object):

    def __init__(self, inputarray):
        self.stacksize = len(inputarray)
        self.array = [None] * self.stacksize * self.number
        self.sp = 0


"""
