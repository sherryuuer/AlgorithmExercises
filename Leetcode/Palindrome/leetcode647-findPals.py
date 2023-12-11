# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

# 输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"

# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

# 动态规划
# [i + 1][j - 1]->[i][j]顺序：j从左往右，i从底往上
# i是行，j是列
# 👉              [i][j]
# ⬆️[i + 1][j - 1]


s = "aaa"


def countSub(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    res = 0
    # loop
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - 1 <= 1:  # 两者相邻或者就是同一个位置
                    res += 1
                    dp[i][j] = True
                elif dp[i + 1][j - 1]:  # 不相邻，所以取决于他们之间的串儿是否是回文
                    res += 1
                    dp[i][j] = True
    return res


# 动态规划的简洁写法
def countSub_simple(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    res = 0
    # loop
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            # 此处合并为一条
            if s[i] == s[j] and (j - 1 <= 1 or dp[i + 1][j - 1]):
                res += 1
                dp[i][j] = True
    return res


# 双指针
def countSub_2pointer(s):
    # n = len(s)
    # 中心点一个的时候是i，两个的时候是i和i+1
    def extend(s, i, j, n):
        res = 0
        for i in range(n):
            if i >= 0 and j < n and s[i] == s[j]:
                res += 1
                # go from center to outside
                i -= 1
                j += 1
        return res

    result = 0
    n = len(s)
    for i in range(n):
        result += extend(s, i, i, n)
        result += extend(s, i, i + 1, n)
    return result


answer = countSub(s)
print(answer)
