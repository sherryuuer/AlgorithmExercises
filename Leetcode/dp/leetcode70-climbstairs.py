# how many ways to climb n stairs
# one time 1 or 2 stairs
n = 2  # output 2


# dp O(n)
def climbStairs(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


res = climbStairs(n)
print(res)


# optimized dp
def climbStairs2(n):
    if n < 2:
        return n
    first, second = 1, 2
    for i in range(3, n + 1):
        second = first + second
        first = second - first
    return second


# 用常数个变量代替长度为n的线性存储结构，使空间复杂度由O(n)降低至O(1)，在提高存储效率的同时执行效率也会得到提升。优化之后我们得到了下面的Python代码。
# 空间复杂度为O(3)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total

        return dp[2]
