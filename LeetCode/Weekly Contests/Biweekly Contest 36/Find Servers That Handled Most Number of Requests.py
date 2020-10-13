from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requestCounter, priorityQueue, serverList, maxRequestHandled = Counter(), [], SortedList(range(k)), 0
        for requestNumber, (requestArrivalTime, requestLoad) in enumerate(zip(arrival, load)):
            while priorityQueue and priorityQueue[0][0] <= requestArrivalTime: # Free up the server if request is completed
                serverList.add(heappop(priorityQueue)[1])
            if not serverList: # Drop the request as no server is busy
                continue
            freeServerIndex = serverList.bisect_left(requestNumber % k)
            if freeServerIndex >= len(serverList):
                freeServerIndex = 0
            serverName = serverList.pop(freeServerIndex)
            heappush(priorityQueue, (requestArrivalTime + requestLoad, serverName))
            requestCounter[serverName] += 1
            maxRequestHandled = max(maxRequestHandled, requestCounter[serverName])
        return [serverName for serverName, count in requestCounter.items() if count == maxRequestHandled]