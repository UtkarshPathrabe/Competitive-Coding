class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x: (x[0], -x[1]))
        if clips[0][0] > 0:
            return -1
        heap, index, count = [(-clips[0][1], clips[0][0]),], 1, 0
        while heap:
            end, start = heapq.heappop(heap)
            end *= -1
            count += 1
            if end >= time:
                return count
            for s, e in clips[index:]:
                if start <= s <= end:
                    heapq.heappush(heap, (-e, s))
                    index += 1
                else:
                    break
        return -1