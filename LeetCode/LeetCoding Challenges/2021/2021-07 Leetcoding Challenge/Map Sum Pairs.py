class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keyValueMap = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.keyValueMap[key]
        self.keyValueMap[key] = val
        current = self.root
        current.score += delta
        for char in key:
            current = current.children.setdefault(char, TrieNode())
            current.score += delta

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)