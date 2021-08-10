from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        sortedQueries = sorted([(size, preferredId, i) for i, (preferredId, size) in enumerate(queries)], reverse=True)
        sortedRooms = sorted([(size, roomId) for roomId, size in rooms], reverse=True)
        lenRooms, lenQueries, roomPointer, queryPointer, availableRooms, result = len(rooms), len(queries), 0, 0, SortedList(), [-1] * len(queries)
        while roomPointer <= lenRooms and queryPointer < lenQueries:
            if roomPointer < lenRooms and sortedRooms[roomPointer][0] >= sortedQueries[queryPointer][0]:
                availableRooms.add(sortedRooms[roomPointer][1])
                roomPointer += 1
            else:
                if len(availableRooms) != 0:
                    preferredId, index = sortedQueries[queryPointer][1], sortedQueries[queryPointer][2]
                    i = availableRooms.bisect(preferredId)
                    candidates = []
                    if i > 0:
                        candidates.append(availableRooms[i - 1])
                    if i < len(availableRooms):
                        candidates.append(availableRooms[i])
                    result[index] = min(candidates, key = lambda x : abs(x - preferredId))
                queryPointer += 1
        return result