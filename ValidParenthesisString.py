class Solution:
    def checkValidString(self, s: str) -> bool:
        max_cnt = min_cnt = 0
        for c in s:
            if c == '(':
                max_cnt, min_cnt = max_cnt + 1, min_cnt + 1
            elif c == ')':
                max_cnt, min_cnt = max_cnt - 1, min_cnt - 1
            else:
                max_cnt, min_cnt = max_cnt + 1, min_cnt - 1
            if max_cnt < 0:
                return False
            if min_cnt < 0:
                min_cnt = 0
        return min_cnt == 0


ss = ["((**)",
      "(((*)"]

for s in ss:
    print(Solution().checkValidString(s))
