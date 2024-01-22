"""
                    Delete the Middle Node of a Linked List
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]


Input: head = [2,1]
Output: [2]
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_middle_node(head):
    # if list is empty or has only one node
    if not head or not head.next:
        return

    slow = head
    fast = head
    prev = None

    # finding middle node
    while fast and fast.next:
        # to store middle node's previous node
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # pointing to next node, so automatically deletes middle node
    if prev:
        prev.next = slow.next
    else:
        # if head is middle, update head
        head = slow.next
    return head


# creating nodes, printing them and calling delete_middle_node()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original linked list ")
current_node = head
while current_node:
    print(current_node.value, end="->")
    current_node = current_node.next

print()

print("Linked list after deleting middle node ")
delete_middle_node(head)

current_node = head
while current_node:
    print(current_node.value, end="->")
    current_node = current_node.next
