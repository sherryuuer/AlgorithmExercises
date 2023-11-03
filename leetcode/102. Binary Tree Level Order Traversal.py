# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            ans.append(vals)
        return ans
