# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
# Example 1:
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        results = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # XOR
                result = nums[i] ^ nums[j]
                results.append(result)
        
        return max(results)
# 上述题解消耗太大内存，内存消耗取决于数据结构和算法选择
# 重新题解
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0 
        
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefix_set = set()
            current_max = max_xor | (1 << i)

            for num in nums:
                prefix_set.add(num & mask)
            
            for prefix in prefix_set:
                if (current_max ^ prefix) in prefix_set:
                    max_xor = current_max
                    break
        
        return max_xor










# XOR数字运算实质上是二进制的运算。
# 两个数字的XOR运算是通过对它们的二进制表示执行按位XOR运算来完成的。具体步骤如下：

# 1. 将两个数字转换为二进制表示，确保它们有相同的位数（在需要的情况下，在较短的二进制数前面添加零以匹配较长的二进制数的位数）。
# 2. 对两个二进制数的每一位执行按位XOR运算。按位XOR运算的规则是，如果两个对应位的值相同，结果为0；如果两个对应位的值不同，结果为1。
# 3. 将得到的按位XOR运算结果组合在一起，形成一个新的二进制数。
# 4. 如果需要，将这个新的二进制数转换回十进制形式，以获得XOR运算的最终结果。

# 让我们以一个示例来说明如何计算两个数字的XOR。假设我们要计算XOR(13, 9)。

# 首先，将数字13和9转换为二进制形式：

# - 13的二进制表示为：1101
# - 9的二进制表示为：1001

# 现在，执行按位XOR运算：

# ```
#   1101
# X 1001
# -------
#   0100
# ```

# 按位XOR运算的结果是二进制数0100。最后，将0100转换回十进制，结果是4。

# 所以，XOR(13, 9) = 4。这就是如何计算两个数字的XOR。您可以使用相同的方法来计算任何两个数字的XOR。

# 使用Python的^
# 定义两个数字
# num1 = 13
# num2 = 9

# # 执行XOR运算
# result = num1 ^ num2

# # 打印结果
# print("XOR({0}, {1}) = {2}".format(num1, num2, result))
