from typing import List

# O(nlogn)
# sortのアルゴに上記の計算時間がかかる
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if (nums[i] == nums[i + 1]):
#                 return True
#         return False


# O(n)
# ユニークな要素のみを保持するsetを用いて、その中から探す。
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for num in nums:
            if num in dict:
                return True
            dict.add(num)
        return False

# O(n)・solution
# setの特性を活かして、元のlenと合うかをチェックする

# def hasDuplicate(self, nums: List[int]) -> bool:
#     return len(set(nums)) < len(nums)

# input_list = [1, 2, 3, 0]
# solver = Solution()
# result = solver.hasDuplicate(input_list)
# print(f"結果は{result}です。")
