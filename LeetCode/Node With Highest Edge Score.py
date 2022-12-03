class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        maxEdgeScore, resultNode = -1, -1
        freqMap = defaultdict(int)
        for startNode, endNode in enumerate(edges):
            freqMap[endNode] += startNode
            if (freqMap[endNode] > maxEdgeScore) or (freqMap[endNode] == maxEdgeScore and resultNode > endNode):
                maxEdgeScore, resultNode = freqMap[endNode], endNode
        return resultNode