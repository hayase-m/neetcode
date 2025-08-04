from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = cols * rows - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // cols][mid % cols] == target:
                return True
            elif matrix[mid // cols][mid % cols] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        #     top = 0
        #     bottom = len(matrix) - 1
        #     while top <= bottom:
        #         if matrix[top][0] == target or matrix[bottom][0] == target:
        #             return True
        #         half = (bottom + top) // 2
        #         if matrix[half][0] > target:
        #             bottom = half - 1
        #         else:
        #             top = half + 1
        #     if bottom == -1:
        #         return False
        #     left = 0
        #     right = len(matrix[0]) - 1
        #     while left <= right:
        #         if right == -1:
        #             return False
        #         half = (left + right) // 2
        #         if matrix[bottom][half] == target:
        #             return True
        #         elif matrix[bottom][half] > target:
        #             right = half - 1
        #         else:
        #             left = half + 1
        #     return False


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 12
print(Solution().searchMatrix(matrix, target))
