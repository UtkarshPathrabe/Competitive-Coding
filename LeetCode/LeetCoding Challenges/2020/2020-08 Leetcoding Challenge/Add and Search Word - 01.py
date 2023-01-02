class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if node.get(c) == None:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word: str) -> bool:
        def searchInNode(word, node) -> bool:
            for i, c in enumerate(word):
                if node.get(c) == None:
                    if c == '.':
                        for x in node:
                            if x != '$' and searchInNode(word[i+1:], node.get(x)):
                                return True
                    return False
                else:
                    node = node[c]
            return '$' in node
        return searchInNode(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)