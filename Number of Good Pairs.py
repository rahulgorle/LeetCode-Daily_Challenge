class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0] * 101  # Initialize a count array to store occurrences (assuming values from 1 to 100)
        result = 0  # Variable to store the total number of good pairs
        
        # Count the occurrences of each number in nums
        for num in nums:
            result += count[num]  # Add the current count to the result
            count[num] += 1  # Increment the count for the current number
        
        return result
