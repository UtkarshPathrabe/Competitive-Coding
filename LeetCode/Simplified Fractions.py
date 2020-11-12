class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if math.gcd(numerator, denominator) == 1:
                    result.append("{}/{}".format(numerator, denominator))
        return result