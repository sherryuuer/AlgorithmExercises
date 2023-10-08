list1 = ["a", "b", "x", "y"]
list2 = ["m", "n", "x"]


# check if there are common element in both list.
# def commonelement(list1, list2):
#     for element in list1:
#         if element in list2:
#             return True
#     return False


# result = commonelement(list1, list2)
# print(result)
# O(a * b)


# another better way.
def commonelement(list1, list2):
    hash_list = {}
    for ele in list1:
        hash_list[ele] = True
    print(hash_list)
    for ele in list2:
        if ele in hash_list:
            return hash_list[ele]
    return False


result = commonelement(list1, list2)
print(result)
# O(n)
