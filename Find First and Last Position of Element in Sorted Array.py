class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, isLeft):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid
                    if isLeft:
                        right = mid - 1  # Search for the leftmost occurrence
                    else:
                        left = mid + 1   # Search for the rightmost occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        leftmost = binarySearch(nums, target, isLeft=True)
        rightmost = binarySearch(nums, target, isLeft=False)
        
        return [leftmost, rightmost]
