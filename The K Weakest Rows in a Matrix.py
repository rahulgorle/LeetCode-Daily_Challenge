class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list of pairs (row_index, num_soldiers) for each row
        row_soldier_counts = [(i, sum(row)) for i, row in enumerate(mat)]
        
        # Sort the list of pairs based on the number of soldiers and row index
        row_soldier_counts.sort(key=lambda x: (x[1], x[0]))
        
        # Get the indices of the k weakest rows
        result = [row[0] for row in row_soldier_counts[:k]]
        
        return result
