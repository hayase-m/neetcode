from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        for _ in range(len(nums) - k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        heapq.heappop(self.nums)
        return self.nums[0]


input = ["KthLargest", [3, [1, 2, 3, 3]], "add", [3],
         "add", [5], "add", [6], "add", [7], "add", [8]]

kth = KthLargest(3, [1, 2, 3, 3])
print(kth.add(3))
print(kth.add(5))
print(kth.add(6))
print(kth.add(7))
print(kth.add(8))
