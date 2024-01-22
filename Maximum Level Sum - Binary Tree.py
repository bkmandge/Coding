"""
                        Maximum Level Sum - Binary Tree

Calculate sum of each level & return level which has maximum sum.
If two levels have same sum return earlier level.

"""


def maxLevelSum(root):
    if not root: return 0

    # initialise queue with root
    q = [root]
    max_level = 1
    current_level = 1
    max_sum = float("-inf")

    while q:
        # initialise level sum to 0
        # next_level_children [] to append if node has any left or right children
        level_sum = 0
        next_level = []

        # traverse q, add sum
        for node in q:
            level_sum += node.val

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = current_level

        q = next_level
        current_level += 1
    return max_level