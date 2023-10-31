class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        xor = 0  # Initialize the cumulative XOR value

        for i in range(len(pref)):
            pref[i] ^= xor  # Calculate pref[i] and update it in the pref list
            xor ^= pref[i]  # Update the cumulative XOR value

        return pref
