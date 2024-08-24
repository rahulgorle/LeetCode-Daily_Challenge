class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        # Candidates to consider
        candidates = set()
        
        # Edge cases for shorter and longer lengths
        candidates.add(10**(length - 1) - 1)  # 999...999 (one digit less)
        candidates.add(10**length + 1)        # 1000...0001 (one digit more)
        
        # Prefix for palindrome
        prefix = int(n[:(length + 1) // 2])
        
        for i in [-1, 0, 1]:
            # Create a new palindrome by changing the prefix
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[-2::-1]
            candidates.add(int(candidate))
        
        # Remove the number itself from candidates
        candidates.discard(num)
        
        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(x - num), x))
        
        return str(closest)
