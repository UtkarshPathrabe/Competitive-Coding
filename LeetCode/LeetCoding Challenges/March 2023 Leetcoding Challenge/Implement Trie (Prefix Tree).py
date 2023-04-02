class TrieNode:
    
    def __init__(self):
        self.childNodes = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            n = node.childNodes.get(c, TrieNode())
            node.childNodes[c] = n
            node = n
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            node = node.childNodes.get(c)
            if not node:
                return False
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            node = node.childNodes.get(c)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)