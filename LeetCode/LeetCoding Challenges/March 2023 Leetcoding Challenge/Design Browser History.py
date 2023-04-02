class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentIndex = 0
        self.maxIndex = 0
        self.history = {self.currentIndex: homepage}

    def visit(self, url: str) -> None:
        self.currentIndex += 1
        self.history[self.currentIndex] = url
        self.maxIndex = self.currentIndex

    def back(self, steps: int) -> str:
        self.currentIndex -= steps
        self.currentIndex = 0 if self.currentIndex < 0 else self.currentIndex
        return self.history[self.currentIndex]

    def forward(self, steps: int) -> str:
        self.currentIndex += steps
        self.currentIndex = self.maxIndex if self.currentIndex > self.maxIndex else self.currentIndex
        return self.history[self.currentIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)