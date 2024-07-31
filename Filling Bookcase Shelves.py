from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No books, no height

        for i in range(1, n + 1):
            width = 0
            height = 0
            j = i
            # Try to place books[i-1] to books[j-1] on the same shelf
            while j > 0:
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1

        return dp[n]
