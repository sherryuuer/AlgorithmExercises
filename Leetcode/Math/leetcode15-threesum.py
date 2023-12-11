# 找出三个元素和为0，答案中不可以包含重复的三元组。
# 所以要去重
# 要找到三个数因此遍历到倒数第三个数即可
# 固定i，寻找哦l和r双指针
nums = [-1, 0, 1, 2, -1, -4]


def threesum(nums):
    n = len(nums)
    nums.sort()
    res = []

    for i in range(n - 2):
        # remove deplicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while (left < right):
            if (nums[i] + nums[left] + nums[right] < 0):
                left += 1
            elif (nums[i] + nums[left] + nums[right] > 0):
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])

                # remove deplicat
                while (left < right and nums[left] == nums[left + 1]):
                    left += 1
                while (left < right and nums[right] == nums[right - 1]):
                    right -= 1

                left += 1
                right -= 1
    return res


res = threesum(nums)
print(res)
