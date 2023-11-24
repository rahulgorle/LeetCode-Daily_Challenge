from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Sort the piles in descending order
        sorted_piles = sorted(piles, reverse=True)
        
        result = 0
        n = len(piles) // 3
        
        # Iterate over every third pile, starting from the second pile
        for i in range(1, 2 * n, 2):
            result += sorted_piles[i]
        
        return result
