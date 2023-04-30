class MyQueue:

    def __init__(self):
        self.stackA, self.stackB, self.front = [], [], None

    def push(self, x: int) -> None:
        if len(self.stackA) == 0:
            self.front = x
        self.stackA.append(x)

    def pop(self) -> int:
        if len(self.stackB) == 0:
            while len(self.stackA) > 0:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    def peek(self) -> int:
        if len(self.stackB) > 0:
            return self.stackB[-1]
        return self.front

    def empty(self) -> bool:
        return len(self.stackA) == 0 and len(self.stackB) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()