class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(startIndex, currentList, requiredTarget):
            if requiredTarget == 0:
                result.append(list(currentList))
                return
            for index in range(startIndex, len(candidates)):
                candidate = candidates[index]
                newTarget = requiredTarget - candidate
                if newTarget >= 0:
                    helper(index, currentList + [candidate], newTarget)
        result = []
        helper(0, [], target)
        return result