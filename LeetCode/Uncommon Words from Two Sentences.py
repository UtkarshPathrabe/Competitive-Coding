class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        freqMapA, freqMapB, result = defaultdict(int), defaultdict(int), []
        for word in A.split():
            freqMapA[word] += 1
        for word in B.split():
            freqMapB[word] += 1
        for word, frequency in freqMapA.items():
            if frequency == 1 and word not in freqMapB:
                result.append(word)
        for word, frequency in freqMapB.items():
            if frequency == 1 and word not in freqMapA:
                result.append(word)
        return result