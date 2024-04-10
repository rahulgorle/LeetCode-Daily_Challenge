from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()  # Sort the deck in ascending order
        n = len(deck)
        queue = deque()  # Initialize a queue to simulate revealing order
        for i in range(n):
            queue.append(i)  # Initialize the queue with indices
            
        result = [0] * n  # Initialize the result array
        
        for card in deck:
            # Place the revealed card in its position in the result array
            result[queue.popleft()] = card
            if queue:  # If there are still unrevealed cards
                # Move the next top card to the bottom
                queue.append(queue.popleft())
        
        return result
