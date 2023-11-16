# 将一块mxn的长方形田地，尽可能多地分成小的正方形
# 本质是求长宽的最大公约数，可以用欧几里得算法
# 这里使用分而治之递归算法
def square(length, width):
    if length != width:
        # 如果长宽不相等，持续辗转相减
        length = length - width
        [length, width] = square(max(length, width), min(length, width))
        return [length, width]
        # 尾递归？
    else:
        return [length, width]


print(square(180, 60))
print(square(1680, 640))

# 分而治之是自上而下，动态规划是自下而上？
