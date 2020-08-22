class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        for i, t1 in enumerate(transactions):
            name, time, amount, city = t1.split(',')
            if int(amount) > 1000:
                result.append(t1)
                continue
            for j, t2 in enumerate(transactions):
                if i != j:
                    name1, time1, amount1, city1 = t2.split(',')
                    if name == name1 and city != city1 and abs(int(time) - int(time1)) <= 60:
                        result.append(t1)
                        break
        return result