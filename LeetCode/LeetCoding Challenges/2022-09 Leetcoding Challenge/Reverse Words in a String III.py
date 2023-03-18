class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split(' ')
        for i in range(len(wordList)):
            wordList[i] = wordList[i][::-1]
        return ' '.join(wordList)