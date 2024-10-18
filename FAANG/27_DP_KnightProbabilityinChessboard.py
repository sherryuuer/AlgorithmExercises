# On an n x n chessboard, a knight starts at the cell (row, column)
# attempts to make exactly k moves. The rows and columns are 0-indexed
# n是棋盘大小，k是它要走的步数，已知
n = 3
k = 2
row = 0
column = 0
# Output: 0.06250


directions = [
    [-2, -1], [-2, 1], [2, -1], [2, 1],
    [-1, -2], [-1, 2], [1, -2], [1, 2],
]


def recursive(n, k, row, column):
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0
    if k == 0:  # must check the boundary first
        return 1
    p = 0
    for direction in directions:
        x, y = direction
        p += recursive(n, k - 1, row + x, column + y)
    return p / 8


print(recursive(n, k, row, column))
