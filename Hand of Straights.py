from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Step 1: Use a Counter to count each card
        count = Counter(hand)
        
        # Step 2: Iterate through the sorted unique cards
        for card in sorted(count):
            if count[card] > 0:
                num_needed = count[card]
                # Try to form a group starting from this card
                for i in range(groupSize):
                    if count[card + i] < num_needed:
                        return False
                    count[card + i] -= num_needed
        
        return True
