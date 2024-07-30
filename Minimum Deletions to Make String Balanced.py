class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0  # Number of 'a' encountered
        min_deletions = 0  # Minimum deletions needed
        
        for char in s:
            if char == 'a':
                # We might need to delete a 'b' encountered earlier to keep balance
                min_deletions = min(min_deletions + 1, a_count)
            else:  # char == 'b'
                a_count += 1
        
        return min_deletions
