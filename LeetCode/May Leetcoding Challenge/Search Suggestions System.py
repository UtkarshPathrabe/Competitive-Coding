class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        start, end, result, i = 0, len(products) - 1, [[] for _ in range(len(searchWord))], 0
        while i < len(searchWord) and start <= end:
            while start <= end and (len(products[start]) <= i or products[start][i] != searchWord[i]):
                start += 1
            while start <= end and (len(products[end]) <= i or products[end][i] != searchWord[i]):
                end -= 1
            for k in range(start, min(start + 3, end + 1)):
                result[i].append(products[k])
            i += 1
        return result