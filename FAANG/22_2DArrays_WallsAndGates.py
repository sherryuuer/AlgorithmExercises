# Quite interesting
# fill all the inf cell, with the steps that will took to get the door(0), the -1s are walls
# Constraints: must have 0? yes
# just like the #21 question, use BFS to find the shortest step to get the infs
# From where to start is the most important point! not the infs, but the doors!!
# test case:
from collections import deque
case1 = [
    [float('inf'), -1, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -1],
    [float('inf'), -1, float('inf'), -1],
    [0, -1, float('inf'), float('inf')],
]

answer = [
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4],
]


# steps:
# variables: queue, countStep
# step1: loop to find the positions of doors, put them into a queue named doors
# step2: use the queue to perform a bfs, count the steps to get all the infs that can be get
#        if the cell is not -1 and inf update it with countStep
# step3: return matrix


def shortestStepsToDoors(matrix):
    """bfs solution"""
    countSteps = 0
    queue = deque()
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                queue.append((r, c))

    while queue:
        countSteps += 1
        for _ in range(len(queue)):
            curRow, curCol = queue.popleft()

            for direction in directions:
                newRow, newCol = curRow + direction[0], curCol + direction[1]
                # constraint
                if (newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS
                        and matrix[newRow][newCol] != -1 and matrix[newRow][newCol] == float('inf')):
                    matrix[newRow][newCol] = countSteps
                    # put into queue
                    queue.append((newRow, newCol))

    return matrix


print(shortestStepsToDoors(case1) == answer)


# prectice with dfs
# steps:
# 1. loop the matrix, find a door
# 2. --> in the loop perform DFS, countSteps, and update the num, if meet smaller one break the loop
# return matrix
def dfs(matrix, row, col, count):
    if (row < 0 or row >= len(matrix)
        or col < 0 or col >= len(matrix[0])
        or matrix[row][col] == -1
            or matrix[row][col] < count):  # out of boundary, -1, count>cell
        return

    matrix[row][col] = count
    dfs(matrix, row + 1, col, count + 1)
    dfs(matrix, row - 1, col, count + 1)
    dfs(matrix, row, col + 1, count + 1)
    dfs(matrix, row, col - 1, count + 1)


def shortestStepsToDoorsDFS(matrix):

    ROWS, COLS = len(matrix), len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                dfs(matrix, r, c, 0)

    return matrix


print(shortestStepsToDoorsDFS(case1) == answer)
# Time O(m x n) Space O(1)
