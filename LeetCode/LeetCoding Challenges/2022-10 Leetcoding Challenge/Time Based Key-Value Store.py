from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].update({timestamp: value})

    def get(self, key: str, timestamp: int) -> str:
        timestampsData = self.store[key]
        k = timestampsData.bisect_right(timestamp)
        if k == 0:
            return ''
        return timestampsData.peekitem(k - 1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)