class Solution:
    def removeDuplicates(self, S: str) -> str:
        dequeue = deque()
        for char in S:
            if not dequeue or dequeue[-1] != char:
                dequeue.append(char)
            else:
                dequeue.pop()
        return ''.join(dequeue)