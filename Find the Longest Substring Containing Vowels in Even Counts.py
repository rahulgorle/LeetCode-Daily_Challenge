class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Vowel to bitmask mapping
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Dictionary to store the first occurrence of each bitmask
        mask_to_index = {0: -1}  # We start with mask 0 at index -1 to handle full string cases.
        
        # Current bitmask
        current_mask = 0
        max_length = 0
        
        # Traverse through the string
        for i, char in enumerate(s):
            if char in vowel_to_bit:
                # Toggle the bit corresponding to the vowel
                current_mask ^= (1 << vowel_to_bit[char])
            
            # Check if this bitmask has been seen before
            if current_mask in mask_to_index:
                # Calculate the length of the valid substring
                max_length = max(max_length, i - mask_to_index[current_mask])
            else:
                # Store the first occurrence of this bitmask
                mask_to_index[current_mask] = i
        
        return max_length
