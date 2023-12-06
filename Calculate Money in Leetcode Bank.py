class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        monday_start = 1
        
        for day in range(1, n + 1):
            total_money += monday_start + (day - 1) % 7
            if day % 7 == 0:
                monday_start += 1
        
        return total_money
