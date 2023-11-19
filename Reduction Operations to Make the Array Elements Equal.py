from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each unique element
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Sort the unique elements in descending order
        unique_elements = sorted(freq_map.keys(), reverse=True)

        # Step 3: Iterate through the sorted unique elements and accumulate the sum
        operations = 0
        current_sum = 0
        for i in range(1, len(unique_elements)):
            current_sum += freq_map[unique_elements[i - 1]]
            operations += current_sum

        return operations
