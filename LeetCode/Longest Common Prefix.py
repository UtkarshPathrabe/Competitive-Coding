class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        def getCommonPrefix(s1, s2):
            result = []
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    result.append(s1[i])
                else:
                    break
            return ''.join(result)
        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            commonPrefix = getCommonPrefix(commonPrefix, strs[i])
        return commonPrefix