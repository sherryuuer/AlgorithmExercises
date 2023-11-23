# 四数之和
# 去重
nums = [1, 0, -1, 0, -2, 2]
target = 0
# 暴力法超时 O(n^4)
# 分治
# 四数分为一个数和三数之和，然后三数之和再分为一个数和两数之和。timeO(n^3), spaceO(n)


def findNsum(nums, target, N, tempList, results):
    if len(nums) < N or N < 2:
        return
    # two-sum
    if N == 2:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                results.append(tempList + [nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicated
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    # reduce problems size
    else:
        for i in range(0, len(nums)):
            # skip duplicated
            if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                findNsum(nums[i + 1:], target - nums[i], N -
                         1, tempList + [nums[i]], results)
    return


def fourSum(nums, target):
    nums.sort()
    results = []
    findNsum(nums, target, 4, [], results)
    return results


print(fourSum(nums, target))
