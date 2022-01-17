class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        tMap = Counter(t)
        required = len(tMap)
        filteredS = []
        for i, char in enumerate(s):
            if char in tMap:
                filteredS.append((i, char))
        l, r = 0, 0
        formed = 0
        windowMap = defaultdict(int)
        result = (float('inf'), None, None)
        while r < len(filteredS):
            char = filteredS[r][1]
            windowMap[char] += 1
            if windowMap[char] == tMap[char]:
                formed += 1
            while l <= r and formed == required:
                c = filteredS[l][1]
                start, end = filteredS[l][0], filteredS[r][0]
                if end - start + 1 < result[0]:
                    result = (end - start + 1, start, end)
                windowMap[c] -= 1
                if windowMap[c] < tMap[c]:
                    formed -= 1
                l += 1
            r += 1
        return '' if result[0] == float('inf') else s[result[1] : result[2] + 1]