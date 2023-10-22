class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        stack = []

        # Find the left boundaries of good subarrays
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)

        stack = []

        # Find the right boundaries of good subarrays
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if not stack:
                right[i] = n - 1
            else:
                right[i] = stack[-1] - 1
            stack.append(i)

        max_score = 0

        # Calculate the score for each good subarray and update max_score
        for i in range(n):
            if left[i] <= k <= right[i]:
                max_score = max(max_score, nums[i] * (right[i] - left[i] + 1))

        return max_score
