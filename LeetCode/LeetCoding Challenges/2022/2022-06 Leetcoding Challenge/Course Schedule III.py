class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda a : a[1])
        queue, time = [], 0
        for c in courses:
            if time + c[0] <= c[1]:
                heapq.heappush(queue, -1 * c[0])
                time += c[0]
            elif len(queue) != 0 and (queue[0] * -1) > c[0]:
                time += c[0] + heapq.heappop(queue)
                heapq.heappush(queue, -1 * c[0])
        return len(queue)