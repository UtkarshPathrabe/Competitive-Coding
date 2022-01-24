class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, inOrderDegree = defaultdict(set), Counter({c: 0 for word in words for c in word})
        for firstWord, secondWord in zip(words, words[1:]):
            for char1, char2 in zip(firstWord, secondWord):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        inOrderDegree[char2] += 1
                    break
            else:
                if len(secondWord) < len(firstWord):
                    return ''
        result = []
        zeroInDegreeQueue = deque([c for c, degree in inOrderDegree.items() if degree == 0])
        while zeroInDegreeQueue:
            char = zeroInDegreeQueue.popleft()
            result.append(char)
            for neighbour in graph[char]:
                inOrderDegree[neighbour] -= 1
                if inOrderDegree[neighbour] == 0:
                    zeroInDegreeQueue.append(neighbour)
        if len(result) < len(inOrderDegree):
            return ''
        return ''.join(result)