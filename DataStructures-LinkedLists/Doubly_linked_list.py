# Create the below linked list: (Javascript)
# myLinkedList = {"head": {"value": 10, "next": {"value": 5, "next": {"value": 16, "next": None}}}}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    # diff
    def append(self, data):

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head  # current is the current pointer.
        while current.next:
            current = current.next  # goto the last node.
        current.next = new_node
        new_node.prev = current

    # diff
    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        current.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traversetoindex(self, position):
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        return current  # get the position data.

    # diff
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.prepend(data)

        current = self.traversetoindex(position)
        if current is None:
            print("Out of range.")
            return
        # if ok insert
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node

    # diff
    def remove(self, position):
        # if linkedlist is empty.
        if not self.head:
            return
        # if the position is 0
        if position == 0:
            self.head = self.head.next
            return

        current = self.traversetoindex(position)
        if current is None:
            print("Out of range.")
            return
        # if ok remove
        current.next = current.next.next
        current.next.prev = current

    def reverse(self):
        current = self.head
        # this is my first wrong answer,why.
        # while current.next:
        #     new_current = current.next
        #     new_current.next = current
        #     current = current.next
        # current = new_current

        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        # Need the prev to keep some info,otherwise we will lose some.


mylinkedlist = DoublyLinkedList()
mylinkedlist.append(5)
mylinkedlist.prepend(7)
mylinkedlist.prepend(8)
mylinkedlist.traversetoindex(2)
mylinkedlist.display()
# mylinkedlist.reverse()
# mylinkedlist.display()
