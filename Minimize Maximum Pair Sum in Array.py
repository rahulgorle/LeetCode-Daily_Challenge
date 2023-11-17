from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        nums.sort()

        # Step 2: Pair up the elements and calculate the sum
        n = len(nums)
        min_max_pair_sum = float('-inf')
        left, right = 0, n - 1

        while left < right:
            pair_sum = nums[left] + nums[right]
            min_max_pair_sum = max(min_max_pair_sum, pair_sum)
            left += 1
            right -= 1

        # Step 3: Return the minimized maximum pair sum
        return min_max_pair_sum
