class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen, haystackLen = len(needle), len(haystack)
        if needleLen == 0:
            return 0
        if needleLen > haystackLen:
            return -1
        base, modulus = 26, 2 ** 32
        
        def charToInt(c):
            return ord(c) - ord('a')
        
        haystackHash = needleHash = 0
        for i in range(needleLen):
            needleHash = (needleHash * base + charToInt(needle[i])) % modulus
            haystackHash = (haystackHash * base + charToInt(haystack[i])) % modulus
        if needleHash == haystackHash:
            return 0
        baseL = pow(base, needleLen, modulus)
        for i in range(1, haystackLen - needleLen + 1):
            haystackHash = ((haystackHash * base) - (charToInt(haystack[i - 1]) * baseL) + charToInt(haystack[i + needleLen - 1])) % modulus
            if needleHash == haystackHash:
                return i
        return -1