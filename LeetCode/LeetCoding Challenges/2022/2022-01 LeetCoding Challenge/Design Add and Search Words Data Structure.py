class TrieNode:
    
    def __init__(self):
        self.childNodes = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            n = node.childNodes.get(c, TrieNode())
            node.childNodes[c] = n
            node = n
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self._searchHelper(word, self.root)
    
    def _searchHelper(self, word: str, node: TrieNode):
        for index, c in enumerate(word):
            if c == '.':
                for char, childNode in node.childNodes.items():
                    if self._searchHelper(word[index + 1:], childNode):
                        return True
                return False
            else:
                node = node.childNodes.get(c)
                if not node:
                    return False
        return node.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)