"""__author__ = 'anyu'
4.5 Implemen t a function to check if a binary tree is a binary search tree.
Our first thought might be to do an in-order traversal, copy the elements to an array,
and then check to see if the array is sorted.This solution takes up a bit of extra memory, but it works mostly.
The only problem is that it can't handle duplicate values in the tree properly. For
example, the algorithm cannot distinguish between the two trees below (one of which
is invalid)sincethey havethe same in-order traversal.
However, if we assume that the tree cannot have duplicatevalues,then this approach works

"""
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

def is_bst_by_dfs(tree):
    if tree is None: return True

    if  tree.left.data <= tree.data < tree.right.data:
        return is_bst_by_dfs(tree.right) and is_bst_by_dfs(tree.left)
    else:
        return False

def is_bst_by_dfs(tree):
    if tree.left is None and tree.right is None: return True

    if tree.right is not None:
        return tree.data <tree.right.data and is_bst_by_dfs(tree.right)
    if tree.left is not None:
        return tree.data >= tree.left.data and is_bst_by_dfs(tree.left)

    if  tree.left.data <= tree.data < tree.right.data:
        return is_bst_by_dfs(tree.right) and is_bst_by_dfs(tree.left)
    else:
        return False





"""
def make_random_btree(depth = 3):
	if depth < 0: return None
	tree = BinaryTree(randrange(10))
	tree.left = make_random_btree(depth - 1)
	tree.right = make_random_btree(depth - 1)
	return tree

def valid_bsearch_tree2(btree):
	#in-order method
	l = in_order_search(btree)
	if sorted(l) == l:
		return True
	return False

def in_order_search(btree):
	if btree is None: return []    #  here the "tree is None" make things concise and simple!!!!!!!!!!!!
	return in_order_search(btree.left) + [btree.content] + in_order_search(btree.right)


	"""