array = [5, 9, 3, 10, 45, 2, 0]


def my_selection_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        min_i = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
        print(arr)
    return arr
# I did the same with my gpt buddy.
# 从第一个数字开始，假定第一个数字是最小的取得它的下标
# 然后再后面的子序列中寻找最小值的下标和左边的互换


sorted_array = my_selection_sort(array)


def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i 
    return smallest_index


def selectionSort(array):
    newarr = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        newarr.append(array.pop(smallest))
    return newarr


print("sort", selectionSort(array))
