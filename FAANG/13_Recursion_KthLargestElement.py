# The data structure that will connect with recursion:
# 2D-Array
# Binary Trees
# Heaps
# Graphs

# The algorithm that related to recursion:
# Sorting
# Greedy method
# Divide and conquer
# DP
# Backtracking

# Normal recursion space O(n)
def recFactorial(x):
    if x <= 1:
        return 1
    return x * recFactorial(x - 1)


# Tail recursion space O(1)
def tailFactorial(x, totalSoFar=1):
    if x == 0:
        return totalSoFar
    return tailFactorial(x - 1, x * totalSoFar)
# 这里可以将空间压缩到1，是因为每次我们只是存储了一个function，关键的不同在于
# 最后的return的部分，第一个的x在递归方程的外面，而第二个在递归方程的内部每次直接进行计算

# Question:
# Give an unsorted array, return the Kth largest number of the array
# not the Kth distinct number

# Constraints:
# Will the k be larger than the array's length? No, assume the answer is always available


# Create some test cases:
testCases = [
    # input, k, answer
    [[5, 3, 1, 6, 4, 2], 2, 5],
    [[2, 3, 1, 2, 4, 2], 4, 2],
    [[3], 1, 3],
]


# 这个问题的答案先从快速排序算法中来：
def partition(arr, start, end):  # time O(n) ~ O(n^2)
    # partition, sort, and get the pivot index
    pivot = arr[end]  # base num
    left = start

    for i in range(start, end):
        if arr[i] >= pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[end] = arr[left]
    arr[left] = pivot

    return left


def quickSort(arr, start, end):  # space O(logn)
    if start <= end:
        partitionIdx = partition(arr, start, end)
        quickSort(arr, start, partitionIdx - 1)
        quickSort(arr, partitionIdx + 1, end)


def kthLargest(arr, start, end, k):
    quickSort(arr, start, end)
    return arr[k - 1]


# Hoare's Quickselect Algorithm!这个算法确实是我开始想的那个，就是只看pivot的位置是不是要找的值
# 重写：
def partition(arr, start, end):
    # partition, sort, and get the pivot index
    pivot = arr[end]  # base num
    left = start

    for i in range(start, end):
        if arr[i] >= pivot:
            # 这里的排序就是找最大
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[end], arr[left] = arr[left], arr[end]

    return left


def KthLargest(arr, start, end, k):
    indexToFind = k - 1

    if start <= end:
        partitionIdx = partition(arr, start, end)

        if indexToFind == partitionIdx:
            return arr[partitionIdx]
        elif indexToFind < partitionIdx:
            return KthLargest(arr, start, partitionIdx - 1, k)
        else:
            # 这里不需要调整k，是因为，我们始终是基于原始的arr进行排序的，使用的是原始的index，并没有生成新的arr
            return KthLargest(arr, partitionIdx + 1, end, k)


# 在排序的时候最坏的情况是完全是反的，那么每轮只能排序一个并且遍历全部元素，所以是O(n^2)
# 在空间复杂度上这里使用了tail recursion，所以是O(1)
# test
for idx, case in enumerate(testCases):
    arr = case[0]
    k = case[1]

    res = KthLargest(arr, 0, len(arr) - 1, k)

    if case[2] == res:
        print(f"Pass the case #{idx}")
    else:
        print(f"Not Pass the case #{idx}: {case}")
