from functools import lru_cache
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        
        # DP to check if the string can be segmented
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        # If the string can't be segmented, return an empty list
        if not dp[n]:
            return []
        
        # Precompute possible endings for each start index
        possible_ends = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    possible_ends[i].append(j)
        
        # Memoization with lru_cache
        @lru_cache(None)
        def dfs(start):
            if start == n:
                return [[]]  # Return list of list to build sentences
            
            res = []
            for end in possible_ends[start]:
                for sub_sentence in dfs(end):
                    res.append([s[start:end]] + sub_sentence)
            
            return res
        
        # Get all possible sentences as list of words
        all_sentences = dfs(0)
        
        # Join words to form sentences
        return [' '.join(words) for words in all_sentences]
