# 如果一个正整数自身是回文数，而且它也是另一个回文数的平方.
# 那么我们称这个数为超级回文数。
# 现在，给定两个正整数L和R（以字符串形式表示），返回包含在范围[L,R]中的,
# 超级回文数的数目。
# 输入：L="4"，R="1000"输出：4
# 解释：4、9、121和484是超级回文数。

# 方法一：暴力遍历 时间复杂度很大，要剪枝
import math


def superpalindromesInRange(L, R):
    cnt = 0

    def validPalindrome(s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    for i in range(math.floor(int(L) ** 0.5), math.ceil(int(R) ** 0.5)):
        if validPalindrome(str(i)) and validPalindrome(str(i ** 2)):
            cnt += 1
    return cnt


L = "4"
R = "1000"
answer = superpalindromesInRange(L, R)
print(answer)


# 方法二：构造回文数，然后只判断它的平方
