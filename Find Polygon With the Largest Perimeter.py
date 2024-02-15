
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum1 = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            sum1 -= nums[i]
            if sum1 > nums[i]:
                return sum1 + nums[i]
        return -1
