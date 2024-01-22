"""
                    Count Good Nodes in Binary Tree

root = [3, 3, null, 4, 2]
o/p = 3

root = [1]
o/p = 1
"""


def goodNodes(root):
    # pass current node i.e. root in dfs & max value so far in the traversing path from root to left and right nodes
    def dfs(root, maxVal):
        if not root:
            return 0

        # add 1 to count if found current node's value >= maxValue & update maxValue accordingly
        count = 1 if root.val >= maxVal else 0
        maxVal = max(maxVal, root.val)

        # recursive call to left and right subtrees
        count += dfs(root.left, maxVal)
        count += dfs(root.right, maxVal)
        return count

    # pass root's value to compute next max value nodes
    return dfs(root, root.val)

