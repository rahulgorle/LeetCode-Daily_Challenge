class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the length of the original array matches the required elements in the 2D array
        if len(original) != m * n:
            return []
        
        # Initialize the 2D array
        result = []
        
        # Iterate over the range from 0 to m and slice the original array into chunks of size n
        for i in range(m):
            result.append(original[i * n: (i + 1) * n])
        
        return result
