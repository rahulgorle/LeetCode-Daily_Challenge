class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(num):
            # Count the number of 1's in the binary representation of num
            count = 0
            while num:
                count += 1
                num &= (num - 1)  # Remove the rightmost set bit
            return count

        # Sort the array in-place
        arr.sort(key=lambda x: (bit_count(x), x))
        return arr
