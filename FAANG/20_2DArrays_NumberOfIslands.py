# Constraints:
# Anything out of the edge is water? yes
test1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
]  # 2
test2 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
]  # 7


# prep: rows, cols, visited(set), numOfIslands = 0
# 1, loop the matrix to find a land
# 2, from the land, traversal to mark the island
# helperFunction(row, col, visited) for traversal
# I think it is O(n)
def dfs(matrix, row, col, visited):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    if (row < 0 or row == ROWS or col < 0 or col == COLS
            or (row, col) in visited or matrix[row][col] == 0):
        return

    visited.add((row, col))

    dfs(matrix, row + 1, col, visited)
    dfs(matrix, row - 1, col, visited)
    dfs(matrix, row, col + 1, visited)
    dfs(matrix, row, col - 1, visited)


def numberOfIslands(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    visited = set()
    total = 0
    # loop the matrix
    for r in range(ROWS):
        for c in range(COLS):

            if (matrix[r][c] == 1 and (r, c) not in visited):
                total += 1
                dfs(matrix, r, c, visited)

    return total


print(numberOfIslands(test1))
print(numberOfIslands(test2))


# try bfs
def numberOfIslandsBFS(matrix):
    from collections import deque
    ROWS = len(matrix)
    COLS = len(matrix[0])

    queue = deque()
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    total = 0
    # loop the matrix
    for r in range(ROWS):
        for c in range(COLS):
            if (matrix[r][c] == 1 and (r, c) not in visited):
                queue.append((r, c))
                visited.add((r, c))
                total += 1

                while queue:
                    row, col = queue.popleft()
                    for direction in directions:
                        newRow = row + direction[0]
                        newCol = col + direction[1]

                        if (newRow >= 0 and newRow < ROWS
                            and newCol >= 0 and newCol < COLS
                            and matrix[newRow][newCol] == 1
                                and (newRow, newCol) not in visited):

                            queue.append((newRow, newCol))
                            visited.add((newRow, newCol))

    return total


print(numberOfIslandsBFS(test1))
print(numberOfIslandsBFS(test2))

# Time is O(m x n)
# 但是空间复杂度需要考虑一下：BFS中的queue每次都在弹出所以O(max(m, n))
# 可惜我的visited是会需要空间的，如果按照示例只是将1转换成0就可以剩下这部分空间
# 使用DFS则可能将 Space 增加到 O(m x n)
# 最好的方案，就是使用BFS来进行1和0的转换，从而缩小空间复杂度！这个很难想，但是如果可以补充说明就很好～
# 最后进行时间空间分析是非常好的，进行方案的比较是必有的步骤！
