import heapq

class SeatManager:

    def __init__(self, n: int):
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        if self.available_seats:
            # Get the smallest available seat and mark it as reserved
            seat = heapq.heappop(self.available_seats)
            return seat
        return -1  # No available seats

    def unreserve(self, seatNumber: int) -> None:
        # Add the unreserved seat back to the available seats
        heapq.heappush(self.available_seats, seatNumber)
