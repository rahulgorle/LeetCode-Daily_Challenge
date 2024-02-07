from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        counts = Counter(s)
        
        # Sort the characters based on their frequencies
        sorted_chars = sorted(counts, key=lambda x: (-counts[x], x))
        
        # Build the sorted string
        sorted_string = ''.join(char * counts[char] for char in sorted_chars)
        
        return sorted_string
