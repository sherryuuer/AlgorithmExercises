# Constraints:
# What if the board can not be solved? leave the suduko puzzle as it is

# in fact, backtracking is a brute force + recursive solution
# add -> decision -> remove
# Space O(81) Time O(9!^9)
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


class Solution:

    def isValid(self, n, rows, cols, boxs, r, c):
        return n not in rows[r] and n not in cols[c] and n not in boxs[(r // 3, c // 3)]

    def backtracking(self, board, rows, cols, boxs, r, c):
        if r == 9:
            return True

        if board[r][c] == ".":
            for n in range(1, 10):
                num = str(n)

                if self.isValid(num, rows, cols, boxs, r, c):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxs[(r // 3, c // 3)].add(num)

                    next_r, next_c = (r, c + 1) if c < 8 else (r + 1, 0)
                    if self.backtracking(board, rows, cols, boxs, next_r, next_c):
                        return True

                    # back tracking
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxs[(r // 3, c // 3)].remove(num)

            # Reset the cell after trying all numbers and backtracking
            board[r][c] = "."

        else:
            next_r, next_c = (r, c + 1) if c < 8 else (r + 1, 0)
            if self.backtracking(board, rows, cols, boxs, next_r, next_c):
                return True

        return False

    def sudokuSolver(self, board):
        from collections import defaultdict
        n = len(board)

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)  # key: (row // 3, col // 3)
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                value = board[r][c]
                rows[r].add(value)
                cols[c].add(value)
                boxs[(r // 3, c // 3)].add(value)

        self.backtracking(board, rows, cols, boxs, 0, 0)
        return board


solution = Solution()
solved_board = solution.sudokuSolver(board)
if solved_board:
    for row in solved_board:
        print(row)
