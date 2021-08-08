class Solution:
    def sortSentence(self, s: str) -> str:
        words, wordMap, result = s.split(' '), defaultdict(str), []
        for word in words:
            wordMap[word[-1]] = word[:-1]
        for index in sorted(wordMap.keys()):
            result.append(wordMap[index])
        return ' '.join(result)