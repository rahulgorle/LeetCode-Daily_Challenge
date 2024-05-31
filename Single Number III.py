class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in the xor_all (i.e., a bit where the two numbers differ)
        # This finds the rightmost set bit
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition the numbers into two groups and XOR each group
        unique1 = 0
        unique2 = 0
        for num in nums:
            if num & diff_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        # The two unique numbers
        return [unique1, unique2]
