# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except
# the one at i.
array = [1, 2, 3, 4, 5]
# result: [120, 60, 40, 30, 24]
# Follow-up: what if you can't use division?


def product_of_array_except_self_division(array):
    if not array:
        return []
    if len(array) == 1:
        return [0]

    total_product = 1
    for num in array:
        total_product *= num

    return [total_product // num for num in array]


# print(product_of_array_except_self_division(array))


def product_of_array_except_self(array):
    if not array:
        return []
    if len(array) == 1:
        return [0]

    n = len(array)
    result = [1] * n

    # prefix product calculate
    prefix = 1
    for i in range(n):
        result[i] *= prefix
        prefix *= array[i]

    # calculate result with the suffix calculate
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= array[i]

    return result


print(product_of_array_except_self(array))
