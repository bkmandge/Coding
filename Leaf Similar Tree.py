"""
                        Leaf Similar Tree

Leaf nodes' sequence in both binary trees must be same from left to right.


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

"""


def leafSimilar(root1, root2):
    def dfs(root, leaf):
        if not root:
            return

        # if root has no left and right child add root's value as leaf node in leaf array
        if not root.left and not root.right:
            leaf.append(root.val)
            return

        # recursively call dfs for left and right subtree
        dfs(root.left, leaf)
        dfs(root.right, leaf)

    # to store leaf node's of both binary trees
    leaf1 = []
    leaf2 = []

    # call dfs() on root1 and root2 and store their leaf nodes in leaf1 and leaf2 arrays
    dfs(root1, leaf1)
    dfs(root2, leaf2)

    # check if both leaf arrays are same, if yes return true
    return leaf1 == leaf2
