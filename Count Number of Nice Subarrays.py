class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = {0: 1}  # To handle the case when prefix sum itself is k
        current_prefix_sum = 0
        nice_subarrays_count = 0
        
        for num in nums:
            # Increment the prefix sum if the number is odd
            if num % 2 == 1:
                current_prefix_sum += 1
            
            # Check if there is a prefix sum such that the difference is k
            if (current_prefix_sum - k) in prefix_sum_counts:
                nice_subarrays_count += prefix_sum_counts[current_prefix_sum - k]
            
            # Update the hash map with the current prefix sum
            if current_prefix_sum in prefix_sum_counts:
                prefix_sum_counts[current_prefix_sum] += 1
            else:
                prefix_sum_counts[current_prefix_sum] = 1
        
        return nice_subarrays_count
