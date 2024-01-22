# 1 -> :- False
# 1 -> 2 -> 3 -> 2 :- True



def detect_cycle(head):
    slow, fast = head

    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
