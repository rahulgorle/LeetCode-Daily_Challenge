class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l1 = [abs(i) for i in nums]
        l1.sort()
        return [i**2 for i in l1]
