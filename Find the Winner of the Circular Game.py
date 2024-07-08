class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # Base case: only one person, so the winner is at index 0 (0-based indexing)
        
        # Iteratively apply the Josephus formula
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        # Convert 0-based index to 1-based index
        return winner + 1
