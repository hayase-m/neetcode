from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = [result_tuple[0] for result_tuple in count.most_common()]
        return result


nums = [1, 2, 2, 3, 3, 3]

k = 2
print(Solution().topKFrequent(nums, k))
