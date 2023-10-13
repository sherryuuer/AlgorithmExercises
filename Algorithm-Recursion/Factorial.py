# 阶乘factorial(x) = factorial(x-1)


def factorial_recursion(x):
    if x == 0:
        return 1
    else:
        return factorial_recursion(x - 1) * x


def factorial_normal(x):
    y = 1
    if x == 0:
        return 1
    else:
        for i in range(x - 1):
            y = y * x
            x -= 1
        return y


print(factorial_formal(5))
