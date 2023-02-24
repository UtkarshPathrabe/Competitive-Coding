class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string2, index = ''.join(word2), 0
        string2Len = len(string2)
        for s in word1:
            for c in s:
                if index >= string2Len or c != string2[index]:
                    return False
                index += 1
        return index == string2Len