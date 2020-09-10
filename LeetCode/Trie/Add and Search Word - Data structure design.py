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
            node = node.childNodes.setdefault(c, TrieNode())
        node.isEnd = True

    def search(self, word: str) -> bool:
        def searchInNode(word, node) -> bool:
            for i, c in enumerate(word):
                if node.childNodes.get(c) == None:
                    if c == '.':
                        for x in node.childNodes:
                            if searchInNode(word[i+1:], node.childNodes.get(x)):
                                return True
                    return False
                else:
                    node = node.childNodes.get(c)
            return node.isEnd
        return searchInNode(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)