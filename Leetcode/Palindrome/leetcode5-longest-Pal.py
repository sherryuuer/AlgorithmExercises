# 给你一个字符串 s，找到 s 中最长的回文子串。
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
s = "babad"


# 双指针，中心扩展法
def longestPal(s):
    n = len(s)
    if n == 0:
        return ""
    res = s[0]

    def extend(s, i, j, n):
        for i in range(n):
            if i >= 0 and j < n and s[i] == s[j]:
                # go from center to outside
                i -= 1
                j += 1
        return s[i + 1: j]

    for i in range(n - 1):
        e1 = extend(s, i, i, n)
        e2 = extend(s, i, i + 1, n)

        if max(len(e1), len(e2)) > len(res):
            res = e1 if len(e1) > len(e2) else e2
    return res


answer = longestPal(s)
print(answer)
