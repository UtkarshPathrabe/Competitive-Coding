class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue, stack, mismatch = deque(students), deque(sandwiches), 0
        while mismatch < len(queue):
            if queue[0] == stack[0]:
                mismatch = 0
                stack.popleft()
            else:
                mismatch += 1
                queue.append(queue[0])
            queue.popleft()
        return len(queue)