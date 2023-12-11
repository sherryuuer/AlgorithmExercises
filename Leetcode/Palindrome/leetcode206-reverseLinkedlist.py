# 双指针法,感觉还是双指针比较清晰
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        pre = None

        while current:
            temp = current.next  # 保存current的下一个节点，因为接下来要改变指向了
            current.next = pre
            # 更新指针
            pre = current
            current = temp
        return pre  # pre is new Linked list's head


# 递归法
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)

    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)
