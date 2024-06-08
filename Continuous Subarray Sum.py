class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # To handle the subarray starting from index 0
        cumulative_sum = 0
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k if k != 0 else cumulative_sum
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
                
        return False
