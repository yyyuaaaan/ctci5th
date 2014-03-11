"""

__author__ = 'anyu'

1.3 Given two strings,write a method to decide if one is a permutation of the other.
"""

def is_str_same_permu(str1,str2): # wrong
    """
    using set as two hash table,wrong method
    for instance: "aaab","bba",return true
    """
    return set(str1) == set(str2)


def is_str_same_permu2(str1,str2): # right
    """
    using sorted() and then compare
    complexity O(nlogn)
    """
    return sorted(str1) == sorted(str2)

def is_str_same_permu2(str1,str2): # wrong
    """
    using dict to implement hash table
    using two hash table for good reason, space exchange for time.
    and good to maintain. easy to understand.
    O(n)
    """
    dic1={}
    for char1 in str1:
        dic1[char1] = dic1.get(char1,0)+1
    dic2={}
    for char2 in str2:
        dic2[char2] = dic2.get(char2,0)+1

    return dic1 == dic2

def anagram(s1,s2):
    """
    counting chars in two strings, assume ascII encoding, and need a array of size 256, if unicode, array size of 611111
    this is trading space for time, comparing to the sorting method, the sorting method take O(1) space, though O(nlogn)time
    """
    pass





print is_str_same_permu2("fdass","fdass")

print isPermutationHash("afsd","asss")