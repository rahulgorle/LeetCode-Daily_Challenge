from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        # Sort the elements based on their frequencies
        sorted_counts = sorted(counter.values())
        unique_ints = len(sorted_counts)
        
        for count in sorted_counts:
            if k >= count:
                k -= count
                unique_ints -= 1
            else:
                break
                
        return unique_ints
