class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        sum_counts = [0] * (len(nums) + 1)
        sum_counts[0] = 1
        
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - goal >= 0:
                count += sum_counts[current_sum - goal]
            sum_counts[current_sum] += 1
        
        return count
