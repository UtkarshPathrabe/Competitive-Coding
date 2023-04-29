class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result, heads = 0, [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)
        for char in s:
            charIndex = ord(char) - ord('a')
            oldBucket = heads[charIndex]
            heads[charIndex] = []
            while oldBucket:
                it = oldBucket.pop()
                nextChar = next(it, None)
                if nextChar:
                    heads[ord(nextChar) - ord('a')].append(it)
                else:
                    result += 1
        return result