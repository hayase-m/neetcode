from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while (two_sum := numbers[left] + numbers[right]) != target:
            if two_sum > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]


numbers = [1, 2, 3, 4]
target = 5
print(Solution().twoSum(numbers, target))
