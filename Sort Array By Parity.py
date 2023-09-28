from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            # Move left pointer to the right until it points to an odd number
            while left < right and nums[left] % 2 == 0:
                left += 1
            
            # Move right pointer to the left until it points to an even number
            while left < right and nums[right] % 2 != 0:
                right -= 1
            
            # Swap the elements at the left and right pointers
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        
        return nums
