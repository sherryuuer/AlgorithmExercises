# 最长公共子串
def find_longest_common_substring(file1, file2):
    m = len(file1)
    n = len(file2)

    # 创建一个二维表格，用于存储最长公共子串的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 记录最长公共子串的长度及其结束位置
    max_length = 0
    end_position = 0

    # 填充表格
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if file1[i - 1] == file2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i - 1  # 记录最长公共子串的结束位置
            else:
                dp[i][j] = 0  # 如果字符不匹配，重新开始计数

    # 根据最长公共子串的长度和结束位置，提取最长公共子串
    longest_common_substring = file1[end_position - max_length + 1: end_position + 1]

    return longest_common_substring


# 示例
file1 = "ABCBDAB"
file2 = "BBDAB"
result = find_longest_common_substring(file1, file2)
print(result)

