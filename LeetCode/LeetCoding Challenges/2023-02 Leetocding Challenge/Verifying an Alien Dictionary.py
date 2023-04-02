class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = defaultdict(int)
        for index, char in enumerate(order, start = 1):
            orderMap[char] = index
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if orderMap[word1[j]] > orderMap[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True