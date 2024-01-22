"""
                    Maximum Twin Sum of a Linked List
"""


def maxPairSum(head):
    if not head:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        # reverse first half of list by finding middle node
        fast = fast.next.next
        temp = slow.next
        slow.next = prev  # 1st iteration:- slow.next = None
        prev = slow
        slow = temp  # slow points to next half's first node

    res = 0
    while slow:
        res = max(res, prev.val + slow.val)
        prev = prev.next
        slow = slow.next

    return res

