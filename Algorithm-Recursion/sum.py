def sum_normal(arr):
    total = 0
    for e in arr:
        total += e
    return total


def sum_recursive(arr):
    if len(arr) == 0:
        return 0
    else:
        n = arr.pop()
        return n + sum_recursive(arr)


print(sum_recursive([2, 4, 6]))
