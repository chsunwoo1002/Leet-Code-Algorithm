# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        square_set = [[set() for j in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                if (board[i][j] == "."):
                    continue
                else:
                    num = board[i][j]
                    if (num in row_set[i] or num in col_set[j] or num in square_set[i // 3][j // 3]):
                        return False
                    else:
                        row_set[i].add(num)
                        col_set[j].add(num)
                        square_set[i // 3][j // 3].add(num)
        return True