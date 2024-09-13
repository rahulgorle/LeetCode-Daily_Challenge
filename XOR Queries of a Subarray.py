class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Create the prefix XOR array
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        # Step 2: Process each query using the prefix XOR array
        result = []
        for l, r in queries:
            result.append(prefix[r + 1] ^ prefix[l])
        
        return result
