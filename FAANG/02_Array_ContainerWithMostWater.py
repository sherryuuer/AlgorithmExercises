# Does the thickness of the lines affect the area? No
# Does the left side and the right side of the graph counts as a wall? No
# Does a line inside a container affect the area? No


# Test Cases
# or heights: a more abstract name!
bars = [7, 1, 2, 3, 9]
result = [0, 4]  # indices
area = 28  # 7 * 4

bars = [6, 9, 3, 4, 5, 8]
result = [1, 5]  # indices
area = 32

bars = []


# Figure out a solution with code
# T:O(n^2)/S:O(1)
class Solution1(object):
    def containerWithMostWater(self, bars):
        # if there is only one bar, no answer
        if len(bars) <= 1:
            return []
        # from here is the logical part
        # check from the beginning as the first bar, calculate the min area and memorize the indices
        # return the answer
        maxArea = 0
        indices = []

        for idxOfLeft in range(len(bars)):
            for idxOfRight in range(idxOfLeft+1, len(bars)):
                area = min(bars[idxOfLeft], bars[idxOfRight]) * \
                    (idxOfRight - idxOfLeft)
                if area > maxArea:
                    maxArea = area
                    indices = [idxOfLeft, idxOfRight]

        return indices


print(bars)
s1 = Solution1()
print(s1.containerWithMostWater(bars))

# Optimize the solution
# Time: O(n) Space: O(1)
# Because the width is become smaller, I have to find a taller bar to make the area portential bigger
# 这里完全是因为我们要分析这个公式area = min(bars[idxOfLeft], bars[idxOfRight]) * (idxOfRight - idxOfLeft)
# 我们只能通过最大化这其中的两个元素，因为要不断缩小index之间的距离，那么唯一可以扩大面积的，就是尽量让bar更高


class Solution2(object):
    def containerWithMostWater(self, bars):
        if not bars:
            return []

        left = 0
        right = len(bars) - 1
        maxArea = 0
        indices = []

        while left < right:
            print(left, right)
            area = min(bars[left], bars[right]) * (right - left)
            if area > maxArea:
                maxArea = area
                indices = [left, right]

            # move the pointer
            if bars[left] < bars[right]:
                left += 1
            else:
                # 不要慌慢慢确定条件和动作！
                right -= 1

        return indices


print(bars)
s2 = Solution2()
print(s2.containerWithMostWater(bars))
