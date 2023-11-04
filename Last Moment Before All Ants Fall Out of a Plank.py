class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_time_left = max(left, default=0)
        max_time_right = max((n - x for x in right), default=0)

        return max(max_time_left, max_time_right)
