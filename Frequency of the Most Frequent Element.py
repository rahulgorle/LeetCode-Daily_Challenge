from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_frequency = 0
        total_operations = 0

        for right in range(len(nums)):
            total_operations += nums[right]

            while (right - left + 1) * nums[right] > total_operations + k:
                total_operations -= nums[left]
                left += 1

            max_frequency = max(max_frequency, right - left + 1)

        return max_frequency
