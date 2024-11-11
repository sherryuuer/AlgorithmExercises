def merge_func(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    return result + left[left_index:] + right[right_index:]


def merge_sort(array):
    """sort the array as a asc way"""
    if len(array) <= 1:
        return array

    mid = len(array) // 2  # 这个地方是易错点
    return merge_func(merge_sort(array[:mid]), merge_sort(array[mid:]))

# print(merge_sort(array))


def quick_sort(array, start, end):
    if end - start <= 0:
        return

    pivot = array[end]
    left = start

    for i in range(start, end):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1

    array[end] = array[left]
    array[left] = pivot

    # 这里绝对不可以用切片，因为切片是一个新的数组
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)

    return array


array = [4, 6, 3, 6, 2, 8, 10]
# 这道题也是left和right指针很tricky
# print(quick_sort(array, 0, len(array) - 1))
