from collections import defaultdict
from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Create a dictionary to store the frequency of each element
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        # Step 2: Sort the array in descending order
        sorted_nums = sorted(nums, reverse=True)

        # Step 3: Initialize an empty list for the resulting 2D array
        result = [[]]

        # Step 4: Iterate through the sorted array and add elements to rows
        for num in sorted_nums:
            added = False
            for row in result:
                if num not in row:
                    row.append(num)
                    added = True
                    break

            if not added:
                result.append([num])

        # Step 5: Return the resulting 2D array
        return result
