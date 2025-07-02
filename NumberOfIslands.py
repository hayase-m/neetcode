from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x_len = len(grid[0])
        y_len = len(grid)
        count = 0

        def dfs(x, y):
            if (x < 0 or x > x_len - 1) or (y < 0 or y > y_len - 1) or (grid[y][x] == "0"):
                return
            grid[y][x] = "0"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == "1":
                    count += 1
                    dfs(x, y)
        return count


grid = [
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(Solution().numIslands(grid))
