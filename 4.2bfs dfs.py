"""__author__ = 'anyu'

4.2 Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.

It may be worth discussing with your interviewer the trade-offs between breadth first search and depth
first search for this and other problems. For example, depth first search is a bit simpler to implement
since it can be done with simple recursion. Breadth first search can also be useful to find the shortest path,
whereas depth first search may traverse one adjacent node very deeply before ever going onto the immediate neighbors.
"""

from collections import deque

class Node(object):
    def __init__(self,data):
        self.data=data
        self.neighbours=[]
    def __str__(self):
        return str(self.data)

# if need to output route, can maintain a parent set outside the hasroute function
# parent = dict(), set() not gonna work, because we need to keep the parent node's address,
# dict can keep address in key/value pairs as value
# parent.update(n1,None)) (x,y),then output the as a linkedlist to indicate the route
#if (str(hash(node1)) + "," + str(hash(node2))) in cache2:
#        return cache2[(str(hash(node1)) + "," + str(hash(node2)))]
def hasroute(n1,n2):
    """
    find route from n1 to n2 ;
    BFS
    """
    frontier = deque(n1) # enque, to the right side of the queue list, frontier as visiting set, as queue
    visited=set(n1)    # because you wanna find route, first node is set to visited ! also,visited include frontier. remember!

    while frontier !=[]:
        ntemp=frontier.pop()
        if ntemp == n2: return True   # we can use : if ntemp is n2

        for neighbour in ntemp.neighbours:
            if (neighbour not in frontier) and (neighbour not in visited):
                frontier.append(neighbour)
                visited.add(neighbour)
    return False


def hasroute2(n1,n2,visited = set(n1)):
    """
    dfs
    visited=set()    to avoid loop, if recursive dfs, visited set should be put outside or in the parameter
    """
    for neighbour in n1.neighbours:
        if neighbour not in visited:
            visited.add(neighbour)
            if neighbour == n2: return True
            hasroute2(neighbour, n2, visited)     # implicitly using stack
    return False


