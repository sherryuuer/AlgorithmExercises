# 广度优先搜索
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


# 创建一个示例二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(None)
root.right.right = TreeNode(7)

print(root)
# 执行横向搜索
result = level_order_traversal(root)
print(result)
