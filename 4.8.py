"""
You have two very large binary trees: T1, with millions of nodes,
and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1
That is, if you cut off the tree at node n, the two trees would be identical.

note: tree mactching can be identical to string matching, 2 solutions, trade off between time and space
      string solution take more space and less time; tree recursion solution more time,less space

note: create algo, not code,! some questions are just design, do not need to code completely
the string matching solution is still wrong , only a binary search tree will be right.
what if we have to check both in-order strings and pre-order strings

another approach be ctti 5th: (i think it may be wrong)
In this smaller, simpler problem, we could create a string representing the in-order and pre-order traversals.
If T2's pre-order traversal is a substring of T l's pre-order traversal, and T2'sin-order traversalisa substring
of Tl's in-order traversal,then T2 isa subtree of Tl.
Substrings can be checked with suffix trees in linear time, so this algorithm is relatively
efficient in terms of the worst case time.

add '(' ')', and then do not need to two times traversal
"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=Non

    def __str__(self):
        return str(self.data)

def inorderdfs(tree, slist=['(']):
    """
    return two list
    """
    if tree is None: return slist.append([')'])  # must have '(', else list and tree can NOT be one to one correspondence!
    inorderdfs(tree.left,slist)
    slist.append(tree.data)   # hash the tree address or data hash(tree.data)
    inorderdfs(tree.right,slist)

def treemathing(t1,t2):
    """
    check if t2 is subtree of t1
    """
    l1 = []
    l1 = inorderdfs(tree,l1)
    l2 = []
    l2 = inorderdfs(tree, l2)

    n = len(l1)
    m = len(l2)

    # for char1 in l1[:n-m]: wrong and copy list
    for i in range(n-m):
        if l1[i:i+m] = l2:
            return True

    return False


def treemathing2(t1,t2):  # not match, but directly checking if t2 is subtree of t1
    """
    this is alternative solution,simple solution is the one above
    Analyzing the runtime is somewhat complex. A naive answer would be to say that it is 0(nm) time,
    wherenisthenumberofnodesinTlandmisthenumberofnodesinT2.
    When might the simple solution be better, and when might the alternative approach be better?
    This is a great conversation to have with your interviewer
    The simple solution takes 0(n + m) memory. The alternative solution takes 0(log(n) + log(m)) memory.
    The simple solution is 0(n + m) time and the alternative solution has a worst case time of 0(nm).
    """
    if t1 is None and t2 is None: return True
    if t1 is not None and t2 is None : return True
    if t1.data == t2.data:
        return treemathing2(t1.left, t2.left) and treemathing2(t1.right, t2.right) or\
            treemathing2(t1.right, t2.left) and treemathing2(t1.left, t2.right)   # be careful, not bSEARCHtt,
                                                                                 # so have to have the second check
                                                                                 # the second depends on how you define identical



"""
bool match(Node* r1, Node* r2){
    if(r1 == NULL && r2 == NULL) return true;
    else if(r1 == NULL || r2 == NULL) return false;
    else if(r1->key != r2->key) return false;
    else return match(r1->lchild, r2->lchild) && match(r1->rchild, r2->rchild);
}
bool subtree(Node* r1, Node* r2){
    if(r1 == NULL) return false;
    else if(r1->key == r2->key){
        if(match(r1, r2)) return true;
    }
    else return subtree(r1->lchild, r2) || subtree(r1->rchild, r2);
}
bool contain_tree(Node* r1, Node* r2){
    if(r2 == NULL) return true;
    else return subtree(r1, r2);
"""