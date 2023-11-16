from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])  # Length of each binary string
        seen = set(nums)  # Convert nums list to a set for faster lookup

        # Iterate through all possible binary strings of length n
        for i in range(2**n):
            binary_str = bin(i)[2:].zfill(n)  # Convert decimal to binary and pad with zeros
            if binary_str not in seen:
                return binary_str

        return ""  # Return an empty string if no unique binary string is found
