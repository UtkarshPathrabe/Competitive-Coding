class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        graph, result = defaultdict(list), []
        timeInSeconds = lambda x : int(x[0:2]) * 3600 + int(x[3:]) * 60
        for name, time in zip(keyName, keyTime):
            graph[name].append(timeInSeconds(time))
        for name in sorted(graph.keys()):
            start, count, times = 0, 0, sorted(graph[name])
            for end in range(len(times)):
                count += 1
                while abs(times[end] - times[start]) > 3600 and end >= start:
                    count -= 1
                    start += 1
                if count == 3:
                    result.append(name)
                    break
        return result