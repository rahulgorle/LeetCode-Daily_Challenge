class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 1D array to represent the glasses in the current row
        glasses = [0.0] * (query_row + 1)
        glasses[0] = poured

        for i in range(query_row):
            # Create a temporary array to store the updated values for the next row
            temp = [0.0] * (query_row + 1)

            for j in range(i + 1):
                # Calculate the excess champagne that overflows from the current glass
                excess_champagne = (glasses[j] - 1.0) / 2.0

                # Distribute the excess champagne to the glasses below
                if excess_champagne > 0:
                    temp[j] += excess_champagne
                    temp[j + 1] += excess_champagne

            # Update the glasses array with the values from the temporary array
            glasses = temp

        # Ensure the value is between 0 and 1 (0 <= x <= 1)
        return min(1.0, glasses[query_glass])
