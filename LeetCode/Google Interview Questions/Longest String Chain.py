class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsListLength = len(words)
        if wordsListLength <= 1:
            return wordsListLength
        def isPredecessor(word1, word2): #is word1 predecessor of word2
            for i in range(len(word2)):
                if word2[:i] + word2[i+1:] == word1:
                    return True
            return False
        words.sort(key = lambda x:len(x))
        result = 1
        dp = [1 for _ in range(wordsListLength)]
        for i in range(wordsListLength):
            for j in range(i + 1, wordsListLength):
                if len(words[i]) + 1 == len(words[j]) and isPredecessor(words[i], words[j]):
                    dp[j] = dp[i] + 1
                    result = max(result, dp[j])
        return result