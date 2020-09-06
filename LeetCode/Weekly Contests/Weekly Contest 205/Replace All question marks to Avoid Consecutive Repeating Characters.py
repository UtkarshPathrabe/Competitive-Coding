class Solution:
    def modifyString(self, s: str) -> str:
        sLen, sList = len(s), list(s)
        CHARACTERS = [chr(ord('a') + i) for i in range(26)]
        for i, c in enumerate(sList):
            if c == '?':
                charIndex = 0
                while (i > 0 and sList[i - 1] != '?' and sList[i - 1] == CHARACTERS[charIndex]) or (i < sLen - 1 and sList[i + 1] != '?' and sList[i + 1] == CHARACTERS[charIndex]):
                    charIndex += 1
                sList[i] = CHARACTERS[charIndex]
        return ''.join(sList)