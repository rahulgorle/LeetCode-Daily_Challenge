class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        piles = [nums[0]]

        for num in nums[1:]:
            if num > piles[-1]:
                piles.append(num)
            else:
                # Use binary search to find the index to update
                left, right = 0, len(piles) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if piles[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                piles[left] = num

        return len(piles)
