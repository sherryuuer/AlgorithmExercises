## Stacks
1. Reverse order processing
2. Nested structures handling
3. State tracking
4. Expression evaluation

- **Valid Parentheses**
```python
def is_valid(s):
    if not s:
        return True

    stack = [] # space O(n)
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for b in s: # time O(n)
        if b in pairs:
            if stack and stack[-1] == pairs.get(b):
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)

    return True if not stack else False
```

## Matrices
1. 2D array input
2. Image Processing
3. Machine Learning

- **Rotate Image**
```python
matrix = [
    [1, 2, 3], # (0, n)->(n, 2)
    [4, 5, 6], # (1, n)->(n, 1)
    [7, 8, 9], # (2, n)->(n, 0)
]
result = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]

# (0, 0)->(0, 2)
# (0, 1)->(1, 2)
# (1, 0)->(0, 1)
def rotate_image(matrix):
    n = len(matrix)
    # space O(n)
    result = [[None for _ in range(n)] for _ in range(n)]
    # time O(n)
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    return result


def rotate_image(matrix):
    n = len(matrix)
    # time O(n)
    for i in range(n):
        for j in range(i, n):
            # 斜角对折
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 横向翻转
    # space O(1)
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix
```
