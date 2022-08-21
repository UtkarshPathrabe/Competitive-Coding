class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            return freq
        maxBFreq = [0] * 26
        for word in B:
            for i, freq in enumerate(count(word)):
                maxBFreq[i] = max(maxBFreq[i], freq)
        result = []
        for word in A:
            if all(x >= y for x, y in zip(count(word), maxBFreq)):
                result.append(word)
        return result