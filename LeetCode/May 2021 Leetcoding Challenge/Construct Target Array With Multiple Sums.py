class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target == [1]
        totalSum = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = totalSum - largest
            # This will only occur if len(target) == 2
            if rest == 1:
                return True
            x = largest % rest
            if x == 0 or x == largest:
                return False
            heapq.heapreplace(target, -x)
            totalSum -= (largest - x)
        return True