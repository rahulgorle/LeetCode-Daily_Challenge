from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # Calculate prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # Calculate suffix sum
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        result = [0] * n

        # Calculate result array
        for i in range(n):
            if i == 0:
                result[i] = suffix_sum[1] - (n - 1) * nums[i]
            elif i == n - 1:
                result[i] = (n - 1) * nums[i] - prefix_sum[n - 2]
            else:
                result[i] = (i + 1) * nums[i] - prefix_sum[i] + suffix_sum[i + 1] - (n - i - 1) * nums[i]

        return result
