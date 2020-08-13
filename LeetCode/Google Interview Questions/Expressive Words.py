class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def runLengthEncoding(string):
            return zip(*[(k, len(list(group))) for k, group in itertools.groupby(string)])
        
        result = 0
        if len(S) > 0:
            R, count = runLengthEncoding(S)
            for word in words:
                R1, count1 = runLengthEncoding(word)
                if R1 != R:
                    continue
                else:
                    result += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count1))
        return result