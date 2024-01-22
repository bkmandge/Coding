# Doubly Linked List Implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def create_dll(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        self.length += 1

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return '<->'.join(values)

    def insert_node(self, index, value):
        newNode = Node(value)
        if index == 0:
            if self.head is None:
                newNode.prev = None
                newNode.next = None
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                newNode.prev = None
                self.head = newNode
                newNode.next.prev = newNode
        elif index == -1:
            if not self.head:
                newNode.prev = None
                newNode.next = None
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            newNode.prev = currNode
            newNode.next = currNode.next
            currNode.next = newNode
            currNode.next.next.prev = newNode
        self.length += 1

    def traverse(self):
        if self.head is None:
            return "DLL does not exist!"
        currNode = self.head
        while currNode:
            print(currNode.value)
            currNode = currNode.next

    def reverse_traverse(self):
        currNode = self.tail
        while currNode:
            print(currNode.value)
            currNode = currNode.prev

    def get_value(self, index):
        if self.head is None:
            return "DLL does not exist!"
        elif index < 0 or index >= self.length:
            return f"Enter valid index from 0 to {self.length}"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            return currNode.value

    def get_index(self, value):
        if self.head is None:
            return "DLL does not exist!"
        index = 0
        currNode = self.head
        while currNode:
            if currNode.value == value:
                return index
            currNode = currNode.next
            index += 1
        return -1

    def set_value(self, index, value):
        if self.length == 0:
            return "DLL does not exist!"

        if index < 0 or index > self.length:
            return f"Enter index 0 to {self.length} only!"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            currNode.value = value
            return self

    def search_node(self, value):
        if self.head is None:
            return "DLL does not exist!"
        else:
            currNode = self.head
            while currNode:
                if currNode.value == value:
                    return "Found!"
                currNode = currNode.next
            return "No such node value in DLL!"

    def delete_node(self, index):
        if self.head is None:
            return "DLL does not exist!"

        if index < 0 or index >= self.length:
            return f"Enter a valid index from 0 to {self.length - 1}"

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            if currNode.next == self.tail:
                currNode.next = None
                self.tail = currNode
            else:
                currNode.next = currNode.next.next
                currNode.next.prev = currNode

        self.length -= 1
        return self

    def delete_dll(self):
        if self.head is None:
            return "DLL does not exist!"

        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.prev = None
            temp.next = None

        self.tail = None
        self.length = 0

        return "Deleted DLL!"


dll = DoublyLL()
dll.insert_node(0, 10)
dll.insert_node(-1, 20)
dll.insert_node(-1, 30)
dll.insert_node(-1, 40)
# print(dll)
dll.insert_node(0, 0)
print(dll)

# print(dll.get_index(40))

# print(dll.get_value())

# print(dll.set_value(4, 5))
# print(dll.search_node(10))

# print(dll.delete_dll())
# print(dll.traverse())

print(dll.delete_node(5))


