"""
                     Path Sum III
Return numbers of paths whose sum is equals to target_sum.
Path may include root node or can exclude it.

"""


def pathSum(root, target_sum):
    def dfs(root, target_sum):
        if not root:
            return 0

        # initial path count
        path_count = 0

        if root.val == target_sum:
            path_count += 1

        # counting paths from left and right subtrees excluding root node & returning count
        path_count += dfs(root.left, target_sum - root.val)
        path_count += dfs(root.right, target_sum - root.val)

        return path_count

    if not root:
        return 0
    else:
        # counting paths from left and right subtrees including root node & returning count
        return pathSum(root.left, target_sum) + dfs(root, target_sum) + pathSum(root.right, target_sum)



    if not root: return 0
    return