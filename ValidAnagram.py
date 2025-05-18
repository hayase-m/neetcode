from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sortedを使うので計算量はnlogn+nlogm
        # s_sorted = sorted(s)
        # t_sorted = sorted(t)
        # return s_sorted == t_sorted

        dict_s = {}
        dict_t = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        return dict_s == dict_t

        # # counterメソッドを使うこともできる
        # s_count = Counter(s)
        # t_count = Counter(t)
        # return s_count == t_count


s = "raccar"
t = "carrace"

solution = Solution()

print(solution.isAnagram(s, t))
