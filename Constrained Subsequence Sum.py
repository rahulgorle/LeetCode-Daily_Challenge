import collections

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        max_sum = float('-inf')
        dq = collections.deque()

        for i in range(n):
            # Pop elements from the back of the deque if they are out of range (i - dq[0] > k)
            while dq and i - dq[0] > k:
                dq.popleft()

            # The current element is included in the sum, or not, choose the max
            dp[i] = max(nums[i], nums[i] + (dp[dq[0]] if dq else 0))

            # Update the maximum sum found so far
            max_sum = max(max_sum, dp[i])

            # Remove elements from the back of the deque if they are smaller than dp[i]
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()

            # Append the current index to the deque
            dq.append(i)

        return max_sum
