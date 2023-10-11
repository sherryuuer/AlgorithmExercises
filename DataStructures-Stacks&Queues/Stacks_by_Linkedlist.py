class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.next = None
        self.length = 0

    def push(self, data):

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head  # current is the current pointer.
        while current.next:
            current = current.next
        current.next = new_node
        self.length += 1

    def peak(self):
        current = self.head
        while current.next:
            current = current.next
        # print(current.data)

    def pop(self):
        current = self.head
        count = 0
        while current.next and count < self.length - 1:
            current = current.next
            count += 1
        popped_data = current.next.data
        print(f"popped_data: {popped_data}")
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traversetoindex(self, position):
        current = self.head
        count = 0
        # handle error 
        while current and count < position:
            current = current.next
            count += 1
        print(current.data)  # get the position data.


mystack = Stack()
mystack.push(1)
mystack.push(2)
mystack.push(9)
mystack.peak()
mystack.pop()
mystack.display()
