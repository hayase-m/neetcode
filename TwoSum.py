from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        dict_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dict_map:
                return [dict_map[diff], index]
            dict_map[value] = index


nums = [3, 4, 5, 6]
target = 10

print(Solution().twoSum(nums, target))
