class Solution:
    def reformat(self, s: str) -> str:
        formatMap = defaultdict(list)
        for char in s:
            if char.isdigit():
                formatMap['digit'].append(char)
            else:
                formatMap['letter'].append(char)
        maxLen = max(len(formatMap['digit']), len(formatMap['letter']))
        minLen = min(len(formatMap['digit']), len(formatMap['letter']))
        if maxLen - minLen == 1:
            result = []
            if maxLen == len(formatMap['digit']):
                first = 'digit'
                second = 'letter'
            else:
                first = 'letter'
                second = 'digit'
            for i in range(minLen):
                result.append(formatMap[first][i])
                result.append(formatMap[second][i])
            result.append(formatMap[first][-1])
            return ''.join(result)
        elif maxLen == minLen:
            result = []
            for i in range(maxLen):
                result.append(formatMap['digit'][i])
                result.append(formatMap['letter'][i])
            return ''.join(result)
        return ''