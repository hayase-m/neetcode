from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        visited = set()

        def dfs():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)
                    dfs()
                    path.pop()
                    visited.discard(i)
        dfs()
        return result


nums = [1, 2, 3]
print(Solution().permute(nums))
