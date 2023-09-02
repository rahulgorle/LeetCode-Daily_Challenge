class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Create a set for faster lookup
        dictionary_set = set(dictionary)
        
        n = len(s)
        
        # Initialize a dp list to store the minimum extra characters at each position
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        
        return dp[n]
