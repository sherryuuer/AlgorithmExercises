
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            # 从左到右依次连接
            next = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur = next
            ans.extend(vals)
        return ans
