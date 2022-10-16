class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        colorMap = defaultdict(int)
        for start, end, color in segments:
            colorMap[start] += color
            colorMap[end] -= color
        result, prev, color = [], None, 0
        for now in sorted(colorMap):
            if color:
                result.append((prev, now, color))
            color += colorMap[now]
            prev = now
        return result