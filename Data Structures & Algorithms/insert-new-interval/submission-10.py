class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Sort by start
        intervals.sort(key=lambda x:x[0])
        #No common points [1,2] is overlapping with [2,3]
        newStart, newEnd = newInterval
        res = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])

            i += 1
        
        res.append([newStart, newEnd])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
        