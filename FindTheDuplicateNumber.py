from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])] *= -1


nums = [[1, 2, 3, 2, 2],
        [1, 2, 3, 4, 4],
        [4, 1, 4, 2, 3],
        [1, 2, 3, 4, 4]
        ]

for num in nums:
    print(Solution().findDuplicate(num))
