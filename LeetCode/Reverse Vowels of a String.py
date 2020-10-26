class Solution:
    def reverseVowels(self, s: str) -> str:
        s, startPointer, endPointer, VOWELS = list(s), 0, len(s) - 1, ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while True:
            while startPointer < len(s) and s[startPointer] not in VOWELS:
                startPointer += 1
            while endPointer >= 0 and s[endPointer] not in VOWELS:
                endPointer -= 1
            if startPointer < endPointer:
                s[startPointer], s[endPointer] = s[endPointer], s[startPointer]
                startPointer += 1
                endPointer -= 1
            else:
                break
        return ''.join(s)