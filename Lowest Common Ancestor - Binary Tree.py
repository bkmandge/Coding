"""
                            Lowest Common Ancestor - Binary Tree

We allow a node to be a descendant of itself).”

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [1,2], p = 1, q = 2
Output: 1

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""


# Recursive way

def lca(root, p, q):
    if not root:
        return None

    if p.val == root.val or q.val == root.val:
        return root

    left_lca = lca(root.left, p, q)
    right_lca = lca(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


# Iterative way
def lowestCommonAncestor(root, p, q):  #p -> node1, q -> node2
    # assign root node to curr variable
    curr = root

    # traverse until end of tree
    # check if p and q values are greater than current root node value then search in right subtree,
    # else if search in left subtree
    # if not fount in either of subtrees then it must be root node, so return it.
    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr

