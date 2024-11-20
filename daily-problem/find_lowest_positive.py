# Given an array of integers, find the first missing positive integer
# in linear time and constant space.
# In other words, find the lowest positive integer that does not exist
# in the array. The array can contain duplicates and negative numbers as well.
# You can modify the input array in-place.
array = [3, -1, 2, 1]  # 2


def find_lowest_positive(array):
    n = len(array)

    for i in range(n):
        while 1 <= array[i] <= n and array[i] != array[array[i] - 1]:
            # 这样交换会陷入死循环
            # array[i], array[array[i] - 1] = array[array[i] - 1], array[i]
            # 先在正确的index放入值，然后再在当前index放入替换的值进行下次判断
            array[array[i] - 1], array[i] = array[i], array[array[i] - 1]

    for i in range(n):
        if array[i] != i + 1:
            return i + 1

    return n + 1


print(find_lowest_positive(array))
