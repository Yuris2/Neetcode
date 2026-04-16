class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        intervals.sort()
        i = 0

        while i < len(intervals) and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        
        res.append([newStart,newEnd])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
