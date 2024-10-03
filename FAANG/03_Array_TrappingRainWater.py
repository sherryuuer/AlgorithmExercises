# Constraints
# Does the left and right side of the graph count as a walls? No
# Will there be any integers be negative? No

# Figure out a solution without code
# https://leetcode.com/problems/trapping-rain-water/description/

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6


# Brute force
# try be myself and totally not right ...... no meaning
# 1. Need to get left side highest and right side highest
# 2. Must find the first left side highest
# 3. Move on to find the right side highest
# 4. calculate the area and add to total
# 5. change the left side highest to the position of right side highest, and do this again
# 6. Until the length of the array
class Solution1(object):
    def trap(self, height):
        if len(height) <= 2:
            return 0

        leftHigh, rightHigh = 0, 0
        total = 0
        left = right = 0

        while right < len(height):
            while left < len(height):
                if height[left] > height[left + 1]:
                    leftHigh = left
                    break
                left += 1

            right = left + 1

            while right < len(height) - 1:
                if height[right + 1] < height[right]:
                    rightHigh = right
                    break
                right += 1

            blocks = 0
            for i in range(leftHigh+1, rightHigh):
                blocks += height[i]
            total = total + (min(height[leftHigh], height[rightHigh]) - blocks)

            left = rightHigh

        return total


# s1 = Solution1()
# print(s1.trap(height))


# Brute force
# Get the true fomula, 要找到每一个点的暴力破解计算的公式： currentWater = min(maxL, maxR) - current
# Only if you understand the logic totally, you finally can code it right
# Then we loop
class Solution2(object):
    def trap(self, height):
        total = 0

        for index in range(len(height)):

            current = height[index]
            maxL, maxR = 0, 0
            left = right = index

            # Get the maxL and maxR at every point
            while left >= 0:
                maxL = max(height[left], maxL)
                left -= 1
            while right < len(height):
                maxR = max(height[right], maxR)
                right += 1

            currentWater = min(maxL, maxR) - current
            total += (currentWater if currentWater > 0 else 0)

        return total


s2 = Solution2()
print(s2.trap(height))


# Optimize Version
# Two-Pointer，left => right, Get a lower bar and decide update the max or calculate the water
# 一边更新最大一边计算，所以两边的point，负担两个责任，一个是更新最大，一个是更新水量
# 因为公式来说，需要的是最小的柱子，只需要和自己身边的柱子比较大小然后计算水量，这很trick！
class Solution3(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        maxL = 0
        maxR = 0
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    total += maxL - height[left]
                left += 1

            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    total += maxR - height[right]
                right -= 1

        return total


testcases = [
    [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6],
    [[], 0],
    [[1, 2, 1], 0],
]
s3 = Solution3()
for testcase in testcases:
    if s3.trap(testcase[0]) == testcase[1]:
        print(f"pass with {testcase}")
