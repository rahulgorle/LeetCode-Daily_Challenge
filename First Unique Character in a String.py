from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)

        # Iterate through the string to find the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no unique character is found, return -1
        return -1
