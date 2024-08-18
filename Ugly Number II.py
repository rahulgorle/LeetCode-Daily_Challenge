class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1] * n  # Initialize an array to store ugly numbers
        i2 = i3 = i5 = 0  # Pointers for multiples of 2, 3, and 5
        
        next2, next3, next5 = 2, 3, 5  # Initial next multiples of 2, 3, and 5
        
        for i in range(1, n):
            # Find the next ugly number
            next_ugly = min(next2, next3, next5)
            ugly_numbers[i] = next_ugly
            
            # Move the pointer for which the current next_ugly was equal
            if next_ugly == next2:
                i2 += 1
                next2 = ugly_numbers[i2] * 2
            if next_ugly == next3:
                i3 += 1
                next3 = ugly_numbers[i3] * 3
            if next_ugly == next5:
                i5 += 1
                next5 = ugly_numbers[i5] * 5
        
        return ugly_numbers[-1]  # The nth ugly number
