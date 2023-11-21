class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        # Function to reverse an integer
        def reverse_num(x):
            return int(str(x)[::-1])

        # Calculate the differences and count occurrences
        diff_counts = {}
        nice_pairs = 0

        for num in nums:
            diff = num - reverse_num(num)
            diff_counts[diff] = diff_counts.get(diff, 0) + 1

        # Calculate the number of nice pairs
        for count in diff_counts.values():
            nice_pairs = (nice_pairs + count * (count - 1) // 2) % mod

        return nice_pairs
