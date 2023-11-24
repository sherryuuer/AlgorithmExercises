# 分数到循环小数
# 给定分子和分母，输出字符串形式的小数。
# 如果有循环小数，返回形式中循环的部分用括号括起来。
# 结果一定是有理数，也就是有限数或者无限循环小数。
# 开始循环的时候, 说明之前已经出现过这个余数, 我们只要记录前面出现余数的位置,插入括号即可。
# 时间和空间复杂度都是 O(denominator)

numerator = 2
denominator = 3


def _fractionToDecimal(numerator, denominator) -> str:
    if numerator == 0:
        return "0"
    res = []
    # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
    if (numerator > 0) ^ (denominator > 0):
        res.append("-")
    numerator, denominator = abs(numerator), abs(denominator)
    # 判读到底有没有小数
    a, b = divmod(numerator, denominator)
    res.append(str(a))
    # 无小数
    if b == 0:
        return "".join(res)
    res.append(".")
    # 处理余数
    # 把所有出现过的余数记录下来
    loc = {b: len(res)}
    while b:
        b *= 10
        # divmod(20, 3) = (6, 2)
        a, b = divmod(b, denominator)
        res.append(str(a))
        # 余数前面出现过,说明开始循环了,加括号
        if b in loc:
            res.insert(loc[b], "(")
            res.append(")")
            break

        # 再把该位置的记录下来
        loc[b] = len(res)
    return "".join(res)


print(_fractionToDecimal(numerator, denominator))


def fractionToDecimal(numerator, denominator) -> str:
    # 长除法
    n, remainder = divmod(abs(numerator), abs(denominator))
    sign = ''
    if numerator // denominator < 0:
        sign = "-"

    res = [str(n), '.']
    seen = []
    while remainder not in seen:
        seen.append(remainder)
        n, remainder = divmod(abs(remainder * 10), abs(denominator))
        res.append(str(n))
    # when loop
    index = seen.index(remainder)
    res.insert(index + 2, '(')
    res.append(')')
    print(res)

    return sign + ''.join(res)


print(fractionToDecimal(numerator, denominator))
