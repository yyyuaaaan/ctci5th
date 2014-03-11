"""__author__ = 'anyu'

Implement a function to check if a tree is balanced.
For the purposes of this question, a balanced tree is defined
to be a tree such that the heights of the two subtrees of any     # this is so called AVL-tree
node never differ by more than one.

4th edi of the book: not the formal definition of balanced tree, it is the deepest node - shallowest node

int d = 0, num = 0, dep[maxn];  #this non-recursive data structure have to be defined out side of the function:
void getDepth(Node *head){
    if(head == NULL) return;
    ++d;                          # before traverse left, depth+=1
    getDepth(head->lchild);
    if(head->lchild == NULL && head->rchild == NULL)
        dep[num++] = d;
    getDepth(head->rchild);
    --d;                          # after traverse left, depth-=1
}
then compute the (max-min) of dep[]

 d=0; dict=[{head:depth}]
void getdepth(Node *head)
    if (head == Null) return
    d += 1
    getdepth(head.left)
    if(head.left==Null)&& head.right==Null
        dict.append({head:d})
    getdepth(head.right)
    d -=1
"""

class Node(object):
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

    def __str__(self):
        return "data:"+str(self.data)+"("+str(self.left)+"|"+str(self.right)+")"+"depth:"+str(self.depth)

#O(n^2) naive algorithm
def height(tree):
    if tree.left==None and tree.right==None:
        return 0
    return max(height(tree.left),height(tree.right))+1

def isbalanced(tree):
    if tree.left==None and tree.right==None:
        return True
    else:
        return abs(height(tree.left)- height(tree.right)) <=1 and\
            isbalanced(tree.left) and isbalanced(tree.right)    # this must be checked
#On each node, we recurse through its entire subtree.
# This means that getHeight is called repeatedly on the same nodes.
# The algorithm is therefore O(N2).
#effcient algorithm, get heights of subtrees and check subtrees if balanced at the same time O(N)

# similar to DFS, post-order traversal

def isbalanced3(tree, height=0):
    if tree.left==None and tree.right==None:
        return [True,0]

    if tree.left is not None:
        [isleftbalanced, leftheight] = isbalanced(tree.left,height+1)

    if tree.right is not None:
        [isrightbalanced, rightheight] = isbalanced(tree.right,height+1)

    if isleftbalanced is True and isrightbalanced is True:
        return abs(leftheight-rightheight)<=1



