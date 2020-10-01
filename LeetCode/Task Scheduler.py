class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFrequency = [0] * 26
        for task in tasks:
            taskFrequency[ord(task) - ord('A')] += 1
        taskFrequency = [i for i in taskFrequency if i > 0]
        taskFrequency.sort()
        maxFrequency = taskFrequency.pop()
        idleTime = (maxFrequency - 1) * n
        while taskFrequency and idleTime > 0:
            idleTime -= min(maxFrequency - 1, taskFrequency.pop())
        idleTime = max(0, idleTime)
        return len(tasks) + idleTime