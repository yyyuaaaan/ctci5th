"""__author__ = 'anyu'
Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

tweak the bfs
>>> frontierset = []
>>> frontierset.append(deque())
>>> frontierset
[deque([])]
>>> frontierset.append([])
>>> frontierset.append({})
>>> frontierset
[deque([]), [], {}]

"""
from collections import deque

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
# visited = set() # visited binary tree DO NOT need visited set, because must not have loop
# O(N) time and space, bfs

def bfs_to_list(tree):   # here tree parameter is just another node,recursively defined, as an pointer
    if tree is None:
        return [[]]

    result = [[tree]]
    queue = [tree]

    while len(queue) >0:
        nextlevelqueue = [] #go to next level
        for node in queue:
            if node.left is not None: nextlevelqueue.append(node.left)
            if node.right is not None: nextlevelqueue.append(node.right)
        queue = nextlevelqueue
        if len(nextlevelqueue) is 0:
            break
        result.append(queue) # or: result.append([node for node in queue]),this is hardcopy:
"""
>>> s=[2,3]
>>> d=[1,4]
>>> s.append(d)
>>> s
[2, 3, [1, 4]]
>>> d
[1, 4]

"""
