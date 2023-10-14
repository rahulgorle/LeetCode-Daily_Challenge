class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost)
        INF = 10 ** 20

        dp = [[-1] * (N + 1) for _ in range(N + 1)]

        def find_min_cost(painting_time, wall_index):
            if painting_time >= N:
                return 0
            if wall_index == N:
                return INF

            if dp[painting_time][wall_index] != -1:
                return dp[painting_time][wall_index]

            use_paid_painter = find_min_cost(painting_time + time[wall_index] + 1, wall_index + 1) + cost[wall_index]
            use_free_painter = find_min_cost(painting_time, wall_index + 1)

            dp[painting_time][wall_index] = min(use_paid_painter, use_free_painter)
            return dp[painting_time][wall_index]

        best_cost = find_min_cost(0, 0)
        return best_cost
