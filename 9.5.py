"""__author__ = 'anyu'
9.5 Write a method to compute all permutations of a string
This solution takes 0(n !) time, since there are n! permutations. We cannot do better than this.
"""

def permurecursive(s):
    if len(s)<=1: return [s]
    result =[]
    for perm in permurecursive(s[1:]):
        result += [perm[:i]+s[0:1]+perm[i:] for i in range(len(perm)+1) ] #must be s[0:1] to allow list AND string
                                 #s=[2,3,4] s[3] is err, s[3:]=[], s[:3] == [2,3,4]
    return result


def permuiter(s):
    if len(s)<=1: yield s
    else:   # must have else, or will trouble, python's problem! when use yield generator, do not forget else!
        for perm in permuiter(s[1:]):
            for i in range(len(perm)+1):
                yield perm[:i]+s[0:1]+perm[i:] #nb s[0:1] works in both string and list contexts


def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    result = []  # here is new list with all permutations! #  here the res definition is ok, because res do not need to be recursive
    for i in range(len(l)):
        s = l[:i] + l[i+1:]
        result += [ [l[i:i+1]] + x for x in perm(s)]
    return result

def permutList(l):
    """
    only for list, if string, use another fuction to call this function, and use list("sdfaf") to convert string to chars
    """
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res+=[[e] + r for r in permutList(temp)]
    return res

print permurecursive("abc")
for x in permuiter("abc"):print x
