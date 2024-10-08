# Constraints:
# What do we return if we get null or single node? Just return the node or null
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head):
        """Reverse the full linked list."""
        if not head or not head.next:
            return head

        curNode = head
        prevNode = None
        while curNode:
            tempNode = curNode.next  # store the next node
            curNode.next = prevNode
            prevNode = curNode
            curNode = tempNode

        return prevNode

    def reverseInterval(self, head, m, n):
        """Reverse the nodes between position m and n."""
        if not head or not head.next:
            return head
        # for global
        preNode = None
        startNode = head
        i = 0

        while i < m:
            preNode = startNode
            startNode = startNode.next
            i += 1

        # for m ~ n
        prev = None
        cur = startNode
        while i <= n and cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            i += 1

        # prev is the m ~ n head
        # the cut down point is preNode(the last node before m) -> startNode(the last node of m~n)
        # the start node will become the tail of the m~n
        preNode.next = prev
        startNode.next = cur

        return head

    def print_list(self, head):
        curNode = head
        while curNode:
            print(curNode.value, end=" -> ")
            curNode = curNode.next
        print("None")


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


ll = LinkedList()
head = create_linked_list([1, 2, 3, 4, 5, 6, 7])  # [1, 2, 3, 4, 5]
print("Original List:")
ll.print_list(head)

reversed_head = ll.reverseInterval(head, 2, 4)
print("Reversed List:")
ll.print_list(reversed_head)
