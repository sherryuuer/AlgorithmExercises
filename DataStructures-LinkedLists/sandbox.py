# 定义一个链表节点类
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 定义一个链表类
class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表末尾添加一个节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 打印链表的所有节点数据
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 创建一个链表实例
my_linked_list = LinkedList()

# 向链表中添加节点
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# 打印链表
my_linked_list.display()
