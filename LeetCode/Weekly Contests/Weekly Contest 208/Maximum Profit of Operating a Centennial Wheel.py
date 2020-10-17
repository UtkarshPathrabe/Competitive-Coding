class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        remainingCustomers, customersServed, rotation, maxProfit, result, i = 0, 0, 0, -1, 0, 0
        while remainingCustomers > 0 or i < len(customers):
            rotation += 1
            remainingCustomers += customers[i] if i < len(customers) else 0
            if remainingCustomers < 4:
                customersServed += remainingCustomers
                remainingCustomers = 0
            else:
                customersServed += 4
                remainingCustomers -= 4
            profit = customersServed * boardingCost - rotation * runningCost
            if maxProfit < profit:
                maxProfit = profit
                result = rotation
            i += 1
        return -1 if maxProfit <= 0 else result 