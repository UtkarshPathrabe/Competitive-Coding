class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        result = set()
        def backtrack(substring, combinations = []):
            if len(combinations) == 4:
                if not substring:
                    current = '.'.join(combinations)
                    if current not in result:
                        result.add(current)
                return
            if not substring:
                return
            for l in range(1, 4):
                if substring[0] == '0' and l > 1:
                    return
                if int(substring[:l]) > 255:
                    return
                combinations.append(substring[:l])
                backtrack(substring[l:], combinations[:])
                combinations.pop()
        backtrack(s)
        return list(result)