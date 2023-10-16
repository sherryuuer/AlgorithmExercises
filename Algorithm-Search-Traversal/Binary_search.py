# Binary Search，array must be ordered.
numbers = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]


def binary_search(array, num):
    # define left and right pointer.
    left = 0
    right = len(array) - 1
    while left <= right:
        # find the middle of the array.
        middle = int((left + right) // 2)
        # compare the num with the middle element.
        if num == array[middle]:
            return "Found the number."
        elif num < array[middle]:  # the num is in the left half.
            right = middle - 1  # change the range.
        else:
            left = middle + 1
    return "Not exsit."
# O(log n)


result = binary_search(numbers, 99)
print(result)
