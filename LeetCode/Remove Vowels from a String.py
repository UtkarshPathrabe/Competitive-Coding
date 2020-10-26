class Solution:
    def removeVowels(self, S: str) -> str:
        S, result, VOWELS = list(S), [], set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']) 
        for char in S:
            if char not in VOWELS:
                result.append(char)
        return ''.join(result)