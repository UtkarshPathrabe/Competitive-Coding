class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[taller - shorter] = taller
        dp = {0:0}
        for r in rods:
            # dp.copy() means we don't add r to these stands
            newDp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                # Add r to the taller stand, thus the height difference is increased to diff + r.
                newDp[diff + r] = max(newDp.get(diff + r, 0), taller + r)
                # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
                newDiff = abs(shorter + r - taller)
                newTaller = max(shorter + r, taller)
                newDp[newDiff] = max(newDp.get(newDiff, 0), newTaller)
            dp = newDp
        # return the maximum height with 0 difference
        return dp.get(0, 0)