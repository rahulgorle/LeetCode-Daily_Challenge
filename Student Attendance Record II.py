class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 3  # "P", "L", "A"
        if n == 2:
            return 8  # "PP", "PL", "LP", "LL", "PA", "AP", "LA", "AL"
        
        P = [0] * (n + 1)
        L = [0] * (n + 1)
        LL = [0] * (n + 1)
        
        # Base cases
        P[0], P[1] = 1, 1
        L[0], L[1] = 0, 1
        LL[0], LL[1] = 0, 0
        
        for i in range(2, n + 1):
            P[i] = (P[i-1] + L[i-1] + LL[i-1]) % MOD
            L[i] = P[i-1] % MOD
            LL[i] = L[i-1] % MOD
        
        total_without_A = (P[n] + L[n] + LL[n]) % MOD
        
        result = total_without_A
        
        for i in range(n):
            total_with_one_A = ((P[i] + L[i] + LL[i]) * (P[n-i-1] + L[n-i-1] + LL[n-i-1])) % MOD
            result = (result + total_with_one_A) % MOD
        
        return result
