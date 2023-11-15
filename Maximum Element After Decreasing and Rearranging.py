from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()  # Sorting for safety to handle duplicates
        max_val = 1

        for i in range(1, n):
            if arr[i] > max_val + 1:
                arr[i] = max_val + 1
            max_val = arr[i]

        return max_val
