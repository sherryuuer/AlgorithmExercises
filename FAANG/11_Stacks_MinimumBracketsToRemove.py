# Give a string with only lower characters or '('')', remove the minimum number of brackets so that the string is valid
# Constraints:
# What we will return? valid string with minimum nums of brackets been removed
# Is there any space in the string? No
# No brackets in the string is valid? Yes


# 我觉得本质上还是用stack的方法，针对括号进行处理
# 以下几种情况
# 初始化一个stack存放备用括号，的index和括号，一种是废物括号，一种是待用括号
# loop并判断情况
# 1，如果是char直接跳过
# 2，如果是没法配对的右边括号，append（会影响后面的右括号配对左边括号吗，不会，因为左边括号一定会被右边的消除或者在最后留下来）
# 3，如果是配对的，直接pop，反之append
# 最后将stack中的index上的括号都删除


class Solution1:
    def MinimumBracketsToRemove(self, s):
        if not s:
            return ""

        stack = []
        for idx, char in enumerate(s):

            if char == '(':
                stack.append(idx)

            if char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(idx)

        return ''.join([char for i, char in enumerate(s) if i not in stack])


testCases = [
    "a)b(cd)", "(ab(c)d", "))((",
]


s1 = Solution1()
# print(s1.MinimumBracketsToRemove("a)b(cd)"))


# Another way: turn the string into a list and modify the elements
class Solution2:
    def MinimumBracketsToRemove(self, s):
        if not s:
            return ""

        s = list(s)
        stack = []

        for idx, char in enumerate(s):

            if char == '(':
                stack.append(idx)

            if char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    s[idx] = ""

        for idx in stack:
            s[idx] = ""

        return ''.join(s)


s2 = Solution2()
for case in testCases:
    print(s2.MinimumBracketsToRemove(case))
