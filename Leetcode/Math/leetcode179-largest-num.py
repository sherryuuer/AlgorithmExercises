# 最大数
# 给定一组非负整数，找出组合后的最大整数
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
from functools import cmp_to_key
nums = [3, 30, 34, 5, 9]


def largestNumber(nums):
    s = [str(i) for i in nums]

    def comp(a, b):
        if (a + b) > (b + a):
            return 1
        if (a + b) < (b + a):
            return -1
        return 0

    s.sort(reverse=True, key=cmp_to_key(comp))

    return str(int(''.join(s)))


print(largestNumber(nums))
