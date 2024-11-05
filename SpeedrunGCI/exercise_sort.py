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

    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)

    return array


def quick_sort_2(array):
    if len(array) <= 1:
        return

    pivot = array[-1]
    left = 0

    for i in range(len(array)):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1

    array[-1] = array[left]
    array[left] = pivot

    quick_sort_2(array[:left - 1])  # 这个写法是行不通的，因为这里的切片是创建了一个新的数组，而不是对原数组排序
    quick_sort_2(array[left + 1:])

    return array


def quick_sort_3(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = 0

    for i in range(len(array)):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1

    array[-1] = array[left]
    array[left] = pivot

    # 这种写法尽管是可行的，但是会增加额外的空间复杂度
    return quick_sort_3(array[:left]) + [array[left]] + quick_sort_3(array[left + 1:])


array = [4, 6, 3, 6, 2, 8, 10]
# 这道题也是left和right指针很tricky
# print(quick_sort(array, 0, len(array) - 1))
# print(quick_sort_2(array))
print(quick_sort_3(array))
