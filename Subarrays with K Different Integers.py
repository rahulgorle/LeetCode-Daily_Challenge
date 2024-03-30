class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = collections.Counter()
            left = right = distinct = res = 0
            while right < len(nums):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                right += 1
                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left
            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)
