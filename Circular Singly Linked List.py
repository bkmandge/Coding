class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CircularSinglyLL:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0
        newNode = Node(value)
        self.head = newNode         # head -> 10 <- tail
        self.tail = newNode
        newNode.next = newNode

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            if currNode == self.head:
                break

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'.join(values)

    def insert_node(self, index, value):
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif index == -1:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            newNode.next = currNode.next
            currNode.next = newNode
        self.length += 1

    def traverse(self):
        if self.head is None:
            return "CSLL does not exist!"
        else:
            currNode = self.head
            while currNode:
                print(currNode.value)
                currNode = currNode.next
                if currNode == self.head:
                    break

    def search_node(self, target):
        if self.head is None:
            return "SLL does not exist!"
        else:
            currNode = self.head
            while currNode:
                if currNode.value == target:
                    return currNode.value
                currNode = currNode.next
                if currNode == self.head:
                    break
            return "No such node value in CSLL."

    def get_value(self, index):
        if self.length == 0:
            return "CSLL does not exist!"
        if index < 0 or index > self.length:
            return f"Enter index from 0 to {self.length}!"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
                if currNode == self.head:
                    break
            return currNode

    def set_value(self, index, value):
        if self.length == 0:
            return "CSLL does not exist!"
        if index < 0 or index > self.length:
            return f"Enter index from 0 to {self.length}!"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
                if currNode == self.head:
                    break
            currNode.value = value
            return self

    def get_index(self, value):
        if self.length == 0:
            return "CSLL does not exist!"
        else:
            index = 0
            currNode = self.head
            while currNode:
                if currNode.value == value:
                    return index
                else:
                    currNode = currNode.next
                    index += 1
                    if currNode == self.head:
                        break
            return "No such value in CSLL!"

    def delete_node(self, index):
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif index == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                curNode = self.head
                while curNode:
                    curNode = curNode.next
                    if curNode.next == self.tail:
                        break
                curNode.next = self.head
                self.tail = curNode
        else:
            curNode = self.head
            for _ in range(index - 1):
                curNode = curNode.next
            curNode.next = curNode.next.next
        self.length -= 1
        return self

    def delete_csll(self):
        if self.head == self.tail:
            self.head.next = None
            self.head = None
            self.tail = None
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
        return "Deleted CSLL successfully!"


csll = CircularSinglyLL(10)
# print(csll)
csll.insert_node(0, 0)  # inserting at first index
# print(csll)
csll.insert_node(-1, 100)  # inserting at last index
csll.insert_node(-1, 200)
csll.insert_node(-1, 300)
print(csll)
# csll.insert_node(3, 3)
# print(csll)

# csll.traverse()  # traversal CSLL

# print(csll.search_node(50))  # searching a node value

# print(csll.get_index(10))  # finding index of given node value

# print(csll.get_value(5))

# print(csll.set_value(2, 20))

# print(csll.get_index(10))

# print(csll.delete_node(0))  # Deleting first node
# print(csll.delete_node(-1))  # Deleting last node
# print(csll.delete_node(2))  # Deleting second node

# print(csll.delete_csll())  # Deleting CSLL
# print(csll.traverse())