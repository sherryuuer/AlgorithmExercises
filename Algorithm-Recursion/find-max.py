arr = [3, 5, 9, 29, 3, 8]


def find_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr.pop()
    else:
        return max(arr[0], find_max(arr[1:]))


print(find_max(arr))
# 虽然递归可以找到最大值，但是其实用一般的循环可以实现就挺好
