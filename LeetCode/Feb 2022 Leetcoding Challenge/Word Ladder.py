class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not endWord or not beginWord or endWord not in wordList:
            return 0
        comboMap, wordLen = defaultdict(set), len(beginWord)
        for word in wordList:
            for i in range(wordLen):
                comboMap[word[:i] + '*' + word[i + 1:]].add(word)
        queue, visited = deque([(beginWord, 1),]), {beginWord}
        while queue:
            currentWord, level = queue.popleft()
            for i in range(wordLen):
                key = currentWord[:i] + '*' + currentWord[i + 1:]
                for dictWord in comboMap[key]:
                    if dictWord == endWord:
                        return level + 1
                    if dictWord not in visited:
                        visited.add(dictWord)
                        queue.append((dictWord, level + 1))
                comboMap[key] = set()
        return 0