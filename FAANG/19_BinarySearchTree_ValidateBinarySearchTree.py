# Valid binary search tree is a tree that all nodes right branch(all nodes) is larger than the left branch
# Constraints:
# Is a empty tree valid?
# Can there be any duplicate values in the tree? yes, but the tree will not be valid
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# I think a preorder traversal and check every value is bigger than the former one
# is the most simple way, maybe it is brute force
def preorder(result, node):
    if not node:
        return
    preorder(result, node.left)
    result.append(node.val)
    preorder(result, node.right)


def validBinarySearchTree(node):
    if not node:
        return True
    result = []
    preorder(result, node)
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            return False
    return True


# Another way, check every node as we go traversal
# Important: boundary, when go left, update the < node, when go right, update the > node
def checkValid(node, left, right):
    if not node:
        return True

    if node.val <= left or node.val >= right:
        return False

    # if node.left:
    #     rightBoundary = node.val
    #     return checkValid(node.left, left, rightBoundary)

    # if node.right:
    #     leftBoundary = node.val
    #     return checkValid(node.right, leftBoundary, right)

    # repair:
    if node.left:
        rightBoundary = node.val
        if not checkValid(node.left, left, rightBoundary):
            return False

    if node.right:
        leftBoundary = node.val
        if not checkValid(node.right, leftBoundary, right):
            return False

    return True

    # How can I check left and right seperately! stupid!
    # 将问题简化为只有三个节点怎么样，剩下的交给递归，仅用下面这一行代码，更加聪明
    # return checkValid(node.left, left, node.val) and checkValid(node.right, node.val, right)


# test case 1
root = TreeNode(15)
root.left = TreeNode(12)
root.left.left = TreeNode(10)
root.left.right = TreeNode(14)
root.right = TreeNode(18)
root.right.left = TreeNode(13)  # less than root so false
root.right.right = TreeNode(20)
# false
# print(validBinarySearchTree(root))
leftBoundary = float("-inf")
rightBoundary = float("inf")
res = checkValid(root, leftBoundary, rightBoundary)
print(res)

# test case 2
root = TreeNode(12)
root.left = TreeNode(7)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.right = TreeNode(18)
root.right.left = TreeNode(16)
root.right.right = TreeNode(25)
# true
# print(validBinarySearchTree(root))
leftBoundary = float("-inf")
rightBoundary = float("inf")
res = checkValid(root, leftBoundary, rightBoundary)
print(res)

# test case 3
root = TreeNode(1)
# true
# print(validBinarySearchTree(root))
leftBoundary = float("-inf")
rightBoundary = float("inf")
res = checkValid(root, leftBoundary, rightBoundary)
print(res)
