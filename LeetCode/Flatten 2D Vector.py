class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.outer = 0
        self.inner = 0
        
    def __advanceToNext(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self.__advanceToNext()
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        self.__advanceToNext()
        return self.outer < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()