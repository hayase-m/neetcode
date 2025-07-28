from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def dfs(open_count, close_count):
            if len(stack) == 2*n:
                result.append("".join(stack))
                return
            if open_count < n:
                stack.append('(')
                dfs(open_count + 1, close_count)
                stack.pop()
            if open_count > close_count:
                stack.append(')')
                dfs(open_count, close_count + 1)
                stack.pop()
        dfs(0, 0)
        return result


# for num in range(0, 5):
#     print(Solution().generateParenthesis(num))
print(Solution().generateParenthesis(3))
