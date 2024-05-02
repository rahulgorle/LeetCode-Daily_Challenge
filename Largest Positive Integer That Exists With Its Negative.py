from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_k = -1
        num_set = set(nums)  # Convert nums to a set for faster lookup
        
        for num in nums:
            if -num in num_set:
                max_k = max(max_k, abs(num))
        
        return max_k if max_k != -1 else -1
