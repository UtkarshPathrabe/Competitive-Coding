class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()
        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if ch not in node:
                return False
            node = node[ch]
        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)