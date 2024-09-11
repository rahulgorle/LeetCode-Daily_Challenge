class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR start and goal to find bits that are different
        xor_value = start ^ goal
        # Count the number of 1s in the binary representation of xor_value
        return bin(xor_value).count('1')
