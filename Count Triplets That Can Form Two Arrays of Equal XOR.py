class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        countMap = {0: 1}  # This handles the case where prefixXor[j] == 0
        indexSumMap = {0: 0}
        prefixXor = 0
        result = 0
        
        for i, num in enumerate(arr):
            prefixXor ^= num
            
            if prefixXor in countMap:
                result += countMap[prefixXor] * i - indexSumMap[prefixXor]
            
            # Update countMap and indexSumMap
            countMap[prefixXor] = countMap.get(prefixXor, 0) + 1
            indexSumMap[prefixXor] = indexSumMap.get(prefixXor, 0) + i + 1  # Store (i+1) for ease of subtraction in result calculation
            
        return result
