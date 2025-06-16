from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def solve(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            solve(i + 1)
            subset.append(nums[i])
            solve(i + 1)
            subset.pop()
        solve(0)
        return result


nums = [1, 2, 3]
print(Solution().subsets(nums))
