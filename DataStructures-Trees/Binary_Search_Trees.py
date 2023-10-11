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

    def print_tree(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is not None:
            # recursion print left child tree
            self._print_inorder(node.left)
            # print the current node
            print(node.data, end=" ")  # use end=" " to divide node data
            # recursion print right child tree
            self._print_inorder(node.right)

    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            # find the delete node.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # if the node have both left and right.
            min_val = self._find_min(node.right)
            node.data = min_val
            # recursion
            node.right = self._remove(node.right, min_val)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.data

# 上述代码中的remove方法采用递归方式实现。它查找要删除的数据，并根据不同情况执行相应的操作：
# 1. 如果要删除的数据小于当前节点的数据，则继续在左子树中查找。
# 2. 如果要删除的数据大于当前节点的数据，则继续在右子树中查找。
# 3. 如果找到了要删除的节点，有以下几种情况：
#    - 如果节点没有子节点，它将被直接删除。
#    - 如果节点只有一个子节点，它将被替换为其子节点。
#    - 如果节点有两个子节点，它将被右子树中最小值节点替换，然后递归地删除最小值节点。

# another way to remove node
# ztm way
# Finally comes the very complicated remove method.
# This one is too complicated for me to explain while writing. So I'll just write the code down with some comments
# explaining which conditions are being checked
    def another_remove(self, data):
        if self.root is None:  # Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node is not None:  # Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:  # Match is found. Different cases to be checked
                # Node has left child only
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                # Node has right child only
                elif current_node.left is None:
                    if parent_node is None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # Node has neither left nor right child
                elif current_node.left is None and current_node.right is None:
                    if parent_node is None:  # Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has both left and right child
                elif current_node.left is not None and current_node.right is not None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left is not None:  # Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data  # The value to be replaced is copied
                    if del_node == del_node_parent:  # If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right is None:  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.lookup(170)
# bst.insert(4)
bst.print_tree()
