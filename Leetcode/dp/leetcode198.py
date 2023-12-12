# 打家劫舍
# 递归法，时间复杂度2^n
def rob(nums):
    if len(nums) <= 0:
        return 0
    return max(rob(nums[1:]), nums[0]) + rob(nums[2:])


# 记忆的递归调用，或者自顶向下动态规划
def rob_memo(nums):
    def helper(n, nums, memo):
        if n >= len(nums):
            return 0
        if memo[n] != -1:
            return memo[n]

        memo[n] = max(
            helper(n + 1, nums, memo),
            helper(n + 2, nums, memo) + nums[n]
        )
        return memo[n]

    memo = [-1 for x in range(len(nums) + 1)]
    memo[-1] = 0
    return helper(0, nums, memo)


# 3 dp
def rob_dp(nums):
    if not nums:
        return 0
    memo = [0 for x in range(len(nums) + 1)]
    # 为了避免下面转移方程计算memo[-2]时memo数组溢出
    memo[-2] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        memo[i] = max(memo[i + 1], memo[i + 2] + nums[i])

    return memo[0]


# 空间优化的dp  ? 指针？？
def rob_dp2(nums):
    prev = 0
    curr = 0

    for i in range(len(nums) - 1, -1, -1):
        temp = curr
        curr = max(curr, nums[i] + prev)
        prev = temp

    return curr
