class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        newStart, newEnd = newInterval

        res = []

        while i < n and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1
        res.append([newStart, newEnd])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res 
        