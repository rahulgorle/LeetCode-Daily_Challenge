class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Precompute whether each substring s[i:j+1] is a palindrome
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True

        def backtrack(start: int, path: List[str]):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result
