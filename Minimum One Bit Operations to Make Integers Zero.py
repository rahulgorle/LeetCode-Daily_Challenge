class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def grayCodeToBinary(gray_code):
            binary = 0
            while gray_code:
                binary ^= gray_code
                gray_code >>= 1
            return binary

        def minimumOperations(gray_code):
            if gray_code == 0:
                return 0
            leading_bit = 1 << (gray_code.bit_length() - 1)
            return leading_bit + minimumOperations(gray_code ^ leading_bit)

        gray_code = grayCodeToBinary(n)
        return minimumOperations(gray_code)
