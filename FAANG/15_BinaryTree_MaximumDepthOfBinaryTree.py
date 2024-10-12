# Give a binary tree, find the depth of the tree
# if the tree is empty, return 0
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def maxDepth(self, root):
        count = 0
        if not root:
            return count

        return self.recursive(root, count)

    def recursive(self, node, count):
        if node == None:
            return count
        count += 1
        return max(self.recursive(node.left, count), self.recursive(node.right, count))


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Create BinaryTree object and find max depth
bt = BinaryTree()
print(bt.maxDepth(root))  # Output will be 3
