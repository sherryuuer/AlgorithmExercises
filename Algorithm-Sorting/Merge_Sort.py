numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def my_mergesort(array):
    if len(array) == 1:
        return array
    # Split Array in into right and left
    if len(array) % 2 == 0:
        middle = int(len(array) / 2)
    else:
        middle = int((len(array) + 1) / 2)
    left = array[:middle]
    right = array[middle:]

    return my_merge(
        my_mergesort(left),
        my_mergesort(right)
    )


def my_merge(left, right):
    merged_list = []
    flag = True
    while flag is True:
        if left[0] < right[0]:
            merged_list.append(left[0])
            del left[0]
            if not left:
                flag = False
        else:
            merged_list.append(right[0])
            del right[0]
            if not right:
                flag = False
        print(merged_list)
    if not left:
        merged_list.extend(right)
    else:
        merged_list.extend(left)
    return merged_list


# left = [3, 9, 56, 78]
# right = [1, 7, 9, 15]
# result = merge(left, right)
# print(result)
# answer = mergesort(numbers)
# print(answer)
# 步骤：
# 如果数组的长度为1或0，那么它已经被视为排序好的。
# 否则，将数组分为左右两部分。
# 对左子数组和右子数组分别应用递归排序。
# 一旦左子数组和右子数组都已经排序，开始合并它们。创建一个新的空数组，并比较左右子数组的元素，按升序将它们合并到新数组中。
# 当一边的子数组被合并完后，将另一边的子数组中的剩余元素全部追加到新数组中。
# 返回新数组，它是已排序的。

def mergesort(arr):  # divide  BigO = logn
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    print('Left {}'.format(left))
    print('Right {}'.format(right))

    return merge(mergesort(left), mergesort(right))  # O(n)


def merge(left, right):  # merge BigO = n
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    print(left, right)
    print(result + left[leftindex:] + right[rightindex:])
    return result + left[leftindex:] + right[rightindex:]


x = mergesort(numbers)
print(x)
