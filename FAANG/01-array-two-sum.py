# https://leetcode.com/problems/two-sum/description/

# Are the nums all positive?
# Are there any duplicates?
# edge case? []case? one element case? Does it have sollution?
# What do I return when no solution? None?
# The solution is only one pair?
# write some test case.


nums = [2, 7, 11, 15]
target = 9


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = 0
        for L in range(len(nums)):
            for R in range(L + 1, len(nums)):
                if nums[R] == target - nums[L]:
                    return [L, R]
        return None


solution = Solution()
res = solution.twoSum(nums, target)
print(res)
