# Constraints:
# if there are no oranges, return 0
# if it is not possiable to rot them all return -1
# test cases:
from collections import deque
case1 = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
]  # take 7 min to rot all

case2 = [
    [1, 1, 0, 0, 0],
    [2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2],
    [0, 1, 0, 0, 1],
]  # not possiable so -1

case3 = []  # return 0
case4 = [[], [],]  # return 0


# BFS
# components: queue, visited?or1->2
# brute force steps:
# prep: edge cases, queue, ROWS, COLS, min = 0
# 1. loop all element, get the 2 position time: O(m x n) get 1 nums
# 2. from 2 positions start the bfs,flap 1 to 2 trace the max min from every 2 process time O(m x n)
#    for all 2 element:
#        curmin = 0
#        while queue: min ++ flap and numOf1 --
#        get the max min for cur loop
# 3. check if there are any 1 in there, if yes return -1, else return time min O(m x n) -> check the numOf1


def rottingOranges(matrix):
    if not matrix or not matrix[0]:
        return 0

    ROWS, COLS = len(matrix), len(matrix[0])

    minOfRotting = 0
    rottedOranges = deque()  # cache the position of 2
    numOfGoodOranges = 0
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

    # step1: check elements
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 2:
                rottedOranges.append((r, c))
            if matrix[r][c] == 1:
                numOfGoodOranges += 1

    if not rottedOranges and numOfGoodOranges >= 0:
        return -1
    if len(rottedOranges) > 0 and numOfGoodOranges == 0:
        return 0

    # step2:
    while rottedOranges:
        for _ in range(len(rottedOranges)):
            curRow, curCol = rottedOranges.popleft()

            for direction in directions:
                newRow, newCol = curRow + \
                    direction[0], curCol + direction[1]

                if (newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS
                        and matrix[newRow][newCol] == 1):
                    rottedOranges.append((newRow, newCol))
                    matrix[newRow][newCol] = 2
                    numOfGoodOranges -= 1

        if rottedOranges:
            minOfRotting += 1

    # step3:
    return minOfRotting if numOfGoodOranges == 0 else -1


print(rottingOranges(case1))
