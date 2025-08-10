from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        left = 0
        window_len = 0
        for c1 in s1:
            count_s1[c1] += 1
        for c2 in s2:
            window_len += 1
            count_s2[c2] += 1
            if window_len > len(s1):
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    count_s2.pop(s2[left])
                left += 1
            if count_s1 == count_s2:
                return True
        return False


s1 = "abc"
s2 = "zecabee"

print(Solution().checkInclusion(s1, s2))
