from typing import List
from collections import deque

# 自分で解いたbrute force
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         iter = len(nums) - k + 1
#         d = deque(nums[:k])
#         for i in range(iter):
#             result.append(max(d))
#             if i == iter - 1:
#                 break
#             d.popleft()
#             d.append(nums[k])
#             k += 1
#         return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = deque()
        for index, value in enumerate(nums):
            if d and d[0] < index - k + 1:
                d.popleft()
            while d and value >= nums[d[-1]]:
                d.pop()
            d.append(index)
            if index >= k - 1:
                result.append(nums[d[0]])
        return result


nums = [1, 2, 1, 0, 4, 2, 6]
k = 3

print(Solution().maxSlidingWindow(nums, k))
