profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8


def knapsack01_recursive(weight, profit, capacity, index):
    """
    0/1 knapsack brute force way
    """
    if index == len(profit) or capacity <= 0:
        return 0

    # skip the unvalid capacity
    if weight[index] > capacity:
        return knapsack01_recursive(weight, profit, capacity, index + 1)

    # not choose the current item
    not_choose = knapsack01_recursive(weight, profit, capacity, index + 1)

    # choose the current item
    choose = profit[index] + \
        knapsack01_recursive(weight, profit, capacity -
                             weight[index], index + 1)

    return max(not_choose, choose)


def knapsack01_dfs(weight, profit, capacity, index):
    if index == len(profit):
        return 0

    # not choose
    maxProfit = knapsack01_dfs(weight, profit, capacity, index + 1)
    # choose
    newCapacity = capacity - weight[index]
    if newCapacity >= 0:
        p = profit[index] + \
            knapsack01_dfs(weight, profit, newCapacity, index + 1)
        maxProfit = max(maxProfit, p)

    return maxProfit


def knapsack01_memorization(weight, profit, capacity):
    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]

    def memorization(index, capacity):
        if index == len(profit):
            return 0
        if cache[index][capacity] != -1:
            return cache[index][capacity]

        # not choose
        cache[index][capacity] = memorization(index + 1, capacity)

        # choose
        newCapacity = capacity - weight[index]
        if newCapacity >= 0:
            p = profit[index] + memorization(index + 1, newCapacity)
            cache[index][capacity] = max(cache[index][capacity], p)

        return cache[index][capacity]

    return memorization(0, capacity)


s1 = "ADCB"
s2 = "ABC"


def longest_common_subsequence_return_length(s1, s2):
    """
    return the length of lcs
    brute force dfs way
    """
    def dfs(s1, s2, l1, l2):
        if l1 == len(s1) or l2 == len(s2):
            return 0

        if s1[l1] == s2[l2]:
            return 1 + dfs(s1, s2, l1 + 1, l2 + 1)
        return max(dfs(s1, s2, l1 + 1, l2),
                   dfs(s1, s2, l1, l2 + 1))
    return dfs(s1, s2, 0, 0)


def longest_common_subsequence_return_array(s1, s2):
    """
    return the array of lcs
    brute force dfs way
    """

    def dfs(s1, s2, l1, l2):
        if l1 == len(s1) or l2 == len(s2):
            return ""

        if s1[l1] == s2[l2]:
            return s1[l1] + dfs(s1, s2, l1 + 1, l2 + 1)

        string1 = dfs(s1, s2, l1 + 1, l2)
        string2 = dfs(s1, s2, l1, l2 + 1)

        return string1 if len(string1) > len(string2) else string2

    return dfs(s1, s2, 0, 0)


def lcs_memorization_way_return_array(s1, s2):
    """
    longest common subsequence
    memorization way
    return the array of lcs
    brute force dfs way
    """
    N, M = len(s1), len(s2)
    cache = [[-1 for _ in range(M)] for _ in range(N)]

    def dfs(s1, s2, l1, l2, cache):
        if l1 == len(s1) or l2 == len(s2):
            return ""
        if cache[l1][l2] != -1:
            return cache[l1][l2]

        if s1[l1] == s2[l2]:
            cache[l1][l2] = s1[l1] + dfs(s1, s2, l1 + 1, l2 + 1, cache)
        else:
            string1 = dfs(s1, s2, l1 + 1, l2, cache)
            string2 = dfs(s1, s2, l1, l2 + 1, cache)
            cache[l1][l2] = string1 if len(string1) > len(string2) else string2
        return cache[l1][l2]

    return dfs(s1, s2, 0, 0, cache)


def lcs_memorization_return_length(s1, s2):
    """
    return the length of lcs
    memorization way
    """
    N, M = len(s1), len(s2)
    cache = [[-1 for _ in range(M)] for _ in range(N)]

    def dfs(s1, s2, l1, l2, cache):
        if l1 == len(s1) or l2 == len(s2):
            return 0
        if cache[l1][l2] != -1:
            return cache[l1][l2]

        if s1[l1] == s2[l2]:
            cache[l1][l2] = 1 + dfs(s1, s2, l1 + 1, l2 + 1, cache)
        else:
            length1 = dfs(s1, s2, l1 + 1, l2, cache)
            length2 = dfs(s1, s2, l1, l2 + 1, cache)
            cache[l1][l2] = length1 if length1 > length2 else length2

        return cache[l1][l2]

    return dfs(s1, s2, 0, 0, cache)


s = "abaab"


def longest_palindrome_1(s):
    if not s:
        return 0

    length = 0
    for i in range(len(s)):
        # odd
        L, R = i, i
        while L >= 0 and R < len(s) and s[L] == s[R]:
            length = max(R - L + 1, length)
            L -= 1
            R += 1

        # even
        L, R = i, i + 1
        while L >= 0 and R < len(s) and s[L] == s[R]:
            length = max(R - L + 1, length)
            L -= 1
            R += 1
    return length


def longest_palindrome_2(s):
    if not s:
        return 0

    def helper(L, R, maxlength):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            maxlength = max(R - L + 1, maxlength)
            L -= 1
            R += 1
        return maxlength

    length = 0
    for i in range(len(s)):
        # odd
        length = helper(i, i, length)
        # even
        length = helper(i, i + 1, length)
    return length


print([[-1 for _ in 3] for _ in 4])
# print(longest_palindrome_1(s))
# print(longest_palindrome_2(s))
# print(lcs_memorization_return_length(s1, s2))
# print(lcs_memorization_way_return_array(s1, s2))
# print(knapsack01_dfs(weight, profit, capacity, 0))
# print(knapsack01_memorization(weight, profit, capacity))
# print(knapsack_recursive(weight, profit, capacity, 0))
