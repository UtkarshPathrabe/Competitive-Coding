class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        for i in range(20):
            for j in range(20):
                val = x ** i + y ** j
                if val <= bound:
                    result.add(val)
        return list(result)