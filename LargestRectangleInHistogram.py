from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and height <= stack[-1][1]:
                pop_info = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1][0] - 1
                area = pop_info[1] * width
                max_area = max(max_area, area)
            stack.append((i, height))
        return max_area


heights = [7, 1, 7, 2, 2, 4]
print(Solution().largestRectangleArea(heights))
