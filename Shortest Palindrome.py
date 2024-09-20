class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Edge case: If s is empty or already a palindrome
        if not s or s == s[::-1]:
            return s
        
        # Create the reverse of the string
        rev_s = s[::-1]
        
        # Concatenate the original string, a separator, and the reversed string
        new_s = s + '#' + rev_s
        
        # Compute the KMP table (LPS array) for new_s
        lps = [0] * len(new_s)
        
        for i in range(1, len(new_s)):
            j = lps[i - 1]
            
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            
            if new_s[i] == new_s[j]:
                j += 1
            
            lps[i] = j
        
        # The length of the longest palindromic prefix is given by lps[-1]
        # Characters after this prefix in rev_s need to be added to the front
        add_length = len(s) - lps[-1]
        return rev_s[:add_length] + s
