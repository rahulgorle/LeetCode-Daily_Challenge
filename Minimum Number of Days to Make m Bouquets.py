class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Check if it's impossible to form m bouquets
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets == m:
                            return True
                else:
                    flowers = 0
            
            return False
        
        # Binary search on the days
        low, high = 1, max(bloomDay)
        
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
