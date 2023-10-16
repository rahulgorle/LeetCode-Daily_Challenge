from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev1, prev2 = 1, 1  # Initialize the first two elements of the row

        result = [1]  # Initialize the result list

        for i in range(1, rowIndex + 1):
            current = prev1 * (rowIndex - i + 1) // i  # Calculate the current element

            result.append(current)

            prev1, prev2 = current, prev1  # Update the last two elements

        return result
