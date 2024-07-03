class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If there are 4 or fewer elements, we can make all elements the same
        if len(nums) <= 4:
            return 0
        
        # Sort the array
        nums.sort()
        
        # Calculate the minimum difference after removing 3 elements
        return min(
            nums[-1] - nums[3],  # Remove the three smallest
            nums[-2] - nums[2],  # Remove the smallest and the two largest
            nums[-3] - nums[1],  # Remove the two smallest and the largest
            nums[-4] - nums[0]   # Remove the three largest
        )
