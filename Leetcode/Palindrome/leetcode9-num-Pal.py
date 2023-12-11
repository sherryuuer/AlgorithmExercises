# 判断是不是回文数
# 可以转化为字符串后指针法但是，进阶解法是不转化
# 思路是转化为逆数字

# 步骤：
# 1，剔除特殊条件，负数直接否定，0直接肯定，大于0但是最后一位是0直接否定
# 2，设定初始值0
# 3，while循环每次取数字的最后一位作为结果的最高位，同时把数字的最后一位去掉
# 4，比较两个数字

x = 343


def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False

    res = 0
    temp = x
    while temp:
        res = res * 10 + temp % 10
        temp //= 10
    return x == res


answer = isPalindrome(x)
print(answer)
# time O(n) space O(1)
