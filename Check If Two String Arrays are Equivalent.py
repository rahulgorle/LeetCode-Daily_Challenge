from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j, x, y = 0, 0, 0, 0

        while i < len(word1) and j < len(word2):
            if word1[i][x] != word2[j][y]:
                return False

            x += 1
            y += 1

            if x == len(word1[i]):
                i += 1
                x = 0

            if y == len(word2[j]):
                j += 1
                y = 0

        return i == len(word1) and j == len(word2)
