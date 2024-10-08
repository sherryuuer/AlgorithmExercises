# 检测在链表中是否有循环，一种使用set数据结构，另一种Floyd's Tortoise And Hare
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def createLinkedList(self, valueList):
        dummy = ListNode(-1)
        cur = dummy
        for v in valueList:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def detectCycle(self, head):
        if not head:
            return False

        hashSet = set()
        cur = head

        while cur:
            if cur in hashSet:
                return False
            hashSet.add(cur)
            cur = cur.next

        return True

    def floyd(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow


ll = LinkedList()
head = ll.createLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 3])
res = ll.detectCycle(head)
print(res)

res2 = ll.floyd(head)
print(res2)
