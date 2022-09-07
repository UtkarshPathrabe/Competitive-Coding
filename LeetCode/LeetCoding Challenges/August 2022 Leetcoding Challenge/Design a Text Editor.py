class TextEditor:

    def __init__(self):
        self.left, self.right = [], []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        count = 0
        while self.left and count < k:
            self.left.pop()
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
        count = 0
        while self.left and count < k:
            self.right.append(self.left.pop())
            count += 1
        return ''.join(self.left[max(-10, -len(self.left)):])

    def cursorRight(self, k: int) -> str:
        count = 0
        while self.right and count < k:
            self.left.append(self.right.pop())
            count += 1
        return ''.join(self.left[max(-10, -len(self.left)):])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)