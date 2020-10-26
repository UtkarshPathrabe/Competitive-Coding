class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        @lru_cache(maxsize=None)
        def getCount(word):
            charFrequencyMap = [0] * 26
            for c in word:
                charFrequencyMap[ord(c) - ord('a')] += 1
            for i in range(26):
                if charFrequencyMap[i] > 0:
                    return charFrequencyMap[i]
            return 0
        wordValues, result, wordsCount = [getCount(word) for word in words], [], len(words)
        wordValues.sort()
        for query in queries:
            val = getCount(query)
            result.append(wordsCount - bisect.bisect(wordValues, val))
        return result