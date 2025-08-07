from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


nums = [[3, 4, 5, 6, 1, 2],
        [4, 5, 0, 1, 2, 3],
        [4, 5, 6, 7],
        [1, 2, 3, 4],
        [6, 1, 2, 3]
        ]

for num in nums:
    print(Solution().findMin(num))
