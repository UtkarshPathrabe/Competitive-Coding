class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        characterMap = {}
        wordList = s.split(' ')
        patternLength = len(pattern)
        wordsLength = len(wordList)
        if patternLength != wordsLength:
            return False
        for i, p in enumerate(pattern):
            if p not in characterMap:
                if wordList[i] in characterMap.values():
                    return False
                else:
                    characterMap[p] = wordList[i]
            else:
                if characterMap[p] != wordList[i]:
                    return False
        return True