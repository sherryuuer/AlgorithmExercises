# 两数之和
nums = [2, 7, 11, 15]
target = 9


# 解法1，排序＋双指针，不可取，因为索引被打乱了 O(nlogn)
def twosum_pointer(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
    return []


# 解法2，空间换时间 O(n)
def twosum_spacetotime(nums, target):
    mapper = {}
    for i in range(len(nums)):
        if target - nums[i] in mapper:
            return [mapper[target - nums[i]], i]
        else:
            mapper[nums[i]] = i
    return []


res = twosum_spacetotime(nums, target)
print(res)
