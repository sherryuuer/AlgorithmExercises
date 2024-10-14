# traversal all elements in a 2d array
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]


def dfsTraversal(matrix):
    """Get all elements from matrix"""
    ROWS = len(matrix)
    COLS = len(matrix[0])

    def dfs(matrix, row, col, result, visited):
        # boundary
        if (row == ROWS or col == COLS
                or row < 0 or col < 0
                or (row, col) in visited):
            return

        result.append(matrix[row][col])
        visited.add((row, col))
        # directions
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # traversal
        for direction in directions:
            dfs(matrix, row + direction[0],
                col + direction[1], result, visited)

    result = []
    visited = set()
    dfs(matrix, 0, 0, result, visited)
    return result


print(dfsTraversal(matrix))


def bfsTraversal(matrix):
    """
    Get all the elements from the matrix
    Time and Space are all O(n)
    """
    ROWS = len(matrix)
    COLS = len(matrix[0])
    from collections import deque
    visited = set()
    result = []
    queue = deque()

    queue.append((0, 0))
    visited.add((0, 0))

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        # length = len(queue)
        # for i in range(length):
        # I dont need to do for loop, because in this case, what matters is just the elements, not the depth
        # this is like batch processing! intresting~
        row, col = queue.popleft()
        result.append(matrix[row][col])

        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]

            if (newRow >= 0 and newRow < ROWS
                and newCol >= 0 and newCol < COLS
                    and (newRow, newCol) not in visited):

                queue.append((newRow, newCol))
                visited.add((newRow, newCol))

    return result


print(bfsTraversal(matrix))
