from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 != 0:
            return False
        target = num_sum // 2

        memo = [[None for _ in range(target + 1)]for _ in range(len(nums))]

        def solve(i, goal):
            if goal == 0:
                return True
            if goal < 0:
                return False
            if i >= len(nums):
                return False
            if memo[i][goal] is not None:
                return memo[i][goal]
            result = solve(i+1, goal) or solve(i+1, goal-nums[i])
            memo[i][goal] = result
            return result

        return solve(0, target)


nums = [[1, 2, 3, 4],
        [1, 2, 3, 4, 5]]

for num in nums:
    print(Solution().canPartition(num))
