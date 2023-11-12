from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_buses = set()
        visited_stops = set()
        queue = deque([(source, 0)])

        while queue:
            current_stop, steps = queue.popleft()

            for bus in stop_to_routes[current_stop]:
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop in visited_stops:
                        continue

                    visited_stops.add(next_stop)

                    if next_stop == target:
                        return steps + 1

                    queue.append((next_stop, steps + 1))

        return -1
