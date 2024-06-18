class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair up difficulty and profit, then sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their abilities
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        j = 0
        n = len(jobs)
        
        for w in worker:
            # Update the maximum profit for the current worker's ability
            while j < n and jobs[j][0] <= w:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit
