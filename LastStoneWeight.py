from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = [-1 * stone for stone in stones]
        heapq.heapify(l)  # 0(N)
        while len(l) > 1:  # O(N)
            x = heapq.heappop(l)  # O(logN)
            y = heapq.heappop(l)
            if x != y:
                heapq.heappush(l, x - y)
        if not l:
            return 0
        return -l[0]


stones = [2, 3, 6, 2, 4]
print(Solution().lastStoneWeight(stones))
