# Full tree : all nodes have left and right nodes, or have no child nodes
# Complete tree : complete binary tree is a tree where every level is fully filled except possibly for the last level, which is filled from the left.
# A brute force solution is to traverse the tree (e.g., using DFS or BFS) and count all the nodes, but that would take O(N) time, where N is the number of nodes. For a large tree, this is inefficient.
# 两种优化方法：
# 第一种是先求上层full complete tree的节点数量然后通过二分树查找，求最后一层的节点数量
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryCompleteTree:
    def calculateHeight(self, node):
        count = 0
        if not node:
            return count

        while node:
            count += 1
            node = node.left
        return count

    def nodeExists(self, idxOfNodeToFind, height, node):
        left, right = 0, (2 ** (height - 1)) - 1
        for _ in range(height - 1):
            mid = (left + right) // 2
            if idxOfNodeToFind <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    def countNodes(self, root):
        if not root:
            return 0

        height = self.calculateHeight(root)
        if height == 1:
            return 1

        upperNodes = (2 ** (height - 1)) - 1

        # calculate last level nodes
        left, right = 0, upperNodes
        while left <= right:
            mid = (left + right) // 2
            if self.nodeExists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1

        return upperNodes + left


# 还有一种方法也很酷，通过递归滴求subtree的高度来缩小计算范围
# 我觉得这个方法很棒！！递归！
class BinaryCompleteTreeRecursive:
    def computeTreeHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def countNodes(self, root):
        if not root:
            return 0

        leftHeight = self.computeTreeHeight(root.left)
        rightHeight = self.computeTreeHeight(root.right)

        # if left subtree height == right subtree height
        if leftHeight == rightHeight:
            # (2 ** (leftHeight)) is the left subtree nodes + root node 1
            # notice the height is subtree's height, so no need to -1
            return (2 ** (leftHeight)) + self.countNodes(root.right)
        # if not, it means the right subtree is short but full, then we calculate the left tree
        else:
            return (2 ** (rightHeight)) + self.countNodes(root.left)


# Creating the tree nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Call the function with this tree
result = BinaryCompleteTreeRecursive().countNodes(root)
print(result)  # Expected output: 6
