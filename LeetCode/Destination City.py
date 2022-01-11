class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        originCities, destCities = set(), set()
        for origin, dest in paths:
            originCities.add(origin)
            destCities.add(dest)
        return list(destCities - originCities)[0]