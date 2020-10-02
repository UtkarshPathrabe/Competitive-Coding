class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.lists = [v1, v2]
        self.count = 0
        self.numberOfLists = len(self.lists)
        self.maxListSize = max(len(l) for l in self.lists)
        
    def __getNextValidCount(self):
        itemIndex, listIndex = divmod(self.count, self.numberOfLists)
        while itemIndex >= len(self.lists[listIndex]) and itemIndex < self.maxListSize:
            self.count += 1
            itemIndex, listIndex = divmod(self.count, self.numberOfLists)

    def next(self) -> int:
        self.__getNextValidCount()
        itemIndex, listIndex = divmod(self.count, self.numberOfLists)
        result = self.lists[listIndex][itemIndex]
        self.count += 1
        return result

    def hasNext(self) -> bool:
        self.__getNextValidCount()
        if self.count // self.numberOfLists < self.maxListSize:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())