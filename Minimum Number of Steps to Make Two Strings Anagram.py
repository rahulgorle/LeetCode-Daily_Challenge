from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(t) - Counter(s)
        return sum(max(0, c) for c in count.values())
