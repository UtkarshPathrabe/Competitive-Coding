class LFUCache:

    def __init__(self, capacity: int):
        self.capacity, self.minFrequency = capacity, 1
        self.keyToFrequencyMap = defaultdict(int)
        self.frequencyToKeyMap = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyToFrequencyMap:
            return -1
        self.frequencyToKeyMap[self.keyToFrequencyMap[key] + 1][key] = self.frequencyToKeyMap[self.keyToFrequencyMap[key]].pop(key)
        if self.minFrequency == self.keyToFrequencyMap[key] and len(self.frequencyToKeyMap[self.keyToFrequencyMap[key]]) == 0:
            self.minFrequency = self.keyToFrequencyMap[key] + 1
        self.keyToFrequencyMap[key] += 1
        return self.frequencyToKeyMap[self.keyToFrequencyMap[key]][key]

    def put(self, key: int, value: int) -> None:
        if key in self.keyToFrequencyMap:
            self.frequencyToKeyMap[self.keyToFrequencyMap[key] + 1][key] = value
            self.frequencyToKeyMap[self.keyToFrequencyMap[key]].pop(key)
            if self.minFrequency == self.keyToFrequencyMap[key] and len(self.frequencyToKeyMap[self.keyToFrequencyMap[key]]) == 0:
                self.minFrequency = self.keyToFrequencyMap[key] + 1
            self.keyToFrequencyMap[key] += 1
        else:
            self.keyToFrequencyMap[key] = 1
            self.frequencyToKeyMap[self.keyToFrequencyMap[key]][key] = value
            self.capacity -= 1
            if self.capacity < 0:
                toDeleteKey, toDeleteValue = self.frequencyToKeyMap[self.minFrequency].popitem(last = False)
                self.keyToFrequencyMap.pop(toDeleteKey)
                self.capacity += 1
            self.minFrequency = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)