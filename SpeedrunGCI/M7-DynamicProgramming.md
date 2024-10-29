- Top-down approach: recursive -> memoization
- Bottom-up approach: iterative

1. Overlapping subproblems
2. Optimal substructure

**Coin Change**
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
