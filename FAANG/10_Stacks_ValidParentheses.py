# 有效括号问题
# Determine if a string with only parentheses is valid
# Constrains:
# Will there be any space in the string? No
# Empty string valid? Yes
# stack非常适合对顺序敏感的case


class Solution1:
    def ValidParentheses(self, s):
        if not s:
            return True

        map = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []
        for b in s:
            if b in map.keys():
                stack.append(b)
                continue

            if stack and map.get(stack[-1]) == b:
                stack.pop()
            else:
                return False

        return True if not stack else False


s1 = Solution1()

testCases = [
    ["", True],
    ["{[()]}", True],
    ["{[()", False],
    ["{[(])}", False],
    ["{()[]}", True],
]

for i, case in enumerate(testCases):
    s = case[0]
    res = case[1]
    if s1.ValidParentheses(s) == res:
        print(f"Passed case {i}")
    else:
        print(f"Can't pass case {i}: {case}")
