class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freqMap = defaultdict(int)
        val = 0
        for char in s:
            freqMap[char] += 1
            val = freqMap[char]
        for k, v in freqMap.items():
            if v != val:
                return False
        return True