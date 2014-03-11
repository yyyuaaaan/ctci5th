"""__author__ = 'anyu'

A magic index in an array A[l.. .n-l] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?,then i will use linear scan
"""

def cleanbs(array): # wrong, see 11.3, to get the reason
    """
    clean binary index search, require l=0
    """
    if len(array) is 1:
        if array[0] == 0: return 0
        else: return -1

    mid = (len(array)-1)//2
    if array[mid] == mid: return mid

    if array[mid]<mid: return cleanbs(array[mid:])
    else: return cleanbs(array[:mid])

def magindex(array, start, end):
    if len(array) < (end-start+1) or start>end or start<0: return -1
     # do not forget 'start' index
    #return cleanbs(array[start:end])+start also wrong!
    if cleanbs(array[start:end]) == -1: return -1
    else: return cleanbs(array[start:end])+start