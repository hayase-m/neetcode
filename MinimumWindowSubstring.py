from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = {}
        target_types = len(target)
        window_types = 0
        left, right = 0, 0
        best_len = float('inf')
        while right < len(s):
            right += 1
            if s[right - 1] in target:
                window[s[right - 1]] = window.get(s[right - 1], 0) + 1
                if window[s[right - 1]] == target[s[right - 1]]:
                    window_types += 1
                while window_types == target_types:
                    if best_len > right - left:
                        best_len = right - left
                        best_left = left
                        best_right = right
                    if s[left] in target:
                        window[s[left]] -= 1
                        if window[s[left]] < target[s[left]]:
                            window_types -= 1
                    left += 1
        if best_len == float('inf'):
            return ""
        return s[best_left:best_right]

        # window[s[right]] = window.get(s[right], 0) + 1
        # cap = target.get(s[right], float('inf'))
        # # print(left, right, window)
        # while window[s[right]] > cap:
        #     # print(s[left], s[right], cap)
        #     window[s[left]] -= 1
        #     left += 1
        # if best_len > right - left + 1:
        #     best_len = right - left + 1
        #     best_left = left
        #     best_right = right
        # right += 1


s = "OUZODYXAZVXYZ"
t = "XYZ"

print(Solution().minWindow(s, t))
