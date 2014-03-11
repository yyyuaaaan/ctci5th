"""

__author__ = 'anyu'

Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.

map addr to hash table
以地址为哈希表的键值，每出现一个地址，就将该键值对应的实值置为true。
那么当某个键值对应的实值已经为true时，说明这个地址之前已经出现过了， 直接返回它就OK了。

python do not support address or linkedlist

"""

class Node(object):
    def __init__(self,data=None):
        self.data=data
        self.next=None

def iscircular(linkedlist):
    #treat list index as pointer in c++, also as address

    p=linkedlist
    if p is None: return "null"
    hashlist=[]
    hashlist.append(p)
    while p.next != None:
        p=p.next
        if hash(p) not in hashlist:
            hashlist.append(hash(p))
        elif:
            hash(p) in hashlist:
            return True
    return False

