from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.SEARCH_RESULT_COUNT, self.REPORT_RESULT_COUNT = 5, 5
        self._getPrice = defaultdict(lambda : defaultdict(int))
        self._searchList = defaultdict(SortedList)
        self._rentedList = SortedList()
        for shop, movie, price in entries:
            self._getPrice[shop][movie] = price
            self._searchList[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        return [data[1] for data in self._searchList[movie][:self.SEARCH_RESULT_COUNT]]

    def rent(self, shop: int, movie: int) -> None:
        price = self._getPrice[shop][movie]
        self._searchList[movie].remove((price, shop))
        self._rentedList.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self._getPrice[shop][movie]
        self._searchList[movie].add((price, shop))
        self._rentedList.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[data[1], data[2]] for data in self._rentedList[:self.REPORT_RESULT_COUNT]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()