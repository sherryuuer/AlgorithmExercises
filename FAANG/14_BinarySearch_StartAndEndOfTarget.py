# first try to implement the binary search
def helperFunction(arr, left, right, target):
    if left >= right:
        return None

    mid = (left + right) // 2
    if target < arr[mid]:
        return helperFunction(arr, 0, mid-1, target)
    elif target > arr[mid]:
        return helperFunction(arr, mid+1, len(arr) - 1, target)
    return mid


def binarySearch(arr, target):
    index = helperFunction(arr, 0, len(arr)-1, target)
    return index if index is not None else -1


# Question is :
# Give an ascending array, return the start and end value of the given target value in the array.
# the solution should run in O(logn) time not O(n)
# Constrains:
# What if the target is not in the array: return -1, because all value in the array is positive
testCases = [
    [[1, 2, 3, 3, 4, 5, 5, 5, 6, 7], 5, [5, 7]],
    [[1, 2, 3, 4, 5, 6, 7], 5, [4, 4]],
    [[1, 2, 3, 4, 5], 9, [-1, -1]],
    [[], 5, [-1, -1]],
]


def StartAndEndOfTarget(arr, target):
    # if no element return [-1, -1]
    if not arr:
        return [-1, -1]
    # do binary search to find the first value
    idx = binarySearch(arr, target)
    # if the value not exsits, return [-1, -1]
    if idx == -1:
        return [-1, -1]

    # find the first value that smaller than the target, so we get the left position tobe smaller + 1
    def findLeft(idx):
        left = 0
        right = idx
        # 边界问题总是很难处理，这里因为有可能idx正是边界，所以我们包括它
        while left <= right:
            mid = (left + right) // 2
            # the left side only can be smaller or equal to target
            if arr[mid] == target and arr[mid - 1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    # find the first value that larger than the target, so we get the right position tobe larger - 1
    def findRight(idx):
        left = idx
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            # the left side only can be smaller or equal to target
            if arr[mid] == target and arr[mid + 1] > target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    print([findLeft(idx), findRight(idx)])
    return [findLeft(idx), findRight(idx)]


# 另一种方法，我们一直进行二分查找，直到返回-1，这个过程我们一直track左右point
def StartAndEndOfTarget(arr, target):
    # if no element return [-1, -1]
    if not arr:
        return [-1, -1]
    # do binary search to find the first value
    idx = binarySearch(arr, target)
    # if the value not exsits, return [-1, -1]
    if idx == -1:
        return [-1, -1]

    startPoint, endPoint = idx, idx

    while True:
        temp = binarySearch(arr[0: startPoint], target)
        if temp != -1:
            startPoint = temp
        else:
            break

    while True:
        temp = binarySearch(arr[endPoint + 1: len(arr) - 1], target)
        if temp != -1:
            endPoint = temp
        else:
            break

    return [startPoint, endPoint]


for case in testCases:
    arr = case[0]
    target = case[1]
    res = case[2]

    if StartAndEndOfTarget(arr, target) == res:
        print("pass")
    else:
        print("NG")
