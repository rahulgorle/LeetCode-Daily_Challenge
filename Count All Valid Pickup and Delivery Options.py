class Solution:
    def countOrders(self, n):
        total = 1
        for i in range(1, n + 1):
            total = (total * comb(2 * i, 2)) % (10**9 + 7)
        return total
