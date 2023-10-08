# def mergesortedarr(arr1, arr2):
#     x = arr1 + arr2
#     x.sort()
#     return x


def mergesortedarr(a, b):
    if len(a) == 0 or len(b) == 0:
        return a + b
    mylist = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            mylist.append(a[i])
            i += 1
        elif b[j] < a[i]:
            mylist.append(b[j])
            j += 1
    return mylist + a[i:] + b[j:]


a = [1, 2, 3, 4]
b = [3, 7, 9, 12]
qw = mergesortedarr(a, b)
print(qw)
