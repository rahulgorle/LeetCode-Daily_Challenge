class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False  # Early exit if you can't provide change
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:  # Prefer giving one $10 and one $5
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise, give three $5 bills
                    five -= 3
                else:
                    return False  # Early exit if you can't provide change
        
        return True  # If all customers received the correct change
