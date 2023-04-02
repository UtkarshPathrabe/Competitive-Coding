class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ideasMap = [set() for _ in range(26)]
        result = 0
        for idea in ideas:
            ideasMap[ord(idea[0]) - ord('a')].add(idea[1:])
        for i in range(25):
            for j in range(i + 1, 26):
                mutualSuffixes = len(ideasMap[i] & ideasMap[j])
                # Valid names are only from distinct suffixes in both groups.
                # Since we can swap a with b and swap b with a to create two valid names, multiple answer by 2.
                result += 2 * (len(ideasMap[i]) - mutualSuffixes) * (len(ideasMap[j]) - mutualSuffixes)
        return result