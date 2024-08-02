class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        if total_ones == 0:
            return 0  # No 1's to group, no swaps needed.
        
        # Create an extended array
        extended_nums = nums + nums
        n = len(nums)
        
        # Initial window of size total_ones
        current_ones = sum(extended_nums[:total_ones])
        max_ones_in_window = current_ones
        
        # Slide the window across the extended array
        for i in range(1, n):
            current_ones += extended_nums[i + total_ones - 1] - extended_nums[i - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        return total_ones - max_ones_in_window
