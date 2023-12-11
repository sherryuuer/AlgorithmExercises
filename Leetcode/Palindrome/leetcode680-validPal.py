# 判断是否回文的指针思路
def isPalindrome(s, n):
    # n = len(str)
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def mysolution(s, n):
    left = 0
    right = n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if isPalindrome((s[:left] + s[right:]), n - 1) or isPalindrome((s[:left + 1] + s[right + 1:]), n - 1):
                return True
            else:
                False
    return True


s = 'aba'
n = 3
res = mysolution(s, n)
print(res)


def validPalindrome(s):
    n = len(s)

    def isPalindrome(s, i, n):
        # 要去掉的index
        left = 0
        right = n - 1
        while left < right:
            if left == i:
                left += 1
            elif right == i:
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    left = 0
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            return isPalindrome(s, left, n) or isPalindrome(s, right, n)
        left += 1
        right -= 1
    return True
