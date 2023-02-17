class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniqueStrings = []
        for substring in arr:
            substringSet = set(substring)
            if len(substringSet) == len(substring):
                uniqueStrings.append(substringSet)
        concatenatedStringSets = [set()]
        result = 0
        for substringSet in uniqueStrings:
            for concatenatedStringSet in concatenatedStringSets:
                if not substringSet & concatenatedStringSet:
                    newSubstringSet = substringSet | concatenatedStringSet
                    concatenatedStringSets.append(newSubstringSet)
                    result = max(result, len(newSubstringSet))
        return result