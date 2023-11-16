arr = [1, 3, 4, 6, 9, 3]


def count_element(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return 1 + count_element(arr)


print(count_element(arr))
