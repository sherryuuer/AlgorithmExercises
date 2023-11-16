# 阶乘factorial(x) = factorial(x-1)


def factorial_recursion(x):
    print(x)
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


def factorial_tail_recursive(n, acc=1):
    print(n, acc)
    if n == 0:
        return acc  # 尾递归使调用发生在最后一行，不需要一层一层取回结果
    else:
        return factorial_tail_recursive(n-1, n*acc)


print(factorial_tail_recursive(5))
