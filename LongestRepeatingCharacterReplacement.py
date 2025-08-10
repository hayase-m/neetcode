from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        max_len = 0
        left = 0
        for i in range(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            if (i - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, i - left + 1)
        return max_len


s = "XYYX"
k = 2

print(Solution().characterReplacement(s, k))
