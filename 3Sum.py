from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if (two_sum := nums[left] + nums[right]) == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right) and (nums[right] == nums[right + 1]):
                        right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
