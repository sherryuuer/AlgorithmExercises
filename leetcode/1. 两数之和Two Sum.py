# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res = {}
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 res[(i, j)] = nums[i] + nums[j]
#                 if res[(i, j)] == target:
#                     print(list((i, j)))
# 上述复杂度太高        

# 为什么会想到用哈希表
# 哈希表为什么用map
# 本题map是用来存什么的
# map中的key和value用来存什么的
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashtable = {}
#         for i, v in enumerate(nums):
#             hashtable[v] = i
#         for key in hashtable:
#             if (target - key) in hashtable:
#                 return [hashtable[key], hashtable[target-key]]
# xxxxxxx
# key用来存储值，值用来存储index

nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    hashtable = {}  # {value : index,}
    for i, v in enumerate(nums):
        if target - v in hashtable:
            return [hashtable[target - v], i]
        hashtable[v] = i
    return []


print(twoSum(nums, target))
