class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        sLength = len(s)
        if sLength == 0 or k == 0:
            return 0
        left, right, hashMap, maxLen = 0, 0, OrderedDict(), 1
        while right < sLength:
            character = s[right]
            if character in hashMap:
                del hashMap[character]
            hashMap[character] = right
            right += 1
            if len(hashMap) == k + 1:
                _, deleteIndex = hashMap.popitem(last = False)
                left = deleteIndex + 1
            maxLen = max(maxLen, right - left)
        return maxLen