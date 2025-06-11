from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)

        def solve(i):
            if i >= len(nums):
                return 0
            if memo[i] >= 0:
                return memo[i]
            current_max = max(solve(i+1), solve(i+2)+nums[i])
            memo[i] = current_max
            return current_max
        return solve(0)


nums = [[1, 1, 3, 3],
        [2, 9, 8, 3, 6]
        ]
for num in nums:
    print(Solution().rob(num))
