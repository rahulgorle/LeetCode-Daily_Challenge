class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Step 1: Sort the seats and students arrays
        seats.sort()
        students.sort()
        
        # Step 2: Calculate the total number of moves
        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        
        return total_moves
