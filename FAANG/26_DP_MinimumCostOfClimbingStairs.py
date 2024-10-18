costs = [20, 15, 30, 5]


def recursive(costs):

    def minCost(i):
        if i == 0:
            return costs[0]
        if i == 1:
            return costs[1]
        return costs[i] + min(minCost(i - 1), minCost(i - 2))

    return minCost(len(costs) - 1)


res = recursive(costs)
print(res)


def recursive2(costs):

    cache = [-1] * len(costs)

    def minCost(i, cache):
        if i < 0:
            return 0
        if i < 2:
            return costs[i]
        if cache[i] != -1:
            return cache[i]
        cache[i] = costs[i] + min(minCost(i - 1, cache), minCost(i - 2, cache))
        return cache[i]

    minCost(len(costs) - 1, cache)

    return cache[-1]


res = recursive2(costs)
print(res)


# 感觉递归或者是memorization（递归的优化）都是自顶向下
# 但是动态规划就完全变成了自底向上，是一种思维方式的转变


def memorization(costs):
    """bottom up 优化的第一步
    Time O(n) Space O(n)
    """

    cache = [-1] * len(costs)
    cache[0] = costs[0]
    cache[1] = costs[1]
    i = 2
    while i < len(costs):
        cache[i] = costs[i] + min(cache[i - 1], cache[i - 2])
        i += 1

    return cache[-1]


res = memorization(costs)
print(res)


def dp(costs):
    """
    Time O(n) Space O(1)
    """

    one = costs[0]
    two = costs[1]
    for i in range(2, len(costs)):
        minCost = costs[i] + min(one, two)
        one = two
        two = minCost

    return minCost


res = dp(costs)
print(res)
