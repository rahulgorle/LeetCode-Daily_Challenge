class Solution:
    def longestPalindrome(self, s: str) -> str:
        def preprocess(s):
            n = len(s)
            if n == 0:
                return "^$"
            result = "^"
            for i in range(n):
                result += "#" + s[i]
            result += "#$"
            return result

        T = preprocess(s)
        n = len(T)
        P = [0] * n
        C, R = 0, 0

        for i in range(1, n - 1):
            mirror = 2 * C - i

            if i < R:
                P[i] = min(R - i, P[mirror])

            # Attempt to expand palindrome centered at i
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while T[a] == T[b]:
                P[i] += 1
                a += 1
                b -= 1

            # If palindrome centered at i expands past R,
            # adjust center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len, center_index = max((n, i) for i, n in enumerate(P))

        start = (center_index - max_len) // 2
        return s[start:start + max_len]
