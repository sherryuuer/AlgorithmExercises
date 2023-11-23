# 最接近的三数之和
# 和三数之和很像，但是返回的是最接近三数之和的结果，可能不是target timeO(n^2)
nums = [-1, 2, 1, -4]
target = 1


def threeSumClosest(nums, target):
    n = len(nums)
    if (n < 3):
        return
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        # skip the duplicated
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # fix i, find left and right
        left = i + 1
        right = n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                return s
            if abs(s - target) < abs(res - target):
                res = s

            if s < target:
                left += 1
            elif s > target:
                right -= 1
    return res


print(threeSumClosest(nums, target))
