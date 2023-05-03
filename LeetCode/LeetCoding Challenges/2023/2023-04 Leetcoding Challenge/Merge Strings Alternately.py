class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result, i, j, n, m = [], 0, 0, len(word1), len(word2)
        while i < n and j < m:
            result.append(word1[i])
            result.append(word2[j])
            i, j = i + 1, j + 1
        while i < n:
            result.append(word1[i])
            i += 1
        while j < m:
            result.append(word2[j])
            j += 1
        return ''.join(result)