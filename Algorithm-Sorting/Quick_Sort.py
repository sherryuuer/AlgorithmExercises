# Solution
# divide and conquer
# Easy to understand
def quicksort_simple(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 选择第一个元素作为基准
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort_simple(less) + [pivot] + quicksort_simple(greater)


# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort_simple(arr)
print(sorted_arr)
