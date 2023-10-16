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

    def breadthfirstsearch(self):
        current = self.root
        result = []  # The answer list
        queue = []  # A queue to store the child data we will check.
        queue.append(current)
        # This queue will become very big.Memory.
        while len(queue) > 0:
            current = queue[0]
            del queue[0]
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return f"result: {result}"

    def breadthfirstsearchR(self, queue, result):
        if len(queue) == 0:
            return f"result: {result}"
        else:
            current = queue[0]
            del queue[0]
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            return self.breadthfirstsearchR(queue, result)


#      9
#  4       20
# 1  6   15  170
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
# bst.lookup(170)
# bst.insert(4)
bst.print_tree()
# print(bst.breadthfirstsearch())
print(bst.breadthfirstsearchR([bst.root,], []))
