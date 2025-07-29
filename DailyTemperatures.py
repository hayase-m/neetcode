from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                pop_idx = stack.pop()
                result[pop_idx] = i - pop_idx
            stack.append(i)
        return result


temperatures = [30, 38, 30, 36, 35, 40, 28]
print(Solution().dailyTemperatures(temperatures))
