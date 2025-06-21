from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            lis = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    lis = max(lis, dp[j] + 1)
            dp.append(lis)
        return max(dp)


nums = [[9, 1, 4, 2, 3, 3, 7],
        [0, 3, 1, 3, 2, 3],
        [4, 3, 2, 1],
        [1, 4, 3, 2]]
for num in nums:
    print(Solution().lengthOfLIS(num))
