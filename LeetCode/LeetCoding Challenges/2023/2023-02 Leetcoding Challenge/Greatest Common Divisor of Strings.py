class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def gcd(i, j):
            while j:
                i, j = j, i % j
            return i
        finalLength = gcd(len1, len2)
        result = str1[:finalLength]
        if result * (len1 // finalLength) == str1 and result * (len2 // finalLength) == str2:
            return result
        else:
            return ''