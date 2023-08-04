class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue, wordDict, visited, sLength = deque([0]), set(wordDict), set(), len(s)
        while queue:
            start = queue.popleft()
            if start not in visited:
                for end in range(start + 1, sLength + 1):
                    if s[start: end] in wordDict:
                        queue.append(end)
                        if end == sLength:
                            return True
                visited.add(start)
        return False