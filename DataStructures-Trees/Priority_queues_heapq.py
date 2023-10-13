# Priority Queues, as the name suggests, are queues where the elements have different priorities
# And it does not always follow the FIFO rule.
# They can be implemented in a number of ways, out of which heap is the most commonly used one.
# In Python, it is available using “heapq” module. The property of this data structure in Python is that each time the smallest of heap element is popped(min heap).
# Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element  returns the smallest element each time.


import heapq

# initializing list
# li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
# heapq.heapify(li)

# printing created heap
# print(f"The created heap is : {li}")
# The created heap is : [1, 3, 9, 7, 5]

# heapq.heappush(li, 4)
# print(f"The modified heap after push is : {li}")
# #The modified heap after push is : [1, 3, 4, 7, 5, 9]

# print(f"The popped and smallest element is : {li}")
# #The popped and smallest element is : 1


# Creating two identical heaps to demonstrate the difference between heappushpop and heapreplace
li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)


print(li1, li2)
# using heappushpop() to push and pop items simultaneously
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))
print(li1)
# The popped item using heappushpop() is : 2


# using heapreplace() to push and pop items simultaneously
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))
print(li2)
# The popped item using heapreplace() is : 3
# in fact is poppush w
