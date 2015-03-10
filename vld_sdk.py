# Valid Sudoku
# Determine if a Sudoku is valid, according to: Sudoku Puzzles 
# - The Rules.
# The Sudoku board could be partially filled, where empty 
# cells are filled with the character '.'.

# A partially filled sudoku which is valid.
# Note:
# A valid Sudoku board (partially filled) is not necessarily 
# solvable. Only the filled cells need to be validated.
# Sudoku Puzzles - The Rules.
# There are just 3 rules to Sudoku.
# Each row must have the numbers 1-9 occuring just once.
# Each column must have the numbers 1-9 occuring just once.
# And the numbers 1-9 must occur just once in each of the 9 sub
# -boxes of the grid.


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(x, y, tmp):
            for idx in range(9):
                if board[idx][y] == tmp:
                    return False
            for idy in range(9):
                if board[x][idy] == tmp:
                    return False
            for idx in range(3):
                for idy in range(3):
                    if board[(x/3)*3+idx][(y/3)*3+idy] == tmp: 
                        return False
            return True
        for idx in range(9):
            for idy in range(9):
                if board[idx][idy] == '.':
                    continue
                tmp = board[idx][idy]
                board[idx][idy] = 'D'
                if isValid(idx, idy, tmp) == False: 
                    return False
                else:
                    board[idx][idy] = tmp
        return True