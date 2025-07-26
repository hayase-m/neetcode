class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        pop_val = self.stack.pop(-1)
        if pop_val == self.min_stack[-1]:
            self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
