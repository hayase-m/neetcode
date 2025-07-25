from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                result += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                result += right_max - height[right]
                right -= 1
        return result


height = [0, 2, 0, 1, 1, 0, 1, 3, 2, 1]
print(Solution().trap(height))
