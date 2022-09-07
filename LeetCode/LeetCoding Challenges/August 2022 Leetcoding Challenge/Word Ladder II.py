class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList.append(beginWord)
        wordList.append(endWord)
        distance = {}
        self.bfs(endWord, distance, wordList)
        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)
        return results

    def bfs(self, start, distance, w):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, w):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, w):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in w:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, w, path, results):
        if curt == target:
            results.append(list(path))
            return
        for word in self.get_next_words(curt, w):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, w, path, results)
            path.pop()