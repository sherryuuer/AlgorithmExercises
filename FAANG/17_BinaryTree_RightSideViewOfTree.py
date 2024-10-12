# Give a binary tree, image you are standing at the right side of the tree
# return the value that you can see, from top to down
# 这道题很有意思，因为看似是找最右边的分支的value，但是有可能不是一个完全的树，所以，可能有很多部分是没有被挡住的，直觉无法直接取node的right分支
# 第一眼看，和上一道BFS有关联，其实就是取得每一层的最后一个元素
# 从BFS来说解答会很简单，但是还可以从DFS来解答，这个就很有趣了
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    # Time O(n) Space O(width) -> 最长的最宽的queue的长度
    def rightSideOfTheTreeBFS(self, root):
        from collections import deque

        result = []
        nodeQueue = deque([])
        if not root:
            return result
        nodeQueue.append(root)
        while nodeQueue:
            curValsList = []
            for _ in range(len(nodeQueue)):
                node = nodeQueue.popleft()
                curValsList.append(node.val)
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            result.append(curValsList[-1])
        return result

    # DFS way Time O(n), Space O(height)
    def rightSideOfTheTreeDFS(self, root):
        result = []
        self.helperFunction(root, 0, result)
        return result

    def helperFunction(self, node, depth, result):
        if not node:
            return

        if depth == len(result):
            result.append(node.val)

        self.helperFunction(node.right, depth+1, result)
        self.helperFunction(node.left, depth+1, result)

    # practice traversal
    def traversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def inorder(self, node, result):
        if not node:
            return
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)

    def preorder(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)

    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.right, result)
        self.postorder(node.left, result)
        result.append(node.val)


# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

#     1
#  2    3
# 4 5     6

# Create BinaryTree object and perform level order traversal
bt = BinaryTree()
print(bt.rightSideOfTheTreeDFS(root))
print(bt.traversal(root))
