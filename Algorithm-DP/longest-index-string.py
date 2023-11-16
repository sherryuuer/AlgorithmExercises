# git diff的实现，用动态规划最长公共子序列
def git_diff(file1, file2):
    m = len(file1)
    n = len(file2)

    # 创建一个二维表格，用于存储最长公共子序列的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print("oright form")
    for row in dp:
        print(row)

    # 填充表格也就是具体实现方法
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if file1[i - 1] == file2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print("full form")
    for row in dp:
        print(row)

    # 构造最长公共子序列
    lcs = []  # 用于存储最长公共子序列的列表
    i, j = m, n  # 初始化遍历起点在右下角最大处(7, 5)

    # 从右下角开始回溯，逐步构造最长公共子序列
    while i > 0 and j > 0:
        if file1[i - 1] == file2[j - 1]:
            lcs.insert(0, file1[i - 1])  # 如果字符相等，将字符插入到最前面
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1  # 如果上方的值较大，向上移动
        else:
            j -= 1  # 如果左侧的值较大，向左移动

    return lcs


# 示例
file1 = "ABCBDAB"
file2 = "BDCAB"
result = git_diff(file1, file2)
print("".join(result))
