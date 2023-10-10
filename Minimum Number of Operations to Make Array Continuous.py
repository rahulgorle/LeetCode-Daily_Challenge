from typing import List
import sys
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_sorted_nums = sorted(set(nums))
        min_operations = sys.maxsize

        for i, start in enumerate(unique_sorted_nums):
            end = start + n - 1
            idx = bisect_right(unique_sorted_nums, end)
            min_operations = min(min_operations, n - idx + i)

        return min_operations
