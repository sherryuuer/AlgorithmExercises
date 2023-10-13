# 斐波那契数列fibonacci(x) = fibonacci(x - 1) * fibonacci(x - 2)
# y 0,1,1,2,3,5,8
# x 0,1,2,3,4,5,6

def fibonacci_recursion(x):
    if x < 2:
        return x
    else:
        return fibonacci_recursion(x - 1) + fibonacci_recursion(x - 2)


def fibonacci_normal(x):
    x1 = 0
    x2 = 1
    answer = 0
    if x < 2:
        return x
    else:  # x from 2
        for i in range(x - 1):
            answer = x1 + x2
            x1 = x2
            x2 = answer
        return answer


def fibonacci_normal_better(index):  # O(n)
    arr = [0, 1]
    for i in range(2, index + 1):
        answer = arr[i - 1] + arr[i - 2]
        arr.append(answer)
    return arr[index]


print(fibonacci_recursion(40))  # O(2^n)
