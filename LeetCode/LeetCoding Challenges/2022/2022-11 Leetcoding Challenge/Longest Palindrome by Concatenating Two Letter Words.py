class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freqMap = Counter(words)
        result, central = 0, False
        for word, freq in freqMap.items():
            if word[0] == word[1]:
                if freq % 2 == 0:
                    result += freq
                else:
                    result += freq - 1
                    central = True
            elif word[0] < word[1]:
                result += 2 * min(freq, freqMap[word[1] + word[0]])
        if central:
            result += 1
        return 2 * result