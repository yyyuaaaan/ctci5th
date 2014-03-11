"""__author__ = 'anyu'
9.4 Write a method to return all subsets of a set.

gives us 2" subsets.We will therefore not be able to do better than 0(2") in time or space complexity.
The subsets of {a^ a2, ..., an} are also called the powerset, P({aj, a2, ..., an}),orjustP(n).
This solution will be 0(2n) in time and space, which is the best we can do. For a slight optimization,
we could also implement this algorithm iteratively.

Generating P(n) for the general case is just a simple generalization of the above steps.
We compute P(n-l), clone the results,and then add an to each of these cloned sets.
How can we use P ( 2 ) to create P( 3 ) ? We can simply clone the subsets in P ( 2 ) and add a3 to them:
P(2) ={} , {aj, {aj, {9lJ a2}
P(2) + a3 = {a3}, {at, aj, {a2, a3}, {aaJ a2, a3}
When merged together, the lines above make P(3).
"""

""" so esoteric
def powersets(listset,index):

    result=[]
    if len(listset) is index:
        result.append([])
    else:
        result=powersets(listset,index+1)
        item=listset[index]

    if len(listset) is 1: result.append([]); result.append([listset])

    for x in powersets(listset,index-1):
        result.append(x+listset[index])
"""

def powerset(myset):
    result = [[]]
    for element in myset:
        result += [subset + [element] for subset in result] # result.extend() also ok
    return result


def powerset2(l):
    if len(l) is 0  : return [[]] #l is [] wrong, but (not l) is ok
    return powerset2(l[1:]) + [[l[0]] + subset for subset in powerset2(l[1:])] # + and append() is very different


print powerset(['a','b','c','d'])
print powerset2(['a','b','c','d'])



