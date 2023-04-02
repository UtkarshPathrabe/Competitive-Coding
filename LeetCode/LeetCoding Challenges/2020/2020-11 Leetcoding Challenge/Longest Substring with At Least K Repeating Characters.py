class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        countMap = Counter(s)
        maxUnique, result = len(countMap), 0
        for currUnique in range(1, maxUnique + 1):
            countMap = defaultdict(int)
            windowStart = windowEnd = unique = countAtLeastK = 0
            while windowEnd < len(s):
                if unique <= currUnique:
                    if countMap[s[windowEnd]] == 0:
                        unique += 1
                    countMap[s[windowEnd]] += 1
                    if countMap[s[windowEnd]] == k:
                        countAtLeastK += 1
                    windowEnd += 1
                else:
                    if countMap[s[windowStart]] == k:
                        countAtLeastK -= 1
                    countMap[s[windowStart]] -= 1
                    if countMap[s[windowStart]] == 0:
                        unique -= 1
                    windowStart += 1
                if unique == currUnique and unique == countAtLeastK:
                    result = max(windowEnd - windowStart, result)
        return result