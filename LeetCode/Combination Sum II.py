class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result, numberOfCandidates = set(), len(candidates)
        def backtrack(remainingSum, currentCombination, startIndex):
            nonlocal candidates, result, numberOfCandidates
            if remainingSum == 0:
                result.add(tuple(currentCombination))
                return
            elif remainingSum < 0:
                return
            else:
                for i in range(startIndex, numberOfCandidates):
                    currentCombination.append(candidates[i])
                    backtrack(remainingSum - candidates[i], currentCombination, i + 1)
                    currentCombination.pop()
        backtrack(target, [], 0)
        return result