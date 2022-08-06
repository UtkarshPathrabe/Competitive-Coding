class OrderedStream:

    def __init__(self, n: int):
        self.stream, self.ptr, self.capacity = defaultdict(str), 1, n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey], currentPtr, result = value, self.ptr, []
        while self.stream[currentPtr] and self.ptr <= currentPtr <= self.capacity:
            result.append(self.stream[currentPtr])
            currentPtr += 1
        self.ptr = currentPtr
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)