from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        last_index = len(nums) - 1

        for i in range(len(nums)):
            if max_index < i:
                break
            max_index = max(max_index, i + nums[i])

        return max_index >= last_index


nums = [[1, 2, 0, 1, 0],
        [1, 2, 1, 0, 1]]

for num in nums:
    print(Solution().canJump(num))
