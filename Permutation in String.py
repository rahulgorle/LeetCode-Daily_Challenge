class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s2 to contain a permutation of s1
        if len1 > len2:
            return False
        
        # Initialize two frequency arrays for s1 and the current window in s2
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Count frequencies of characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Sliding window over s2
        for i in range(len2):
            # Add the current character to the window count
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # If the window exceeds the length of s1, remove the leftmost character
            if i >= len1:
                window_count[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Compare the frequency arrays
            if window_count == s1_count:
                return True
        
        return False
