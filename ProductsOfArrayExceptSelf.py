from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        suf = 1
        for i in range(1, len(nums)):
            result.append(result[i - 1] * nums[i - 1])
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= suf
            suf *= nums[j]
        return result


nums = [1, 2, 4, 6]
print(Solution().productExceptSelf(nums))
