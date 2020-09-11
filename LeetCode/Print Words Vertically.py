class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        maxWordLen = max([len(word) for word in words])
        i, result = 0, []
        while i < maxWordLen:
            tempWord = []
            for word in words:
                try:
                    tempWord.append(word[i])
                except IndexError as e:
                    tempWord.append(' ')
            result.append(''.join(tempWord).rstrip())
            i += 1
        return result