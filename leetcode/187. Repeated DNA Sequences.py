# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# 实现步骤：
# 声明结果数组res和map数据结构用来保存每个字符串出现的次数
# 遍历字符串，用下标i
# 开始，用slice截取长度为10的子序列，保存在map中，如果出现过那么次数+1否则次数为1
# 同时判断如果出现次数等于2那么就push到res中

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        map = {}
        for index in range(len(s)-9):
            substr = s[index:index+10]
            if substr not in map:
                map[substr] = 1
            else:
                map[substr] += 1
                if map[substr] == 2:
                    res.append(substr)
        return res
