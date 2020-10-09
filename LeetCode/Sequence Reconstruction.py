class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not org or not seqs:
            return False
        graph, nodeInDegree, seqItems = defaultdict(set), defaultdict(int), set()
        for num in org:
            nodeInDegree[num] == 0
        for seq in seqs:
            for index, num in enumerate(seq):
                seqItems.add(num)
                if index > 0 and num not in graph[seq[index - 1]]:
                    graph[seq[index - 1]].add(num)
                    nodeInDegree[num] += 1
        if Counter(org) != Counter(seqItems):
            return False
        zeroInDegreeNodesQueue = deque([])
        for node, inDegree in nodeInDegree.items():
            if inDegree == 0:
                zeroInDegreeNodesQueue.append(node)
        topologicalSort = []
        while zeroInDegreeNodesQueue:
            if len(zeroInDegreeNodesQueue) != 1:
                return False
            node = zeroInDegreeNodesQueue.popleft()
            topologicalSort.append(node)
            for neighbour in graph[node]:
                nodeInDegree[neighbour] -= 1
                if nodeInDegree[neighbour] == 0:
                    zeroInDegreeNodesQueue.append(neighbour)
        return org == topologicalSort