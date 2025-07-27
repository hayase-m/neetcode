from typing import List
import operator


class Solution:
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     ops = {'+': operator.add, '-': operator.sub,
    #            '*': operator.mul, '/': operator.floordiv}
    #     for i in range(len(tokens) - 1, -1, -1):
    #         stack.append(tokens[i])
    #         while len(stack) > 2 and stack[-2] not in ops and stack[-1] not in ops:
    #             first_num = int(stack.pop(-1))
    #             second_num = int(stack.pop(-1))
    #             op_func = ops[stack.pop(-1)]
    #             result = op_func(first_num, second_num)
    #             stack.append(str(result))
    #     return int(stack[-1])
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+': operator.add, '-': operator.sub,
               '*': operator.mul, '/': operator.truediv}
        for i in range(0, len(tokens)):
            if tokens[i] not in ops:
                stack.append(tokens[i])
            else:
                op_func = ops[tokens[i]]
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                stack.append(int(op_func(first_num, second_num)))
        return int(stack[-1])


tokens = ["1", "2", "+", "3", "*", "4", "-"]
print(Solution().evalRPN(tokens))
