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

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def insert(self, index, value):
        newNode = Node(value)
        if index < 0:
            return None
        if index == 0:
            self.prepend(newNode)
        if index == -1:
            self.append(newNode)
        else:
            currNode = self.head
            for _ in range(index - 1):
                if currNode is None:
                    return currNode
                currNode = currNode.next
            newNode.next = currNode.next
            currNode.next = newNode
            self.length += 1

    def traverse(self):
        currNode = self.head
        while currNode:
            print(currNode.value)
            currNode = currNode.next

    def search_node(self, target):
        if self.head is None:
            return "SLL does not exist!"
        currNode = self.head
        while currNode:
            if currNode.value == target:
                return currNode.value
            currNode = currNode.next
        return "No such node in SLL!"

    def get_index_value(self, index):
        if self.length == 0:
            return "SLL does not exist!"
        if index < 0 or index > self.length:
            return f"Enter index above 0 and below {self.length}!"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            return currNode.value

    def get_index(self, value):
        if self.head is None:
            return "SLL does not exist!"
        else:
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
            return "SLL does not exist!"
        if index < 0 or index > self.length:
            return f"Enter index between 0 and {self.length}!"
        else:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            currNode.value = value
            return self

    def delete_node(self, index):
        if self.head is None:
            return "LL does not exist!"

        if index < 0 or index >= self.length:
            return f"Enter a valid index from 0 to {self.length - 1}"

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == self.length - 1:
            currNode = self.head
            while currNode.next is not self.tail:
                currNode = currNode.next
            self.tail = currNode
            currNode.next = None
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            currNode.next = currNode.next.next
        self.length -= 1
        return self

    def delete_ll(self):
        self.head = None
        self.tail = None
        print("Deleted ll")


ll = LinkedList()
ll.append(10)
ll.append(20)
# print(ll)  # append
ll.prepend(1)
# print(ll)  # prepend
ll.insert(2, 2)
print(ll)  # insert
# print(ll.insert(-1, 100))

# print(ll.search_node(30))

# ll.traverse()  # traverse

print(ll.delete_node(5))
# ll.delete_node(1)
# ll.delete_node(-1)
# ll.delete_ll()  # delete ll

# print(ll.get_index_value(3))

# print(ll.set_value(3, 100))
# print(ll.get_index(10))