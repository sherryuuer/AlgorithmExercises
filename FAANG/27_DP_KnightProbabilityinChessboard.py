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


def memorization(n, k, row, column):
    cache = [[[None for _ in range(n)] for _ in range(n)]
             for _ in range(k + 1)]
    return helper(n, k, row, column, cache)


def helper(n, k, row, column, cache):
    """T/S O(N^2*K)"""
    # check result no need to be store in the dp
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0
    if k == 0:  # must check the boundary first
        return 1
    if cache[k][row][column] is not None:
        return cache[k][row][column]

    p = 0
    for direction in directions:
        x, y = direction
        p += helper(n, k - 1, row + x, column + y, cache) / 8
    # store the p result
    cache[k][row][column] = p
    return cache[k][row][column]


print(memorization(n, k, row, column))


def dp_solution(n, k, start_row, start_column):
    # Initialize the 3D DP array
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]

    # Base case: when k == 0, the probability is 1 at the start position
    dp[0][start_row][start_column] = 1

    # Possible directions of movement (8 directions)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Fill the DP table
    for moves in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                # Update dp for each cell by looking at all 8 possible previous cells
                for x, y in directions:
                    prev_row, prev_col = row + x, col + y
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        dp[moves][row][col] += (dp[moves - 1]
                                                [prev_row][prev_col] / 8)

    # Total probability after k moves is the sum of probabilities across all possible positions
    total_probability = 0
    for row in range(n):
        for col in range(n):
            total_probability += dp[k][row][col]

    return total_probability


def dp_optimized(n, k, start_row, start_column):
    # Initialize two 2D DP grids for current and previous states
    prev_dp = [[0 for _ in range(n)] for _ in range(n)]
    curr_dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: when k == 0, the probability is 1 at the start position
    prev_dp[start_row][start_column] = 1

    # Possible directions of movement (8 directions)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Fill the DP table for each move
    for moves in range(1, k + 1):
        # Reset current dp grid for the new move
        curr_dp = [[0 for _ in range(n)] for _ in range(n)]

        for row in range(n):
            for col in range(n):
                # Update dp for each cell by looking at all 8 possible previous cells
                for x, y in directions:
                    prev_row, prev_col = row + x, col + y
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        curr_dp[row][col] += prev_dp[prev_row][prev_col] / 8

        # After processing, current dp becomes the previous dp for the next iteration
        prev_dp = curr_dp

    # Total probability after k moves is the sum of probabilities across all possible positions
    total_probability = 0
    for row in range(n):
        for col in range(n):
            total_probability += prev_dp[row][col]

    return total_probability

# https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns
