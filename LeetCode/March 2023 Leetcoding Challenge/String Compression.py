class Solution:
    def compress(self, chars: List[str]) -> int:
        i, res = 0, 0
        while i < len(chars):
            groupLength = 1
            while i + groupLength < len(chars) and chars[i + groupLength] == chars[i]:
                groupLength += 1
            chars[res] = chars[i]
            res += 1
            if groupLength > 1:
                strRepr = str(groupLength)
                chars[res:res + len(strRepr)] = list(strRepr)
                res += len(strRepr)
            i += groupLength
        return res