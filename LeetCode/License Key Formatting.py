class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        stringContentsReversed = S.replace('-', '').upper()[::-1]
        return '-'.join(stringContentsReversed[i:i+K] for i in range(0, len(stringContentsReversed), K))[::-1]