class Solution:
    def minDeletions(self, s: str) -> int:
        freqMap = Counter(s)
        frequency = sorted(freqMap.values(), reverse=True)
        deleteCount, maxFreqAllowed = 0, len(s)
        # Iterate over the frequencies in descending order
        for freq in frequency:
            # Delete characters to make the frequency equal the maximum frequency allowed
            if freq > maxFreqAllowed:
                deleteCount += freq - maxFreqAllowed
                freq = maxFreqAllowed
            # Update the maximum allowed frequency
            maxFreqAllowed = max(0, freq - 1)
        return deleteCount