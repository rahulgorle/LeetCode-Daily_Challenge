class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        x0, xN = 1 << 31, -(1 << 31)
        diff = 0
        for arr in arrays:
            a0, aN = arr[0], arr[-1]
            diff = max(diff, aN - x0, xN - a0)
            x0 = min(x0, a0)
            xN = max(xN, aN)
        return diff
