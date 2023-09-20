class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target_sum = total_sum - x

        if target_sum < 0:
            return -1

        left, current_sum, min_ops = 0, 0, float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target_sum:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                min_ops = min(min_ops, len(nums) - (right - left + 1))

        return min_ops if min_ops != float('inf') else -1
