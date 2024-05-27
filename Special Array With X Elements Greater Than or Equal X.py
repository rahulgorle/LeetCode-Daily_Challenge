class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_val = 1000
        freq = [0] * (max_val + 1)
        
        # Count the frequency of each number
        for num in nums:
            freq[num] += 1
        
        # Traverse from the largest possible value down to 0
        count = 0
        for x in range(max_val, -1, -1):
            count += freq[x]
            if count == x:
                return x
        
        return -1
