# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意： 答案中不可以包含重复的三元组。

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]


# 使用哈希表去重细节太复杂所以不推介
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         nums.sort()
#         # 找出a + b + c = 0
#         # a = nums[i], b = nums[j], c = -(a + b)
#         for i in range(len(nums)):
#             # 排序之后如果第一个元素已经大于零，那么不可能凑成三元组
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i - 1]: #三元组元素a去重
#                 continue
#             d = {}
#             for j in range(i + 1, len(nums)):
#                 if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]: # 三元组元素b去重
#                     continue
#                 c = 0 - (nums[i] + nums[j])
#                 if c in d:
#                     result.append([nums[i], nums[j], c])
#                     d.pop(c) # 三元组元素c去重
#                 else:
#                     d[nums[j]] = j
#         return result

# 双指针check
class Solution:
    def threeSum(self, nums):
        result = []  # abc
        nums.sort()

        # 遍历
        for i in range(len(nums)):
            # 如果第一个i就大于零那么直接break结束
            if nums[i] > 0:
                return result
            # 如果i大于0并且每个数字和前一个数字相等，continue为了去重a
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 定义左右指针
            left = i + 1
            right = len(nums) - 1
            # sum = nums[i] + nums[left] + nums[right]
            # 当右边指针大于左边指针就可以满足while条件
            while right > left:
                # 左指针和右指针调整。i和左和右数字相加为0就满足条件 
                sum = nums[i] + nums[left] + nums[right]  # 写错行    
                # 当sum大于零右指针向左移动一格
                if sum > 0:
                    right -= 1
                # 当sum小于零左指针向右移动一格
                elif sum < 0:
                    left += 1
                # 其他就是等于零，于是推入result
                else:
                    result.append([nums[i], nums[left], nums[right]])
                # 对左右指针进行去重并且移动
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    # 移动窗口
                    left += 1
                    right -= 1

        # 返回结果
        return result


# numslist = [-1, 0, 1, 2, -1, -4]
numslist = [1, -1, -1, 0]
solution = Solution()
res = solution.threeSum(numslist)
print(res)
