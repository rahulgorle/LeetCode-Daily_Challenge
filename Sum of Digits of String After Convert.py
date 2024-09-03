class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Directly calculate the initial sum of digits from the string
        digit_sum = 0
        for char in s:
            num = ord(char) - ord('a') + 1
            while num > 0:
                digit_sum += num % 10
                num //= 10

        # Step 2: Perform the transformation `k` times
        for _ in range(k - 1):
            if digit_sum < 10:
                break
            digit_sum = sum(int(d) for d in str(digit_sum))

        return digit_sum
