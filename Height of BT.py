"""
                    Height of Binary Tree
-> calculating edges from Root to Deepest node (last node)

Height = 1 + no. of edges from root to the deepest node
         1:- for including root node
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def heightOfTree(rootnode):
    if not rootnode:
        return 0
    else:
        lDepth = heightOfTree(rootnode.leftchild)
        rDepth = heightOfTree(rootnode.rightchild)

        if lDepth > rDepth:
            return 1 + lDepth
        else:
            return 1 + rDepth


new_BT = TreeNode(1)
new_BT.leftchild = TreeNode(2)
new_BT.rightchild = TreeNode(3)
new_BT.leftchild.leftchild = TreeNode(4)
new_BT.leftchild.rightchild = TreeNode(5)
new_BT.leftchild.leftchild.leftchild = TreeNode(7)
new_BT.rightchild.rightchild = TreeNode(6)

print(heightOfTree(new_BT))
