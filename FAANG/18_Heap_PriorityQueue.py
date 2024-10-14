# Priority Queue Implementation, or Minheap
# size(), isEmpty(), peek(), pop(), push()
# Make it easy to calculate the index:
# Parent: idx; left: idx * 2; right: idx * 2 + 1
# Left: idx; parent: idx // 2
class MinHeap:
    def __init__(self):
        # the first element is dummy so it is easy to calculate
        self.heap = [0]

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return True if len(self.heap) == 1 else False

    def peek(self):
        if not self.isEmpty():
            return self.heap[1]
        return None

    def pop(self):
        if self.isEmpty():
            return None
        if self.size() == 1:
            return self.heap.pop()

        value = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return value

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def heapify(self, arr):
        self.heap = [0] + arr
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self._bubble_down(i)

    def _bubble_down(self, i):
        child = i * 2
        while child <= self.size():
            # compare the left and right child
            if child + 1 <= self.size() and self.heap[child + 1] < self.heap[child]:
                child += 1
            # compare the child and parent
            if self.heap[child] > self.heap[i]:
                break

            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
            child = i * 2

    def _bubble_up(self, i):
        parent = i // 2
        while i > 1 and self.heap[i] <= self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = i // 2
