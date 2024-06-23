from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Insert current number into maxDeque and minDeque
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)
            
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)
            
            # Ensure the current window is valid
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()
            
            # Update the maximum length of valid subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length
