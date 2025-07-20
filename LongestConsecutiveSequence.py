from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in s:
            if num - 1 in s:
                continue
            cur_num = num
            cur_len = 1
            while cur_num + 1 in s:
                cur_len += 1
                cur_num += 1
            max_len = max(max_len, cur_len)
        return max_len


nums = [[2, 20, 4, 10, 3, 4, 5],
        [0, 3, 2, 5, 4, 6, 1, 1]]

for num in nums:
    print(Solution().longestConsecutive(num))
