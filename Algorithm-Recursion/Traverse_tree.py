class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1. 前序遍历（Preorder traversal）：根节点 -> 左子树 -> 右子树
def preorder_traversal(node):
    if node is not None:
        print(node.value)  # 访问根节点
        preorder_traversal(node.left)  # 前序遍历左子树
        preorder_traversal(node.right)  # 前序遍历右子树


# 2. 中序遍历（Inorder traversal）：左子树 -> 根节点 -> 右子树
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)  # 中序遍历左子树
        print(node.value)  # 访问根节点
        inorder_traversal(node.right)  # 中序遍历右子树


# 3. 后序遍历（Postorder traversal）：左子树 -> 右子树 -> 根节点
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # 后序遍历左子树
        postorder_traversal(node.right)  # 后序遍历右子树
        print(node.value)  # 访问根节点

# 通过传入树的根节点来调用这些遍历函数，根据需要选择前序、中序或后序遍历来遍历树的节点。例如：


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("前序遍历:")
preorder_traversal(root)

print("\n中序遍历:")
inorder_traversal(root)

print("\n后序遍历:")
postorder_traversal(root)
