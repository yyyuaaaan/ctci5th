"""

__author__ = 'anyu'

Assume you have a method isSubstring which checks if one word is asubstring
of another. Given two strings, si and s2, write code to check Ifs2 isa rotation
 of si using only onecalltoisSubstring (e.g., "waterbottLe" is a rotation of "erbot- tLewat").
"""

def strrotation(s1,s2):
    if len(s1) !=len(s2):
        return False
    stemp= s1+s2
    return isSubstring(s2,stemp)

def isSubstring(sub1,sub2):
    """
    check if sub1 is in sub2
    """
    if len(sub1) > len(sub2):
        return False
    return sub2.find(sub1)  > -1

print strrotation("waterbottle", "erbottLewat")