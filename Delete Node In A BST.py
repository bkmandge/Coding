"""
                             Delete Node in a BST

"""


def delete_nodeBST(root, key):
    if not root:
        return

    # find the key matching node in BST
    if key > root.val:
        root.right = delete_nodeBST(root.right, key)
    elif key < root.val:
        root.left = delete_nodeBST(root.left, key)
    else:  # if key == root, then assign new value at root & delete root at the end
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # find the min from right subtree
        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val  # assigning new value to root node
        root.right = delete_nodeBST(root.right, cur.val)  # delete that duplicate node from bottom

    return root

