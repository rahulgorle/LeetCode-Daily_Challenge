from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a count map for elements in arr1
        count = defaultdict(int)
        for num in arr1:
            count[num] += 1
        
        # Result list to store sorted elements
        result = []
        
        # Add elements in the order of arr2
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  # Remove the element from count
        
        # Collect remaining elements, sort them, and add to result
        remaining = sorted(count.keys())
        for num in remaining:
            result.extend([num] * count[num])
        
        return result
