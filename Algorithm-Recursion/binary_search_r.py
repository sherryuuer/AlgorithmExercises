# Binary Search，array must be ordered.
# 用递归的方法写二分查找
numbers = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]


def binary_search_r(array, num):
    # define left and right pointer.
    left = 0
    right = len(array) - 1
    middle = int((left + right) // 2)
    print(array)

    if middle == 0:
        if num == array[left]:
            return "Found the number."
        elif num == array[right]:
            return "Found the number."
        else:
            return "Not exsit."
    else:
        # compare the num with the middle element.
        if num == array[middle]:
            return "Found the number."
        elif num < array[middle]:  # the num is in the left half.
            return binary_search_r(array[:(middle - 1)], num)
        else:
            return binary_search_r(array[(middle + 1):], num)  # O(log n)


result = binary_search_r(numbers, 99)
print(result)
