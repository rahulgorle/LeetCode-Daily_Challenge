class Solution:
    def minDeletions(self, s: str) -> int:
        # Step 1: Count character frequencies using an array
        char_count = [0] * 26  # Assuming lowercase English letters only

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        # Step 2: Initialize sets and variables
        used_freqs = set()
        deletions = 0

        # Step 3 and 4: Iterate through frequencies
        for freq in char_count:
            while freq in used_freqs:
                # Decrement the frequency until it's unique
                freq -= 1
                deletions += 1
                if freq == 0:
                    break
            if freq > 0:
                used_freqs.add(freq)

        return deletions
