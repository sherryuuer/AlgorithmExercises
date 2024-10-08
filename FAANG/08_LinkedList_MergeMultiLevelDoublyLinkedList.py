# The "Merge Multi-Level Doubly Linked List" problem involves
# flattening a multilevel doubly linked list where
# nodes may have a child pointer to another doubly linked list,
# combining all levels into a single-level doubly linked list
# while maintaining the original node order.
# Node 中增加了一个child节点的属性，如果存在child节点，就将子链表添加到本链表中
# 这里我用了递归，重新开一个文件尝试可不可以不用递归，直接traversal到最后
class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.child = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def _mergeNode(self, node, nextNode):
        child = node.child
        node.child = None

        node.next = child
        child.prev = node

        # find the tail of the child
        cur = child
        while cur.next:
            nxt = cur.next
            if cur.child:
                # instead of recursive use stack is better
                self._mergeNode(cur, nxt)
            cur = nxt

        cur.next = nextNode
        if nextNode:
            nextNode.prev = cur

        # last node hasn's been checked so
        if cur.child:
            self._mergeNode(cur, nextNode)

    def mergeMultiLevelDoublyLinkedList(self, head):
        if not head:
            return None

        curNode = head
        while curNode:
            nextNode = curNode.next
            if curNode.child:
                self._mergeNode(curNode, nextNode)
            curNode = nextNode

        return head

    def print_list(self, head):
        cur = head
        while cur:
            print(cur.value, end=" -> ")
            cur = cur.next
        print("None")


# Test case creation
def create_test_case():
    # Creating the main level
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    head.next = node2
    node2.prev = head
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5

    # Creating the child list of node3
    child1 = ListNode(7)
    child2 = ListNode(8)
    child3 = ListNode(9)
    child4 = ListNode(10)

    node3.child = child1
    child1.next = child2
    child2.prev = child1
    child2.child = child3
    child3.next = child4
    child4.prev = child3

    # 1 2 3 7 8 9 10 4 5 6
    # Creating a DoublyLinkedList object and assigning the head
    dll = DoublyLinkedList()
    dll.head = head

    return dll


# Example usage
dll = create_test_case()
print("Original list (multilevel):")
dll.print_list(dll.head)  # This will just print the top level

print("After merge list (multilevel):")
dll.mergeMultiLevelDoublyLinkedList(dll.head)
dll.print_list(dll.head)
