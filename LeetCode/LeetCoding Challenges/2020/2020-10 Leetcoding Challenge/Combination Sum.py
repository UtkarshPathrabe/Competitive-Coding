class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, numberOfCandidates = [], len(candidates)
        def backtrack(remainingSum, currentCombination, startIndex):
            if remainingSum == 0:
                result.append(list(currentCombination))
                return
            elif remainingSum < 0:
                return
            else:
                for i in range(startIndex, numberOfCandidates):
                    currentCombination.append(candidates[i])
                    backtrack(remainingSum - candidates[i], currentCombination, i)
                    currentCombination.pop()
        backtrack(target, [], 0)
        return result