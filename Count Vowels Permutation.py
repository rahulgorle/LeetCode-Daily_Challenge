class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        # Initialize arrays to store counts for each vowel
        a_count, e_count, i_count, o_count, u_count = 1, 1, 1, 1, 1

        for _ in range(2, n + 1):
            # Update the counts for each vowel based on the rules
            new_a_count = (e_count + u_count + i_count) % MOD
            new_e_count = (a_count + i_count) % MOD
            new_i_count = (e_count + o_count) % MOD
            new_o_count = i_count
            new_u_count = (o_count + i_count) % MOD

            a_count, e_count, i_count, o_count, u_count = (
                new_a_count, new_e_count, new_i_count, new_o_count, new_u_count
            )

        # Sum up the counts for all valid strings of length n
        total_count = (a_count + e_count + i_count + o_count + u_count) % MOD

        return total_count
