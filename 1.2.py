
"""

__author__ = 'anyu'

Implement a function void reverse (char* str) in C or C++
which reverses a null-terminated string.
Just reverse a string.
"""

def reverse_a_string(input_string_list):
    """
    we use list() to convert input str into a python list,
    because python string do not support char assignment

    """
    slist = list(input_string_list)
    for i in range(len(slist)/2): # swap two chars iteratively
        slist[i],slist[len(slist)-1-i] =\
        slist[len(slist)-1-i],slist[i]
    print slist
    return slist

reverse_a_string(reverse_a_string("fdsagfs"))
# if we recursively do this problem, it will take too much space, not in place,
# because everytime the python interpreter calls a recursive function, it set
# a new stack frame, it is too costly, in other languges surporting CPS transformation
# we can use recursive way.