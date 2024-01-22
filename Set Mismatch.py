class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        xorAll = 0
        xorArray = 0

        # Calculate the XOR of all numbers from 1 to n
        for i in range(1, n + 1):
            xorAll ^= i

        # Calculate the XOR of all elements in the array
        for num in nums:
            xorArray ^= num

        # XOR of xorAll and xorArray gives the XOR of duplicate and missing numbers
        xorResult = xorArray ^ xorAll

        # Find the rightmost set bit in the XOR result
        rightmostSetBit = xorResult & -xorResult

        xorSet = 0
        xorNotSet = 0

        # Divide the numbers into two groups based on the rightmost set bit
        for i in range(1, n + 1):
            if (i & rightmostSetBit) != 0:
                xorSet ^= i
            else:
                xorNotSet ^= i

        for num in nums:
            if (num & rightmostSetBit) != 0:
                xorSet ^= num
            else:
                xorNotSet ^= num

        # Check which one is the duplicate by iterating through the array
        for num in nums:
            if num == xorSet:
                return [xorSet, xorNotSet]

        return [xorNotSet, xorSet]
