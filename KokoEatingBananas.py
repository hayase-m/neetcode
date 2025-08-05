import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            total_hour = 0
            mid = (left+right)//2
            for pile in piles:
                total_hour += math.ceil(pile / mid)
            if total_hour > h:
                left = mid + 1
            else:
                min_rate = mid
                right = mid - 1
        return min_rate


piles = [1, 4, 3, 2]
h = 9

print(Solution().minEatingSpeed(piles, h))
