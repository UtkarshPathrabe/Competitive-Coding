class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or self.minStack[-1][0] > x:
            self.minStack.append([x, 1])
        elif self.minStack[-1][0] == x:
            self.minStack[-1][1] += 1

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
        if self.minStack[-1][1] == 0:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()