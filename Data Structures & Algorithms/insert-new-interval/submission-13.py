class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start, end = newInterval
        intervals.sort()

        ptr = 0

        while ptr < len(intervals) and intervals[ptr][1] < start:
            res.append(intervals[ptr])
            ptr += 1
        
        while ptr < len(intervals) and intervals[ptr][0] <= end:
            start = min(intervals[ptr][0], start)
            end = max(intervals[ptr][1], end)
            ptr += 1
        
        res.append([start,end])

        while ptr < len(intervals):
            res.append(intervals[ptr])
            ptr += 1
        
        return res


        