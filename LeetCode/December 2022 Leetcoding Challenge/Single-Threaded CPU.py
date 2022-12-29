class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        modifiedTasks = deque(sorted([(enqueueTime, processingTime, index) for index, (enqueueTime, processingTime) in enumerate(tasks)]))
        result, heap, time = [], [], modifiedTasks[0][0]
        while len(modifiedTasks) > 0 or len(heap) > 0:
            while modifiedTasks and time >= modifiedTasks[0][0]:
                task = modifiedTasks.popleft()
                heapq.heappush(heap, (task[1], task[2]))
            if heap:
                task = heapq.heappop(heap)
                result.append(task[1])
                time = time + task[0]
            else:
                time = modifiedTasks[0][0]
        return result