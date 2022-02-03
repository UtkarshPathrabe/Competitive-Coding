class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.chars = characters
        self.nums = list(range(self.k))
        self.hasNextFlag = True

    def next(self) -> str:
        currentCombination = [self.chars[i] for i in self.nums]
        i = self.k - 1
        while i >= 0 and self.nums[i] == self.n - self.k + i:
            i -= 1
        self.nums[i] += 1
        if i >= 0:
            for j in range(i + 1, self.k):
                self.nums[j] = self.nums[i] + j - i
        else:
            self.hasNextFlag = False
        return ''.join(currentCombination)

    def hasNext(self) -> bool:
        return self.hasNextFlag


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()