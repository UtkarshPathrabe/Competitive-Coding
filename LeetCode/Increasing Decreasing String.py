class Solution:
    def sortString(self, s: str) -> str:
        charFrequencyMap, result, length = [0] * 26, [], len(s)
        for c in s:
            charFrequencyMap[ord(c) - ord('a')] += 1
        while len(result) != length:
            for index in range(26):
                if charFrequencyMap[index] > 0:
                    result.append(chr(ord('a') + index))
                    charFrequencyMap[index] -= 1
            for index in range(25, -1, -1):
                if charFrequencyMap[index] > 0:
                    result.append(chr(ord('a') + index))
                    charFrequencyMap[index] -= 1
        return ''.join(result)