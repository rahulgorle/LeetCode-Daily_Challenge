class Solution:
    def insert(self, intervals, newInterval):
        merged = []
        i = 0
        
        # Add all intervals that come before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # Merge intervals that overlap with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        merged.append(newInterval)
        
        # Add all intervals that come after newInterval
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
