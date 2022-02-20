class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.wordEnd = -1
        self.palindromeSuffix = set([])

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1]
            currentNode = trie
            for j, char in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    currentNode.palindromeSuffix.add(i)
                currentNode = currentNode.children[char]
            currentNode.wordEnd = i
        result = []
        for i, word in enumerate(words):
            currentNode = trie
            for j, char in enumerate(word):
                if currentNode.wordEnd != -1:
                    if word[j:] == word[j:][::-1]:
                        result.append([i, currentNode.wordEnd])
                if char not in currentNode.children:
                    break
                currentNode = currentNode.children[char]
            else:
                if currentNode.wordEnd != -1 and currentNode.wordEnd != i:
                    result.append([i, currentNode.wordEnd])
                for j in currentNode.palindromeSuffix:
                    result.append([i, j])
        return result