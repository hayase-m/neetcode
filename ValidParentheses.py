from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        brackets = {']': '[', '}': '{', ')': '('}
        stack = deque()
        for c in s:
            if c in brackets:
                if not stack or brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack


ss = ["[]",
      "([{}])",
      "[(])",
      "]",
      "{{{"
      ]

for s in ss:
    print(Solution().isValid(s))
