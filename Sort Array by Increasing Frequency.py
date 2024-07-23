from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        freq = Counter(nums)
        
        # Sort the array in-place based on the frequency, and by value descending if frequencies are the same
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums
