class Solution:
    def minEnd(self, n: int, x: int) -> int:
        num = n - 1
        ans = ""
        while num > 0 or x > 0:
            lb = num & 1
            while x & 1:
                ans = "1" + ans
                x >>= 1
            ans = str(lb) + ans
            num >>= 1
            x >>= 1
        number = int(ans, 2) # converting the bit string to number
        return number
