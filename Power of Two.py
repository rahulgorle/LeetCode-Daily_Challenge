class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is greater than 0 and has only one bit set
        return n > 0 and (n & (n - 1)) == 0
