class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        locationsLen, modulus = len(locations), 10 ** 9 + 7
        dp = [[-1] * (fuel + 1) for _ in range(locationsLen)]
        
        def dfs(city, fuel):
            if fuel < 0:
                return 0
            if dp[city][fuel] != -1:
                return dp[city][fuel]
            result = 0
            if city == finish:
                result = 1
            for i in range(locationsLen):
                if i != city and fuel - abs(locations[i] - locations[city]) >= 0:
                    result += dfs(i, fuel - abs(locations[i] - locations[city])) % modulus
            dp[city][fuel] = result
            return result
            
        return dfs(start, fuel) % modulus