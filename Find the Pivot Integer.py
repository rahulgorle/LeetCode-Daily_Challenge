class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2  # Sum of all elements from 1 to n

        left_sum = 0
        for x in range(1, n + 1):
            left_sum += x
            right_sum = total_sum - left_sum + x  # Adjusting for inclusive sum
            if left_sum == right_sum:
                return x
        return -1
