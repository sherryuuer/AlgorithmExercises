# dp space time O(mn)
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    # print(dp)
    for col in range(1, m):
        for row in range(1, n):
            dp[col][row] = dp[col - 1][row] + dp[col][row - 1]

    return dp[m - 1][n - 1]


res = uniquePaths(7, 3)
print(res)


# 优化dp，将空间复杂度降为n
def uniquePaths2(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]
