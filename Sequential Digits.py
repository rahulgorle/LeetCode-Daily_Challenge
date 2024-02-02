from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        max_len = len(str(high))
        
        for length in range(len(str(low)), max_len + 1):
            for start in range(10 - length):
                num_str = digits[start:start+length]
                num = int(num_str)
                if num > high:
                    return result  # No need to continue if we've exceeded the upper bound
                if low <= num <= high:
                    result.append(num)
        
        return result
