class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = 0
        bob_moves = 0
        n = len(colors)
        
        # Count consecutive 'A' and 'B' sequences
        a_count = 0
        b_count = 0
        
        for i in range(n):
            if colors[i] == 'A':
                a_count += 1
                if a_count >= 3:
                    alice_moves += 1
            else:
                b_count += 1
                if b_count >= 3:
                    bob_moves += 1
            
            # Reset counts when 'B' is encountered
            if colors[i] == 'B':
                a_count = 0
            # Reset counts when 'A' is encountered
            if colors[i] == 'A':
                b_count = 0
        
        # Alice wins if she has more valid moves than Bob
        return alice_moves > bob_moves
