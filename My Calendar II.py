class MyCalendarTwo:

    def __init__(self):
        # List to store the ranges of single bookings
        self.bookings = []
        # List to store the ranges of double bookings
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking causes a triple booking by overlapping with any "double booking"
        for os, oe in self.overlaps:
            if start < oe and end > os:  # If there's an overlap with a double booking, return False
                return False
        
        # If the new booking only overlaps with single bookings, add those overlaps to "double bookings"
        for bs, be in self.bookings:
            if start < be and end > bs:  # Calculate the overlap between new booking and existing booking
                overlap_start = max(start, bs)
                overlap_end = min(end, be)
                self.overlaps.append((overlap_start, overlap_end))  # Store the overlap in double bookings
        
        # Add the new booking to the list of single bookings
        self.bookings.append((start, end))
        return True
