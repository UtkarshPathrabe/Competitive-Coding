class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms, queue, N = set(), deque([0]), len(rooms)
        while queue:
            currentRoom = queue.popleft()
            if currentRoom not in visitedRooms:
                for neighbour in rooms[currentRoom]:
                    queue.append(neighbour)
                visitedRooms.add(currentRoom)
        return len(visitedRooms) == N