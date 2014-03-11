"""
__author__ = 'anyu'

Write a program to sort a stack in ascending order. You should not make any assumptions
about how the stack is implemented. The following are the only functions that should be
used to write this program: push | pop | peek | isEmpty.

1,insertion sort, use the helping stack

2,unlimited stack, use recursion   i.e.If we were allowed to use unlimited stacks,
 we could implement a modified quicksort or mergesort.
With the mergesort solution, we would create two extra stacks and divide the stack
into two parts. We would recursively sort each stack, and then merge them back together
in sorted order into the original stack. Note that this would require the creation of
two additional stacks per level of recursion.

3,priority queue, until all
void Qsort(stack<int> &s){
    priority_queue< int,vector<int>,greater<int> > q;
    while(!s.empty()){
        q.push(s.top());
        s.pop();
    }
    while(!q.empty()){
        s.push(q.top());
        q.pop();
4 use list as linked list, to do selection sort, or make a  linked list by myself
% use list to implement priority queue, because list is hashtable O(1), better then priority queue

"""
def ssort(s):
    t= New stack   # simulate selection sort,This algorithm is 0(N2) time and 0(N) space.
    while not s.isEmpty:
        value = s.pop
        while (not t.isEmpty) and value < t.peek:
            s.push(t.peek)
            t.pop
        t.push(value)
    return t





