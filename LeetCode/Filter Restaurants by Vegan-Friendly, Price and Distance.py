class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filteredRestaurants = []
        for restaurant in restaurants:
            if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                if veganFriendly:
                    if restaurant[2] == veganFriendly:
                        filteredRestaurants.append((restaurant[0], restaurant[1]))
                else:
                    filteredRestaurants.append((restaurant[0], restaurant[1]))
        return [i[0] for i in sorted(filteredRestaurants, key = lambda x: (x[1], x[0]), reverse = True)]