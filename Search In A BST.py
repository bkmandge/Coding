"""
                        Search in a Binary Search Tree

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []
"""


def searchBST(root, val):
    currNode = root

    while currNode:
        if currNode.val == val:
            return currNode
        elif currNode.val > val:
            currNode = currNode.left
        else:
            currNode = currNode.right
    return currNode
