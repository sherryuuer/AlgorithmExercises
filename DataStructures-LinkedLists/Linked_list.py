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

    def traversetoindex(self, position):
        current = self.head
        count = 0
        # handle error 
        while current and count < position:
            current = current.next
            count += 1
        print(current.data)  # get the position data.

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
        # while current.next:  123 while 2
        #     new_current = current.next  new_current = 3
        #     new_current.next = current  new_current.next = 2
        #     current = current.next      current = 3
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
mylinkedlist.traversetoindex(2)
mylinkedlist.display()
mylinkedlist.reverse()
mylinkedlist.display()

# 解释以下逆转算法。
# 这是一个链表逆转的经典算法，通常被称为"迭代法"。

# 1. `prev` 是一个用来跟踪上一个节点的指针，初始时设为 `None`。
# 2. `current` 是用来遍历链表的指针，初始时指向链表的头部 (`self.head`)。
# 3. `while current:` 这是一个循环，它会一直执行，直到 `current` 变为 `None`，也就是遍历完整个链表。
# 4. `next_node` 用来保存当前节点 (`current`) 的下一个节点，因为在逆转链表时，我们需要改变当前节点的 `next` 指针，如果不提前保存下一个节点，会丢失后续节点的引用。
# 5. `current.next = prev` 这一行将当前节点的 `next` 指针指向前一个节点 (`prev`)，实现了链表节点的逆转。
# 6. `prev = current` 更新 `prev` 指针，让它指向当前节点，以备下一次循环使用。
# 7. `current = next_node` 更新 `current` 指针，让它指向下一个节点，继续遍历链表。
# 8. 最后一行 `self.head = prev` 更新链表的头节点，因为原先的头节点现在已经变成了逆转后的链表的尾节点，所以需要将链表的头指针指向逆转后的链表的头节点。

# 通过这个算法逆转了链表，使原先的链表方向反转，变成了逆序的链表。这在许多情况下都是非常有用的操作，特别是在处理链表数据结构时。
