from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create a frequency array for heights
        max_height = 100
        height_freq = [0] * (max_height + 1)
        
        for height in heights:
            height_freq[height] += 1
        
        # Step 2: Compare heights with the sorted order derived from the frequency array
        mismatch_count = 0
        current_height = 0
        
        for height in heights:
            # Find the next height in the expected sorted order
            while height_freq[current_height] == 0:
                current_height += 1
            
            if height != current_height:
                mismatch_count += 1
            
            height_freq[current_height] -= 1
        
        return mismatch_count
