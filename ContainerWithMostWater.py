from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_water = 0
        while start < end:
            current_height = min(heights[start], heights[end])
            current_width = end - start
            max_water = max(max_water, current_height * current_width)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_water


height = [1, 7, 2, 5, 4, 7, 3, 6]
print(Solution().maxArea(height))
