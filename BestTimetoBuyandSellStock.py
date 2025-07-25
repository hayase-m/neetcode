from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - cur_min)
            cur_min = min(cur_min, price)
        return max_profit


prices = [[10, 1, 5, 6, 7, 1],
          [10, 8, 7, 5, 2]]

for price in prices:
    print(Solution().maxProfit(price))
