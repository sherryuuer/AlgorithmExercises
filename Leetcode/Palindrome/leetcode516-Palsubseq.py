# 总之就是动态规划

# 最长回文子序列
# 给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
# 输入："bbbab"
# 输出：4一个可能的最长回文子序列为"bbbb"。
s = 'bbbab'


def longestPalindromeSubseq(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s) - 1, -1, -1):  # i 从下往上，倒着loop
        for j in range(i + 1, len(s)):  # j从左往右， 顺着loop
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][-1]  # 因为是从坐下往右上方递推的，所以只要取右上方的就可以了


answer = longestPalindromeSubseq(s)
print(answer)
