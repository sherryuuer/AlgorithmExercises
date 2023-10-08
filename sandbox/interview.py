# google interview video question.
# Naive
# array1 = [1, 2, 3, 4, 5]
# def hasPairWithSum(arr, sum):
#     length = len(arr)  # 5
#     for i in range(length-1):  # range(4) 3
#         for j in range(i + 1, length):  # 4
#             if arr[i] + arr[j] == sum:
#                 return True
#     return False


# Better
def hasPairWithSum2(arr, sum):
    mySet = set()
    length = len(arr)
    for i in range(length):
        if arr[i] in mySet:
            return True
        mySet.add(sum - arr[i])
    return False


print(hasPairWithSum2([6, 4, 3, 2, 1, 7], 9))

# JS
# // Better
# function hasPairWithSum2(arr, sum) {
#     const mySet = new Set();
#     const len = arr.length;
#     for (let i = 0; i < len; i++) {
#         if (mySet.has(arr[i])) {
#             return true;
#         }
#         mySet.add(sum - arr[i]);
#     }
#     return false;
# }

# console.log(hasPairWithSum2([6,4,3,2,1,7], 9))
