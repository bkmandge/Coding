
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return '->'.join(values)

    def prepend(self, value, index):
        self.length += 1
        pass

    def append(self, index, value):
        self.length += 1
        pass

    def insert(self, index, value):
        self.length += 1
        pass

    def traverse(self):
        currNode = self.head
        while currNode:
            print(currNode.value)
            currNode = currNode.next

    def get_Node(self, index):
        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
        return currNode

    def set_newValue(self, index, value):
        pass

    def pop_node(self):
        pass

    def pop_firstNode(self):
        pass

    def remove_node(self, index):
        pass

    def delete_linkedList(self):
        pass