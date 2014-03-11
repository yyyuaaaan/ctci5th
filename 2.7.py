"""

__author__ = 'anyu'

2.7 Implement a function to check if a linked list is a palindrome,
"""
# if do it as a linked list, push all data in a stack, than popup and compare

def ispalindrome(llist):
    if len(llist)<=1:
        return True
    elif len(llist)==2:
        return llist[0]==llist[1]
    elif len(llist)==3:
        return llist[0]==llist[2]
    else:
        return ispalindrome(llist[1:len(llist)-1])


def ispalindrome2(llist):
    ltemp=llist[:]
    llist.reverse()
    return llist == ltemp

# Iterative Approach is just push in to stack, which is implicitly recursive

print ispalindrome([1,2,3,4,4,3,2,1])
