"""__author__ = 'anyu'
h
Design an algorithm and write code to find the first common ancestor of
 two nodes in a binary tree. Avoid storing additional nodes in a data structure.
 NOTE: This is not necessarily a binary search tree.

 Avoid storing additional nodes in a data structure.???  meaning not in Node??

 If this were a binary search tree,we could modify the find operation for the two nodes
 and see where the paths diverge. Unfortunately, this is not a binary search tree, so we must
 try other approaches.

 1,hashtable
 2,iteratively do n1's parent, until find the common, or root
 3,post order traversal!!! and push into stack! topological sort, (1)one stack, still have to do every node
                                                                  (2)two stack from n1 and n2, when you pop out the first common node!
                                                                  bingo! complex!
 4,if no parent pointer: from root, do recursion.


"""

class Node(object):
    def __init__(self):
        self.data= None
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.data)
def commonancester(n1, n2, tree):
    if tree.data == None:
        return "no nodes in tree"
    if n1 is n2:      # must not n1 == n2
        return n1.parent
    hashtable=set()

    p1 = n1.parent
    while p1 is not None:
        hashtable.add(p1)
        p1 = p1.parent

    p2 = n2.parent
    while p2 is not None:
        if p2 in hashtable:
            return p2
        p2 = p2.parent
    else:
        return "no common parent"



def commonancester2(n1, n2, tree): # no hash data structure, then iteratively try only n1's parent, exponential time?
    if n1 is None or n2 is None: return "no comm"

    p1 = n1.parent
    while p1 is not None:
        if isancestor(n2,p1): return p1
        p1=p1.parent

def isancestor(s2,tree):
    """
    check if tree is s2's ancestor
    """
    if tree is s2: return True
    if tree is None: return False
    else:
        return isancestor(s2, tree.left) or isancestor(s2, tree.right)


def commonAncestor3_helper(n1, n2, tree): # no parent pointer, hard! and complex!
    """Alternatively, you could follow a chain in which p and q are on the same side.
    That is, if p and q are both on the left of the node, branch left to look for the common
    ancestor. If they are both on the right, branch right to look for the common ancestor.
    When p and q are no longer on the same side, you must have found the first common ancestor.

    This algorithm runs in O(n)time on a balanced tree.
    """
    # when do this recursion, we keep track fo two things, isancester? and node to return, a smart technique!
    # no! [True, tree] is not smart ,it is stupid, making things complex

    if tree is None: return None
    if tree is n1 or tree is n2: return tree  # this line can be omited, need to double check
    if isancestor(n1,tree.left) and isancestor(n2, tree.right)\
        or isancestor(n1, tree.right) and isancestor(n2, tree.left)
        return tree

    if isancestor(n1,tree.left):
        return commonAncestor3_helper(n1, n2, tree.left)
    else:
        return commonAncestor3_helper(n1, n2, tree.right)
