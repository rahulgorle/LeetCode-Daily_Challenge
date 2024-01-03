class Solution:
    def numberOfBeams(self, bank):
        ans, temp = 0, 0
        for s in bank:
            n = s.count('1')
            if n > 0:
                ans += temp * n
                temp = n
        return ans
