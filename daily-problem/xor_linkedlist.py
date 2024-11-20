# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element)
# which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume
# you have access to get_pointer and dereference_pointer functions that converts
# between nodes and memory addresses.
# 中间节点可以通过前后节点计算出both值，从而反推前后节点
# XOR反向推导：
# 如果有 c = a XOR b，想求出 a 或 b：
# a = c XOR b
# b = c XOR a

class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = []  # save the nodes address

    def get_pointer(self, node):
        return self.nodes.index(node)  # get index of the node

    def dereference_pointer(self, pointer):
        return self.nodes[pointer]

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # get tail index
            tail_pointer = self.get_pointer(self.tail)
            # update new node BOTH
            new_node.both = tail_pointer ^ 0
            # update old tail BOTH
            self.tail.both ^= self.get_pointer(new_node)
            # update tail node
            self.tail = new_node
        self.nodes.append(new_node)

    def get(self, index):
        prev_addr = 0  # 初始化前指针
        current = self.head  # 初始化当前node
        for i in range(index):
            next_addr = current.both ^ prev_addr  # 计算下一个指针
            prev_addr = self.get_pointer(current)  # 当前节点->前指针
            current = self.dereference_pointer(next_addr)  # 下一个节点变当前节点
        return current.val
