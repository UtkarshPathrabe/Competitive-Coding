class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomFreqMap, magazineFreqMap = Counter(ransomNote), Counter(magazine)
        for char, freq in ransomFreqMap.items():
            if char not in magazineFreqMap or freq > magazineFreqMap[char]:
                return False
        return True