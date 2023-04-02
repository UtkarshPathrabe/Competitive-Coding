class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        patternMap, wordMap = {}, {}
        if len(pattern) != len(words):
            return False
        for index, char in enumerate(pattern):
            if char in patternMap:
                if patternMap[char] != words[index]:
                    return False
            else:
                if words[index] in wordMap:
                    return False
                else:
                    patternMap[char] = words[index]
                    wordMap[words[index]] = char
        return True