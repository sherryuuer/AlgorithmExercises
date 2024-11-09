## Backtracking
1. has a state tree
2. recursive
3. is Good because has constraints to make the recursive stop early
4. easy to think, sames like a brute force, but more efficient
5. steps:
   - 1-If the current point represents a feasible solution, declare success and terminate the search.
   - 2-If all paths from the current point have been explored (i.e., the current point is a dead-end) without finding a feasible solution, backtrack to the previous point.
   - 3-If the current point is not a dead-end, keep progressing towards the solution, and reiterate all the steps until a solution is found or all possibilities are exhausted.
   - 有几个机制，停止check的if机制，在各种可以更早结束的地方return
   - 在分情况的时候，注意*路径隔离*，我总是处理不好
4. Syntax analysis / Game AI / Pathfinding

**House Robber III**
- tree
- connect node is not allowed
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(25)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)

# a way not work
def backtrack(node, canChoose, curP, maxP): # need a switch
    # constraints
    if not node:
        return maxP

    # choose cur node
    if canChoose:
        maxP = max(maxP, curP + node.data)
        maxP = max(maxP, backtrack(node.left, False, curP + node.data, maxP))
        maxP = max(maxP, backtrack(node.right, False, curP + node.data, maxP))

    maxP = max(maxP, backtrack(node.left, True, curP, maxP))
    maxP = max(maxP, backtrack(node.right, True, curP, maxP))

    return maxP

def rob(root):
    if not root:
        return 0

    return max(backtrack(root, True, 0, 0), backtrack(root, False, 0, 0))


# rewrite: I made things complex
def backtrack(node, canRob):
    if not node:
        return 0

    if canRob:
        robCurrent = node.data + backtrack(node.left, False) + backtrack(node.right, False)
        skipCurrent = backtrack(node.left, True) + backtrack(node.right, True)
        return max(robCurrent, skipCurrent)

    return backtrack(node.left, True) + backtrack(node.right, True)

def rob(root):
    if not root:
        return 0

    return backtrack(root, True)


# add memorization
def backtrack(node, canRob, memo):
    if not node:
        return 0

    state = (node, canRob)
    if state in memo:
        return memo[state]

    if canRob:
        robCurrent = node.data + backtrack(node.left, False, memo) + backtrack(node.right, False, memo)
        skipCurrent = backtrack(node.left, True, memo) + backtrack(node.right, True, memo)
        memo[state] = max(robCurrent, skipCurrent)

    else:
        memo[state] = backtrack(node.left, True, memo) + backtrack(node.right, True, memo)

    return memo[state]

def rob(root):
    if not root:
        return 0
    memo = {}

    return backtrack(root, True, memo)


# dfs way
def rob(root):
    if not root:
        return 0

    def dfs(node): # return [withnode, withoutnode] # time O(n)
        if not node:
            return [0, 0] # space O(n) is the max stack of the recursive

        left = dfs(node.left)
        right = dfs(node.right)

        withnode = node.data + left[1] + right[1]
        withoutnode = max(left[0]) + max(right[0])

        return [withnode, withoutnode]

    return max(dfs(root))
```

## Subsets
- Permutations
- Combinations
- Subsets

### **Letter Combinations of a Phone Number**
```python
def letter_combinations(digits):
    result = []
    if not digits:
        return []

    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    digits = list(str(digits))

    def backtrack(path, result, idxOfDigit):
        if len(path) == len(digits):
            result.append("".join(path))
            return

        lst = mapping[digits[idxOfDigit]]
        for i in range(len(lst)): # time O(k^n x N)
            path.append(lst[i])
            backtrack(path, result, idxOfDigit + 1)
            path.pop()

    path = []
    backtrack(path, result, 0)
    return result # space O(n)
```

### **Generate Parentheses**
```python
def helper(result, string, left, right, n):
    if left == n and right == n:
        result.append(string)
        return

    if left < n:
        helper(result, string + "(", left + 1, right, n)
    if right < left:
        helper(result, string + ")", left, right + 1, n)


def generate_combinations(n):
    result = []
    helper(result, "", 0, 0, n)
    return result
```
