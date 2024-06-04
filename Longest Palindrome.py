class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create an array to count occurrences of each character
        count = [0] * 128  # ASCII size covers all possible characters in the input

        # Count each character in the string
        for char in s:
            count[ord(char)] += 1

        length_of_palindrome = 0
        odd_count_exists = False
        
        # Calculate the maximum length of the palindrome
        for cnt in count:
            if cnt % 2 == 0:
                length_of_palindrome += cnt
            else:
                length_of_palindrome += cnt - 1
                odd_count_exists = True
        
        # Add one if there is any odd count to place one character in the center
        if odd_count_exists:
            length_of_palindrome += 1
        
        return length_of_palindrome
