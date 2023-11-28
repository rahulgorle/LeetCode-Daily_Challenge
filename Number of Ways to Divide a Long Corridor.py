class Solution:
    def numberOfWays(self, corridor):
        seats_count = 0
        plants_count = 0
        dividers = 1
        mod = 1000000007
        
        for char in corridor:
            if char == 'S':
                seats_count += 1
            if seats_count == 2 and char == 'P':
                plants_count += 1
            if seats_count == 3:
                dividers *= (plants_count + 1)
                dividers %= mod
                seats_count = 1
                plants_count = 0
        
        if seats_count < 2:
            return 0
        return dividers
