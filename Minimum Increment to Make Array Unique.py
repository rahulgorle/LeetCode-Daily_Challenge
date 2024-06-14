class Solution:
    def minIncrementForUnique(self, nums):
        if not nums:
            return 0
        
        # Find the maximum value in nums to know the range
        max_num = max(nums)
        
        # Frequency array
        count = [0] * (max_num + len(nums))  # We need more space than max_num to handle increments
        
        # Fill the frequency array
        for num in nums:
            count[num] += 1
        
        moves = 0
        excess = 0
        
        # Process the count array to handle duplicates
        for i in range(len(count)):
            if count[i] > 1:
                excess += count[i] - 1
                moves -= (count[i] - 1) * i
            elif count[i] == 0 and excess > 0:
                excess -= 1
                moves += i
        
        return moves
