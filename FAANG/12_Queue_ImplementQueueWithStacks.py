# Implement a Queue with stack
# Method should have: enqueue, dequeue, peek, empty
# Because we are use stack, it is not possible be enficent as a real queue, but we have to make it as perfoment as possible
# Key point is we have 2 stack!!, one for append, one for pop, when the pop one empty, reverse element from the append one
# Intresting!
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        popped = None
        if not self.isEmpty():
            popped = self.stack[-1]
            self.stack = self.stack[:-1]
        return popped

    def push(self, value):
        self.stack.append(value)

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None


class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, value):  # O(1)
        self.inStack.push(value)

    def dequeue(self):  # O(n)
        if self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                value = self.inStack.pop()
                self.outStack.push(value)
        return self.outStack.pop()

    def peek(self):  # O(n)
        if not self.outStack.isEmpty():
            return self.outStack.peek()
        elif not self.inStack.isEmpty:
            return self.inStack[0]
        else:
            return None

    def isEmpty(self):  # O(1)
        return self.outStack.isEmpty() and self.inStack.isEmpty()


q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())  # 1
print(q.dequeue())  # 4
q.enqueue(0)
q.enqueue(8)
print(q.isEmpty())  # false
print(q.peek())  # 5
