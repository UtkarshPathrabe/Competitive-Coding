class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph, currentPath, shortestPaths = defaultdict(list), [beginWord,], []
        def getNeighbour(word: str, wordSet):
            neighbours, charList = [], list(word)
            for i in range(len(charList)):
                oldChar = charList[i]
                for o in range(ord('a'), ord('z') + 1):
                    currentChar = chr(o)
                    charList[i] = currentChar
                    newWord = ''.join(charList)
                    if currentChar == oldChar or newWord not in wordSet:
                        continue
                    neighbours.append(newWord)
                charList[i] = oldChar
            return neighbours
        def backtrack(source, destination):
            if source == destination:
                shortestPaths.append(list(currentPath))
                return
            if source not in graph:
                return
            for neighbour in graph[source]:
                currentPath.append(neighbour)
                backtrack(neighbour, destination)
                currentPath.pop()
        def createGraphUsingBFS():
            wordSet, queue, isEnqueued = set(wordList), deque([beginWord,]), set([beginWord,])
            if beginWord in wordSet:
                wordSet.remove(beginWord)
            while queue:
                visited = set() # to store words in current layer
                for i in range(len(queue) - 1, -1, -1):
                    currentWord = queue.popleft()
                    for word in getNeighbour(currentWord, wordSet):
                        visited.add(word)
                        graph[currentWord].append(word)
                        if word not in isEnqueued:
                            isEnqueued.add(word)
                            queue.append(word)
                for word in visited:
                    if word in wordSet:
                        wordSet.remove(word)
        createGraphUsingBFS()
        backtrack(beginWord, endWord)
        return shortestPaths