"""
                                Reverse given linked lists
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = []
Output: []

"""


def reverse_list(head):
    # if empty list is given, then return same empty list
    if not head:
        return

    # 3 pointers needed prev, current, next_node to reverse pointers
    prev = None  # pointer before first node
    current = head  # pointer for first node
    while current:
        next_node = current.next  # pointer to second node
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head
