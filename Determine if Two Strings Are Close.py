from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Use Counter to get frequency dictionaries
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Check if the sets of characters are the same
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Check if the sorted frequency lists are the same
        return sorted(freq1.values()) == sorted(freq2.values())
