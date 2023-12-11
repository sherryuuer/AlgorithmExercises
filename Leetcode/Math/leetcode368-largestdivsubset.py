# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对(Si,Sj)都要满足Si % Sj=0或Sj % Si =0。如果有多个目标子集，返回其中任何一个均可。
# 如果存在一个整除子集S及整数x，x能够被S中最大的数整除，那么将x加入S就可以组成一个更大的整除子集。这个其实就是递推公式

nums = [1, 2, 4, 8]


def largestDivisibleSubset(nums):
    S = {-1: set()}
    nums.sort()
    for x in nums:
        temp = []
        for d in S:
            if x % d == 0:
                S[d].add(x)
                temp.append(S[d])
                S[d].remove(x)
        S[x] = max(temp, key=len) | {x}
        print(S)
    return list(max(S.values(), key=len))


largestDivisibleSubset(nums)
