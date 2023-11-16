import heapq


x = [5, 2, 8, 1, 6, 7, 4, 9]
# Heapify method sorts the list , this is min heap  
heapq.heapify(x)
print(x)
# heapq.heappush(x, 0)
# print(x)
# print(heapq.heappop(x))
# print(x)
# # Used to pop and push the element in same time
# print(heapq.heappushpop(x, 5))
# print(x)
# Used to get n largest elements in heap
# print(heapq.nlargest(4, x))
print(heapq.nlargest(1, x))
# # Used to get n smallest elements in heap
# print(heapq.nsmallest(4, x))

# heap = []

# # insert element
# heapq.heapify(heap)
# print(heap)
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 2)

# # pop min
# print(heap)
# print(heapq.heappop(heap))

# heapq 是 Python 标准库中的一个模块，用于实现最小堆（min-heap）和最大堆（max-heap）数据结构。每个节点的值都小于或等于（最小堆）或大于或等于（最大堆）其子节点的值。
# heapify(iterable): 将一个可迭代对象转化为一个堆。
# heappush(heap, element): 将一个元素插入到堆中。
# heappop(heap): 弹出并返回堆中的最小元素。
# heappushpop(heap, element): 插入一个元素到堆中，并立刻弹出并返回堆中的最小元素。
# heapreplace(heap, element): 弹出并返回堆中的最小元素，然后插入一个新元素到堆中。
# heapq 使得实现基于堆的数据结构（如优先队列）非常容易。堆常常用于解决与优先级相关的问题，例如调度算法、最短路径算法（如 Dijkstra 算法）等。

# 两个方法的关键区别：
# heappushpop 先弹出再插入，而 heapreplace 先插入再弹出。在 heappushpop 中，得到的是插入元素之后的堆顶元素，而在 heapreplace 中，得到的是插入元素之前的堆顶元素。
