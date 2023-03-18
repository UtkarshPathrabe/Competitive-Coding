class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stampLen, targetLen = len(stamp), len(target)
        queue, done, result, A = deque(), [False] * targetLen, [], []
        for i in range(targetLen - stampLen + 1):
            # For each window [i, i + stampLen), A[i] will contain info on what needs to change before we can reverse stamp at i
            made, todo = set(), set()
            for j, char in enumerate(stamp):
                if target[i + j] == char:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))
            # If we can reverse stamp at i immediately, enqueue letters from this window
            if not todo:
                result.append(i)
                for j in range(i, i + stampLen):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True
        # For each enqueued letter
        while queue:
            i = queue.popleft()
            # For each window that is potentially affected, j: start of window
            for j in range(max(0, i - stampLen + 1), min(targetLen - stampLen, i) + 1):
                if i in A[j][1]: # This window is affected
                    A[j][1].discard(i) # Remove it from todo list of this window
                    if not A[j][1]: # Todo list of this window is empty
                        result.append(j)
                        for k in A[j][0]: # For each letter to potentially enqueue
                            if not done[k]:
                                queue.append(k)
                                done[k] = True
        return result[::-1] if all(done) else []