class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count, result = collections.Counter(str), []
        for char in order:
            result.append(char * count[char])
            count[char] = 0
        for char in count:
            result.append(char * count[char])
        return ''.join(result)