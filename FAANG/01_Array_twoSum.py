# https://leetcode.com/problems/two-sum/description/

nums = [2, 7, 11, 15]
target = 9


# O(n^2) solution
# 2 pointer way, brute force
class Solution1(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return None

        L = 0
        for L in range(len(nums)):
            for R in range(L + 1, len(nums)):
                if nums[R] == target - nums[L]:
                    return [L, R]
        return None


solution = Solution1()
res = solution.twoSum(nums, target)
print(res)


class Solution2(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return None

        valueIndexMap = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in valueIndexMap:
                return [valueIndexMap[complement], index]
            valueIndexMap[value] = index

        return None

# When we want to find sth, we think about hashmap


solution = Solution2()
res = solution.twoSum(nums, target)
print(res)
