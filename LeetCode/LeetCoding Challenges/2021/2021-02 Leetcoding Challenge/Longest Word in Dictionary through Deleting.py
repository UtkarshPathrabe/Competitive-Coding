class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubsequence(x, y):
            j = 0
            for char in y:
                if j < len(x) and x[j] == char:
                    j += 1
            return j == len(x)
        result = ''
        for string in d:
            if isSubsequence(string, s):
                if len(string) > len(result) or (len(string) == len(result) and string < result):
                    result = string
        return result