# 1. Valid Palindrome is a easy one
class Solution1(object):
    def validPalindrome(self, s):
        import re
        s = re.sub(r'[^a-zA-Z]', '', s).lower()

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


s1 = Solution1()

testCases = [
    ["acbca", True],
    ["acbbca", True],
    ["abc", False],
    ["a", True],
    ["", True],
    ["A man, a plan, a canal: Panama", True],
]

# Almost palindrome problem, by remove on character, will it become a palindrome?
# Verify some constraints:
# Do we consider a palindrome as a almost palindrome? yes


class Solution2(object):
    def almostPalindrome(self, s):
        import re
        s = re.sub(r'[^a-zA-Z]', '', s).lower()
        left = 0
        right = len(s) - 1

        removed = False
        while left <= right:

            if s[left] != s[right]:
                if removed:
                    return False

                if s[left + 1] == s[right]:
                    left += 1
                    removed = True
                elif s[left] == s[right - 1]:
                    right -= 1
                    removed = True
                else:
                    return False

            left += 1
            right -= 1

        return True


s2 = Solution2()


testCases = [
    ["race a car", True],
    ["abccdba", True],
    ["abcdefdba", False],
    ["a", True],
    ["", True],
    ["ab", True],
]


for index, testcase in enumerate(testCases):
    s = testcase[0]
    result = testcase[1]
    if s2.almostPalindrome(s) == result:
        print(f"Passed the case {index + 1}")
    else:
        print(f"Can't passed the case {index + 1}: {testcase}")


# 虽然上面的方法OK，但是我还是觉得用子问题分解比较好，在移除一个字母后判断子问题比较resonable
# Time O(n) Space O(1)
class Solution3(object):
    def almostPalindrome(self, s):
        import re
        s = re.sub(r'[^a-zA-Z]', '', s).lower()

        def validPalindrome(s, left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left <= right:

            if s[left] != s[right]:
                return validPalindrome(s, left + 1, right) or validPalindrome(s, left, right - 1)

            left += 1
            right -= 1

        return True


s3 = Solution3()


testCases = [
    ["race a car", True],
    ["abccdba", True],
    ["abcdefdba", False],
    ["a", True],
    ["", True],
    ["ab", True],
]


for index, testcase in enumerate(testCases):
    s = testcase[0]
    result = testcase[1]
    if s3.almostPalindrome(s) == result:
        print(f"Passed the case {index + 1}")
    else:
        print(f"Can't passed the case {index + 1}: {testcase}")
