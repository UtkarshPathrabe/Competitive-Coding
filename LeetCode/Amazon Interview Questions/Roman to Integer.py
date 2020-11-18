class Solution:
    def romanToInt(self, s: str) -> int:
        CHARACTER_MAP = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result, i, sLength = 0, 0, len(s)
        while i < sLength:
            if i + 1 < sLength and CHARACTER_MAP[s[i]] < CHARACTER_MAP[s[i + 1]]:
                result += (CHARACTER_MAP[s[i + 1]] - CHARACTER_MAP[s[i]])
                i += 2
            else:
                result += CHARACTER_MAP[s[i]]
                i += 1
        return result