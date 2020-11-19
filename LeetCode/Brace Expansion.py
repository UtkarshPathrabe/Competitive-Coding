class Solution:
    def expand(self, S: str) -> List[str]:
        tokens = [s.split(',') for s in S.replace('{', '|').replace('}', '|').split('|') if s != '']
        result = []
        def helper(index, currentString):
            if index == len(tokens):
                result.append(currentString)
                return
            for token in tokens[index]:
                helper(index + 1, currentString + token)
        helper(0, '')
        return sorted(result)