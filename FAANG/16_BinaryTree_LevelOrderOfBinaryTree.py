# Give a binary tree, return the level order of the nodes value
# I think, this is a BFS traversal
# every level will be return as a array
# at last we return a array of arrays
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# I think I need a queue
# Time O(n) Space O(n)
class BinaryTree:

    def levelOrderValue(self, root):
        from collections import deque

        if not root:
            return []

        result = []
        nodeQueue = deque([root])

        while nodeQueue:
            size = len(nodeQueue)
            valList = []
            for _ in range(size):
                node = nodeQueue.popleft()
                valList.append(node.val)
                if node.left:
                    nodeQueue.append(node.left)
                if node.right:
                    nodeQueue.append(node.right)
            result.append(valList)

        return result


# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Create BinaryTree object and perform level order traversal
bt = BinaryTree()
print(bt.levelOrderValue(root))
