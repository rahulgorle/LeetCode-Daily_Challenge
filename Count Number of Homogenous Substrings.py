class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        length = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                length += 1
            else:
                total = (total + length * (length + 1) // 2) % MOD
                length = 1

        total = (total + length * (length + 1) // 2) % MOD
        return total
