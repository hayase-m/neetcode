from typing import List
from collections import defaultdict


class Solution:
    def _init_dict(self, board):
        char_positions = defaultdict(list)
        for row, rows in enumerate(board):
            for col, char in enumerate(rows):
                char_positions[char].append((row, col))
        return char_positions

    def exist(self, board: List[List[str]], word: str) -> bool:
        char_positions = self._init_dict(board)
        visited = set()
        first_idx = char_positions[word[0]]
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        num_row = len(board)
        num_col = len(board[0])

        def dfs(row, col, k) -> bool:
            if k == len(word):
                return True
            if not (0 <= row < num_row and 0 <= col < num_col):
                return False
            if ((row, col) in visited):
                return False
            if (board[row][col] != word[k]):
                return False

            visited.add((row, col))
            for dr, dc in directions:
                next_r, next_c = row + dr, col + dc
                if dfs(next_r, next_c, k + 1):
                    return True
            visited.remove((row, col))
            return False

        for first_row, first_col in first_idx:
            if dfs(first_row, first_col, 0):
                return True
        return False


board = [
    ["A", "B", "C", "D"],
    ["S", "A", "A", "T"],
    ["A", "C", "A", "E"]
]
word = "CAT"
print(Solution().exist(board, word))
