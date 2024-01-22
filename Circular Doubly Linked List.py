class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
            if currNode == self.head:
                break

    def __str__(self):
        values = [str(node.value) for node in self]
        return '<->'.join(values)

    def create_cdll(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.head = newNode
        self.tail.next = newNode
        self.length += 1
        return self

    def append(self, value):
        newNode = Node(value)
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def insert_node(self, index, value):
        newNode = Node(value)
        currNode = self.head
        for _ in range(index - 1):
            currNode = currNode.next
        newNode.next = currNode.next
        newNode.prev = currNode
        currNode.next = newNode
        newNode.next.prev = newNode
        self.length += 1
        return self

    def search_node(self, value):
        currNode = self.head
        while currNode:
            if currNode.value == value:
                return "Found!"
            currNode = currNode.next
            if currNode == self.head:
                break
        return "No such node in CDLL!"

    def get_index(self, value):
        currNode = self.head
        index = 0
        while currNode:
            if currNode.value == value:
                return index
            currNode = currNode.next
            index += 1
            if currNode == self.head:
                break
        return "No such node in CDLL"

    def get_value(self, index):
        if index >= self.length:
            return f"Enter valid index from 0 to {self.length - 1}"
        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
            if currNode == self.head:
                break
        return currNode

    def traverse(self):
        if self.length == 0:
            return "CDLL does not exist!"

        currNode = self.head
        while currNode:
            print(currNode.value)
            currNode = currNode.next
            if currNode == self.head:
                break

    def reverse_traverse(self):
        if self.length == 0:
            return "CDLL does not exist!"

        currNode = self.tail
        while currNode:
            print(currNode.value)
            currNode = currNode.prev
            if currNode == self.tail:
                break

    def pop_first(self):
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1
        return self

    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length -= 1
        return self

    def remove(self, index):
        if index == 0:
            self.pop_first()
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            currNode.next = currNode.next.next
            currNode.next.prev = currNode
        self.length -= 1
        return self

    def delete_cdll(self):
        currNode = self.head
        while currNode:
            currNode.next = None
            currNode.prev = None
            currNode = currNode.next
            if currNode == self.head:
                break
        self.head = None
        self.tail = None
        self.length = 0
        return "Deleted CDLL"


cdll = CircularDoublyLL()
print(cdll.create_cdll(10))
print(cdll.prepend(100))
print(cdll.append(20))
print(cdll.prepend(0))
print(cdll.insert_node(2, 2))

# print(cdll.search_node(200))
# print(cdll.get_index(100))
# print(cdll.get_value(5))
# cdll.traverse()
# cdll.reverse_traverse()

# print(cdll.pop_first())
# print(cdll.pop())
# print(cdll.remove(0))
# print(cdll.delete_cdll())
# print(cdll.traverse())