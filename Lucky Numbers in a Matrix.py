from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []
        
        for i in range(len(matrix)):
            # Find the minimum value in the current row and its column index
            min_val = min(matrix[i])
            min_col = matrix[i].index(min_val)
            
            # Check if this minimum value is the maximum in its column
            is_lucky = True
            for row in matrix:
                if row[min_col] > min_val:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_val)
        
        return lucky_numbers
