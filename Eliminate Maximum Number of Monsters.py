class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrival_time = [math.ceil(dist[i] / speed[i]) for i in range(n)]
        arrival_time.sort()  # Sort the monsters by their arrival time

        for i in range(n):
            if i >= arrival_time[i]:
                return i  # You cannot eliminate the i-th monster
        return n  # You can eliminate all the monsters before they reach the city
