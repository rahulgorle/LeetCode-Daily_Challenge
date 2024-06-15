import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of projects with (capital, profit)
        projects = sorted(zip(capital, profits))
        
        # Min-heap for project capitals (will be managed by their capital)
        min_capital_heap = []
        
        # Max-heap for project profits (using negative values to simulate max-heap with heapq)
        max_profit_heap = []
        
        # Index to iterate through the sorted projects
        i = 0
        n = len(projects)
        
        # Iterate up to k times to select at most k projects
        for _ in range(k):
            # Push all projects that can be afforded into the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_profit_heap, -projects[i][1])
                i += 1
            
            # If there are no projects in the max-heap, break the loop
            if not max_profit_heap:
                break
            
            # Take the project with the maximum profit
            w += -heapq.heappop(max_profit_heap)
        
        return w
