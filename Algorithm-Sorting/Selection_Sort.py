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


sorted_array = my_selection_sort(array)
