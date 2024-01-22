class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rightSideView(root):
    def right_view(root, level, result):
        if not root:
            return

        if level > len(result):
            result.append(root.val)

        right_view(root.right, level + 1, result)
        right_view(root.left, level + 1, result)

    result = []
    right_view(root, 1, result)
    return result



# another way


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def right_view(root, level, max_level):
#     if root is not None:
#         if max_level[0] < level:
#             print(root.data)
#             max_level[0] = level
#
#         right_view(root.right, level + 1, max_level)
#         right_view(root.left, level + 1, max_level)


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.right.left = Node('d')
root.right.right = Node('e')
root.right.left.left = Node('f')
root.right.right.right = Node('g')


# max_level = [0]
# right_view(root, 1, max_level)

print(rightSideView(root))