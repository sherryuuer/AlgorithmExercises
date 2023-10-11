class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.next = None
        self.length = 0

    def enqueue(self, data):

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head  # current is the current pointer.
        while current.next:
            current = current.next
        current.next = new_node
        self.length += 1

    # become simple
    def peak(self):
        return self.head

    def dequeue(self):
        if not self.head:
            return None
        current = self.head
        dequeued_data = current
        self.head = current.next
        print(f"dequeued_data: {dequeued_data.data}")

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


myqueue = Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(9)
myqueue.peak()
myqueue.dequeue()
myqueue.display()
