class Solution:
    def countOrders(self, n: int) -> int:
        @functools.cache
        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                #We have completed all orders
                return 1
            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                # We can't pick or deliver more than N items
                # Number of deliveries can't exceed number of pickups 
                # as we can only deliver after a pickup.
                return 0
            # Count all choices of picking up an order.
            ans = unpicked * totalWays(unpicked - 1, undelivered)
            ans %= MOD
            # Count all choices of delivering a picked order.
            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)
            ans %= MOD
            return ans
        MOD = 1_000_000_007
        return totalWays(n, n)