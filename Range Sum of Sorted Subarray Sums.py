class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []

        # Step 1: Generate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        # Step 2: Sort the subarray sums
        subarray_sums.sort()

        # Step 3: Sum the elements from index `left` to `right`
        result_sum = sum(subarray_sums[left-1:right]) % MOD
        
        return result_sum
