class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Step 1: Calculate the base satisfaction without using the secret technique
        base_satisfaction = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        
        # Step 2: Use a sliding window to find the best interval to apply the secret technique
        max_additional_satisfaction = 0
        current_additional_satisfaction = 0
        
        # Initial window
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
        max_additional_satisfaction = current_additional_satisfaction
        
        # Sliding the window across the rest of the array
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                current_additional_satisfaction -= customers[i - minutes]
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
            max_additional_satisfaction = max(max_additional_satisfaction, current_additional_satisfaction)
        
        # Step 3: The result is the base satisfaction plus the best additional satisfaction found
        return base_satisfaction + max_additional_satisfaction
