class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        # check if there exsit root.
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if new_node.data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            elif new_node.data > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return
            else:
                return

    def lookup(self, data):
        current = self.root
        count = 0

        while current:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                print(f"Found it with {count + 1} times!")
                return True
            count += 1

        print("Oops, not exists.")
        return False

    def inorder(self, current, result):
        if current is not None:
            # Traverse the left subtree
            self.inorder(current.left, result) 
            # Visit the current node (append its data to the result)
            result.append(current.data)
            # Traverse the right subtree
            self.inorder(current.right, result)

        return f"result: {result}"

    # A esay way to understand.
    def inorder_ztm(self, current, result):
        if current.left:
            # Traverse the left subtree
            self.inorder_ztm(current.left, result) 
            # Visit the current node (append its data to the result)
        result.append(current.data)
        if current.right:
            # Traverse the right subtree
            self.inorder_ztm(current.right, result)

        return f"result: {result}"

    def preorder(self, current, result):
        if current is not None:
            result.append(current.data)
            # Recursively traverse the left subtree
            self.preorder(current.left, result)
            # Recursively traverse the right subtree
            self.preorder(current.right, result)

        return f"result: {result}"

    # A esay way to understand.
    def preorder_ztm(self, current, result):
        result.append(current.data)
        if current.left:
            # Recursively traverse the left subtree
            self.preorder_ztm(current.left, result)
        if current.right:
            # Recursively traverse the right subtree
            self.preorder_ztm(current.right, result)

        return f"result: {result}"

    def postorder(self, current, result):
        if current is not None:
            self.postorder(current.left, result)
            self.postorder(current.right, result)
            result.append(current.data)

        return f"result: {result}"

    # A esay way to understand.
    def postorder_ztm(self, current, result):
        if current.left:
            self.postorder_ztm(current.left, result)
        if current.right:
            self.postorder_ztm(current.right, result)
        result.append(current.data)
        return result

    # leetcode 98
    def is_valid_BST(self, root):
        return self.is_valid_BST_helper(root, float("-inf"), float("inf"))

    def is_valid_BST_helper(self, node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.data < max_val):
            return False

        # Recursively check the left and right subtrees
        return (self.is_valid_BST_helper(node.left, min_val, node.data) and
                self.is_valid_BST_helper(node.right, node.data, max_val))


#      9
#  4       20
# 1  6   15  170
# InOrder-[1, 4, 6, 9, 15, 20, 170]
# PreOrder-[9, 4, 1, 6, 20, 15, 170]
# PostOrder-[1, 6, 4, 15, 170, 20, 9]
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.isVaildBST(bst.root))
# print(bst.inorder(bst.root, []))
# print(bst.inorder_ztm(bst.root, []))
# print(bst.preorder_ztm(bst.root, []))
# print(bst.postorder(bst.root, []))
# print(bst.postorder_ztm(bst.root, []))
