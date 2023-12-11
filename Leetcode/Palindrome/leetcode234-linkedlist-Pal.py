# 链表回文判断
# input: 1->2->2->1 True
# input: 1->2 False
# space O(n) 但是可以做到space O(1)
# 快慢指针，取中，和，反转技能


# 反转链表函数
def reverseList(head):
    # head: ListNode
    if not head:
        return None
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


# 通过书完整解法
def isPalindrome(head):
    pre = None
    slow = fast = head
    # 一边反转前半，一边找中点
    while fast and fast.next:
        # 先更新fast指针
        fast = fast.next.next
        # 再反转和更新slow指针
        next = slow.next
        slow.next = pre
        pre = slow
        slow = next
    # 处理奇数个节点的情况
    if fast:
        slow = slow.next
    # 从中点开始分别向前和向后遍历，逐个比较是否相同即可
    while slow:
        if slow.val != pre.val:
            return False
        pre = pre.next
        slow = slow.next
    return True


# 要考虑到链表！的特殊之处！因为它不能往回走
# 双指针左右移动法
# 模拟成数组链表，判断回文： 很好理解
def isPalindrome(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next

    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True


# 栈和递归法，正入反出 space O(n)
# 进阶技巧：快慢指针 space O(1)
def isPalindrome(head):
    fast = slow = head
    # 找中点
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    node = None  # pre
    # 反转后半段
    # 1221的情况反转的是21，12321的情况反转的是321，都可以达到后期可以比较的效果
    # 参见链表的双指针206题
    while slow:  # slow is current, node is pre
        temp = slow.next
        slow.next = node
        node = slow
        slow = temp
        # simple way:
        # slow.next, slow, node = node, slow.next, slow

    # 比较
    while node:  # node 是新的，反转过的后半段链表的，head节点
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True
