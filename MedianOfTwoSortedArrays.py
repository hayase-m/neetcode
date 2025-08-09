from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        half = total_len // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low, high = 0, len(nums1)
        while low <= high:
            mid = (low+high) // 2
            left_nums1 = float('-inf') if mid == 0 else nums1[mid - 1]
            left_nums2 = float('-inf') if (
                half - mid) == 0 else nums2[half - mid - 1]
            left_max = max(left_nums1, left_nums2)
            right_nums1 = float('inf') if mid == len(
                nums1) else nums1[mid]
            right_nums2 = float('inf') if (
                half - mid) == len(nums2) else nums2[half - mid]
            right_min = min(right_nums1, right_nums2)

            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                if total_len % 2 == 0:
                    return (left_max+right_min)/2
                else:
                    return right_min
            elif left_nums1 > right_nums2:
                high = mid - 1
            elif left_nums2 > right_nums1:
                low = mid + 1


nums1 = [1, 2]
nums2 = [3]

print(Solution().findMedianSortedArrays(nums1, nums2))
