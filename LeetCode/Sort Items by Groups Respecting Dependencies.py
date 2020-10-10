class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupSet = set(group)
        validGroupIndex = [i for i in range(max(m, n)) if i not in groupSet]
        for index, g in enumerate(group):
            if g == -1:
                group[index] = validGroupIndex[-1]
                validGroupIndex.pop()
        itemsGraph, groupGraph, itemsInDegree, groupInDegree = defaultdict(list), defaultdict(list), [0] * n, [0] * n
        for index, node in enumerate(beforeItems):
            for item in node:
                itemsGraph[item].append(index)
                itemsInDegree[index] += 1
                if group[item] != group[index]:
                    groupGraph[group[item]].append(group[index])
                    groupInDegree[group[index]] += 1
        
        def topologicalSort(graph, inDegree):
            queue = deque([node for node, degree in enumerate(inDegree) if degree == 0])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbour in graph[node]:
                    inDegree[neighbour] -= 1
                    if inDegree[neighbour] == 0:
                        queue.append(neighbour)
            return [] if len(result) != len(graph) else result
        
        itemsOrder, groupOrder = topologicalSort(itemsGraph, itemsInDegree), topologicalSort(groupGraph, groupInDegree)
        if itemsOrder == [] or groupOrder == []:
            return []
        itemsGroup = defaultdict(list)
        for item in itemsOrder:
            itemsGroup[group[item]].append(item)
        result = []
        for g in groupOrder:
            result.extend(itemsGroup[g])
        return result