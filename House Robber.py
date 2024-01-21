class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        prev_two_max = 0
        prev_max = 0

        for num in nums:
            current_max = max(prev_two_max + num, prev_max)
            prev_two_max, prev_max = prev_max, current_max

        return prev_max
