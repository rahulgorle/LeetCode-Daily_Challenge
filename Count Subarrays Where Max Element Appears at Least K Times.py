class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def count_subarrays_with_at_least_k(num):
            count = 0
            result = 0
            left = 0

            for right in range(len(nums)):
                if nums[right] == num:
                    count += 1

                while count >= k:
                    result += len(nums) - right
                    if nums[left] == num:
                        count -= 1
                    left += 1

            return result

        max_num = max(nums)
        return count_subarrays_with_at_least_k(max_num)
