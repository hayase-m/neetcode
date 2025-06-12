from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


nums = [[-1, 0, 2, 4, 6, 8],
        [-1, 0, 2, 4, 6, 8]]
target = [4, 3]
for num, tar in zip(nums, target):
    print(Solution().search(num, tar))
