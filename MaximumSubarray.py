from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = global_max = nums[0]
        for num in nums[:1]:
            current_max = max(current_max + nums, nums)
            global_max = max(global_max, current_max)
        return global_max


nums = [2, -3, 4, -2, 2, 1, -1, 4]

print(Solution().maxSubArray(nums))
