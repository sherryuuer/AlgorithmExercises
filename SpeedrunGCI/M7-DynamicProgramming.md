- Top-down approach: recursive -> memoization
- Bottom-up approach: iterative

1. Overlapping subproblems
2. Optimal substructure

### **Coin Change**
```python
def coin_change(coins, total):
    count = 0
    if total == 0:
        return 0

    cache = {} # space O(total)

    def add_coin(remaining):
        if remaining == 0:
            return 0

        if remaining < 0:
            return float('inf')

        if remaining in cache:
            return cache[remaining]

        minCount = float('inf')

        for i in range(len(coins)): # time O(len(coins) * total) -> O(m * n)
            count = add_coin(remaining - coins[i])
            if count != float('inf'):
                minCount = min(minCount, count + 1)

        cache[remaining] = minCount

        return cache[remaining]

    result = add_coin(total)
    return result if result != float('inf') else -1
```

### **House Robber II**
```python
def house_robber(money):
    """brute force dfs"""
    maxProfit = 0
    if not money:
        return maxProfit

    def dfs(index, limit):
        if index >= limit:
            return 0

        # rob current
        maxProfit = money[index] + dfs(index + 2, limit)
        # not rob current
        maxProfit = max(dfs(index + 1, limit), maxProfit)

        return maxProfit

    return max(dfs(0, len(money) - 1), dfs(1, len(money)))


def house_robber(money):
    """memorization way"""
    if not money:
        return 0
    if len(money) == 1:
        return money[0]

    def helper(index, limit, cache):
        if index >= limit:
            return 0
        if cache[index] != -1:
            return cache[index]

        # rob current
        rob = money[index] + helper(index + 2, limit, cache)
        # not rob current
        not_rob = helper(index + 1, limit, cache)
        cache[index] = max(rob, not_rob)

        return cache[index] # space O(n)

    return max(helper(0, len(money) - 1, [-1] * len(money)), helper(1, len(money), [-1] * len(money)))


def house_robber(money):
    """dp"""
    if not money:
        return 0
    if len(money) == 1:
        return money[0]

    def helper(array):
        rob1, rob2 = 0, 0
        for n in array:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2

    return max(helper(money[1:]), helper(money[:-1]))
```

### **House Robber**
```python
def rob_houses(nums):
    if not nums:
        return 0

    rob1, rob2 = 0, 0
    for n in nums:
        new_rob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = new_rob
    return rob2
```

### **Climbing Stairs**
```python
def climb_stairs(nums):
    """brute force"""
    if nums <= 2:
        return nums

    def dfs(index):
        if index == nums:
            return 1
        if index > nums:
            return 0

        return dfs(index + 1) + dfs(index + 2)

    return dfs(0)

def climb_stairs(nums):
    """memorization"""
    if nums <= 2:
        return nums

    cache = [-1] * nums

    def cacher(index):
        if index == nums:
            return 1
        if index > nums:
            return 0
        if cache[index] != -1:
            return cache[index]

        cache[index] = (
            cacher(index + 1) + cacher(index + 2)
        )
        return cache[index]

    return cacher(0)
```
- memorization本质还是一种自顶向下，只是用cache优化了查找。

```python
def climb_stairs(nums):
    """dp"""
    if nums <= 2:
        return nums

    step1, step2 = 1, 2
    for n in range(3, nums + 1):
        temp = step1 + step2
        step1 = step2
        step2 = temp

    return step2

```

**Combination Sum**
```python
def combination_sum(nums, target):
    """
    backtracking the brute force way
    """
    if not nums:
        return []

    result = []
    def backtrack(i, path, cur_sum):
        if cur_sum > target or i >= len(nums):
            return
        if cur_sum == target:
            result.append(path[:])
            return

        # choose the current num
        path.append(nums[i])
        cur_sum += nums[i]
        backtrack(i, path, cur_sum)

        # not choose the current num
        path.pop()
        cur_sum -= nums[i]
        backtrack(i + 1, path, cur_sum)

    backtrack(0, [], 0)
    return result

# test [3] target = 3
# [2, ] 2
# 我感觉dp很难理解可能是因为嵌套array的缘故
```

### **Unique Paths**
```python
def unique_paths(m, n):
    """
    brute force, backtracking way
    """
    if m == 1 or n == 1:
        return 1

    def find_path(row, col):
        if row >= m or col >= n:
            return 0
        if row == m - 1 and col == n - 1:
            return 1

        return find_path(row + 1, col) + find_path(row, col + 1)

    return find_path(0, 0)


def unique_paths(m, n):
    """
    memorization way
    """
    if m == 1 or n == 1:
        return 1

    cache = [[-1 for _ in range(n)] for _ in range(m)]

    def helper(row, col):
        if row >= m or col >= n:
            return 0
        if row == m - 1 and col == n - 1:
            return 1
        if cache[row][col] != -1:
            return cache[row][col]

        cache[row][col] = helper(row + 1, col) + helper(row, col + 1)
        return cache[row][col]

    return helper(0, 0)


def unique_paths(m, n):
    """dp"""
    if m == 1 or n == 1:
        return 1

    dp = [1 for _ in range(n)]
    for row in range(m - 2, -1, -1):
        dp_above = [0 for _ in range(n)]
        dp_above[n - 1] = 1
        for col in range(n - 2, -1, -1):
            dp_above[col] = dp_above[col + 1] + dp[col]

        dp = dp_above

    return dp[0]

# m = 3, n = 2
# [
#     [3, 1]
#     [2, 1]
#     [1, 1]
# ]
```
