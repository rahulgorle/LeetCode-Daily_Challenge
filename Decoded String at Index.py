class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0
        
        # Calculate the length of the decoded string without actually decoding it
        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1
        
        # Start from the end of the string and work backwards
        for char in reversed(s):
            k %= decoded_length  # Ensure k is within the length of the decoded string
            
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                decoded_length //= int(char)
            else:
                decoded_length -= 1
