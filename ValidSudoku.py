from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value == '.':
                    continue
                box_index = (y // 3) * 3 + x // 3
                if (value in rows[y]) or (value in cols[x]) or (value in boxes[box_index]):
                    return False
                rows[y].add(value)
                cols[x].add(value)
                boxes[box_index].add(value)
        return True


board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


print(Solution().isValidSudoku(board))
