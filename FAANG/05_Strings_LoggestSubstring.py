# Find out the loggest substring without repeat characters
# Notice the different of 'substring and subsequence': sequence can have break between them


# Brute force should be find all substring and check them, but I came up with a different one
class Solution1(object):
    def loggestSubstring(self, s):
        if not s:
            return 0
        # track the max length
        maxLenght = 1
        # set left and right point for the substring
        left, right = 0, 0
        # loop from the first to the end
        for i in range(1, len(s)):
            # check if the next is in the [left, right + 1]
            repeat = False
            for j in range(right, left - 1, -1):
                if s[i] == s[j]:
                    # if yes, move the right to next, move the left after the repeat char and update the length
                    left = j + 1
                    right += 1
                    maxLenght = max(maxLenght, right - left + 1)
                    repeat = True
                    break
            # if no, move the right to next and update the lenght
            if repeat:
                continue
            else:
                right += 1
                maxLenght = max(maxLenght, right - left + 1)

        # return the length
        return maxLenght


s1 = Solution1()


# Brute force (the real one? but when search if exsits, I want a hashmap to make it fast)
# Time: O(n^2) Space: O(n)
class Solution2(object):
    def loggestSubstring(self, s):
        if not s:
            return 0

        maxLength = 0
        for i in range(len(s)):
            stringSet = set()
            currLength = 0
            for j in range(i, len(s)):
                if s[j] not in stringSet:
                    stringSet.add(s[j])
                    currLength += 1
                    maxLength = max(maxLength, currLength)
                else:
                    break

        return maxLength


s2 = Solution2()


# Optimize the solution1 with sliding window, and use hashmap to track the index of the value instead of the second loop
class Solution3(object):
    def loggestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        maxLenght = 1
        left = 0
        # hashmap to track the index
        charToIndex = {s[0]: 0, }

        for right in range(1, len(s)):

            # if (s[right] not in charToIndex or charToIndex[s[right]] < left):
            #     charToIndex[s[right]] = right
            # else:
            #     # The code order matters!
            #     left = charToIndex[s[right]] + 1
            #     charToIndex[s[right]] = right

            # right += 1 # with the while solution
            # 这里不需要加一是因为一开始我用的是while的方法进行递增，所以需要right++，因此下面的计算不需要加一
            # maxLenght = max(maxLenght, right - left)

            # better way:
            if (s[right] in charToIndex and charToIndex[s[right]] >= left):
                left = charToIndex[s[right]] + 1

            charToIndex[s[right]] = right
            # 这里使用的是for loop，所以没有right++，因此为了数端点我们要+1！
            maxLenght = max(maxLenght, right - left + 1)

        return maxLenght


s3 = Solution3()


testCases = [
    ["abccabb", 3],
    ["", 0],
    ["abcbda", 4],
    ["ccccccc", 1],
]

for i, testcase in enumerate(testCases):
    string = testcase[0]
    result = testcase[1]
    if s3.loggestSubstring(string) == result:
        print(f"Passed case {i + 1}")
    else:
        print(f"Not pass case {i + 1}: {testcase}")
