"""
                    Longest ZigZag Path in a Binary Tree

Zigzag:- Choose any node in the binary tree and a direction (right or left).

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

"""


def longest_zigzag(root):
    # If we are at left node go to right node & add depth + 1, else start again from next left node, set depth back to 0
    # else if we are at right node go to left node & add depth + 1, else start again from next right node, set depth back to 0
    # at the end return depth

    def dfs(root, is_left, depth):
        if is_left:
            depth = max(depth, dfs(root.right, False, depth+1), dfs(root.left, True, 0))
        else:
            depth = max(depth, dfs(root.left, False, depth + 1), dfs(root.right, True, 0 ))

        return depth

    return max(dfs(root.left, True, 0), dfs(root.right, False, 0))



