class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            next_val = mountain_arr.get(mid + 1)

            if mid_val < next_val:
                left = mid + 1
            else:
                right = mid

        peak = left
        peak_val = mountain_arr.get(peak)

        if peak_val == target:
            return peak

        # Search in the left subarray (ascending order)
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        # Search in the right subarray (descending order)
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
