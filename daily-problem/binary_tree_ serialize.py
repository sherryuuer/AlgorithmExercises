# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def helper(node):
        if not node:
            return "None"
        left_serialize = helper(node.left)
        right_serialize = helper(node.right)
        return f"{node.val},{left_serialize},{right_serialize}"

    return helper(root)


def deserialize(string):
    def helper(nodes):
        val = nodes.pop(0)
        if val == "None":
            return None
        node = Node(val)
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    nodes = string.split(",")
    return helper(nodes)


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')
