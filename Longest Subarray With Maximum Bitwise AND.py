class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = float('-inf')  # Initially set to negative infinity
        longest = 0  # To store the longest subarray length
        current_length = 0  # To count the length of current subarray of max elements

        for num in nums:
            # Update the max_value and reset current_length if a new max is found
            if num > max_value:
                max_value = num
                current_length = 1
                longest = 1
            # If the current number equals max_value, increase the current subarray length
            elif num == max_value:
                current_length += 1
                longest = max(longest, current_length)
            else:
                # Reset current subarray length if the number is less than max_value
                current_length = 0
        
        return longest
