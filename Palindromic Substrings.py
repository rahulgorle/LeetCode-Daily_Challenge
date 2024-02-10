class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        for i in range(n):
            # Palindromes with odd length
            expandAroundCenter(i, i)
            # Palindromes with even length
            expandAroundCenter(i, i + 1)
        
        return count
