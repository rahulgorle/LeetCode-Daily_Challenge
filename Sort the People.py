from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Sort based on heights in descending order using indices to avoid additional memory overhead
        sorted_indices = sorted(range(len(heights)), key=lambda i: heights[i], reverse=True)
        
        # Use the sorted indices to rearrange the names
        return [names[i] for i in sorted_indices]
