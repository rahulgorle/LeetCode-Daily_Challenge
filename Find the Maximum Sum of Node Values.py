from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        totalSum = 0
        positiveMin = float("inf")
        negativeMax = float("-inf")
        count = 0

        for value in nums:
            xorValue = value ^ k
            totalSum += value
            change = xorValue - value

            if change > 0:
                positiveMin = min(positiveMin, change)
                totalSum += change
                count += 1
            else:
                negativeMax = max(negativeMax, change)

        if count % 2 == 0:
            return totalSum
        return max(totalSum - positiveMin, totalSum + negativeMax)
