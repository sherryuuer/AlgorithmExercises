# Create the below linked list: (Javascript)
# myLinkedList = {"head": {"value": 10, "next": {"value": 5, "next": {"value": 16, "next": None}}}}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # {data: data, next: None}


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def append(self, data):
        # new_node = Node(data)
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = self.head
        #     self.length = 1
        # else:
        #     self.tail.next = new_node
        #     # {data: data, next: {data: data, next: None}}
        #     self.tail = new_node
        #     self.length += 1

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head  # current is the current pointer.
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        # handle error
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Out of range.")
            return
        # if ok insert
        new_node.next = current.next
        current.next = new_node

    def remove(self, position):
        # if linkedlist is empty.
        if not self.head:
            return

        current = self.head
        count = 0
        # if the position is 0
        if current == self.head:
            self.head = self.head.next
            return
        # else
        # handle error
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Out of range.")
            return
        # if ok remove
        current.next = current.next.next

        # if not position but value:
        # current = self.head
        # while current.next:
        #     if current.next.data == value:
        #         current.next = current.next.next
        #         return
        #     current = current.next

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


mylinkedlist = LinkedList()
mylinkedlist.append(5)
mylinkedlist.prepend(7)
mylinkedlist.prepend(8)
mylinkedlist.display()
mylinkedlist.reverse()
mylinkedlist.display()
