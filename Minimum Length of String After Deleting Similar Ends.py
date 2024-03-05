class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            
            # Move left pointer to the right until different character found
            while left <= right and s[left] == char:
                left += 1
            
            # Move right pointer to the left until different character found
            while right >= left and s[right] == char:
                right -= 1
        
        return right - left + 1
