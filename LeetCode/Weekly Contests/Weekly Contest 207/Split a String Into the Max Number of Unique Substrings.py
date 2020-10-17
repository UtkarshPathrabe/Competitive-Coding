class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen, result, sLength = set(), 0, len(s)
        def backtrack(start):
            nonlocal result
            if start == sLength:
                return True
            elif start > sLength:
                return False
            else:
                for end in range(start + 1, sLength + 1):
                    if s[start:end] not in seen:
                        seen.add(s[start:end])
                        temp = backtrack(end)
                        if temp:
                            result = max(result, len(seen))
                        seen.remove(s[start:end])
                return True
        backtrack(0)
        return result
        