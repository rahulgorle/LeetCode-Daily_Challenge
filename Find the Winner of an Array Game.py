from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                win_count = 1
            else:
                win_count += 1

            if win_count == k:
                return current_winner

        # After going through the array once, we know that the current winner
        # is the maximum element in the array, and it will win all subsequent rounds.
        return current_winner
