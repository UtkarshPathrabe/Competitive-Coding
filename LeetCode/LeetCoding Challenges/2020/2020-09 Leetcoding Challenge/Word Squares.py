class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        wordLen = len(words[0])
        trie, result = {}, []
        
        def buildTrie():
            nonlocal trie
            for wordIndex, word in enumerate(words):
                currentNode = trie
                for char in word:
                    currentNode = currentNode.setdefault(char, {'#': set([])})
                    currentNode['#'].add(wordIndex)
        
        def getWordsWithPrefix(prefix):
            currentNode = trie
            for char in prefix:
                if char not in currentNode:
                    return set([])
                currentNode = currentNode[char]
            for wordIndex in currentNode['#']:
                yield words[wordIndex]
        
        def backtrack(step, wordSquare):
            if step == wordLen:
                result.append(wordSquare[:])
                return
            prefix = ''.join([word[step] for word in wordSquare])
            for candidate in getWordsWithPrefix(prefix):
                wordSquare.append(candidate)
                backtrack(step + 1, wordSquare)
                wordSquare.pop()
        
        buildTrie()
        for word in words:
            wordSquare = [word]
            backtrack(1, wordSquare)
        return result