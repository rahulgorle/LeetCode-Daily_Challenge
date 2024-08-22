class Solution:
    def findComplement(self, num: int) -> int:
        # Find the bit length of the number (i.e., how many bits are used in the binary representation)
        bit_length = num.bit_length()
        
        # Create a mask with all bits set to 1 for the length of the bit_length
        # For example, if num = 5 (binary 101), bit_length is 3, so mask will be 111 (binary)
        mask = (1 << bit_length) - 1
        
        # XOR the number with the mask to get the complement
        return num ^ mask
