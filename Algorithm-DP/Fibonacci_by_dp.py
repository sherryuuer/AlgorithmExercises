# 斐波那契数列fibonacci(x) = fibonacci(x - 1) * fibonacci(x - 2)
# y 0,1,1,2,3,5,8
# x 0,1,2,3,4,5,6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...
import time


def fibonacci(x):  # O(2^n)
    if x < 2:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


def fibonacciMaster():  # O(n)
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]
    return fib


# Bottom-Up
def fibonacciMaster2(index):  # O(n)
    arr = [0, 1]
    for i in range(2, index + 1):
        answer = arr[i - 1] + arr[i - 2]
        arr.append(answer)
    return arr[index]


fasterFib = fibonacciMaster()

time1 = time.time()
print('Slow', fibonacci(35))
time2 = time.time()
timefib = time2 - time1
print(timefib)

time1 = time.time()
print('DP', fasterFib(35))
time2 = time.time()
timedp1 = time2 - time1
print(timedp1)

time1 = time.time()
print('DP2', fibonacciMaster2(35))
time2 = time.time()
timedp2 = time2 - time1
print(timedp2)
