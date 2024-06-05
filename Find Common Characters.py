from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the minimum frequency list for each letter (a-z) to a high value
        min_freq = [float('inf')] * 26
        
        # Update the minimum frequency list based on each word's frequencies
        for word in words:
            # Count frequency of each character in the current word
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            
            # Update the minimum frequency for each character
            for i in range(26):
                min_freq[i] = min(min_freq[i], char_count[i])
        
        # Build the result list based on the minimum frequency of each character
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * min_freq[i])
        
        return result
