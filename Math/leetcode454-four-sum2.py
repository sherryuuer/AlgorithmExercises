# 四数相加
# 给定四个包含整数的数组列表A，B，C，D，计算有多少个元组(i,j,k,l)使得A[i]+B[j]+C[k]+D[l]=0
# 为了使问题简化，所有的数组列表具有相同的长度n，且0<=n<=500，所有整数范围在-228到228-1之间，最终结果不会超过2^31-1
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]

# output shoud be 2 (0, 0, 0, 1) and (1, 1, 0, 0)
# 固定两个元素找另外两个时间复杂度为O(n^2)


def fourSumCount(A, B, C, D):
    mapper = {}
    res = 0
    for i in A:
        for j in B:
            mapper[i + j] = mapper.get(i + j, 0) + 1
    for i in C:
        for j in D:
            res += mapper.get(-1 + (i + j), 0)
    return res


print(fourSumCount(A, B, C, D))
