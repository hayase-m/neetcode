from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col_has_zero = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                matrix[0][0] = 0
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(len(matrix)-1, 0, -1):
            for j in range(len(matrix[i])-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for row in range(len(matrix[0])):
                matrix[0][row] = 0
        if first_col_has_zero:
            for col in range(len(matrix)):
                matrix[col][0] = 0


matrix = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

print(Solution().setZeroes(matrix))
