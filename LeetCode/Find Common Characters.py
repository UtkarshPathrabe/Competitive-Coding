class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counter, result = Counter(A[0]), []
        for word in A[1:]:
            wordFreqCounter = Counter(word)
            tempCounter = defaultdict(int)
            for char, freq in counter.items():
                if char in wordFreqCounter:
                    tempCounter[char] = min(freq, wordFreqCounter[char])
            counter = tempCounter
        for char, freq in counter.items():
            result.extend([char] * freq)
        return result