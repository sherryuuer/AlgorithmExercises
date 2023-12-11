# 最大连续子序列的和
# 子数组连续，不返回位置只返回和
# 数组中元素是整数，正数，负数，和零
# 子序列的最小长度是1
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Input: nums = [5,4,-1,7,8]
# Output: 23
nums = [5, 4, -1, 7, 8]


# 暴力法超时风险 timeO(n^2) spaceO(1)
def _maxSubArray(nums):
    n = len(nums)
    maxSum = float("-inf")
    total = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            maxSum = max(maxSum, total)
    return maxSum


# 分治法 timeO(nlogn) spaceO(logn)
def helper(nums, left, right):
    if left > right:
        return float("-inf")
    mid = (left + right) // 2
    left_sum = helper(nums, left, mid - 1)
    right_sum = helper(nums, mid + 1, right)
    left_suffix_max_sum = right_prefix_max_sum = 0
    total = 0
    for i in reversed(range(left, mid)):
        total += nums[i]
        left_suffix_max_sum = max(left_suffix_max_sum, total)
    total = 0
    for i in range(mid + 1, right + 1):
        total += nums[i]
        right_prefix_max_sum = max(right_prefix_max_sum, total)
    cross_max_sum = left_suffix_max_sum + right_prefix_max_sum + nums[mid]
    return max(cross_max_sum, left_sum, right_sum)


def maxSubArray(nums):
    return helper(nums, 0, len(nums) - 1)


print(maxSubArray(nums))


# 动态规划法, 贪心Q(list,i)=max(0,Q(list,i-1))+nums[i] timeO(n), spaceO(1)
def maxSubArray_dp(nums):
    n = len(nums)
    max_sum_ending_curr_index = max_sum = nums[0]
    for i in range(1, n):
        max_sum_ending_curr_index = max(
            max_sum_ending_curr_index + nums[i], nums[i])
        max_sum = max(max_sum_ending_curr_index, max_sum)
    return max_sum


print(maxSubArray_dp(nums))

# 前缀和 time O(n) space O(1)
# 是一种数学方法


def maxSubArray_minsum(nums):
    n = len(nums)
    maxSum = nums[0]
    minSum = sum = 0
    for i in range(n):
        sum += nums[i]
        maxSum = max(maxSum, sum - minSum)
        minSum = min(minSum, sum)
    return maxSum


print(maxSubArray_minsum(nums))
