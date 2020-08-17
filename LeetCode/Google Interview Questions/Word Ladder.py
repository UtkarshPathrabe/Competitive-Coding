class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        wordLength = len(beginWord)
        allComboDictionary = defaultdict(list)
        for word in wordList:
            for i in range(wordLength):
                allComboDictionary[word[:i] + '*' + word[i+1:]].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            word, level = queue.popleft()
            for i in range(wordLength):
                intermediateDummy = word[:i] + '*' + word[i+1:]
                for dummyWord in allComboDictionary[intermediateDummy]:
                    if dummyWord == endWord:
                        return level + 1
                    if dummyWord not in visited:
                        visited[dummyWord] = True
                        queue.append((dummyWord, level + 1))
                allComboDictionary[intermediateDummy] = []
        return 0